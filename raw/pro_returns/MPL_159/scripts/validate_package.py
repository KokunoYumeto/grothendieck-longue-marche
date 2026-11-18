#!/usr/bin/env python3
"""Structural validation of MPL_159 deliverables; no OCR or semantic review.

Run from any directory:
    python scripts/validate_package.py
    python scripts/validate_package.py --partial

The default package root is the directory above scripts/.  This script does
not open source images, source archives, or extracted context.  It reads only
deliverable files to check their structure and byte-level consistency.  Passing
these checks cannot certify that a transcription accurately represents ink.

Canonical progress-log hash syntax:
    sha256 pages/MPL_159_159_scan001.tex <64 hexadecimal characters>
    sha256 MPL_159_transcription.tex <64 hexadecimal characters>
    transcription frozen YYYY-MM-DD HH:MM:SS UTC
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys


SCANS = tuple(n for n in range(1, 35) if n not in (14, 24))
INVENTORY_FIELDS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion",
    "deletion",
}
REQUIRED = (
    "MPL_159_transcription.tex", "MPL_159_doubts.md",
    "MPL_159_inventory.csv", "MPL_159_notes.md", "progress.log",
    "CHECK_EVENTS.tsv",
)
TIME_PATTERN = (
    r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}"
    r"(?:\.\d+)?(?: UTC|Z|\+00:00)"
)


def uncomment(text: str) -> str:
    """Remove TeX comments without treating escaped percent signs as comments."""
    result = []
    for line in text.splitlines():
        for i, char in enumerate(line):
            if char != "%":
                continue
            slashes = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                slashes += 1
                j -= 1
            if slashes % 2 == 0:
                line = line[:i]
                break
        result.append(line)
    return "\n".join(result)


def validate(root: Path, partial: bool = False) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    details: dict = {"root": str(root), "partial": partial}

    def error(message: str) -> None:
        errors.append(message)

    def read(relative: str, required: bool = True) -> str | None:
        path = root / relative
        if not path.is_file():
            if required:
                error(f"Missing file: {relative}")
            return None
        try:
            return path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            error(f"Cannot read UTF-8 file {relative}: {exc}")
            return None

    for relative in REQUIRED:
        if not (root / relative).is_file() and not partial:
            error(f"Missing required deliverable: {relative}")

    expected_paths = {
        f"pages/MPL_159_159_scan{n:03d}.tex": n for n in SCANS
    }
    actual_paths = {
        str(path.relative_to(root))
        for path in (root / "pages").glob("*.tex")
    }
    unexpected = sorted(actual_paths - set(expected_paths))
    for relative in unexpected:
        error(f"Unexpected page file: {relative}")
    missing = sorted(set(expected_paths) - actual_paths)
    if missing and not partial:
        error("Missing page files: " + ", ".join(missing))

    pages: dict[int, bytes] = {}
    for relative, scan in expected_paths.items():
        if relative not in actual_paths:
            continue
        text = read(relative)
        if text is None:
            continue
        body = uncomment(text)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", body)
        if markers != [str(scan)]:
            error(f"{relative}: expected exactly scan marker {scan}; found {markers}")
        if scan == 1 and not re.match(
            r"\s*\\cotefile\{159\}\s*\\scanpage\{1\}", body
        ):
            error(f"{relative}: must start with cotefile 159 and scanpage 1")
        if re.search(r"\\(?:documentclass|begin\{document\}|end\{document\})", body):
            error(f"{relative}: contains a document wrapper; fragment required")
        pages[scan] = (root / relative).read_bytes()
    details["page_count"] = len(pages)
    details["expected_page_count"] = len(SCANS)

    combined_path = root / "MPL_159_transcription.tex"
    if combined_path.is_file():
        combined = combined_path.read_bytes()
        ordered = [pages[n] for n in SCANS if n in pages]
        direct = b"".join(ordered)
        separated = b"\n".join(ordered)
        if combined == direct:
            details["concatenation"] = "exact direct concatenation"
        elif combined == separated:
            details["concatenation"] = "exact newline-separated concatenation"
        else:
            error("Combined transcription differs from exact ordered concatenation of page files")
        combined_text = read("MPL_159_transcription.tex")
        if combined_text is not None:
            markers = [int(n) for n in re.findall(
                r"\\scanpage\s*\{\s*(\d+)\s*\}", uncomment(combined_text)
            )]
            expected_markers = [n for n in SCANS if n in pages]
            if markers != expected_markers:
                error("Combined transcription scan markers are missing, duplicated, or out of order")

    inventory = read("MPL_159_inventory.csv", required=not partial)
    inventory_scans: set[int] = set()
    if inventory is not None:
        reader = csv.DictReader(io.StringIO(inventory))
        if reader.fieldnames != INVENTORY_FIELDS:
            error(f"Inventory columns must be exactly {INVENTORY_FIELDS}")
        seen_elements: set[tuple[str, int, str]] = set()
        row_count = 0
        for line, row in enumerate(reader, 2):
            row_count += 1
            if None in row:
                error(f"Inventory line {line}: malformed row or extra columns")
            if row.get("cote") != "159":
                error(f"Inventory line {line}: cote must be 159")
            try:
                scan = int(row.get("scan", ""))
            except (TypeError, ValueError):
                error(f"Inventory line {line}: invalid scan number")
                continue
            inventory_scans.add(scan)
            if scan not in SCANS:
                error(f"Inventory line {line}: unexpected scan {scan}")
            if row.get("sheet_kind") not in SHEET_KINDS:
                error(f"Inventory line {line}: unrecognized sheet_kind")
            if row.get("kind") not in ELEMENT_KINDS:
                error(f"Inventory line {line}: unrecognized element kind")
            if row.get("transcribed") != "yes":
                error(f"Inventory line {line}: transcribed is not yes")
            for field in ("element", "position", "first_words_or_objects"):
                if not (row.get(field) or "").strip():
                    error(f"Inventory line {line}: empty {field}")
            key = (row.get("cote", ""), scan, row.get("element", ""))
            if key in seen_elements:
                error(f"Inventory line {line}: duplicate element identifier on scan {scan}")
            seen_elements.add(key)
        expected_coverage = set(pages) if partial else set(SCANS)
        if inventory_scans != expected_coverage:
            error(
                "Inventory page coverage mismatch: "
                f"missing={sorted(expected_coverage - inventory_scans)}, "
                f"extra={sorted(inventory_scans - expected_coverage)}"
            )
        details["inventory_rows"] = row_count

    progress = read("progress.log", required=not partial)
    if progress is not None:
        lines = progress.splitlines()
        if not lines or not re.fullmatch(TIME_PATTERN, lines[0].strip()):
            error("First progress.log line must be the starting UTC timestamp")
        done: dict[int, int] = {}
        audited: dict[int, int] = {}
        frozen_lines: list[int] = []
        context_lines: list[int] = []
        hashes: dict[str, list[tuple[int, str]]] = {}
        for index, line in enumerate(lines):
            match = re.fullmatch(r"159 scan (\d{3}) done (" + TIME_PATTERN + r")", line)
            if match:
                scan = int(match.group(1))
                if scan in done:
                    warnings.append(f"Duplicate done event for scan {scan:03d}")
                done[scan] = index
            match = re.fullmatch(r"scan (\d{3}) audited (" + TIME_PATTERN + r")", line)
            if match:
                audited[int(match.group(1))] = index
            if re.fullmatch(r"transcription frozen " + TIME_PATTERN, line):
                frozen_lines.append(index)
            if re.fullmatch(r"context opened " + TIME_PATTERN, line):
                context_lines.append(index)
            match = re.fullmatch(r"sha256 (\S+) ([0-9a-fA-F]{64})", line)
            if match:
                hashes.setdefault(match.group(1), []).append((index, match.group(2).lower()))

        needed = set(pages) if partial else set(SCANS)
        if set(done) != needed:
            error(f"Done events mismatch: missing={sorted(needed - set(done))}, extra={sorted(set(done) - needed)}")
        if not partial and set(audited) != set(SCANS):
            error(f"Audit events mismatch: missing={sorted(set(SCANS) - set(audited))}, extra={sorted(set(audited) - set(SCANS))}")
        for scan in set(done) & set(audited):
            if audited[scan] <= done[scan]:
                error(f"Scan {scan:03d}: audit event precedes completion")
        if not partial and not frozen_lines:
            error("No valid transcription frozen event")
        if len(frozen_lines) > 1:
            error("More than one transcription frozen event")
        if frozen_lines:
            freeze = frozen_lines[0]
            if any(index >= freeze for index in done.values()):
                error("A done event occurs at or after freezing")
            if set(audited) != set(SCANS) or any(index >= freeze for index in audited.values()):
                error("All 32 audit events must precede freezing")
            if not context_lines and not partial:
                error("No context opened event after freezing")
            if any(index <= freeze for index in context_lines):
                error("Context opened event precedes transcription freezing")
            hash_paths = set(expected_paths) | {"MPL_159_transcription.tex"}
            for relative in sorted(hash_paths):
                entries = hashes.get(relative, [])
                before = [digest for index, digest in entries if index < freeze]
                if not before:
                    error(f"Missing pre-freeze SHA-256: {relative}")
                    continue
                if len(set(digest for _, digest in entries)) != 1:
                    error(f"Logged hashes disagree: {relative}")
                path = root / relative
                if path.is_file():
                    digest = hashlib.sha256(path.read_bytes()).hexdigest()
                    if digest != before[-1]:
                        error(f"Frozen SHA-256 mismatch: {relative}")
            details["frozen_hash_files_checked"] = len(hash_paths)
            manifest = read("TRANSCRIPTION_SHA256SUMS")
            if manifest is not None:
                manifest_hashes = {}
                for line_number, line in enumerate(manifest.splitlines(), 1):
                    match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
                    if not match:
                        error(f"TRANSCRIPTION_SHA256SUMS line {line_number}: malformed hash record")
                        continue
                    digest, relative = match.groups()
                    if relative in manifest_hashes:
                        error(f"TRANSCRIPTION_SHA256SUMS: duplicate path {relative}")
                    manifest_hashes[relative] = digest.lower()
                    if relative not in hash_paths:
                        error(f"TRANSCRIPTION_SHA256SUMS: unexpected path {relative}")
                        continue
                    recorded = [value for index, value in hashes.get(relative, []) if index < freeze]
                    if recorded and digest.lower() != recorded[-1]:
                        error(f"Manifest and frozen log hashes differ: {relative}")
                    if (root / relative).is_file() and hashlib.sha256((root / relative).read_bytes()).hexdigest() != digest.lower():
                        error(f"Manifest SHA-256 mismatch: {relative}")
                if set(manifest_hashes) != hash_paths:
                    error("TRANSCRIPTION_SHA256SUMS does not cover exactly the 32 pages and combined file")
                details["manifest_hash_files_checked"] = len(manifest_hashes)
            if context_lines and not any(
                "unchanged" in line.lower() and "hash" in line.lower()
                for line in lines[max(context_lines) + 1:]
            ):
                warnings.append("No explicit final 'hashes unchanged' statement found after context opened")
        details["done_events"] = len(done)
        details["audit_events"] = len(audited)
        details["frozen"] = bool(frozen_lines)

    events = read("CHECK_EVENTS.tsv", required=not partial)
    if events is not None:
        event_rows = list(csv.reader(io.StringIO(events), delimiter="\t"))
        if not event_rows:
            error("CHECK_EVENTS.tsv is empty and has no header")
        elif any(len(row) != len(event_rows[0]) for row in event_rows[1:] if row):
            error("CHECK_EVENTS.tsv has inconsistent column counts")
        details["check_event_rows"] = max(0, len(event_rows) - 1)

    from check_research_metadata import validate_research
    research = validate_research(root, partial=partial)
    errors.extend(research["errors"])
    warnings.extend(research["warnings"])
    details["research_metadata"] = research["details"]

    return {
        "ok": not errors, "details": details, "errors": errors,
        "warnings": warnings,
        "scope": "Structural and byte-level checks only; no visual or mathematical certification.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true", help="Allow unfinished pages, audits, and research files")
    parser.add_argument("--json", action="store_true", help="Print machine-readable results")
    args = parser.parse_args()
    result = validate(args.root.resolve(), partial=args.partial)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("PASS" if result["ok"] else "FAIL")
        for key, value in result["details"].items():
            print(f"{key}: {value}")
        for message in result["errors"]:
            print(f"ERROR: {message}")
        for message in result["warnings"]:
            print(f"WARNING: {message}")
        print(result["scope"])
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
