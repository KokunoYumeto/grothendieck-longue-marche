#!/usr/bin/env python3
"""Read-only structural validation for the SP65_C13_16 deliverable.

This checks files, table schemas, row identities, ordering, archive contents,
and recorded hashes. It does not assess a reading, inspect a scan, perform OCR,
compile TeX, or certify that a human/model actually performed a reading.

Example (from any directory):
    python /path/to/SP65_C13_16/scripts/validate.py \
        --source /path/to/source/SP65_C13_16_texts \
        --zip /path/to/SP65_C13_16.zip

The source directory is used only for filename listings, H availability, and
MARKS.tsv's id/cote/scan fields. Witness page contents are never opened.
The delivered page contents are compared as opaque text/bytes.

Recommended progress hash syntax:
    sha256 <64 hexadecimal characters> pages/16_scan017.tex
    sha256 <64 hexadecimal characters> SP65_C13_16_transcription.tex
    transcription frozen YYYY-MM-DD HH:MM:SS UTC
    frozen hashes checked unchanged YYYY-MM-DD HH:MM:SS UTC

The hash lines may precede or follow the freeze line. Only relative paths to
the 25 page files and the combined fragment are accepted as frozen targets.
Use --before-freeze after both reading passes to check the other requirements
before writing frozen hashes.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path, PurePosixPath


PREFIX = "SP65_C13_16"
EXPECTED_SCANS = (
    17, 18, 20, 22, 25, 27, 28, 29, 33, 34, 36, 38, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
)
REQUIRED_FILES = (
    f"{PREFIX}_transcription.tex",
    f"{PREFIX}_changes.md",
    f"{PREFIX}_collation.tsv",
    "decisions.tsv",
    f"{PREFIX}_doubts.md",
    f"{PREFIX}_inventory.csv",
    f"{PREFIX}_notes.md",
    "CHECK_EVENTS.tsv",
    "progress.log",
    f"{PREFIX}_sheet_feedback.md",
    f"{PREFIX}_hand_log.md",
)
DECISION_COLUMNS = (
    "id", "cote", "scan", "decision", "reading", "what the ink shows",
    "crop", "confidence",
)
COLLATION_COLUMNS = (
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind",
    "marked_in_H", "confidence",
)
INVENTORY_COLUMNS = (
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
CONFIDENCES = {"high", "medium", "low"}
DECISIONS = {"first", "alternative", "other", "undecided"}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list",
    "cancelled_draft", "cover",
}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion",
    "deletion",
}
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission",
    "text not on the page", "deletion state (struck given live or live given struck)",
    "deletion state", "insertion or placement",
    "abbreviation expanded or spelling modernised",
    "readable ink left as \\ill{}", "readable ink left as `\\ill{}`",
    "drawing or diagram", "other",
}
EVENT_TYPES = {
    "targeted proof check", "independent re-proof",
    "computation or formal certificate", "used and rechecked in this run",
    "carried as background without fault found",
}
STAMP_RE = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
STAMP_FORMAT = "%Y-%m-%d %H:%M:%S UTC"


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.facts: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def fact(self, message: str) -> None:
        self.facts.append(message)

    def finish(self) -> int:
        for message in self.facts:
            print(f"OK: {message}")
        for message in self.warnings:
            print(f"WARNING: {message}")
        for message in self.errors:
            print(f"ERROR: {message}")
        print(
            f"Structural validation: {len(self.errors)} error(s), "
            f"{len(self.warnings)} warning(s)."
        )
        print("Scope: structure and bytes only; no certification of readings or mathematics.")
        return 1 if self.errors else 0


def read_table(path: Path, delimiter: str, columns: tuple[str, ...] | None,
               report: Report) -> list[dict[str, str]] | None:
    if not path.is_file():
        return None  # Required-file check reports the missing path once.
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, delimiter=delimiter)
            if columns is not None and tuple(reader.fieldnames or ()) != columns:
                report.error(f"{path.name}: header must be {list(columns)!r}; got {reader.fieldnames!r}")
                return None
            if reader.fieldnames is None:
                report.error(f"{path.name}: missing header")
                return None
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        report.error(f"{path.name}: cannot read table: {exc}")
        return None
    for number, row in enumerate(rows, 2):
        if None in row or any(value is None for value in row.values()):
            report.error(f"{path.name}:{number}: row width differs from header")
    return rows


def number(value: object, label: str, report: Report) -> int | None:
    if not isinstance(value, str) or not re.fullmatch(r"\d+", value.strip()):
        report.error(f"{label}: expected decimal integer, got {value!r}")
        return None
    return int(value)


def source_metadata(source: Path, report: Report):
    page_dir = source / "pages"
    names = sorted(p.name for p in page_dir.glob("*.tex"))
    expected_names = [f"16_scan{scan:03d}.tex" for scan in EXPECTED_SCANS]
    if names != expected_names:
        report.error(f"Source page filename listing differs from the expected 25 names: {names!r}")
    h_names = {p.name for p in (source / "hua").glob("*.tex")}
    h_scans = {
        scan for scan in EXPECTED_SCANS if f"hua_16_scan{scan:03d}.tex" in h_names
    }
    if len(h_scans) != 21:
        report.error(f"Source H filename listing has {len(h_scans)} matched pages, expected 21")
    path = source / "MARKS.tsv"
    if not path.is_file():
        report.error(f"Source marks file missing: {path}")
        marks = None
    else:
        # Only the structural identity fields are retained; no readings are inspected.
        rows = read_table(path, "\t", None, report)
        marks = [] if rows is not None else None
        if rows is not None:
            for row in rows:
                try:
                    marks.append((row["id"], int(row["cote"]), int(row["scan"])))
                except (KeyError, ValueError, TypeError):
                    report.error("Source MARKS.tsv has an invalid id/cote/scan row")
        if marks is not None and len(marks) != 211:
            report.error(f"Source MARKS.tsv contains {len(marks)} rows, expected 211")
    return expected_names, h_scans, marks


def validate_pages(root: Path, expected_names: list[str], report: Report) -> None:
    names = sorted(p.name for p in (root / "pages").glob("*.tex"))
    missing = sorted(set(expected_names) - set(names))
    extra = sorted(set(names) - set(expected_names))
    if missing:
        report.error(f"Missing consolidated page files: {', '.join(missing)}")
    if extra:
        report.error(f"Unexpected consolidated page files: {', '.join(extra)}")
    if missing or extra:
        return
    combined_path = root / f"{PREFIX}_transcription.tex"
    if not combined_path.is_file():
        return
    try:
        combined = combined_path.read_text(encoding="utf-8")
        chunks = [(root / "pages" / name).read_text(encoding="utf-8") for name in expected_names]
    except (OSError, UnicodeError) as exc:
        report.error(f"Cannot compare transcription files: {exc}")
        return
    rest = combined.strip("\r\n \t")
    prefix = re.match(r"\\cotefile\{16\}(?:[ \t]*\r?\n)*", rest)
    if prefix:
        rest = rest[prefix.end():].lstrip("\r\n \t")
    for name, chunk in zip(expected_names, chunks):
        fragment = chunk.strip("\r\n \t")
        if not fragment:
            report.error(f"pages/{name}: empty fragment")
            continue
        if not rest.startswith(fragment):
            report.error(f"Combined transcription differs from ordered page contents at pages/{name}")
            return
        rest = rest[len(fragment):].lstrip("\r\n \t")
    if rest:
        report.error("Combined transcription contains content after the last page fragment")
    elif all(chunk.strip() for chunk in chunks):
        report.fact("Combined fragment matches all 25 page files in source filename order")
    if re.search(r"\\(?:documentclass|begin\{document\}|end\{document\})", combined):
        report.error("Combined transcription contains a document wrapper; a fragment is required")


def validate_decisions(root: Path, marks, report: Report) -> None:
    rows = read_table(root / "decisions.tsv", "\t", DECISION_COLUMNS, report)
    if rows is None:
        return
    identities = []
    for n, row in enumerate(rows, 2):
        label = f"decisions.tsv:{n}"
        cote = number(row.get("cote"), f"{label} cote", report)
        scan = number(row.get("scan"), f"{label} scan", report)
        identities.append((row.get("id"), cote, scan))
        if row.get("decision") not in DECISIONS:
            report.error(f"{label}: invalid decision {row.get('decision')!r}")
        if row.get("confidence") not in CONFIDENCES:
            report.error(f"{label}: invalid confidence {row.get('confidence')!r}")
        for field in ("reading", "what the ink shows", "crop"):
            if not (row.get(field) or "").strip():
                report.error(f"{label}: empty {field!r}")
        crop = row.get("crop") or ""
        if crop and crop != "page":
            match = re.search(
                r"(\d+)\D+[\[(]\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*[\])]",
                crop,
            )
            if not match:
                report.error(f"{label}: crop must be 'page' or contain scan and (x0, y0, x1, y1)")
            else:
                crop_scan, x0, y0, x1, y1 = map(int, match.groups())
                if crop_scan != scan:
                    report.error(f"{label}: crop scan {crop_scan} differs from row scan {scan}")
                if not (x0 < x1 and y0 < y1):
                    report.error(f"{label}: invalid crop rectangle")
    if marks is not None:
        if identities != marks:
            first = next((i for i, pair in enumerate(zip(identities, marks), 1) if pair[0] != pair[1]), None)
            report.error(
                f"decisions.tsv: identities/order differ from MARKS.tsv "
                f"({len(identities)} versus {len(marks)} rows; first unequal row {first})"
            )
        else:
            report.fact(f"All {len(rows)} doubt-mark decisions match original IDs, cotes, scans, and order")


def validate_collation(root: Path, h_scans: set[int], report: Report) -> None:
    path = root / f"{PREFIX}_collation.tsv"
    rows = read_table(path, "\t", COLLATION_COLUMNS, report)
    if rows is None:
        return
    for n, row in enumerate(rows, 2):
        label = f"{path.name}:{n}"
        scan = number(row.get("our_scan"), f"{label} our_scan", report)
        their_page = number(row.get("their_page"), f"{label} their_page", report)
        if scan not in h_scans:
            report.error(f"{label}: H has no supplied page for scan {scan}")
        if scan is not None and their_page is not None and their_page != scan - 1:
            report.error(f"{label}: their_page must equal our_scan - 1")
        if row.get("folder") != "16":
            report.error(f"{label}: folder must be '16'")
        if row.get("kind") not in COLLATION_KINDS:
            report.error(f"{label}: unknown collation kind {row.get('kind')!r}")
        if row.get("confidence") not in CONFIDENCES:
            report.error(f"{label}: invalid confidence {row.get('confidence')!r}")
        if (row.get("marked_in_H") or "").lower() not in {"yes", "no"}:
            report.error(f"{label}: marked_in_H must say yes or no")
        for field in ("line", "scan_shows"):
            if not (row.get(field) or "").strip():
                report.error(f"{label}: empty {field!r}")
    report.fact(f"Read {len(rows)} H-collation rows; allowed source coverage is 21 pages")


def validate_inventory(root: Path, report: Report) -> None:
    path = root / f"{PREFIX}_inventory.csv"
    rows = read_table(path, ",", INVENTORY_COLUMNS, report)
    if rows is None:
        return
    scans = []
    for n, row in enumerate(rows, 2):
        label = f"{path.name}:{n}"
        scan = number(row.get("scan"), f"{label} scan", report)
        if scan is not None:
            scans.append(scan)
        if scan not in EXPECTED_SCANS:
            report.error(f"{label}: unknown scan {scan}")
        if row.get("sheet_kind") not in SHEET_KINDS:
            report.error(f"{label}: invalid sheet_kind {row.get('sheet_kind')!r}")
        if row.get("kind") not in ELEMENT_KINDS:
            report.error(f"{label}: invalid element kind {row.get('kind')!r}")
        if row.get("transcribed") != "yes":
            report.error(f"{label}: transcribed must be 'yes'")
        for field in ("hand", "element", "position", "first_words_or_objects"):
            if not (row.get(field) or "").strip():
                report.error(f"{label}: empty {field!r}")
    missing = sorted(set(EXPECTED_SCANS) - set(scans))
    if missing:
        report.error(f"Inventory lacks scans: {missing}")
    if scans != sorted(scans):
        report.error("Inventory scan groups are not in page order")
    report.fact(f"Read {len(rows)} inventory elements across {len(set(scans))} scans")


def parse_stamp(text: str, label: str, report: Report) -> datetime | None:
    try:
        return datetime.strptime(text, STAMP_FORMAT)
    except ValueError:
        report.error(f"{label}: invalid UTC timestamp {text!r}")
        return None


def hash_entry(line: str):
    patterns = (
        r"(?:sha-?256\s+)?([0-9a-fA-F]{64})\s+\*?(.+)",
        r"sha-?256\s+(.+?)\s+([0-9a-fA-F]{64})",
        r"sha-?256\s*\((.+?)\)\s*=\s*([0-9a-fA-F]{64})",
    )
    for i, pattern in enumerate(patterns):
        match = re.fullmatch(pattern, line.strip(), flags=re.IGNORECASE)
        if match:
            digest, name = match.groups() if i == 0 else match.groups()[::-1]
            return name.strip().replace("\\", "/"), digest.lower()
    return None


def validate_progress(root: Path, expected_names: list[str], report: Report,
                      require_frozen: bool = True) -> None:
    path = root / "progress.log"
    if not path.is_file():
        return
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        report.error(f"Cannot read progress.log: {exc}")
        return
    if not lines or not re.fullmatch(STAMP_RE, lines[0]):
        report.error("progress.log: first line must be the starting UTC timestamp alone")
        start = None
    else:
        start = parse_stamp(lines[0], "progress.log:1", report)
    done = []
    audited = []
    freeze = []
    hashes: dict[str, list[tuple[int, str]]] = {}
    unchanged = []
    for index, line in enumerate(lines, 1):
        match = re.fullmatch(rf"scan\s+(\d+)\s+done\s+({STAMP_RE})\s+cote\s+(\d+)", line)
        if match:
            scan, stamp, cote = match.groups()
            done.append((int(scan), index, parse_stamp(stamp, f"progress.log:{index}", report)))
            if int(cote) != 16:
                report.error(f"progress.log:{index}: wrong cote {cote}")
        match = re.fullmatch(rf"scan\s+(\d+)\s+audited\s+({STAMP_RE})", line)
        if match:
            scan, stamp = match.groups()
            audited.append((int(scan), index, parse_stamp(stamp, f"progress.log:{index}", report)))
        match = re.fullmatch(rf"transcription frozen\s+({STAMP_RE})", line)
        if match:
            freeze.append((index, parse_stamp(match.group(1), f"progress.log:{index}", report)))
        entry = hash_entry(line)
        if entry:
            name, digest = entry
            hashes.setdefault(name, []).append((index, digest))
        if re.search(r"hash", line, flags=re.IGNORECASE) and re.search(r"unchanged", line, flags=re.IGNORECASE):
            unchanged.append(index)
    for label, events in (("done", done), ("audited", audited)):
        scans = [item[0] for item in events]
        if scans != list(EXPECTED_SCANS):
            report.error(f"progress.log: {label} scans must occur once each in order; got {scans}")
    if done and audited and max(item[1] for item in done) >= min(item[1] for item in audited):
        report.error("progress.log: the second-reading entries begin before all first readings finish")
    dated = [(1, start)] + [(i, t) for _, i, t in done + audited] + freeze
    dated = sorted((i, t) for i, t in dated if t is not None)
    if any(b[1] < a[1] for a, b in zip(dated, dated[1:])):
        report.error("progress.log: recorded timestamps go backwards")
    if not require_frozen:
        report.fact("Reading-pass entries inspected; freeze/hash requirements deferred")
        return
    if len(freeze) != 1:
        report.error(f"progress.log: expected one 'transcription frozen' entry, got {len(freeze)}")
    elif audited and freeze[0][0] <= max(item[1] for item in audited):
        report.error("progress.log: transcription freeze must follow all second readings")
    if not unchanged:
        report.error("progress.log: missing explicit final statement that hashes were checked unchanged")
    elif freeze and unchanged[-1] <= freeze[-1][0]:
        report.error("progress.log: unchanged-hash check must follow the freeze")
    expected = [f"pages/{name}" for name in expected_names] + [f"{PREFIX}_transcription.tex"]
    for name in expected:
        entries = hashes.get(name, [])
        if not entries:
            report.error(f"progress.log: missing frozen SHA-256 for {name}")
            continue
        if len({digest for _, digest in entries}) != 1:
            report.error(f"progress.log: conflicting SHA-256 entries for {name}")
        target = root / name
        if target.is_file():
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            if digest != entries[0][1]:
                report.error(f"Frozen SHA-256 differs from current bytes: {name}")
    extras = sorted(set(hashes) - set(expected))
    if extras:
        report.warn(f"Additional hash targets in progress.log: {extras}")
    if all(name in hashes for name in expected):
        report.fact("Recorded SHA-256 entries cover all 25 pages and the combined transcription")


def validate_events(root: Path, report: Report) -> None:
    path = root / "CHECK_EVENTS.tsv"
    rows = read_table(path, "\t", None, report)
    if rows is None:
        return
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        fields = next(csv.reader(handle, delimiter="\t"), [])
    # The prompt specifies field meanings, not exact spelling for this table.
    normalized = {re.sub(r"[ _-]+", "_", field.strip().lower()): field for field in fields}
    required_groups = {
        "statement id": ("statement_id", "statement"),
        "date": ("date", "utc_date"),
        "who": ("who", "who_(model,_effort,_run)"),
        "type": ("type", "event_type", "check_type"),
        "outcome": ("outcome", "result"),
    }
    selected = {}
    for meaning, choices in required_groups.items():
        actual = next((normalized[key] for key in choices if key in normalized), None)
        if actual is None:
            if meaning == "who" and {"model", "effort", "run"}.issubset(normalized):
                selected[meaning] = None
            else:
                report.error(f"CHECK_EVENTS.tsv: missing field for {meaning!r}")
        else:
            selected[meaning] = actual
    for n, row in enumerate(rows, 2):
        for meaning, field in selected.items():
            if field is not None and not (row.get(field) or "").strip():
                report.error(f"CHECK_EVENTS.tsv:{n}: empty {meaning}")
        type_field = selected.get("type")
        event_type = row.get(type_field, "") if type_field else ""
        if event_type and event_type not in EVENT_TYPES and not event_type.startswith("refuted"):
            report.error(f"CHECK_EVENTS.tsv:{n}: unknown event type {event_type!r}")
    report.fact(f"Read {len(rows)} check-event rows (their evidential adequacy requires editorial review)")


def validate_archive(root: Path, archive: Path, expected_names: list[str], report: Report) -> None:
    if not archive.is_file():
        report.error(f"ZIP not found: {archive}")
        return
    required = set(REQUIRED_FILES) | {f"pages/{name}" for name in expected_names} | {"scripts/validate.py"}
    banned_suffixes = {
        ".png", ".jpg", ".jpeg", ".jpe", ".gif", ".tif", ".tiff", ".bmp",
        ".webp", ".svg", ".heic", ".avif", ".pdf", ".eps", ".ps",
        ".ico", ".pnm", ".ppm", ".pgm", ".zip", ".pyc",
    }
    banned_parts = {"source", "upload", "hua", f"{PREFIX}_scans", f"{PREFIX}_texts", "__pycache__"}
    try:
        with zipfile.ZipFile(archive) as bundle:
            bad_crc = bundle.testzip()
            if bad_crc:
                report.error(f"ZIP CRC failure: {bad_crc}")
            members = [info for info in bundle.infolist() if not info.is_dir()]
            names = [info.filename for info in members]
            duplicate = [name for name, count in Counter(names).items() if count > 1]
            if duplicate:
                report.error(f"ZIP has duplicate members: {duplicate}")
            prefix = f"{PREFIX}/" if names and all(name.startswith(f"{PREFIX}/") for name in names) else ""
            relative = {}
            for info in members:
                name = info.filename[len(prefix):]
                member = PurePosixPath(name)
                if member.is_absolute() or ".." in member.parts or "\\" in name:
                    report.error(f"Unsafe ZIP path: {info.filename}")
                if member.suffix.lower() in banned_suffixes:
                    report.error(f"Forbidden image, input archive, nested ZIP, or cache file: {info.filename}")
                if (set(member.parts) & banned_parts
                        or member.name in {"MARKS.tsv", "PREAMBLE.tex"}
                        or (member.name.startswith("PROMPT") and member.suffix.lower() == ".md")):
                    report.error(f"ZIP includes supplied source material or cache: {info.filename}")
                if "checkpoint" in member.name.lower() and member.suffix.lower() == ".zip":
                    report.error(f"ZIP includes a checkpoint member: {info.filename}")
                relative[name] = info
            absent = sorted(required - set(relative))
            if absent:
                report.error(f"ZIP lacks required members: {absent}")
            for name, info in relative.items():
                local = root / name
                if local.is_file() and bundle.read(info) != local.read_bytes():
                    report.error(f"ZIP member differs from current deliverable: {name}")
            deliverable_files = {
                p.relative_to(root).as_posix() for p in root.rglob("*")
                if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
            }
            missing_local = sorted(deliverable_files - set(relative))
            if missing_local:
                report.error(f"ZIP omits written deliverables/documentation: {missing_local}")
            report.fact(f"ZIP inspected: {len(members)} files; {archive.stat().st_size:,} bytes")
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        report.error(f"Cannot inspect ZIP: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    default_root = Path(__file__).resolve().parents[1]
    parser.add_argument("--root", type=Path, default=default_root, help="Deliverable directory")
    parser.add_argument("--source", type=Path, default=default_root.parent / "source" / f"{PREFIX}_texts", help="Supplied texts directory; only metadata is read")
    parser.add_argument("--zip", dest="archive", type=Path, help="Final ZIP to check; omit before packaging")
    parser.add_argument("--before-freeze", action="store_true", help="Check both completed reading passes and all schemas, deferring frozen-hash requirements")
    args = parser.parse_args()
    root, source = args.root.resolve(), args.source.resolve()
    report = Report()
    for name in REQUIRED_FILES:
        path = root / name
        if not path.is_file():
            report.error(f"Missing required file: {name}")
        elif path.stat().st_size == 0:
            report.error(f"Empty required file: {name}")
    doubts_path = root / f"{PREFIX}_doubts.md"
    if doubts_path.is_file() and "Assessment remains open during the reading." in doubts_path.read_text(encoding="utf-8"):
        report.error("The doubts file still contains the unfinished legibility-assessment placeholder")
    expected_names, h_scans, marks = source_metadata(source, report)
    validate_pages(root, expected_names, report)
    validate_decisions(root, marks, report)
    validate_collation(root, h_scans, report)
    validate_inventory(root, report)
    validate_events(root, report)
    validate_progress(root, expected_names, report, require_frozen=not args.before_freeze)
    if args.archive is not None:
        validate_archive(root, args.archive.resolve(), expected_names, report)
    else:
        report.warn("ZIP check omitted; pass --zip after packaging")
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
