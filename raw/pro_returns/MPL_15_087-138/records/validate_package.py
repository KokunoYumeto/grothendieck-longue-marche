#!/usr/bin/env python3
"""Mechanical checks only; this script cannot certify a manuscript reading.

Run from anywhere:
  python records/validate_package.py /absolute/path/to/MPL_15_087-138_work

Use --partial while work is in progress. No files are written or changed.
The final exit status is 1 for structural errors and 0 otherwise. Warnings,
including possible placeholder text, always require human consideration.

Suggested log forms (in addition to the user's required event lines):
  sha256 <64-hex-digest> pages/MPL_15_087-138_15_scan087.tex
  sha256 <64-hex-digest> MPL_15_087-138_transcription.tex
  frozen hashes unchanged YYYY-MM-DD HH:MM:SS UTC
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "MPL_15_087-138"
SCANS = tuple(n for n in range(87, 139) if n not in (116, 127, 134, 136))
HEADER = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
STATE_MACROS = ("cotefile", "scanpage", "mspage", "deleted", "inserted", "margin", "uline", "uuline", "diagram", "figure", "unsure", "illegible")
CONTROL_RE = re.compile(r"\\([A-Za-z]+|.)", re.S)
STAMP = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
PAGE_RE = re.compile(rf"{PREFIX}_15_scan(\d{{3}})\.tex\Z")
HEX_RE = re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])")
PLACEHOLDERS = (
    ("bracketed omission", re.compile(r"\[(?:\s*\.\s*\.\s*\.|\s*…\s*)\]")),
    ("TODO/FIXME/TBD marker", re.compile(r"\b(?:TODO|FIXME|TBD|PLACEHOLDER)\b", re.I)),
    ("possible replacement description", re.compile(r"\b(?:not transcribed|transcription pending|and so on)\b", re.I)),
    ("ellipsis macro or characters", re.compile(r"\\(?:ldots|cdots|dots)\b|…|\.\.\.")),
    ("etc. (may be genuine manuscript text)", re.compile(r"\betc\.", re.I)),
)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def without_comments(text: str) -> str:
    """Drop unescaped TeX comments, preserving line count and escaped percent."""
    output = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for pos, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            k = pos - 1
            while k >= 0 and line[k] == "\\":
                backslashes += 1
                k -= 1
            if backslashes % 2 == 0:
                cut = pos
                break
        output.append(line[:cut] + ("\n" if cut < len(line) and line.endswith("\n") else ""))
    return "".join(output)


def check_tex(text: str, label: str, report: Report) -> None:
    text = without_comments(text)
    for token in CONTROL_RE.finditer(text):
        if token[1] not in STATE_MACROS:
            continue
        suffix = text[token.end():].lstrip()
        if not suffix.startswith("{"):
            lineno = text.count("\n", 0, token.start()) + 1
            report.error(f"{label}:{lineno}: state macro \\{token[1]} lacks its required braced argument")
    stack: list[int] = []
    line = 1
    slash_count = 0
    for char in text:
        escaped = slash_count % 2 == 1
        if char == "{" and not escaped:
            stack.append(line)
        elif char == "}" and not escaped:
            if stack:
                stack.pop()
            else:
                report.error(f"{label}:{line}: unmatched closing brace")
        if char == "\n":
            line += 1
        slash_count = slash_count + 1 if char == "\\" else 0
    for opened in stack:
        report.error(f"{label}:{opened}: unclosed opening brace")
    envs: list[tuple[str, int]] = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        kind, name = match.groups()
        lineno = text.count("\n", 0, match.start()) + 1
        if kind == "begin":
            envs.append((name, lineno))
        elif not envs or envs[-1][0] != name:
            report.error(f"{label}:{lineno}: unmatched or out-of-order end of {name}")
        else:
            envs.pop()
    for name, lineno in envs:
        report.error(f"{label}:{lineno}: unclosed environment {name}")
    for diagram in re.finditer(r"\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}", text, re.S):
        for candidate in re.finditer(r"(?<!\\)\\[ \t]*\n", diagram.group(1)):
            lineno = text.count("\n", 0, diagram.start(1) + candidate.start()) + 1
            report.warn(f"{label}:{lineno}: single backslash at line end inside tikz-cd; check intended row separator")
    for description, pattern in PLACEHOLDERS:
        for match in pattern.finditer(text):
            lineno = text.count("\n", 0, match.start()) + 1
            report.warn(f"{label}:{lineno}: {description}: {match.group(0)!r}")
    if re.search(r"\\(?:documentclass|usepackage)\b|\\begin\s*\{document\}", text):
        report.error(f"{label}: transcription must be a fragment without a preamble")
    if re.search(r"\\includegraphics\b", text):
        report.error(f"{label}: image inclusion found; user requires transcribed content")


def print_macro_report(root: Path, page_texts: dict[int, str], report: Report) -> None:
    """Count syntax and page-level register presence; make no reading judgment."""
    totals: Counter[str] = Counter()
    per_page: dict[int, Counter[str]] = {}
    for scan, text in sorted(page_texts.items()):
        clean = without_comments(text)
        counts = Counter(token[1] for token in CONTROL_RE.finditer(clean) if token[1] in STATE_MACROS)
        totals.update(counts)
        per_page[scan] = counts
    doubt_rows: Counter[int] = Counter()
    doubt_path = root / f"{PREFIX}_doubts.md"
    if doubt_path.is_file():
        section = False
        for line in doubt_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                section = line.strip() in {"# Doubt register", "# Current doubt register"}
            if not section or not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            if len(cells) >= 2 and cells[1].isdigit():
                scan = int(cells[1])
                page_match = PAGE_RE.fullmatch(cells[0])
                if cells[0] == "15" or (page_match and int(page_match[1]) == scan):
                    doubt_rows[scan] += 1
    print("State-macro counts: " + "; ".join(f"{name}={totals[name]}" for name in STATE_MACROS))
    print("Scan | unsure | illegible | exported doubt-register rows")
    for scan, counts in per_page.items():
        print(f"{scan:03d} | {counts['unsure']} | {counts['illegible']} | {doubt_rows[scan]}")
        if counts["unsure"] + counts["illegible"] and not doubt_rows[scan]:
            report.warn(f"Scan {scan:03d}: doubt macros present but no scan row found in the exported doubt register")
    print("Register-row presence does not establish coverage of each individual doubt; rows may group several readings.")


def read_utf8(path: Path, report: Report) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.error(f"Cannot read {path.name}: {exc}")
        return None


def normalized_boundaries(text: str) -> str:
    """Allow separator whitespace, without normalizing any page's content."""
    return re.sub(r"\s*(?=\\scanpage\s*\{)", "\n", text.strip())


