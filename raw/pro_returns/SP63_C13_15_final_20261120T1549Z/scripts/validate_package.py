#!/usr/bin/env python3
"""Mechanical validation of the SP63_C13_15 deliverable.

This program does not evaluate readings, mathematics, or visual fidelity.  It
checks filenames, table schemas, identifiers, bookkeeping, byte concatenation,
and recorded SHA-256 digests.  It never opens scan images or witness page files.

Usage:
    python validate_package.py WORK_DIR ORIGINAL_TEXTS_DIR [--partial]

Supported progress.log digest formats (paths relative to WORK_DIR):
    <64 hex digits>  pages/15_scan139.tex
    SHA256 <64 hex digits> pages/15_scan139.tex
    SHA256 pages/15_scan139.tex <64 hex digits>
    SHA256 (pages/15_scan139.tex) = <64 hex digits>

The combined fragment must equal the page files concatenated in filename order.
For convenience a single newline separator between each file is also accepted;
the exact detected convention is reported.  No other added text is accepted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path


PREFIX = "SP63_C13_15"
SCANS = (139, 141, 142, 143, 144, 147, 148, 149, 150, 151, 152,
         157, 159, 160, 161, 162, 163, 164, 165, 172, 173, 174,
         176, 177, 179)
EXPECTED_PAGES = tuple(f"15_scan{scan:03d}.tex" for scan in SCANS)
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
TABLE_HEADERS = {
    "decisions.tsv": (
        "id", "cote", "scan", "decision", "reading", "what the ink shows",
        "crop", "confidence",
    ),
    f"{PREFIX}_collation.tsv": (
        "folder", "their_page", "our_scan", "line", "their_reading",
        "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
        "confidence",
    ),
    f"{PREFIX}_inventory.csv": (
        "scan", "sheet_kind", "hand", "element", "kind", "position",
        "first_words_or_objects", "transcribed",
    ),
}
INVENTORY_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion",
    "deletion",
}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list", "cancelled_draft",
    "cover",
}
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission",
    "text not on the page", "deletion state (struck given live or live given struck)",
    "deletion state", "insertion or placement",
    "abbreviation expanded or spelling modernised", "readable ink left as \\ill{}",
    "readable ink left as `\\ill{}`",
    "drawing or diagram", "other",
}
EVENT_TYPES = {
    "targeted proof check", "independent re-proof",
    "computation or formal certificate", "used and rechecked in this run",
    "carried as background without fault found",
}
FORBIDDEN_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tif", ".tiff",
    ".heic", ".heif", ".avif", ".svg", ".pdf", ".zip", ".tar", ".tgz",
    ".gz", ".bz2", ".xz", ".7z", ".rar",
}
HEX64 = r"[0-9a-fA-F]{64}"


class Validator:
    def __init__(self, work: Path, original: Path, partial: bool):
        self.work = work.resolve()
        self.original = original.resolve()
        self.partial = partial
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []
        self.tables: dict[str, list[dict[str, str]]] = {}

    def error(self, message: str) -> None:
        self.errors.append(message)

    def incomplete(self, message: str) -> None:
        (self.warnings if self.partial else self.errors).append(message)

    def read_table(self, path: Path, delimiter: str,
                   expected: tuple[str, ...] | None = None):
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle, delimiter=delimiter)
                headers = tuple(reader.fieldnames or ())
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            self.error(f"Cannot parse table {path.name}: {exc}")
            return (), []
        if expected is not None and headers != expected:
            self.error(
                f"{path.name}: wrong header or column order. Expected "
                f"{list(expected)!r}; found {list(headers)!r}."
            )
        if len(set(headers)) != len(headers):
            self.error(f"{path.name}: duplicate header names.")
        for lineno, row in enumerate(rows, start=2):
            if None in row:
                self.error(f"{path.name}:{lineno}: extra delimiter-separated fields.")
            if any(value is None for value in row.values()):
                self.error(f"{path.name}:{lineno}: missing delimiter-separated fields.")
        self.info.append(f"{path.name}: {len(rows)} data rows.")
        return headers, rows

    def check_tree(self) -> list[str]:
        if not self.work.is_dir():
            self.error(f"Work directory does not exist: {self.work}")
            return []
        for name in REQUIRED_FILES:
            path = self.work / name
            if not path.is_file():
                self.incomplete(f"Missing deliverable: {name}")
            elif not path.stat().st_size:
                self.incomplete(f"Empty deliverable: {name}")
        for path in sorted(self.work.rglob("*")):
            if path.is_symlink():
                self.error(f"Symlink must not be packaged: {path.relative_to(self.work)}")
            if path.is_file() and (
                path.suffix.lower() in FORBIDDEN_SUFFIXES
                or "_checkpoint_" in path.name.lower()
            ):
                self.error(f"Excluded file is inside work tree: {path.relative_to(self.work)}")
        page_dir = self.work / "pages"
        actual = sorted(path.name for path in page_dir.glob("*.tex"))
        extras = sorted(set(actual) - set(EXPECTED_PAGES))
        missing = sorted(set(EXPECTED_PAGES) - set(actual))
        if extras:
            self.error(f"Unexpected page filenames: {', '.join(extras)}")
        if missing:
            self.incomplete(f"Missing page filenames: {', '.join(missing)}")
        original_dir = self.original / "pages"
        if not original_dir.is_dir():
            self.error(f"Original page directory is absent: {original_dir}")
        else:
            source_names = sorted(path.name for path in original_dir.glob("*.tex"))
            if source_names != sorted(EXPECTED_PAGES):
                self.error("Original page filename inventory differs from the expected 25 names.")
        self.info.append(f"Page files: {len(actual)}/{len(EXPECTED_PAGES)} expected.")
        return actual

    def check_concatenation(self, actual: list[str]) -> None:
        combined = self.work / f"{PREFIX}_transcription.tex"
        if not combined.is_file() or not actual:
            return
        try:
            pieces = [(self.work / "pages" / name).read_bytes() for name in actual]
            data = combined.read_bytes()
        except OSError as exc:
            self.error(f"Cannot check concatenation: {exc}")
            return
        if data == b"".join(pieces):
            self.info.append("Combined transcription: exact byte concatenation in filename order.")
        elif data == b"\n".join(pieces):
            self.info.append("Combined transcription: exact page bytes with one newline separator.")
        else:
            self.error(
                "Combined transcription differs from page files in filename order. "
                "Rebuild it by byte concatenation (or with one newline between files)."
            )

    def check_tables(self) -> None:
        for filename, expected in TABLE_HEADERS.items():
            path = self.work / filename
            if path.is_file():
                _, rows = self.read_table(path, "\t" if path.suffix == ".tsv" else ",", expected)
                self.tables[filename] = rows

        decisions = self.tables.get("decisions.tsv")
        marks_path = self.original / "MARKS.tsv"
        if not marks_path.is_file():
            self.error(f"Original MARKS.tsv is absent: {marks_path}")
        elif decisions is not None:
            # Only the source id column is used; mark/readings are never interpreted.
            headers, marks = self.read_table(marks_path, "\t")
            if "id" not in headers:
                self.error("Original MARKS.tsv has no id column.")
            else:
                expected_ids = [row.get("id", "") for row in marks]
                actual_ids = [row.get("id", "") for row in decisions]
                if self.partial:
                    if actual_ids != expected_ids[:len(actual_ids)]:
                        self.error("decisions.tsv IDs are not an initial prefix of MARKS.tsv IDs in their original order.")
                    if len(actual_ids) < len(expected_ids):
                        self.warnings.append(f"Decisions pending: {len(expected_ids) - len(actual_ids)}.")
                elif actual_ids != expected_ids:
                    self.error("decisions.tsv IDs or row order do not exactly match MARKS.tsv.")
                duplicates = [key for key, count in Counter(actual_ids).items() if count > 1]
                if duplicates:
                    self.error(f"Duplicate decision IDs: {', '.join(duplicates)}")
            for lineno, row in enumerate(decisions, start=2):
                if row.get("decision") not in {"first", "alternative", "other", "undecided"}:
                    self.error(f"decisions.tsv:{lineno}: invalid decision value.")
                if row.get("confidence") not in {"high", "medium", "low"}:
                    self.error(f"decisions.tsv:{lineno}: invalid confidence value.")
                if row.get("cote") != "15":
                    self.error(f"decisions.tsv:{lineno}: cote must be 15.")

        inventory = self.tables.get(f"{PREFIX}_inventory.csv", [])
        inventory_scans: set[int] = set()
        for lineno, row in enumerate(inventory, start=2):
            filename = f"{PREFIX}_inventory.csv"
            if row.get("transcribed") != "yes":
                self.error(f"{filename}:{lineno}: transcribed must be yes.")
            if row.get("kind") not in INVENTORY_KINDS:
                self.error(f"{filename}:{lineno}: invalid element kind.")
            if row.get("sheet_kind") not in SHEET_KINDS:
                self.error(f"{filename}:{lineno}: invalid sheet_kind.")
            try:
                scan = int(row.get("scan", ""))
            except (TypeError, ValueError):
                self.error(f"{filename}:{lineno}: scan is not an integer.")
                continue
            inventory_scans.add(scan)
            if scan not in SCANS:
                self.error(f"{filename}:{lineno}: unexpected scan {scan}.")
        if f"{PREFIX}_inventory.csv" in self.tables:
            missing_inventory = sorted(set(SCANS) - inventory_scans)
            if missing_inventory:
                self.incomplete(f"Inventory has no elements for scans: {missing_inventory}")

        for lineno, row in enumerate(self.tables.get(f"{PREFIX}_collation.tsv", []), start=2):
            filename = f"{PREFIX}_collation.tsv"
            if row.get("confidence") not in {"high", "medium", "low"}:
                self.error(f"{filename}:{lineno}: invalid confidence value.")
            if row.get("kind") not in COLLATION_KINDS:
                self.error(f"{filename}:{lineno}: invalid kind value.")
            if row.get("folder") != "15":
                self.error(f"{filename}:{lineno}: folder must be 15.")
            try:
                scan = int(row.get("our_scan", ""))
                their_page = int(row.get("their_page", ""))
            except (TypeError, ValueError):
                self.error(f"{filename}:{lineno}: page numbers must be integers.")
                continue
            if scan not in SCANS:
                self.error(f"{filename}:{lineno}: unexpected scan {scan}.")
            if their_page != scan - 1:
                self.error(f"{filename}:{lineno}: their_page must equal our_scan minus one.")
            if not (self.original / "hua" / f"hua_15_scan{scan:03d}.tex").is_file():
                self.error(f"{filename}:{lineno}: H has no supplied file for scan {scan}.")

        events_path = self.work / "CHECK_EVENTS.tsv"
        if events_path.is_file():
            headers, rows = self.read_table(events_path, "\t")
            # The prompt specifies semantic fields but not literal column spellings.
            normalized = {name.lower().strip().replace(" ", "_"): name for name in headers}
            for needed in ("statement_id", "date", "type", "outcome"):
                if needed not in normalized:
                    self.error(f"CHECK_EVENTS.tsv: missing {needed} column.")
            if "who" not in normalized and not {"model", "effort", "run"}.issubset(normalized):
                self.error("CHECK_EVENTS.tsv: supply who or separate model, effort, run columns.")
            type_header = normalized.get("type")
            if type_header:
                for lineno, row in enumerate(rows, start=2):
                    event_type = row.get(type_header, "") or ""
                    if event_type not in EVENT_TYPES and not event_type.startswith("refuted"):
                        self.error(f"CHECK_EVENTS.tsv:{lineno}: unrecognized event type.")

    @staticmethod
    def digest_line(line: str):
        patterns = (
            rf"^\s*(?:SHA-?256\s+)?({HEX64})\s+\*?(.+?)\s*$",
            rf"^\s*SHA-?256\s+(.+?)\s+({HEX64})\s*$",
            rf"^\s*SHA-?256\s*\((.+?)\)\s*=\s*({HEX64})\s*$",
        )
        for index, pattern in enumerate(patterns):
            match = re.match(pattern, line, re.I)
            if match:
                digest, filename = match.groups() if index == 0 else reversed(match.groups())
                return str(filename).replace("\\", "/"), str(digest).lower()
        return None

    def check_progress(self) -> None:
        progress = self.work / "progress.log"
        if not progress.is_file():
            return
        try:
            lines = progress.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError) as exc:
            self.error(f"Cannot read progress.log: {exc}")
            return
        timestamp = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
        if not lines or not re.fullmatch(timestamp, lines[0]):
            self.error("progress.log first line must be a UTC timestamp, YYYY-MM-DD HH:MM:SS UTC.")
        done: list[int] = []
        audited: list[int] = []
        hashes: dict[str, str] = {}
        freeze_count = 0
        for lineno, line in enumerate(lines, start=1):
            match = re.fullmatch(rf"scan (\d+) done ({timestamp}) cote (\S+)", line)
            if match:
                scan = int(match.group(1))
                done.append(scan)
                if match.group(3) != "15":
                    self.error(f"progress.log:{lineno}: done line has cote other than 15.")
            elif re.match(r"scan \d+ done", line):
                self.error(f"progress.log:{lineno}: malformed done line.")
            match = re.fullmatch(rf"scan (\d+) audited ({timestamp})", line)
            if match:
                audited.append(int(match.group(1)))
            elif re.match(r"scan \d+ audited", line):
                self.error(f"progress.log:{lineno}: malformed audited line.")
            if re.fullmatch(rf"transcription frozen ({timestamp})", line):
                freeze_count += 1
            elif line.startswith("transcription frozen"):
                self.error(f"progress.log:{lineno}: malformed freeze line.")
            parsed = self.digest_line(line)
            if parsed:
                filename, digest = parsed
                filename = filename.removeprefix("./")
                if filename in hashes and hashes[filename] != digest:
                    self.error(f"progress.log:{lineno}: conflicting frozen hashes for {filename}.")
                hashes[filename] = digest
        for label, observed in (("done", done), ("audited", audited)):
            if self.partial:
                if observed != list(SCANS[:len(observed)]):
                    self.error(f"progress.log {label} scan order is not the expected initial sequence.")
            elif observed != list(SCANS):
                self.error(f"progress.log must contain each expected scan exactly once, in order, as {label}.")
            self.info.append(f"Progress {label}: {len(observed)}/{len(SCANS)}.")
        first_audit = next((i for i, line in enumerate(lines) if re.match(r"scan \d+ audited", line)), None)
        last_done = max((i for i, line in enumerate(lines) if re.match(r"scan \d+ done", line)), default=-1)
        if first_audit is not None and (first_audit < last_done or len(done) != len(SCANS)):
            self.error("Audit entries must begin after all 25 done entries.")
        if not freeze_count:
            self.incomplete("No transcription frozen UTC line in progress.log.")
        if freeze_count > 1:
            self.warnings.append("More than one freeze line is present; all retained hashes must still agree.")
        required_hashes = {f"pages/{name}" for name in EXPECTED_PAGES}
        required_hashes.add(f"{PREFIX}_transcription.tex")
        if freeze_count:
            missing = sorted(required_hashes - hashes.keys())
            if missing:
                self.error(f"Frozen hashes missing for: {', '.join(missing)}")
        for filename, recorded in hashes.items():
            path = self.work / filename
            try:
                path.resolve().relative_to(self.work)
            except ValueError:
                self.error(f"Frozen hash path escapes work directory: {filename}")
                continue
            if not path.is_file():
                self.error(f"Frozen hash refers to missing file: {filename}")
                continue
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != recorded:
                self.error(f"Frozen SHA-256 mismatch: {filename}")
        self.info.append(f"Recorded SHA-256 entries checked: {len(hashes)}.")
        if freeze_count and not any(re.search(r"hash(?:es)?\b.*\bunchanged\b|\bunchanged\b.*\bhash(?:es)?\b", line, re.I) for line in lines):
            self.incomplete("progress.log has no final statement that hashes are unchanged.")

    def run(self) -> int:
        actual = self.check_tree()
        self.check_concatenation(actual)
        self.check_tables()
        self.check_progress()
        for message in self.info:
            print(f"INFO: {message}")
        for message in self.warnings:
            print(f"PENDING: {message}")
        for message in self.errors:
            print(f"ERROR: {message}")
        mode = "partial" if self.partial else "complete"
        print(f"RESULT ({mode}): {len(self.errors)} error(s), {len(self.warnings)} pending/warning item(s).")
        return 1 if self.errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("work_dir", type=Path)
    parser.add_argument("original_texts_dir", type=Path)
    parser.add_argument("--partial", action="store_true", help="allow expected files/rows/stages to remain incomplete")
    args = parser.parse_args()
    return Validator(args.work_dir, args.original_texts_dir, args.partial).run()


if __name__ == "__main__":
    sys.exit(main())
