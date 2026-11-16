#!/usr/bin/env python3
"""Read-only structural checks for MPL_15_139-194.

This program does not read image pixels, run OCR, infer a reading, or inspect the
context ZIP. The scan ZIP is used only as a filename manifest. It cannot certify
that every mark was transcribed or that any reading is correct.

Usage from the deliverable directory:
    python scripts/validate_deliverables.py --stage draft
    python scripts/validate_deliverables.py --stage frozen
    python scripts/validate_deliverables.py --stage final

The combined fragment must equal the exact page bytes, in manifest order,
joined by --separator (default: one additional LF between files). No whitespace
normalization occurs. Every page retains its own terminal newline.

Preferred progress checksum format:
    sha256 <64 hexadecimal characters> pages/MPL_15_139-194_15_scan139.tex
    sha256 <64 hexadecimal characters> MPL_15_139-194_transcription.tex
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile


PACKAGE = "MPL_15_139-194"
COTE = "15"
EXPECTED_SCANS = (
    139, 141, 142, 143, 144, 145, 147, 148, 149, 150, 151, 152,
    154, 155, 157, 159, 160, 161, 162, 163, 164, 165, 166, 168,
    172, 173, 174, 175, 176, 177, 178, 179, 180, 182, 183, 184,
    185, 186, 187, 189, 190, 191, 192, 193, 194,
)
INVENTORY_HEADER = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
STAMP = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC)"
MATH_ENVS = {
    "math", "displaymath", "equation", "equation*", "align", "align*",
    "alignat", "alignat*", "gather", "gather*", "multline", "multline*",
    "eqnarray", "eqnarray*", "flalign", "flalign*",
}


@dataclass
class Finding:
    level: str
    code: str
    message: str


class Report:
    def __init__(self) -> None:
        self.findings: list[Finding] = []
        self.stats: dict[str, object] = {}

    def add(self, level: str, code: str, message: str) -> None:
        self.findings.append(Finding(level, code, message))

    def error(self, code: str, message: str) -> None:
        self.add("error", code, message)

    def warning(self, code: str, message: str) -> None:
        self.add("warning", code, message)

    @property
    def errors(self) -> int:
        return sum(x.level == "error" for x in self.findings)


def clean_tex(source: str) -> str:
    """Remove unescaped comments, preserving line numbers and text lengths."""
    result = []
    for line in source.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char != "%":
                continue
            j = i - 1
            backslashes = 0
            while j >= 0 and line[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                end = len(line.rstrip("\r\n"))
                line = line[:i] + " " * (end - i) + line[end:]
                break
        result.append(line)
    return "".join(result)


def tex_checks(source: str, label: str, report: Report) -> None:
    text = clean_tex(source)
    brace_stack: list[int] = []
    env_stack: list[tuple[str, int]] = []
    math_stack: list[tuple[str, int]] = []
    text_argument_starts: set[int] = set()
    text_argument_frames: list[tuple[int, list[tuple[str, int]]]] = []
    line = 1
    i = 0

    def error(code: str, message: str) -> None:
        report.error(code, f"{label}:{line}: {message}")

    def math_token(token: str) -> None:
        opening = {"\\(": "\\)", "\\[": "\\]"}
        closing = {"\\)": "\\(", "\\]": "\\["}
        if token in opening:
            if math_stack:
                error("tex-math", f"nested math delimiter {token}")
            math_stack.append((token, line))
        elif token in closing:
            if not math_stack or math_stack[-1][0] != closing[token]:
                error("tex-math", f"unmatched math delimiter {token}")
            else:
                math_stack.pop()
        else:
            if math_stack and math_stack[-1][0] == token:
                math_stack.pop()
            elif math_stack:
                error("tex-math", f"mixed math delimiters {math_stack[-1][0]} and {token}")
            else:
                math_stack.append((token, line))

    while i < len(text):
        char = text[i]
        if char == "\n":
            line += 1
            i += 1
            continue
        if char == "\\":
            command_match = re.match(r"\\([A-Za-z@]+|.)", text[i:])
            if not command_match:
                error("tex-command", "terminal backslash")
                i += 1
                continue
            token = command_match.group(0)
            command = command_match.group(1)
            if command in {
                "text", "mbox", "hbox", "textrm", "textnormal", "textsf",
                "texttt", "textbf", "textit", "textsl", "textsc", "emph",
            } and (math_stack or any(env in MATH_ENVS for env, _ in env_stack)):
                argument_match = re.match(r"\s*\{", text[i + len(token):])
                if argument_match:
                    text_argument_starts.add(i + len(token) + argument_match.end() - 1)
            if token in {"\\(", "\\)", "\\[", "\\]"}:
                math_token(token)
            if command in {"begin", "end"}:
                env_match = re.match(r"\\(?:begin|end)\s*\{([^{}]+)\}", text[i:])
                if not env_match:
                    error("tex-environment", f"malformed {token}")
                else:
                    env = env_match.group(1)
                    if command == "begin":
                        env_stack.append((env, line))
                    elif not env_stack:
                        error("tex-environment", f"unmatched end of {env}")
                    elif env_stack[-1][0] != env:
                        error("tex-environment", f"end of {env} closes {env_stack[-1][0]}")
                    else:
                        env_stack.pop()
            if command in {"documentclass", "usepackage", "includegraphics", "input", "include"}:
                error("tex-fragment", f"unexpected {token} in a self-contained fragment")
            if command == "illegible":
                arg = re.match(r"\\illegible\s*\{([1-9][0-9]*)\}", text[i:])
                if not arg:
                    error("illegible-count", "illegible needs a positive integer word count")
                if math_stack or any(env in MATH_ENVS for env, _ in env_stack):
                    error("illegible-in-math", "illegible occurs within detected mathematics")
            i += len(token)
            continue
        if char == "{":
            brace_stack.append(line)
            if i in text_argument_starts:
                text_argument_frames.append((len(brace_stack), math_stack))
                math_stack = []
        elif char == "}":
            if not brace_stack:
                error("tex-braces", "unmatched closing brace")
            else:
                if text_argument_frames and text_argument_frames[-1][0] == len(brace_stack):
                    for delimiter, start_line in math_stack:
                        report.error("tex-math", f"{label}:{start_line}: unclosed math delimiter {delimiter} in text argument")
                    _, math_stack = text_argument_frames.pop()
                brace_stack.pop()
        elif char == "$":
            token = "$$" if text[i:i + 2] == "$$" else "$"
            math_token(token)
            i += len(token)
            continue
        i += 1
    for start_line in brace_stack:
        report.error("tex-braces", f"{label}:{start_line}: unclosed brace")
    for env, start_line in env_stack:
        report.error("tex-environment", f"{label}:{start_line}: unclosed environment {env}")
    for token, start_line in math_stack:
        report.error("tex-math", f"{label}:{start_line}: unclosed math delimiter {token}")


def get_manifest(path: Path | None, report: Report) -> tuple[int, ...]:
    if path is None or not path.exists():
        report.stats["manifest"] = "embedded filename-only manifest from supplied scan ZIP"
        return EXPECTED_SCANS
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()  # Deliberately never read member bytes.
    except (OSError, zipfile.BadZipFile) as exc:
        report.error("scan-manifest", str(exc))
        return EXPECTED_SCANS
    regex = re.compile(rf"{PACKAGE}_{COTE}_scan([0-9]{{3}})\.jpg")
    scans = tuple(sorted(int(m.group(1)) for name in names if (m := regex.fullmatch(name))))
    if scans != EXPECTED_SCANS:
        report.error("scan-manifest", f"supplied ZIP whole-page manifest differs: {scans}")
    for scan in scans:
        for suffix in ("", "_a", "_b"):
            filename = f"{PACKAGE}_{COTE}_scan{scan:03d}{suffix}.jpg"
            if names.count(filename) != 1:
                report.error("scan-manifest", f"expected exactly one ZIP entry: {filename}")
    report.stats["manifest"] = str(path)
    return scans


def check_pages(root: Path, scans: tuple[int, ...], stage: str, separator: bytes, report: Report) -> dict[int, bytes]:
    pages: dict[int, bytes] = {}
    expected_names = {f"{PACKAGE}_{COTE}_scan{scan:03d}.tex" for scan in scans}
    page_dir = root / "pages"
    actual_names = {p.name for p in page_dir.glob("*.tex")}
    for name in sorted(actual_names - expected_names):
        report.error("extra-page", name)
    for scan in scans:
        path = page_dir / f"{PACKAGE}_{COTE}_scan{scan:03d}.tex"
        if not path.exists():
            if stage != "draft":
                report.error("missing-page", str(path.relative_to(root)))
            continue
        data = path.read_bytes()
        pages[scan] = data
        try:
            source = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            report.error("page-encoding", f"{path.name}: {exc}")
            continue
        if not data:
            report.error("empty-page", path.name)
        text = clean_tex(source)
        markers = re.findall(r"\\scanpage\s*\{\s*([0-9]+)\s*\}", text)
        if markers != [str(scan)]:
            report.error("scan-marker", f"{path.name}: markers are {markers}")
        cote_markers = re.findall(r"\\cotefile\s*\{\s*([^{}]+)\s*\}", text)
        expected_cotes = [COTE] if scan == scans[0] else []
        if cote_markers != expected_cotes:
            report.error("cote-marker", f"{path.name}: expected {expected_cotes}, found {cote_markers}")
        first = rf"\s*\\cotefile\s*\{{{COTE}\}}\s*\\scanpage\s*\{{{scan}\}}" if scan == scans[0] else rf"\s*\\scanpage\s*\{{{scan}\}}"
        if not re.match(first, text):
            report.error("page-start", f"{path.name}: required opening marker sequence missing")
        tex_checks(source, path.name, report)
    present = tuple(scan for scan in scans if scan in pages)
    if present != scans[:len(present)]:
        report.error("page-order", "completed pages do not form an initial segment of the manifest")
    combined_path = root / f"{PACKAGE}_transcription.tex"
    if combined_path.exists():
        expected = separator.join(pages[scan] for scan in present)
        actual = combined_path.read_bytes()
        if expected != actual:
            mismatch = next((i for i, (a, b) in enumerate(zip(expected, actual)) if a != b), min(len(expected), len(actual)))
            report.error("combined-bytes", f"combined file differs from exact page concatenation at byte {mismatch}; expected {len(expected)} bytes, found {len(actual)}")
    elif stage != "draft":
        report.error("combined-missing", combined_path.name)
    report.stats["expected_pages"] = len(scans)
    report.stats["present_pages"] = len(pages)
    report.stats["page_bytes"] = sum(map(len, pages.values()))
    return pages


def check_inventory(root: Path, scans: tuple[int, ...], pages: dict[int, bytes], stage: str, report: Report) -> None:
    path = root / f"{PACKAGE}_inventory.csv"
    if not path.exists():
        report.error("inventory-missing", path.name)
        return
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != INVENTORY_HEADER:
                report.error("inventory-header", f"expected {INVENTORY_HEADER}; found {reader.fieldnames}")
                return
            rows = list(reader)
    except (OSError, csv.Error, UnicodeDecodeError) as exc:
        report.error("inventory-read", str(exc))
        return
    seen: set[tuple[int, str]] = set()
    covered: set[int] = set()
    sheet_kinds: dict[int, set[str]] = {}
    row_scans: list[int] = []
    for number, row in enumerate(rows, 2):
        where = f"{path.name}:{number}"
        if None in row or any(value is None for value in row.values()):
            report.error("inventory-width", f"{where}: incorrect number of CSV fields")
            continue
        if row["cote"] != COTE:
            report.error("inventory-cote", f"{where}: cote must equal {COTE}")
        try:
            scan = int(row["scan"])
        except ValueError:
            report.error("inventory-scan", f"{where}: noninteger scan")
            continue
        if scan not in scans:
            report.error("inventory-scan", f"{where}: scan {scan} is outside the manifest")
        if scan not in pages:
            report.error("inventory-page", f"{where}: no page file for scan {scan}")
        covered.add(scan)
        row_scans.append(scan)
        if row["sheet_kind"] not in SHEET_KINDS:
            report.error("sheet-kind", f"{where}: invalid sheet_kind {row['sheet_kind']!r}")
        sheet_kinds.setdefault(scan, set()).add(row["sheet_kind"])
        if row["kind"] not in ELEMENT_KINDS:
            report.error("element-kind", f"{where}: invalid kind {row['kind']!r}")
        for field in ("element", "position", "first_words_or_objects"):
            if not row[field].strip():
                report.error("inventory-empty", f"{where}: empty {field}")
        key = (scan, row["element"])
        if key in seen:
            report.error("inventory-duplicate", f"{where}: duplicate element identifier for scan {scan}")
        seen.add(key)
        if row["transcribed"] != "yes":
            report.error("inventory-status", f"{where}: transcribed must be exactly yes")
    for scan, kinds in sheet_kinds.items():
        if len(kinds) != 1:
            report.error("sheet-kind", f"scan {scan}: inconsistent sheet_kind values {sorted(kinds)}")
    for scan in pages:
        if scan not in covered:
            report.error("inventory-coverage", f"scan {scan}: no inventory rows")
    if row_scans != sorted(row_scans):
        report.error("inventory-order", "inventory pages are not in manifest order")
    report.stats["inventory_rows"] = len(rows)
    report.stats["inventory_pages"] = len(covered)
    report.stats["sheet_kind_counts"] = {kind: sum(kinds == {kind} for kinds in sheet_kinds.values()) for kind in sorted(SHEET_KINDS)}


def parse_hash(line: str) -> tuple[str, str] | None:
    patterns = (
        r"(?i)^\s*(?:sha-?256\s*[: ]\s*)?([0-9a-f]{64})\s+\*?(.+?)\s*$",
        r"(?i)^\s*sha-?256\s+(.+?)\s+([0-9a-f]{64})\s*$",
        r"(?i)^\s*sha-?256\s*\((.+?)\)\s*=\s*([0-9a-f]{64})\s*$",
    )
    for index, pattern in enumerate(patterns):
        match = re.match(pattern, line)
        if match:
            return (match.group(2), match.group(1).lower()) if index == 0 else (match.group(1), match.group(2).lower())
    return None


def check_progress(root: Path, scans: tuple[int, ...], pages: dict[int, bytes], stage: str, report: Report) -> None:
    path = root / "progress.log"
    if not path.exists():
        report.error("progress-missing", path.name)
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not re.fullmatch(STAMP, lines[0]):
        report.error("progress-start", "first progress.log line must be a UTC timestamp")
    done: dict[int, list[int]] = {}
    audited: dict[int, list[int]] = {}
    done_order: list[int] = []
    freeze_lines: list[int] = []
    context_lines: list[int] = []
    unchanged_lines: list[int] = []
    timestamps: list[tuple[int, datetime]] = []
    for number, line in enumerate(lines, 1):
        stamp_match = re.search(STAMP + r"$", line)
        if stamp_match:
            try:
                timestamps.append((number, datetime.strptime(stamp_match.group(1), "%Y-%m-%d %H:%M:%S UTC")))
            except ValueError:
                report.error("progress-time", f"progress.log:{number}: invalid UTC timestamp")
        match = re.fullmatch(rf"{COTE} scan ([0-9]+) done {STAMP}", line)
        if match:
            scan = int(match.group(1))
            done.setdefault(scan, []).append(number)
            done_order.append(scan)
        match = re.fullmatch(rf"scan ([0-9]+) audited {STAMP}", line)
        if match:
            audited.setdefault(int(match.group(1)), []).append(number)
        if re.fullmatch(rf"transcription frozen {STAMP}", line):
            freeze_lines.append(number)
        if re.fullmatch(rf"context opened {STAMP}", line):
            context_lines.append(number)
        if re.search(r"(?i)(hash.*unchanged|unchanged.*hash|frozen.*hash.*verified)", line):
            unchanged_lines.append(number)
    for (earlier_line, earlier), (later_line, later) in zip(timestamps, timestamps[1:]):
        if later < earlier:
            report.error("progress-time-order", f"progress.log:{later_line}: timestamp precedes line {earlier_line}")
    if done_order != sorted(done_order):
        report.error("done-order", "done entries are not in scan order")
    for scan in pages:
        if scan not in done:
            report.error("done-missing", f"scan {scan}: no done entry")
    for scan in done:
        if scan not in pages:
            report.error("done-without-page", f"scan {scan}: done entry without a page file")
        if len(done[scan]) != 1:
            report.warning("done-repeat", f"scan {scan}: {len(done[scan])} done entries")
    for scan in audited:
        if scan not in pages:
            report.error("audit-without-page", f"scan {scan}: audit entry without a page file")
    require_frozen = stage in {"frozen", "final"} or bool(freeze_lines or context_lines)
    if require_frozen:
        for scan in scans:
            if scan not in audited:
                report.error("audit-missing", f"scan {scan}: no audit entry")
        if not freeze_lines:
            report.error("freeze-missing", "no transcription frozen entry")
        if len(freeze_lines) > 1:
            report.error("freeze-repeat", "multiple transcription frozen entries")
        if done and audited and min(min(v) for v in audited.values()) <= max(max(v) for v in done.values()):
            report.error("audit-order", "a second-reading audit entry precedes completion of the first pass")
        if freeze_lines and audited and freeze_lines[0] <= max(max(v) for v in audited.values()):
            report.error("freeze-order", "transcription frozen entry precedes an audit entry")
    if context_lines:
        if not freeze_lines or min(context_lines) <= min(freeze_lines):
            report.error("context-order", "context opened entry does not follow transcription frozen")
        if len(context_lines) > 1:
            report.warning("context-repeat", "multiple context opened entries")
    if stage == "final":
        if not context_lines:
            report.error("context-missing", "no context opened entry")
        if not unchanged_lines:
            report.error("hash-verification-log", "no final hashes-unchanged statement")
        elif context_lines and max(unchanged_lines) <= max(context_lines):
            report.error("hash-verification-order", "hashes-unchanged statement does not follow context opening")
    boundary = min(context_lines) if context_lines else len(lines) + 1
    recorded: dict[str, str] = {}
    for number, line in enumerate(lines, 1):
        parsed = parse_hash(line)
        if parsed is None or number >= boundary:
            continue
        filename, checksum = parsed
        target = Path(filename)
        if target.is_absolute():
            try:
                target = target.relative_to(root)
            except ValueError:
                continue
        if target.parent == Path(".") and target.name.startswith(f"{PACKAGE}_{COTE}_scan"):
            target = Path("pages") / target
        key = target.as_posix()
        if key in recorded and recorded[key] != checksum:
            report.error("hash-conflict", f"conflicting frozen checksums for {key}")
        recorded[key] = checksum
    expected_paths = [f"pages/{PACKAGE}_{COTE}_scan{scan:03d}.tex" for scan in scans]
    expected_paths.append(f"{PACKAGE}_transcription.tex")
    for relative in expected_paths:
        if relative not in recorded:
            if require_frozen:
                report.error("hash-missing", f"no checksum before context opening for {relative}")
            continue
        file = root / relative
        if file.exists():
            actual = hashlib.sha256(file.read_bytes()).hexdigest()
            if actual != recorded[relative]:
                report.error("hash-changed", f"frozen checksum does not match {relative}")
        else:
            report.error("hash-file-missing", relative)
    report.stats["done_entries"] = sum(map(len, done.values()))
    report.stats["audit_entries"] = sum(map(len, audited.values()))
    report.stats["frozen_checksums"] = sum(p in recorded for p in expected_paths)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--scans-zip", type=Path, help="Optional scan ZIP, read only for member filenames")
    parser.add_argument("--stage", choices=("draft", "frozen", "final"), default="final")
    parser.add_argument("--separator", choices=("none", "newline", "blankline"), default="newline", help="Exact bytes inserted between page files: 0, 1, or 2 LF characters")
    parser.add_argument("--json", action="store_true", help="Print the report as JSON to stdout")
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = args.scans_zip
    if manifest is None:
        nearby = root.parent / "upload" / f"{PACKAGE}_scans.zip"
        if nearby.exists():
            manifest = nearby
    report = Report()
    report.stats["stage"] = args.stage
    report.stats["root"] = str(root)
    scans = get_manifest(manifest, report)
    separator = {"none": b"", "newline": b"\n", "blankline": b"\n\n"}[args.separator]
    pages = check_pages(root, scans, args.stage, separator, report)
    check_inventory(root, scans, pages, args.stage, report)
    check_progress(root, scans, pages, args.stage, report)
    for suffix in ("doubts.md", "notes.md"):
        file = root / f"{PACKAGE}_{suffix}"
        required = suffix == "doubts.md" or args.stage == "final"
        if required and (not file.exists() or not file.read_bytes().strip()):
            report.error("required-file", f"missing or empty {file.name}")
    result = {
        "ok": report.errors == 0,
        "scope": "Structural checks only; no image reading, OCR, or transcription verification.",
        "stats": report.stats,
        "findings": [asdict(x) for x in report.findings],
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("PASS" if result["ok"] else "FAIL", "— structural validation")
        for key, value in report.stats.items():
            print(f"{key}: {value}")
        for finding in report.findings:
            print(f"{finding.level.upper()} [{finding.code}] {finding.message}")
        print(result["scope"])
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
