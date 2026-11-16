#!/usr/bin/env python3
"""Mechanical checks and source-free ZIP packaging for MPL_43_094-142.

This utility does not evaluate readings, identify handwriting, perform OCR, or
certify visual completeness.  It is intended to be run by the sole transcriber
after files have been written.  Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "MPL_43_094-142"
SCANS = [n for n in range(94, 143) if n not in {99, 111, 127}]
FIELDS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
STATE_MACROS = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
    "uline", "uuline", "diagram", "figure", "unsure", "illegible",
}
EXCLUDED_DIRS = {"scans", "upload", "context", "__pycache__", ".git", ".pytest_cache"}
EXCLUDED_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".webp", ".bmp",
    ".pdf", ".zip", ".pyc", ".pyo", ".tmp", ".part",
}


def page_name(scan: int) -> str:
    return f"{PREFIX}_43_scan{scan:03d}.tex"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utc_timestamp(value: str) -> datetime | None:
    """Accept explicit UTC timestamps in the log, including ISO 8601."""
    try:
        if value.endswith(" UTC"):
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is not None and parsed.utcoffset().total_seconds() == 0:
            return parsed
    except (ValueError, AttributeError):
        pass
    return None


def latex_surface(text: str) -> tuple[str, list[tuple[int, str]]]:
    """Mask comments/verbatim and check braces without treating escaped braces as groups."""
    clean = list(text)
    stack: list[int] = []
    problems: list[tuple[int, str]] = []
    i = 0
    line = 1
    while i < len(text):
        char = text[i]
        if char == "\n":
            line += 1
            i += 1
        elif char == "%":
            end = text.find("\n", i)
            end = len(text) if end == -1 else end
            clean[i:end] = " " * (end - i)
            i = end
        elif char == "\\":
            match = re.match(r"\\([A-Za-z@]+|.)", text[i:], re.DOTALL)
            if not match:
                problems.append((line, "A final backslash has no following command character."))
                i += 1
                continue
            command = match.group(1)
            start = i
            i += len(match.group(0))
            if command == "verb":
                if i < len(text) and text[i] == "*":
                    i += 1
                if i >= len(text) or text[i].isspace():
                    problems.append((line, "Malformed inline verbatim command."))
                    continue
                delimiter = text[i]
                end = text.find(delimiter, i + 1)
                if end == -1 or "\n" in text[i:end]:
                    problems.append((line, "Unclosed inline verbatim command."))
                    continue
                clean[start:end + 1] = " " * (end + 1 - start)
                i = end + 1
        elif char == "{":
            stack.append(line)
            i += 1
        elif char == "}":
            if stack:
                stack.pop()
            else:
                problems.append((line, "Closing brace has no matching opening brace."))
            i += 1
        else:
            i += 1
    problems.extend((where, "Opening brace has no matching closing brace.") for where in stack)
    return "".join(clean), problems


class Validator:
    def __init__(self, root: Path, stage: str):
        self.root = root.resolve()
        self.final = stage == "final"
        self.report = {
            "stage": stage,
            "root": str(self.root),
            "expected_page_count": len(SCANS),
            "errors": [],
            "warnings": [],
            "limitations": [
                "Mechanical validation does not certify readings or visual coverage.",
                "Counts do not prove that every mark on a scan has been transcribed.",
            ],
        }
        self.pages: dict[int, bytes] = {}
        self.combined: bytes | None = None
        self.rows: list[dict[str, str]] = []
        self.log: list[str] = []

    def issue(self, code: str, message: str, *, warning: bool = False, **details) -> None:
        target = "warnings" if warning else "errors"
        self.report[target].append({"code": code, "message": message, **details})

    def read(self, relative: str, *, required: bool = True) -> bytes | None:
        path = self.root / relative
        if path.is_symlink():
            self.issue("symlink", "Symbolic links are not read or packaged.", path=relative)
            return None
        if not path.is_file():
            if required:
                self.issue("missing_file", "Required file is missing.", warning=not self.final, path=relative)
            return None
        try:
            return path.read_bytes()
        except OSError as exc:
            self.issue("read_error", str(exc), path=relative)
            return None

    def decode(self, data: bytes, relative: str) -> str | None:
        try:
            return data.decode("utf-8")
        except UnicodeDecodeError as exc:
            self.issue("encoding", f"File is not valid UTF-8: {exc}", path=relative)
            return None

    def check_latex(self, data: bytes, relative: str, scan: int) -> None:
        text = self.decode(data, relative)
        if text is None:
            return
        if not text.strip():
            self.issue("empty_page", "A page file is empty.", path=relative)
            return
        surface, braces = latex_surface(text)
        for line, message in braces:
            self.issue("latex_braces", message, path=relative, line=line)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", surface)
        if len(markers) != 1 or int(markers[0]) != scan:
            self.issue("page_marker", "Page must have exactly one matching scanpage macro.", path=relative)
        cotes = re.findall(r"\\cotefile\s*\{\s*([^{}]+)\s*\}", surface)
        if any(cote.strip() != "43" for cote in cotes):
            self.issue("cote_marker", "A cotefile macro has an unexpected argument.", path=relative)
        if scan == SCANS[0]:
            if not re.match(r"\s*\\cotefile\s*\{43\}\s*\\scanpage\s*\{0*94\}", surface):
                self.issue("opening_markers", "First page must begin with cotefile{43}, then scanpage{94}.", path=relative)
        elif cotes:
            self.issue("repeated_cote", "cotefile is repeated after the first page of cote 43.", path=relative)
        commands = Counter(re.findall(r"\\([A-Za-z@]+)\b", surface))
        for command in ("documentclass", "usepackage", "includegraphics", "input", "include"):
            if commands[command]:
                self.issue("fragment_command", "Standalone fragments must contain their text, without preamble, external input, or images.", path=relative, command=command)
        env_stack: list[str] = []
        for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", surface):
            action, env = match.groups()
            line = surface.count("\n", 0, match.start()) + 1
            if env == "document":
                self.issue("document_environment", "Page files must remain LaTeX fragments.", path=relative, line=line)
            if action == "begin":
                env_stack.append(env)
            elif not env_stack or env_stack[-1] != env:
                self.issue("latex_environment", "Environment closing order does not match its opening order.", path=relative, line=line, environment=env)
            else:
                env_stack.pop()
        for env in env_stack:
            self.issue("latex_environment", "An environment was not closed within its page.", path=relative, environment=env)
        for match in re.finditer(r"\\illegible\s*\{([^{}]*)\}", surface):
            if not re.fullmatch(r"[1-9]\d*", match.group(1).strip()):
                self.issue("illegible_count", "illegible must contain a positive integer word estimate.", path=relative, line=surface.count("\n", 0, match.start()) + 1)
        for command in STATE_MACROS:
            if re.search(r"\\" + command + r"\s*\{\s*\}", surface):
                self.issue("empty_state_macro", "A page-state macro has an empty argument.", path=relative, command=command)
        counts = self.report.setdefault("state_macro_counts", {})
        for command in STATE_MACROS:
            counts[command] = counts.get(command, 0) + commands[command]

    def check_pages(self) -> None:
        directory = self.root / "pages"
        if directory.is_symlink():
            self.issue("symlink", "The pages directory must not be a symbolic link.", path="pages")
            return
        if directory.is_dir():
            expected_names = {page_name(scan) for scan in SCANS}
            for path in sorted(directory.glob("*.tex")):
                if path.name not in expected_names:
                    self.issue("unexpected_page", "Unexpected page filename.", path=path.relative_to(self.root).as_posix())
        for scan in SCANS:
            relative = "pages/" + page_name(scan)
            data = self.read(relative, required=self.final)
            if data is not None:
                self.pages[scan] = data
                self.check_latex(data, relative, scan)
        present = sorted(self.pages)
        self.report["present_scans"] = present
        self.report["missing_scans"] = [scan for scan in SCANS if scan not in self.pages]
        if present != SCANS[:len(present)]:
            self.issue("page_sequence", "Existing pages must form a contiguous prefix of the requested scan sequence.")
        relative = PREFIX + "_transcription.tex"
        self.combined = self.read(relative, required=self.final)
        if self.combined is not None:
            expected = b"".join(self.pages[scan] for scan in sorted(self.pages))
            if self.combined != expected:
                self.issue("combined_mismatch", "Combined transcription differs from exact page-byte concatenation in scan order.", path=relative)
            self.report["combined_sha256"] = digest(self.combined)

    def check_inventory(self) -> None:
        relative = PREFIX + "_inventory.csv"
        data = self.read(relative)
        if data is None:
            return
        text = self.decode(data, relative)
        if text is None:
            return
        try:
            reader = csv.DictReader(io.StringIO(text, newline=""), strict=True)
            if reader.fieldnames != FIELDS:
                self.issue("inventory_schema", "Inventory column names or order differ from the required schema.", path=relative, expected=FIELDS, actual=reader.fieldnames)
                return
            self.rows = list(reader)
        except csv.Error as exc:
            self.issue("inventory_csv", str(exc), path=relative)
            return
        counts: Counter[int] = Counter()
        seen: set[tuple[int, str]] = set()
        sheets: dict[int, str] = {}
        for number, row in enumerate(self.rows, start=2):
            if None in row or any(value is None for value in row.values()):
                self.issue("inventory_width", "Inventory record has the wrong number of columns.", row=number)
                continue
            row = {key: value.strip() for key, value in row.items()}
            if row["cote"] != "43":
                self.issue("inventory_cote", "Inventory cote must be 43.", row=number)
            try:
                scan = int(row["scan"])
            except ValueError:
                scan = -1
            if scan not in SCANS:
                self.issue("inventory_scan", "Inventory row has an unexpected scan number.", row=number)
                continue
            counts[scan] += 1
            if row["sheet_kind"] not in SHEET_KINDS:
                self.issue("inventory_sheet_kind", "Inventory sheet_kind is not permitted.", row=number)
            if scan in sheets and sheets[scan] != row["sheet_kind"]:
                self.issue("inventory_sheet_inconsistent", "Rows for one scan use different sheet kinds.", row=number, scan=scan)
            sheets[scan] = row["sheet_kind"]
            if row["kind"] not in KINDS:
                self.issue("inventory_kind", "Inventory kind is not permitted.", row=number)
            if row["transcribed"] != "yes":
                self.issue("inventory_unfinished", "Every inventory row must have transcribed=yes.", row=number, scan=scan)
            for key in ("element", "position", "first_words_or_objects"):
                if not row[key]:
                    self.issue("inventory_empty", "An inventory identification field is empty.", row=number, column=key)
            identity = (scan, row["element"])
            if identity in seen:
                self.issue("inventory_duplicate", "Element identifiers must be unique within a scan.", row=number, scan=scan)
            seen.add(identity)
            if scan not in self.pages:
                self.issue("inventory_missing_page", "Inventory row refers to a missing page file.", row=number, scan=scan)
        for scan in self.pages:
            if not counts[scan]:
                self.issue("inventory_coverage", "A written page has no inventory records.", scan=scan)
        self.report["inventory"] = {"rows": len(self.rows), "rows_by_scan": dict(sorted(counts.items()))}

    def check_log(self) -> None:
        data = self.read("progress.log")
        if data is None:
            return
        text = self.decode(data, "progress.log")
        if text is None:
            return
        self.log = text.splitlines()
        if not self.log or utc_timestamp(self.log[0].strip()) is None:
            self.issue("log_start", "The first line of progress.log must be an explicit UTC timestamp.")
        done: dict[int, int] = {}
        audited: dict[int, int] = {}
        frozen: list[int] = []
        context: list[int] = []
        verified: list[int] = []
        hashes: dict[str, tuple[str, int]] = {}
        patterns = [
            ("done", re.compile(r"43 scan (\d{3}) done (.+)")),
            ("audited", re.compile(r"(?:43 )?scan (\d{3}) audited (.+)")),
            ("frozen", re.compile(r"transcription frozen (.+)")),
            ("context", re.compile(r"context opened (.+)")),
            ("verified", re.compile(r"(?:frozen )?hashes (?:verified )?unchanged (.+)")),
        ]
        for index, raw in enumerate(self.log, start=1):
            line = raw.strip()
            for event, pattern in patterns:
                match = pattern.fullmatch(line)
                if match is None:
                    continue
                stamp = match.groups()[-1]
                if utc_timestamp(stamp) is None:
                    self.issue("log_timestamp", "Event has no parseable explicit UTC timestamp.", line=index, event=event)
                if event in {"done", "audited"}:
                    scan = int(match.group(1))
                    target = done if event == "done" else audited
                    if scan not in SCANS:
                        self.issue("log_scan", "Log event refers to an unexpected scan.", line=index, scan=scan)
                    if scan in target:
                        self.issue("duplicate_event", "Log contains a repeated page event; the first occurrence is used for sequence checks.", warning=True, line=index, scan=scan, event=event)
                    else:
                        target[scan] = index
                else:
                    {"frozen": frozen, "context": context, "verified": verified}[event].append(index)
                break
            match = re.fullmatch(r"sha256 ([0-9a-fA-F]{64}) (.+)", line)
            if match:
                value, relative = match.groups()
                path = Path(relative)
                if path.is_absolute() or ".." in path.parts or path.as_posix() != relative:
                    self.issue("hash_path", "Hash paths must be relative POSIX paths without parent traversal.", line=index)
                elif relative in hashes and hashes[relative][0] != value.lower():
                    self.issue("hash_conflict", "Progress log records different freeze hashes for one file.", line=index, path=relative)
                else:
                    hashes[relative] = (value.lower(), index)
            elif line.startswith("sha256 "):
                self.issue("hash_syntax", "Use: sha256 <64 hexadecimal characters> <relative-path>.", line=index)
        for scan in self.pages:
            if scan not in done:
                self.issue("missing_done", "Written page lacks its completion event.", scan=scan)
        for scan in done:
            if scan not in self.pages:
                self.issue("done_missing_page", "Completion event refers to a missing page file.", scan=scan)
        if list(done) != SCANS[:len(done)]:
            self.issue("done_order", "First completion events do not follow the requested page sequence.")
        audit_required = self.final or bool(frozen)
        if audit_required:
            for scan in SCANS:
                if scan not in audited:
                    self.issue("missing_audit", "Page lacks its second-reading audit event.", scan=scan)
        for scan, index in audited.items():
            if scan not in done or index <= done[scan]:
                self.issue("audit_before_done", "Audit must follow the page completion event.", scan=scan)
        if audited and done and min(audited.values()) <= max(done.values()):
            self.issue("audit_before_full_pass", "Second-reading audits must follow completion of the entire first pass.")
        if self.final and not frozen:
            self.issue("missing_freeze", "No transcription frozen event is recorded.")
        if len(frozen) > 1:
            self.issue("multiple_freezes", "More than one freeze event is recorded; the first is authoritative.", warning=True)
        if context and (not frozen or min(context) <= min(frozen)):
            self.issue("context_before_freeze", "Context opening must follow the freeze event.")
        if self.final and not context:
            self.issue("missing_context_event", "No context opened event is recorded.")
        if frozen:
            freeze_index = min(frozen)
            if audited and max(audited.values()) >= freeze_index:
                self.issue("freeze_before_audit", "Freeze event must follow every audit event.")
            required_hashes = ["pages/" + page_name(scan) for scan in SCANS] + [PREFIX + "_transcription.tex"]
            for relative in required_hashes:
                if relative not in hashes:
                    self.issue("missing_freeze_hash", "Frozen transcription file has no SHA-256 entry.", path=relative)
                elif hashes[relative][1] >= freeze_index:
                    self.issue("late_freeze_hash", "Freeze hashes must be recorded before the freeze event.", path=relative)
        mismatches = []
        for relative, (expected, _) in hashes.items():
            data = self.read(relative)
            if data is not None and digest(data) != expected:
                mismatches.append(relative)
                self.issue("changed_frozen_file", "File bytes differ from the hash recorded at freeze.", path=relative)
        if self.final and (not verified or (context and max(verified) <= max(context))):
            self.issue("missing_hash_verification_event", "Record 'frozen hashes unchanged <UTC timestamp>' after the context work and hash verification.")
        self.report["progress"] = {
            "done_scans": list(done), "audited_scans": list(audited),
            "freeze_events": len(frozen), "context_open_events": len(context),
            "hash_entries": len(hashes), "hash_mismatches": mismatches,
            "post_context_verification_events": len(verified),
        }

    def check_other_deliverables(self) -> None:
        for suffix in ("_doubts.md", "_notes.md"):
            relative = PREFIX + suffix
            data = self.read(relative, required=self.final)
            if data is not None and not data.strip():
                self.issue("empty_deliverable", "A required deliverable is empty.", path=relative)
            if data is not None:
                self.decode(data, relative)

    def validate(self) -> dict:
        if not self.root.is_dir():
            self.issue("missing_root", "Package root does not exist.")
        else:
            self.check_pages()
            self.check_inventory()
            self.check_log()
            self.check_other_deliverables()
        self.report["ok"] = not self.report["errors"]
        return self.report

    def package(self, destination: Path) -> None:
        """Archive the complete work directory, excluding supplied sources and old ZIPs."""
        if self.report["errors"]:
            self.report["zip"] = {"created": False, "reason": "Validation errors must be resolved before packaging."}
            return
        destination = destination.resolve()
        candidates: list[tuple[Path, str]] = []
        excluded = []
        for path in sorted(self.root.rglob("*")):
            relative = path.relative_to(self.root)
            name = relative.as_posix()
            if any(part in EXCLUDED_DIRS for part in relative.parts):
                if path.is_file():
                    excluded.append(name)
                continue
            if path.is_symlink():
                self.issue("symlink", "Symbolic links are not read or packaged.", path=name)
                continue
            if not path.is_file():
                continue
            if path.suffix.lower() in EXCLUDED_SUFFIXES or path == destination or path.name == ".DS_Store":
                excluded.append(name)
                continue
            candidates.append((path, name))
        if self.report["errors"]:
            self.report["ok"] = False
            self.report["zip"] = {"created": False, "reason": "Unsafe archive members were found."}
            return
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            self.issue("zip_exists", "Refusing to overwrite an existing ZIP; choose a new destination or remove the intended replaceable final ZIP explicitly.", path=str(destination))
            self.report["ok"] = False
            return
        temporary = destination.with_name(destination.name + ".tmp")
        if temporary.exists():
            self.issue("zip_temporary_exists", "Refusing to overwrite an existing temporary archive.", path=str(temporary))
            self.report["ok"] = False
            return
        try:
            with zipfile.ZipFile(temporary, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
                for path, relative in candidates:
                    archive.write(path, relative)
            with zipfile.ZipFile(temporary) as archive:
                bad_member = archive.testzip()
                if bad_member is not None:
                    raise OSError("ZIP CRC validation failed for " + bad_member)
            temporary.rename(destination)
        except (OSError, zipfile.BadZipFile) as exc:
            self.issue("zip_error", str(exc), path=str(destination))
            self.report["ok"] = False
            if temporary.exists():
                temporary.unlink()
            return
        self.report["zip"] = {
            "created": True, "path": str(destination), "member_count": len(candidates),
            "size_bytes": destination.stat().st_size, "sha256": digest(destination.read_bytes()),
            "excluded": excluded,
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="Package directory (default: parent of this scripts directory).")
    parser.add_argument("--stage", required=True, choices=("checkpoint", "final"))
    parser.add_argument("--zip", type=Path, dest="zip_path", help="Create a new ZIP after successful validation; never overwrite one.")
    arguments = parser.parse_args(argv)
    validator = Validator(arguments.root, arguments.stage)
    report = validator.validate()
    if arguments.zip_path is not None:
        validator.package(arguments.zip_path)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
