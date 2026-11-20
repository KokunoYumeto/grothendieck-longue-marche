#!/usr/bin/env python3
"""Mechanical checks only; this program does not assess manuscript readings.

Usage:
    python validate_package.py OUTPUT_ROOT [SOURCE_TEXTS_ROOT] [--zip FINAL_ZIP]
    python validate_package.py OUTPUT_ROOT [SOURCE_TEXTS_ROOT] --partial
    python validate_package.py OUTPUT_ROOT [SOURCE_TEXTS_ROOT] --pre-freeze

SOURCE_TEXTS_ROOT, when supplied, is used only for MARKS.tsv identifier/order
validation. No scan is opened, and no witness transcription is read.
Standard hash lines in progress.log may be either:
    <64 hex digits>  pages/136_scan330.tex
    sha256 pages/136_scan330.tex <64 hex digits>
The --partial option validates a checkpoint without requiring unfinished pages.
The --pre-freeze option keeps strict completeness/audit checks but defers only
the not-yet-written freeze marker and frozen-hash requirements.
Exit codes: 0 = no errors (warnings are permitted), 1 = validation errors,
2 = invalid command line.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import io
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath


SCANS = (330, 332, 333, 334, 335, 337, 338, 339, 340, 342, 343, 345,
         346, 348, 350, 351, 352, 355, 357, 358, 359, 360, 361, 362, 363)
PREFIX = "SP67_C13_136"
PAGE_NAMES = tuple(f"136_scan{scan:03d}.tex" for scan in SCANS)
REQUIRED = (
    f"{PREFIX}_transcription.tex", f"{PREFIX}_changes.md",
    f"{PREFIX}_collation.tsv", "decisions.tsv", f"{PREFIX}_doubts.md",
    f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md", "CHECK_EVENTS.tsv",
    "progress.log", f"{PREFIX}_sheet_feedback.md", f"{PREFIX}_hand_log.md",
)
COLLATION_COLUMNS = (
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
    "confidence",
)
DECISION_COLUMNS = (
    "id", "cote", "scan", "decision", "reading", "what the ink shows",
    "crop", "confidence",
)
INVENTORY_COLUMNS = (
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
EVENT_COLUMNS = ("statement_id", "date", "who", "type", "outcome")
CONFIDENCES = {"high", "medium", "low"}
DECISIONS = {"first", "alternative", "other", "undecided"}
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission",
    "text not on the page", "deletion state (struck given live or live given struck)",
    "deletion state", "insertion or placement",
    "abbreviation expanded or spelling modernised",
    "readable ink left as \\ill{}", "readable ink left as `\\ill{}`",
    "drawing or diagram", "other",
}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list",
    "cancelled_draft", "cover",
}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion",
    "deletion",
}
ADDITIONAL_DOUBT_FIELDS = {"place", "reading", "alternatives", "evidence", "confidence"}
IMAGE_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".webp",
    ".bmp", ".svg", ".avif", ".heic", ".heif", ".ico", ".jp2",
    ".ppm", ".pgm", ".pbm", ".pnm", ".jxl",
}
TEXT_SUFFIXES = {
    ".tex", ".md", ".tsv", ".csv", ".log", ".py", ".txt", ".json",
    ".yaml", ".yml", ".toml", ".sh",
}
CACHE_PARTS = {"__pycache__", ".cache", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".git", "node_modules"}
SOURCE_PARTS = {"source", "upload", "SP67_C13_136_scans", "SP67_C13_136_texts", "hua", "views", "crops", "halves"}
SOURCE_NAMES = {"MARKS.tsv", "PREAMBLE.tex"}


def is_cache_path(relative):
    path = PurePosixPath(relative)
    return bool(set(path.parts) & CACHE_PARTS) or path.suffix.lower() in {".pyc", ".pyo"}


def package_file_allowed(relative):
    """Shared archive filter: deliverables/documentation, never inputs or caches."""
    path = PurePosixPath(relative)
    return not (
        is_cache_path(path)
        or set(path.parts) & SOURCE_PARTS
        or path.name in SOURCE_NAMES
        or (path.name.startswith("PROMPT(") and path.suffix.lower() == ".md")
        or path.suffix.lower() in IMAGE_SUFFIXES | {".zip"}
    )


class Checks:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, message):
        self.errors.append(str(message))

    def warn(self, message):
        self.warnings.append(str(message))

    def text(self, path):
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error(f"Cannot read UTF-8 file {path}: {exc}")
            return None


def strip_comments(text):
    """Remove TeX comments while retaining escaped percent signs."""
    result = []
    i = 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            result.append(text[i:i + 2])
            i += 2
        elif text[i] == "%":
            end = text.find("\n", i)
            if end < 0:
                break
            result.append("\n")
            i = end + 1
        else:
            result.append(text[i])
            i += 1
    return "".join(result)


def canonical_tex(text):
    text = strip_comments(text)
    text = re.sub(r"\\(?:newpage|clearpage|pagebreak)(?:\[\d\])?(?![A-Za-z])", "", text)
    return re.sub(r"\s+", "", text)


def check_braces(text, filename, checks):
    text = strip_comments(text)
    openings = []
    i = 0
    line = 1
    while i < len(text):
        char = text[i]
        if char == "\\" and i + 1 < len(text):
            if text[i + 1] == "\n":
                line += 1
            i += 2
            continue
        if char == "\n":
            line += 1
        elif char == "{":
            openings.append(line)
        elif char == "}":
            if openings:
                openings.pop()
            else:
                checks.warn(f"{filename}:{line}: unmatched closing TeX brace")
        i += 1
    for opening in openings:
        checks.warn(f"{filename}:{opening}: unmatched opening TeX brace")


def read_table(root, name, columns, checks, delimiter="\t"):
    path = root / name
    if not path.is_file():
        return []
    text = checks.text(path)
    if text is None:
        return []
    try:
        reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff")), delimiter=delimiter)
        header = reader.fieldnames or []
        if len(header) != len(set(header)):
            checks.error(f"{name}: duplicate header name")
        if set(header) != set(columns):
            missing = sorted(set(columns) - set(header))
            extra = sorted(set(header) - set(columns))
            checks.error(f"{name}: incorrect headers; missing={missing}, extra={extra}")
        rows = list(reader)
        for number, row in enumerate(rows, 2):
            if None in row or any(value is None for value in row.values()):
                checks.error(f"{name}:{number}: wrong number of fields")
        return rows
    except csv.Error as exc:
        checks.error(f"{name}: malformed table: {exc}")
        return []


def integer(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def check_additional_doubts(root, partial, checks):
    """Partial work permits legacy strings; final work requires explicit confidence."""
    legacy = []
    identifiers = {}
    for path in sorted((root / "records").glob("scan*.py")):
        try:
            record = ast.literal_eval(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError, SyntaxError) as exc:
            checks.error(f"Cannot validate additional doubts in {path.name}: {exc}")
            continue
        if not isinstance(record, dict):
            checks.error(f"{path.name}: record must be a dictionary")
            continue
        scan = record.get("scan")
        unresolved = record.get("unresolved", [])
        if not isinstance(unresolved, list):
            checks.error(f"{path.name}: unresolved must be a list")
            continue
        for index, item in enumerate(unresolved, 1):
            location = f"{path.name}, additional doubt {index}"
            if isinstance(item, str):
                legacy.append((scan, index))
                continue
            if not isinstance(item, dict):
                checks.error(f"{location}: expected a structured dictionary")
                continue
            missing = ADDITIONAL_DOUBT_FIELDS - set(item)
            extra = set(item) - ADDITIONAL_DOUBT_FIELDS - {"id"}
            if missing or extra:
                checks.error(f"{location}: missing fields={sorted(missing)}, extra fields={sorted(extra)}")
            for field in ADDITIONAL_DOUBT_FIELDS:
                if not isinstance(item.get(field), str):
                    checks.error(f"{location}: {field} must be a string")
            for field in ("place", "reading"):
                if not isinstance(item.get(field), str) or not item[field].strip():
                    checks.error(f"{location}: {field} must be nonempty")
            if not isinstance(item.get("confidence"), str) or item["confidence"] not in CONFIDENCES:
                checks.error(f"{location}: explicit confidence must be low, medium, or high")
            identifier = item.get("id", f"U136-{scan}-{index:02d}")
            if not isinstance(identifier, str) or not identifier.strip():
                checks.error(f"{location}: id must be a nonempty string when supplied")
            elif identifier in identifiers:
                checks.error(f"{location}: duplicate additional-doubt id also used at {identifiers[identifier]}")
            else:
                identifiers[identifier] = location
    if legacy:
        scans = sorted({scan for scan, _ in legacy}, key=str)
        message = (f"{len(legacy)} additional doubts remain legacy strings on scans {scans}; "
                   "the sole reader must supply structured entries with explicit confidence before final validation")
        (checks.warn if partial else checks.error)(message)


def check_progress(root, present_scans, partial, checks, pre_freeze=False):
    path = root / "progress.log"
    if not path.is_file():
        return
    text = checks.text(path)
    if text is None:
        return
    first = text.splitlines()[0] if text.splitlines() else ""
    if not re.search(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}", first):
        checks.error("progress.log: first line does not contain a UTC timestamp")
    if not ("UTC" in first or re.search(r"(?:Z|\+00:?00)\s*$", first)):
        checks.warn("progress.log: first-line timezone is not explicitly UTC")
    done = [int(value) for value in re.findall(r"(?m)^scan\s+(\d+)\s+done\b", text)]
    audited = [int(value) for value in re.findall(r"(?m)^scan\s+(\d+)\s+audited\b", text)]
    for name, values in (("done", done), ("audited", audited)):
        unknown = sorted(set(values) - set(SCANS))
        if unknown:
            checks.error(f"progress.log: unexpected {name} scan numbers {unknown}")
        duplicates = sorted(scan for scan, count in Counter(values).items() if count > 1)
        if duplicates:
            checks.warn(f"progress.log: repeated {name} entries {duplicates}")
    missing_done = sorted(set(present_scans) - set(done))
    if missing_done:
        checks.error(f"progress.log: pages lack done entries: {missing_done}")
    if not partial:
        missing_audited = sorted(set(SCANS) - set(audited))
        if missing_audited:
            checks.error(f"progress.log: pages lack audited entries: {missing_audited}")
        if not pre_freeze and not re.search(r"(?m)^transcription frozen\b", text):
            checks.error("progress.log: missing 'transcription frozen' entry")
    ordered_done = list(dict.fromkeys(done))
    if ordered_done != sorted(ordered_done, key=lambda value: SCANS.index(value) if value in SCANS else len(SCANS)):
        checks.error("progress.log: first done entries are not in required scan order")
    # Recognize both GNU-style and label/path/digest forms without requiring
    # a particular timestamp or explanatory prefix on the line.
    recorded = {}
    for line in text.splitlines():
        digest_match = re.search(r"\b([0-9a-fA-F]{64})\b", line)
        if not digest_match:
            continue
        name_match = re.search(r"(?:pages/)?136_scan\d{3}\.tex|SP67_C13_136_transcription\.tex", line)
        if not name_match:
            continue
        name = name_match.group(0)
        if name.startswith("136_scan"):
            name = "pages/" + name
        digest = digest_match.group(1).lower()
        recorded.setdefault(name, []).append(digest)
        candidate = root / name
        if not candidate.is_file():
            checks.error(f"progress.log: hash names a missing file: {name}")
            continue
        actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
        if actual != digest:
            checks.error(f"progress.log: SHA-256 mismatch for {name}")
    if not partial and not pre_freeze:
        expected = {f"pages/{name}" for name in PAGE_NAMES}
        expected.add(f"{PREFIX}_transcription.tex")
        missing_hashes = sorted(expected - set(recorded))
        if missing_hashes:
            checks.error(f"progress.log: missing frozen hashes for {missing_hashes}")
        if not re.search(r"hash(?:es)?.{0,80}unchanged|unchanged.{0,80}hash(?:es)?", text, re.I):
            checks.warn("progress.log: no explicit final statement that hashes are unchanged")


def validate_zip(archive_path, root, partial, checks):
    try:
        with zipfile.ZipFile(archive_path) as archive:
            infos = [item for item in archive.infolist() if not item.is_dir()]
            names = [item.filename for item in infos]
            duplicates = [name for name, count in Counter(names).items() if count > 1]
            if duplicates:
                checks.error(f"ZIP has duplicate members: {duplicates}")
            prefix = PREFIX + "/"
            common_prefix = prefix if names and all(name.startswith(prefix) for name in names) else ""
            normalized = {}
            for item in infos:
                name = item.filename
                path = PurePosixPath(name)
                if path.is_absolute() or ".." in path.parts or "\\" in name:
                    checks.error(f"ZIP has unsafe or nonportable member path: {name}")
                relative = name[len(common_prefix):]
                normalized[relative] = item
                if path.suffix.lower() in IMAGE_SUFFIXES:
                    checks.error(f"ZIP contains prohibited image: {name}")
                if path.suffix.lower() == ".zip":
                    checks.error(f"ZIP contains a nested ZIP: {name}")
                elif not package_file_allowed(relative) and path.suffix.lower() not in IMAGE_SUFFIXES:
                    checks.error(f"ZIP contains an excluded source/cache member: {name}")
            required = set(REQUIRED)
            required.update(f"pages/{name}" for name in PAGE_NAMES)
            if partial:
                required = {name for name in required if (root / name).is_file()}
            missing = sorted(required - set(normalized))
            if missing:
                checks.error(f"ZIP missing required members: {missing}")
            bad_crc = archive.testzip()
            if bad_crc:
                checks.error(f"ZIP CRC error: {bad_crc}")
            for local in sorted(root.rglob("*")):
                if not local.is_file() or local.resolve() == archive_path.resolve():
                    continue
                relative = local.relative_to(root).as_posix()
                if not package_file_allowed(relative):
                    continue
                if relative not in normalized:
                    checks.error(f"ZIP omits output file: {relative}")
                elif archive.read(normalized[relative]) != local.read_bytes():
                    checks.error(f"ZIP member differs from output file: {relative}")
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        checks.error(f"Cannot validate ZIP {archive_path}: {exc}")


def validate(args):
    root = args.output_root.resolve()
    checks = Checks()
    if not root.is_dir():
        checks.error(f"Output root does not exist: {root}")
        return checks
    for name in REQUIRED:
        if not (root / name).is_file():
            (checks.warn if args.partial else checks.error)(f"Missing deliverable: {name}")
    files = [path for path in root.rglob("*") if path.is_file() and not is_cache_path(path.relative_to(root).as_posix())]
    for path in sorted(files):
        relative = path.relative_to(root).as_posix()
        if path.suffix.lower() in IMAGE_SUFFIXES:
            checks.error(f"Output contains prohibited image: {relative}")
        if path.suffix.lower() == ".zip":
            if not (args.zip and path.resolve() == args.zip.resolve()):
                checks.error(f"Output contains a nested ZIP: {relative}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            checks.text(path)
    pages_dir = root / "pages"
    actual_names = {path.name for path in pages_dir.glob("*.tex")} if pages_dir.is_dir() else set()
    unexpected = sorted(actual_names - set(PAGE_NAMES))
    missing = sorted(set(PAGE_NAMES) - actual_names)
    if unexpected:
        checks.error(f"Unexpected page filenames: {unexpected}")
    if missing and not args.partial:
        checks.error(f"Missing page files: {missing}")
    present_scans = [scan for scan in SCANS if f"136_scan{scan:03d}.tex" in actual_names]
    fragments = []
    for name in PAGE_NAMES:
        path = pages_dir / name
        if not path.is_file():
            continue
        text = checks.text(path)
        if text is not None:
            fragments.append(text)
            check_braces(text, f"pages/{name}", checks)
    combined = root / f"{PREFIX}_transcription.tex"
    if combined.is_file():
        text = checks.text(combined)
        if text is not None:
            check_braces(text, combined.name, checks)
            if canonical_tex(text) != canonical_tex("\n".join(fragments)):
                checks.error("Combined transcription differs from the ordered page fragments")
    decisions = read_table(root, "decisions.tsv", DECISION_COLUMNS, checks)
    identifiers = [row.get("id", "") for row in decisions]
    duplicate_ids = sorted(value for value, count in Counter(identifiers).items() if count > 1)
    if duplicate_ids:
        checks.error(f"decisions.tsv: duplicate IDs: {duplicate_ids}")
    for number, row in enumerate(decisions, 2):
        if row.get("decision") not in DECISIONS:
            checks.error(f"decisions.tsv:{number}: invalid decision")
        if row.get("confidence") not in CONFIDENCES:
            checks.error(f"decisions.tsv:{number}: invalid confidence")
        if integer(row.get("scan")) not in present_scans:
            checks.error(f"decisions.tsv:{number}: scan is not a present page")
        if str(row.get("cote")) != "136":
            checks.error(f"decisions.tsv:{number}: cote must be 136")
        for field in ("id", "reading", "what the ink shows", "crop"):
            # An empty string can be the reader's positive finding of absence.
            # Do not confuse it with a missing column/value or unresolved data.
            if (field == "reading" and row.get("reading") == ""
                    and row.get("decision") == "other"
                    and isinstance(row.get("what the ink shows"), str)
                    and row["what the ink shows"].strip()):
                continue
            if not str(row.get(field, "")).strip():
                checks.error(f"decisions.tsv:{number}: empty {field}")
    if args.source_texts_root:
        marks_path = args.source_texts_root / "MARKS.tsv"
        marks_text = checks.text(marks_path)
        if marks_text is not None:
            marks_reader = csv.DictReader(io.StringIO(marks_text.lstrip("\ufeff")), delimiter="\t")
            if not {"id", "scan"}.issubset(set(marks_reader.fieldnames or [])):
                checks.error("Source MARKS.tsv lacks id/scan headers")
            else:
                marks = list(marks_reader)
                if args.partial:
                    marks = [row for row in marks if integer(row.get("scan")) in present_scans]
                expected_ids = [row["id"] for row in marks]
                if identifiers != expected_ids:
                    checks.error("decisions.tsv IDs do not exactly match MARKS.tsv in order")
                for decision, mark in zip(decisions, marks):
                    if decision.get("id") == mark.get("id") and integer(decision.get("scan")) != integer(mark.get("scan")):
                        checks.error(f"decisions.tsv: wrong scan for {decision.get('id')}")
    else:
        checks.warn("MARKS.tsv identifier coverage was not checked (no source texts root supplied)")
    collation = read_table(root, f"{PREFIX}_collation.tsv", COLLATION_COLUMNS, checks)
    for number, row in enumerate(collation, 2):
        scan = integer(row.get("our_scan"))
        if scan not in present_scans:
            checks.error(f"Collation row {number}: scan is not a present page")
        if scan == 351:
            checks.error(f"Collation row {number}: scan 351 has no witness H")
        if scan is not None and integer(row.get("their_page")) != scan - 1:
            checks.error(f"Collation row {number}: their_page must equal our_scan minus 1")
        if str(row.get("folder")) != "136":
            checks.error(f"Collation row {number}: folder must be 136")
        if row.get("kind") not in COLLATION_KINDS:
            checks.error(f"Collation row {number}: invalid kind {row.get('kind')!r}")
        if row.get("confidence") not in CONFIDENCES:
            checks.error(f"Collation row {number}: invalid confidence")
        if not str(row.get("marked_in_H", "")).strip():
            checks.error(f"Collation row {number}: marked_in_H is empty")
    inventory = read_table(root, f"{PREFIX}_inventory.csv", INVENTORY_COLUMNS, checks, delimiter=",")
    inventory_scans = set()
    for number, row in enumerate(inventory, 2):
        scan = integer(row.get("scan"))
        inventory_scans.add(scan)
        if scan not in present_scans:
            checks.error(f"Inventory row {number}: scan is not a present page")
        if row.get("transcribed") != "yes":
            checks.error(f"Inventory row {number}: transcribed must be yes")
        if row.get("sheet_kind") not in SHEET_KINDS:
            checks.error(f"Inventory row {number}: invalid sheet_kind")
        if row.get("kind") not in ELEMENT_KINDS:
            checks.error(f"Inventory row {number}: invalid kind")
    missing_inventory = sorted(set(present_scans) - inventory_scans)
    if missing_inventory:
        checks.error(f"Inventory lacks pages: {missing_inventory}")
    read_table(root, "CHECK_EVENTS.tsv", EVENT_COLUMNS, checks)
    check_additional_doubts(root, args.partial, checks)
    check_progress(root, present_scans, args.partial, checks, getattr(args, "pre_freeze", False))
    if args.zip:
        validate_zip(args.zip, root, args.partial, checks)
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output_root", type=Path)
    parser.add_argument("source_texts_root", type=Path, nargs="?")
    parser.add_argument("--zip", type=Path, help="also validate an assembled ZIP against the output directory")
    parser.add_argument("--partial", action="store_true", help="allow unfinished scans in a checkpoint")
    parser.add_argument("--pre-freeze", action="store_true", help="strict final readiness, deferring only freeze-marker and hash-presence requirements")
    args = parser.parse_args()
    if args.partial and args.pre_freeze:
        parser.error("--partial and --pre-freeze are mutually exclusive")
    checks = validate(args)
    for warning in checks.warnings:
        print("WARNING:", warning)
    for error in checks.errors:
        print("ERROR:", error)
    print(f"Mechanical validation: {len(checks.errors)} error(s), {len(checks.warnings)} warning(s).")
    print("No manuscript reading, mathematical claim, or completeness of ink transcription was assessed.")
    return 1 if checks.errors else 0


if __name__ == "__main__":
    sys.exit(main())
