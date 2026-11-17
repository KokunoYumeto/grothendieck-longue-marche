#!/usr/bin/env python3
"""Build the doubts file mechanically from page fragments and reader records.

No interpretation or confidence reassessment is performed.  Recorded judgments
are copied; occurrence-level defaults are medium for unsure and low for illegible.
The default output is overwritten.  Supply --review-note to append an approved
reader-written legibility/abbreviation section instead of the pending sections.
"""

from __future__ import annotations

import argparse
from collections import OrderedDict
import html
import json
from pathlib import Path
import re
import sys


STEM = "MPL_83_178-222"
PAGE_NAME = re.compile(rf"{re.escape(STEM)}_83_scan(\d{{3}})\.tex\Z")
COMMAND = re.compile(r"\\([A-Za-z@]+|[^\n])")


def remove_comments(source: str) -> str:
    """Replace unescaped comments with spaces while preserving source offsets."""
    clean = list(source)
    offset = 0
    while offset < len(source):
        if source[offset] == "\\":
            offset += 2
        elif source[offset] == "%":
            while offset < len(source) and source[offset] != "\n":
                clean[offset] = " "
                offset += 1
        else:
            offset += 1
    return "".join(clean)


def brace_end(clean: str, opening: int) -> int:
    """Return the matching closing brace; escaped braces have no nesting effect."""
    depth = 0
    offset = opening
    while offset < len(clean):
        char = clean[offset]
        if char == "\\":
            match = COMMAND.match(clean, offset)
            offset = match.end() if match else offset + 1
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return offset
        offset += 1
    raise ValueError("Unbalanced argument braces")


def split_alternatives(raw: str, clean: str) -> list[str]:
    """Split only on unescaped | at brace depth zero, without semantic guessing."""
    depth = 0
    offset = 0
    boundaries = [-1]
    while offset < len(clean):
        char = clean[offset]
        if char == "\\":
            match = COMMAND.match(clean, offset)
            offset = match.end() if match else offset + 1
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "|" and depth == 0:
            boundaries.append(offset)
        offset += 1
    boundaries.append(len(raw))
    return [raw[left + 1:right].strip() for left, right in zip(boundaries, boundaries[1:])]


def occurrences(source: str, path: Path):
    clean = remove_comments(source)
    offset = 0
    while offset < len(clean):
        if clean[offset] != "\\":
            offset += 1
            continue
        match = COMMAND.match(clean, offset)
        if match is None:
            offset += 1
            continue
        name = match.group(1)
        if name in {"unsure", "illegible"}:
            line = source.count("\n", 0, offset) + 1
            opening = match.end()
            while opening < len(clean) and clean[opening].isspace():
                opening += 1
            if opening >= len(clean) or clean[opening] != "{":
                raise ValueError(f"{path.name}:{line}: \\{name} requires a braced argument")
            try:
                closing = brace_end(clean, opening)
            except ValueError as exc:
                raise ValueError(f"{path.name}:{line}: \\{name} has unbalanced argument braces") from exc
            raw = source[opening + 1:closing]
            if name == "unsure":
                parts = split_alternatives(raw, clean[opening + 1:closing])
                reading, alternatives = parts[0], " | ".join(parts[1:])
                confidence = "medium"
            else:
                reading, alternatives, confidence = raw.strip(), "", "low"
            yield {"line": line, "macro": name, "reading": reading,
                   "alternatives": alternatives, "confidence": confidence}
        # Do not skip an argument: nested unsure/illegible occurrences must count.
        offset = match.end()


def cell(value, literal: bool = False) -> str:
    text = html.escape(str(value), quote=False).replace("|", "&#124;")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if literal:
        return "<code>" + text.replace("\n", "<br>") + "</code>"
    for char, entity in [("\\", "&#92;"), ("`", "&#96;"), ("*", "&#42;"),
                         ("_", "&#95;"), ("[", "&#91;"), ("]", "&#93;"), ("$", "&#36;")]:
        text = text.replace(char, entity)
    return text.replace("\n", "<br>")


def table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines) + "\n"


