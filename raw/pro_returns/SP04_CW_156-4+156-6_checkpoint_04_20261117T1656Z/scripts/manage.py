#!/usr/bin/env python3
"""Administrative helpers for SP04. No image reading or textual decisions.

Only explicit mark_done/mark_audited calls record a reading as completed.
The caller authors every page and every evidence record. See README.md.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

PREFIX = "SP04_CW_156-4+156-6"
DEFAULT_OUT = Path(__file__).resolve().parents[1]
DEFAULT_MAP = DEFAULT_OUT.parent / "witnesses" / "page_map.tsv"
EXPECTED_COUNT = 120
CONFIDENCES = ("high", "medium", "low")
KINDS = (
    "misread word", "misread symbol or index", "omission",
    "text not on the page", "deletion state (struck given live or live given struck)",
    "insertion or placement", "abbreviation expanded or spelling modernised",
    "readable ink left as \\ill{}", "drawing or diagram", "other",
)
INVENTORY_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def parse_time(value: str) -> datetime:
    value = value.strip()
    if value.endswith(" UTC"):
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)


def atomic_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(value, encoding="utf-8")
    temp.replace(path)


def md(value) -> str:
    if isinstance(value, list):
        value = "; ".join(str(x) for x in value)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", "<br>")


class Project:
    def __init__(self, out=DEFAULT_OUT, page_map=DEFAULT_MAP):
        self.out = Path(out).resolve()
        self.page_map = Path(page_map).resolve()
        with self.page_map.open(encoding="utf-8", newline="") as handle:
            self.pages = list(csv.DictReader(handle, delimiter="\t"))
        self.by_key = {(row["cote"], int(row["our_scan"])): row for row in self.pages}
        if len(self.by_key) != len(self.pages):
            raise ValueError("page_map contains duplicate cote/scan pairs")

    def row(self, cote, scan):
        return self.by_key[(str(cote), int(scan))]

    def record_path(self, cote, scan):
        return self.out / "records" / f"{cote}_scan{int(scan):03d}.json"

    def page_path(self, cote, scan):
        return self.out / "pages" / Path(self.row(cote, scan)["codex_file"]).name

    def load_record(self, cote, scan):
        path = self.record_path(cote, scan)
        if not path.exists():
            return {"cote": str(cote), "scan": int(scan)}
        result = json.loads(path.read_text(encoding="utf-8"))
        if str(result.get("cote")) != str(cote) or int(result.get("scan", -1)) != int(scan):
            raise ValueError(f"Record identity mismatch: {path}")
        return result

    def save_record(self, record):
        """Save caller-authored data, preserving completion status from disk.

        Status cannot be set through this API: use the explicit mark methods.
        Direct manual JSON editing remains the caller's responsibility.
        """
        cote, scan = str(record["cote"]), int(record["scan"])
        self.row(cote, scan)
        old = self.load_record(cote, scan)
        record = dict(record)
        record["status"] = old.get("status", {})
        self._save_record(record)

    def _save_record(self, record):
        atomic_text(self.record_path(record["cote"], record["scan"]),
                    json.dumps(record, ensure_ascii=False, indent=2) + "\n")

    def _append_log(self, line):
        path = self.out / "progress.log"
        if not path.exists() or not path.read_text(encoding="utf-8").strip():
            raise ValueError("Root must initialize progress.log with current UTC before any mark")
        with path.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")

    def _require_log(self):
        path = self.out / "progress.log"
        if not path.exists() or not path.read_text(encoding="utf-8").strip():
            raise ValueError("Root must initialize progress.log with current UTC before any mark")

    def _assert_unfrozen(self):
        if (self.out / "freeze.sha256").exists():
            raise ValueError("Transcription is frozen; page completion/audit mutations are locked")

    def validate_record(self, cote, scan):
        record = self.load_record(cote, scan)
        if not self.record_path(cote, scan).exists():
            raise ValueError(f"Missing manually authored record: {cote} {scan}")
        for key in ("changes", "inventory", "doubts"):
            if not isinstance(record.get(key), list):
                raise ValueError(f"{cote} {scan}: {key} must be an explicit list")
        if not record["inventory"]:
            raise ValueError(f"{cote} {scan}: inventory must contain actual element rows")
        for i, change in enumerate(record["changes"], 1):
            required = ("place", "C", "H", "final", "scan_shows", "crop", "confidence", "differs_C", "differs_H")
            if any(k not in change for k in required):
                raise ValueError(f"{cote} {scan}: change {i} lacks required fields")
            if change["confidence"] not in CONFIDENCES:
                raise ValueError(f"{cote} {scan}: change {i} invalid confidence")
            if not isinstance(change["differs_C"], bool) or not isinstance(change["differs_H"], bool):
                raise ValueError(f"{cote} {scan}: difference flags must be booleans")
            if change["differs_H"]:
                if change.get("kind") not in KINDS:
                    raise ValueError(f"{cote} {scan}: change {i} invalid collation kind")
                if change.get("marked_in_H") not in ("yes", "no", "unclear"):
                    raise ValueError(f"{cote} {scan}: change {i} marked_in_H must be yes/no/unclear")
        for i, element in enumerate(record["inventory"], 1):
            required = ("element", "kind", "position", "first_words_or_objects", "sheet_kind", "hand", "transcribed")
            if any(k not in element for k in required):
                raise ValueError(f"{cote} {scan}: inventory {i} lacks required fields")
            if element["kind"] not in INVENTORY_KINDS or element["sheet_kind"] not in SHEET_KINDS:
                raise ValueError(f"{cote} {scan}: inventory {i} invalid kind")
            if element["transcribed"] != "yes":
                raise ValueError(f"{cote} {scan}: inventory {i} not confirmed transcribed")
        for i, doubt in enumerate(record["doubts"], 1):
            if any(k not in doubt for k in ("line", "reading", "alternatives", "confidence")):
                raise ValueError(f"{cote} {scan}: doubt {i} lacks required fields")
            if doubt["confidence"] not in CONFIDENCES:
                raise ValueError(f"{cote} {scan}: doubt {i} invalid confidence")
        return record

    def mark_done(self, cote, scan):
        """Explicit caller attestation; never performs or asserts image inspection."""
        self._assert_unfrozen()
        target = self.row(cote, scan)
        for row in self.pages:
            if row is target:
                break
            prior = self.load_record(row["cote"], row["our_scan"])
            if not prior.get("status", {}).get("done"):
                raise ValueError(f"Earlier page is not done: {row['cote']} {row['our_scan']}")
        record = self.validate_record(cote, scan)
        if record.get("status", {}).get("done"):
            raise ValueError("Page already marked done; edit its record without adding another completion mark")
        page = self.page_path(cote, scan)
        if not page.exists() or not page.read_text(encoding="utf-8").strip():
            raise ValueError(f"Missing transcription: {page}")
        problems = check_latex(page.read_text(encoding="utf-8"))
        if problems:
            raise ValueError(f"Syntax check failed for {page.name}: {problems}")
        self._require_log()
        now = utcnow()
        record.setdefault("status", {})["done"] = now
        self._save_record(record)
        try:
            self.render()
        except Exception:
            record["status"].pop("done", None)
            self._save_record(record)
            raise
        self._append_log(f"scan {int(scan):03d} done {now} cote {cote}")
        return {"cote": str(cote), "scan": int(scan), "done": now}

    def mark_audited(self, cote, scan, audit_note=None):
        """Record an audit only on the caller's explicit instruction."""
        self._assert_unfrozen()
        if len(self.pages) != EXPECTED_COUNT:
            raise ValueError(f"Expected exactly {EXPECTED_COUNT} page-map rows")
        for row in self.pages:
            if not self.load_record(row["cote"], row["our_scan"]).get("status", {}).get("done"):
                raise ValueError("All pages must be done before second reading can be recorded")
        target = self.row(cote, scan)
        for row in self.pages:
            if row is target:
                break
            if not self.load_record(row["cote"], row["our_scan"]).get("status", {}).get("audited"):
                raise ValueError(f"Earlier page has no audit: {row['cote']} {row['our_scan']}")
        record = self.validate_record(cote, scan)
        if record.get("status", {}).get("audited"):
            raise ValueError("Page already marked audited")
        self._require_log()
        now = utcnow()
        record.setdefault("status", {})["audited"] = now
        if audit_note is not None:
            record["audit"] = audit_note
        self._save_record(record)
        try:
            self.render()
        except Exception:
            record["status"].pop("audited", None)
            self._save_record(record)
            raise
        self._append_log(f"scan {int(scan):03d} audited {now} cote {cote}")
        return {"cote": str(cote), "scan": int(scan), "audited": now}

    def completed(self):
        return [(row, self.load_record(row["cote"], row["our_scan"])) for row in self.pages
                if self.load_record(row["cote"], row["our_scan"]).get("status", {}).get("done")]

    def render(self):
        """Derive deliverables solely from completed page files and authored records."""
        completed = self.completed()
        combined = "\n\n".join(self.page_path(row["cote"], row["our_scan"]).read_text(encoding="utf-8").rstrip()
                              for row, _ in completed)
        if combined:
            combined += "\n"
        combined_path = self.out / f"{PREFIX}_transcription.tex"
        if (self.out / "freeze.sha256").exists():
            if not combined_path.exists() or combined_path.read_text(encoding="utf-8") != combined:
                raise ValueError("Frozen combined transcription would change; render refused")
        else:
            atomic_text(combined_path, combined)
        self._render_changes(completed)
        self._render_collation(completed)
        self._render_inventory(completed)
        self._render_doubts(completed)
        return {"completed": len(completed), "total": len(self.pages)}

    def _render_changes(self, completed):
        rows = [f"# {PREFIX}: changes", "", "Counts describe recorded places; a place may differ from both witnesses.", "",
                "| Cote / scan | Against C | C high | C medium | C low | Against H | H high | H medium | H low | Recorded places |",
                "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
        totals = [0] * 9
        for page, record in completed:
            changes = record.get("changes", [])
            counts = []
            for witness in ("C", "H"):
                subset = [c for c in changes if c.get(f"differs_{witness}")]
                counts.extend([len(subset)] + [sum(c["confidence"] == level for c in subset) for level in CONFIDENCES])
            counts.append(len(changes))
            totals = [x+y for x,y in zip(totals, counts)]
            rows.append(f"| {page['cote']} / {int(page['our_scan']):03d} | " + " | ".join(map(str, counts)) + " |")
        rows.append("| **Total** | " + " | ".join(map(str, totals)) + " |")
        rows.extend(["", "## Consequential corrections", ""])
        consequential = []
        for page, record in completed:
            for change in record.get("changes", []):
                if change.get("consequential"):
                    consequential.append(f"- {page['cote']} scan {int(page['our_scan']):03d}, {change['place']}: {change['consequential']}")
        rows.extend(consequential or ["No consequential correction has been recorded in the completed-page records."])
        for page, record in completed:
            rows.extend(["", f"## {page['cote']} — scan {int(page['our_scan']):03d}", "",
                         "| Place | Witness C | Witness H | Consolidated reading | Scan evidence and crop | Confidence |",
                         "|---|---|---|---|---|---|"])
            for change in record.get("changes", []):
                ink = change["scan_shows"] + ("; crop: " + str(change["crop"]) if change["crop"] else "")
                rows.append("| " + " | ".join(md(x) for x in (change["place"], change["C"], change["H"], change["final"], ink, change["confidence"])) + " |")
            if not record.get("changes"):
                rows.append("| — | — | — | — | No differences recorded for this page. | — |")
            rows.extend(["", "### Unresolved places", ""])
            doubts = record.get("doubts", [])
            rows.extend([f"- {d['line']}: {d['reading']}; alternatives: {md(d['alternatives'])}; confidence: {d['confidence']}. {d.get('comment', '')}" for d in doubts]
                        or ["None recorded."])
        atomic_text(self.out / f"{PREFIX}_changes.md", "\n".join(rows) + "\n")

    def _render_collation(self, completed):
        fields = ("folder", "their_page", "our_scan", "line", "their_reading", "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H", "confidence")
        buf = io.StringIO(newline="")
        writer = csv.writer(buf, delimiter="\t", lineterminator="\n")
        writer.writerow(fields)
        for page, record in completed:
            if page["hua_has"] != "text":
                continue
            for c in record.get("changes", []):
                if c.get("differs_H"):
                    evidence = c["scan_shows"] + ("; crop: " + str(c["crop"]) if c["crop"] else "")
                    writer.writerow([page["folder"], page["their_page"], page["our_scan"], c["place"], c["H"], c["C"], c["final"], evidence, c["kind"], c["marked_in_H"], c["confidence"]])
        atomic_text(self.out / f"{PREFIX}_collation.tsv", buf.getvalue())

    def _render_inventory(self, completed):
        fields = ("scan", "sheet_kind", "hand", "element", "kind", "position", "first_words_or_objects", "transcribed")
        buf = io.StringIO(newline="")
        writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for page, record in completed:
            for element in record.get("inventory", []):
                item = {key: element[key] for key in fields if key != "scan"}
                item["scan"] = record.get("scan_label", f"{page['cote']}:{int(page['our_scan']):03d}")
                writer.writerow(item)
        atomic_text(self.out / f"{PREFIX}_inventory.csv", buf.getvalue())

    def _render_doubts(self, completed):
        global_path = self.out / "notation.json"
        global_data = json.loads(global_path.read_text(encoding="utf-8")) if global_path.exists() else {}
        rows = [f"# {PREFIX}: notation and doubts", "", "## Notation table", "",
                "| Sign / function | LaTeX reading | Visible form | Locations | Alternatives / qualification |",
                "|---|---|---|---|---|"]
        notation = list(global_data.get("notation", []))
        for _, record in completed:
            notation.extend(record.get("notation", []))
        seen = set()
        for entry in notation:
            values = tuple(md(entry.get(k, "")) for k in ("sign", "latex", "appearance", "locations", "alternatives"))
            if values not in seen:
                rows.append("| " + " | ".join(values) + " |")
                seen.add(values)
        rows.extend(["", "## Remaining doubts", "", "| Cote / scan | Line / place | Reading | Alternatives | Confidence | Comment |", "|---|---|---|---|---|---|"])
        for page, record in completed:
            for doubt in record.get("doubts", []):
                rows.append("| " + " | ".join(md(v) for v in (f"{page['cote']} / {int(page['our_scan']):03d}", doubt["line"], doubt["reading"], doubt["alternatives"], doubt["confidence"], doubt.get("comment", ""))) + " |")
        rows.extend(["", "## Abbreviations", "", "Expansions in this table are editorial and are not inserted in the transcription.", "",
                     "| Written abbreviation | Proposed expansion | Evidence / qualification |", "|---|---|---|"])
        abbreviations = list(global_data.get("abbreviations", []))
        for _, record in completed:
            abbreviations.extend(record.get("abbreviations", []))
        seen = set()
        for entry in abbreviations:
            values = tuple(md(entry.get(k, "")) for k in ("abbreviation", "expansion", "evidence"))
            if values not in seen:
                rows.append("| " + " | ".join(values) + " |")
                seen.add(values)
        rows.extend(["", "## Legibility and witness comparison", ""])
        legibility = self.out / "legibility.md"
        rows.append(legibility.read_text(encoding="utf-8").strip() if legibility.exists()
                    else "Assessment has not yet been written.")
        atomic_text(self.out / f"{PREFIX}_doubts.md", "\n".join(rows) + "\n")

    def syntax_check(self, completed_only=True):
        result = {}
        for row in self.pages:
            if completed_only and not self.load_record(row["cote"], row["our_scan"]).get("status", {}).get("done"):
                continue
            path = self.page_path(row["cote"], row["our_scan"])
            result[path.name] = check_latex(path.read_text(encoding="utf-8")) if path.exists() else ["Missing page file"]
        return result

    def _validate_freeze_history(self, records):
        """Require canonical UTC statuses and exact ordered log corroboration."""
        timestamp_pattern = re.compile(r"\d{4}-\d\d-\d\d \d\d:\d\d:\d\d UTC")

        def timestamp(value, description):
            if not isinstance(value, str) or timestamp_pattern.fullmatch(value) is None:
                raise ValueError(f"{description}: expected an actual UTC timestamp string")
            try:
                return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
            except ValueError as error:
                raise ValueError(f"{description}: invalid UTC timestamp") from error

        log_path = self.out / "progress.log"
        if not log_path.is_file():
            raise ValueError("Missing progress.log")
        log_text = log_path.read_text(encoding="utf-8")
        lines = log_text.splitlines()
        if not lines:
            raise ValueError("progress.log is empty")
        started = timestamp(lines[0], "progress.log first line")
        now = datetime.now(timezone.utc)
        expected = {}
        for page, record in zip(self.pages, records):
            key = (page["cote"], int(page["our_scan"]))
            status = record.get("status")
            if not isinstance(status, dict):
                raise ValueError(f"{key}: status must be an object")
            for kind in ("done", "audited"):
                value = status.get(kind)
                parsed = timestamp(value, f"{key} status.{kind}")
                if parsed < started or parsed > now:
                    raise ValueError(f"{key} status.{kind}: timestamp is outside this run's elapsed interval")
                expected[(*key, kind)] = value
        event_pattern = re.compile(r"^scan (\d{3}) (done|audited) (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d UTC) cote ([0-9-]+)$")
        events = []
        seen = set()
        for number, line in enumerate(lines[1:], 2):
            if not line.startswith("scan ") or not re.search(r"\b(done|audited)\b", line):
                continue
            match = event_pattern.fullmatch(line)
            if match is None:
                raise ValueError(f"progress.log line {number}: malformed completion/audit event")
            scan, kind, value, cote = match.groups()
            key = (cote, int(scan), kind)
            timestamp(value, f"progress.log line {number}")
            if key not in expected:
                raise ValueError(f"progress.log line {number}: unexpected page/status event")
            if key in seen:
                raise ValueError(f"progress.log line {number}: duplicate completion/audit event")
            if value != expected[key]:
                raise ValueError(f"progress.log line {number}: timestamp does not match page record")
            seen.add(key)
            events.append((key, value))
        missing = [key for key in expected if key not in seen]
        if missing:
            raise ValueError(f"Missing matching progress.log event: {missing[0]} ({len(missing)} absent)")
        required_order = [(page["cote"], int(page["our_scan"]), kind)
                          for kind in ("done", "audited") for page in self.pages]
        if [key for key, _ in events] != required_order:
            raise ValueError("Completion/audit log events are not one full ordered done pass followed by one full ordered audit pass")
        values = [value for _, value in events]
        if values != sorted(values):
            raise ValueError("Completion/audit timestamps decrease in log order")
        return log_text

    def freeze(self):
        self._assert_unfrozen()
        if len(self.pages) != EXPECTED_COUNT:
            raise ValueError(f"Expected {EXPECTED_COUNT} pages, found {len(self.pages)}")
        records = []
        for page in self.pages:
            record = self.validate_record(page["cote"], page["our_scan"])
            if not isinstance(record.get("status"), dict) or not all(record["status"].get(k) for k in ("done", "audited")):
                raise ValueError(f"Page lacks completion or audit: {page['cote']} {page['our_scan']}")
            records.append(record)
        log_text = self._validate_freeze_history(records)
        failures = {k: v for k, v in self.syntax_check().items() if v}
        if failures:
            raise ValueError(f"Syntax failures: {failures}")
        self.render()
        paths = [self.page_path(row["cote"], row["our_scan"]) for row in self.pages]
        paths.append(self.out / f"{PREFIX}_transcription.tex")
        manifest = "".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(self.out).as_posix()}\n" for path in paths)
        if (self.out / "progress.log").read_text(encoding="utf-8") != log_text:
            raise ValueError("progress.log changed during freeze preparation; no frozen event was published")
        # Prepare and atomically persist every hash before publishing the frozen
        # event. The entire appended event/hash block is one atomic log replace.
        atomic_text(self.out / "freeze.sha256", manifest)
        separator = "" if log_text.endswith("\n") else "\n"
        atomic_text(self.out / "progress.log", log_text + separator + f"transcription frozen {utcnow()}\n" + manifest)
        return {"files": len(paths), "manifest": str(self.out / "freeze.sha256")}

    def verify_freeze(self, log=False):
        path = self.out / "freeze.sha256"
        if not path.exists():
            raise ValueError("No freeze manifest exists")
        results = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            expected, relative = line.split("  ", 1)
            target = self.out / relative
            results[relative] = target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() == expected
        ok = len(results) == EXPECTED_COUNT + 1 and all(results.values())
        if log:
            self._append_log(f"frozen hashes {'unchanged' if ok else 'FAILED'} {utcnow()}")
        return {"ok": ok, "files": len(results), "mismatches": [k for k, v in results.items() if not v]}

    def checkpoint(self):
        """Create an hourly ZIP only when >=3600 seconds have elapsed; never upload."""
        log = self.out / "progress.log"
        lines = log.read_text(encoding="utf-8").splitlines()
        if not lines:
            raise ValueError("progress.log is empty")
        started = parse_time(lines[0])
        last = started
        number = 0
        pattern = re.compile(r"^checkpoint (\d+) created (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d UTC)")
        for line in lines:
            match = pattern.match(line)
            if match:
                number = max(number, int(match.group(1)))
                last = max(last, parse_time(match.group(2)))
        now = datetime.now(timezone.utc)
        elapsed = (now - last).total_seconds()
        if elapsed < 3600:
            raise ValueError(f"Checkpoint not due: {3600-elapsed:.0f} seconds remain")
        existing = list(self.out.parent.glob(f"{PREFIX}_checkpoint_*.zip"))
        for file in existing:
            match = re.search(r"_checkpoint_(\d+)\.zip$", file.name)
            if match:
                number = max(number, int(match.group(1)))
        number += 1
        target = self.out.parent / f"{PREFIX}_checkpoint_{number:02d}.zip"
        if target.exists():
            raise FileExistsError(target)
        self.render()
        entry = f"checkpoint {number:02d} created {utcnow()} {target.name}"
        with zipfile.ZipFile(target, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for file in sorted(self.out.rglob("*")):
                if not file.is_file() or file.is_symlink():
                    continue
                relative = file.relative_to(self.out)
                if any(part in {"scans", "witnesses", "context", "upload", "__pycache__"} for part in relative.parts):
                    continue
                if file.suffix.lower() == ".zip" or file.name.endswith(".tmp"):
                    continue
                if relative.as_posix() == "progress.log":
                    archive.writestr(relative.as_posix(), file.read_text(encoding="utf-8") + entry + "\n")
                else:
                    archive.write(file, relative.as_posix())
        self._append_log(entry)
        return {"checkpoint": str(target), "number": number, "bytes": target.stat().st_size, "uploaded": False}

    def status(self):
        done, audited, outstanding = [], [], []
        for row in self.pages:
            key = f"{row['cote']}:{int(row['our_scan']):03d}"
            status = self.load_record(row["cote"], row["our_scan"]).get("status", {})
            (done if status.get("done") else outstanding).append(key)
            if status.get("audited"):
                audited.append(key)
        return {"total": len(self.pages), "done": len(done), "audited": len(audited), "outstanding": outstanding,
                "frozen": (self.out / "freeze.sha256").exists()}


def strip_comments(text):
    result = []
    for line in text.splitlines():
        for i, char in enumerate(line):
            if char == "%":
                count, j = 0, i - 1
                while j >= 0 and line[j] == "\\":
                    count += 1
                    j -= 1
                if count % 2 == 0:
                    line = line[:i]
                    break
        result.append(line)
    return "\n".join(result)


def check_latex(text):
    """Conservative structural check. It does not compile or validate readings."""
    text = strip_comments(text)
    problems = []
    stack = []
    tokens = re.finditer(r"\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\[\[\]()]|\\.|[{}]|\$\$|\$", text)
    math = None
    environments = []
    for match in tokens:
        token = match.group(0)
        line = text.count("\n", 0, match.start()) + 1
        if match.group(1):
            environments.append((match.group(1), line))
        elif match.group(2):
            name = match.group(2)
            if not environments:
                problems.append(f"line {line}: unmatched end {name}")
            else:
                old, start = environments.pop()
                if old != name:
                    problems.append(f"line {line}: end {name} closes {old} from line {start}")
        elif token == "{":
            stack.append(line)
        elif token == "}":
            if stack:
                stack.pop()
            else:
                problems.append(f"line {line}: unmatched closing brace")
        elif token in ("$", "$$", "\\[", "\\("):
            if math is None:
                math = (token, line)
            elif token == math[0] and token in ("$", "$$"):
                math = None
            elif token in ("$", "$$") and math[0] in ("\\[", "\\("):
                # Inline math can occur in text inside a display; track separately.
                # A full TeX parser would be needed to reject genuine nested math.
                pass
            else:
                problems.append(f"line {line}: math delimiter {token} inside {math[0]}")
        elif token in ("\\]", "\\)"):
            opener = "\\[" if token == "\\]" else "\\("
            if math and math[0] == opener:
                math = None
            else:
                problems.append(f"line {line}: unmatched math close {token}")
    problems.extend(f"line {line}: unclosed brace" for line in stack)
    problems.extend(f"line {line}: unclosed environment {name}" for name, line in environments)
    if math:
        problems.append(f"line {math[1]}: unclosed math {math[0]}")
    # Count inline dollars even inside display-text groups.
    single_dollars = [m for m in re.finditer(r"(?<!\\)\$(?!\$)", text) if m.start() == 0 or text[m.start()-1] != "$"]
    if len(single_dollars) % 2:
        problems.append("Odd number of unescaped single-dollar delimiters")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--page-map", type=Path, default=DEFAULT_MAP)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("status", "render", "freeze", "checkpoint"):
        sub.add_parser(command)
    check = sub.add_parser("check")
    check.add_argument("--all", action="store_true", help="Also report absent/uncompleted page files")
    verify = sub.add_parser("verify")
    verify.add_argument("--log", action="store_true")
    for command in ("mark-done", "mark-audited"):
        page = sub.add_parser(command)
        page.add_argument("cote")
        page.add_argument("scan", type=int)
    args = parser.parse_args()
    project = Project(args.out, args.page_map)
    if args.command == "mark-done":
        result = project.mark_done(args.cote, args.scan)
    elif args.command == "mark-audited":
        result = project.mark_audited(args.cote, args.scan)
    elif args.command == "check":
        result = project.syntax_check(completed_only=not args.all)
    elif args.command == "verify":
        result = project.verify_freeze(log=args.log)
    else:
        result = getattr(project, args.command)()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.command == "check" and any(result.values()):
        raise SystemExit(1)
    if args.command == "verify" and not result["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
