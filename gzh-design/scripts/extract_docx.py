#!/usr/bin/env python3
"""Convert a .docx file into the Markdown this skill's workflow expects.

No external dependencies: a .docx is just a zip archive of XML parts, so this
reads word/document.xml (plus styles.xml for heading levels and the
relationship file for embedded images) with the standard library only.

Headings become `#`..`######`, bold/underline runs become `**x**`/`<u>x</u>`,
list paragraphs become `- x`, embedded images are unpacked next to the
output file and referenced with relative paths, and tables become Markdown
tables. Anything this script can't confidently model (text boxes, nested
tables) is left out rather than guessed at; a short summary line at the end
reports what was extracted.

Usage:
    extract_docx.py report.docx [-o report.md]

Exit code 0 on success, 1 if the input isn't a readable .docx.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

NS_WORD = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NS_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
NS_DRAWING = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def _heading_levels_by_style_id(archive: zipfile.ZipFile) -> dict[str, int]:
    """Map a paragraph styleId to a heading level 1-6, for styles that are
    headings. Non-heading styles are simply absent from the result."""
    try:
        root = ET.fromstring(archive.read("word/styles.xml"))
    except KeyError:
        return {}

    levels: dict[str, int] = {}
    for style_el in root.iter(f"{NS_WORD}style"):
        style_id = style_el.get(f"{NS_WORD}styleId") or ""
        name_el = style_el.find(f"{NS_WORD}name")
        display_name = (name_el.get(f"{NS_WORD}val") if name_el is not None else "") or ""
        match = re.search(r"(?:heading|标题)\s*([1-6])", display_name, re.I) \
            or re.fullmatch(r"([1-6])", style_id)
        if match:
            levels[style_id] = int(match.group(1))
    return levels


def _image_targets_by_relationship_id(archive: zipfile.ZipFile) -> dict[str, str]:
    """Map a relationship id (r:embed) to its media file path inside the zip."""
    try:
        root = ET.fromstring(archive.read("word/_rels/document.xml.rels"))
    except KeyError:
        return {}

    targets: dict[str, str] = {}
    for relationship in root:
        target = relationship.get("Target") or ""
        if "media/" in target:
            targets[relationship.get("Id")] = "word/" + target.lstrip("/").replace("../", "")
    return targets


def _paragraph_to_markdown_inline(paragraph_el: ET.Element) -> str:
    """Render one <w:p>'s runs as inline Markdown (bold, underline)."""
    pieces: list[str] = []
    for run_el in paragraph_el.iter(f"{NS_WORD}r"):
        run_props = run_el.find(f"{NS_WORD}rPr")
        is_bold = (run_props is not None and run_props.find(f"{NS_WORD}b") is not None
                   and (run_props.find(f"{NS_WORD}b").get(f"{NS_WORD}val") or "1") not in ("0", "false"))
        is_underlined = run_props is not None and run_props.find(f"{NS_WORD}u") is not None

        text = "".join(t.text or "" for t in run_el.iter(f"{NS_WORD}t"))
        if not text:
            continue
        if is_bold:
            text = f"**{text}**"
        if is_underlined:
            text = f"<u>{text}</u>"
        pieces.append(text)

    joined = "".join(pieces)
    return re.sub(r"\*\*\*\*", "", joined)  # adjacent bold runs leave an empty **** seam


def _table_el_to_markdown_rows(table_el: ET.Element) -> list[str]:
    rows: list[str] = []
    for row_el in table_el.findall(f"{NS_WORD}tr"):
        cells = []
        for cell_el in row_el.findall(f"{NS_WORD}tc"):
            cell_text = "".join(t.text or "" for t in cell_el.iter(f"{NS_WORD}t")).strip()
            cells.append(cell_text.replace("|", "\\|") or " ")
        rows.append("| " + " | ".join(cells) + " |")

    if not rows:
        return []
    column_count = rows[0].count("|") - 1
    separator = "|" + "---|" * column_count
    return [rows[0], separator] + rows[1:]


