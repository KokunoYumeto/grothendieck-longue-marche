#!/usr/bin/env python3
"""Validate packaging syntax only; this does not assess manuscript fidelity.

No images, OCR, source archives, or context materials are opened. The report
contains filenames and structural diagnostics, never transcription excerpts.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

PREFIX = "MPL_12_099-149"
SCANS = (99, 101, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114,
         115, 116, 118, 119, 120, 122, 125, 127, 129, 131, 133, 135,
         137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149)
HEADER = ("cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed")
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
KINDS = {"text", "display", "diagram", "drawing", "margin note",
         "insertion", "deletion"}
STAMP = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
MARKERS = re.compile(r"\\(unsure|illegible)\b")


def uncomment(text: str) -> str:
    """Remove TeX comments while retaining newlines and escaped percent signs."""
    result = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for i, char in enumerate(line):
            if char != "%":
                continue
            j = i - 1
            while j >= 0 and line[j] == "\\":
                j -= 1
            if (i - j - 1) % 2 == 0:
                cut = i
                break
        result.append(line[:cut] + ("\n" if cut < len(line) and line.endswith("\n") else ""))
    return "".join(result)


def unescaped(text: str, pos: int) -> bool:
    j = pos - 1
    while j >= 0 and text[j] == "\\":
        j -= 1
    return (pos - j - 1) % 2 == 0


def argument(text: str, pos: int) -> tuple[str | None, int]:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text) or text[pos] != "{":
        return None, pos
    start, depth = pos + 1, 1
    pos += 1
    while pos < len(text):
        if unescaped(text, pos):
            if text[pos] == "{":
                depth += 1
            elif text[pos] == "}":
                depth -= 1
                if depth == 0:
                    return text[start:pos], pos + 1
        pos += 1
    return None, pos


class Check:
    def __init__(self, root: Path, final: bool):
        self.root, self.final = root, final
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.page_paths: dict[int, Path] = {}
        self.inventory_rows = 0

    def error(self, message: str) -> None:
        self.errors.append(message)

    def check_tex(self, path: Path, scan: int | None = None) -> None:
        try:
            raw = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error(f"{path.name}: cannot read UTF-8 ({type(exc).__name__})")
            return
        text = uncomment(raw)
        if re.search(r"\\(?:documentclass|usepackage|newcommand|renewcommand)\b", text):
            self.error(f"{path.name}: preamble or macro-definition command in fragment")
        if re.search(r"\\(?:includegraphics|includepdf|epsfig|epsfbox|pgfimage)\b", text):
            self.error(f"{path.name}: image-inclusion command is forbidden in the transcription")
        if scan is not None:
            markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", text)
            if [int(x) for x in markers] != [scan]:
                self.error(f"{path.name}: expected exactly one matching scanpage marker")
        depth = 0
        for i, char in enumerate(text):
            if char in "{}" and unescaped(text, i):
                depth += 1 if char == "{" else -1
                if depth < 0:
                    self.error(f"{path.name}: unmatched closing brace")
                    break
        if depth > 0:
            self.error(f"{path.name}: unclosed brace(s): {depth}")
        for match in MARKERS.finditer(text):
            content, _ = argument(text, match.end())
            line = text.count("\n", 0, match.start()) + 1
            if content is None or not content.strip():
                self.error(f"{path.name}:{line}: missing, empty, or unbalanced doubt argument")
            elif match.group(1) == "illegible" and not re.fullmatch(r"\s*[1-9]\d*\s*", content):
                self.error(f"{path.name}:{line}: illegible argument is not a positive word count")
        # Ordinary ellipses and 'etc.' may be genuine source text: do not reject them.
        forbidden = re.compile(r"\b(?:TODO|TBD|PLACEHOLDER)\b|\[(?:omitted|transcription pending|insert transcription)\]", re.I)
        for match in forbidden.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            self.error(f"{path.name}:{line}: apparent editorial placeholder; review required")
        if "[...]" in text:
            self.warnings.append(f"{path.name}: literal bracketed ellipsis requires human source review")

    def pages(self) -> None:
        directory = self.root / "pages"
        expected_names = {f"{PREFIX}_12_scan{n:03d}.tex": n for n in SCANS}
        if directory.exists():
            for path in sorted(directory.glob("*.tex")):
                if path.name not in expected_names:
                    self.error(f"pages/{path.name}: unexpected page filename")
                else:
                    n = expected_names[path.name]
                    self.page_paths[n] = path
                    self.check_tex(path, n)
        if self.final:
            missing = sorted(set(SCANS) - self.page_paths.keys())
            if missing:
                self.error("Missing page files: " + ", ".join(f"{n:03d}" for n in missing))
        combined = self.root / f"{PREFIX}_transcription.tex"
        if combined.exists():
            self.check_tex(combined)
            actual = combined.read_bytes()
            expected = b"".join(self.page_paths[n].read_bytes() for n in SCANS if n in self.page_paths)
            if actual != expected:
                self.error("Combined transcription is not the exact byte concatenation of page files in scan order")
            text = uncomment(actual.decode("utf-8")).lstrip()
            if not re.match(r"\\cotefile\{12\}\s*\\scanpage\{0?99\}", text):
                self.error("Combined fragment must begin with cotefile{12} followed by scanpage{99}")
            if len(re.findall(r"\\cotefile\s*\{", text)) != 1:
                self.error("Combined fragment must contain exactly one cotefile marker")
        elif self.final:
            self.error("Combined transcription is missing")

    def inventory(self) -> None:
        path = self.root / f"{PREFIX}_inventory.csv"
        if not path.exists():
            if self.final or self.page_paths:
                self.error("Inventory file is missing")
            return
        seen, kinds, identifiers = set(), defaultdict(set), set()
        try:
            with path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle, strict=True)
                if tuple(reader.fieldnames or ()) != HEADER:
                    self.error("Inventory header does not exactly match the required columns")
                    return
                for line, row in enumerate(reader, 2):
                    self.inventory_rows += 1
                    where = f"Inventory row {line}"
                    if None in row or any(v is None for v in row.values()):
                        self.error(f"{where}: incorrect field count")
                        continue
                    try:
                        scan = int(row["scan"])
                    except ValueError:
                        self.error(f"{where}: invalid scan number")
                        continue
                    if scan not in SCANS or row["cote"] != "12":
                        self.error(f"{where}: unexpected cote or scan")
                    seen.add(scan)
                    kinds[scan].add(row["sheet_kind"])
                    if row["sheet_kind"] not in SHEET_KINDS:
                        self.error(f"{where}: invalid sheet_kind")
                    if row["kind"] not in KINDS:
                        self.error(f"{where}: invalid element kind")
                    if row["transcribed"] != "yes":
                        self.error(f"{where}: transcribed must equal yes")
                    for field in ("element", "position", "first_words_or_objects"):
                        if not row[field].strip():
                            self.error(f"{where}: {field} is empty")
                    key = (row["cote"], scan, row["element"])
                    if key in identifiers:
                        self.error(f"{where}: repeated element identifier within page")
                    identifiers.add(key)
        except (OSError, UnicodeError, csv.Error) as exc:
            self.error(f"Inventory cannot be parsed ({type(exc).__name__})")
            return
        expected = set(SCANS) if self.final else set(self.page_paths)
        if expected - seen:
            self.error("Inventory lacks page coverage: " + ", ".join(f"{n:03d}" for n in sorted(expected - seen)))
        if seen - set(self.page_paths):
            self.error("Inventory references pages without saved page files")
        for scan, values in kinds.items():
            if len(values) != 1:
                self.error(f"Inventory scan {scan:03d}: inconsistent sheet_kind")

    def progress(self) -> None:
        path = self.root / "progress.log"
        if not path.exists():
            if self.final or self.page_paths:
                self.error("progress.log is missing")
            return
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or not re.fullmatch(STAMP, lines[0]):
            self.error("progress.log first line must be YYYY-MM-DD HH:MM:SS UTC")
        done, audits, frozen, opened, unchanged = {}, {}, [], [], []
        dated_events: list[tuple[int, datetime]] = []
        hashes: dict[str, list[tuple[int, str]]] = defaultdict(list)
        for line_no, line in enumerate(lines, 1):
            match = re.fullmatch(r"12 scan (\d+) done (" + STAMP + r")", line)
            audit = re.fullmatch(r"(?:12 )?scan (\d+) audited (" + STAMP + r")", line)
            if match:
                done[int(match.group(1))] = line_no
            if audit:
                audits[int(audit.group(1))] = line_no
            if re.fullmatch(r"transcription frozen " + STAMP, line):
                frozen.append(line_no)
            if re.fullmatch(r"context opened " + STAMP, line):
                opened.append(line_no)
            if re.fullmatch(r"transcription hashes unchanged " + STAMP, line):
                unchanged.append(line_no)
            if (match or audit or line_no in frozen + opened + unchanged or line_no == 1):
                event_time = re.search(STAMP + r"$", line)
                if event_time:
                    try:
                        dated_events.append((line_no, datetime.strptime(event_time.group(), "%Y-%m-%d %H:%M:%S UTC")))
                    except ValueError:
                        pass  # Reported by the complete timestamp pass below.
            digest = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
            if digest:
                hashes[digest.group(2)].append((line_no, digest.group(1).lower()))
            for timestamp in re.findall(STAMP, line):
                try:
                    datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S UTC")
                except ValueError:
                    self.error(f"progress.log:{line_no}: invalid UTC timestamp")
        expected = set(SCANS) if self.final else set(self.page_paths)
        if expected - done.keys():
            self.error("Missing done records: " + ", ".join(f"{n:03d}" for n in sorted(expected - done.keys())))
        if (set(done) | set(audits)) - set(SCANS):
            self.error("progress.log contains unexpected scan IDs")
        if list(done) != sorted(done):
            self.error("Page-completion records are not in increasing scan order")
        for earlier, later in zip(dated_events, dated_events[1:]):
            if earlier[1] > later[1]:
                self.error(f"progress.log:{later[0]}: milestone timestamp precedes the prior milestone")
        if self.final:
            if set(SCANS) - audits.keys():
                self.error("Final log lacks an audit record for every scan")
            if audits and done and min(audits.values()) < max(done.values()):
                self.error("Second-reading audit began before the last page was recorded done")
            if len(frozen) != 1:
                self.error("Final log must contain exactly one transcription frozen record")
            if len(opened) != 1:
                self.error("Final log must contain exactly one context opened record")
            if not unchanged:
                self.error("Final log lacks transcription hashes unchanged record")
            if frozen:
                boundary = frozen[0]
                if audits and max(audits.values()) > boundary:
                    self.error("An audit record occurs after the freeze")
                if opened and opened[0] <= boundary:
                    self.error("Context opened record must occur after the freeze")
                if unchanged and unchanged[-1] <= max(frozen + opened):
                    self.error("Final unchanged record must follow freeze and context opening")
                targets = list(self.page_paths.values()) + [self.root / f"{PREFIX}_transcription.tex"]
                for target in targets:
                    if not target.exists():
                        continue
                    name = target.relative_to(self.root).as_posix()
                    records = [(index, value) for index, value in hashes.get(name, []) if index < boundary]
                    if not records:
                        self.error(f"No pre-freeze SHA-256 entry for {name}")
                    else:
                        if audits and records[-1][0] <= max(audits.values()):
                            self.error(f"Frozen SHA-256 entry precedes completion of the audit: {name}")
                        if records[-1][1] != hashlib.sha256(target.read_bytes()).hexdigest():
                            self.error(f"Current SHA-256 differs from frozen value: {name}")

    def run(self) -> dict:
        self.pages()
        self.inventory()
        self.progress()
        if self.final:
            for name in (f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md"):
                path = self.root / name
                if not path.exists() or path.stat().st_size == 0:
                    self.error(f"Required nonempty file missing: {name}")
        return {"scope": "Structural checks only; no semantic or visual completeness assessment",
                "mode": "final" if self.final else "partial", "page_files": len(self.page_paths),
                "expected_page_files": len(SCANS), "inventory_rows": self.inventory_rows,
                "passed": not self.errors, "errors": self.errors, "warnings": self.warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--final", action="store_true", help="require all deliverables, audits, and frozen hashes")
    parser.add_argument("--json", action="store_true", help="emit a machine-readable report")
    args = parser.parse_args()
    report = Check(args.root.resolve(), args.final).run()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(report["scope"])
        print(f"{report['mode']}: {report['page_files']}/{report['expected_page_files']} page files; "
              f"{report['inventory_rows']} inventory rows")
        for category in ("errors", "warnings"):
            for message in report[category]:
                print(f"{category.upper()}: {message}")
        print("PASS" if report["passed"] else "FAIL")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
