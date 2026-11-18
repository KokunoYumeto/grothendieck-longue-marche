#!/usr/bin/env python3
"""Read-only structural checks for MPL_64_116-157.

This checks packaging, not transcription accuracy or manuscript coverage.
It neither reads source images/context nor changes any deliverable.
Run only when the principal transcriber is ready for the requested checks.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path


PACKAGE = "MPL_64_116-157"
EXPECTED_SCANS = tuple(n for n in range(116, 158) if n not in {122, 130, 142})
INVENTORY_HEADER = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
CHECK_EVENTS_HEADER = ["statement_id", "date", "who", "type", "outcome"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}


def without_comments(text: str) -> str:
    """Remove unescaped TeX comments; preserve line boundaries."""
    result = []
    for line in text.splitlines():
        for i, char in enumerate(line):
            if char == "%":
                backslashes = 0
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    backslashes += 1
                    j -= 1
                if backslashes % 2 == 0:
                    line = line[:i]
                    break
        result.append(line)
    return "\n".join(result)


def tex_warnings(text: str) -> list[str]:
    """Conservative balance checks; warnings are not claims about TeX validity."""
    source = without_comments(text)
    warnings = []
    depth = 0
    first_negative = None
    for match in re.finditer(r"\\.|[{}]", source, re.DOTALL):
        token = match.group()
        if token == "{":
            depth += 1
        elif token == "}":
            depth -= 1
            if depth < 0 and first_negative is None:
                first_negative = source.count("\n", 0, match.start()) + 1
    if first_negative is not None:
        warnings.append(f"closing brace before matching opening brace near line {first_negative}")
    if depth:
        warnings.append(f"net unescaped brace balance is {depth:+d}")

    stack = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", source):
        operation, name = match.groups()
        line = source.count("\n", 0, match.start()) + 1
        if operation == "begin":
            stack.append((name, line))
        elif not stack:
            warnings.append(f"unmatched end of {name!r} near line {line}")
        elif stack[-1][0] != name:
            warnings.append(
                f"end of {name!r} near line {line} conflicts with open {stack[-1][0]!r}"
            )
        else:
            stack.pop()
    for name, line in stack:
        warnings.append(f"unclosed {name!r} environment begun near line {line}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root", nargs="?", type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="package working directory (default: parent of scripts directory)",
    )
    parser.add_argument(
        "--partial", action="store_true",
        help="check existing pages and their inventory only; do not require final deliverables",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors = []
    warnings = []
    page_texts = {}
    expected_names = {f"{PACKAGE}_64_scan{n:03d}.tex" for n in EXPECTED_SCANS}
    existing = {p.name for p in (root / "pages").glob("*.tex")}
    extra = sorted(existing - expected_names)
    if extra:
        errors.append("unexpected page files: " + ", ".join(extra))

    for scan in EXPECTED_SCANS:
        path = root / "pages" / f"{PACKAGE}_64_scan{scan:03d}.tex"
        if not path.is_file():
            if not args.partial:
                errors.append(f"missing page file: {path.name}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read {path.name}: {exc}")
            continue
        page_texts[scan] = text
        source = without_comments(text)
        scan_macros = re.findall(r"\\scanpage\s*\{\s*([^{}]+?)\s*\}", source)
        if scan_macros != [str(scan)]:
            errors.append(f"{path.name}: expected exactly \\scanpage{{{scan}}}; found {scan_macros!r}")
        if re.search(r"\\(?:documentclass|usepackage)\b|\\begin\s*\{document\}", source):
            errors.append(f"{path.name}: preamble/document wrapper found in fragment")
        warnings.extend(f"{path.name}: {message}" for message in tex_warnings(text))

    combined = root / f"{PACKAGE}_transcription.tex"
    if combined.is_file():
        try:
            actual = combined.read_text(encoding="utf-8")
            expected = "\n".join(page_texts[n] for n in EXPECTED_SCANS if n in page_texts)
            if actual != expected:
                errors.append("combined transcription differs from page files joined in scan order with '\\n'")
            source = without_comments(actual).lstrip()
            if not re.match(r"\\cotefile\s*\{64\}\s*\\scanpage\s*\{116\}", source):
                errors.append("combined transcription does not begin with \\cotefile{64} then \\scanpage{116}")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read combined transcription: {exc}")
    elif not args.partial:
        errors.append(f"missing {combined.name}")

    inventory = root / f"{PACKAGE}_inventory.csv"
    inventory_scans = set()
    inventory_count = 0
    if inventory.is_file():
        try:
            with inventory.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                if reader.fieldnames != INVENTORY_HEADER:
                    errors.append(f"inventory header differs: {reader.fieldnames!r}")
                else:
                    seen_elements = set()
                    for line, row in enumerate(reader, 2):
                        inventory_count += 1
                        if None in row or any(value is None for value in row.values()):
                            errors.append(f"inventory line {line}: wrong number of fields")
                            continue
                        if row["cote"] != "64":
                            errors.append(f"inventory line {line}: unexpected cote {row['cote']!r}")
                        try:
                            scan = int(row["scan"])
                        except ValueError:
                            errors.append(f"inventory line {line}: invalid scan {row['scan']!r}")
                            continue
                        inventory_scans.add(scan)
                        if scan not in EXPECTED_SCANS:
                            errors.append(f"inventory line {line}: unexpected scan {scan}")
                        if row["transcribed"] != "yes":
                            errors.append(f"inventory line {line}: transcribed is not 'yes'")
                        if row["kind"] not in KINDS:
                            errors.append(f"inventory line {line}: unknown kind {row['kind']!r}")
                        if row["sheet_kind"] not in SHEET_KINDS:
                            errors.append(f"inventory line {line}: unknown sheet_kind {row['sheet_kind']!r}")
                        for key in ("element", "position", "first_words_or_objects"):
                            if not row[key].strip():
                                errors.append(f"inventory line {line}: empty {key}")
                        element_key = (scan, row["element"])
                        if element_key in seen_elements:
                            warnings.append(f"inventory line {line}: repeated element identifier {element_key!r}")
                        seen_elements.add(element_key)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"cannot read inventory: {exc}")
        required_scans = set(page_texts) if args.partial else set(EXPECTED_SCANS)
        missing = sorted(required_scans - inventory_scans)
        if missing:
            errors.append(f"scans absent from inventory: {missing}")
        dangling = sorted(inventory_scans - set(page_texts))
        if dangling:
            errors.append(f"inventory scans without readable page files: {dangling}")
    else:
        errors.append(f"missing {inventory.name}")

    events = root / "CHECK_EVENTS.tsv"
    event_count = 0
    if events.is_file():
        try:
            with events.open(encoding="utf-8", newline="") as handle:
                reader = csv.reader(handle, delimiter="\t")
                header = next(reader, None)
                if header != CHECK_EVENTS_HEADER:
                    errors.append(f"CHECK_EVENTS.tsv header differs: {header!r}")
                for line, row in enumerate(reader, 2):
                    event_count += 1
                    if len(row) != len(CHECK_EVENTS_HEADER):
                        errors.append(f"CHECK_EVENTS.tsv line {line}: expected five fields")
                    elif any(not value.strip() for value in row):
                        errors.append(f"CHECK_EVENTS.tsv line {line}: empty event field")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"cannot read CHECK_EVENTS.tsv: {exc}")
    else:
        errors.append("missing CHECK_EVENTS.tsv")

    if not args.partial:
        for name in (f"{PACKAGE}_doubts.md", f"{PACKAGE}_notes.md", "progress.log"):
            path = root / name
            if not path.is_file() or path.stat().st_size == 0:
                errors.append(f"missing or empty required deliverable: {name}")

    checksum_file = root / "SHA256SUMS.txt"
    hash_count = 0
    if checksum_file.is_file():
        try:
            for line, entry in enumerate(checksum_file.read_text(encoding="utf-8").splitlines(), 1):
                if not entry.strip() or entry.lstrip().startswith("#"):
                    continue
                match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", entry)
                if not match:
                    errors.append(f"SHA256SUMS.txt line {line}: expected SHA-256 and filename")
                    continue
                digest, filename = match.groups()
                path = (root / filename).resolve()
                if not path.is_relative_to(root):
                    errors.append(f"SHA256SUMS.txt line {line}: path escapes package directory")
                    continue
                if not path.is_file():
                    errors.append(f"SHA256SUMS.txt line {line}: missing {filename}")
                    continue
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                hash_count += 1
                if actual != digest.lower():
                    errors.append(f"SHA-256 mismatch: {filename}")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot verify SHA256SUMS.txt: {exc}")

    print(f"Pages read: {len(page_texts)}/{len(EXPECTED_SCANS)}")
    print(f"Inventory rows: {inventory_count}; check events: {event_count}; hashes checked: {hash_count}")
    for message in warnings:
        print("WARNING: " + message)
    for message in errors:
        print("ERROR: " + message)
    print(f"Structural validation: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    print("This result does not verify readings, omissions, or scholarly conclusions.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
