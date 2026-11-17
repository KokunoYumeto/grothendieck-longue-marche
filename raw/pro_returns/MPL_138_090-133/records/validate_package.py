#!/usr/bin/env python3
"""Mechanical checks only: this program never reads images or context sources.

No result from this script establishes manuscript accuracy or visual completeness.
It uses only deliverable TeX/CSV/TSV/Markdown and progress.log in the supplied root.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import re
import sys
from datetime import datetime
from pathlib import Path

PREFIX = "MPL_138_090-133"
SCANS = [90, 91, *range(93, 134)]
INVENTORY_COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
EVENT_COLUMNS = ["statement_id", "date", "who", "type", "outcome"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEETS = {"text", "reused_typed", "cancelled_draft", "cover"}
EVENT_TYPES = {
    "targeted proof check", "independent re-proof", "computation or formal certificate",
    "used and rechecked in this run", "carried as background without fault found",
}
SCOPE = ("Mechanical validation only. The program does not open scans or context sources, "
         "assess readings, establish diagram fidelity, or certify visual completeness. "
         "An inventory entry or audit log line records an assertion; it does not prove that assertion.")


def escaped(text: str, index: int) -> bool:
    n = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        n += 1
        index -= 1
    return bool(n % 2)


def uncomment(text: str) -> str:
    """Blank comments without changing character positions or line numbers."""
    out = list(text)
    in_comment = False
    for i, ch in enumerate(text):
        if ch == "\n":
            in_comment = False
        elif in_comment:
            out[i] = " "
        elif ch == "%" and not escaped(text, i):
            in_comment = True
            out[i] = " "
    return "".join(out)


def line_at(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def group_at(text: str, opening: int) -> tuple[str | None, int]:
    if opening >= len(text) or text[opening] != "{":
        return None, opening
    depth = 1
    for i in range(opening + 1, len(text)):
        if escaped(text, i):
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[opening + 1:i], i + 1
    return None, len(text)


def argument_at(text: str, opening: int) -> tuple[str | None, int]:
    """Read one TeX argument, including a legal unbraced single token."""
    while opening < len(text) and text[opening].isspace():
        opening += 1
    if opening >= len(text) or text[opening] == "}":
        return None, opening
    if text[opening] == "{":
        return group_at(text, opening)
    if text[opening] == "\\":
        match = re.match(r"\\(?:[A-Za-z]+|[^A-Za-z])", text[opening:])
        if match:
            return match.group(0), opening + len(match.group(0))
        return None, opening
    return text[opening], opening + 1


def timestamp(value: str) -> datetime | None:
    value = value.strip()
    for fmt in ("%Y-%m-%d %H:%M:%S UTC", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass
    return None


class Validator:
    def __init__(self, root: Path, partial: bool):
        self.root, self.partial = root, partial
        self.issues: list[dict] = []
        self.uncertainties: list[dict] = []
        self.counts: dict = {}
        self.pages: dict[int, str] = {}

    def issue(self, level: str, code: str, message: str, path: str | None = None, line: int | None = None):
        item = {"level": level, "code": code, "message": message}
        if path is not None:
            item["path"] = path
        if line is not None:
            item["line"] = line
        self.issues.append(item)

    def missing(self, code: str, message: str, path: str | None = None):
        self.issue("info" if self.partial else "error", code, message, path)

    def read(self, relative: str, required: bool = True) -> str | None:
        path = self.root / relative
        if not path.is_file():
            if required:
                self.missing("missing_file", "Required deliverable is absent.", relative)
            return None
        try:
            return path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            self.issue("error", "unreadable_file", str(exc), relative)
            return None

    def check_tex(self, text: str, path: str, collect: bool = True):
        clean = uncomment(text)
        forbidden = r"\\(?:documentclass|usepackage|RequirePackage|newcommand|renewcommand|providecommand|def|gdef|xdef|includegraphics|includesvg|includepdf|include|input)\b|\\begin\s*\{document\}"
        for match in re.finditer(forbidden, clean):
            self.issue("error", "preamble_or_external_content", f"Disallowed fragment command: {match.group(0)}", path, line_at(clean, match.start()))
        stack: list[int] = []
        for i, char in enumerate(clean):
            if escaped(clean, i):
                continue
            if char == "{":
                stack.append(i)
            elif char == "}":
                if stack:
                    stack.pop()
                else:
                    self.issue("error", "extra_closing_brace", "Unmatched closing brace.", path, line_at(clean, i))
        for pos in stack:
            self.issue("error", "unclosed_brace", "Unclosed brace.", path, line_at(clean, pos))
        envs: list[tuple[str, int]] = []
        for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
            action, name = match.groups()
            if action == "begin":
                envs.append((name, match.start()))
            elif not envs:
                self.issue("error", "extra_environment_end", f"Unmatched end of {name}.", path, line_at(clean, match.start()))
            elif envs[-1][0] != name:
                self.issue("error", "environment_mismatch", f"End of {name} while {envs[-1][0]} is open.", path, line_at(clean, match.start()))
            else:
                envs.pop()
        for name, pos in envs:
            self.issue("error", "unclosed_environment", f"Unclosed {name} environment.", path, line_at(clean, pos))
        placeholder = r"\[\s*(?:\.\s*\.\s*\.|…)\s*\]|\b(?:TODO|FIXME|TBD|PLACEHOLDER)\b"
        for match in re.finditer(placeholder, clean):
            self.issue("warning", "possible_placeholder", f"Review literal {match.group(0)!r}; it may be manuscript text but must not substitute for omitted content.", path, line_at(clean, match.start()))
        for match in re.finditer(r"\\(unsure|illegible|diagram|figure)(?![A-Za-z])\s*", clean):
            if escaped(clean, match.start()):
                continue
            macro = match.group(1)
            body, end = argument_at(clean, match.end())
            if body is None:
                self.issue("error", "missing_macro_argument", f"Missing or unclosed argument for \\{macro}.", path, line_at(clean, match.start()))
                continue
            if not body.strip():
                self.issue("error", "empty_macro_argument", f"Empty argument for \\{macro}.", path, line_at(clean, match.start()))
            if macro in {"unsure", "illegible"} and collect:
                self.uncertainties.append({"path": path, "line": line_at(clean, match.start()), "macro": macro, "content": body.strip()})
            if macro == "illegible" and not re.fullmatch(r"\d+", body.strip()):
                self.issue("warning", "illegible_count", "The illegible argument should estimate a number of words.", path, line_at(clean, match.start()))
            if macro == "diagram" and not re.search(r"\\begin\s*\{(?:tikzcd|array)\}", body):
                self.issue("warning", "diagram_form", "No tikzcd or array environment found in diagram argument; review against the requested form.", path, line_at(clean, match.start()))
            if macro == "figure" and not re.search(r"\\begin\s*\{tikzpicture\}|\\tikz\b", body):
                self.issue("warning", "figure_form", "No TikZ construction found in figure argument.", path, line_at(clean, match.start()))

    def check_pages(self):
        expected_names = {f"{PREFIX}_138_scan{scan:03d}.tex" for scan in SCANS}
        for path in sorted((self.root / "pages").glob("*.tex")):
            if path.name not in expected_names:
                self.issue("error", "unexpected_page_file", "Unexpected TeX filename in pages/.", f"pages/{path.name}")
        for scan in SCANS:
            name = f"pages/{PREFIX}_138_scan{scan:03d}.tex"
            text = self.read(name)
            if text is None:
                continue
            self.pages[scan] = text
            clean = uncomment(text)
            matches = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
            if matches != [str(scan)]:
                self.issue("error", "scanpage_mismatch", f"Expected exactly \\scanpage{{{scan}}}; found {matches}.", name)
            cotefiles = re.findall(r"\\cotefile\s*\{([^{}]*)\}", clean)
            if cotefiles and (scan != SCANS[0] or cotefiles != ["138"]):
                self.issue("error", "cotefile_placement", "Only the first page may contain the single cote 138 marker.", name)
            prefix = re.split(r"\\scanpage\s*\{\s*\d+\s*\}", clean, maxsplit=1)[0]
            prefix = re.sub(r"\\cotefile\s*\{138\}", "", prefix)
            if prefix.strip():
                self.issue("warning", "text_before_scanpage", "Non-comment content precedes the page marker.", name)
            self.check_tex(text, name)
        self.counts["expected_pages"] = len(SCANS)
        self.counts["present_pages"] = len(self.pages)

    def check_combined(self):
        name = f"{PREFIX}_transcription.tex"
        text = self.read(name)
        if text is None:
            return
        clean = uncomment(text)
        markers = list(re.finditer(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean))
        found = [int(x.group(1)) for x in markers]
        expected = list(self.pages) if self.partial else SCANS
        if found != expected:
            self.issue("error", "combined_scan_order", f"Combined page order {found} differs from expected {expected}.", name)
        prefix = clean[:markers[0].start()].strip() if markers else clean.strip()
        if prefix != r"\cotefile{138}":
            self.issue("error", "combined_cote_prefix", "Combined fragment must begin with the single cote 138 marker before its first scan.", name)
        for i, marker in enumerate(markers):
            scan = int(marker.group(1))
            if scan not in self.pages:
                continue
            end = markers[i + 1].start() if i + 1 < len(markers) else len(text)
            combined_block = text[marker.start():end].strip()
            page = self.pages[scan]
            page_marker = re.search(r"\\scanpage\s*\{\s*\d+\s*\}", uncomment(page))
            if page_marker and combined_block != page[page_marker.start():].strip():
                self.issue("error", "combined_page_difference", f"Combined scan {scan:03d} is not byte-for-byte equal to its page fragment after trimming boundary whitespace.", name)
        self.check_tex(text, name, collect=False)

    def check_inventory(self):
        name = f"{PREFIX}_inventory.csv"
        text = self.read(name)
        if text is None:
            return
        reader = csv.DictReader(io.StringIO(text))
        if reader.fieldnames != INVENTORY_COLUMNS:
            self.issue("error", "inventory_header", f"Expected header {INVENTORY_COLUMNS}; found {reader.fieldnames}.", name)
            return
        counts = collections.Counter()
        keys: set[tuple[str, int, str]] = set()
        row_count = 0
        for row in reader:
            row_count += 1
            line = reader.line_num
            if None in row or any(value is None for value in row.values()):
                self.issue("error", "inventory_column_count", "Row has missing or extra CSV columns.", name, line)
                continue
            try:
                scan = int(row["scan"])
            except ValueError:
                self.issue("error", "inventory_scan", "Scan is not an integer.", name, line)
                continue
            counts[scan] += 1
            if row["cote"] != "138" or scan not in SCANS:
                self.issue("error", "inventory_source", "Unexpected cote or scan.", name, line)
            if row["sheet_kind"] not in SHEETS:
                self.issue("error", "inventory_sheet_kind", f"Invalid sheet_kind {row['sheet_kind']!r}.", name, line)
            if row["kind"] not in KINDS:
                self.issue("error", "inventory_kind", f"Invalid kind {row['kind']!r}.", name, line)
            if row["transcribed"] != "yes":
                self.issue("error", "inventory_not_yes", "transcribed must be exactly yes.", name, line)
            for field in ("element", "position", "first_words_or_objects"):
                if not row[field].strip():
                    self.issue("error", "inventory_empty_field", f"Empty {field}.", name, line)
            key = (row["cote"], scan, row["element"])
            if key in keys:
                self.issue("error", "inventory_duplicate_element", f"Duplicate element key {key}.", name, line)
            keys.add(key)
        for scan in SCANS:
            if not counts[scan]:
                self.missing("inventory_missing_scan", f"No inventory elements for scan {scan:03d}.", name)
        self.counts["inventory_rows"] = row_count
        self.counts["inventory_rows_by_scan"] = dict(sorted(counts.items()))

    def check_events(self):
        name = "CHECK_EVENTS.tsv"
        text = self.read(name)
        if text is None:
            return
        reader = csv.DictReader(io.StringIO(text), delimiter="\t")
        if reader.fieldnames != EVENT_COLUMNS:
            self.issue("error", "events_header", f"Expected header {EVENT_COLUMNS}; found {reader.fieldnames}.", name)
            return
        count = 0
        for row in reader:
            count += 1
            if None in row or any(value is None for value in row.values()):
                self.issue("error", "events_column_count", "Event has missing or extra TSV columns.", name, reader.line_num)
                continue
            for field, value in row.items():
                if not value.strip():
                    self.issue("error", "events_empty_field", f"Empty {field}.", name, reader.line_num)
            if timestamp(row["date"]) is None:
                self.issue("warning", "event_date_format", "Date is not in a recognized ISO/UTC form.", name, reader.line_num)
            if row["type"] not in EVENT_TYPES and not row["type"].startswith("refuted"):
                self.issue("error", "event_type", f"Unrecognized check-event type {row['type']!r}.", name, reader.line_num)
        self.counts["check_events"] = count

    def check_progress(self):
        name = "progress.log"
        text = self.read(name)
        if text is None:
            return
        lines = text.splitlines()
        if not lines or timestamp(lines[0]) is None:
            self.issue("error", "start_timestamp", "First progress.log line must be the initial current UTC time.", name, 1)
        done, audited = collections.defaultdict(list), collections.defaultdict(list)
        done_order: list[int] = []
        freeze_lines, context_lines = [], []
        for i, line in enumerate(lines, 1):
            match = re.match(r"^138 scan (\d+) done\s+(.+)$", line)
            if match:
                scan = int(match.group(1))
                done[scan].append(i)
                done_order.append(scan)
                if timestamp(match.group(2)) is None:
                    self.issue("warning", "done_timestamp", "Unrecognized done timestamp.", name, i)
            match = re.match(r"^(?:138 )?scan (\d+) audited\s+(.+)$", line)
            if match:
                scan = int(match.group(1))
                audited[scan].append(i)
                if timestamp(match.group(2)) is None:
                    self.issue("warning", "audit_timestamp", "Unrecognized audit timestamp.", name, i)
            if re.match(r"^transcription frozen\b", line):
                freeze_lines.append(i)
            if re.match(r"^context opened\b", line):
                context_lines.append(i)
        for scan in SCANS:
            if not done[scan]:
                self.missing("missing_done_record", f"No done record for scan {scan:03d}.", name)
            if not audited[scan]:
                self.missing("missing_audit_record", f"No audit record for scan {scan:03d}.", name)
            if len(done[scan]) > 1 or len(audited[scan]) > 1:
                self.issue("warning", "duplicate_progress_record", f"More than one done or audited entry for scan {scan:03d}; review chronology.", name)
        for scan in set(done) | set(audited):
            if scan not in SCANS:
                self.issue("error", "unexpected_progress_scan", f"Unexpected scan {scan} in a progress event.", name)
        first_done_order = list(dict.fromkeys(done_order))
        if first_done_order != sorted(first_done_order):
            self.issue("error", "done_order", "First done records do not follow increasing scan order.", name)
        actual_done_lines = [n for entries in done.values() for n in entries]
        actual_audit_lines = [n for entries in audited.values() for n in entries]
        if actual_done_lines and actual_audit_lines and min(actual_audit_lines) < max(actual_done_lines):
            self.issue("warning", "audit_before_all_done", "An audit record precedes a later done record; check whether the required second full reading is documented separately.", name)
        if not freeze_lines:
            self.missing("missing_freeze_record", "No transcription frozen event.", name)
        if context_lines and (not freeze_lines or min(context_lines) < min(freeze_lines)):
            self.issue("error", "context_before_freeze", "Context-opened event occurs before any freeze event.", name)
        if freeze_lines and actual_audit_lines and min(freeze_lines) < max(actual_audit_lines):
            self.issue("warning", "audit_after_freeze", "An audit record occurs after freezing; review the chronology and whether any text changed.", name)
        # Accept sha256sum format, labelled SHA-256 lines, or path: hash lines.
        # Only exact expected deliverable basenames are recognized; nothing outside root is read.
        expected_paths = [f"pages/{PREFIX}_138_scan{s:03d}.tex" for s in SCANS] + [f"{PREFIX}_transcription.tex"]
        hashes: dict[str, tuple[str, int]] = {}
        limit = min(context_lines) - 1 if context_lines else len(lines)
        for i, line in enumerate(lines[:limit], 1):
            digests = re.findall(r"(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])", line)
            if len(digests) != 1:
                continue
            for rel in expected_paths:
                if Path(rel).name in line:
                    hashes[rel] = (digests[0].lower(), i)
        for rel, (expected, line) in hashes.items():
            path = self.root / rel
            if path.is_file():
                observed = hashlib.sha256(path.read_bytes()).hexdigest()
                if observed != expected:
                    self.issue("error", "frozen_hash_mismatch", f"Current SHA-256 {observed} differs from logged {expected}.", rel, line)
        if freeze_lines:
            for rel in expected_paths:
                if rel not in hashes:
                    self.issue("error", "missing_frozen_hash", "Freeze recorded but no corresponding SHA-256 found before context was opened.", rel)
            if not re.search(r"hash(?:es)?.*(?:unchanged|verified)|(?:unchanged|verified).*hash", text, re.I):
                self.issue("warning", "final_hash_confirmation", "No explicit unchanged/verified-hashes statement detected; add the actual final check to progress.log.", name)
        self.counts["done_records"] = sum(len(x) for x in done.values())
        self.counts["audit_records"] = sum(len(x) for x in audited.values())
        self.counts["recognized_frozen_hashes"] = len(hashes)

    def check_notes_and_doubts(self):
        name = f"{PREFIX}_doubts.md"
        doubts = self.read(name)
        self.read(f"{PREFIX}_notes.md")
        if doubts is not None:
            if not re.search(r"notation", doubts[:3000], re.I):
                self.issue("warning", "notation_table_heading", "No notation heading detected near the top of the doubts file.", name)
            for term in ("abbreviations", "legib"):
                if not re.search(term, doubts, re.I):
                    self.issue("warning", "doubts_section", f"No heading or text matching {term!r} detected.", name)
        by_scan = collections.Counter()
        for item in self.uncertainties:
            match = re.search(r"scan(\d+)", item["path"])
            if match:
                by_scan[int(match.group(1))] += 1
        self.counts["uncertainty_occurrences"] = len(self.uncertainties)
        self.counts["uncertainties_by_scan"] = dict(sorted(by_scan.items()))

    def run(self) -> dict:
        self.check_pages()
        self.check_combined()
        self.check_inventory()
        self.check_events()
        self.check_progress()
        self.check_notes_and_doubts()
        levels = collections.Counter(item["level"] for item in self.issues)
        return {"scope": SCOPE, "mode": "partial" if self.partial else "final", "root": str(self.root),
                "mechanical_status": "errors" if levels["error"] else "no_mechanical_errors_detected",
                "issue_counts": {k: levels[k] for k in ("error", "warning", "info")},
                "counts": self.counts, "issues": self.issues, "uncertainties": self.uncertainties}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--partial", action="store_true", help="Treat absent work as informational while production is ongoing.")
    parser.add_argument("--json", action="store_true", help="Print the complete JSON report, including every uncertainty occurrence.")
    parser.add_argument("--output", type=Path, help="Also write the complete JSON report to this explicit output path.")
    args = parser.parse_args()
    result = Validator(args.root.resolve(), args.partial).run()
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    if args.json:
        print(payload, end="")
    else:
        print(SCOPE)
        print(f"Mode: {result['mode']}; status: {result['mechanical_status']}")
        print("Issues: " + ", ".join(f"{key}={value}" for key, value in result["issue_counts"].items()))
        print("Counts: " + json.dumps(result["counts"], ensure_ascii=False, sort_keys=True))
        for item in result["issues"]:
            location = item.get("path", "") + (f":{item['line']}" if "line" in item else "")
            print(f"{item['level'].upper()} {item['code']} {location}: {item['message']}")
    return 1 if result["issue_counts"]["error"] else 0


if __name__ == "__main__":
    sys.exit(main())
