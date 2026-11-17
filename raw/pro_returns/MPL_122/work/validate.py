#!/usr/bin/env python3
"""Read-only mechanical checks for the MPL_122 transcription package.

This is not a handwriting, completeness, or mathematical correctness check.
Run from any directory:
    python MPL_122/work/validate.py --partial
    python MPL_122/work/validate.py

The package root defaults to this script's parent's parent. All input files
are read as UTF-8. The script never modifies the package or reads the scans
or context material.

Recommended progress-log hash lines:
    sha256 <64 hexadecimal digits> pages/MPL_122_122_scan003.tex
    sha256 <64 hexadecimal digits> MPL_122_transcription.tex
Conventional sha256sum lines and `SHA-256 filename: digest` also work.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path


EXPECTED = tuple(range(3, 19)) + tuple(range(20, 36))
PAGE_RE = re.compile(r"MPL_122_122_scan(\d{3})\.tex\Z")
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
FORBIDDEN = re.compile(
    r"\\(?:documentclass|usepackage|RequirePackage|includegraphics|input|include|"
    r"newcommand|renewcommand|providecommand|DeclareRobustCommand|newenvironment|"
    r"renewenvironment|def|gdef|edef|xdef|let|newcount|newlength|newdimen)\b"
    r"|\\(?:begin|end)\s*\{document\}"
)
HEX = r"[0-9a-fA-F]{64}"
HASH_PATTERNS = (
    re.compile(rf"^\s*(?:sha256|sha-256)\s+({HEX})\s+\*?(.+?)\s*$", re.I),
    re.compile(rf"^\s*({HEX})\s+\*?(.+?)\s*$"),
    re.compile(rf"^\s*(?:sha256|sha-256)\s+(.+?)\s*[:=]\s*({HEX})\s*$", re.I),
)


class Report:
    def __init__(self, partial: bool):
        self.partial = partial
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def incomplete(self, message: str) -> None:
        (self.warn if self.partial else self.error)(message)

    def emit(self) -> int:
        for label, messages in (("INFO", self.info), ("WARNING", self.warnings), ("ERROR", self.errors)):
            for message in messages:
                print(f"{label}: {message}")
        mode = "partial" if self.partial else "final"
        print(f"{mode.upper()} VALIDATION: {len(self.errors)} error(s), {len(self.warnings)} warning(s).")
        print("Mechanical validation cannot establish fidelity to handwriting or inventory completeness.")
        return 1 if self.errors else 0


def read_text(path: Path, report: Report) -> str | None:
    if not path.is_file():
        report.incomplete(f"Missing {path.name}.")
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.error(f"Cannot read {path}: {exc}")
        return None


def strip_comments(text: str) -> str:
    """Strip TeX comments while retaining line numbers and escaped percent signs."""
    result = []
    for line in text.splitlines(keepends=True):
        cut = None
        for index, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        result.append(line if cut is None else line[:cut] + ("\n" if line.endswith("\n") else ""))
    return "".join(result)


def escaped(text: str, index: int) -> bool:
    cursor = index - 1
    count = 0
    while cursor >= 0 and text[cursor] == "\\":
        count += 1
        cursor -= 1
    return bool(count % 2)


def latex_checks(text: str, name: str, report: Report) -> None:
    clean = strip_comments(text)
    stack: list[int] = []
    line_number = 1
    for index, char in enumerate(clean):
        if char == "\n":
            line_number += 1
        elif char == "{" and not escaped(clean, index):
            stack.append(line_number)
        elif char == "}" and not escaped(clean, index):
            if stack:
                stack.pop()
            else:
                report.error(f"{name}:{line_number}: unmatched closing brace.")
    for opening_line in stack:
        report.error(f"{name}:{opening_line}: unmatched opening brace.")

    environments: list[tuple[str, int]] = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
        action, environment = match.groups()
        line = clean.count("\n", 0, match.start()) + 1
        if action == "begin":
            environments.append((environment, line))
        elif not environments:
            report.error(f"{name}:{line}: end of {environment} without a begin.")
        else:
            expected, opening_line = environments.pop()
            if expected != environment:
                report.error(
                    f"{name}:{line}: ends {environment}, but {expected} opened on line {opening_line}."
                )
    for environment, opening_line in environments:
        report.error(f"{name}:{opening_line}: unclosed {environment} environment.")

    for match in FORBIDDEN.finditer(clean):
        line = clean.count("\n", 0, match.start()) + 1
        report.error(f"{name}:{line}: forbidden fragment/preamble command {match.group(0)}.")
    # A row break such as \\[2pt] is not the display opener \[.
    math_delimiters = Counter(
        match.group(0)
        for match in re.finditer(r"\\[\[\]\(\)]", clean)
        if not escaped(clean, match.start())
    )
    for opening, closing in ((r"\[", r"\]"), (r"\(", r"\)")):
        if math_delimiters[opening] != math_delimiters[closing]:
            report.error(f"{name}: unequal counts of {opening} and {closing}.")
    if re.search(r"\\illegible\s*\{\s*[^\d\s}][^}]*\}", clean):
        report.error(f"{name}: illegible argument is not a numeric word estimate.")


def page_checks(root: Path, report: Report) -> tuple[dict[int, str], list[Path]]:
    pages: dict[int, str] = {}
    paths: list[Path] = []
    page_dir = root / "pages"
    if not page_dir.is_dir():
        report.incomplete("Missing pages/ directory.")
        return pages, paths
    for path in sorted(page_dir.glob("*.tex")):
        match = PAGE_RE.fullmatch(path.name)
        if not match:
            report.error(f"Unexpected page filename {path.name}.")
            continue
        scan = int(match.group(1))
        if scan not in EXPECTED:
            report.error(f"Unexpected scan {scan:03d} in {path.name}.")
            continue
        text = read_text(path, report)
        if text is None:
            continue
        pages[scan] = text
        paths.append(path)
        clean = strip_comments(text)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if markers != [str(scan)] and [int(x) for x in markers] != [scan]:
            report.error(f"{path.name}: expected exactly one scanpage{{{scan}}}, found {markers}.")
        cote = re.findall(r"\\cotefile\s*\{([^{}]*)\}", clean)
        if cote and (scan != EXPECTED[0] or cote != ["122"]):
            report.error(f"{path.name}: cotefile must be 122 and appear only before the first page.")
        latex_checks(text, path.name, report)
    found = tuple(sorted(pages))
    if report.partial:
        if found != EXPECTED[:len(found)]:
            report.error(f"Written pages are not a sequential prefix of the expected scans: {found}.")
    elif found != EXPECTED:
        missing = sorted(set(EXPECTED) - set(found))
        report.error("Missing page files: " + ", ".join(f"{scan:03d}" for scan in missing) + ".")
    report.info.append(f"Read {len(pages)} of {len(EXPECTED)} expected page fragments.")
    return pages, paths


def combined_checks(root: Path, pages: dict[int, str], report: Report) -> Path | None:
    path = root / "MPL_122_transcription.tex"
    text = read_text(path, report)
    if text is None:
        return None
    clean = strip_comments(text)
    if not re.match(r"\s*\\cotefile\{122\}\s*\\scanpage\{0*3\}", clean):
        report.error("Combined transcription must begin with cotefile{122} then scanpage{3}.")
    markers = tuple(int(x) for x in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean))
    expected = tuple(sorted(pages)) if report.partial else EXPECTED
    if markers != expected:
        report.error(f"Combined scan order {markers} differs from expected order {expected}.")
    if len(re.findall(r"\\cotefile\s*\{", clean)) != 1:
        report.error("Combined transcription must contain exactly one cotefile macro.")
    concatenated = "".join(pages[scan] for scan in sorted(pages))
    if text != concatenated:
        report.error(
            "Combined transcription is not the exact concatenation of page files in scan order. "
            "Put cotefile{122} in the first page file and preserve its bytes when concatenating."
        )
    latex_checks(text, path.name, report)
    return path


def inventory_checks(root: Path, pages: dict[int, str], report: Report) -> None:
    path = root / "MPL_122_inventory.csv"
    if not path.is_file():
        report.incomplete("Missing MPL_122_inventory.csv.")
        return
    seen_elements: set[tuple[int, str]] = set()
    counts: Counter[int] = Counter()
    order: list[int] = []
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != COLUMNS:
                report.error(f"Inventory columns must be exactly {COLUMNS}; found {reader.fieldnames}.")
                return
            for line, row in enumerate(reader, 2):
                label = f"MPL_122_inventory.csv:{line}"
                if None in row or any(value is None for value in row.values()):
                    report.error(f"{label}: malformed CSV row.")
                    continue
                if row["cote"].strip() != "122":
                    report.error(f"{label}: cote is not 122.")
                try:
                    scan = int(row["scan"])
                except ValueError:
                    report.error(f"{label}: scan is not an integer.")
                    continue
                if scan not in EXPECTED:
                    report.error(f"{label}: unexpected scan {scan}.")
                if scan not in pages:
                    report.error(f"{label}: inventory names scan {scan:03d} without a page file.")
                if row["sheet_kind"] not in SHEET_KINDS:
                    report.error(f"{label}: unknown sheet_kind {row['sheet_kind']!r}.")
                if row["kind"] not in KINDS:
                    report.error(f"{label}: unknown element kind {row['kind']!r}.")
                if row["transcribed"] != "yes":
                    report.error(f"{label}: transcribed must be exactly 'yes'.")
                element = row["element"].strip()
                if not element:
                    report.error(f"{label}: empty element identifier.")
                if (scan, element) in seen_elements:
                    report.error(f"{label}: duplicate element {element!r} for scan {scan:03d}.")
                seen_elements.add((scan, element))
                counts[scan] += 1
                order.append(scan)
    except (OSError, UnicodeError, csv.Error) as exc:
        report.error(f"Cannot parse inventory: {exc}")
        return
    if order != sorted(order):
        report.error("Inventory scan groups are not in scan order.")
    required = set(pages) if report.partial else set(EXPECTED)
    missing = sorted(required - set(counts))
    if missing:
        report.error("Inventory has no elements for scan(s): " + ", ".join(f"{x:03d}" for x in missing) + ".")
    report.info.append(f"Inventory contains {sum(counts.values())} rows across {len(counts)} scans.")


def normalize_hash_path(raw: str, root: Path) -> str:
    raw = raw.strip().strip('"').replace("\\", "/")
    path = Path(raw)
    if path.is_absolute():
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            return raw
    while raw.startswith("./"):
        raw = raw[2:]
    if raw.startswith(root.name + "/"):
        raw = raw[len(root.name) + 1:]
    return raw


def progress_checks(root: Path, pages: dict[int, str], paths: list[Path], combined: Path | None, report: Report) -> None:
    text = read_text(root / "progress.log", report)
    if text is None:
        return
    lines = text.splitlines()
    if not lines or not re.search(r"\d{4}-\d{2}-\d{2}.*(?:UTC|Z|\+00:00)", lines[0]):
        report.error("progress.log first line must be the starting UTC time.")
    done: dict[int, int] = {}
    audits: dict[int, int] = {}
    freezes: list[int] = []
    contexts: list[int] = []
    hashes: dict[str, list[tuple[int, str]]] = {}
    unchanged: list[int] = []
    for line_no, line in enumerate(lines, 1):
        match = re.search(r"^122\s+scan\s+(\d+)\s+done\s+(.+)$", line)
        if match:
            scan = int(match.group(1))
            if scan in done:
                report.warn(f"progress.log:{line_no}: duplicate done record for scan {scan:03d}.")
            done[scan] = line_no
            if not re.search(r"(?:UTC|Z|\+00:00)", match.group(2)):
                report.error(f"progress.log:{line_no}: done timestamp lacks UTC designation.")
        match = re.search(r"^(?:122\s+)?scan\s+(\d+)\s+audited\s+(.+)$", line)
        if match:
            scan = int(match.group(1))
            audits[scan] = line_no
            if not re.search(r"(?:UTC|Z|\+00:00)", match.group(2)):
                report.error(f"progress.log:{line_no}: audit timestamp lacks UTC designation.")
        if line.startswith("transcription frozen "):
            freezes.append(line_no)
        if line.startswith("context opened "):
            contexts.append(line_no)
        if re.search(r"(?:hash|sha-?256).*unchanged|unchanged.*(?:hash|sha-?256)", line, re.I):
            unchanged.append(line_no)
        for index, pattern in enumerate(HASH_PATTERNS):
            match = pattern.match(line)
            if not match:
                continue
            if index == 2:
                filename, digest = match.groups()
            else:
                digest, filename = match.groups()
            filename = normalize_hash_path(filename, root)
            hashes.setdefault(filename, []).append((line_no, digest.lower()))
            break
    for label, records in (("done", done), ("audited", audits)):
        unexpected = sorted(set(records) - set(EXPECTED))
        if unexpected:
            report.error(f"Progress log has unexpected {label} scans: {unexpected}.")
    for scan in pages:
        if scan not in done:
            report.error(f"No done record for written scan {scan:03d}.")
    done_order = sorted(done, key=done.get)
    if done_order != sorted(done_order):
        report.error("Page done records are not in scan order.")
    if not report.partial:
        for scan in EXPECTED:
            if scan not in audits:
                report.error(f"Missing second-reading audit record for scan {scan:03d}.")
    for scan, audit_line in audits.items():
        if scan not in done or audit_line <= done[scan]:
            report.error(f"Audit of scan {scan:03d} must follow its done record.")
    if not freezes:
        report.incomplete("Missing transcription frozen record.")
    elif len(freezes) > 1:
        report.warn("Multiple transcription frozen records; checking the first freeze against context opening.")
    if contexts and not freezes:
        report.error("Context was opened without a recorded transcription freeze.")
    if freezes:
        freeze = freezes[0]
        for scan in EXPECTED:
            if scan not in audits or audits[scan] >= freeze:
                report.error(f"Scan {scan:03d} lacks an audit before the first freeze.")
        if contexts and contexts[0] <= freeze:
            report.error("Context opening does not follow transcription freeze.")
    if not contexts:
        report.incomplete("Missing context opened record.")
    if not unchanged:
        report.incomplete("Missing final record stating frozen hashes are unchanged.")
    elif contexts and unchanged[-1] <= contexts[0]:
        report.error("Final unchanged-hash record must follow context opening.")

    hash_required = bool(freezes) or not report.partial
    if hash_required:
        expected_paths = paths + ([combined] if combined else [])
        for path in expected_paths:
            filename = path.relative_to(root).as_posix()
            records = hashes.get(filename, [])
            if not records:
                report.error(f"No frozen SHA-256 recorded for {filename}.")
                continue
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            for hash_line, digest in records:
                if digest != actual:
                    report.error(f"progress.log:{hash_line}: SHA-256 mismatch for {filename}.")
            if contexts and records[0][0] >= contexts[0]:
                report.error(f"First SHA-256 of {filename} was not recorded before context opening.")
        report.info.append(f"Checked frozen SHA-256 values for {len(expected_paths)} current files.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--partial", action="store_true", help="Allow a sequential prefix and unfinished final-stage records.")
    args = parser.parse_args()
    root = args.root.resolve()
    report = Report(args.partial)
    if not root.is_dir():
        report.error(f"Package root does not exist: {root}")
        return report.emit()
    pages, paths = page_checks(root, report)
    combined = combined_checks(root, pages, report)
    inventory_checks(root, pages, report)
    for filename in ("MPL_122_doubts.md", "MPL_122_notes.md"):
        path = root / filename
        if not path.is_file():
            report.incomplete(f"Missing {filename}.")
        elif not args.partial and path.stat().st_size == 0:
            report.error(f"{filename} is empty.")
    progress_checks(root, pages, paths, combined, report)
    return report.emit()


if __name__ == "__main__":
    sys.exit(main())
