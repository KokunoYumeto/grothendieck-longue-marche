#!/usr/bin/env python3
"""Mechanical checks for MPL_105; does not assess manuscript readings.

Usage: python scripts/validate_package.py [WORK_DIRECTORY]
Canonical assembly is the byte-for-byte concatenation of page files in scan order.
The optional frozen_hashes.json is either {relative_path: sha256} or
{"files": {relative_path: sha256}}; a files list of path/sha256 objects is also
accepted. Paths are relative to WORK_DIRECTORY.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


SCANS = tuple(n for n in range(2, 54) if n not in {9, 24, 29, 42})
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
COMBINED = "MPL_105_transcription.tex"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work_directory", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.work_directory.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    page_paths = [f"pages/MPL_105_105_scan{n:03d}.tex" for n in SCANS]
    expected_pages = {Path(p).name for p in page_paths}
    actual_pages = {p.name for p in (root / "pages").glob("*.tex")}
    for name in sorted(expected_pages - actual_pages):
        errors.append(f"Missing page file: pages/{name}")
    for name in sorted(actual_pages - expected_pages):
        errors.append(f"Unexpected page file: pages/{name}")

    contents: list[bytes] = []
    for scan, relative in zip(SCANS, page_paths):
        path = root / relative
        if not path.is_file():
            continue
        data = path.read_bytes()
        contents.append(data)
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"Not UTF-8: {relative}")
            continue
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", text)
        if markers != [str(scan)] and markers != [f"{scan:03d}"]:
            errors.append(f"Incorrect scanpage markers in {relative}: {markers!r}")
        if not data.endswith(b"\n"):
            warnings.append(f"Page has no final newline: {relative}")
        if re.search(r"\\(?:documentclass|begin\s*\{document\})", text):
            errors.append(f"Page contains a document wrapper: {relative}")

    combined_path = root / COMBINED
    if not combined_path.is_file():
        errors.append(f"Missing combined transcription: {COMBINED}")
    else:
        combined = combined_path.read_bytes()
        if len(contents) == len(SCANS) and combined != b"".join(contents):
            errors.append("Combined transcription is not the exact ordered concatenation of page files")
        if not re.match(rb"\\cotefile\s*\{105\}\s*\\scanpage\s*\{0*2\}", combined):
            errors.append("Combined transcription does not begin with cotefile 105 and scanpage 2")
        if re.search(rb"\\(?:documentclass|begin\s*\{document\})", combined):
            errors.append("Combined transcription contains a document wrapper")

    inventory_path = root / "MPL_105_inventory.csv"
    inventory_scans: set[int] = set()
    inventory_count = 0
    if not inventory_path.is_file():
        errors.append("Missing inventory")
    else:
        try:
            with inventory_path.open(newline="", encoding="utf-8-sig") as stream:
                reader = csv.DictReader(stream)
                if reader.fieldnames != COLUMNS:
                    errors.append(f"Incorrect inventory columns: {reader.fieldnames!r}")
                for number, row in enumerate(reader, 2):
                    inventory_count += 1
                    prefix = f"Inventory row {number}"
                    if None in row or any(row.get(column) is None for column in COLUMNS):
                        errors.append(f"{prefix}: malformed row")
                        continue
                    if row["cote"].strip() != "105":
                        errors.append(f"{prefix}: cote must be 105")
                    try:
                        scan = int(row["scan"])
                        inventory_scans.add(scan)
                        if scan not in SCANS:
                            errors.append(f"{prefix}: unexpected scan {scan}")
                    except ValueError:
                        errors.append(f"{prefix}: invalid scan {row['scan']!r}")
                    if row["transcribed"].strip() != "yes":
                        errors.append(f"{prefix}: transcribed must be yes")
                    if row["kind"].strip() not in KINDS:
                        errors.append(f"{prefix}: invalid element kind {row['kind']!r}")
                    if row["sheet_kind"].strip() not in SHEET_KINDS:
                        errors.append(f"{prefix}: invalid sheet_kind {row['sheet_kind']!r}")
                    for column in ("element", "position", "first_words_or_objects"):
                        if not row[column].strip():
                            errors.append(f"{prefix}: empty {column}")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"Cannot parse inventory: {exc}")
        for scan in sorted(set(SCANS) - inventory_scans):
            errors.append(f"No inventory rows for scan {scan:03d}")

    log_path = root / "progress.log"
    if not log_path.is_file():
        errors.append("Missing progress.log")
    else:
        log = log_path.read_text(encoding="utf-8")
        first_line = log.splitlines()[0] if log.splitlines() else ""
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC", first_line):
            errors.append("First progress.log line is not a UTC timestamp")
        for scan in SCANS:
            if not re.search(rf"(?m)^105 scan {scan:03d} done .+UTC\s*$", log):
                errors.append(f"Missing done log entry for scan {scan:03d}")
            if not re.search(rf"(?m)^scan {scan:03d} audited .+UTC\s*$", log):
                errors.append(f"Missing audit log entry for scan {scan:03d}")
        if not re.search(r"(?m)^transcription frozen .+UTC\s*$", log):
            errors.append("Missing transcription frozen log entry")

    for relative in ("MPL_105_doubts.md", "MPL_105_notes.md"):
        path = root / relative
        if not path.is_file() or not path.stat().st_size:
            errors.append(f"Missing or empty deliverable: {relative}")

    freeze_path = root / "records/frozen_hashes.json"
    hash_count = 0
    if freeze_path.exists():
        try:
            frozen = json.loads(freeze_path.read_text(encoding="utf-8"))
            entries = frozen.get("files", frozen) if isinstance(frozen, dict) else frozen
            if isinstance(entries, list):
                entries = {entry["path"]: entry["sha256"] for entry in entries}
            if not isinstance(entries, dict):
                raise ValueError("Expected a filename-to-SHA-256 mapping or a files list")
            for relative in page_paths + [COMBINED]:
                if relative not in entries:
                    errors.append(f"Frozen hash missing: {relative}")
            for relative, digest in entries.items():
                if not isinstance(relative, str) or not isinstance(digest, str):
                    raise ValueError("Hash paths and digests must be strings")
                path = (root / relative).resolve()
                if not path.is_relative_to(root):
                    errors.append(f"Frozen hash path escapes work directory: {relative}")
                    continue
                if not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
                    errors.append(f"Invalid SHA-256 digest: {relative}")
                elif not path.is_file():
                    errors.append(f"Frozen file missing: {relative}")
                elif hashlib.sha256(path.read_bytes()).hexdigest() != digest.lower():
                    errors.append(f"Frozen SHA-256 mismatch: {relative}")
                else:
                    hash_count += 1
        except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"Cannot validate frozen hashes: {exc}")
    else:
        warnings.append("No records/frozen_hashes.json; hash verification was not performed")

    print(json.dumps({
        "ok": not errors, "expected_pages": len(SCANS),
        "present_page_files": len(actual_pages), "inventory_rows": inventory_count,
        "verified_hashes": hash_count, "errors": errors, "warnings": warnings,
    }, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
