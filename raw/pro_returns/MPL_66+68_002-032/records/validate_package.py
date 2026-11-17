#!/usr/bin/env python3
"""Read-only, mechanical checks for MPL_66+68_002-032 deliverables.

This program does not OCR, inspect images, open the context archive, assess
readings, interpret mathematical content, or certify transcription accuracy.
It reads deliverable text solely to check structure, bookkeeping, and hashes.
It never changes a transcription or any other input file.

Usage:
    python work/records/validate_package.py work --mode partial
    python work/records/validate_package.py work --mode final --hashes

The combined transcription must be the exact byte concatenation of the page
files in scan order. Include \\cotefile{68} in the first page file, before its
\\scanpage{2} (zero-padded scan macro arguments are also accepted).

Recognized SHA-256 log formats (relative paths or basenames):
    sha256 HEX_DIGEST pages/FILENAME.tex
    HEX_DIGEST  pages/FILENAME.tex
    SHA-256 pages/FILENAME.tex HEX_DIGEST

Final verification should be logged after context opening, for example:
    frozen hashes verified unchanged YYYY-MM-DD HH:MM:SS UTC
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

PREFIX = "MPL_66+68_002-032"
SCANS = tuple(range(2, 23)) + tuple(range(24, 33))
FIELDS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
TIME_RE = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
HEX_RE = r"[0-9a-fA-F]{64}"
PAGE_RE = re.compile(re.escape(PREFIX) + r"_(\d+)_scan(\d{3})\.tex$")


class Checker:
    def __init__(self, root: Path, mode: str):
        self.root = root.resolve()
        self.final = mode == "final"
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.counts: dict[str, int] = {}
        self.page_paths: dict[int, Path] = {}
        self.hashes: dict[str, str] = {}

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.error(message)

    def read(self, path: Path) -> str | None:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error(f"Cannot read {path.relative_to(self.root)}: {exc}")
            return None

    def timestamp(self, value: str, location: str) -> datetime | None:
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
        except ValueError:
            self.error(f"Invalid UTC timestamp at {location}")
            return None

    @staticmethod
    def strip_comments(text: str) -> str:
        """Mask TeX comments while preserving character and line positions."""
        chars = list(text)
        for match in re.finditer(r"%", text):
            pos = match.start()
            nback = 0
            cursor = pos - 1
            while cursor >= 0 and text[cursor] == "\\":
                nback += 1
                cursor -= 1
            if nback % 2:
                continue
            end = text.find("\n", pos)
            end = len(text) if end < 0 else end
            chars[pos:end] = " " * (end - pos)
        return "".join(chars)

    def tex_structure(self, path: Path, text: str) -> None:
        name = path.relative_to(self.root).as_posix()
        text = self.strip_comments(text)
        stack: list[int] = []
        envstack: list[tuple[str, int]] = []
        tokens = re.compile(r"\\(?:begin|end)\s*\{([^{}]+)\}|\\.|[{}]", re.DOTALL)
        for match in tokens.finditer(text):
            token = match.group(0)
            line = text.count("\n", 0, match.start()) + 1
            if token == "{":
                stack.append(line)
            elif token == "}":
                if stack:
                    stack.pop()
                else:
                    self.error(f"{name}:{line}: unmatched closing brace")
            elif match.group(1) is not None:
                env = match.group(1).strip()
                if token.startswith("\\begin"):
                    envstack.append((env, line))
                elif not envstack:
                    self.error(f"{name}:{line}: unmatched end of environment {env}")
                elif envstack[-1][0] != env:
                    self.error(f"{name}:{line}: end {env} mismatches open {envstack[-1][0]}")
                else:
                    envstack.pop()
        for line in stack:
            self.error(f"{name}:{line}: unclosed opening brace")
        for env, line in envstack:
            self.error(f"{name}:{line}: unclosed environment {env}")
        if re.search(r"\\(?:documentclass|usepackage)\b", text):
            self.error(f"{name}: preamble command in required LaTeX fragment")
        if re.search(r"\\(?:includegraphics|include|input)\b", text):
            self.error(f"{name}: external inclusion command in self-contained transcription fragment")

    def check_pages(self) -> None:
        pages = self.root / "pages"
        self.require(pages.is_dir(), "Missing pages/ directory")
        if not pages.is_dir():
            return
        for path in sorted(pages.glob("*.tex")):
            match = PAGE_RE.fullmatch(path.name)
            if not match:
                self.error(f"Unexpected page filename: {path.name}")
                continue
            cote, scan = map(int, match.groups())
            if cote != 68 or scan not in SCANS:
                self.error(f"Unexpected cote/scan in page filename: {path.name}")
                continue
            self.page_paths[scan] = path
        found = sorted(self.page_paths)
        self.counts["pages"] = len(found)
        if self.final:
            missing = sorted(set(SCANS) - set(found))
            self.require(not missing, "Missing page files: " + ", ".join(f"{n:03}" for n in missing))
        else:
            self.require(found == list(SCANS[:len(found)]), "Partial page files are not an unbroken prefix of supplied scan order")
        cotefiles: list[tuple[int, int, int]] = []
        for scan, path in sorted(self.page_paths.items()):
            text = self.read(path)
            if text is None:
                continue
            clean = self.strip_comments(text)
            scans = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
            self.require([int(n) for n in scans] == [scan], f"{path.name}: scanpage macro does not identify exactly scan {scan}")
            for match in re.finditer(r"\\cotefile\s*\{\s*(\d+)\s*\}", clean):
                cotefiles.append((scan, int(match.group(1)), match.start()))
            self.tex_structure(path, text)
        if found:
            self.require(len(cotefiles) == 1 and cotefiles[0][:2] == (2, 68), "Exactly one cotefile{68} must occur, in the first page file")
            first_text = self.read(self.page_paths[found[0]])
            if first_text is not None:
                clean = self.strip_comments(first_text).lstrip()
                self.require(re.match(r"\\cotefile\s*\{\s*68\s*\}\s*\\scanpage\s*\{\s*0*2\s*\}", clean) is not None,
                             "First page must start with cotefile{68}, then scanpage{2}")

        combined = self.root / f"{PREFIX}_transcription.tex"
        if not combined.is_file():
            if self.final:
                self.error("Missing combined transcription")
            return
        try:
            expected = b"".join(self.page_paths[n].read_bytes() for n in found)
            actual = combined.read_bytes()
            self.require(actual == expected, "Combined transcription differs from exact ordered byte concatenation of page files")
        except OSError as exc:
            self.error(f"Cannot compare combined transcription: {exc}")
        text = self.read(combined)
        if text is not None:
            self.tex_structure(combined, text)

    def check_inventory(self) -> None:
        path = self.root / f"{PREFIX}_inventory.csv"
        if not path.is_file():
            self.error("Missing inventory CSV")
            return
        seen: set[tuple[int, int, str]] = set()
        rows_by_scan: Counter[int] = Counter()
        try:
            with path.open(newline="", encoding="utf-8-sig") as handle:
                reader = csv.DictReader(handle)
                self.require(reader.fieldnames == FIELDS, "Inventory CSV column names/order differ from required schema")
                if reader.fieldnames != FIELDS:
                    return
                for line, row in enumerate(reader, 2):
                    where = f"Inventory row {line}"
                    if None in row or any(row.get(field) is None for field in FIELDS):
                        self.error(f"{where}: malformed CSV row")
                        continue
                    try:
                        cote, scan = int(row["cote"]), int(row["scan"])
                    except (ValueError, KeyError):
                        self.error(f"{where}: cote/scan must be integers")
                        continue
                    self.require(cote == 68 and scan in SCANS, f"{where}: unexpected cote/scan")
                    self.require(scan in self.page_paths, f"{where}: no corresponding completed page file")
                    self.require(row["transcribed"] == "yes", f"{where}: transcribed is not exactly yes")
                    self.require(row["sheet_kind"] in SHEET_KINDS, f"{where}: invalid sheet_kind")
                    self.require(row["kind"] in KINDS, f"{where}: invalid kind")
                    for field in ("element", "position", "first_words_or_objects"):
                        self.require(bool(row[field].strip()), f"{where}: empty {field}")
                    key = (cote, scan, row["element"])
                    self.require(key not in seen, f"{where}: duplicate element identifier within page")
                    seen.add(key)
                    rows_by_scan[scan] += 1
        except (OSError, UnicodeError, csv.Error) as exc:
            self.error(f"Cannot read inventory: {exc}")
        for scan in self.page_paths:
            self.require(rows_by_scan[scan] > 0, f"Scan {scan:03} has no inventory rows")
        self.counts["inventory_rows"] = sum(rows_by_scan.values())

    def hash_record(self, line: str) -> tuple[str, str] | None:
        match = re.match(rf"\s*(?:(?:sha-?256)\s+)?({HEX_RE})\s+[* ]?(.+?)\s*$", line, re.I)
        if match:
            return match.group(2), match.group(1).lower()
        match = re.match(rf"\s*sha-?256\s+(.+?)\s+({HEX_RE})\s*$", line, re.I)
        if match:
            return match.group(1), match.group(2).lower()
        return None

    def check_log(self) -> None:
        path = self.root / "progress.log"
        if not path.is_file():
            self.error("Missing progress.log")
            return
        text = self.read(path)
        if text is None:
            return
        lines = text.splitlines()
        self.require(bool(lines) and re.fullmatch(TIME_RE, lines[0]) is not None,
                     "First progress.log line must be only the starting UTC time")
        timestamps: list[tuple[int, datetime]] = []
        done: list[tuple[int, int]] = []
        audited: list[tuple[int, int]] = []
        freezes: list[int] = []
        contexts: list[int] = []
        verifications: list[int] = []
        recorded_hashes: dict[str, list[tuple[int, str]]] = {}
        done_pattern = re.compile(rf"68 scan (\d{{3}}) done ({TIME_RE})$")
        audit_pattern = re.compile(rf"(?:68 )?scan (\d{{3}}) audited ({TIME_RE})$")
        for index, line in enumerate(lines):
            time_match = re.search(rf"({TIME_RE})$", line)
            if time_match:
                stamp = self.timestamp(time_match.group(1), f"progress.log:{index + 1}")
                if stamp is not None:
                    timestamps.append((index, stamp))
            match = done_pattern.fullmatch(line)
            if match:
                done.append((int(match.group(1)), index))
            match = audit_pattern.fullmatch(line)
            if match:
                audited.append((int(match.group(1)), index))
            if re.fullmatch(rf"transcription frozen {TIME_RE}", line):
                freezes.append(index)
            if re.fullmatch(rf"context opened {TIME_RE}", line):
                contexts.append(index)
            if re.search(r"(?:frozen\s+)?hashes\s+(?:verified\s+)?unchanged", line, re.I):
                verifications.append(index)
            record = self.hash_record(line)
            if record:
                filename, digest = record
                filename = filename.strip("`\"'")
                file_path = Path(filename)
                if file_path.is_absolute():
                    try:
                        filename = file_path.relative_to(self.root).as_posix()
                    except ValueError:
                        self.error(f"Hash record at log line {index + 1} refers outside work directory")
                        continue
                if "/" not in filename and filename.startswith(f"{PREFIX}_68_scan"):
                    filename = "pages/" + filename
                if ".." in Path(filename).parts:
                    self.error(f"Unsafe relative hash path at log line {index + 1}")
                    continue
                recorded_hashes.setdefault(filename, []).append((index, digest))
        for (i1, t1), (i2, t2) in zip(timestamps, timestamps[1:]):
            self.require(t1 <= t2, f"UTC time decreases between log lines {i1 + 1} and {i2 + 1}")
        self.require([n for n, _ in done] == sorted(self.page_paths), "Done log entries do not match completed page files in scan order")
        self.require(len({n for n, _ in audited}) == len(audited), "Duplicate audited log entry")
        self.require([n for n, _ in audited] == [n for n in SCANS if n in {s for s, _ in audited}], "Audited log entries are out of scan order")
        for scan, index in audited:
            matching = [i for n, i in done if n == scan]
            self.require(bool(matching) and matching[0] < index, f"Scan {scan:03} audit precedes its completion")
        if audited:
            self.require(len(done) == len(SCANS) and done[-1][1] < audited[0][1], "Second-reading audits began before all pages were done")
        self.counts["done_entries"] = len(done)
        self.counts["audit_entries"] = len(audited)
        self.counts["hash_records"] = sum(len(v) for v in recorded_hashes.values())
        if self.final:
            self.require([n for n, _ in audited] == list(SCANS), "Final log must audit every supplied page in order")
            self.require(len(freezes) == 1, "Final log must contain one transcription frozen event")
            self.require(len(contexts) == 1, "Final log must contain one context opened event")
        if freezes:
            self.require(len(audited) == len(SCANS), "Transcription frozen before all scans had audit entries")
            self.require(not audited or audited[-1][1] < freezes[0], "Freeze event precedes final audit")
        if contexts:
            self.require(bool(freezes) and freezes[-1] < contexts[0], "Context opened without an earlier freeze event")
        expected_hash_paths = [p.relative_to(self.root).as_posix() for _, p in sorted(self.page_paths.items())]
        expected_hash_paths.append(f"{PREFIX}_transcription.tex")
        if freezes or self.final:
            for name in expected_hash_paths:
                self.require(name in recorded_hashes, f"Missing frozen SHA-256 record: {name}")
                if contexts and name in recorded_hashes:
                    self.require(recorded_hashes[name][0][0] < contexts[0], f"First SHA-256 record for {name} follows context opening")
        for name, values in recorded_hashes.items():
            target = self.root / name
            if not target.is_file():
                self.error(f"SHA-256 log record has no file: {name}")
                continue
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            for index, expected in values:
                self.require(digest == expected, f"SHA-256 mismatch at log line {index + 1}: {name}")
        if self.final:
            after = contexts[-1] if contexts else (freezes[-1] if freezes else -1)
            self.require(any(i > after for i in verifications), "Final log lacks a post-context statement that frozen hashes are unchanged")

    def check_deliverables(self) -> None:
        for suffix in ("doubts.md", "notes.md"):
            path = self.root / f"{PREFIX}_{suffix}"
            if not path.is_file():
                if self.final or suffix == "doubts.md":
                    self.error(f"Missing {path.name}")
            elif self.final:
                self.require(path.stat().st_size > 0, f"Empty {path.name}")

    def compute_hashes(self) -> None:
        # Only the deliverables directory; never scans/, upload/, or context/.
        for path in sorted(self.root.rglob("*")):
            relative = path.relative_to(self.root)
            if any(part in {"context", "scans", "upload", "sources", "__pycache__"} for part in relative.parts):
                continue
            if path.is_symlink():
                self.warn(f"Skipped symlink: {path.relative_to(self.root)}")
                continue
            if not path.is_file():
                continue
            if path.suffix.lower() in {".zip", ".jpg", ".jpeg", ".png", ".pdf"}:
                # Inputs / accidental nested archives must not be read by this checker.
                self.warn(f"Skipped non-deliverable binary: {path.relative_to(self.root)}")
                continue
            rel = path.relative_to(self.root).as_posix()
            self.hashes[rel] = hashlib.sha256(path.read_bytes()).hexdigest()

    def run(self) -> dict[str, object]:
        if not self.root.is_dir():
            self.error("Work directory does not exist")
        else:
            self.check_pages()
            self.check_inventory()
            self.check_log()
            self.check_deliverables()
            self.compute_hashes()
        manifest = "".join(f"{digest}  {name}\n" for name, digest in sorted(self.hashes.items()))
        return {
            "scope": "Mechanical structure and bookkeeping only; no handwriting/content accuracy assessment.",
            "mode": "final" if self.final else "partial",
            "ok": not self.errors,
            "counts": self.counts,
            "errors": self.errors,
            "warnings": self.warnings,
            "manifest_sha256": hashlib.sha256(manifest.encode()).hexdigest(),
            "file_hashes": self.hashes,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("work_dir", type=Path)
    parser.add_argument("--mode", choices=("partial", "final"), default="partial")
    parser.add_argument("--json", action="store_true", help="Print a machine-readable report, including all file hashes")
    parser.add_argument("--hashes", action="store_true", help="Print file SHA-256 values after the concise report")
    args = parser.parse_args()
    result = Checker(args.work_dir, args.mode).run()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"{args.mode.upper()} mechanical validation: {'PASS' if result['ok'] else 'FAIL'}")
        print(result["scope"])
        print(", ".join(f"{key}={value}" for key, value in result["counts"].items()))
        for label, key in (("ERROR", "errors"), ("WARNING", "warnings")):
            for message in result[key]:
                print(f"{label}: {message}")
        print(f"Checked-file manifest SHA-256: {result['manifest_sha256']}")
        if args.hashes:
            for name, digest in result["file_hashes"].items():
                print(f"{digest}  {name}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
