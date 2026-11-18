#!/usr/bin/env python3
"""Check the package's structure; never certify its transcription accuracy.

Run only when the primary reader authorizes inspection of the saved text.
No image, source archive, context archive, network, or OCR access is performed.
This program is read-only.  Its JSON output goes to stdout, never to a file.

Recommended frozen-hash log syntax (one file per line):
    sha256 <64 lowercase hexadecimal digits> pages/<filename>.tex
    sha256 <64 lowercase hexadecimal digits> MPL_29_141-187_transcription.tex
The SHA-256 lines and `transcription frozen <UTC time>` must precede any
`context opened <UTC time>` line.  Standard sha256sum output is also accepted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import sys


PREFIX = "MPL_29_141-187"
COTE = "29"
SCANS = list(range(141, 188))
COMBINED = f"{PREFIX}_transcription.tex"
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
# `typed` is explicitly required in the prompt's typed-sheet instructions.
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
STAMP = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
DISCLAIMER = (
    "STRUCTURAL CHECK ONLY: no judgment is made about readings, omissions, "
    "diplomatic fidelity, mathematical correctness, research completeness, "
    "or whether any image was actually inspected."
)


def filename(scan: int) -> str:
    return f"{PREFIX}_{COTE}_scan{scan:03d}.tex"


class Report:
    def __init__(self, root: Path, partial: bool) -> None:
        self.root = root
        self.partial = partial
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.counts: dict[str, object] = {}

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def missing(self, message: str) -> None:
        (self.warn if self.partial else self.error)(message)

    def read(self, path: Path) -> str | None:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error(f"Cannot read {path.relative_to(self.root)}: {exc}")
            return None


def check_pages(r: Report) -> tuple[dict[int, str], list[int]]:
    folder = r.root / "pages"
    if not folder.is_dir():
        r.error("Missing pages/ directory.")
        return {}, []
    expected = {filename(n): n for n in SCANS}
    found = {p.name: p for p in folder.glob("*.tex")}
    missing = sorted(set(expected) - set(found))
    extra = sorted(set(found) - set(expected))
    if missing:
        r.missing("Missing page files: " + ", ".join(missing))
    if extra:
        r.error("Unexpected .tex page filenames: " + ", ".join(extra))
    present = sorted(expected[name] for name in found if name in expected)
    if present and present != SCANS[:len(present)]:
        r.error("Present pages do not form the required uninterrupted numeric prefix.")
    texts: dict[int, str] = {}
    for n in present:
        text = r.read(folder / filename(n))
        if text is None:
            continue
        texts[n] = text
        if not text.strip():
            r.error(f"scan {n}: empty page file.")
        markers = re.findall(r"\\scanpage\{(\d+)\}", text)
        if markers != [str(n)]:
            r.error(f"scan {n}: expected exactly its own scanpage marker; got {markers!r}.")
        cotes = re.findall(r"\\cotefile\{([^}]+)\}", text)
        if n == SCANS[0] and cotes != [COTE]:
            r.error("First page must have exactly one cotefile{29} marker.")
        elif n != SCANS[0] and cotes:
            r.error(f"scan {n}: unexpected repeated cotefile marker.")
        if re.search(r"\\(?:documentclass|begin\{document\}|end\{document\})", text):
            r.error(f"scan {n}: standalone-document command appears in a fragment.")
    r.counts["page_files"] = len(present)
    r.counts["expected_pages"] = len(SCANS)
    return texts, present


def check_inventory(r: Report, present: list[int]) -> None:
    path = r.root / f"{PREFIX}_inventory.csv"
    if not path.is_file():
        r.missing("Inventory CSV is missing.")
        return
    coverage: set[int] = set()
    ids: set[tuple[int, str]] = set()
    rows = 0
    by_sheet: dict[int, set[str]] = {}
    try:
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != COLUMNS:
                r.error(f"Inventory header must be exactly {COLUMNS!r}; got {reader.fieldnames!r}.")
                return
            for line, row in enumerate(reader, 2):
                rows += 1
                label = f"Inventory row {line}"
                if None in row or any(value is None for value in row.values()):
                    r.error(f"{label}: malformed CSV field count.")
                    continue
                if row["cote"] != COTE:
                    r.error(f"{label}: cote must be 29.")
                try:
                    scan = int(row["scan"])
                except ValueError:
                    r.error(f"{label}: invalid scan number {row['scan']!r}.")
                    continue
                if scan not in SCANS:
                    r.error(f"{label}: scan {scan} is outside 141–187.")
                coverage.add(scan)
                if scan not in present:
                    r.error(f"{label}: inventory claims scan {scan}, whose page file is absent.")
                if row["sheet_kind"] not in SHEET_KINDS:
                    r.error(f"{label}: unsupported sheet_kind {row['sheet_kind']!r}.")
                by_sheet.setdefault(scan, set()).add(row["sheet_kind"])
                if row["kind"] not in KINDS:
                    r.error(f"{label}: unsupported element kind {row['kind']!r}.")
                if row["transcribed"] != "yes":
                    r.error(f"{label}: transcribed is not exactly 'yes'.")
                for key in ("element", "position", "first_words_or_objects"):
                    if not row[key].strip():
                        r.error(f"{label}: empty {key}.")
                identity = (scan, row["element"])
                if identity in ids:
                    r.error(f"{label}: duplicate element ID {identity!r}.")
                ids.add(identity)
    except (OSError, UnicodeError, csv.Error) as exc:
        r.error(f"Cannot parse inventory: {exc}")
        return
    missing = sorted(set(present) - coverage)
    if missing:
        r.error(f"Saved page files without inventory rows: {missing}.")
    if not r.partial and coverage != set(SCANS):
        r.error("Final inventory does not cover exactly scans 141–187.")
    for n, kinds in by_sheet.items():
        if len(kinds) > 1:
            r.error(f"scan {n}: inconsistent sheet_kind values on one sheet: {sorted(kinds)}.")
    r.counts["inventory_rows"] = rows
    r.counts["inventory_scans"] = len(coverage)


def check_combined(r: Report, texts: dict[int, str], present: list[int]) -> None:
    path = r.root / COMBINED
    if not path.is_file():
        r.missing("Combined transcription fragment is missing.")
        return
    combined = r.read(path)
    if combined is None:
        return
    if not re.match(r"\s*\\cotefile\{29\}\s*\\scanpage\{141\}", combined):
        r.error("Combined fragment must start with cotefile{29}, then scanpage{141}.")
    markers = [int(n) for n in re.findall(r"\\scanpage\{(\d+)\}", combined)]
    expected_scans = present if r.partial else SCANS
    if markers != expected_scans:
        r.error(f"Combined scanpage order differs from expected order: {markers}.")
    # Only blank newlines at file boundaries are ignored.  Internal words,
    # symbols, spacing, comments, and line breaks must agree byte-for-text.
    offset = 0
    for n in present:
        if n not in texts:
            continue
        while offset < len(combined) and combined[offset] in "\r\n":
            offset += 1
        chunk = texts[n].strip("\r\n")
        if not combined.startswith(chunk, offset):
            r.error(f"Combined fragment differs from saved scan {n} at its expected position.")
            return
        offset += len(chunk)
    if combined[offset:].strip("\r\n"):
        r.error("Combined fragment has unexpected text after the last saved page.")


def parse_hash(line: str) -> tuple[str, str] | None:
    patterns = (
        r"(?:sha256|SHA256)\s+([0-9a-fA-F]{64})\s+(.+)",
        r"([0-9a-fA-F]{64})\s+[* ]?(.+)",
    )
    for pattern in patterns:
        match = re.fullmatch(pattern, line.strip())
        if match:
            return match[1].lower(), match[2].strip().strip('"')
    match = re.fullmatch(r"SHA256\s*\((.+)\)\s*=\s*([0-9a-fA-F]{64})", line.strip())
    if match:
        return match[2].lower(), match[1].strip().strip('"')
    return None


def canonical_hash_path(raw: str, root: Path) -> str:
    path = Path(raw)
    if path.is_absolute():
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            return raw
    normalized = path.as_posix()
    prefix = root.name + "/"
    return normalized[len(prefix):] if normalized.startswith(prefix) else normalized


def check_progress_and_hashes(r: Report, present: list[int]) -> None:
    path = r.root / "progress.log"
    if not path.is_file():
        r.error("progress.log is missing.")
        return
    text = r.read(path)
    if text is None:
        return
    lines = text.splitlines()
    if not lines or not re.fullmatch(STAMP, lines[0]):
        r.error("The first progress.log line must be the initial UTC timestamp.")
    done: dict[int, list[int]] = {}
    audited: dict[int, list[int]] = {}
    frozen: list[int] = []
    context: list[int] = []
    hash_rows: dict[str, list[tuple[int, str]]] = {}
    done_order: list[int] = []
    for i, line in enumerate(lines, 1):
        match = re.fullmatch(rf"29 scan (\d+) done ({STAMP})", line)
        if match:
            n = int(match[1])
            done.setdefault(n, []).append(i)
            done_order.append(n)
        match = re.fullmatch(rf"scan (\d+) audited ({STAMP})", line)
        if match:
            audited.setdefault(int(match[1]), []).append(i)
        if re.fullmatch(rf"transcription frozen ({STAMP})", line):
            frozen.append(i)
        if re.fullmatch(rf"context opened ({STAMP})", line):
            context.append(i)
        parsed = parse_hash(line)
        if parsed:
            digest, rawpath = parsed
            relpath = canonical_hash_path(rawpath, r.root)
            hash_rows.setdefault(relpath, []).append((i, digest))
    if set(done) != set(present):
        r.error(f"Done log/page-file mismatch: logged={sorted(done)}, files={present}.")
    unique_done_order = list(dict.fromkeys(done_order))
    if unique_done_order != sorted(unique_done_order):
        r.error("Initial page completion entries are not in numeric page order.")
    for n, positions in done.items():
        if len(positions) > 1:
            r.warn(f"scan {n}: duplicate done log entries ({len(positions)}).")
    for n, positions in audited.items():
        if n not in present:
            r.error(f"scan {n}: audited entry without a saved page.")
        if n in done and positions[0] < done[n][0]:
            r.error(f"scan {n}: audit logged before completion.")
    if not r.partial and set(audited) != set(SCANS):
        r.error(f"Second-audit coverage is incomplete: {sorted(audited)}.")
    if audited and done and min(i for v in audited.values() for i in v) < max(v[0] for v in done.values()):
        r.error("A second-audit entry precedes completion of the last page.")
    if not frozen:
        r.missing("No transcription frozen timestamp is recorded.")
    elif len(frozen) > 1:
        r.error("Multiple transcription frozen markers; freeze state is ambiguous.")
    if frozen:
        if set(audited) != set(SCANS):
            r.error("Transcription was marked frozen without all 47 audit entries.")
        if audited and max(i for v in audited.values() for i in v) > frozen[0]:
            r.error("An audit entry follows the frozen marker.")
        if context and context[0] <= frozen[0]:
            r.error("Context was opened before the frozen marker.")
    elif context:
        r.error("Context opened entry exists without a transcription freeze.")
    required = {f"pages/{filename(n)}" for n in SCANS} | {COMBINED}
    if frozen or not r.partial:
        missing = sorted(required - set(hash_rows))
        if missing:
            r.error("Missing frozen SHA-256 entries: " + ", ".join(missing))
        for relative in sorted(required & set(hash_rows)):
            rows = hash_rows[relative]
            values = {digest for _, digest in rows}
            if len(values) > 1:
                r.error(f"Conflicting frozen hashes for {relative}.")
                continue
            if context and rows[0][0] >= context[0]:
                r.error(f"Hash for {relative} was first recorded after context opened.")
            target = r.root / relative
            try:
                current = hashlib.sha256(target.read_bytes()).hexdigest()
            except OSError as exc:
                r.error(f"Cannot verify hash of {relative}: {exc}")
                continue
            if current != rows[0][1]:
                r.error(f"Frozen SHA-256 mismatch: {relative}.")
    r.counts.update({
        "done_scans": len(done), "audited_scans": len(audited),
        "frozen_markers": len(frozen), "context_opened_markers": len(context),
        "required_hashes_recorded": len(required & set(hash_rows)),
    })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true", help="Check a completed-page prefix; warn for unfinished final work.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable report to stdout.")
    args = parser.parse_args()
    report = Report(args.root.resolve(), args.partial)
    texts, present = check_pages(report)
    check_inventory(report, present)
    check_combined(report, texts, present)
    check_progress_and_hashes(report, present)
    for name in (f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md", "CHECK_EVENTS.tsv"):
        if not (report.root / name).is_file():
            report.missing(f"Required deliverable is missing: {name}.")
    result = {
        "scope": "partial structural validation" if args.partial else "final structural validation",
        "passed": not report.errors,
        "disclaimer": DISCLAIMER,
        "counts": report.counts,
        "errors": report.errors,
        "warnings": report.warnings,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(DISCLAIMER)
        print(result["scope"] + ": " + ("PASS" if result["passed"] else "FAIL"))
        for key, value in report.counts.items():
            print(f"  {key}: {value}")
        for message in report.errors:
            print("ERROR: " + message)
        for message in report.warnings:
            print("WARNING: " + message)
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
