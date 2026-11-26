#!/usr/bin/env python3
"""Wrap a validated article fragment in a one-click "copy to WeChat" preview.

The exported article is a bare <section>...</section>: no <html>/<body>, no
script, no style class -- it must stay that way so a validator can check it
and so pasting it keeps only compliant markup. This script does NOT modify
that fragment; it drops it, unmodified, into a tiny HTML shell (template at
assets/preview-template.html) that adds a "Copy" button around it. The button
selects the rendered fragment and copies it as rich text (same effect as a
manual Ctrl+A / Ctrl+C), so pasting into the WeChat editor keeps every style.

Because the button/script live only in the shell -- never inside the
fragment itself -- the thing that actually gets copied is still exactly the
compliant <section> that validate_gzh_html.py already approved.

Usage:
    wrap_preview.py <section.html> [output.html]
    (output defaults to <section-without-extension>_preview.html)
"""

from __future__ import annotations

import pathlib
import sys

PLACEHOLDER_TITLE = "{{TITLE}}"
PLACEHOLDER_BODY = "<!--GZH_CONTENT-->"


def build_preview(fragment_path: pathlib.Path, template_path: pathlib.Path) -> str:
    fragment = fragment_path.read_text(encoding="utf-8").strip()
    template = template_path.read_text(encoding="utf-8")
    title = fragment_path.stem
    return template.replace(PLACEHOLDER_TITLE, title).replace(PLACEHOLDER_BODY, fragment)


def default_output_path(fragment_path: pathlib.Path) -> pathlib.Path:
    return fragment_path.with_name(fragment_path.stem + "_preview.html")


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: wrap_preview.py <section.html> [output.html]")
        sys.exit(1)

    fragment_path = pathlib.Path(sys.argv[1])
    if not fragment_path.is_file():
        print(f"not found: {fragment_path}")
        sys.exit(1)

    script_dir = pathlib.Path(__file__).resolve().parent
    template_path = script_dir.parent / "assets" / "preview-template.html"

    preview_html = build_preview(fragment_path, template_path)

    output_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else default_output_path(fragment_path)
    output_path.write_text(preview_html, encoding="utf-8")

    print(f"Wrote preview with a copy button: {output_path}")
    print('Open it in a browser, click "Copy to WeChat" top-right, '
          "then Ctrl/Cmd+V into the WeChat editor.")


if __name__ == "__main__":
    main()
