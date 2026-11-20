#!/usr/bin/env python3
"""Validate the package's structure without evaluating its readings.

Usage:
    python scripts/validate_package.py WORK_DIR \
        --source-marks /path/to/MARKS.tsv --zip /path/to/package.zip

Exit codes: 0 = requested checks verified; 1 = structural errors;
2 = no structural errors, but one or more checks lack their evidence.

Only file/page mappings, internal scan labels, lexical brace balance, table
schemas/counts and supplied value vocabularies, mark-ID order and associations,
the specified rebuild convention, progress/crop records, the supplied
literal macro blacklist, archive membership, and SHA256 digests are checked.
No OCR, TeX compilation, proof checking, or interpretation of readings occurs.
Table contents and transcription excerpts are never printed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import runpy
import sys
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path


PREFIX = "SP64_C13_15+16"
SCANS = {
    "15": ("180", "183", "184", "185", "187", "189", "190", "191", "192", "193", "194"),
    "16": tuple(f"{number:03d}" for number in range(3, 17)),
}
PAGE_KEYS = tuple((cote, scan) for cote, scans in SCANS.items() for scan in scans)
PAGE_FILES = tuple(f"pages/{cote}_scan{scan}.tex" for cote, scan in PAGE_KEYS)
COMBINED = f"{PREFIX}_transcription.tex"
MARK_COUNT = 151
DECISION_CHOICES = {"first", "alternative", "other", "undecided"}
CONFIDENCE_LEVELS = {"high", "medium", "low"}
REFUTED_EVENT_TYPES = {
    "refuted, with the refined statement's id",
    "refuted, with the refined statement’s id",
}
CHECK_EVENT_TYPES = {
    "targeted proof check", "independent re-proof", "computation or formal certificate",
    "used and rechecked in this run", "carried as background without fault found",
} | REFUTED_EVENT_TYPES
INVENTORY_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}
KNOWN_H_ONLY_MACROS = {"note", "struck", "add", "marginal", "ill", "unftnt"}
TABLE_SCHEMAS = {
    f"{PREFIX}_collation.tsv": (
        "folder", "their_page", "our_scan", "line", "their_reading",
        "codex_reading", "final_reading", "scan_shows", "kind",
        "marked_in_H", "confidence",
    ),
    f"{PREFIX}_inventory.csv": (
        "scan", "sheet_kind", "hand", "element", "kind", "position",
        "first_words_or_objects", "transcribed",
    ),
    "decisions.tsv": (
        "id", "cote", "scan", "decision", "reading", "what the ink shows",
        "crop", "confidence",
    ),
    "CHECK_EVENTS.tsv": ("statement_id", "date", "who", "type", "outcome"),
}
OPTIONAL_TABLE_SCHEMAS = {
    "visual_audit.tsv": ("cote", "scan", "audited_UTC", "reader", "findings"),
    "cancelled_doubt_review.tsv": (
        "cote", "scan", "C_occurrence", "C_line", "C_mark", "final_reading",
        "disposition", "evidence", "confidence",
    ),
    "certainty_only.tsv": ("scan", "line", "old_mark", "reading", "evidence", "confidence"),
    "remaining_doubts.tsv": ("scan", "line", "reading", "alternatives", "confidence"),
    "changes_records.tsv": (
        "cote", "scan", "place", "C", "H", "final", "scan_shows", "confidence",
        "kind", "against_C", "against_H", "crop", "consequential",
    ),
}
DOCUMENTS = tuple(
    f"{PREFIX}_{suffix}.md"
    for suffix in ("changes", "doubts", "notes", "hand_log", "sheet_feedback")
)
SUPPORT_TSVS = {
    "changes_records.tsv", "notation.tsv", "remaining_doubts.tsv",
    "abbreviations.tsv", "audit_notes.tsv", "certainty_only.tsv", "cancelled_doubt_review.tsv", "visual_audit.tsv",
}
REQUIRED_FILES = PAGE_FILES + (COMBINED,) + tuple(TABLE_SCHEMAS) + DOCUMENTS + ("progress.log",)
IMAGE_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".jpe", ".gif", ".webp", ".bmp", ".tif",
    ".tiff", ".heic", ".heif", ".avif", ".ico", ".svg", ".pdf", ".jp2",
    ".j2k", ".pbm", ".pgm", ".ppm", ".pnm", ".eps", ".ps", ".psd",
    ".xcf", ".raw", ".dng",
}
ARCHIVE_SUFFIXES = {".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar", ".tgz"}
PROHIBITED_COMPONENT = re.compile(
    r"(?:^|[_.+ -])(?:sources?|witness(?:es)?|scans?|images?|crops?|"
    r"checkpoints?|backups?|previous|earlier|__pycache__)(?:$|[_.+ -])",
    re.IGNORECASE,
)
PROGRESS = re.compile(
    r"^(?P<prefix>audited[ \t]+)?scan[ \t]+(?P<scan>[0-9]{3})[ \t]+"
    r"(?P<status>done|audited)[ \t]+"
    r"(?P<timestamp>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})"
    r"[ \t]+UTC(?:[ \t]+cote[ \t]+(?P<cote>[0-9]+))?[ \t]*$"
)


class Report:
    def __init__(self) -> None:
        self.errors = 0
        self.unverified = 0
        self.passes = 0

    def ok(self, message: str) -> None:
        self.passes += 1
        print(f"PASS: {message}")

    def error(self, message: str) -> None:
        self.errors += 1
        print(f"ERROR: {message}")

    def unknown(self, message: str) -> None:
        self.unverified += 1
        print(f"UNVERIFIED: {message}")

    def finish(self) -> int:
        print(
            f"\nSummary: {self.passes} passed checks; {self.errors} structural errors; "
            f"{self.unverified} unverified checks."
        )
        print(
            "Scope: file/page mappings, internal labels, lexical braces, schemas and supplied value vocabularies, row counts and ID associations/order, "
            "the specified concatenation convention, recorded progress/crops, the supplied "
            "literal macro blacklist, archive membership, and checksums."
        )
        print(
            "Outside this validator's scope: reading accuracy, witness fidelity, "
            "mathematical correctness, editorial judgment, and whether recorded "
            "reading or auditing actually occurred."
        )
        return 1 if self.errors else (2 if self.unverified else 0)


def read_bytes(path: Path, report: Report, label: str) -> bytes | None:
    try:
        return path.read_bytes()
    except OSError as exc:
        report.error(f"{label}: cannot read file ({type(exc).__name__}).")
        return None


def parse_table(
    data: bytes, delimiter: str, schema: tuple[str, ...] | None,
    report: Report, label: str,
) -> tuple[tuple[str, ...], list[dict[str, str]]] | None:
    try:
        stream = io.StringIO(data.decode("utf-8-sig"), newline="")
        reader = csv.reader(stream, delimiter=delimiter, strict=True)
        raw_header = next(reader, None)
        if raw_header is None:
            report.error(f"{label}: empty table; header absent.")
            return None
        header = tuple(raw_header)
        if len(header) != len(set(header)):
            report.error(f"{label}: duplicate header fields.")
            return None
        if schema is not None and header != schema:
            report.error(f"{label}: header/order mismatch; expected {','.join(schema)}.")
            return None
        rows = []
        invalid_rows = 0
        for row_number, row in enumerate(reader, start=2):
            if len(row) != len(header):
                report.error(
                    f"{label}: logical row {row_number} has {len(row)} fields; "
                    f"expected {len(header)}."
                )
                invalid_rows += 1
                continue
            rows.append(dict(zip(header, row)))
        if invalid_rows:
            return None
        return header, rows
    except (UnicodeError, csv.Error):
        report.error(f"{label}: UTF-8 decoding or delimited-table parsing failed.")
        return None


def check_files(work: Path, report: Report) -> set[str]:
    missing = [name for name in REQUIRED_FILES if not (work / name).is_file()]
    if missing:
        report.error("Missing required files: " + ", ".join(missing))
    else:
        report.ok(f"All {len(REQUIRED_FILES)} required files are present.")
    empty = [name for name in REQUIRED_FILES if (work / name).is_file() and (work / name).stat().st_size == 0]
    if empty:
        report.error("Empty required files: " + ", ".join(empty))
    tex_files = {
        path.relative_to(work).as_posix()
        for path in work.rglob("*")
        if path.suffix.lower() == ".tex" and (path.is_file() or path.is_symlink())
    }
    extras = sorted(tex_files - set(PAGE_FILES) - {COMBINED})
    candidates = tex_files - {COMBINED}
    absent = sorted(set(PAGE_FILES) - tex_files)
    if extras:
        report.error("Unexpected local TeX paths outside the exact page/combined mapping: " + ", ".join(extras))
    if absent:
        report.error("Expected page paths absent from the local TeX enumeration: " + ", ".join(absent))
    if not extras and not absent and len(candidates) == 25:
        report.ok("Exactly the specified 25 page filenames are present.")
    approved = set(REQUIRED_FILES)
    approved.update(p.name for p in work.glob("*.md") if p.is_file())
    approved.update(p.relative_to(work).as_posix() for p in (work / "scripts").glob("*.py") if p.is_file())
    approved.update(name for name in SUPPORT_TSVS if (work / name).is_file())
    if (work / "hashes.tsv").is_file():
        approved.add("hashes.tsv")
    return approved


def check_combined(work: Path, report: Report) -> None:
    if any(not (work / name).is_file() for name in PAGE_FILES + (COMBINED,)):
        report.unknown("Concatenation: one or more input files are unavailable.")
        return
    parts = []
    previous_cote = None
    for key, name in zip(PAGE_KEYS, PAGE_FILES):
        data = read_bytes(work / name, report, name)
        if data is None:
            report.unknown("Concatenation: one or more page files could not be read.")
            return
        try:
            with io.TextIOWrapper(io.BytesIO(data), encoding="utf-8", newline=None) as handle:
                page_text = handle.read()
        except UnicodeError:
            report.error(f"{name}: UTF-8 decoding failed during the concatenation check.")
            return
        cote, _ = key
        if cote != previous_cote:
            parts.append("\\cotefile{" + cote + "}\n")
        parts.append(page_text.rstrip() + "\n")
        previous_cote = cote
    combined = read_bytes(work / COMBINED, report, COMBINED)
    if combined is None:
        return
    expected = "\n".join(parts).encode("utf-8")
    if combined == expected:
        report.ok(
            "Combined transcription matches workflow.rebuild(): page order, cote wrappers, "
            "each page's rstrip() plus one newline, and one separator newline."
        )
    else:
        report.error(
            "Combined transcription differs from the specified workflow.rebuild() convention "
            f"(combined {len(combined)} bytes; expected {len(expected)} bytes)."
        )


def decimal_scan(value: str) -> int | None:
    """Map an ASCII digit-only token to its base-10 integer for comparisons."""
    return int(value) if re.fullmatch(r"[0-9]+", value) else None


def check_page_labels_and_braces(work: Path, report: Report) -> None:
    helper = work / "scripts" / "audit_uncertainty.py"
    if not helper.is_file():
        report.unknown("Page-label/brace checks require scripts/audit_uncertainty.py for the declared lexer.")
        return
    try:
        namespace = runpy.run_path(str(helper))
        lex = namespace["lex"]
        skip_tex_space = namespace["skip_tex_space"]
    except (OSError, UnicodeError, SyntaxError, KeyError, ValueError):
        report.error("The shared lexer could not be loaded for page-label/brace checks.")
        return
    expected_scans = {name: int(scan) for name, (_, scan) in zip(PAGE_FILES, PAGE_KEYS)}
    checked = balanced = labelled = 0
    for name in PAGE_FILES + (COMBINED,):
        path = work / name
        if not path.is_file():
            continue
        data = read_bytes(path, report, name)
        if data is None:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeError:
            report.error(f"{name}: UTF-8 decoding failed during page-label/brace checks.")
            continue
        checked += 1
        tokens, lexical_issues = lex(text)
        brace_errors = 0
        stack = []
        openings = set()
        closing_for = {}
        for token in tokens:
            if token.kind == "open":
                stack.append(token.start)
                openings.add(token.start)
            elif token.kind == "close":
                if stack:
                    closing_for[stack.pop()] = token.start
                else:
                    report.error(f"{name}: unmatched closing brace at character offset {token.start}.")
                    brace_errors += 1
        for offset in stack:
            report.error(f"{name}: unmatched opening brace at character offset {offset}.")
            brace_errors += 1
        for issue, offset in lexical_issues:
            report.error(f"{name}: lexical issue {issue} at character offset {offset}.")
            brace_errors += 1
        balanced += int(brace_errors == 0)
        if name not in expected_scans:
            continue
        labels = [token for token in tokens if token.kind == "command" and token.value == "scanpage"]
        label_errors = 0
        if not labels:
            report.error(f"{name}: no literal internal \\scanpage label was found.")
            label_errors += 1
        for token in labels:
            opening = skip_tex_space(text, token.end)
            if opening not in openings or opening not in closing_for:
                report.error(f"{name}: \\scanpage at character offset {token.start} lacks a balanced braced argument.")
                label_errors += 1
                continue
            argument = text[opening + 1:closing_for[opening]]
            value = decimal_scan(argument)
            if value is None:
                report.error(f"{name}: \\scanpage at character offset {token.start} requires an ASCII digit-only argument.")
                label_errors += 1
            elif value != expected_scans[name]:
                report.error(f"{name}: internal \\scanpage at character offset {token.start} disagrees with expected scan {expected_scans[name]}.")
                label_errors += 1
        labelled += int(bool(labels) and label_errors == 0)
    if checked != 26:
        report.unknown(f"Lexical page/combined coverage: {checked} of 26 transcription files were readable.")
    elif balanced == 26:
        report.ok("Lexical braces balance in all 25 pages and the combined transcription, respecting comments, escaped symbols, and recognized verbatim text.")
    if labelled == 25:
        report.ok("Every page contains its expected integer-valued internal scan label, with no differing literal scan labels; zero-padding is accepted.")


def check_tables(work: Path, source_marks: Path | None, report: Report) -> None:
    tables = {}
    for name, schema in {**TABLE_SCHEMAS, **OPTIONAL_TABLE_SCHEMAS}.items():
        if not (work / name).is_file():
            continue
        data = read_bytes(work / name, report, name)
        if data is None:
            continue
        parsed = parse_table(data, "," if name.endswith(".csv") else "\t", schema, report, name)
        if parsed is not None:
            tables[name] = parsed[1]
            report.ok(f"{name}: exact header, consistent field counts, {len(parsed[1])} data rows.")
    for name, rows in tables.items():
        schema = TABLE_SCHEMAS.get(name, OPTIONAL_TABLE_SCHEMAS.get(name, ()))
        if "confidence" not in schema:
            continue
        before = report.errors
        for number, row in enumerate(rows, start=2):
            if row["confidence"] not in CONFIDENCE_LEVELS:
                report.error(f"{name} logical row {number}: confidence must be high, medium, or low.")
        if report.errors == before:
            report.ok(f"{name}: confidence values use the documented high/medium/low vocabulary.")
    events = tables.get("CHECK_EVENTS.tsv")
    if events is not None:
        before = report.errors
        for number, row in enumerate(events, start=2):
            if row["type"] not in CHECK_EVENT_TYPES:
                report.error(f"CHECK_EVENTS.tsv logical row {number}: type is outside the supplied allowed strings.")
            if row["type"] in REFUTED_EVENT_TYPES and not row["outcome"].strip():
                report.error(f"CHECK_EVENTS.tsv logical row {number}: a refuted event requires a nonempty outcome.")
        if report.errors == before:
            report.ok("CHECK_EVENTS.tsv uses the allowed event strings; refuted outcomes are nonempty.")
    inventory = tables.get(f"{PREFIX}_inventory.csv")
    if inventory is not None:
        before = report.errors
        expected_inventory_pages = {(cote, int(scan)) for cote, scan in PAGE_KEYS}
        covered_inventory_pages = set()
        for number, row in enumerate(inventory, start=2):
            identity = re.fullmatch(r"(15|16)/([0-9]+)", row["scan"])
            key = (identity.group(1), decimal_scan(identity.group(2))) if identity else None
            if key not in expected_inventory_pages:
                report.error(f"Inventory logical row {number}: scan must identify one of the required cote/scan pages.")
            else:
                covered_inventory_pages.add(key)
            if row["kind"] not in INVENTORY_KINDS:
                report.error(f"Inventory logical row {number}: kind is outside the supplied vocabulary.")
            if row["sheet_kind"] not in SHEET_KINDS:
                report.error(f"Inventory logical row {number}: sheet_kind is outside the supplied vocabulary.")
            if row["transcribed"] != "yes":
                report.error(f"Inventory logical row {number}: transcribed must be exactly yes.")
        missing_inventory_pages = [f"{cote}/{scan}" for cote, scan in PAGE_KEYS if (cote, int(scan)) not in covered_inventory_pages]
        if missing_inventory_pages:
            report.error("Inventory has no row for required pages: " + ", ".join(missing_inventory_pages))
        if report.errors == before:
            report.ok("Inventory covers all 25 required pages, uses allowed kind/sheet_kind values, and every transcribed value is yes.")
    decisions = tables.get("decisions.tsv")
    if decisions is not None:
        before = report.errors
        for number, row in enumerate(decisions, start=2):
            if row["decision"] not in DECISION_CHOICES:
                report.error(f"decisions.tsv logical row {number}: decision must be first, alternative, other, or undecided.")
        if report.errors == before:
            report.ok("decisions.tsv uses the documented first/alternative/other/undecided vocabulary.")
        if len(decisions) != MARK_COUNT:
            report.error(f"decisions.tsv has {len(decisions)} data rows; expected {MARK_COUNT}.")
        else:
            report.ok(f"decisions.tsv contains {MARK_COUNT} data rows.")
        ids = [row["id"] for row in decisions]
        if any(value == "" for value in ids):
            report.error("decisions.tsv contains an empty mark ID.")
        duplicates = sum(count - 1 for count in Counter(ids).values() if count > 1)
        if duplicates:
            report.error(f"decisions.tsv contains {duplicates} repeated mark-ID occurrences.")
    if source_marks is None:
        candidate = work / "MARKS.tsv"
        source_marks = candidate if candidate.is_file() else None
    if source_marks is None:
        report.unknown("Source mark-ID coverage/order: provide --source-marks PATH (or a local MARKS.tsv).")
        return
    source_data = read_bytes(source_marks, report, "Source MARKS.tsv")
    if source_data is None:
        report.unknown("Source mark-ID coverage/order: source file could not be read.")
        return
    source = parse_table(source_data, "\t", None, report, "Source MARKS.tsv")
    if source is None:
        report.unknown("Source mark-ID coverage/order: source table could not be parsed.")
        return
    header, source_rows = source
    id_fields = [field for field in ("id", "mark_id", "ID", "MARK_ID", "mark", "Mark ID", "markid") if field in header]
    if len(id_fields) != 1:
        report.unknown("Source MARKS.tsv requires one recognizable ID column (id, mark_id, ID, MARK_ID, mark, Mark ID, or markid).")
        return
    source_ids = [row[id_fields[0]] for row in source_rows]
    if len(source_ids) != MARK_COUNT:
        report.error(f"Source MARKS.tsv has {len(source_ids)} data rows; expected {MARK_COUNT}.")
    if any(value == "" for value in source_ids) or len(set(source_ids)) != len(source_ids):
        report.error("Source MARKS.tsv contains empty or duplicate mark IDs.")
    if decisions is None:
        report.unknown("Source mark-ID coverage/order: decisions.tsv is unavailable or structurally invalid.")
        return
    decision_ids = [row["id"] for row in decisions]
    if decision_ids != source_ids:
        mismatches = sum(left != right for left, right in zip(decision_ids, source_ids)) + abs(len(decision_ids) - len(source_ids))
        report.error(f"decisions.tsv mark-ID sequence differs from source order at {mismatches} row positions.")
    elif len(source_ids) == MARK_COUNT and len(set(source_ids)) == MARK_COUNT and all(source_ids):
        report.ok(f"decisions.tsv has exactly one row for each of the {MARK_COUNT} source mark IDs, in source order.")
    if "cote" not in header or "scan" not in header:
        report.unknown("Source-to-decision page associations require cote and scan columns in source MARKS.tsv.")
        return
    if not all(source_ids) or len(set(source_ids)) != len(source_ids):
        report.unknown("Source-to-decision page associations cannot be resolved uniquely because source IDs are empty or repeated.")
        return
    source_by_id = {row[id_fields[0]]: (number, row) for number, row in enumerate(source_rows, start=2)}
    expected_pages = {(cote, int(scan)) for cote, scan in PAGE_KEYS}
    before_mapping = report.errors
    for number, row in enumerate(source_rows, start=2):
        scan_number = decimal_scan(row["scan"])
        if (row["cote"], scan_number) not in expected_pages:
            report.error(f"Source MARKS.tsv logical row {number}: cote/scan is outside the exact 25-page mapping.")
    for number, row in enumerate(decisions, start=2):
        found = source_by_id.get(row["id"])
        if found is None:
            report.error(f"decisions.tsv logical row {number}: ID has no source MARKS row for its page association.")
            continue
        source_number, source_row = found
        source_scan, decision_scan = decimal_scan(source_row["scan"]), decimal_scan(row["scan"])
        if source_scan is None or decision_scan is None:
            report.error(f"decisions.tsv logical row {number} / source row {source_number}: scan association requires ASCII digit-only values.")
        elif row["cote"] != source_row["cote"] or decision_scan != source_scan:
            report.error(f"decisions.tsv logical row {number}: cote/scan disagrees with the matching source MARKS ID row {source_number}.")
    if report.errors == before_mapping:
        report.ok("Every decision's cote and integer-valued scan agree with its source MARKS ID row; source associations lie in the exact 25-page mapping.")


def check_progress(work: Path, report: Report) -> None:
    path = work / "progress.log"
    if not path.is_file():
        report.unknown("Progress coverage: progress.log is unavailable.")
        return
    data = read_bytes(path, report, "progress.log")
    if data is None:
        return
    try:
        lines = data.decode("utf-8-sig").splitlines()
    except UnicodeError:
        report.error("progress.log: UTF-8 decoding failed.")
        return
    recorded = {"done": set(), "audited": set()}
    timestamps = {"done": {}, "audited": {}}
    for line_number, line in enumerate(lines, start=1):
        match = PROGRESS.fullmatch(line)
        if match is None:
            if re.search(r"\b(?:done|audited)\b", line) and re.search(r"\bscan\b", line):
                report.error(f"progress.log line {line_number}: unrecognized completion/audit entry format.")
            continue
        if match["prefix"] and match["status"] != "audited":
            report.error(f"progress.log line {line_number}: audit prefix disagrees with status.")
            continue
        try:
            timestamp = datetime.strptime(match["timestamp"], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            report.error(f"progress.log line {line_number}: invalid UTC timestamp.")
            continue
        scan, cote = match["scan"], match["cote"]
        possible = [key for key in PAGE_KEYS if key[1] == scan and (cote is None or key[0] == cote)]
        if len(possible) != 1:
            report.error(f"progress.log line {line_number}: scan/cote does not identify exactly one required page.")
            continue
        recorded[match["status"]].add(possible[0])
        timestamps[match["status"]].setdefault(possible[0], []).append(timestamp)
    for status, keys in recorded.items():
        missing = [f"{cote}_scan{scan}" for cote, scan in PAGE_KEYS if (cote, scan) not in keys]
        if missing:
            report.error(f"Missing '{status}' progress entries: " + ", ".join(missing))
        else:
            report.ok(f"All 25 pages have a valid timestamped '{status}' progress entry.")
    chronologically_audited = 0
    for key in PAGE_KEYS:
        done_times = timestamps["done"].get(key, [])
        audit_times = timestamps["audited"].get(key, [])
        if not done_times or not audit_times:
            continue
        if max(audit_times) <= max(done_times):
            report.error(f"Progress for {key[0]}/{key[1]} requires an audited timestamp strictly later than its latest done timestamp.")
        else:
            chronologically_audited += 1
    if chronologically_audited == 25:
        report.ok("Every page has an audited timestamp strictly later than its latest done timestamp.")


def check_crop_register(work: Path, report: Report) -> None:
    changes = work / f"{PREFIX}_changes.md"
    helper = work / "scripts" / "report_helpers.py"
    progress = work / "progress.log"
    if not changes.is_file() or not helper.is_file() or not progress.is_file():
        report.unknown("Crop-register freshness: changes.md, progress.log, or report_helpers.py is unavailable.")
        return
    try:
        functions = runpy.run_path(str(helper))
        expected = functions["crop_register_markdown"](work)
        start, end = functions["CROP_START"], functions["CROP_END"]
        actual = changes.read_text(encoding="utf-8")
        if actual.count(start) != 1 or actual.count(end) != 1:
            report.error("changes.md must contain exactly one managed crop-register block.")
            return
        left, right = actual.index(start), actual.index(end)
        if right < left or actual[left:right + len(end)] != expected:
            report.error("The crop-register block differs from the complete current progress-log rendering.")
            return
        count = sum(line.startswith("crop ") for line in progress.read_text(encoding="utf-8-sig").splitlines())
        report.ok(f"The crop register matches all {count} logged crop entries and the specified count-separation text.")
    except (OSError, UnicodeError, ValueError, KeyError):
        report.error("Crop-register freshness could not be checked because its helper, log, or managed block is invalid.")


def literal_control_words(text: str):
    """Read literal control words while skipping comments and verbatim text."""
    position = 0
    while position < len(text):
        character = text[position]
        if character == "%":
            newline = text.find("\n", position + 1)
            position = len(text) if newline == -1 else newline + 1
            continue
        if character != "\\":
            position += 1
            continue
        position += 1
        start = position
        while position < len(text) and (text[position] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@"):
            position += 1
        if position == start:
            position += 1
            continue
        command = text[start:position]
        yield command
        if command == "verb":
            if position < len(text) and text[position] == "*":
                position += 1
            if position < len(text) and text[position] not in "\r\n":
                closing = text.find(text[position], position + 1)
                if closing != -1:
                    position = closing + 1
        elif command == "begin":
            environment = re.match(r"\s*\{(verbatim\*?|Verbatim|lstlisting|minted)\}", text[position:])
            if environment:
                closing_marker = "\\end{" + environment.group(1) + "}"
                closing = text.find(closing_marker, position + environment.end())
                if closing != -1:
                    position = closing + len(closing_marker)


def check_forbidden_macros(work: Path, report: Report) -> None:
    before = report.errors
    checked = 0
    for name in PAGE_FILES:
        path = work / name
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            report.error(f"{name}: could not read page for the literal macro blacklist check.")
            continue
        forbidden = sorted(set(literal_control_words(content)) & KNOWN_H_ONLY_MACROS)
        if forbidden:
            report.error(f"{name}: known H-only commands present: " + ", ".join("\\" + name for name in forbidden))
        checked += 1
    if checked != 25:
        report.unknown(f"Literal macro blacklist coverage: {checked} of 25 page files were readable.")
    elif report.errors == before:
        report.ok("All 25 pages are free of literal uses of the six supplied H-only commands, outside comments and verbatim text.")


def unsafe_path(name: str) -> bool:
    parts = name.split("/")
    return (
        not name or name.startswith("/") or "\\" in name or "\x00" in name
        or bool(re.match(r"^[A-Za-z]:", name))
        or any(part in ("", ".", "..") for part in parts)
    )


def prohibited_path(name: str) -> str | None:
    parts = name.split("/")
    if len(parts) == 2 and parts[0] == "scripts" and parts[1].endswith(".py"):
        return None
    if len(parts) == 1 and parts[0].endswith(".md"):
        return None
    if any(part in (".git", ".venv", "__pycache__") or PROHIBITED_COMPONENT.search(part) for part in parts):
        return "source, witness, image, cache, or checkpoint path marker"
    suffix = Path(name).suffix.lower()
    if suffix in IMAGE_SUFFIXES:
        return "image/scan file extension"
    if suffix in ARCHIVE_SUFFIXES:
        return "nested archive"
    if suffix in {".pyc", ".pyo", ".bak", ".tmp", ".old", ".orig"}:
        return "cache, backup, or temporary file extension"
    return None


def check_hashes(
    data: bytes, available: set[str], get_data, required: set[str],
    report: Report, label: str,
) -> None:
    parsed = parse_table(data, "\t", ("file", "sha256"), report, label)
    if parsed is None:
        return
    before = report.errors
    seen = set()
    verified = 0
    for row_number, row in enumerate(parsed[1], start=2):
        name, digest = row["file"], row["sha256"]
        if unsafe_path(name):
            report.error(f"{label} row {row_number}: unsafe or empty relative path.")
            continue
        if name in seen:
            report.error(f"{label} row {row_number}: duplicate file entry.")
            continue
        seen.add(name)
        if not re.fullmatch(r"[0-9A-Fa-f]{64}", digest):
            report.error(f"{label} row {row_number}: malformed SHA256 digest.")
            continue
        if name not in available:
            report.error(f"{label} row {row_number}: referenced file is unavailable or outside the approved package.")
            continue
        payload = get_data(name)
        if payload is None:
            continue
        if hashlib.sha256(payload).hexdigest().lower() != digest.lower():
            report.error(f"{label} row {row_number}: SHA256 mismatch for {name}.")
        else:
            verified += 1
    uncovered = sorted(required - {"hashes.tsv"} - seen)
    if uncovered:
        report.unknown(f"{label}: checksum coverage absent for " + ", ".join(uncovered))
    if report.errors == before:
        report.ok(f"{label}: all {verified} listed SHA256 digests match their files.")


def check_local_hashes(work: Path, approved: set[str], report: Report) -> None:
    path = work / "hashes.tsv"
    if not path.is_file():
        report.unknown("Optional hashes.tsv is absent; local SHA256 checks were not performed.")
        return
    data = read_bytes(path, report, "hashes.tsv")
    if data is None:
        return
    available = {name for name in approved if (work / name).is_file()}

    def get_data(name: str) -> bytes | None:
        target = work / name
        try:
            target.resolve().relative_to(work.resolve())
        except (OSError, ValueError):
            report.error("hashes.tsv: referenced file resolves outside work_dir.")
            return None
        return read_bytes(target, report, f"hashes.tsv file {name}")

    check_hashes(data, available, get_data, approved, report, "hashes.tsv")


def check_zip(path: Path | None, work: Path, approved: set[str], report: Report) -> None:
    if path is None:
        report.unknown("Final ZIP membership and byte identity: provide --zip PATH.")
        return
    try:
        with zipfile.ZipFile(path) as archive:
            members = archive.infolist()
            file_members = [member for member in members if not member.is_dir()]
            if not file_members:
                report.error("Final ZIP has no files.")
                return
            raw_names = [member.filename for member in members]
            if len(raw_names) != len(set(raw_names)):
                report.error("Final ZIP contains duplicate member names.")
            first_parts = {member.filename.split("/")[0] for member in file_members}
            wrapper = ""
            if len(first_parts) == 1 and all("/" in member.filename for member in file_members):
                wrapper = next(iter(first_parts)) + "/"
            mapped = {}
            rejected = 0
            if wrapper and prohibited_path(wrapper[:-1]):
                report.error("Final ZIP uses a prohibited source/cache/checkpoint enclosing directory.")
                rejected += 1
            for member in members:
                raw = member.filename[:-1] if member.is_dir() else member.filename
                if unsafe_path(raw):
                    report.error("Final ZIP contains an unsafe member path.")
                    rejected += 1
                    continue
                mode = member.external_attr >> 16
                if (mode & 0o170000) == 0o120000:
                    report.error(f"Final ZIP contains a symbolic link: {raw}.")
                    rejected += 1
                    continue
                relative = raw[len(wrapper):] if wrapper and raw.startswith(wrapper) else raw
                if member.is_dir() and wrapper and raw == wrapper[:-1]:
                    continue
                reason = prohibited_path(relative)
                if reason:
                    report.error(f"Final ZIP member {relative}: prohibited {reason}.")
                    rejected += 1
                    continue
                if member.is_dir():
                    if relative not in {"scripts", "pages"}:
                        report.error(f"Final ZIP contains an unapproved directory: {relative}.")
                        rejected += 1
                    continue
                if relative not in approved and relative != "hashes.tsv":
                    report.error(f"Final ZIP contains an unapproved file: {relative}.")
                    rejected += 1
                    continue
                if relative in mapped:
                    report.error(f"Final ZIP repeats a package-relative filename: {relative}.")
                    rejected += 1
                    continue
                mapped[relative] = member
            missing = sorted(approved - set(mapped))
            if missing:
                report.error("Final ZIP omits deliverables, documentation, or scripts: " + ", ".join(missing))
            if not rejected and not missing:
                report.ok(f"Final ZIP contains the approved {len(mapped)} files and no prohibited path types.")
            payloads = {}
            compared = 0
            for name, member in mapped.items():
                try:
                    payloads[name] = archive.read(member)
                except (OSError, RuntimeError, zipfile.BadZipFile, NotImplementedError):
                    report.error(f"Final ZIP member {name}: decompression or CRC check failed.")
                    continue
                local_path = work / name
                if local_path.is_file():
                    local = read_bytes(local_path, report, f"Local archive counterpart {name}")
                    if local is not None:
                        if local != payloads[name]:
                            report.error(f"Final ZIP member differs from work_dir bytes: {name}.")
                        else:
                            compared += 1
                else:
                    report.unknown(f"Final ZIP member has no local counterpart for byte comparison: {name}.")
            if compared == len(mapped) and not missing and not rejected:
                report.ok(f"All {compared} archived files pass CRC reading and match work_dir byte for byte.")
            if "hashes.tsv" in payloads:
                check_hashes(
                    payloads["hashes.tsv"], set(payloads), payloads.get,
                    approved, report, "Final ZIP hashes.tsv",
                )
            else:
                report.unknown("Final ZIP has no hashes.tsv; archive SHA256 checks were not performed.")
    except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile):
        report.error("Final ZIP is unavailable or cannot be opened as a ZIP archive.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("work_dir", type=Path, help="Directory containing the final page and documentation files")
    parser.add_argument("--source-marks", type=Path, help="Original MARKS.tsv; its exact ID sequence is checked")
    parser.add_argument("--zip", dest="zip_path", type=Path, help="Final ZIP to check against work_dir")
    args = parser.parse_args(argv)
    report = Report()
    work = args.work_dir.expanduser().resolve()
    if not work.is_dir():
        report.error("work_dir is unavailable or is not a directory.")
        return report.finish()
    approved = check_files(work, report)
    check_combined(work, report)
    check_page_labels_and_braces(work, report)
    check_tables(work, args.source_marks, report)
    check_progress(work, report)
    check_crop_register(work, report)
    check_forbidden_macros(work, report)
    check_local_hashes(work, approved, report)
    check_zip(args.zip_path, work, approved, report)
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
