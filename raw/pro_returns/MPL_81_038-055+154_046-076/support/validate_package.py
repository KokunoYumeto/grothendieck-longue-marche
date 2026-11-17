#!/usr/bin/env python3
"""Read-only structural validation of MPL_81_038-055+154_046-076.

This does not assess readings, completeness against scans, or mathematical
correctness. It does not use OCR, image libraries, or any context documents.
Run only when the transcription owner authorizes checking the completed files.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

PACKAGE = "MPL_81_038-055+154_046-076"
SCANS = tuple(range(46, 77))
HEADER = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEETS = {"text", "reused_typed", "cancelled_draft", "cover"}


def tex_without_comments(text: str) -> str:
    """Remove unescaped TeX comments; preserve newlines and escaped percent signs."""
    result = []
    for line in text.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char != "%":
                continue
            j = i - 1
            while j >= 0 and line[j] == "\\":
                j -= 1
            if (i - j - 1) % 2 == 0:
                line = line[:i] + ("\n" if line.endswith("\n") else "")
                break
        result.append(line)
    return "".join(result)


def brace_errors(text: str) -> list[str]:
    """Check grouping braces, ignoring TeX control symbols and comments."""
    source = tex_without_comments(text)
    stack: list[tuple[int, int]] = []
    errors: list[str] = []
    line = column = 1
    i = 0
    while i < len(source):
        c = source[i]
        if c == "\\" and i + 1 < len(source):
            # A control symbol consumes the following non-letter, including
            # literal braces. Control words do not consume following groups.
            if not source[i + 1].isalpha():
                i += 2
                column += 2
                continue
        if c == "{":
            stack.append((line, column))
        elif c == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at {line}:{column}")
        if c == "\n":
            line += 1
            column = 1
        else:
            column += 1
        i += 1
    errors.extend(f"unmatched opening brace at {line}:{column}" for line, column in stack)
    return errors


def validate(directory: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    pages: dict[int, str] = {}
    page_dir = directory / "pages"
    required = [f"{PACKAGE}_transcription.tex", f"{PACKAGE}_doubts.md",
                f"{PACKAGE}_inventory.csv", f"{PACKAGE}_notes.md", "progress.log"]
    for name in required:
        path = directory / name
        if not path.is_file():
            errors.append(f"missing required file: {name}")
        elif path.stat().st_size == 0:
            errors.append(f"empty required file: {name}")

    expected_names = {f"{PACKAGE}_154_scan{scan:03d}.tex" for scan in SCANS}
    actual_names = {p.name for p in page_dir.glob("*.tex")} if page_dir.is_dir() else set()
    for name in sorted(expected_names - actual_names):
        errors.append(f"missing page file: pages/{name}")
    for name in sorted(actual_names - expected_names):
        errors.append(f"unexpected page file: pages/{name}")
    for scan in SCANS:
        name = f"{PACKAGE}_154_scan{scan:03d}.tex"
        path = page_dir / name
        if not path.is_file():
            continue
        try:
            source = path.read_bytes().decode("utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read {name}: {exc}")
            continue
        pages[scan] = source
        clean = tex_without_comments(source)
        found_scans = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if found_scans != [str(scan)]:
            errors.append(f"{name}: expected one scan marker {scan}; found {found_scans}")
        found_cotes = re.findall(r"\\cotefile\s*\{\s*([^{}]+)\s*\}", clean)
        expected_cotes = ["154"] if scan == SCANS[0] else []
        if found_cotes != expected_cotes:
            errors.append(f"{name}: expected cote markers {expected_cotes}; found {found_cotes}")
        beginning = (r"\s*\\cotefile\s*\{154\}\s*\\scanpage\s*\{46\}" if scan == 46
                     else rf"\s*\\scanpage\s*\{{{scan}\}}")
        if not re.match(beginning, clean):
            errors.append(f"{name}: required marker(s) not at the beginning")
        errors.extend(f"{name}: {message}" for message in brace_errors(source))
        if not source.endswith("\n"):
            warnings.append(f"{name}: no terminal newline")

    combined_path = directory / f"{PACKAGE}_transcription.tex"
    combined = ""
    if combined_path.is_file():
        try:
            combined = combined_path.read_bytes().decode("utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read combined transcription: {exc}")
        if len(pages) == len(SCANS):
            expected = "".join(pages[scan] for scan in SCANS)
            if combined != expected:
                mismatch = next((i for i, (a, b) in enumerate(zip(combined, expected)) if a != b),
                                min(len(combined), len(expected)))
                errors.append("combined transcription differs from exact ordered page concatenation "
                              f"at character {mismatch} (lengths {len(combined)}/{len(expected)})")
        clean = tex_without_comments(combined)
        found = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if found != [str(s) for s in SCANS]:
            errors.append(f"combined scan sequence incorrect: {found}")
        for command in ("includegraphics", "input", "include", "documentclass", "usepackage",
                        "newcommand", "renewcommand", "def"):
            if re.search(r"\\" + command + r"(?![A-Za-z])", clean):
                errors.append(f"combined transcription contains prohibited fragment command: \\{command}")
        if re.search(r"!\[[^\]]*\]\([^\)]*\)|<img\b|data:image/", clean, re.IGNORECASE):
            errors.append("combined transcription contains an image embedding")
        errors.extend(f"combined transcription: {message}" for message in brace_errors(combined))

    inventory_path = directory / f"{PACKAGE}_inventory.csv"
    rows = []
    if inventory_path.is_file():
        try:
            with inventory_path.open(newline="", encoding="utf-8-sig") as stream:
                reader = csv.DictReader(stream)
                if reader.fieldnames != HEADER:
                    errors.append(f"inventory header differs: {reader.fieldnames}")
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"cannot read inventory: {exc}")
        if not rows:
            errors.append("inventory contains no elements")
        counts: Counter[int] = Counter()
        element_ids = set()
        for line, row in enumerate(rows, start=2):
            label = f"inventory row {line}"
            if None in row:
                errors.append(f"{label}: more cells than columns")
            if any(row.get(k) is None for k in HEADER):
                errors.append(f"{label}: missing cells")
            cote = (row.get("cote") or "").strip()
            if cote != "154":
                errors.append(f"{label}: cote {cote!r}, expected 154")
            try:
                scan = int(row.get("scan") or "")
            except ValueError:
                errors.append(f"{label}: invalid scan {row.get('scan')!r}")
                scan = -1
            if scan not in SCANS:
                errors.append(f"{label}: scan outside 46–76: {scan}")
            else:
                counts[scan] += 1
            if row.get("sheet_kind") not in SHEETS:
                errors.append(f"{label}: invalid sheet_kind {row.get('sheet_kind')!r}")
            if row.get("kind") not in KINDS:
                errors.append(f"{label}: invalid kind {row.get('kind')!r}")
            if row.get("transcribed") != "yes":
                errors.append(f"{label}: transcribed must be 'yes'")
            for key in ("element", "position", "first_words_or_objects"):
                if not (row.get(key) or "").strip():
                    errors.append(f"{label}: empty {key}")
            identity = (cote, scan, row.get("element"))
            if identity in element_ids:
                errors.append(f"{label}: repeated element identifier {identity}")
            element_ids.add(identity)
        for scan in SCANS:
            if counts[scan] == 0:
                errors.append(f"inventory has no elements for scan {scan}")
    else:
        counts = Counter()

    return {
        "ok": not errors,
        "directory": str(directory.resolve()),
        "expected_pages": len(SCANS),
        "page_files_read": len(pages),
        "inventory_rows": len(rows),
        "inventory_rows_by_scan": {str(s): counts[s] for s in SCANS},
        "errors": errors,
        "warnings": warnings,
        "scope": "Structural checks only; no verification of manuscript readings or visual completeness.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path,
                        default=Path("/workspace/scratch/89f8415d3ab0/deliver"))
    parser.add_argument("--json", action="store_true", help="emit a JSON report to stdout")
    args = parser.parse_args()
    report = validate(args.directory)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("PASS" if report["ok"] else "FAIL")
        print(f"Pages: {report['page_files_read']}/{report['expected_pages']}; "
              f"inventory elements: {report['inventory_rows']}")
        for error in report["errors"]:
            print(f"ERROR: {error}")
        for warning in report["warnings"]:
            print(f"WARNING: {warning}")
        print(report["scope"])
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