def check_inventory(root: Path, present: set[int], partial: bool, report: Report) -> int:
    path = root / f"{PREFIX}_inventory.csv"
    if not path.is_file():
        report.error(f"Missing {path.name}")
        return 0
    counts: Counter[int] = Counter()
    seen: set[tuple[int, str]] = set()
    kinds: dict[int, set[str]] = {}
    try:
        with path.open(encoding="utf-8-sig", newline="") as source:
            reader = csv.DictReader(source)
            if reader.fieldnames != HEADER:
                report.error(f"{path.name}: header differs from the required exact header")
            for lineno, row in enumerate(reader, 2):
                label = f"{path.name}:{lineno}"
                if None in row or any(row.get(key) is None for key in HEADER):
                    report.error(f"{label}: malformed CSV row")
                    continue
                try:
                    scan = int(row["scan"])
                except ValueError:
                    report.error(f"{label}: invalid scan number {row['scan']!r}")
                    continue
                counts[scan] += 1
                if row["cote"] != "15":
                    report.error(f"{label}: cote must be 15")
                if scan not in SCANS:
                    report.error(f"{label}: scan {scan} is outside the required set")
                if row["sheet_kind"] not in SHEET_KINDS:
                    report.error(f"{label}: unknown sheet_kind {row['sheet_kind']!r}")
                if row["kind"] not in ELEMENT_KINDS:
                    report.error(f"{label}: unknown kind {row['kind']!r}")
                if row["transcribed"] != "yes":
                    report.error(f"{label}: transcribed is not exactly yes")
                for column in ("element", "position", "first_words_or_objects"):
                    if not row[column].strip():
                        report.error(f"{label}: empty {column}")
                key = (scan, row["element"])
                if key in seen:
                    report.warn(f"{label}: duplicate element identifier {key}")
                seen.add(key)
                kinds.setdefault(scan, set()).add(row["sheet_kind"])
    except (OSError, UnicodeError, csv.Error) as exc:
        report.error(f"Cannot parse {path.name}: {exc}")
    required = present if partial else set(SCANS)
    for scan in sorted(required - counts.keys()):
        report.error(f"{path.name}: no inventory rows for scan {scan:03d}")
    for scan in sorted(counts.keys() - present):
        report.error(f"{path.name}: rows for scan {scan:03d} have no corresponding page file")
    for scan, values in kinds.items():
        if len(values) != 1:
            report.error(f"{path.name}: scan {scan:03d} has multiple sheet_kind values: {sorted(values)}")
    return sum(counts.values())


