#!/usr/bin/env python3
"""Read-only structural checks for the MPL_116+117 transcription package.

This script does not perform OCR, assess handwriting, or certify visual
completeness. It checks files, markers, inventory, and recorded SHA-256 values.
The combined TeX fragment must be the exact byte concatenation of the page
files in manuscript order, with any separators already in the page files.

Usage:
    python validate_package.py WORK_DIRECTORY --partial
    python validate_package.py WORK_DIRECTORY
    python validate_package.py WORK_DIRECTORY --final

Hash log lines should contain the exact artifact filename and its 64-character
SHA-256 digest, e.g.:
    sha256 pages/MPL_116+117_116_scan002.tex <digest>

Audit log lines may carry the cote (recommended), e.g.:
    116 scan 002 audited 2026-11-17 18:00:00 UTC
When the cote is omitted, audit records must follow the complete page order.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

PREFIX = "MPL_116+117"
EXPECTED = [(116, n) for n in (*range(2, 9), 10, 11)] + [(117, n) for n in range(2, 27)]
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
PAGE_RE = re.compile(r"^MPL_116\+117_(116|117)_scan(\d{3})\.tex$")
SHA_RE = re.compile(r"(?<![0-9A-Fa-f])[0-9A-Fa-f]{64}(?![0-9A-Fa-f])")


def filename(cote: int, scan: int) -> str:
    return f"{PREFIX}_{cote}_scan{scan:03d}.tex"


def remove_comments(text: str) -> str:
    """Strip TeX comments, preserving line numbers and escaped percent signs."""
    lines = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for index, char in enumerate(line):
            if char != "%":
                continue
            slash_count = 0
            back = index - 1
            while back >= 0 and line[back] == "\\":
                slash_count += 1
                back -= 1
            if slash_count % 2 == 0:
                cut = index
                break
        clean = line[:cut]
        if cut < len(line) and line.endswith("\n"):
            clean += "\n"
        lines.append(clean)
    return "".join(lines)


def brace_errors(text: str) -> list[str]:
    """Check unescaped TeX braces, excluding comments and control symbols."""
    clean = remove_comments(text)
    stack: list[int] = []
    errors: list[str] = []
    index = 0
    line = 1
    while index < len(clean):
        char = clean[index]
        if char == "\n":
            line += 1
        elif char == "\\":
            # A TeX control symbol consumes its following non-letter character;
            # this handles escaped braces, %, and doubled backslashes correctly.
            if index + 1 < len(clean) and not clean[index + 1].isalpha():
                if clean[index + 1] == "\n":
                    line += 1
                index += 2
                continue
        elif char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace on line {line}")
        index += 1
    for opening_line in stack:
        errors.append(f"unclosed opening brace on line {opening_line}")
    return errors


def read_text(path: Path, errors: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read {path.name}: {exc}")
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("work_directory", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--partial", action="store_true", help="Allow an unfinished sequential prefix of pages and optional combined file.")
    mode.add_argument("--final", action="store_true", help="Also require audits, freeze hashes, context-open order, final hash verification, and all deliverables.")
    args = parser.parse_args()
    root = args.work_directory.resolve()
    errors: list[str] = []
    notices: list[str] = []
    if not root.is_dir():
        print(f"ERROR: Work directory does not exist: {root}")
        return 2

    page_dir = root / "pages"
    actual_paths = sorted(page_dir.glob("*.tex")) if page_dir.is_dir() else []
    expected_names = {filename(*page) for page in EXPECTED}
    extra = [path.name for path in actual_paths if path.name not in expected_names]
    if extra:
        errors.append("Unexpected page filenames: " + ", ".join(extra))
    available = [page for page in EXPECTED if (page_dir / filename(*page)).is_file()]
    missing = [page for page in EXPECTED if page not in available]
    if args.partial:
        if available != EXPECTED[:len(available)]:
            errors.append("Present pages are not a sequential prefix of the required page order.")
    elif missing:
        errors.append("Missing pages: " + ", ".join(f"{c}/{s:03d}" for c, s in missing))

    page_bytes: list[bytes] = []
    for cote, scan in available:
        path = page_dir / filename(cote, scan)
        text = read_text(path, errors)
        if text is None:
            continue
        page_bytes.append(path.read_bytes())
        clean = remove_comments(text)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if markers != [str(scan)]:
            errors.append(f"{path.name}: expected one scanpage{{{scan}}}, found {markers}.")
        cotes = re.findall(r"\\cotefile\s*\{\s*(\d+)\s*\}", clean)
        required_cotes = [str(cote)] if scan == 2 else []
        if cotes != required_cotes:
            errors.append(f"{path.name}: expected cotefile markers {required_cotes}, found {cotes}.")
        start = re.compile(
            (rf"\s*\\cotefile\s*\{{\s*{cote}\s*\}}\s*" if scan == 2 else r"\s*")
            + rf"\\scanpage\s*\{{\s*{scan}\s*\}}"
        )
        if not start.match(clean):
            errors.append(f"{path.name}: page does not begin with its required cote/scan markers.")
        errors.extend(f"{path.name}: {issue}." for issue in brace_errors(text))

    combined = root / f"{PREFIX}_transcription.tex"
    if combined.is_file():
        if combined.read_bytes() != b"".join(page_bytes):
            errors.append(f"{combined.name}: not the exact byte concatenation of present page files in required order.")
    elif not args.partial:
        errors.append(f"Missing {combined.name}.")
    else:
        notices.append("Combined transcription has not yet been created.")

    inventory = root / f"{PREFIX}_inventory.csv"
    rows: list[dict[str, str]] = []
    covered: set[tuple[int, int]] = set()
    if inventory.is_file():
        try:
            with inventory.open(newline="", encoding="utf-8-sig") as handle:
                reader = csv.DictReader(handle)
                if reader.fieldnames != COLUMNS:
                    errors.append(f"Inventory columns must be exactly {COLUMNS}; found {reader.fieldnames}.")
                rows = list(reader)
            for row_number, row in enumerate(rows, 2):
                label = f"Inventory row {row_number}"
                if None in row:
                    errors.append(f"{label}: extra fields (possibly an unquoted comma).")
                try:
                    page = (int(row.get("cote", "")), int(row.get("scan", "")))
                except (TypeError, ValueError):
                    errors.append(f"{label}: invalid cote or scan.")
                    continue
                covered.add(page)
                if page not in EXPECTED:
                    errors.append(f"{label}: unexpected page {page}.")
                elif page not in available:
                    errors.append(f"{label}: page file has not been saved for {page}.")
                if row.get("transcribed") != "yes":
                    errors.append(f"{label}: transcribed must be exactly 'yes'.")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"{label}: invalid sheet_kind {row.get('sheet_kind')!r}.")
                if row.get("kind") not in ELEMENT_KINDS:
                    errors.append(f"{label}: invalid kind {row.get('kind')!r}.")
                for field in ("element", "position", "first_words_or_objects"):
                    if not (row.get(field) or "").strip():
                        errors.append(f"{label}: empty {field}.")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"Cannot read inventory: {exc}")
    elif available or not args.partial:
        errors.append(f"Missing {inventory.name}.")
    uncovered = [page for page in available if page not in covered]
    if uncovered:
        errors.append("No inventory rows for saved pages: " + ", ".join(f"{c}/{s:03d}" for c, s in uncovered))

    log_path = root / "progress.log"
    log = read_text(log_path, errors) if log_path.is_file() else None
    if log is None:
        errors.append("Missing or unreadable progress.log.")
    else:
        lines = log.splitlines()
        if not lines:
            errors.append("progress.log is empty.")
        else:
            try:
                datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S UTC")
            except ValueError:
                errors.append("progress.log must start with a UTC timestamp in YYYY-MM-DD HH:MM:SS UTC form.")
        done = [(int(c), int(s)) for c, s in re.findall(r"^\s*(116|117)\s+scan\s+(\d+)\s+done\b", log, flags=re.MULTILINE)]
        if done != available:
            errors.append("Page-done log records must match the saved pages exactly, in required order.")

        if args.final:
            for name in (f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md"):
                path = root / name
                if not path.is_file() or path.stat().st_size == 0:
                    errors.append(f"Missing or empty final deliverable {name}.")

            audit_records = []
            for line_number, line in enumerate(lines):
                match = re.match(r"\s*(?:(116|117)\s+)?scan\s+(\d+)\s+audited\b", line)
                if match:
                    audit_records.append((int(match[1]) if match[1] else None, int(match[2]), line_number))
            if len(audit_records) != len(EXPECTED):
                errors.append(f"Expected 34 page audit records, found {len(audit_records)}.")
            for index, (cote, scan, _) in enumerate(audit_records[:len(EXPECTED)]):
                expected_cote, expected_scan = EXPECTED[index]
                if scan != expected_scan or (cote is not None and cote != expected_cote):
                    errors.append(f"Audit record {index + 1}: expected {expected_cote}/{expected_scan:03d}, found {cote or 'unspecified'}/{scan:03d}.")

            freeze_indices = [i for i, line in enumerate(lines) if re.match(r"\s*transcription frozen\b", line)]
            context_indices = [i for i, line in enumerate(lines) if re.match(r"\s*context opened\b", line)]
            if len(freeze_indices) != 1:
                errors.append(f"Expected exactly one 'transcription frozen' record, found {len(freeze_indices)}.")
            if len(context_indices) != 1:
                errors.append(f"Expected exactly one 'context opened' record, found {len(context_indices)}.")
            if freeze_indices and audit_records and max(record[2] for record in audit_records) >= freeze_indices[0]:
                errors.append("All page audit records must precede transcription frozen.")
            if freeze_indices and context_indices and freeze_indices[0] >= context_indices[0]:
                errors.append("Transcription must be frozen before context opened.")

            artifacts = [page_dir / filename(*page) for page in EXPECTED] + [combined]
            for artifact in artifacts:
                if not artifact.is_file():
                    continue
                hash_lines = [(i, line) for i, line in enumerate(lines) if artifact.name in line and SHA_RE.search(line)]
                if not hash_lines:
                    errors.append(f"No SHA-256 log record for {artifact.name}.")
                    continue
                digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
                first_index, first_line = hash_lines[0]
                recorded_digests = [match.group(0).lower() for match in SHA_RE.finditer(first_line)]
                if digest not in recorded_digests:
                    errors.append(f"SHA-256 mismatch against first recorded digest for {artifact.name}.")
                if context_indices and first_index >= context_indices[0]:
                    errors.append(f"First SHA-256 for {artifact.name} was recorded after context opened.")

            # Require an explicit after-context verification statement, while
            # allowing the transcriber to phrase it naturally in English.
            verified = [i for i, line in enumerate(lines) if (
                re.search(r"(?:hash(?:es)?|sha-?256)", line, re.IGNORECASE)
                and re.search(r"(?:unchanged|verified|match(?:es|ed)?|verification.*(?:pass|success))", line, re.IGNORECASE)
            )]
            if not verified:
                errors.append("Missing final explicit hash-verification/unchanged record.")
            elif context_indices and max(verified) <= context_indices[0]:
                errors.append("Final hash verification must be recorded after context opened.")

    print(f"Pages saved: {len(available)}/34")
    print(f"Inventory: {len(rows)} element rows; {len(covered)} pages represented")
    print(f"Mode: {'partial' if args.partial else 'final' if args.final else 'complete structural'}")
    for notice in notices:
        print("NOTE: " + notice)
    if errors:
        print(f"FAILED: {len(errors)} structural issue(s)")
        for error in errors:
            print("ERROR: " + error)
        return 1
    print("PASS: requested structural checks succeeded.")
    print("Visual completeness and accuracy remain the responsibility of the manuscript reader.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
