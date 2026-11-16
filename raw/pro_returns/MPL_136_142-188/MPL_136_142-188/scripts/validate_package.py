#!/usr/bin/env python3
"""Read-only mechanical validation of the MPL_136_142-188 deliverables.

No OCR, image access, context-archive access, or textual interpretation occurs.
The report contains structural findings, never manuscript excerpts.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

PACKAGE = "MPL_136_142-188"
COTE = "136"
SCANS = tuple(n for n in range(142, 189) if n != 161)
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.details: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def finish(self) -> int:
        for message in self.details:
            print("INFO:", message)
        for message in self.warnings:
            print("WARNING:", message)
        for message in self.errors:
            print("ERROR:", message)
        print(f"RESULT: {len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        return 1 if self.errors else 0


def uncomment(text: str) -> str:
    """Remove unescaped TeX comments while preserving line numbers.

    Escaped control symbols are copied in pairs, so \\% and \\\\% behave
    differently, as they do in TeX. No expansion or verbatim interpretation.
    """
    result: list[str] = []
    i = 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            result.append(text[i:i + 2])
            i += 2
        elif text[i] == "%":
            end = text.find("\n", i)
            if end < 0:
                break
            result.append("\n")
            i = end + 1
        else:
            result.append(text[i])
            i += 1
    return "".join(result)


def check_tex(text: str, label: str, report: Report) -> str:
    text = uncomment(text)
    stack: list[int] = []
    line = 1
    i = 0
    while i < len(text):
        char = text[i]
        if char == "\n":
            line += 1
        if char == "\\" and i + 1 < len(text):
            # Skip a control symbol or the first letter of a control word.
            # A following opening brace is visited normally on the next turn.
            i += 2
            continue
        if char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                report.error(f"{label}: unmatched closing brace at line {line}")
        i += 1
    for opening_line in stack:
        report.error(f"{label}: unclosed brace from line {opening_line}")

    envs: list[tuple[str, int]] = []
    # Ignore control sequences immediately preceded by an odd slash run.
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        preceding = 0
        k = match.start() - 1
        while k >= 0 and text[k] == "\\":
            preceding += 1
            k -= 1
        if preceding % 2:
            continue
        verb, env = match.groups()
        lineno = text.count("\n", 0, match.start()) + 1
        if verb == "begin":
            envs.append((env, lineno))
        elif not envs:
            report.error(f"{label}: unmatched environment end at line {lineno}")
        elif envs[-1][0] != env:
            report.error(f"{label}: crossed/mismatched environments at line {lineno}")
        else:
            envs.pop()
    for _, lineno in envs:
        report.error(f"{label}: unclosed environment from line {lineno}")
    return text


def digest_entries(text: str) -> dict[str, str]:
    """Accept sha256sum lines, optionally prefixed with 'sha256 '."""
    entries: dict[str, str] = {}
    for line in text.splitlines():
        match = re.fullmatch(r"(?:sha256\s+)?([0-9a-fA-F]{64})\s+\*?(.+?)\s*", line)
        if match:
            entries[match[2].removeprefix("./")] = match[1].lower()
    return entries


def verify_digests(entries: dict[str, str], root: Path, label: str,
                   report: Report) -> None:
    for name, expected in entries.items():
        path = (root / name).resolve()
        if not path.is_relative_to(root.resolve()):
            report.error(f"{label}: digest path outside package directory")
            continue
        if not path.is_file():
            report.error(f"{label}: missing hashed file {name}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            report.error(f"{label}: SHA-256 mismatch for {name}")
    report.details.append(f"{label}: checked {len(entries)} SHA-256 entries")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--partial", action="store_true", help="allow unfinished scans (default)")
    mode.add_argument("--final", action="store_true", help="require the complete frozen package")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--hash-manifest", type=Path,
                        help="optional sha256sum-format manifest, relative to package root")
    args = parser.parse_args()
    root = args.root.resolve()
    report = Report()
    expected = {n: f"pages/{PACKAGE}_{COTE}_scan{n:03d}.tex" for n in SCANS}
    present = {n: root / name for n, name in expected.items() if (root / name).is_file()}
    expected_paths = {root / name for name in expected.values()}
    extras = sorted(set((root / "pages").glob("*.tex")) - expected_paths)
    for path in extras:
        report.error(f"Unexpected page filename: {path.name}")
    missing = sorted(set(SCANS) - set(present))
    if args.final and missing:
        report.error("Missing scan files: " + ", ".join(map(str, missing)))
    if present and list(present) != list(SCANS[:len(present)]):
        report.error("Completed page files do not form the prescribed sequential prefix")
    report.details.append(f"Page files: {len(present)}/{len(SCANS)}")
    for scan, path in present.items():
        try:
            tex = path.read_text(encoding="utf-8")
        except UnicodeError:
            report.error(f"{path.name}: invalid UTF-8")
            continue
        if not tex.strip():
            report.error(f"{path.name}: empty file")
        cleaned = check_tex(tex, path.name, report)
        marks = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", cleaned)
        if marks != [str(scan)]:
            report.error(f"{path.name}: expected exactly one matching scanpage marker")
        if re.search(r"\\(?:documentclass|usepackage)\b", cleaned):
            report.error(f"{path.name}: fragment contains a preamble command")

    inventory = root / f"{PACKAGE}_inventory.csv"
    inventory_scans: set[int] = set()
    row_count = 0
    identifiers: set[tuple[int, str]] = set()
    if not inventory.is_file():
        report.error("Missing inventory CSV")
    else:
        with inventory.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != FIELDS:
                report.error("Inventory column names/order differ from required schema")
            else:
                for line, row in enumerate(reader, 2):
                    row_count += 1
                    prefix = f"Inventory row {line}"
                    if None in row or any(value is None for value in row.values()):
                        report.error(prefix + ": malformed field count")
                        continue
                    try:
                        scan = int(row["scan"])
                    except ValueError:
                        report.error(prefix + ": invalid scan number")
                        continue
                    inventory_scans.add(scan)
                    if scan not in SCANS or row["cote"] != COTE:
                        report.error(prefix + ": unexpected scan/cote")
                    if row["sheet_kind"] not in SHEET_KINDS:
                        report.error(prefix + ": unsupported sheet_kind")
                    if row["kind"] not in KINDS:
                        report.error(prefix + ": unsupported element kind")
                    if row["transcribed"] != "yes":
                        report.error(prefix + ": transcribed is not yes")
                    if any(not row[key].strip() for key in FIELDS):
                        report.error(prefix + ": empty required value")
                    identifier = (scan, row["element"])
                    if identifier in identifiers:
                        report.error(prefix + ": duplicate element identifier within scan")
                    identifiers.add(identifier)
        without_rows = sorted(set(present) - inventory_scans)
        if without_rows:
            report.error("Pages without inventory rows: " + ", ".join(map(str, without_rows)))
        without_files = sorted(inventory_scans - set(present))
        if without_files:
            report.error("Inventory scans without page files: " + ", ".join(map(str, without_files)))
    report.details.append(f"Inventory: {row_count} rows across {len(inventory_scans)} scans")

    combined = root / f"{PACKAGE}_transcription.tex"
    if combined.is_file():
        concatenated = b"".join(path.read_bytes() for path in present.values())
        if combined.read_bytes() != concatenated:
            report.error("Combined transcription differs from exact page-byte concatenation")
        report.details.append("Compared combined transcription with ordered page concatenation")
    elif args.final:
        report.error("Missing combined transcription")

    log = root / "progress.log"
    entries: dict[str, str] = {}
    if not log.is_file():
        report.error("Missing progress.log")
    else:
        logtext = log.read_text(encoding="utf-8")
        first = logtext.splitlines()[0] if logtext.splitlines() else ""
        if not re.search(r"\d{4}-\d\d-\d\d[T ]\d\d:\d\d:\d\d.*(?:Z|UTC|\+00:00)$", first):
            report.error("progress.log first line is not an explicit UTC timestamp")
        done = [int(n) for n in re.findall(r"(?m)^136 scan (\d+) done .+", logtext)]
        audited = [int(n) for n in re.findall(r"(?m)^(?:136 )?scan (\d+) audited .+", logtext)]
        missing_done = sorted(set(present) - set(done))
        if missing_done:
            report.error("Page files missing done log entries: " + ", ".join(map(str, missing_done)))
        for name, values in (("done", done), ("audited", audited)):
            if set(values) - set(present):
                report.error(f"{name} log refers to scans without page files")
            if any(count > 1 for count in Counter(values).values()):
                report.warning(f"Repeated {name} log entries")
        if args.final and set(audited) != set(SCANS):
            report.error("Final log lacks complete second-reading audit coverage")
        freeze = re.search(r"(?m)^transcription frozen .+", logtext)
        opened = re.search(r"(?m)^context opened .+", logtext)
        if args.final and not freeze:
            report.error("Final log lacks transcription frozen entry")
        if opened and (not freeze or opened.start() < freeze.start()):
            report.error("Context-open log entry precedes the transcription freeze")
        entries = digest_entries(logtext)
        if args.final:
            required_hashes = set(expected.values()) | {combined.name}
            absent = required_hashes - set(entries)
            if absent:
                report.error(f"progress.log lacks {len(absent)} required file SHA-256 entries")
        if entries:
            verify_digests(entries, root, "progress.log", report)
        report.details.append(f"Log coverage: {len(set(done))} done, {len(set(audited))} audited")

    manifest = args.hash_manifest
    if manifest is None:
        candidates = [root / "records" / name for name in
                      ("frozen.sha256", "frozen_hashes.sha256", "freeze.sha256")]
        found = [path for path in candidates if path.is_file()]
        if len(found) > 1:
            report.warning("Several known freeze manifests exist; checking all")
    else:
        found = [manifest if manifest.is_absolute() else root / manifest]
    for path in found:
        if not path.is_file():
            report.error("Specified hash manifest does not exist")
        else:
            hashes = digest_entries(path.read_text(encoding="utf-8"))
            if not hashes:
                report.error(f"{path.name}: no recognizable SHA-256 entries")
            verify_digests(hashes, root, path.name, report)

    if args.final:
        for suffix in ("doubts.md", "notes.md"):
            path = root / f"{PACKAGE}_{suffix}"
            if not path.is_file() or not path.stat().st_size:
                report.error(f"Missing or empty {path.name}")
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
