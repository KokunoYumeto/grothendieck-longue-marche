#!/usr/bin/env python3
"""Report structural checks without modifying manuscript or package files.

The combined fragment is defined as the literal byte concatenation of the
34 ordered page files. No whitespace normalization is performed.

Accepted freeze-manifest formats:
    {"files": {"pages/name.tex": "<sha256>", ...}}
    {"pages/name.tex": "<sha256>", ...}
The manifest must cover every page and the combined transcription.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path


STEM = "MPL_60_002-035"
SCANS = tuple(range(2, 36))
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}


def uncomment(text: str) -> str:
    """Remove unescaped TeX comments while preserving line count."""
    lines = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for i, char in enumerate(line):
            if char != "%":
                continue
            slashes = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                slashes += 1
                j -= 1
            if slashes % 2 == 0:
                cut = i
                break
        lines.append(line[:cut] + ("\n" if cut < len(line) and line.endswith("\n") else ""))
    return "".join(lines)


def brace_errors(text: str) -> list[str]:
    """Check grouping braces, excluding comments and literal \\{ / \\}."""
    clean = uncomment(text)
    stack: list[int] = []
    problems: list[str] = []
    line = 1
    slash_run = 0
    for char in clean:
        if char == "\n":
            line += 1
        if char == "\\":
            slash_run += 1
            continue
        escaped = slash_run % 2 == 1
        slash_run = 0
        if escaped:
            continue
        if char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                problems.append(f"unmatched closing brace at line {line}")
    problems.extend(f"unmatched opening brace at line {n}" for n in stack)
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root", nargs="?", type=Path,
        default=Path(__file__).resolve().parents[1],
        help="deliverable directory (default: parent of scripts/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    expected = {
        scan: root / "pages" / f"{STEM}_60_scan{scan:03d}.tex" for scan in SCANS
    }
    required = [
        root / f"{STEM}_transcription.tex",
        root / f"{STEM}_doubts.md",
        root / f"{STEM}_inventory.csv",
        root / f"{STEM}_notes.md",
        root / "progress.log",
    ]
    for path in [*required, *expected.values()]:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(root)}")
        elif path.stat().st_size == 0:
            errors.append(f"empty required file: {path.relative_to(root)}")

    actual_pages = set((root / "pages").glob("*.tex"))
    for path in sorted(actual_pages - set(expected.values())):
        errors.append(f"unexpected page filename: {path.relative_to(root)}")

    page_bytes: list[bytes] = []
    pages_read = 0
    for scan, path in expected.items():
        if not path.is_file():
            continue
        raw = path.read_bytes()
        page_bytes.append(raw)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.name}: not UTF-8 ({exc})")
            continue
        pages_read += 1
        clean = uncomment(text)
        headers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if len(headers) != 1 or int(headers[0]) != scan:
            errors.append(f"{path.name}: expected one scanpage{{{scan}}}; found {headers}")
        if scan == 2:
            prefix = r"\A\s*\\cotefile\s*\{\s*60\s*\}\s*\\scanpage\s*\{\s*0*2\s*\}"
            if not re.search(prefix, clean):
                errors.append(f"{path.name}: first page must start with cotefile{{60}}, scanpage{{2}}")
        else:
            prefix = rf"\A\s*\\scanpage\s*\{{\s*0*{scan}\s*\}}"
            if not re.search(prefix, clean):
                errors.append(f"{path.name}: page does not begin with its scanpage header")
        for issue in brace_errors(text):
            errors.append(f"{path.name}: {issue}")

    combined = required[0]
    if combined.is_file():
        raw = combined.read_bytes()
        if len(page_bytes) == len(SCANS) and raw != b"".join(page_bytes):
            errors.append("combined transcription differs from literal ordered page-file concatenation")
        try:
            combined_text = raw.decode("utf-8")
            for issue in brace_errors(combined_text):
                errors.append(f"{combined.name}: {issue}")
            combined_scans = [int(x) for x in re.findall(
                r"\\scanpage\s*\{\s*(\d+)\s*\}", uncomment(combined_text)
            )]
            if combined_scans != list(SCANS):
                errors.append(f"combined scan order is {combined_scans}, expected 2 through 35")
        except UnicodeDecodeError as exc:
            errors.append(f"{combined.name}: not UTF-8 ({exc})")

    inventory = required[2]
    counts = {n: 0 for n in SCANS}
    seen_elements: set[tuple[int, str]] = set()
    inventory_rows = 0
    if inventory.is_file():
        try:
            reader = csv.DictReader(io.StringIO(inventory.read_text(encoding="utf-8-sig"), newline=""))
            if reader.fieldnames != COLUMNS:
                errors.append(f"inventory header mismatch: {reader.fieldnames}")
            for lineno, row in enumerate(reader, start=2):
                inventory_rows += 1
                if None in row or any(value is None for value in row.values()):
                    errors.append(f"inventory row {lineno}: malformed column count")
                    continue
                try:
                    scan = int(row.get("scan", ""))
                except ValueError:
                    errors.append(f"inventory row {lineno}: invalid scan {row.get('scan')!r}")
                    continue
                if scan not in counts:
                    errors.append(f"inventory row {lineno}: unexpected scan {scan}")
                else:
                    counts[scan] += 1
                if row.get("cote") != "60":
                    errors.append(f"inventory row {lineno}: cote must be 60")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"inventory row {lineno}: invalid sheet_kind {row.get('sheet_kind')!r}")
                if row.get("kind") not in ELEMENT_KINDS:
                    errors.append(f"inventory row {lineno}: invalid kind {row.get('kind')!r}")
                if row.get("transcribed") != "yes":
                    errors.append(f"inventory row {lineno}: transcribed is not yes")
                for key in ("element", "position", "first_words_or_objects"):
                    if not row.get(key, "").strip():
                        errors.append(f"inventory row {lineno}: {key} is blank")
                identity = (scan, row.get("element", ""))
                if identity in seen_elements:
                    errors.append(f"inventory row {lineno}: duplicate element {identity}")
                seen_elements.add(identity)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"cannot read inventory: {exc}")
        for scan, count in counts.items():
            if not count:
                errors.append(f"inventory has no elements for scan {scan:03d}")

    manifest = root / "records" / "frozen_hashes.json"
    hashes_verified = 0
    if manifest.is_file():
        try:
            obj = json.loads(manifest.read_text(encoding="utf-8"))
            entries = obj.get("files", obj) if isinstance(obj, dict) else None
            if not isinstance(entries, dict):
                raise ValueError("expected an object mapping relative paths to SHA-256 strings")
            expected_hash_paths = {
                str(path.relative_to(root)) for path in [*expected.values(), combined]
            }
            for relative in sorted(expected_hash_paths - set(entries)):
                errors.append(f"frozen manifest omits {relative}")
            for relative, digest in entries.items():
                if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
                    errors.append(f"invalid frozen SHA-256 for {relative!r}")
                    continue
                path = (root / relative).resolve()
                if not path.is_relative_to(root):
                    errors.append(f"frozen manifest path leaves package root: {relative!r}")
                    continue
                if not path.is_file():
                    errors.append(f"frozen file is missing: {relative}")
                    continue
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                if actual != digest.lower():
                    errors.append(f"frozen SHA-256 changed: {relative}")
                else:
                    hashes_verified += 1
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            errors.append(f"cannot validate frozen manifest: {exc}")
    else:
        warnings.append("records/frozen_hashes.json is absent; frozen hashes were not checked")

    print(f"Package: {root}")
    print(f"Page files read: {pages_read}/34")
    print(f"Inventory elements: {inventory_rows}")
    print(f"Frozen files verified: {hashes_verified}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print("STRUCTURAL VALIDATION: " + ("FAIL" if errors else "PASS"))
    print("This check does not assess paleographic accuracy or visual completeness.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
