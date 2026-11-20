#!/usr/bin/env python3
"""Mechanical validation only: no OCR, reading decisions, or TeX compilation.

Run during work:
  python scripts/validate_records.py
Run on completed work, optionally including its final ZIP:
  python scripts/validate_records.py --final --archive ../SP68_C13_136+141.zip

The validator opens records and generated tables only to check schemas, metadata,
counts and consistency. It never prints manuscript/witness text. Page .tex files
are read as bytes solely for combination and SHA-256 checks. Source MARKS.tsv is
projected immediately to its id/cote/scan metadata columns. Source image headers
may be opened solely to obtain dimensions for crop bounds; no pixels are loaded.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

PREFIX = "SP68_C13_136+141"
ORDER = [("136", s) for s in (364, 365, 366, 367, 368, 370, 371, 372, 373, 374, 375, 376)] + [("141", s) for s in range(2, 15)]
KEYS = [f"{c}_scan{s:03d}" for c, s in ORDER]
NO_H = {"141_scan003", "141_scan005", "141_scan007"}
CONFIDENCES = {"high", "medium", "low"}
DECISIONS = {"first", "alternative", "other", "undecided"}
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
CHANGE_KINDS = {"misread word", "misread symbol or index", "omission", "text not on the page", "deletion state", "deletion state (struck given live or live given struck)", "insertion or placement", "abbreviation expanded or spelling modernised", r"readable ink left as \ill{}", "drawing or diagram", "other"}
FEEDBACK_CATEGORIES = ["Symbols and indices", "Words", "Omissions", "Drawings and diagrams", "Readable ink left as illegible", "Insertions put in wrong place", "Struck text", "Abbreviations expanded/spelling modernised", "Text not on page", "Other"]
KIND_TO_FEEDBACK = {
    "misread symbol or index": "Symbols and indices",
    "misread word": "Words",
    "omission": "Omissions",
    "drawing or diagram": "Drawings and diagrams",
    r"readable ink left as \ill{}": "Readable ink left as illegible",
    "insertion or placement": "Insertions put in wrong place",
    "deletion state": "Struck text",
    "deletion state (struck given live or live given struck)": "Struck text",
    "abbreviation expanded or spelling modernised": "Abbreviations expanded/spelling modernised",
    "text not on the page": "Text not on page",
    "other": "Other",
}
CHECK_TYPES = {"targeted proof check", "independent re-proof", "computation or formal certificate", "used and rechecked in this run", "carried as background without fault found"}
HEADERS = {
    "decisions.tsv": ["id", "cote", "scan", "decision", "reading", "what the ink shows", "crop", "confidence"],
    PREFIX + "_collation.tsv": ["folder", "their_page", "our_scan", "line", "their_reading", "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H", "confidence"],
    PREFIX + "_inventory.csv": ["scan", "sheet_kind", "hand", "element", "kind", "position", "first_words_or_objects", "transcribed"],
    "CHECK_EVENTS.tsv": ["statement_id", "date", "who", "type", "outcome"],
}
DOCS = [PREFIX + suffix for suffix in ("_changes.md", "_doubts.md", "_inventory.csv", "_collation.tsv", "_notes.md", "_sheet_feedback.md", "_hand_log.md", "_transcription.tex")] + ["decisions.tsv", "CHECK_EVENTS.tsv", "progress.log"]
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".tif", ".tiff", ".bmp", ".svg", ".pdf"}
BOX_RE = re.compile(r"(?P<key>(?:136|141)_scan\d{3})\s*\(\s*(?P<x0>\d+)\s*,\s*(?P<y0>\d+)\s*,\s*(?P<x1>\d+)\s*,\s*(?P<y1>\d+)\s*\)")
LOG_CROP_RE = re.compile(r"^crop (?P<key>(?:136|141)_scan\d{3}) (?P<tag>\S+) (?P<box>\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)) rotation (?P<rotation>\S+) width (?P<width>\d+)$", re.M)
STAMP = "%Y-%m-%d %H:%M:%S UTC"


class Validator:
    def __init__(self, root: Path, final: bool, marks_path: Path | None, scans: Path | None):
        self.root, self.final = root, final
        self.marks_path, self.scans = marks_path, scans
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.stats: dict[str, int] = {}
        self.dimensions: dict[str, tuple[int, int] | None] = {}

    def require(self, condition: bool, message: str):
        if not condition:
            self.errors.append(message)

    def stamp(self, value: str, label: str):
        try:
            return datetime.strptime(value, STAMP).replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            self.errors.append(label + ": malformed UTC timestamp")
            return None

    def table(self, name: str):
        path = self.root / name
        if not path.is_file():
            self.errors.append("Missing file: " + name)
            return []
        with path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter="," if name.endswith(".csv") else "\t")
            self.require(reader.fieldnames == HEADERS[name], name + ": incorrect column header/order")
            rows = list(reader)
        self.require(all(None not in row and all(v is not None for v in row.values()) for row in rows), name + ": malformed row width")
        return rows

    def markdown_table(self, text: str, header: str):
        """Extract one generated table without displaying manuscript cells."""
        lines = text.splitlines()
        if header not in lines:
            return []
        start = lines.index(header)
        end = start + 1
        while end < len(lines) and lines[end].startswith("| "):
            end += 1
        return lines[start:end]

    def dims(self, key: str):
        if key not in self.dimensions:
            path = self.scans / (key + ".jpg") if self.scans else None
            if path and path.is_file():
                from PIL import Image
                # Image.open reads headers lazily; no load/convert/getdata call.
                with Image.open(path) as im:
                    self.dimensions[key] = im.size
            else:
                self.dimensions[key] = None
        return self.dimensions[key]

    def crop(self, value: str, label: str):
        if value == "page":
            return []
        found = list(BOX_RE.finditer(value or ""))
        self.require(bool(found), label + ": crop must be page or source scan plus pixel box")
        out = []
        for m in found:
            k = m["key"]
            box = tuple(int(m[x]) for x in ("x0", "y0", "x1", "y1"))
            self.require(k in KEYS, label + ": unknown source scan")
            self.require(box[0] < box[2] and box[1] < box[3], label + ": empty/reversed crop")
            dims = self.dims(k)
            if dims:
                self.require(0 <= box[0] < box[2] <= dims[0] and 0 <= box[1] < box[3] <= dims[1], label + ": crop outside original image")
            out.append((k, box))
        return out

    def run(self):
        paths = sorted((self.root / "records").glob("*.json"))
        actual_keys = {p.stem for p in paths}
        self.require(actual_keys <= set(KEYS), "Unexpected record filename(s)")
        complete_keys = [k for k in KEYS if k in actual_keys]
        self.require(complete_keys == KEYS[:len(complete_keys)], "Completed pages are not a prefix of the supplied reading order")
        if self.final:
            self.require(complete_keys == KEYS, "Final output must contain all 25 pages")
        records = []
        for k in complete_keys:
            try:
                r = json.loads((self.root / "records" / (k + ".json")).read_text(encoding="utf-8"))
            except (ValueError, OSError):
                self.errors.append(k + ": record cannot be parsed")
                continue
            records.append(r)
            self.require(r.get("key") == k, k + ": record key differs from filename")
            c, s = ORDER[KEYS.index(k)]
            self.require(str(r.get("cote")) == c and str(r.get("scan")) == str(s), k + ": record cote/scan mismatch")
            for field in ("changes", "decisions", "inventory", "notes", "hand", "notation", "doubts", "abbreviations", "checks", "audit"):
                self.require(isinstance(r.get(field), list), k + ": missing/non-list " + field)
            self.require(isinstance(r.get("extra_decisions", []), list), k + ": non-list extra_decisions")
            self.require((self.root / "pages" / (k + ".tex")).is_file(), k + ": page file missing")
            self.stamp(r.get("done_utc", ""), k + " done")
            if self.final:
                self.require(bool(r.get("audit")) and bool(r.get("audited_utc")), k + ": second reading not logged")
                if r.get("audited_utc"):
                    self.stamp(r["audited_utc"], k + " audited")
        if len(records) != len(complete_keys) or any(any(not isinstance(r.get(f), list) for f in ("changes", "decisions", "inventory", "notes", "hand", "notation", "doubts", "abbreviations", "checks", "audit")) for r in records):
            return

        for name in DOCS:
            self.require((self.root / name).is_file(), "Missing deliverable: " + name)
        if self.final:
            for name in ("legibility.txt", "sheet_feedback.txt"):
                path = self.root / "scripts" / name
                self.require(path.is_file() and bool(path.read_text().strip()), "Missing/empty final synthesis hook: scripts/" + name)
        tables = {name: self.table(name) for name in HEADERS}
        decisions = tables["decisions.tsv"]
        inventory = tables[PREFIX + "_inventory.csv"]
        collation = tables[PREFIX + "_collation.tsv"]
        checks = tables["CHECK_EVENTS.tsv"]
        raw_decisions = [d for r in records for d in r["decisions"]]
        extra_decisions = [d for r in records for d in r.get("extra_decisions", [])]
        raw_inventory = [d for r in records for d in r["inventory"]]
        raw_checks = [d for r in records for d in r["checks"]]
        for name, generated, raw in [("decisions.tsv", decisions, raw_decisions), (PREFIX + "_inventory.csv", inventory, raw_inventory), ("CHECK_EVENTS.tsv", checks, raw_checks)]:
            normalized = [{f: str(row.get(f, "")) for f in HEADERS[name]} for row in raw]
            self.require(generated == normalized, name + ": generated rows differ from records/order")

        expected_marks = []
        if self.marks_path and self.marks_path.is_file():
            with self.marks_path.open(encoding="utf-8", newline="") as f:
                # Other cells are discarded; no source readings enter output.
                expected_marks = [{f: row[f] for f in ("id", "cote", "scan")} for row in csv.DictReader(f, delimiter="\t")]
            selected = [m for m in expected_marks if f"{m['cote']}_scan{int(m['scan']):03d}" in complete_keys]
            got = [(d.get("id"), str(d.get("cote")), int(d.get("scan", -1))) for d in decisions]
            wanted = [(d["id"], d["cote"], int(d["scan"])) for d in selected]
            self.require(got == wanted, "decisions.tsv: MARKS identities/order not exactly covered for completed pages")
            self.stats["source_marks"] = len(expected_marks)
        else:
            self.warnings.append("Source MARKS.tsv unavailable: coverage check skipped; use --marks for a relocated deliverable")
        ids = [d.get("id") for d in decisions]
        self.require(len(ids) == len(set(ids)), "decisions.tsv: duplicate mark id")
        recorded_crops = set()
        for i, d in enumerate(decisions, 1):
            label = "Decision row " + str(i)
            self.require(d.get("decision") in DECISIONS, label + ": invalid decision")
            self.require(d.get("confidence") in CONFIDENCES, label + ": invalid confidence")
            for field in ("reading", "what the ink shows"):
                self.require(bool(d.get(field)), label + ": empty " + field)
            recorded_crops.update(self.crop(d.get("crop", ""), label))
        extra_ids = [d.get("id") for d in extra_decisions]
        self.require(len(extra_ids) == len(set(extra_ids)), "Additional decisions contain duplicate identifiers")
        self.require(not set(extra_ids).intersection(ids), "Additional decisions reuse supplied MARKS identifiers")
        for i, d in enumerate(extra_decisions, 1):
            label = "Additional decision row " + str(i)
            self.require(bool(d.get("id")) and str(d.get("id", "")).startswith("X-"), label + ": expected an X- identifier")
            self.require(d.get("decision") in DECISIONS, label + ": invalid decision")
            self.require(d.get("confidence") in CONFIDENCES, label + ": invalid confidence")
            for field in ("place", "reading", "what the ink shows"):
                self.require(bool(d.get(field)), label + ": empty " + field)
            recorded_crops.update(self.crop(d.get("crop", ""), label))
        for r in records:
            k = r["key"]
            for d in r.get("extra_decisions", []):
                self.require(str(d.get("cote")) == str(r["cote"]) and int(d.get("scan", -1)) == int(r["scan"]), k + ": additional decision belongs to another page")
            self.require(bool(r["inventory"]), k + ": empty inventory")
            numbers = []
            for i, d in enumerate(r["inventory"], 1):
                label = k + " inventory element " + str(i)
                numbers.append(d.get("element"))
                self.require(d.get("scan") == k, label + ": scan mismatch")
                self.require(d.get("sheet_kind") in SHEET_KINDS, label + ": invalid sheet kind")
                self.require(d.get("kind") in ELEMENT_KINDS, label + ": invalid element kind")
                self.require(d.get("transcribed") == "yes", label + ": not marked transcribed")
                for field in ("position", "hand", "first_words_or_objects"):
                    self.require(bool(d.get(field)), label + ": missing " + field)
            self.require(numbers == list(range(1, len(numbers)+1)), k + ": element numbers not consecutive")
            self.require(bool(r["notes"]), k + ": no reading note")
            for i, x in enumerate(r["changes"], 1):
                label = k + " change " + str(i)
                self.require(x.get("confidence") in CONFIDENCES, label + ": invalid confidence")
                self.require(str(x.get("kind", "")).replace("`", "") in CHANGE_KINDS, label + ": unrecognized collation kind")
                self.require(type(x.get("against_c")) is bool and type(x.get("against_h")) is bool, label + ": nonboolean witness flags")
                self.require(x.get("against_c") or x.get("against_h"), label + ": differs from neither witness")
                if k in NO_H:
                    self.require(not x.get("against_h"), label + ": H absent on this page; against_h must be false")
                for field in ("place", "scan_shows", "final"):
                    self.require(bool(x.get(field)), label + ": missing " + field)
                recorded_crops.update(self.crop(x.get("crop", ""), label))
        expected_collation = []
        for r in records:
            for x in r["changes"]:
                if x["against_h"]:
                    expected_collation.append(dict(folder=r["cote"], their_page=str(r["scan"]-1), our_scan=f"{r['scan']:03d}", line=x["place"], their_reading=x["H"], codex_reading=x["C"], final_reading=x["final"], scan_shows=x["scan_shows"]+"; "+x["crop"], kind=x["kind"], marked_in_H=x["marked_in_H"], confidence=x["confidence"]))
        self.require(collation == expected_collation, "Collation rows differ from H-flagged records/order")
        self.require(all(row.get("marked_in_H") in {"yes", "no"} for row in collation), "Collation has invalid marked_in_H value")
        for i, check in enumerate(checks, 1):
            label = "Check event " + str(i)
            self.require(all(check.get(f) for f in HEADERS["CHECK_EVENTS.tsv"]), label + ": empty field")
            typ = check.get("type", "")
            self.require(typ in CHECK_TYPES or typ.startswith("refuted"), label + ": unrecognized event type")
            self.stamp(check.get("date", ""), label)

        progress_path = self.root / "progress.log"
        progress = progress_path.read_text(encoding="utf-8") if progress_path.is_file() else ""
        self.stamp(progress.splitlines()[0] if progress else "", "Progress first line")
        logged = re.findall(r"^scan (\d{3}) done (.+? UTC) cote (\d+)$", progress, re.M)
        logged_keys = [f"{c}_scan{s}" for s, _, c in logged]
        self.require(logged_keys == complete_keys, "Progress done entries must appear exactly once, in page order")
        for m in LOG_CROP_RE.finditer(progress):
            pairs = self.crop(m["key"] + " " + m["box"], "Progress crop " + m["tag"])
            for pair in pairs:
                # A crop may have just been made for the still-open next page.
                # Require a decision reference once that page is committed.
                if m["key"] in complete_keys or self.final:
                    self.require(pair in recorded_crops, "A logged crop has no matching changes/decisions reference: " + m["key"] + " " + m["tag"])
        crop_log_entries = list(LOG_CROP_RE.finditer(progress))
        self.require(len(crop_log_entries) == sum(line.startswith("crop ") for line in progress.splitlines()), "Malformed crop entry in progress log")
        changes_path = self.root / (PREFIX+"_changes.md")
        if changes_path.is_file():
            changes_report = changes_path.read_text(encoding="utf-8")
            summary_header = "| scan | against C | against H | places | high | medium | low |"
            summary_rows = [summary_header, "| --- | --- | --- | --- | --- | --- | --- |"]
            totals = [0] * 6
            for r in records:
                cc = r["changes"]
                confidence_counts = Counter(x["confidence"] for x in cc)
                values = [sum(x["against_c"] for x in cc), sum(x["against_h"] for x in cc), len(cc), confidence_counts["high"], confidence_counts["medium"], confidence_counts["low"]]
                summary_rows.append("| " + r["key"] + " | " + " | ".join(map(str, values)) + " |")
                totals = [a+b for a,b in zip(totals, values)]
            summary_rows.append("| TOTAL | " + " | ".join(map(str, totals)) + " |")
            self.require(self.markdown_table(changes_report, summary_header) == summary_rows, "Changes-log summary counts differ from recorded places/confidences")
            heading = "## Complete crop register\n"
            self.require(heading in changes_report, "Changes log lacks complete crop register")
            register = changes_report.partition(heading)[2]
            actual_rows = [line for line in register.splitlines() if line.startswith("| ")]
            expected_rows = ["| scan | crop | original pixel box | rotation (degrees) | output width (pixels) |", "| --- | --- | --- | --- | --- |"]
            expected_rows += [f"| {m['key']} | {m['tag']} | {m['box']} | {m['rotation']} | {m['width']} |" for m in crop_log_entries]
            self.require(actual_rows == expected_rows, "Changes-log crop register differs from progress metadata/order; rebuild before validation/package")
        feedback_path = self.root / (PREFIX+"_sheet_feedback.md")
        if feedback_path.is_file():
            feedback = feedback_path.read_text(encoding="utf-8")
            all_categories = Counter()
            c_categories = Counter()
            for r in records:
                for x in r["changes"]:
                    category = KIND_TO_FEEDBACK.get(x["kind"].replace("`", ""), "Other")
                    all_categories[category] += 1
                    if x["against_c"]:
                        c_categories[category] += 1
            header = "| error-sheet category | against C | all witness differences |"
            expected_rows = [header, "| --- | --- | --- |"] + [f"| {k} | {c_categories[k]} | {all_categories[k]} |" for k in FEEDBACK_CATEGORIES]
            self.require(self.markdown_table(feedback, header) == expected_rows, "Feedback must contain all ten categories in order with matching C/all-place counts")
        if self.final:
            audited = re.findall(r"^scan (\d{3}) audited (.+? UTC)(?: cote (\d+))?$", progress, re.M)
            # Current workflow includes cote; an unqualified scan can be resolved
            # against supplied order (scan numbers are unique in this batch).
            audit_keys = [f"{c or next(c2 for c2,s2 in ORDER if s2==int(s))}_scan{s}" for s, _, c in audited]
            self.require(audit_keys == KEYS, "Progress audit entries must appear exactly once, in page order")
            done_times = [self.stamp(t, "Progress completion") for _,t,_ in logged]
            audit_times = [self.stamp(t, "Progress audit") for _,t,_ in audited]
            if done_times and audit_times and all(done_times+audit_times):
                self.require(min(audit_times) >= max(done_times), "Second reading started before all first readings were completed")
            self.require("transcription frozen " in progress, "No transcription-frozen log entry")
            self.require("frozen hashes unchanged " in progress, "No final unchanged-hashes log entry")

        # Byte/metadata-only checks do not interpret transcription content.
        page_files = [self.root / "pages" / (k+".tex") for k in complete_keys]
        combined = self.root / (PREFIX+"_transcription.tex")
        if all(p.is_file() for p in page_files) and combined.is_file():
            chunks = []
            previous_cote = None
            expected_cotes = []
            for r, path in zip(records, page_files):
                fragment = path.read_bytes().rstrip()
                cote = str(r["cote"]).encode("ascii")
                if cote != previous_cote:
                    expected_cotes.append(cote)
                    before_scan = fragment.split(br"\scanpage", 1)[0]
                    marker = re.compile(rb"(?m)^[ \t]*\\cotefile\s*\{\s*"+re.escape(cote)+rb"\s*\}")
                    if not marker.search(before_scan):
                        fragment = b"\\cotefile{"+cote+b"}\n"+fragment
                chunks.append(fragment)
                previous_cote = cote
            expected_bytes = b"\n\n".join(chunks)+b"\n"
            actual_bytes = combined.read_bytes()
            self.require(actual_bytes == expected_bytes, "Combined transcription differs from ordered pages plus required cote boundaries")
            actual_cotes = re.findall(rb"(?m)^[ \t]*\\cotefile\s*\{\s*(\d+)\s*\}", actual_bytes)
            self.require(actual_cotes == expected_cotes, "Combined transcription has missing, duplicate or misplaced cote markers")
            actual_scanpages = re.findall(rb"(?m)^[ \t]*\\scanpage\s*\{\s*(\d+)\s*\}", actual_bytes)
            expected_scanpages = [str(r["scan"]).encode("ascii") for r in records]
            self.require([int(x) for x in actual_scanpages] == [int(x) for x in expected_scanpages], "Combined transcription has missing/duplicate/out-of-order scanpage markers")
            self.require(not re.search(rb"(?m)^[ \t]*\\(?:documentclass|usepackage)\b|^[ \t]*\\begin\s*\{document\}", actual_bytes), "Combined transcription must be a fragment without a preamble/document wrapper")
        hashes_path = self.root / "scripts" / "frozen_hashes.json"
        if hashes_path.is_file():
            frozen = json.loads(hashes_path.read_text())
            expected_paths = {"pages/"+k+".tex" for k in KEYS} | {PREFIX+"_transcription.tex"}
            self.require(set(frozen) == expected_paths, "Frozen manifest must cover exactly 25 pages plus combined transcription")
            for rel, value in frozen.items():
                p = self.root / rel
                self.require(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == value, "Frozen hash mismatch: " + rel)
        elif self.final:
            self.errors.append("Missing frozen hash manifest")
        self.stats.update(pages=len(records), changes=sum(len(r["changes"]) for r in records), against_C=sum(x["against_c"] for r in records for x in r["changes"]), against_H=len(collation), decisions=len(decisions), additional_decisions=len(extra_decisions), registered_crops=len(crop_log_entries), inventory_elements=len(inventory), check_events=len(checks), remaining_doubts=sum(len(r["doubts"]) for r in records))
        self.stats.update({"confidence_"+k: v for k,v in Counter(x["confidence"] for r in records for x in r["changes"]).items()})

    def archive(self, path: Path):
        if not path.is_file():
            self.errors.append("Archive not found: " + str(path))
            return
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            self.require(len(names) == len(set(names)), "Archive contains duplicate member names")
            for name in names:
                p = PurePosixPath(name)
                self.require(not p.is_absolute() and ".." not in p.parts, "Archive has unsafe member path")
                self.require(p.suffix.lower() not in IMAGE_SUFFIXES | {".zip", ".pyc"}, "Archive contains image, nested ZIP or bytecode: " + name)
                self.require(not any(x in p.parts for x in ("source", "upload", "hua", "halves", "crops", "__pycache__")) and not any(x.endswith("_scans") or x.endswith("_texts") for x in p.parts), "Archive contains attached input/work-image directory: " + name)
                self.require(p.name not in {"MARKS.tsv", "PREAMBLE.tex"} and not p.name.startswith("PROMPT("), "Archive contains an attached input: " + name)
                local = self.root / name
                if not name.endswith("/"):
                    self.require(local.is_file() and z.read(name) == local.read_bytes(), "Archive member differs from current deliverable: " + name)
            for required in DOCS + ["pages/"+k+".tex" for k in KEYS if (self.root/"pages"/(k+".tex")).is_file()]:
                self.require(required in names, "Archive missing required member: " + required)
            bad = z.testzip()
            self.require(bad is None, "Archive CRC check failed")
            self.stats["archive_members"] = len(names)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--marks", type=Path)
    parser.add_argument("--scans", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    workspace = root.parents[1]
    marks = args.marks or workspace / "source" / (PREFIX+"_texts") / "MARKS.tsv"
    scans = args.scans or workspace / "source" / (PREFIX+"_scans")
    v = Validator(root, args.final, marks, scans)
    try:
        v.run()
        if args.archive:
            v.archive(args.archive.resolve())
    except (KeyError, ValueError, TypeError, OSError, zipfile.BadZipFile) as exc:
        # Do not print data-bearing exception messages.
        v.errors.append("Validation could not complete: " + type(exc).__name__)
    print(json.dumps({"status": "PASS" if not v.errors else "FAIL", "mode": "final" if args.final else "in-progress", "counts": v.stats, "errors": v.errors, "warnings": v.warnings}, ensure_ascii=False, indent=2))
    return 1 if v.errors else 0


if __name__ == "__main__":
    sys.exit(main())
