#!/usr/bin/env python3
"""Validate a generated WeChat-article HTML fragment before it gets pasted.

WeChat's official-account editor silently strips tags/attributes it doesn't
like and can lose inline styles on paste unless every text node sits inside
a <span leaf="">...</span> wrapper. This turns that platform behaviour from
"something the model has to remember" into a deterministic pass/fail check.

Usage:
    validate_gzh_html.py <file.html>
    validate_gzh_html.py --stdin < file.html

Exit code 1 if any ERROR is found (would be filtered out or lose styling),
else 0.
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser

HAS_HAN = re.compile(r"[一-鿿㐀-䶿]")

# tags whose text never ends up in the pasted article body
NON_BODY_TAGS = {"head", "title", "style", "script"}

# a CJK character immediately followed by an ASCII comma/semicolon/bang/
# question mark almost always means someone forgot to use the full-width
# punctuation form; restricting to "CJK before" avoids false positives on
# mixed CJK/English/code text.
HALF_WIDTH_AFTER_CJK = re.compile(r"[一-鿿㐀-䶿][,;!?]")
STRAIGHT_QUOTE = re.compile(r"[\"']")

# inside a monospace/code block, ASCII punctuation is expected and fine
LOOKS_LIKE_CODE = re.compile(r"monospace|white-space\s*:\s*pre|courier|consolas|sf mono", re.I)

BANNED_PATTERNS = [
    (re.compile(r"<style\b", re.I), "a <style> block is present; all styling must be inline"),
    (re.compile(r"<script\b", re.I), "a <script> tag is present"),
    (re.compile(r"</?div\b", re.I), "a <div> is present; use <section> instead"),
    (re.compile(r"<link\b", re.I), "an external <link> (css/font) is present"),
    (re.compile(r"\bclass\s*=", re.I), "a class attribute is present; it gets stripped"),
    (re.compile(r"\bid\s*=", re.I), "an id attribute is present; it gets stripped"),
    (re.compile(r"position\s*:\s*(fixed|absolute|sticky)", re.I), "position fixed/absolute/sticky is unsupported"),
    (re.compile(r"float\s*:", re.I), "float is unsupported"),
    (re.compile(r"@media\b", re.I), "an @media query is present; unsupported"),
    (re.compile(r"@keyframes\b", re.I), "an @keyframes animation is present; unsupported"),
    (re.compile(r"@import\b", re.I), "an @import is present; unsupported"),
    (re.compile(r"display\s*:\s*grid", re.I), "display:grid is unsupported; use flex"),
    (re.compile(r"var\s*\(\s*--", re.I), "a CSS custom property var(--x) is present; hard-code the value"),
    (re.compile(r"url\s*\(\s*['\"]?https?://[^)]*\.(?:woff2?|ttf|otf|eot)", re.I),
     "an externally hosted web font is referenced"),
]


class ArticleWalker(HTMLParser):
    """Walks the fragment tracking two nested-depth counters as it goes:
    how many ancestor <span leaf> wrappers we're inside, and how many
    ancestor "this looks like a code block" elements we're inside."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._open_tags: list[tuple[str, bool, bool]] = []
        self.leaf_depth = 0
        self.code_depth = 0
        self.leaf_span_count = 0
        self.text_outside_leaf: list[tuple[str, str]] = []  # (snippet, parent tag)
        self.ascii_punct_hits: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        is_leaf = tag == "span" and "leaf" in attr_map
        is_code = bool(LOOKS_LIKE_CODE.search(attr_map.get("style") or ""))
        if is_leaf:
            self.leaf_span_count += 1
            self.leaf_depth += 1
        if is_code:
            self.code_depth += 1
        self._open_tags.append((tag, is_leaf, is_code))

    def handle_endtag(self, tag: str) -> None:
        # close the nearest matching open tag, unwinding anything left
        # unbalanced above it (tolerant of malformed fragments)
        for i in range(len(self._open_tags) - 1, -1, -1):
            if self._open_tags[i][0] == tag:
                for _, was_leaf, was_code in self._open_tags[i:]:
                    if was_leaf:
                        self.leaf_depth -= 1
                    if was_code:
                        self.code_depth -= 1
                del self._open_tags[i:]
                return

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text or not HAS_HAN.search(text):
            return
        if any(tag in NON_BODY_TAGS for tag, _, _ in self._open_tags):
            return
        if self.leaf_depth == 0:
            parent = self._open_tags[-1][0] if self._open_tags else "(root)"
            self.text_outside_leaf.append((_truncate(text), parent))
        if self.code_depth == 0 and (HALF_WIDTH_AFTER_CJK.search(text) or STRAIGHT_QUOTE.search(text)):
            self.ascii_punct_hits.append(_truncate(text))


def _truncate(text: str, limit: int = 24) -> str:
    return text if len(text) <= limit else text[:limit] + "..."


def validate(html: str) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []

    for pattern, message in BANNED_PATTERNS:
        count = len(pattern.findall(html))
        if count:
            errors.append(f"{message} ({count} occurrence{'s' if count != 1 else ''})")

    walker = ArticleWalker()
    try:
        walker.feed(html)
    except Exception as exc:  # a parse hiccup shouldn't hide the rest of the report
        warnings.append(f"HTML parsing stopped early: {exc}")

    if HAS_HAN.search(html) and walker.leaf_span_count == 0:
        errors.append('no <span leaf=""> wrapper found anywhere; '
                       "styling will be lost almost entirely on paste")
    elif walker.text_outside_leaf:
        examples = "; ".join(f'"{snippet}" (inside <{parent}>)'
                              for snippet, parent in walker.text_outside_leaf[:5])
        warnings.append(f"{len(walker.text_outside_leaf)} text run(s) sit outside a "
                         f'<span leaf=""> wrapper, styling may be lost. e.g. {examples}')

    if walker.ascii_punct_hits:
        examples = "; ".join(f'"{s}"' for s in walker.ascii_punct_hits[:5])
        warnings.append(f"{len(walker.ascii_punct_hits)} spot(s) of half-width punctuation "
                         f"or straight quotes next to Chinese text (should be full-width; "
                         f"code spans are exempt). e.g. {examples}")

    return errors, warnings, walker.leaf_span_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", help="path to the HTML fragment")
    parser.add_argument("--stdin", action="store_true", help="read the fragment from stdin")
    args = parser.parse_args()

    if args.stdin or not args.file:
        html = sys.stdin.read()
        label = "<stdin>"
    else:
        with open(args.file, encoding="utf-8", errors="replace") as f:
            html = f.read()
        label = args.file

    errors, warnings, leaf_count = validate(html)

    print(f"Validating: {label}")
    print(f"  <span leaf> wrappers found: {leaf_count}")
    if errors:
        print(f"\nERRORS ({len(errors)}) -- must fix, paste will break otherwise:")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}) -- worth a human look:")
        for w in warnings:
            print(f"  - {w}")
    if not errors and not warnings:
        print("\nClean. Safe to paste into the WeChat editor.")
    elif not errors:
        print("\nNo blocking issues; review the warnings above before pasting.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
