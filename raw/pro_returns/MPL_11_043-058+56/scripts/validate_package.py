#!/usr/bin/env python3
"""Check package structure, never assess manuscript readings.

Run after authoring: python scripts/validate_package.py [PACKAGE_DIR] [--partial]
Accepted hash records in progress.log include sha256sum format and records
containing a known relative filename and its 64-digit SHA-256 in either order.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


PREFIX = "MPL_11_043-058+56"
EXPECTED = [(11, n) for n in range(43, 59) if n != 50] + [
    (56, n) for n in range(2, 40) if n not in {10, 19, 34}
]
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}


def page_name(cote: int, scan: int) -> str:
    return f"{PREFIX}_{cote}_scan{scan:03d}.tex"


def escaped(text: str, pos: int) -> bool:
    count = 0
    pos -= 1
    while pos >= 0 and text[pos] == "\\":
        count += 1
        pos -= 1
    return count % 2 == 1


def remove_comments(text: str) -> str:
    """Preserve line count while removing unescaped TeX comments."""
    output = []
    for line in text.splitlines(keepends=True):
        for pos, char in enumerate(line):
            if char == "%" and not escaped(line, pos):
                line = line[:pos] + ("\n" if line.endswith("\n") else "")
                break
        output.append(line)
    return "".join(output)


def brace_errors(text: str) -> list[str]:
    stack: list[int] = []
    errors = []
    line = 1
    clean = remove_comments(text)
    for pos, char in enumerate(clean):
        if char == "\n":
            line += 1
        elif char in "{}" and not escaped(clean, pos):
            if char == "{":
                stack.append(line)
            elif stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at line {line}")
    errors.extend(f"unclosed opening brace at line {n}" for n in stack)
    return errors


def markers(text: str) -> list[tuple[str, int]]:
    clean = remove_comments(text)
    return [
        (match.group(1), int(match.group(2)))
        for match in re.finditer(r"\\(cotefile|scanpage)\s*\{\s*(\d+)\s*\}", clean)
        if not escaped(clean, match.start())
    ]


def compact_boundary_whitespace(text: str) -> str:
    """Only ignore whitespace at file/page boundaries, never inside content."""
    chunks = re.split(r"(?=\\(?:cotefile|scanpage)\s*\{)", text)
    return "\n".join(chunk.strip() for chunk in chunks if chunk.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true",
                        help="Report missing deliverables as incomplete, not errors.")
    args = parser.parse_args()
    root = args.directory.resolve()
    errors: list[str] = []
    incomplete: list[str] = []
    warnings: list[str] = []
    texts: dict[tuple[int, int], str] = {}

    def absent(message: str) -> None:
        (incomplete if args.partial else errors).append(message)

    def read(relative: str) -> str | None:
        path = root / relative
        if not path.is_file():
            absent(f"missing file: {relative}")
            return None
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read {relative}: {exc}")
            return None

    def check_tex(relative: str, text: str) -> None:
        errors.extend(f"{relative}: {e}" for e in brace_errors(text))
        clean = remove_comments(text)
        for match in re.finditer(r"\\(?:includegraphics|include|input|includepdf)\b", clean):
            if not escaped(clean, match.start()):
                errors.append(f"{relative}: prohibited external-content command {match.group()}")
        # Only mechanical placeholder conventions are checked. Ordinary words
        # or uncertainty macros cannot be classified without reading the ink.
        for pattern in [r"\[OCR[^\]]*\]", r"\[TRANSCRIPTION(?:\s+PLACEHOLDER)?\]",
                        r"\[TO\s+BE\s+TRANSCRIBED\]", r"<OCR[^>]*>"]:
            if re.search(pattern, clean, flags=re.IGNORECASE):
                errors.append(f"{relative}: machine/transcription placeholder detected")

    expected_names = {page_name(c, s) for c, s in EXPECTED}
    page_dir = root / "pages"
    if page_dir.is_dir():
        for path in sorted(page_dir.glob("*.tex")):
            if path.name not in expected_names:
                errors.append(f"unexpected page file: pages/{path.name}")
    for cote, scan in EXPECTED:
        relative = f"pages/{page_name(cote, scan)}"
        text = read(relative)
        if text is None:
            continue
        texts[(cote, scan)] = text
        check_tex(relative, text)
        expected_markers = [("scanpage", scan)]
        if (cote, scan) in {(11, 43), (56, 2)}:
            expected_markers.insert(0, ("cotefile", cote))
        found = markers(text)
        if found != expected_markers:
            errors.append(f"{relative}: markers {found!r}; expected {expected_markers!r}")
        clean = remove_comments(text).lstrip()
        if not re.match(r"\\(?:cotefile|scanpage)\s*\{", clean):
            errors.append(f"{relative}: page does not start with its required marker")
        if re.search(r"\\(?:documentclass|begin\s*\{document\}|end\s*\{document\})", clean):
            errors.append(f"{relative}: fragment contains a document wrapper")

    present_keys = [key for key in EXPECTED if key in texts]
    if present_keys and present_keys != EXPECTED[:len(present_keys)]:
        errors.append("available pages do not form a consecutive prefix of the required order")

    combined_name = f"{PREFIX}_transcription.tex"
    combined = read(combined_name)
    if combined is not None:
        check_tex(combined_name, combined)
        expected_combined = "\n\n".join(texts[key].strip() for key in present_keys)
        if compact_boundary_whitespace(combined) != compact_boundary_whitespace(expected_combined):
            errors.append("combined transcription differs from ordered page-file concatenation")
        combined_markers = [item for key in present_keys for item in markers(texts[key])]
        if markers(combined) != combined_markers:
            errors.append("combined transcription markers have incorrect coverage/order")

    inventory_name = f"{PREFIX}_inventory.csv"
    inventory = read(inventory_name)
    inventory_counts: dict[tuple[int, int], int] = {}
    row_count = 0
    if inventory is not None:
        import io
        reader = csv.DictReader(io.StringIO(inventory))
        if reader.fieldnames != COLUMNS:
            errors.append(f"inventory columns {reader.fieldnames!r}; expected {COLUMNS!r}")
        else:
            last_order = -1
            seen_elements: set[tuple[int, int, str]] = set()
            for row_number, row in enumerate(reader, start=2):
                row_count += 1
                label = f"inventory row {row_number}"
                if None in row or any(value is None for value in row.values()):
                    errors.append(f"{label}: malformed CSV row")
                    continue
                try:
                    key = (int(row["cote"]), int(row["scan"]))
                except ValueError:
                    errors.append(f"{label}: cote/scan must be integers")
                    continue
                if key not in EXPECTED:
                    errors.append(f"{label}: unexpected cote/scan {key}")
                    continue
                order = EXPECTED.index(key)
                if order < last_order:
                    errors.append(f"{label}: page rows are out of order")
                last_order = order
                inventory_counts[key] = inventory_counts.get(key, 0) + 1
                element_key = (*key, row["element"])
                if element_key in seen_elements:
                    errors.append(f"{label}: duplicate element identifier on this page")
                seen_elements.add(element_key)
                if not row["element"].strip():
                    errors.append(f"{label}: empty element identifier")
                if row["sheet_kind"] not in SHEET_KINDS:
                    errors.append(f"{label}: invalid sheet_kind {row['sheet_kind']!r}")
                if row["kind"] not in ELEMENT_KINDS:
                    errors.append(f"{label}: invalid kind {row['kind']!r}")
                if row["transcribed"] != "yes":
                    errors.append(f"{label}: transcribed is not yes")
                if key not in texts:
                    errors.append(f"{label}: inventory has no corresponding page file")
            for key in present_keys:
                if key not in inventory_counts:
                    errors.append(f"page {key[0]} scan {key[1]:03d} has no inventory rows")

    for suffix in ("doubts.md", "notes.md"):
        read(f"{PREFIX}_{suffix}")
    log = read("progress.log")
    checked_hashes = 0
    hash_records: dict[str, str] = {}
    known_paths = [f"pages/{page_name(*key)}" for key in EXPECTED] + [combined_name]
    if log is not None:
        for number, line in enumerate(log.splitlines(), start=1):
            digest_match = re.search(r"\b[0-9a-fA-F]{64}\b", line)
            if not digest_match:
                continue
            matches = [path for path in known_paths if path in line]
            if not matches:
                # Also accept page basenames, avoiding double matches.
                matches = [path for path in known_paths if Path(path).name in line]
            if len(matches) != 1:
                warnings.append(f"progress.log line {number}: hash record has no unique known filename")
                continue
            relative = matches[0]
            digest = digest_match.group().lower()
            if relative in hash_records and hash_records[relative] != digest:
                errors.append(f"progress.log: conflicting recorded hashes for {relative}")
            hash_records[relative] = digest
        frozen = bool(re.search(r"^transcription frozen\b", log, flags=re.MULTILINE))
        if frozen:
            for relative in known_paths:
                if relative not in hash_records:
                    errors.append(f"frozen transcription has no hash record for {relative}")
        for relative, recorded in hash_records.items():
            path = root / relative
            if not path.is_file():
                errors.append(f"hash record refers to missing file: {relative}")
                continue
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            checked_hashes += 1
            if actual != recorded:
                errors.append(f"SHA-256 mismatch: {relative}")

    result = {
        "structural_validation_only": True,
        "status": "failed" if errors else ("incomplete" if incomplete else "passed"),
        "directory": str(root),
        "expected_page_count": len(EXPECTED),
        "present_page_count": len(texts),
        "inventory_row_count": row_count,
        "hashes_checked": checked_hashes,
        "errors": errors,
        "incomplete": incomplete,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
