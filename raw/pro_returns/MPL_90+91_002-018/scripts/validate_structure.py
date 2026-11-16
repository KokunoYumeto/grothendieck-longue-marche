#!/usr/bin/env python3
"""Check the structure (never the readings) of MPL_90+91_002-018.

Uses Python's standard library only. It never opens scan images or context.
The TeX checks are deliberately lexical, not a TeX compiler or semantic audit.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


PREFIX = "MPL_90+91_002-018"
EXPECTED = [(90, n) for n in range(2, 26)] + [
    (91, n) for n in range(2, 19) if n not in (4, 15)
]
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion",
    "deletion",
}
PAGE_NAME = re.compile(re.escape(PREFIX) + r"_(\d+)_scan(\d{3})\.tex\Z")
FORBIDDEN_COMMANDS = re.compile(
    r"\\(?:documentclass|usepackage|RequirePackage|includegraphics|includepdf|"
    r"pgfimage|epsfig|psfig|pdfximage|pdfrefximage|includestandalone)\b"
    r"|\\(?:begin|end)\s*\{document\}"
)
PLACEHOLDERS = re.compile(
    r"\[\s*(?:\.{3}|…)\s*\]"
    r"|<\s*(?:TODO|TBD|PLACEHOLDER|INSERT\b[^>]*)\s*>"
    r"|\b(?:TODO|TBD|FIXME)\b"
)


def filename(key: tuple[int, int]) -> str:
    return f"{PREFIX}_{key[0]}_scan{key[1]:03d}.tex"


def unescaped(text: str, index: int) -> bool:
    """A special character is escaped iff preceded by an odd slash run."""
    preceding = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        preceding += 1
        index -= 1
    return preceding % 2 == 0


def without_comments(text: str) -> str:
    """Blank comments while retaining offsets and line numbers."""
    chars = list(text)
    comment = False
    for index, char in enumerate(text):
        if char == "\n":
            comment = False
        elif comment:
            chars[index] = " "
        elif char == "%" and unescaped(text, index):
            chars[index] = " "
            comment = True
    return "".join(chars)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def brace_errors(text: str) -> list[str]:
    stack: list[int] = []
    errors: list[str] = []
    for index, char in enumerate(text):
        if char not in "{}" or not unescaped(text, index):
            continue
        if char == "{":
            stack.append(index)
        elif not stack:
            errors.append(f"unmatched closing brace at line {line_number(text, index)}")
        else:
            stack.pop()
    for index in stack:
        errors.append(f"unclosed opening brace at line {line_number(text, index)}")
    return errors


def command_arguments(text: str, command: str) -> tuple[list[str], int]:
    """Return balanced braced arguments and count lexical occurrences.

    Nested doubt macros are valid, for example mspage{unsure{1|7}}.
    """
    start = re.compile(r"\\" + command + r"\b")
    occurrences = list(start.finditer(text))
    arguments: list[str] = []
    for match in occurrences:
        index = match.end()
        while index < len(text) and text[index].isspace():
            index += 1
        if index >= len(text) or text[index] != "{":
            continue
        begin = index + 1
        depth = 1
        index += 1
        while index < len(text) and depth:
            if unescaped(text, index):
                if text[index] == "{":
                    depth += 1
                elif text[index] == "}":
                    depth -= 1
            if not depth:
                arguments.append(text[begin:index].strip())
                break
            index += 1
    return arguments, len(occurrences)


def validate(root: Path, partial: bool) -> tuple[list[str], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    facts: list[str] = []
    pages_dir = root / "pages"
    page_bytes: dict[tuple[int, int], bytes] = {}
    page_text: dict[tuple[int, int], str] = {}

    if not pages_dir.is_dir():
        errors.append(f"Missing page directory: {pages_dir}")
        return errors, warnings, facts

    for path in sorted(pages_dir.glob("*.tex")):
        match = PAGE_NAME.fullmatch(path.name)
        if not match:
            errors.append(f"Unexpected page filename: {path.name}")
            continue
        key = int(match.group(1)), int(match.group(2))
        if key not in EXPECTED:
            errors.append(f"Unexpected page: {path.name}")
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.name}: invalid UTF-8 ({exc})")
            continue
        page_bytes[key] = raw
        page_text[key] = text

    present = [key for key in EXPECTED if key in page_bytes]
    missing = [key for key in EXPECTED if key not in page_bytes]
    if partial:
        if present != EXPECTED[:len(present)]:
            errors.append("Partial pages are not a consecutive prefix of the required order.")
        facts.append(f"Partial mode: {len(present)}/39 expected page files present.")
    elif missing:
        errors.append("Missing pages: " + ", ".join(filename(key) for key in missing))
    facts.append(f"Page count: {len(present)} (expected 39 in final mode).")

    manuscript_markers = 0
    for key in present:
        name = filename(key)
        original = page_text[key]
        clean = without_comments(original)
        if not clean.strip():
            errors.append(f"{name}: empty page.")
        errors.extend(f"{name}: {message}" for message in brace_errors(clean))
        scans, scan_count = command_arguments(clean, "scanpage")
        if scan_count != 1 or scans != [str(key[1])]:
            errors.append(
                f"{name}: expected exactly \\scanpage{{{key[1]}}}; "
                f"found {scan_count} command(s), arguments {scans!r}."
            )
        cotes, cote_count = command_arguments(clean, "cotefile")
        expected_cotes = [str(key[0])] if key[1] == 2 else []
        if cotes != expected_cotes or cote_count != len(expected_cotes):
            errors.append(f"{name}: expected cotefile arguments {expected_cotes!r}; got {cotes!r}.")
        opening = clean.lstrip()
        expected_opening = (
            rf"\\cotefile\s*\{{{key[0]}\}}\s*\\scanpage\s*\{{{key[1]}\}}"
            if expected_cotes else rf"\\scanpage\s*\{{{key[1]}\}}"
        )
        if not re.match(expected_opening, opening):
            errors.append(f"{name}: page does not start with the required cote/scan marker(s).")
        ms_pages, ms_count = command_arguments(clean, "mspage")
        manuscript_markers += ms_count
        if len(ms_pages) != ms_count or any(not item for item in ms_pages):
            errors.append(f"{name}: malformed or empty mspage marker.")
        for match in FORBIDDEN_COMMANDS.finditer(clean):
            errors.append(
                f"{name}:{line_number(clean, match.start())}: forbidden preamble/image command "
                f"{match.group(0)!r}."
            )
        for match in PLACEHOLDERS.finditer(clean):
            errors.append(
                f"{name}:{line_number(clean, match.start())}: possible literal placeholder "
                f"{match.group(0)!r}; inspect manually."
            )

    facts.append(f"Manuscript page markers found: {manuscript_markers} (presence is not inferred).")
    combined_path = root / f"{PREFIX}_transcription.tex"
    if combined_path.exists():
        combined = combined_path.read_bytes()
        expected_combined = b"".join(page_bytes[key] for key in present)
        if combined != expected_combined:
            errors.append("Combined transcription is not the exact ordered byte concatenation of page files.")
        else:
            facts.append("Combined transcription exactly matches ordered page-file bytes.")
    elif partial:
        warnings.append("Combined transcription not yet present (permitted in partial mode).")
    else:
        errors.append(f"Missing combined transcription: {combined_path.name}")

    inventory_path = root / f"{PREFIX}_inventory.csv"
    covered: set[tuple[int, int]] = set()
    element_ids: set[tuple[int, int, str]] = set()
    row_count = 0
    if inventory_path.exists():
        try:
            with inventory_path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                if reader.fieldnames != COLUMNS:
                    errors.append(f"Inventory header must be exactly {COLUMNS!r}; got {reader.fieldnames!r}.")
                else:
                    for row_no, row in enumerate(reader, 2):
                        row_count += 1
                        label = f"Inventory row {row_no}"
                        if None in row or any(value is None for value in row.values()):
                            errors.append(f"{label}: wrong number of CSV fields.")
                            continue
                        try:
                            key = int(row["cote"]), int(row["scan"])
                        except ValueError:
                            errors.append(f"{label}: cote and scan must be integers.")
                            continue
                        if key not in EXPECTED:
                            errors.append(f"{label}: unexpected cote/scan {key!r}.")
                        elif key not in page_bytes:
                            errors.append(f"{label}: inventory refers to a missing page file {filename(key)}.")
                        else:
                            covered.add(key)
                        if row["transcribed"] != "yes":
                            errors.append(f"{label}: transcribed must be exactly 'yes'.")
                        if row["sheet_kind"] not in SHEET_KINDS:
                            errors.append(f"{label}: invalid sheet_kind {row['sheet_kind']!r}.")
                        if row["kind"] not in ELEMENT_KINDS:
                            errors.append(f"{label}: invalid kind {row['kind']!r}.")
                        for field in ("element", "position", "first_words_or_objects"):
                            if not row[field].strip():
                                errors.append(f"{label}: empty {field}.")
                        element_key = key + (row["element"],)
                        if element_key in element_ids:
                            errors.append(f"{label}: duplicate element identifier {element_key!r}.")
                        element_ids.add(element_key)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"Cannot read inventory: {exc}")
        for key in present:
            if key not in covered:
                errors.append(f"No inventory element for {filename(key)}.")
        facts.append(f"Inventory: {row_count} element rows covering {len(covered)} pages.")
    elif partial and not present:
        warnings.append("Inventory not yet present (permitted before the first completed page).")
    else:
        errors.append(f"Missing inventory: {inventory_path.name}")

    if not partial:
        for name in (f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md", "progress.log"):
            path = root / name
            if not path.is_file() or path.stat().st_size == 0:
                errors.append(f"Missing or empty required file: {name}")

    warnings.append(
        "Structural checks cannot establish faithful readings, completeness of page elements, "
        "correct diagrams, appropriate doubt marks, visual audits, or research quality."
    )
    warnings.append(
        "Brace/command checks are lexical: escaped braces and TeX comments are handled, "
        "but verbatim, catcode changes, and arbitrary macro expansion are not interpreted."
    )
    return errors, warnings, facts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Package directory (default: script's parent package directory)")
    parser.add_argument("--partial", action="store_true", help="Validate a consecutive completed prefix")
    parser.add_argument("--report", type=Path, help="Also write the plain-text report to this path")
    args = parser.parse_args()
    errors, warnings, facts = validate(args.root, args.partial)
    lines = ["STRUCTURAL VALIDATION: " + ("FAIL" if errors else "PASS")]
    lines += ["INFO: " + item for item in facts]
    lines += ["ERROR: " + item for item in errors]
    lines += ["NOTE: " + item for item in warnings]
    report = "\n".join(lines) + "\n"
    print(report, end="")
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
