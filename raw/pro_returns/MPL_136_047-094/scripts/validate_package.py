#!/usr/bin/env python3
"""Read-only structural validation for MPL_136_047-094.

Usage:
    python scripts/validate_package.py [PACKAGE_DIRECTORY] [--require-frozen]

The default directory is the parent of this script's directory. This script
does not read scan images or the context archive, perform OCR, or assess the
accuracy or completeness of manuscript readings. It never modifies files.

Recommended progress.log hash record (other common sha256sum formats work):
    sha256 <64 hexadecimal digits> pages/MPL_136_047-094_136_scan048.tex
    sha256 <64 hexadecimal digits> MPL_136_047-094_transcription.tex
    transcription frozen YYYY-MM-DD HH:MM:SS UTC

Brace/environment checking is a heuristic, not a TeX compiler. Escaped braces,
comments, and inline verbatim are excluded from structural token counting.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path


PREFIX = "MPL_136_047-094"
SCANS = tuple(range(48, 79)) + tuple(range(80, 95))
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
MACRO_RE = re.compile(r"\\(scanpage|cotefile)\s*\{\s*([^{}]*?)\s*\}")
ENV_RE = re.compile(r"\\(begin|end)\s*\{\s*([^{}]+?)\s*\}")
HASH_RE = re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])")
HASH_FILE_RE = re.compile(
    r"(?:pages[/\\])?MPL_136_047-094_(?:136_scan\d{3}|transcription)\.tex"
)


class Report:
    def __init__(self) -> None:
        self.errors = 0
        self.warnings = 0

    def error(self, message: str) -> None:
        self.errors += 1
        print(f"ERROR: {message}")

    def warning(self, message: str) -> None:
        self.warnings += 1
        print(f"WARNING: {message}")

    @staticmethod
    def info(message: str) -> None:
        print(f"INFO: {message}")


def escaped(text: str, index: int) -> bool:
    """True when a character is preceded by an odd run of backslashes."""
    count = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        count += 1
        index -= 1
    return bool(count % 2)


def sanitize_tex(text: str) -> str:
    """Blank comments and inline \\verb contents, retaining line numbers."""
    chars = list(text)
    i = 0
    while i < len(text):
        if text[i] == "%" and not escaped(text, i):
            j = text.find("\n", i)
            if j < 0:
                j = len(text)
            chars[i:j] = [" "] * (j - i)
            i = j
        elif text.startswith("\\verb", i) and not escaped(text, i):
            j = i + 5
            if j < len(text) and text[j] == "*":
                j += 1
            if j < len(text) and not text[j].isalpha() and text[j] not in "\r\n":
                delimiter = text[j]
                k = text.find(delimiter, j + 1)
                newline = text.find("\n", j + 1)
                if k >= 0 and (newline < 0 or k < newline):
                    chars[i:k + 1] = [" "] * (k + 1 - i)
                    i = k + 1
                    continue
            i += 1
        else:
            i += 1
    return "".join(chars)


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def check_tex(text: str, label: str, report: Report) -> str:
    clean = sanitize_tex(text)
    braces: list[int] = []
    for index, char in enumerate(clean):
        if char not in "{}" or escaped(clean, index):
            continue
        if char == "{":
            braces.append(index)
        elif braces:
            braces.pop()
        else:
            report.error(f"{label}:{line_number(clean, index)}: unmatched closing brace")
    for index in braces:
        report.error(f"{label}:{line_number(clean, index)}: unmatched opening brace")
    environments: list[tuple[str, int]] = []
    for match in ENV_RE.finditer(clean):
        if escaped(clean, match.start()):
            continue
        action, name = match.groups()
        if action == "begin":
            environments.append((name, match.start()))
        elif not environments:
            report.error(f"{label}:{line_number(clean, match.start())}: unmatched end of {name}")
        elif environments[-1][0] != name:
            report.error(
                f"{label}:{line_number(clean, match.start())}: end of {name} "
                f"does not match open {environments[-1][0]}"
            )
        else:
            environments.pop()
    for name, index in environments:
        report.error(f"{label}:{line_number(clean, index)}: unclosed environment {name}")
    if re.search(r"\\(?:documentclass|usepackage)\b", clean):
        report.error(f"{label}: contains a preamble command; the deliverable must be a fragment")
    if re.search(r"\\includegraphics\b", clean):
        report.error(f"{label}: contains an image inclusion command")
    return clean


def read_text(path: Path, report: Report) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        report.error(f"Cannot read {path.name}: {error}")
        return None


def check_pages(root: Path, report: Report) -> dict[str, Path]:
    expected = {f"{PREFIX}_136_scan{scan:03d}.tex": scan for scan in SCANS}
    actual = {path.name for path in (root / "pages").glob("*.tex")}
    for name in sorted(set(expected) - actual):
        report.error(f"Missing page file: pages/{name}")
    for name in sorted(actual - set(expected)):
        report.error(f"Unexpected page file: pages/{name}")
    targets: dict[str, Path] = {}
    page_texts: list[str] = []
    for name, scan in expected.items():
        path = root / "pages" / name
        targets[f"pages/{name}"] = path
        if name not in actual:
            continue
        text = read_text(path, report)
        if text is None:
            continue
        page_texts.append(text)
        clean = check_tex(text, f"pages/{name}", report)
        macros = [(m.group(1), m.group(2)) for m in MACRO_RE.finditer(clean)
                  if not escaped(clean, m.start())]
        pages = [value for macro, value in macros if macro == "scanpage"]
        if len(pages) != 1 or not pages[0].isdigit() or int(pages[0]) != scan:
            report.error(f"pages/{name}: expected exactly one scanpage macro for {scan}, found {pages}")
        cotes = [value for macro, value in macros if macro == "cotefile"]
        if (scan != SCANS[0] and cotes) or any(value != "136" for value in cotes) or len(cotes) > 1:
            report.error(f"pages/{name}: unexpected cotefile macro(s): {cotes}")
    combined_name = f"{PREFIX}_transcription.tex"
    combined_path = root / combined_name
    targets[combined_name] = combined_path
    combined = read_text(combined_path, report)
    if combined is not None:
        clean = check_tex(combined, combined_name, report)
        macros = [(m.group(1), m.group(2)) for m in MACRO_RE.finditer(clean)
                  if not escaped(clean, m.start())]
        scan_values = [value for macro, value in macros if macro == "scanpage"]
        if not all(value.isdigit() for value in scan_values) or tuple(map(int, scan_values)) != SCANS:
            report.error(f"{combined_name}: scanpage sequence is not the expected 46 scans")
        if [value for macro, value in macros if macro == "cotefile"] != ["136"]:
            report.error(f"{combined_name}: expected exactly one cotefile macro for 136")
        if not re.match(r"\s*\\cotefile\s*\{136\}\s*\\scanpage\s*\{0*48\}", clean):
            report.error(f"{combined_name}: must begin with cotefile 136 and scanpage 48")
        if len(page_texts) == len(SCANS):
            # Permit only whitespace separators between otherwise identical page files.
            first_has_cote = bool(re.match(r"\s*\\cotefile\s*\{136\}", sanitize_tex(page_texts[0])))
            prefixes = ("",) if first_has_cote else ("\\cotefile{136}",)
            candidates = {
                (prefix + separator + separator.join(text.strip() for text in page_texts)).strip()
                for prefix in prefixes for separator in ("", "\n", "\n\n", "\n\n\n")
            }
            if combined.strip() not in candidates:
                report.error(f"{combined_name}: differs from the ordered page-file concatenation")
    report.info(f"Page-file presence: {len(set(expected) & actual)}/{len(SCANS)} expected files")
    return targets


def check_inventory(root: Path, report: Report) -> None:
    path = root / f"{PREFIX}_inventory.csv"
    counts: Counter[int] = Counter()
    elements: set[tuple[int, str]] = set()
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != COLUMNS:
                report.error(f"{path.name}: expected columns {COLUMNS}, found {reader.fieldnames}")
                return
            for number, row in enumerate(reader, 2):
                label = f"{path.name}:{number}"
                if None in row or any(value is None for value in row.values()):
                    report.error(f"{label}: malformed CSV row")
                    continue
                if row["cote"].strip() != "136":
                    report.error(f"{label}: unexpected cote {row['cote']!r}")
                try:
                    scan = int(row["scan"].strip())
                except ValueError:
                    report.error(f"{label}: invalid scan {row['scan']!r}")
                    continue
                if scan not in SCANS:
                    report.error(f"{label}: unexpected scan {scan}")
                counts[scan] += 1
                key = (scan, row["element"].strip())
                if not key[1]:
                    report.error(f"{label}: empty element identifier")
                elif key in elements:
                    report.error(f"{label}: duplicate element identifier {key}")
                elements.add(key)
                if row["sheet_kind"].strip() not in SHEET_KINDS:
                    report.error(f"{label}: invalid sheet_kind {row['sheet_kind']!r}")
                if row["kind"].strip() not in KINDS:
                    report.error(f"{label}: invalid kind {row['kind']!r}")
                if row["transcribed"].strip() != "yes":
                    report.error(f"{label}: transcribed is not yes")
                for column in ("position", "first_words_or_objects"):
                    if not row[column].strip():
                        report.error(f"{label}: empty {column}")
    except (OSError, UnicodeError, csv.Error) as error:
        report.error(f"Cannot read inventory: {error}")
        return
    for scan in SCANS:
        if not counts[scan]:
            report.error(f"Inventory has no elements for scan {scan:03d}")
    report.info(f"Inventory: {sum(counts.values())} elements across {len(counts)} scans")


def check_frozen_hashes(root: Path, targets: dict[str, Path], require: bool, report: Report) -> None:
    log = read_text(root / "progress.log", report)
    if log is None:
        return
    frozen = bool(re.search(r"^transcription frozen\b", log, re.MULTILINE))
    if require and not frozen:
        report.error("progress.log: no transcription frozen record")
    recorded: dict[str, str] = {}
    for number, line in enumerate(log.splitlines(), 1):
        digest_match = HASH_RE.search(line)
        path_match = HASH_FILE_RE.search(line)
        if not digest_match or not path_match:
            continue
        name = path_match.group().replace("\\", "/")
        if "_136_scan" in name and not name.startswith("pages/"):
            name = "pages/" + name
        digest = digest_match.group().lower()
        if name in recorded and recorded[name] != digest:
            report.error(f"progress.log:{number}: conflicting recorded hashes for {name}")
        recorded[name] = digest
    if frozen or require:
        for name in targets:
            if name not in recorded:
                report.error(f"No frozen SHA-256 record for {name}")
    checked = 0
    for name, expected in recorded.items():
        if name not in targets:
            report.warning(f"Hash record names an unexpected transcription file: {name}")
            continue
        try:
            actual = hashlib.sha256(targets[name].read_bytes()).hexdigest()
        except OSError as error:
            report.error(f"Cannot verify hash of {name}: {error}")
            continue
        checked += 1
        if actual != expected:
            report.error(f"Frozen SHA-256 mismatch: {name}")
    report.info(f"SHA-256: {checked} records checked; frozen marker {'present' if frozen else 'absent'}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("directory", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--require-frozen", action="store_true", help="Require the frozen marker and all 47 SHA-256 records")
    args = parser.parse_args()
    report = Report()
    if not args.directory.is_dir():
        report.error(f"Package directory does not exist: {args.directory}")
        return 1
    targets = check_pages(args.directory, report)
    check_inventory(args.directory, report)
    check_frozen_hashes(args.directory, targets, args.require_frozen, report)
    for name in (f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md"):
        if not (args.directory / name).is_file():
            report.error(f"Missing required deliverable: {name}")
    status = "PASS" if report.errors == 0 else "FAIL"
    print(f"{status}: {report.errors} error(s), {report.warnings} warning(s). Structural checks only; no reading accuracy claim.")
    return 0 if report.errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