def check_log(root: Path, page_paths: dict[int, Path], partial: bool, report: Report) -> None:
    path = root / "progress.log"
    if not path.is_file():
        report.error("Missing progress.log")
        return
    text = read_utf8(path, report)
    if text is None:
        return
    lines = text.splitlines()
    if not lines or not re.fullmatch(STAMP, lines[0].strip()):
        report.error("progress.log: first line must be the start timestamp in UTC")
    done: dict[int, int] = {}
    audited: dict[int, int] = {}
    frozen: list[int] = []
    opened: list[int] = []
    verified: list[int] = []
    for index, line in enumerate(lines):
        stamp = re.search(STAMP, line)
        if stamp:
            try:
                datetime.strptime(stamp.group(), "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
            except ValueError:
                report.error(f"progress.log:{index+1}: invalid UTC timestamp")
        m = re.fullmatch(rf"15 scan (\d{{3}}) done ({STAMP})", line.strip())
        if m:
            done.setdefault(int(m[1]), index)
        m = re.fullmatch(rf"scan (\d{{3}}) audited ({STAMP})", line.strip())
        if m:
            audited.setdefault(int(m[1]), index)
        if re.fullmatch(rf"transcription frozen {STAMP}", line.strip()):
            frozen.append(index)
        if re.fullmatch(rf"context opened {STAMP}", line.strip()):
            opened.append(index)
        if re.search(r"hashes?.*(?:unchanged|verified)|(?:unchanged|verified).*hashes?", line, re.I):
            verified.append(index)
    required = set(page_paths) if partial else set(SCANS)
    for scan in sorted(required - done.keys()):
        report.error(f"progress.log: missing exact done event for scan {scan:03d}")
    for scan in sorted((done.keys() | audited.keys()) - set(SCANS)):
        report.error(f"progress.log: event for excluded or unexpected scan {scan:03d}")
    completed_order = [scan for scan, _ in sorted(done.items(), key=lambda item: item[1])]
    if completed_order != sorted(completed_order):
        report.error("progress.log: first done events are not in ascending scan order")
    if not partial or frozen:
        for scan in sorted(set(SCANS) - audited.keys()):
            report.error(f"progress.log: missing exact audit event for scan {scan:03d}")
        if audited and done and min(audited.values()) < max(done.values()):
            report.error("progress.log: final audit began before every page had a done event")
        if not frozen:
            report.error("progress.log: missing exact transcription frozen event")
        elif audited and frozen[-1] <= max(audited.values()):
            report.error("progress.log: freeze event precedes completion of all audits")
        if not opened and not partial:
            report.error("progress.log: missing exact context opened event")
        if opened and (not frozen or opened[0] <= frozen[-1]):
            report.error("progress.log: context opened before the final freeze event")
        if not verified and not partial:
            report.error("progress.log: missing final unchanged/verified hash statement")
        elif verified and opened and verified[-1] <= opened[-1] and not partial:
            report.error("progress.log: final hash verification precedes context opening")
        targets = list(page_paths.values()) + [root / f"{PREFIX}_transcription.tex"]
        frozen_records = lines[:opened[0]] if opened else lines
        for target in targets:
            candidates = [HEX_RE.findall(line) for line in frozen_records if target.name in line]
            recorded = [digest.lower() for values in candidates for digest in values]
            if not recorded:
                report.error(f"progress.log: no SHA-256 recorded before context opening for {target.name}")
            elif target.is_file() and any(digest != hashlib.sha256(target.read_bytes()).hexdigest() for digest in recorded):
                report.error(f"progress.log: a pre-context SHA-256 does not match {target.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--partial", action="store_true", help="validate completed pages without requiring final artifacts")
    parser.add_argument("--macro-report", action="store_true", help="list authorized state-macro counts and page-level exported doubt-register coverage")
    args = parser.parse_args()
    root = args.root.resolve()
    report = Report()
    page_paths: dict[int, Path] = {}
    page_texts: dict[int, str] = {}
    for path in sorted((root / "pages").glob("*.tex")):
        match = PAGE_RE.fullmatch(path.name)
        if not match:
            report.error(f"Unexpected page filename: {path.name}")
            continue
        scan = int(match[1])
        page_paths[scan] = path
        if scan not in SCANS:
            report.error(f"Unexpected or excluded scan file: {path.name}")
        text = read_utf8(path, report)
        if text is None:
            continue
        page_texts[scan] = text
        content = without_comments(text)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", content)
        if markers != [str(scan)] and markers != [f"{scan:03d}"]:
            report.error(f"{path.name}: expected exactly one matching scanpage marker, got {markers}")
        check_tex(text, path.name, report)
    if not args.partial:
        for scan in sorted(set(SCANS) - page_paths.keys()):
            report.error(f"Missing page file for scan {scan:03d}")
    combined_path = root / f"{PREFIX}_transcription.tex"
    if combined_path.is_file():
        combined = read_utf8(combined_path, report)
        if combined is not None:
            content = without_comments(combined)
            markers = [int(n) for n in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", content)]
            required_order = sorted(page_paths) if args.partial else list(SCANS)
            if markers != required_order:
                report.error("Combined transcription: scanpage markers do not match required page order")
            if not re.match(r"\s*\\cotefile\s*\{15\}\s*\\scanpage\s*\{0?87\}", content):
                report.error("Combined transcription must start with cotefile{15} and scanpage{87}")
            if len(re.findall(r"\\cotefile\s*\{", content)) != 1:
                report.error("Combined transcription: expected exactly one cotefile marker")
            joined = "\n".join(page_texts[n].strip() for n in sorted(page_texts))
            variants = [joined, "\\cotefile{15}\n" + joined]
            if normalized_boundaries(combined) not in [normalized_boundaries(v) for v in variants]:
                report.error("Combined transcription differs from ordered page concatenation beyond separator whitespace")
    elif not args.partial:
        report.error(f"Missing {combined_path.name}")
    for suffix in ("doubts.md", "notes.md"):
        path = root / f"{PREFIX}_{suffix}"
        if not args.partial and (not path.is_file() or path.stat().st_size == 0):
            report.error(f"Missing or empty {path.name}")
    inventory_rows = check_inventory(root, set(page_paths), args.partial, report)
    check_log(root, page_paths, args.partial, report)
    if args.macro_report:
        print_macro_report(root, page_texts, report)
    print(f"Mechanical check: {len(page_paths)}/{len(SCANS)} page files; {inventory_rows} inventory rows")
    print("This check does not establish reading accuracy, image inspection, or inventory completeness.")
    for message in report.errors:
        print("ERROR:", message)
    for message in report.warnings:
        print("REVIEW:", message)
    print(f"Result: {len(report.errors)} error(s), {len(report.warnings)} review item(s)")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