class DocxToMarkdown:
    """Stateful converter: one instance per document, accumulates output
    lines and a few counters for the closing summary."""

    def __init__(self, archive: zipfile.ZipFile, image_dir: pathlib.Path) -> None:
        self.archive = archive
        self.image_dir = image_dir
        self.heading_levels = _heading_levels_by_style_id(archive)
        self.image_targets = _image_targets_by_relationship_id(archive)
        self.lines: list[str] = []
        self.image_count = 0
        self.table_count = 0

    def convert_body(self, body_el: ET.Element) -> None:
        for child in body_el:
            if child.tag == f"{NS_WORD}tbl":
                self._emit_table(child)
            elif child.tag == f"{NS_WORD}p":
                self._emit_paragraph(child)

    def _emit_table(self, table_el: ET.Element) -> None:
        rows = _table_el_to_markdown_rows(table_el)
        if not rows:
            return
        self.lines.extend(rows)
        self.lines.append("")
        self.table_count += 1

    def _emit_paragraph(self, paragraph_el: ET.Element) -> None:
        self._emit_inline_images(paragraph_el)

        text = _paragraph_to_markdown_inline(paragraph_el).strip()
        if not text:
            return

        style_id = self._paragraph_style_id(paragraph_el)
        heading_level = self.heading_levels.get(style_id)
        if heading_level:
            text_without_bold = re.sub(r"^\*\*(.*)\*\*$", r"\1", text)
            self.lines.append("#" * min(heading_level, 6) + " " + text_without_bold)
        elif self._is_list_paragraph(paragraph_el, style_id):
            self.lines.append("- " + text)
        else:
            self.lines.append(text)
        self.lines.append("")

    def _emit_inline_images(self, paragraph_el: ET.Element) -> None:
        for blip_el in paragraph_el.iter(f"{NS_DRAWING}blip"):
            relationship_id = blip_el.get(f"{NS_REL}embed")
            media_path = self.image_targets.get(relationship_id)
            if not media_path:
                continue
            self.image_dir.mkdir(parents=True, exist_ok=True)
            self.image_count += 1
            filename = f"{self.image_count:02d}-{pathlib.Path(media_path).name}"
            (self.image_dir / filename).write_bytes(self.archive.read(media_path))
            self.lines.append(f"![](images/{filename})")
            self.lines.append("")

    @staticmethod
    def _paragraph_style_id(paragraph_el: ET.Element) -> str:
        paragraph_props = paragraph_el.find(f"{NS_WORD}pPr")
        if paragraph_props is None:
            return ""
        style_el = paragraph_props.find(f"{NS_WORD}pStyle")
        return style_el.get(f"{NS_WORD}val") if style_el is not None else ""

    @staticmethod
    def _is_list_paragraph(paragraph_el: ET.Element, style_id: str) -> bool:
        paragraph_props = paragraph_el.find(f"{NS_WORD}pPr")
        has_numbering = paragraph_props is not None and paragraph_props.find(f"{NS_WORD}numPr") is not None
        has_list_style_name = bool(re.search(r"list|列表", style_id, re.I))
        return has_numbering or has_list_style_name

    def render(self) -> str:
        return "\n".join(self.lines).rstrip() + "\n"

    def summary(self) -> str:
        body_paragraphs = sum(1 for l in self.lines if l and not l.startswith(("#", "-", "![", "|")))
        headings = sum(1 for l in self.lines if l.startswith("#"))
        list_items = sum(1 for l in self.lines if l.startswith("- "))
        parts = [f"paragraphs {body_paragraphs}", f"headings {headings}",
                 f"list items {list_items}", f"images {self.image_count}"]
        if self.table_count:
            parts.append(f"tables {self.table_count} (converted to Markdown tables)")
        return " | ".join(parts)


def convert(docx_path: pathlib.Path, output_path: pathlib.Path) -> int:
    try:
        archive = zipfile.ZipFile(docx_path)
        document_root = ET.fromstring(archive.read("word/document.xml"))
    except (zipfile.BadZipFile, KeyError) as exc:
        print(f"not a readable .docx: {exc}", file=sys.stderr)
        return 1

    body_el = document_root.find(f"{NS_WORD}body")
    converter = DocxToMarkdown(archive, output_path.parent / "images")
    converter.convert_body(body_el)

    output_path.write_text(converter.render(), encoding="utf-8")
    print(f"{docx_path.name} -> {output_path}")
    print(f"  {converter.summary()}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", help="path to the .docx file")
    parser.add_argument("-o", "--out", help="output .md path (defaults to the same name)")
    args = parser.parse_args()

    docx_path = pathlib.Path(args.docx)
    if not docx_path.is_file():
        print(f"file not found: {docx_path}", file=sys.stderr)
        sys.exit(1)

    output_path = pathlib.Path(args.out) if args.out else docx_path.with_suffix(".md")
    sys.exit(convert(docx_path, output_path))


if __name__ == "__main__":
    main()
