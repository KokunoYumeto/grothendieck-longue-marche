#!/usr/bin/env python3
"""Read-only structural validation for the MPL 154, scans 127–176 package.

Usage:
    python scripts/validate_package.py --root /path/to/package
    python scripts/validate_package.py --root /path/to/package --complete

The default mode checks the available page fragments and their inventory rows.
Complete mode additionally requires all 50 scans, the combined transcription,
recorded completion and audit events, and valid frozen hashes if supplied.

Package paths are relative to --root:
    pages/MPL_154_127-176_154_scanNNN.tex
    MPL_154_127-176_inventory.csv
    MPL_154_127-176_transcription.tex
    progress.log
    records/frozen_hashes.sha256                  (optional)

The combined transcription must equal b'\\n'.join(page_bytes), in scan order.
Each page retains its own final newline. One extra final LF is also accepted,
so b''.join(page_bytes + b'\\n' for page_bytes in pages) is equivalent for this
check. No other changes to whitespace or content are accepted.

Log event lines must use these forms, substituting the scan and actual time:
    154 scan 127 done 2026-11-14 12:00:00 UTC
    scan 127 audited 2026-11-14 12:01:00 UTC
    transcription frozen 2026-11-14 13:00:00 UTC
The example timestamps above illustrate syntax only. Actual events must retain
their actual timestamps. Complete mode requires a single freeze event after
all recorded page audits.

The optional hash manifest uses sha256sum format with paths relative to --root:
    <64 hexadecimal characters>  pages/<page filename>
If present in complete mode, it must cover every page fragment. Additional
root-relative files may also be listed and are checked.

This script does not write or repair any file. It is not a full TeX parser.
Semantic and visual correctness cannot be mechanically validated: passing
checks do not establish transcription accuracy, completeness of visible marks,
reading order, image-to-page correspondence, or that an audit took place.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
from pathlib import Path, PurePosixPath
import re
import sys


SCANS = tuple(range(127, 177))
SCAN_SET = set(SCANS)
PAGE_PREFIX = "MPL_154_127-176_154_scan"
PAGE_PATTERN = re.compile(r"MPL_154_127-176_154_scan([0-9]{3})\.tex\Z")
INVENTORY_NAME = "MPL_154_127-176_inventory.csv"
COMBINED_NAME = "MPL_154_127-176_transcription.tex"
INVENTORY_HEADER = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
UTC_TIMESTAMP_PATTERN = r"([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} UTC)"
DONE_EVENT = re.compile(r"154 scan ([0-9]{3}) done " + UTC_TIMESTAMP_PATTERN)
AUDIT_EVENT = re.compile(r"scan ([0-9]{3}) audited " + UTC_TIMESTAMP_PATTERN)
FREEZE_EVENT = re.compile(r"transcription frozen " + UTC_TIMESTAMP_PATTERN)
DISCLAIMER = (
    "Mechanical validation cannot establish semantic or visual correctness, "
    "transcription accuracy, completeness of visible marks, reading order, "
    "image-to-page correspondence, or whether an audit was actually performed."
)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.notes: list[str] = []

    def error(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    def note(self, message: str) -> None:
        self.notes.append(message)

    def finish(self) -> int:
        for note in self.notes:
            print(f"INFO: {note}")
        for error in self.errors:
            print(f"ERROR: {error}")
        print(f"RESULT: {'FAIL' if self.errors else 'PASS'} ({len(self.errors)} error(s))")
        print(f"LIMIT: {DISCLAIMER}")
        return 1 if self.errors else 0


def read_bytes(root: Path, relative: str, report: Report) -> bytes | None:
    """Read a regular file while refusing paths that resolve outside the root."""
    path = root / relative
    try:
        resolved = path.resolve()
        if resolved != root and root not in resolved.parents:
            report.error(relative, "path resolves outside the package root")
            return None
        if not resolved.is_file():
            report.error(relative, "required regular file is missing")
            return None
        return resolved.read_bytes()
    except (OSError, RuntimeError) as exc:
        report.error(relative, f"cannot read file: {exc}")
        return None


def decode_utf8(data: bytes, relative: str, report: Report, *, csv_file: bool = False) -> str | None:
    try:
        return data.decode("utf-8-sig" if csv_file else "utf-8")
    except UnicodeDecodeError as exc:
        report.error(relative, f"invalid UTF-8: {exc}")
        return None


def active_latex(text: str) -> str:
    """Blank comments without changing character offsets or line numbers.

    A backslash escapes the immediately following character. Thus \\% remains
    active text, whereas two backslashes followed by % start a comment.
    """
    chars = list(text)
    index = 0
    while index < len(chars):
        if chars[index] == "\\":
            index += 2
        elif chars[index] == "%":
            while index < len(chars) and chars[index] not in "\r\n":
                chars[index] = " "
                index += 1
        else:
            index += 1
    return "".join(chars)


def commands(text: str) -> list[tuple[str, int, int]]:
    """Return active control words as (name, start, end) tuples."""
    result: list[tuple[str, int, int]] = []
    index = 0
    while index < len(text):
        if text[index] != "\\":
            index += 1
            continue
        start = index
        index += 1
        if index < len(text) and (text[index].isalpha() or text[index] == "@"):
            name_start = index
            while index < len(text) and (text[index].isalpha() or text[index] == "@"):
                index += 1
            result.append((text[name_start:index], start, index))
        else:
            index += 1
    return result


def group_after(text: str, offset: int) -> tuple[str, int] | None:
    """Read a braced argument after a command, respecting escaped braces."""
    index = offset
    while index < len(text) and text[index].isspace():
        index += 1
    if index == len(text) or text[index] != "{":
        return None
    start = index + 1
    depth = 1
    index += 1
    while index < len(text):
        if text[index] == "\\":
            index += 2
            continue
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return text[start:index].strip(), index + 1
        index += 1
    return None


def check_braces(text: str, relative: str, report: Report) -> None:
    opens: list[int] = []
    index = 0
    line = 1
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text):
            if text[index + 1] == "\n":
                line += 1
            index += 2
            continue
        if char == "\n":
            line += 1
        elif char == "{":
            opens.append(line)
        elif char == "}":
            if opens:
                opens.pop()
            else:
                report.error(f"{relative}:{line}", "unmatched closing brace")
        index += 1
    if opens:
        lines = ", ".join(str(number) for number in opens)
        report.error(relative, f"unclosed opening brace(s) on line(s): {lines}")


def check_page(scan: int, text: str, relative: str, report: Report) -> None:
    active = active_latex(text)
    check_braces(active, relative, report)
    found = commands(active)
    for name, start, _ in found:
        if name in {"includegraphics", "documentclass"}:
            line = active.count("\n", 0, start) + 1
            report.error(f"{relative}:{line}", f"forbidden command \\{name}")

    markers = [entry for entry in found if entry[0] == "scanpage"]
    if len(markers) != 1:
        report.error(relative, f"expected exactly one \\scanpage{{{scan}}}; found {len(markers)} marker(s)")
    else:
        argument = group_after(active, markers[0][2])
        if argument is None or argument[0] != str(scan):
            report.error(relative, f"expected marker \\scanpage{{{scan}}}")

    cotes = [entry for entry in found if entry[0] == "cotefile"]
    if scan == 127:
        if len(cotes) != 1:
            report.error(relative, "first page must contain exactly one \\cotefile{154}")
        else:
            argument = group_after(active, cotes[0][2])
            if argument is None or argument[0] != "154":
                report.error(relative, "expected marker \\cotefile{154}")
            if active[:cotes[0][1]].strip():
                report.error(relative, "\\cotefile{154} must be the first active content")
            if argument is not None and len(markers) == 1:
                if markers[0][1] < argument[1] or active[argument[1]:markers[0][1]].strip():
                    report.error(relative, "first-page \\scanpage{127} must follow \\cotefile{154}")
    elif cotes:
        report.error(relative, "\\cotefile is permitted only in the first page fragment")


def check_pages(root: Path, complete: bool, report: Report) -> dict[int, bytes]:
    directory = root / "pages"
    pages: dict[int, bytes] = {}
    try:
        resolved = directory.resolve()
        if resolved != root and root not in resolved.parents:
            report.error("pages", "directory resolves outside the package root")
            return pages
        if not directory.is_dir():
            report.error("pages", "required directory is missing")
            return pages
        entries = sorted(directory.iterdir(), key=lambda item: item.name)
    except (OSError, RuntimeError) as exc:
        report.error("pages", f"cannot list directory: {exc}")
        return pages

    for path in entries:
        if path.suffix.lower() != ".tex":
            continue
        relative = f"pages/{path.name}"
        match = PAGE_PATTERN.fullmatch(path.name)
        if match is None:
            report.error(relative, "unexpected page filename")
            continue
        scan = int(match.group(1))
        if scan not in SCAN_SET:
            report.error(relative, "scan is outside the expected range 127–176")
            continue
        data = read_bytes(root, relative, report)
        if data is None:
            continue
        pages[scan] = data
        if not data.endswith(b"\n"):
            report.error(relative, "page fragment must end with a newline")
        text = decode_utf8(data, relative, report)
        if text is not None:
            check_page(scan, text, relative, report)

    if not pages:
        report.error("pages", "no readable page fragments found")
    if complete:
        missing = sorted(SCAN_SET - pages.keys())
        if missing:
            report.error("pages", "missing scan(s): " + ", ".join(map(str, missing)))
    report.note(f"Checked {len(pages)} page fragment(s).")
    return pages


def check_inventory(root: Path, pages: dict[int, bytes], complete: bool, report: Report) -> None:
    data = read_bytes(root, INVENTORY_NAME, report)
    if data is None:
        return
    text = decode_utf8(data, INVENTORY_NAME, report, csv_file=True)
    if text is None:
        return
    reader = csv.reader(io.StringIO(text, newline=""), strict=True)
    observed: set[int] = set()
    elements: set[tuple[int, str]] = set()
    count = 0
    try:
        header = next(reader, None)
        if header != INVENTORY_HEADER:
            report.error(INVENTORY_NAME, "header must be exactly " + ",".join(INVENTORY_HEADER))
            return
        for fields in reader:
            if not fields or all(not value.strip() for value in fields):
                continue
            count += 1
            location = f"{INVENTORY_NAME}:{reader.line_num}"
            if len(fields) != len(INVENTORY_HEADER):
                report.error(location, f"expected 8 columns; found {len(fields)}")
                continue
            row = dict(zip(INVENTORY_HEADER, (value.strip() for value in fields)))
            missing_fields = [name for name, value in row.items() if not value]
            if missing_fields:
                report.error(location, "empty required field(s): " + ", ".join(missing_fields))
            if row["cote"] != "154":
                report.error(location, "cote must be 154")
            if row["kind"] not in KINDS:
                report.error(location, "invalid kind; expected one of: " + ", ".join(sorted(KINDS)))
            if row["transcribed"] != "yes":
                report.error(location, "transcribed must be yes")
            if not re.fullmatch(r"[0-9]{3}", row["scan"]) or int(row["scan"]) not in SCAN_SET:
                report.error(location, "scan must be an integer from 127 through 176")
                continue
            scan = int(row["scan"])
            observed.add(scan)
            key = (scan, row["element"])
            if key in elements:
                report.error(location, f"duplicate element identifier for scan {scan}")
            elements.add(key)
            if scan not in pages:
                report.error(location, f"inventory refers to absent or unreadable scan {scan}")
    except csv.Error as exc:
        report.error(f"{INVENTORY_NAME}:{reader.line_num}", f"invalid CSV: {exc}")
    expected = SCAN_SET if complete else set(pages)
    missing_scans = sorted(expected - observed)
    if missing_scans:
        report.error(INVENTORY_NAME, "no inventory rows for scan(s): " + ", ".join(map(str, missing_scans)))
    if count == 0:
        report.error(INVENTORY_NAME, "inventory has no data rows")
    report.note(f"Checked {count} inventory row(s), covering {len(observed)} scan(s).")


def check_combined(root: Path, pages: dict[int, bytes], report: Report) -> None:
    actual = read_bytes(root, COMBINED_NAME, report)
    if actual is None:
        return
    if set(pages) != SCAN_SET:
        report.error(COMBINED_NAME, "cannot check concatenation until all 50 pages are readable")
        return
    expected = b"\n".join(pages[scan] for scan in SCANS)
    if actual not in (expected, expected + b"\n"):
        offset = next((index for index, pair in enumerate(zip(actual, expected)) if pair[0] != pair[1]), min(len(actual), len(expected)))
        report.error(COMBINED_NAME, f"does not match the documented page concatenation (first difference at byte {offset})")
    else:
        report.note("Combined transcription matches the documented byte-for-byte page concatenation.")


def check_log(root: Path, report: Report) -> None:
    relative = "progress.log"
    data = read_bytes(root, relative, report)
    if data is None:
        return
    text = decode_utf8(data, relative, report)
    if text is None:
        return
    events: dict[int, dict[str, list[tuple[int, datetime | None]]]] = {
        scan: {"done": [], "audited": []} for scan in SCANS
    }
    freezes: list[tuple[int, datetime | None]] = []

    def timestamp_value(value: str, location: str) -> datetime | None:
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
        except ValueError:
            report.error(location, "event has an invalid UTC timestamp")
            return None

    for number, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        location = f"{relative}:{number}"
        frozen = FREEZE_EVENT.fullmatch(line)
        if frozen is not None:
            freezes.append((number, timestamp_value(frozen.group(1), location)))
            continue
        done = DONE_EVENT.fullmatch(line)
        audited = AUDIT_EVENT.fullmatch(line)
        matched = done if done is not None else audited
        if matched is None:
            if line.lower().startswith("transcription frozen"):
                report.error(location, "expected: transcription frozen YYYY-MM-DD HH:MM:SS UTC")
            elif re.search(r"\bscan\b", line, flags=re.IGNORECASE) and re.search(r"\b(?:done|audited)\b", line, flags=re.IGNORECASE):
                report.error(location, "expected: 154 scan NNN done YYYY-MM-DD HH:MM:SS UTC; or scan NNN audited YYYY-MM-DD HH:MM:SS UTC")
            continue
        scan = int(matched.group(1))
        if scan not in SCAN_SET:
            report.error(location, "event scan is outside the expected range 127–176")
            continue
        status = "done" if done is not None else "audited"
        events[scan][status].append((number, timestamp_value(matched.group(2), location)))

    for scan in SCANS:
        done, audited = events[scan]["done"], events[scan]["audited"]
        if not done:
            report.error(relative, f"missing done event for scan {scan}")
        if not audited:
            report.error(relative, f"missing audited event for scan {scan}")
        if done and audited:
            if audited[0][0] <= done[0][0]:
                report.error(relative, f"scan {scan}: first audited event must be on a later line than first done event")
            if done[0][1] is not None and audited[0][1] is not None and audited[0][1] < done[0][1]:
                report.error(relative, f"scan {scan}: first audit timestamp precedes first done timestamp")
    if len(freezes) != 1:
        report.error(relative, f"expected exactly one transcription frozen event; found {len(freezes)}")
    else:
        freeze_line, freeze_time = freezes[0]
        for scan in SCANS:
            for audit_line, audit_time in events[scan]["audited"]:
                if audit_line >= freeze_line:
                    report.error(relative, f"scan {scan}: audit event occurs after the freeze event")
                if freeze_time is not None and audit_time is not None and audit_time > freeze_time:
                    report.error(relative, f"scan {scan}: audit timestamp is later than the freeze timestamp")
    report.note("Checked recorded done, audited, and transcription frozen events and UTC timestamp syntax.")


def check_hashes(root: Path, report: Report) -> None:
    relative = "records/frozen_hashes.sha256"
    path = root / relative
    if not path.exists() and not path.is_symlink():
        report.note("No optional frozen hash manifest was supplied.")
        return
    data = read_bytes(root, relative, report)
    if data is None:
        return
    text = decode_utf8(data, relative, report)
    if text is None:
        return
    seen: set[str] = set()
    verified = 0
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        location = f"{relative}:{number}"
        match = re.fullmatch(r"([0-9a-fA-F]{64})[ \t]+\*?(.+)", line)
        if match is None:
            report.error(location, "expected sha256sum syntax: 64-digit hash, whitespace, relative path")
            continue
        digest, filename = match.groups()
        parsed = PurePosixPath(filename)
        if parsed.is_absolute() or ".." in parsed.parts or "\\" in filename or not parsed.parts:
            report.error(location, "hash filename must be a safe root-relative POSIX path")
            continue
        filename = parsed.as_posix()
        if filename in seen:
            report.error(location, f"duplicate hash record: {filename}")
            continue
        seen.add(filename)
        contents = read_bytes(root, filename, report)
        if contents is None:
            continue
        actual = hashlib.sha256(contents).hexdigest()
        if actual != digest.lower():
            report.error(location, f"SHA256 mismatch: {filename}")
        else:
            verified += 1
    expected = {f"pages/{PAGE_PREFIX}{scan}.tex" for scan in SCANS}
    missing = sorted(expected - seen)
    if missing:
        report.error(relative, "missing frozen page hash(es): " + ", ".join(Path(item).name for item in missing))
    report.note(f"Verified {verified} frozen SHA256 record(s).")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", required=True, type=Path, help="package directory")
    parser.add_argument("--complete", action="store_true", help="require all 50 pages and final-package records")
    args = parser.parse_args()
    report = Report()
    try:
        root = args.root.expanduser().resolve()
    except (OSError, RuntimeError) as exc:
        report.error(str(args.root), f"cannot resolve package root: {exc}")
        return report.finish()
    if not root.is_dir():
        report.error(str(root), "package root is not a directory")
        return report.finish()
    pages = check_pages(root, args.complete, report)
    check_inventory(root, pages, args.complete, report)
    if args.complete:
        check_combined(root, pages, report)
        check_log(root, report)
        check_hashes(root, report)
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
