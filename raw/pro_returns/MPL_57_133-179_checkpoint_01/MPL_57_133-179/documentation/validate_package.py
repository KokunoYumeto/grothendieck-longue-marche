#!/usr/bin/env python3
"""Read-only structural validation for MPL_57_133-179 deliverables.

This script never views scan images, performs OCR, accesses the context archive,
or rewrites a manuscript or log. It cannot certify transcription accuracy or
the completeness of an inventory relative to the images. Brace checking is
lexical and deliberately conservative: TeX comments and escaped braces are
excluded, but full TeX expansion is not attempted.

The combined fragment must equal the raw byte concatenation, in scan order,
of the individual page fragments. Put any desired separating whitespace in
the individual page files themselves.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


PREFIX = "MPL_57_133-179"
SCANS = tuple(n for n in range(133, 180) if n not in {137, 146, 168, 172})
INVENTORY_COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"
}


def brace_issues(text: str) -> list[str]:
    """Find unbalanced literal grouping braces, skipping comments/control symbols."""
    issues: list[str] = []
    stack: list[int] = []
    line = 1
    i = 0
    while i < len(text):
        char = text[i]
        if char == "\\":
            # A control symbol consumes the following non-letter, so \\{ and
            # \\} are literal characters; a control word does not consume its
            # following group. Two backslashes are likewise one control symbol.
            if i + 1 < len(text) and not text[i + 1].isalpha():
                if text[i + 1] == "\n":
                    line += 1
                i += 2
                continue
            i += 1
            while i < len(text) and text[i].isalpha():
                i += 1
            continue
        if char == "%":
            next_line = text.find("\n", i)
            if next_line == -1:
                break
            i = next_line
            continue
        if char == "\n":
            line += 1
        elif char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                issues.append(f"unmatched closing brace near line {line}")
        i += 1
    issues.extend(f"unclosed opening brace near line {n}" for n in stack)
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.package.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    required = [
        f"{PREFIX}_transcription.tex", f"{PREFIX}_doubts.md",
        f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md", "progress.log",
        "CHECK_EVENTS.tsv",
    ]
    missing = [name for name in required if not (root / name).is_file()]
    errors.extend(f"missing required deliverable: {name}" for name in missing)
    expected_pages = [f"{PREFIX}_57_scan{n:03d}.tex" for n in SCANS]
    found_pages = sorted(p.name for p in (root / "pages").glob("*.tex"))
    missing_pages = sorted(set(expected_pages) - set(found_pages))
    extra_pages = sorted(set(found_pages) - set(expected_pages))
    errors.extend(f"missing page: {name}" for name in missing_pages)
    errors.extend(f"unexpected page: {name}" for name in extra_pages)

    page_bytes: list[bytes] = []
    hashes: dict[str, str] = {}
    for scan, name in zip(SCANS, expected_pages):
        path = root / "pages" / name
        if not path.is_file():
            continue
        data = path.read_bytes()
        hashes[f"pages/{name}"] = hashlib.sha256(data).hexdigest()
        page_bytes.append(data)
        try:
            content = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{name}: invalid UTF-8: {exc}")
            continue
        markers = re.findall(r"\\scanpage\{([^{}]+)\}", content)
        if markers != [str(scan)]:
            errors.append(f"{name}: expected one scanpage marker {{{scan}}}, found {markers}")
        if scan == SCANS[0] and not content.lstrip().startswith("\\cotefile{57}"):
            errors.append(f"{name}: first page must start with \\cotefile{{57}}")
        for issue in brace_issues(content):
            errors.append(f"{name}: {issue}")

    combined_path = root / f"{PREFIX}_transcription.tex"
    concat_matches = None
    if combined_path.is_file():
        combined = combined_path.read_bytes()
        hashes[combined_path.name] = hashlib.sha256(combined).hexdigest()
        if not missing_pages:
            concat_matches = combined == b"".join(page_bytes)
            if not concat_matches:
                errors.append("combined transcription differs from raw byte concatenation of page files")

    inventory_path = root / f"{PREFIX}_inventory.csv"
    inventory_count = 0
    inventory_scans: set[int] = set()
    if inventory_path.is_file():
        try:
            with inventory_path.open(encoding="utf-8", newline="") as stream:
                reader = csv.DictReader(stream)
                if reader.fieldnames != INVENTORY_COLUMNS:
                    errors.append(f"inventory columns differ: {reader.fieldnames}")
                seen_elements: set[tuple[str, str, str]] = set()
                for row_number, row in enumerate(reader, 2):
                    inventory_count += 1
                    location = f"inventory row {row_number}"
                    if None in row:
                        errors.append(f"{location}: extra CSV fields")
                    for field in INVENTORY_COLUMNS:
                        if not str(row.get(field, "") or "").strip():
                            errors.append(f"{location}: empty {field}")
                    if row.get("cote") != "57":
                        errors.append(f"{location}: cote is not 57")
                    try:
                        scan = int(row.get("scan", ""))
                        inventory_scans.add(scan)
                        if scan not in SCANS:
                            errors.append(f"{location}: unexpected scan {scan}")
                    except (ValueError, TypeError):
                        errors.append(f"{location}: nonnumeric scan")
                    if row.get("sheet_kind") not in SHEET_KINDS:
                        errors.append(f"{location}: unsupported sheet_kind {row.get('sheet_kind')!r}")
                    if row.get("kind") not in ELEMENT_KINDS:
                        errors.append(f"{location}: unsupported kind {row.get('kind')!r}")
                    if row.get("transcribed") != "yes":
                        errors.append(f"{location}: transcribed is not yes")
                    key = (row.get("cote", ""), row.get("scan", ""), row.get("element", ""))
                    if key in seen_elements:
                        errors.append(f"{location}: duplicate element identifier {key}")
                    seen_elements.add(key)
            for scan in sorted(set(SCANS) - inventory_scans):
                errors.append(f"inventory lacks scan {scan}")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"inventory unreadable: {exc}")

    checks_path = root / "CHECK_EVENTS.tsv"
    check_count = 0
    if checks_path.is_file():
        with checks_path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            if reader.fieldnames != ["statement_id", "date", "who", "type", "outcome"]:
                errors.append(f"CHECK_EVENTS.tsv columns differ: {reader.fieldnames}")
            check_count = sum(1 for _ in reader)
        if not check_count:
            warnings.append("CHECK_EVENTS.tsv has no check events; this may be expected before research")

    result = {
        "package": str(root), "expected_page_count": len(SCANS),
        "found_page_count": len(found_pages), "missing_required": missing,
        "missing_pages": missing_pages, "unexpected_pages": extra_pages,
        "combined_matches_raw_concatenation": concat_matches,
        "inventory_element_count": inventory_count,
        "inventory_page_count": len(inventory_scans), "check_event_count": check_count,
        "errors": errors, "warnings": warnings, "sha256": hashes,
        "limitations": "Structural checks only. No image access, OCR, reading audit, semantic verification, or context access.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
