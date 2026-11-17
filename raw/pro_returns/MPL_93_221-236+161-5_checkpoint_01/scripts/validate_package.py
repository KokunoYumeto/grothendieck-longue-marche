#!/usr/bin/env python3
"""Read-only structural checks for the MPL transcription deliverable.

This script cannot establish the accuracy or completeness of a transcription.
It checks its packaging and syntax, and reports candidates requiring human
inspection. It never rewrites a source file.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

PREFIX = "MPL_93_221-236+161-5"
EXPECTED_PAGES = [("93", n) for n in range(221, 237)] + [
    ("161-5", n) for n in range(3, 30)
]
INVENTORY_COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}


def uncomment(text: str) -> str:
    """Remove TeX comments without removing newlines or escaped percent signs."""
    out = []
    for line in text.splitlines(keepends=True):
        cut = None
        for i, char in enumerate(line):
            if char != "%":
                continue
            j = i - 1
            while j >= 0 and line[j] == "\\":
                j -= 1
            if (i - 1 - j) % 2 == 0:
                cut = i
                break
        out.append(line if cut is None else line[:cut] + ("\n" if line.endswith("\n") else ""))
    return "".join(out)


def is_escaped(text: str, index: int) -> bool:
    j = index - 1
    while j >= 0 and text[j] == "\\":
        j -= 1
    return (index - 1 - j) % 2 == 1


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checked_pages = 0
        self.inventory_rows = 0
        self.hashes_checked = 0

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def check_tex(path: Path, report: Report) -> str | None:
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.error(f"Cannot read {path.name}: {exc}")
        return None
    text = uncomment(source)
    stack: list[int] = []
    line = 1
    for index, char in enumerate(text):
        if char == "\n":
            line += 1
        elif char in "{}" and not is_escaped(text, index):
            if char == "{":
                stack.append(line)
            elif stack:
                stack.pop()
            else:
                report.error(f"{path.name}:{line}: unmatched closing brace")
    for opening in stack:
        report.error(f"{path.name}:{opening}: unmatched opening brace")

    environments: list[tuple[str, int]] = []
    pattern = re.compile(r"\\(begin|end)\s*\{([^{}]+)\}")
    for match in pattern.finditer(text):
        if is_escaped(text, match.start()):
            continue
        action, name = match.groups()
        loc = text.count("\n", 0, match.start()) + 1
        if action == "begin":
            environments.append((name, loc))
        elif not environments:
            report.error(f"{path.name}:{loc}: closing unopened environment {name}")
        elif environments[-1][0] != name:
            report.error(
                f"{path.name}:{loc}: environment {name} closes while "
                f"{environments[-1][0]} remains open"
            )
        else:
            environments.pop()
    for name, loc in environments:
        report.error(f"{path.name}:{loc}: unclosed environment {name}")

    prohibited = re.compile(r"\\(?:documentclass|usepackage|includegraphics|includepdf|pgfimage)\b")
    for match in prohibited.finditer(text):
        loc = text.count("\n", 0, match.start()) + 1
        report.error(f"{path.name}:{loc}: forbidden fragment/image command {match.group()}")

    # A manuscript may itself contain an ellipsis. Flag only likely editorial
    # placeholders, and do not confuse ordinary mathematical \\cdots with them.
    candidates = re.compile(r"\[\s*(?:\.{3}|…|\\(?:dots|ldots))\s*\]|\b(?:TODO|TBD|PLACEHOLDER)\b")
    for match in candidates.finditer(text):
        loc = text.count("\n", 0, match.start()) + 1
        report.warn(f"{path.name}:{loc}: inspect possible placeholder {match.group()!r}")
    return text


def check_inventory(work: Path, report: Report, partial: bool) -> None:
    path = work / f"{PREFIX}_inventory.csv"
    if not path.exists():
        report.error(f"Missing {path.name}")
        return
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != INVENTORY_COLUMNS:
                report.error(f"Inventory columns differ: {reader.fieldnames!r}")
                return
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        report.error(f"Cannot read inventory: {exc}")
        return
    report.inventory_rows = len(rows)
    page_counts: Counter[tuple[str, int]] = Counter()
    element_keys: set[tuple[str, int, str]] = set()
    observed_order: list[tuple[str, int]] = []
    for row_number, row in enumerate(rows, 2):
        location = f"Inventory row {row_number}"
        try:
            key = (row["cote"].strip(), int(row["scan"]))
        except (AttributeError, TypeError, ValueError):
            report.error(f"{location}: invalid cote/scan")
            continue
        if key not in EXPECTED_PAGES:
            report.error(f"{location}: unexpected page {key}")
        page_counts[key] += 1
        if not observed_order or observed_order[-1] != key:
            observed_order.append(key)
        if row["transcribed"] != "yes":
            report.error(f"{location}: transcribed is {row['transcribed']!r}, not 'yes'")
        if row["sheet_kind"] not in SHEET_KINDS:
            report.error(f"{location}: unknown sheet_kind {row['sheet_kind']!r}")
        if row["kind"] not in ELEMENT_KINDS:
            report.error(f"{location}: unknown kind {row['kind']!r}")
        for column in INVENTORY_COLUMNS:
            if row.get(column) is None or not row[column].strip():
                report.error(f"{location}: empty field {column}")
        element_key = key + (row["element"],)
        if element_key in element_keys:
            report.error(f"{location}: duplicate element identifier {element_key}")
        element_keys.add(element_key)
    expected_order = [key for key in EXPECTED_PAGES if key in page_counts]
    if observed_order != expected_order:
        report.error("Inventory pages are repeated in separate groups or are out of required order")
    if not partial:
        for key in EXPECTED_PAGES:
            if not page_counts[key]:
                report.error(f"Inventory has no rows for {key[0]} scan {key[1]:03d}")


def normalize_hashes(data: object, report: Report) -> dict[str, str]:
    """Accept a path-to-hash mapping, or conventional files/hashes containers."""
    if isinstance(data, dict):
        for key in ("hashes", "files"):
            if key in data and isinstance(data[key], (dict, list)):
                return normalize_hashes(data[key], report)
        result = {}
        for key, value in data.items():
            if isinstance(value, str) and re.fullmatch(r"[a-fA-F0-9]{64}", value):
                result[str(key)] = value.lower()
            elif isinstance(value, dict) and "sha256" in value:
                result[str(value.get("path", key))] = str(value["sha256"]).lower()
        if result:
            return result
    elif isinstance(data, list):
        result = {}
        for item in data:
            if isinstance(item, dict) and "sha256" in item:
                path = item.get("path", item.get("file", item.get("filename")))
                if path is not None:
                    result[str(path)] = str(item["sha256"]).lower()
        if result:
            return result
    report.error("Frozen hash manifest has no recognized path/sha256 entries")
    return {}


def check_hashes(work: Path, report: Report) -> None:
    manifest = work / "records" / "frozen_hashes.json"
    if not manifest.exists():
        report.warn("No records/frozen_hashes.json: freeze-hash integrity not checked")
        return
    try:
        mapping = normalize_hashes(json.loads(manifest.read_text(encoding="utf-8")), report)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.error(f"Cannot read frozen hashes: {exc}")
        return
    expected = {f"pages/{PREFIX}_{cote}_scan{scan:03d}.tex" for cote, scan in EXPECTED_PAGES}
    expected.add(f"{PREFIX}_transcription.tex")
    resolved_names: set[str] = set()
    for name, expected_hash in mapping.items():
        path = Path(name)
        if not path.is_absolute():
            path = work / path
        try:
            relative = path.resolve().relative_to(work.resolve()).as_posix()
        except ValueError:
            report.error(f"Hash path escapes work directory: {name}")
            continue
        resolved_names.add(relative)
        try:
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as exc:
            report.error(f"Cannot hash {relative}: {exc}")
            continue
        report.hashes_checked += 1
        if actual != expected_hash:
            report.error(f"Frozen hash changed: {relative}")
    for name in sorted(expected - resolved_names):
        report.error(f"Missing frozen hash for {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workdir", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--partial", action="store_true", help="Allow a contiguous unfinished page set and absent final notes")
    parser.add_argument("--json", action="store_true", help="Print a machine-readable report to stdout")
    args = parser.parse_args()
    work = args.workdir.resolve()
    report = Report()
    expected_names = {f"{PREFIX}_{cote}_scan{scan:03d}.tex" for cote, scan in EXPECTED_PAGES}
    for path in sorted((work / "pages").glob("*.tex")):
        if path.name not in expected_names:
            report.error(f"Unexpected page filename: {path.name}")
    present = []
    for cote, scan in EXPECTED_PAGES:
        path = work / "pages" / f"{PREFIX}_{cote}_scan{scan:03d}.tex"
        if not path.exists():
            if not args.partial:
                report.error(f"Missing page {path.name}")
            continue
        present.append((cote, scan))
        text = check_tex(path, report)
        if text is None:
            continue
        report.checked_pages += 1
        scan_markers = re.findall(r"\\scanpage\s*\{([^{}]+)\}", text)
        if len(scan_markers) != 1 or not scan_markers[0].isdigit() or int(scan_markers[0]) != scan:
            report.error(f"{path.name}: wrong scanpage marker(s) {scan_markers!r}")
        cote_markers = re.findall(r"\\cotefile\s*\{([^{}]+)\}", text)
        if any(value != cote for value in cote_markers):
            report.error(f"{path.name}: wrong cotefile marker(s) {cote_markers!r}")
    if present != EXPECTED_PAGES[:len(present)]:
        report.error("Present page files do not form a contiguous prefix in the required transcription order")

    combined = work / f"{PREFIX}_transcription.tex"
    if combined.exists():
        text = check_tex(combined, report)
        if text is not None:
            current_cote = None
            order = []
            cote_order = []
            for match in re.finditer(r"\\(cotefile|scanpage)\s*\{([^{}]+)\}", text):
                kind, value = match.groups()
                if kind == "cotefile":
                    current_cote = value
                    cote_order.append(value)
                else:
                    try:
                        order.append((current_cote, int(value)))
                    except ValueError:
                        report.error(f"Combined transcription has nonnumeric scanpage {value!r}")
            wanted = present if args.partial else EXPECTED_PAGES
            if order != wanted:
                report.error("Combined transcription page order/coverage differs from the required order")
            wanted_cotes = list(dict.fromkeys(cote for cote, _ in wanted))
            if cote_order != wanted_cotes:
                report.error(f"Combined transcription cotefile order differs: {cote_order!r}")
            if not re.match(r"\s*\\cotefile\{93\}\s*\\scanpage\{221\}", text):
                report.error("Combined fragment does not start with cotefile{93}, scanpage{221}")
            page_text = "\n".join(
                (work / "pages" / f"{PREFIX}_{cote}_scan{scan:03d}.tex").read_text(encoding="utf-8").strip()
                for cote, scan in present
            )
            if re.sub(r"\s+", " ", uncomment(page_text)).strip() != re.sub(r"\s+", " ", text).strip():
                report.warn("Combined transcription differs from a whitespace-normalized concatenation of page files")
    elif not args.partial:
        report.error(f"Missing {combined.name}")

    check_inventory(work, report, args.partial)
    for name in (f"{PREFIX}_doubts.md", "progress.log"):
        if not (work / name).is_file():
            report.error(f"Missing {name}")
    if not args.partial and not (work / f"{PREFIX}_notes.md").is_file():
        report.error(f"Missing {PREFIX}_notes.md")
    check_hashes(work, report)
    result = {
        "ok": not report.errors,
        "pages_checked": report.checked_pages,
        "inventory_rows": report.inventory_rows,
        "frozen_hashes_checked": report.hashes_checked,
        "errors": report.errors,
        "warnings": report.warnings,
        "scope": "Structural validation only; no image reading or transcription-accuracy assessment.",
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"{'PASS' if result['ok'] else 'FAIL'}: {report.checked_pages} pages; {report.inventory_rows} inventory rows; {report.hashes_checked} hashes")
        for message in report.errors:
            print(f"ERROR: {message}")
        for message in report.warnings:
            print(f"WARNING: {message}")
        print(result["scope"])
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