def build(package: Path, output: Path, review_note: Path | None = None) -> dict:
    records = []
    for path in (package / "records").glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("scan"), int):
            records.append((data["scan"], path, data))
    records.sort(key=lambda item: (item[0], item[1].name))
    notation = OrderedDict()
    manual_rows = []
    for scan, path, record in records:
        for entry in record.get("notation", []):
            if not isinstance(entry, list) or len(entry) != 3:
                raise ValueError(f"{path.name}: notation entry must have three fields")
            sign, latex, comment = entry
            key = (str(sign), str(latex))
            row = notation.setdefault(key, {"scans": set(), "comments": OrderedDict()})
            row["scans"].add(scan)
            if str(comment):
                row["comments"].setdefault(str(comment), set()).add(scan)
        for entry in record.get("doubts", []):
            if not isinstance(entry, list) or len(entry) != 4:
                raise ValueError(f"{path.name}: doubt entry must have four fields")
            location, reading, alternatives, confidence = entry
            manual_rows.append(["83", str(scan), cell(location), cell(reading, True),
                                cell(alternatives), cell(confidence)])
    notation_rows = []
    for (sign, latex), row in notation.items():
        comments = [f"Scans {', '.join(map(str, sorted(scans)))}: {comment}"
                    for comment, scans in row["comments"].items()]
        notation_rows.append([cell(sign), cell(latex, True),
                              ", ".join(map(str, sorted(row["scans"]))), cell("\n".join(comments))])
    occurrence_rows = []
    counts = {"unsure": 0, "illegible": 0}
    page_count = 0
    for path in sorted((package / "pages").glob("*.tex")):
        match = PAGE_NAME.fullmatch(path.name)
        if match is None:
            continue
        scan = int(match.group(1))
        page_count += 1
        for occurrence in occurrences(path.read_text(encoding="utf-8"), path):
            counts[occurrence["macro"]] += 1
            occurrence_rows.append(["83", str(scan), str(occurrence["line"]),
                                    cell("\\" + occurrence["macro"], True),
                                    cell(occurrence["reading"], True),
                                    cell(occurrence["alternatives"], True), occurrence["confidence"]])
    sections = [
        f"# {STEM} — notation and doubts\n",
        "This register is assembled from the reader's page records and the current page fragments. "
        "It preserves recorded readings and judgments without resolving them.\n",
        "## Recurring notation\n",
        "Identical pairs of recorded sign and LaTeX representation are grouped; all associated scans "
        "and comments are retained. Grouping is exact and does not establish that differently recorded signs are equivalent.\n",
        table(["Recorded sign", "LaTeX", "Scans", "Recorded comments"], notation_rows),
        "## Reader-recorded doubts\n",
        "Locations, proposed readings, alternatives, and confidence values below are copied from the page records.\n",
        table(["File", "Scan", "Approximate location", "Reading", "Alternatives / recorded explanation", "Confidence"], manual_rows),
        "## Occurrence-level concordance\n",
        f"Line numbers refer to `pages/{STEM}_83_scanNNN.tex`, not the combined fragment or manuscript lines. "
        "Every balanced-brace occurrence of `\\unsure` or `\\illegible` is included, including nested occurrences "
        "inside deletions, insertions, and other macros. Alternatives are split only at unescaped vertical bars "
        "outside nested braces; no mathematical or linguistic interpretation is applied.\n",
        "The confidence entries in this concordance are mechanical defaults: **medium** for `\\unsure` and "
        "**low** for `\\illegible`. They are not a fresh assessment and do not supersede the reader-recorded "
        "confidence above. For `\\illegible`, the reading/argument column gives the macro's argument.\n",
        table(["File", "Scan", "Page-file line", "Macro", "Reading / argument", "Alternatives", "Default confidence"], occurrence_rows),
    ]
    if review_note is not None:
        sections.append(review_note.read_text(encoding="utf-8").rstrip() + "\n")
    else:
        sections.extend([
            "## Legibility assessment — pending primary-reader review\n",
            "PENDING: the primary reader will supply an honest assessment of legibility, the least secure passages, "
            "and the limits of confidence after the visual audit. This placeholder is not a completed assessment.\n",
            "## Abbreviations — pending primary-reader review\n",
            "PENDING: the primary reader will supply the abbreviations encountered and their proposed expansions. "
            "Expansions belong here only and must not be inserted into the diplomatic transcription.\n",
        ])
    output.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")
    return {"records": len(records), "pages": page_count, "notation_pairs": len(notation_rows),
            "manual_doubts": len(manual_rows), "occurrences": counts, "output": str(output)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--review-note", type=Path, help="Append this reader-approved narrative instead of pending sections.")
    args = parser.parse_args()
    package = args.package.resolve()
    output = args.output.resolve() if args.output else package / f"{STEM}_doubts.md"
    try:
        result = build(package, output, args.review_note)
    except (ValueError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
