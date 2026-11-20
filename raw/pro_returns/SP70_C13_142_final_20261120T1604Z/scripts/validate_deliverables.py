#!/usr/bin/env python3
"""Mechanical validation only; no image access, OCR, TeX compilation, or reading decisions.

Usage:
  python3 validate_deliverables.py /absolute/path/to/final-directory
  python3 validate_deliverables.py /absolute/path/to/SP70_C13_142.zip
  python3 validate_deliverables.py --interim /absolute/path/to/work
  python3 validate_deliverables.py BUNDLE --marks /path/to/SP70_C13_142_texts/MARKS.tsv

The source MARKS.tsv is consulted only for its id, cote, and scan fields.
If --marks is omitted, common source locations adjacent to the bundle or this
script are searched by exact path. The source register is not bundled here.
This program checks packaging and record structure, not palaeographic correctness.
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

SCANS = (26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51)
PREFIX = "SP70_C13_142"
PAGE_NAMES = tuple(f"pages/142_scan{scan:03d}.tex" for scan in SCANS)
REQUIRED = (*PAGE_NAMES, f"{PREFIX}_transcription.tex", f"{PREFIX}_changes.md", f"{PREFIX}_collation.tsv",
            "decisions.tsv", f"{PREFIX}_doubts.md", f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md",
            "CHECK_EVENTS.tsv", "progress.log", f"{PREFIX}_sheet_feedback.md", f"{PREFIX}_hand_log.md")
COLLATION_HEADER = ["folder", "their_page", "our_scan", "line", "their_reading", "codex_reading", "final_reading",
                    "scan_shows", "kind", "marked_in_H", "confidence"]
DECISIONS_HEADER = ["id", "cote", "scan", "decision", "reading", "what the ink shows", "crop", "confidence"]
INVENTORY_HEADER = ["scan", "sheet_kind", "hand", "element", "kind", "position", "first_words_or_objects", "transcribed"]
COLLATION_KINDS = {"misread word", "misread symbol or index", "omission", "text not on the page",
                   "deletion state", "deletion state (struck given live or live given struck)",
                   "insertion or placement", "abbreviation expanded or spelling modernised",
                   r"readable ink left as \ill{}", r"readable ink left as `\ill{}`", "drawing or diagram", "other"}
INVENTORY_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}
CONFIDENCES = {"high", "medium", "low"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff", ".bmp", ".svg", ".heic", ".avif"}
ARCHIVE_EXTENSIONS = {".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".rar"}


def scan_number(value: str) -> int | None:
    matches = re.findall(r"\d+", value.strip())
    return int(matches[-1]) if matches else None


def logical_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def tex_structure_issues(text: str) -> list[str]:
    """Conservative lexical checks, not a TeX parser or compilation."""
    issues: list[str] = []
    braces: list[int] = []
    math: list[tuple[str, int]] = []
    # TikZ pictures execute node text in their own text context even when the
    # picture itself sits inside display math. Keep outer delimiters suspended.
    math_suspensions: list[list[tuple[str, int]]] = []
    environments: list[tuple[str, int]] = []
    left_right: list[int] = []
    i, line = 0, 1
    while i < len(text):
        char = text[i]
        if char == "\n":
            line += 1
            i += 1
            continue
        if char == "%":
            end = text.find("\n", i)
            i = len(text) if end < 0 else end
            continue
        if char == "\\":
            match = re.match(r"\\([A-Za-z]+|.)", text[i:], flags=re.S)
            if not match:
                issues.append(f"line {line}: trailing backslash")
                break
            command = match.group(1)
            i += len(match.group())
            if command in ("[", "("):
                if math:
                    issues.append(f"line {line}: nested math opener \\{command}")
                math.append((command, line))
            elif command in ("]", ")"):
                expected = {"]": "[", ")": "("}[command]
                if math and math[-1][0] == expected:
                    math.pop()
                else:
                    issues.append(f"line {line}: mismatched math closer \\{command}")
            elif command in ("begin", "end"):
                match_env = re.match(r"\s*\{([^}]+)\}", text[i:])
                if match_env:
                    environment = match_env.group(1)
                    if command == "begin":
                        environments.append((environment, line))
                        if environment == "tikzpicture":
                            math_suspensions.append(math)
                            math = []
                    elif environments and environments[-1][0] == environment:
                        environments.pop()
                        if environment == "tikzpicture":
                            if math:
                                issues.append(f"line {line}: unclosed math inside TikZ picture {math}")
                            math = math_suspensions.pop() if math_suspensions else []
                    else:
                        issues.append(f"line {line}: mismatched environment end {environment}")
            elif command == "left":
                left_right.append(line)
            elif command == "right":
                if left_right:
                    left_right.pop()
                else:
                    issues.append(f"line {line}: unmatched \\right")
            continue
        if char == "{":
            braces.append(line)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                issues.append(f"line {line}: unmatched closing brace")
        elif char == "$":
            token = "$$" if text[i:i + 2] == "$$" else "$"
            if math and math[-1][0] == token:
                math.pop()
            else:
                if math:
                    issues.append(f"line {line}: mixed/nested math delimiter {token}")
                math.append((token, line))
            i += len(token)
            continue
        i += 1
    if braces:
        issues.append(f"unclosed braces opened on lines {braces}")
    if math:
        issues.append(f"unclosed math delimiters {math}")
    if environments:
        issues.append(f"unclosed environments {environments}")
    if left_right:
        issues.append(f"unmatched \\left on lines {left_right}")
    return issues


class Bundle:
    def __init__(self, path: Path):
        self.path = path
        self.zf = zipfile.ZipFile(path) if path.is_file() else None
        if self.zf:
            self.names = [item.filename for item in self.zf.infolist() if not item.is_dir()]
        elif path.is_dir():
            self.names = [str(p.relative_to(path)).replace("\\", "/") for p in path.rglob("*") if p.is_file()]
        else:
            raise ValueError(f"Not a directory or ZIP: {path}")

    def read(self, name: str) -> bytes:
        return self.zf.read(name) if self.zf else (self.path / name).read_bytes()

    def text(self, name: str) -> str:
        return self.read(name).decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def validate(bundle: Bundle, marks_path: Path, interim: bool = False) -> tuple[dict, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    names = set(bundle.names)
    progress = bundle.text("progress.log") if "progress.log" in names else ""
    done_scans = tuple(int(x) for x in re.findall(r"(?m)^scan (\d+) done .*cote 142\s*$", progress))
    target_scans = done_scans if interim else SCANS
    target_pages = tuple(f"pages/142_scan{scan:03d}.tex" for scan in target_scans)
    required = tuple(name for name in REQUIRED if not name.startswith("pages/")) + target_pages
    if len(done_scans) != len(set(done_scans)):
        errors.append("progress.log: duplicate done entries.")
    if done_scans != SCANS[:len(done_scans)]:
        errors.append("progress.log: done scans are not a prefix of the required reading order.")
    if len(names) != len(bundle.names):
        errors.append("ZIP contains duplicate filenames.")
    for name in bundle.names:
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name:
            errors.append(f"Unsafe archive member: {name}")
        if path.suffix.casefold() in IMAGE_EXTENSIONS:
            errors.append(f"Image present in deliverable: {name}")
        if path.suffix.casefold() in ARCHIVE_EXTENSIONS:
            errors.append(f"Nested archive/checkpoint present: {name}")
        if any(part in {f"{PREFIX}_scans", f"{PREFIX}_texts", "upload", "source"} for part in path.parts):
            errors.append(f"Attached source material present: {name}")
        if "checkpoint_" in path.name.casefold():
            errors.append(f"Checkpoint material nested in bundle: {name}")
    missing = sorted(set(required) - names)
    errors.extend(f"Missing required file: {name}" for name in missing)
    actual_pages = {name for name in names if name.startswith("pages/") and name.endswith(".tex")}
    if actual_pages != set(target_pages):
        errors.append("Page-file set differs from the completed scans." if interim else "Page-file set differs from the exact 24 expected scans.")
    for name in sorted(set(required) & names):
        if not bundle.read(name).strip():
            errors.append(f"Empty required file: {name}")
    for name in sorted(actual_pages):
        errors.extend(f"{name}: {issue}" for issue in tex_structure_issues(bundle.text(name)))

    def table(name: str, delimiter: str, expected_header: list[str] | None = None) -> tuple[list[str], list[dict]]:
        if name not in names:
            return [], []
        try:
            reader = csv.DictReader(io.StringIO(bundle.text(name)), delimiter=delimiter)
            header = reader.fieldnames or []
            rows = list(reader)
            if expected_header is not None and header != expected_header:
                errors.append(f"{name}: header differs; expected {expected_header!r}, got {header!r}.")
            if len(set(header)) != len(header):
                errors.append(f"{name}: duplicate column names.")
            for line, row in enumerate(rows, 2):
                if None in row or any(value is None for value in row.values()):
                    errors.append(f"{name}:{line}: row has wrong number of columns.")
            return header, rows
        except (UnicodeError, csv.Error) as exc:
            errors.append(f"{name}: unreadable table ({exc}).")
            return [], []

    with marks_path.open(encoding="utf-8-sig", newline="") as handle:
        marks_reader = csv.DictReader(handle, delimiter="\t")
        all_marks = [{key: row[key] for key in ("id", "cote", "scan")} for row in marks_reader]
        marks = [row for row in all_marks if scan_number(row["scan"]) in target_scans] if interim else all_marks
    _, decisions = table("decisions.tsv", "\t", DECISIONS_HEADER)
    if [row.get("id") for row in decisions] != [row["id"] for row in marks]:
        errors.append("decisions.tsv: IDs/count/order do not match MARKS.tsv.")
    if len({row.get("id") for row in decisions}) != len(decisions):
        errors.append("decisions.tsv: duplicate IDs.")
    for line, (decision, mark) in enumerate(zip(decisions, marks), 2):
        if decision.get("cote", "").strip() != mark["cote"].strip() or scan_number(decision.get("scan", "")) != scan_number(mark["scan"]):
            errors.append(f"decisions.tsv:{line}: cote/scan mismatch against source mark.")
        if decision.get("decision") not in {"first", "alternative", "other", "undecided"}:
            errors.append(f"decisions.tsv:{line}: invalid decision value.")
        if decision.get("confidence") not in CONFIDENCES:
            errors.append(f"decisions.tsv:{line}: invalid confidence.")
        for column in ("reading", "what the ink shows", "crop"):
            if not decision.get(column, "").strip():
                errors.append(f"decisions.tsv:{line}: empty {column!r}.")

    _, collation = table(f"{PREFIX}_collation.tsv", "\t", COLLATION_HEADER)
    for line, row in enumerate(collation, 2):
        scan = scan_number(row.get("our_scan", ""))
        if scan not in target_scans:
            errors.append(f"collation:{line}: unexpected scan.")
        if scan is not None and scan_number(row.get("their_page", "")) != scan - 1:
            errors.append(f"collation:{line}: H page is not our scan minus one.")
        if row.get("kind") not in COLLATION_KINDS:
            errors.append(f"collation:{line}: invalid kind {row.get('kind')!r}.")
        if row.get("confidence") not in CONFIDENCES:
            errors.append(f"collation:{line}: invalid confidence.")
        if not row.get("scan_shows", "").strip():
            errors.append(f"collation:{line}: empty scan evidence.")
    if "CHANGES.tsv" in names:
        _, changes = table("CHANGES.tsv", "\t")
        if len({row.get("id") for row in changes}) != len(changes):
            errors.append("CHANGES.tsv: duplicate IDs.")
        for line, row in enumerate(changes, 2):
            for field in ("against_C", "against_H"):
                if row.get(field) not in {"yes", "no"}:
                    errors.append(f"CHANGES.tsv:{line}: invalid {field} flag.")
            if row.get("kind") not in COLLATION_KINDS:
                errors.append(f"CHANGES.tsv:{line}: invalid kind.")
            if row.get("confidence") not in CONFIDENCES:
                errors.append(f"CHANGES.tsv:{line}: invalid confidence.")
            if row.get("error_category") not in {str(n) for n in range(1, 11)}:
                errors.append(f"CHANGES.tsv:{line}: invalid error category.")
        c_keys = ("scan", "place", "C", "H", "final", "kind", "confidence")
        h_keys = ("our_scan", "line", "codex_reading", "their_reading", "final_reading", "kind", "confidence")
        c_rows = Counter(tuple(row.get(k) for k in c_keys) for row in changes if row.get("against_H") == "yes")
        h_rows = Counter(tuple(row.get(k) for k in h_keys) for row in collation)
        if c_rows != h_rows:
            errors.append(f"Changes/collation mismatch: {sum((c_rows-h_rows).values())} changes absent from collation; {sum((h_rows-c_rows).values())} collation rows absent from changes.")

    _, inventory = table(f"{PREFIX}_inventory.csv", ",", INVENTORY_HEADER)
    inventory_scans: set[int] = set()
    for line, row in enumerate(inventory, 2):
        scan = scan_number(row.get("scan", ""))
        if scan not in target_scans:
            errors.append(f"inventory:{line}: unexpected scan.")
        elif scan is not None:
            inventory_scans.add(scan)
        if row.get("transcribed") != "yes":
            errors.append(f"inventory:{line}: transcribed is not 'yes'.")
        if row.get("kind") not in INVENTORY_KINDS:
            errors.append(f"inventory:{line}: invalid element kind.")
        if row.get("sheet_kind") not in SHEET_KINDS:
            errors.append(f"inventory:{line}: invalid sheet kind.")
        for column in ("hand", "element", "position", "first_words_or_objects"):
            if not row.get(column, "").strip():
                errors.append(f"inventory:{line}: empty {column!r}.")
    if inventory_scans != set(target_scans):
        errors.append("Inventory does not cover the expected completed scans." if interim else "Inventory does not cover all 24 expected scans.")
    inventory_keys = [(row.get("scan"), row.get("element")) for row in inventory]
    if len(set(inventory_keys)) != len(inventory_keys):
        errors.append("Inventory contains duplicate (scan, element) keys.")

    events_header, events = table("CHECK_EVENTS.tsv", "\t")
    logical = {logical_header(h) for h in events_header}
    for alternatives, label in (({"statementid", "statement"}, "statement id"), ({"date", "datetime", "utctime"}, "date"),
                                ({"type", "eventtype", "checktype"}, "type"), ({"outcome", "result"}, "outcome")):
        if not logical.intersection(alternatives):
            errors.append(f"CHECK_EVENTS.tsv: missing logical column {label!r}.")
    if not any(h.startswith("who") for h in logical) and not {"model", "effort", "run"}.issubset(logical):
        errors.append("CHECK_EVENTS.tsv: missing who/model-effort-run identification.")

    combined_name = f"{PREFIX}_transcription.tex"
    if combined_name in names and set(target_pages).issubset(names):
        combined = bundle.text(combined_name)
        cursor = 0
        for name in target_pages:
            page = bundle.text(name).strip()
            position = combined.find(page, cursor)
            if position < 0:
                errors.append(f"Combined transcription: exact page content absent/out of order: {name}")
                break
            gap = combined[cursor:position]
            if any(line.strip() and not line.lstrip().startswith("%") for line in gap.splitlines()):
                errors.append(f"Combined transcription: non-comment text before {name}.")
            cursor = position + len(page)
        else:
            if any(line.strip() and not line.lstrip().startswith("%") for line in combined[cursor:].splitlines()):
                errors.append("Combined transcription: unexpected non-comment trailing text.")
        if re.search(r"\\(?:documentclass|begin\{document\}|end\{document\})", combined):
            errors.append("Combined transcription includes document-level wrapper instead of fragment.")

    if "progress.log" in names:
        first_line = progress.splitlines()[0] if progress.splitlines() else ""
        if not re.search(r"\d{4}-\d{2}-\d{2}.*(?:UTC|Z)", first_line):
            errors.append("progress.log: first line does not identify a UTC start timestamp.")
        for scan in target_scans:
            if not re.search(rf"(?m)^scan {scan:03d} done .*cote 142\s*$", progress):
                errors.append(f"progress.log: missing done entry for scan {scan:03d}.")
            if not interim and not re.search(rf"(?m)^scan {scan:03d} audited .+", progress):
                errors.append(f"progress.log: missing audited entry for scan {scan:03d}.")
        if not interim and "transcription frozen " not in progress:
            errors.append("progress.log: missing transcription frozen event.")
        hash_matches = 0
        for name in (() if interim else (*PAGE_NAMES, combined_name)):
            if name in names:
                digest = hashlib.sha256(bundle.read(name)).hexdigest()
                matching_lines = [line for line in progress.splitlines() if name in line and digest in line]
                if matching_lines:
                    hash_matches += 1
                else:
                    errors.append(f"progress.log: current SHA-256 not recorded for {name}.")
        if not interim and not re.search(r"(?i)(hash(?:es)?[^\n]*(?:unchanged|verified)|(?:unchanged|verified)[^\n]*hash(?:es)?)", progress):
            warnings.append("progress.log: no recognizable final hash-unchanged statement; inspect wording.")
    else:
        hash_matches = 0

    summary = {"status": "PASS" if not errors else "FAIL", "bundle": str(bundle.path), "files": len(names),
               "mode": "interim" if interim else "final", "expected_pages": len(target_scans), "actual_page_files": len(actual_pages), "source_marks": len(marks),
               "decision_rows": len(decisions), "collation_rows": len(collation), "inventory_rows": len(inventory),
               "check_event_rows": len(events), "matching_recorded_sha256": hash_matches,
               "scope": "Mechanical packaging/schema/concatenation/hash checks only; no manuscript reading validation."}
    if interim:
        summary["expected_pending"] = {"unread_scans": [f"{scan:03d}" for scan in SCANS if scan not in target_scans],
                                       "second_reading": "pending unless individually logged",
                                       "transcription_freeze_and_hashes": "pending"}
    return summary, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path, help="Final deliverable directory or ZIP")
    parser.add_argument("--marks", type=Path, help="Original source MARKS.tsv; otherwise locate in common adjacent source directories")
    parser.add_argument("--interim", action="store_true", help="Validate only scans logged done; audit/freeze/full coverage are expected pending")
    args = parser.parse_args()
    try:
        marks_path = args.marks
        if marks_path is None:
            script_parent = Path(__file__).resolve().parent
            roots = [Path.cwd(), args.bundle.resolve().parent, script_parent, script_parent.parent, script_parent.parent.parent]
            candidates = [root / relative for root in roots for relative in
                          (Path("source") / f"{PREFIX}_texts" / "MARKS.tsv", Path(f"{PREFIX}_texts") / "MARKS.tsv", Path("MARKS.tsv"))]
            marks_path = next((candidate for candidate in candidates if candidate.is_file()), None)
            if marks_path is None:
                raise ValueError("Original MARKS.tsv not found. Supply --marks /path/to/SP70_C13_142_texts/MARKS.tsv.")
        bundle = Bundle(args.bundle)
        summary, errors, warnings = validate(bundle, marks_path, args.interim)
    except (OSError, ValueError, KeyError, UnicodeError, zipfile.BadZipFile) as exc:
        print(json.dumps({"status": "FAIL", "fatal": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps({**summary, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
