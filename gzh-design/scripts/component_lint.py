#!/usr/bin/env python3
"""Lint the theme component libraries themselves (references/*.md).

Why this exists: a theme file is prose + fenced ```html blocks. A model
editing that prose can accidentally introduce a WeChat-incompatible pattern
inside a code block, and nobody notices until an actual article breaks. This
script is the first half of a two-stage check:

    edit a theme file -> component_lint.py (checks the library)
        -> generate an article -> validate_gzh_html.py (checks the output)

Usage:
    component_lint.py [skill-root]      # defaults to the current directory

Exit code 1 if any ERROR-level finding exists, else 0.
"""

from __future__ import annotations

import pathlib
import re
import sys
from dataclasses import dataclass, field

FENCE_START = re.compile(r"^```html\s*$")
FENCE_END = re.compile(r"^```\s*$")


@dataclass
class Rule:
    pattern: re.Pattern
    severity: str  # "error" | "warn"
    message: str


RULES: list[Rule] = [
    Rule(re.compile(r"white-space\s*:\s*pre", re.I), "error",
         "white-space:pre renders the source's own indentation/newlines as a "
         "huge left margin and blank lines; use one <p style=\"margin:0\"> per "
         "line and full-width spaces for indent instead."),
    Rule(re.compile(r"</?div\b", re.I), "error", "<div> is present; use <section>."),
    Rule(re.compile(r"\bclass\s*=", re.I), "error", "class=\"...\" is present (stripped by WeChat)."),
    Rule(re.compile(r"\bid\s*=", re.I), "error", "id=\"...\" is present (stripped by WeChat)."),
    Rule(re.compile(r"<style\b", re.I), "error", "<style> block is present."),
    Rule(re.compile(r"position\s*:\s*(fixed|absolute|sticky)", re.I), "error",
         "position:fixed/absolute/sticky is not supported."),
    Rule(re.compile(r"display\s*:\s*grid", re.I), "error", "display:grid is not supported."),
    Rule(re.compile(r"var\s*\(\s*--", re.I), "error", "CSS custom property var(--x) is not supported."),
    Rule(re.compile(r"@(media|keyframes|import)\b", re.I), "error",
         "@media / @keyframes / @import is not supported."),
]

# A four-sided dashed border is a lazy "emphasis box" anti-pattern UNLESS the
# block is a centered placeholder (e.g. "drop your screenshot here").
FOUR_SIDED_DASHED = re.compile(r"border\s*:\s*[^;{}]*dashed", re.I)
IS_CENTERED = re.compile(r"text-align\s*:\s*center", re.I)


def iter_html_blocks(markdown_text: str):
    """Yield the body of each fenced ```html ... ``` block, line-accurate."""
    lines = markdown_text.splitlines()
    buf: list[str] | None = None
    for line in lines:
        if buf is None:
            if FENCE_START.match(line):
                buf = []
            continue
        if FENCE_END.match(line):
            yield "\n".join(buf)
            buf = None
        else:
            buf.append(line)


def audit_theme_file(path: pathlib.Path) -> list[tuple[str, str]]:
    """Return a de-duplicated (severity, message) list for one theme file."""
    text = path.read_text(encoding="utf-8", errors="replace")
    findings: dict[str, str] = {}  # message -> severity, dedup by message

    for block in iter_html_blocks(text):
        for rule in RULES:
            if rule.pattern.search(block):
                findings[rule.message] = rule.severity
        if FOUR_SIDED_DASHED.search(block) and not IS_CENTERED.search(block):
            findings["uses a four-sided dashed border outside a centered "
                      "placeholder block; emphasis should be a left rule or "
                      "card, not a dashed box around it"] = "warn"

    # stable order: errors first, then warnings, in first-seen order of RULES
    ordered = sorted(findings.items(), key=lambda kv: 0 if kv[1] == "error" else 1)
    return [(sev, msg) for msg, sev in ordered]


def main() -> None:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    theme_files = sorted((root / "references").glob("*.md"))
    if not theme_files:
        print(f"no references/*.md found under {root}")
        sys.exit(1)

    print(f"Auditing {len(theme_files)} component librar{'y' if len(theme_files) == 1 else 'ies'}\n")

    clean = 0
    error_total = 0
    warn_total = 0
    for path in theme_files:
        findings = audit_theme_file(path)
        if not findings:
            clean += 1
            continue
        label = path.stem.replace("theme-", "")
        print(f"[{label}]")
        for severity, message in findings:
            if severity == "error":
                error_total += 1
                print(f"  ERROR  {message}")
            else:
                warn_total += 1
                print(f"  WARN   {message}")

    print(f"\n{clean}/{len(theme_files)} clean -- errors: {error_total}, warnings: {warn_total}")
    if error_total == 0 and warn_total == 0:
        print("All component libraries are free of known anti-patterns.")
    sys.exit(1 if error_total else 0)


if __name__ == "__main__":
    main()
