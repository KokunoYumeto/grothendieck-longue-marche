#!/usr/bin/env python3
"""Read-only mechanical checks for MPL_133; never establishes reading accuracy.

Run only when explicitly requested by the transcriber. No file is changed.
The canonical combined file is the byte-for-byte concatenation of the sorted
page files, without additional separators. A recommended progress hash line is:
    sha256 <64 lowercase hexadecimal characters> <relative path>
Standard sha256sum output lines are also accepted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


EXPECTED_SCANS = tuple(n for n in range(2, 55) if n not in {5, 10, 41})
EXPECTED_COLUMNS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"
}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC")
PAGE_RE = re.compile(r"MPL_133_133_scan(\d{3})\.tex\Z")


def without_comments(value: str) -> str:
    """Remove TeX comments, preserving newlines for diagnostics."""
    output = []
    for line in value.splitlines(keepends=True):
        cut = len(line)
        for i, char in enumerate(line):
            if char != "%":
                continue
            previous = i - 1
            slashes = 0
            while previous >= 0 and line[previous] == "\\":
                previous -= 1
                slashes += 1
            if slashes % 2 == 0:
                cut = i
                break
        output.append(line[:cut] + ("\n" if cut < len(line) and line.endswith("\n") else ""))
    return "".join(output)


def escaped(value: str, pos: int) -> bool:
    count = 0
    pos -= 1
    while pos >= 0 and value[pos] == "\\":
        count += 1
        pos -= 1
    return bool(count % 2)


def tex_structure(value: str, label: str) -> list[str]:
    value = without_comments(value)
    problems: list[str] = []
    braces: list[int] = []
    for pos, char in enumerate(value):
        if char not in "{}" or escaped(value, pos):
            continue
        line = value.count("\n", 0, pos) + 1
        if char == "{":
            braces.append(line)
        elif braces:
            braces.pop()
        else:
            problems.append(f"{label}:{line}: unmatched closing brace")
    problems.extend(f"{label}:{line}: unclosed opening brace" for line in braces)

    environments: list[tuple[str, int]] = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", value):
        action, name = match.groups()
        line = value.count("\n", 0, match.start()) + 1
        if action == "begin":
            environments.append((name, line))
        elif not environments:
            problems.append(f"{label}:{line}: end of unopened environment {name}")
        elif environments[-1][0] != name:
            problems.append(f"{label}:{line}: end {name} mismatches {environments[-1][0]}")
        else:
            environments.pop()
    problems.extend(f"{label}:{line}: unclosed environment {name}" for name, line in environments)

    delimiters: list[tuple[str, int]] = []
    for match in re.finditer(r"\\[\[\]\(\)]", value):
        if escaped(value, match.start()):
            continue
        token = match.group()
        line = value.count("\n", 0, match.start()) + 1
        if token in {r"\[", r"\("}:
            delimiters.append((token, line))
        elif delimiters and delimiters[-1][0] == {r"\]": r"\[", r"\)": r"\("}[token]:
            delimiters.pop()
        else:
            problems.append(f"{label}:{line}: unmatched math delimiter {token}")
    problems.extend(f"{label}:{line}: unclosed math delimiter {token}" for token, line in delimiters)
    dollars = sum(1 for i, char in enumerate(value) if char == "$" and not escaped(value, i))
    if dollars % 2:
        problems.append(f"{label}: odd number of unescaped dollar signs")
    if re.search(r"\\(?:documentclass|usepackage|includegraphics)\b", value):
        problems.append(f"{label}: preamble or image command in transcription fragment")
    return problems


def log_hashes(log: str) -> tuple[dict[str, str], list[str]]:
    hashes: dict[str, str] = {}
    problems = []
    patterns = [
        re.compile(r"(?:sha256|sha-256)\s+([0-9a-f]{64})\s+(.+)$", re.I),
        re.compile(r"([0-9a-f]{64})\s+\*?(.+)$", re.I),
        re.compile(r"(?:sha256|sha-256)\s+(.+?)\s+([0-9a-f]{64})$", re.I),
    ]
    for line in log.splitlines():
        for i, pattern in enumerate(patterns):
            match = pattern.fullmatch(line.strip())
            if not match:
                continue
            digest, name = match.groups() if i < 2 else match.groups()[::-1]
            name = name.removeprefix("./")
            if name in hashes and hashes[name] != digest.lower():
                problems.append(f"progress.log: conflicting frozen hashes for {name}")
            hashes[name] = digest.lower()
            break
    return hashes, problems


def validate(root: Path, partial: bool) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    counts: dict[str, int] = {}
    expected_names = {f"MPL_133_133_scan{n:03d}.tex" for n in EXPECTED_SCANS}
    pages_dir = root / "pages"
    files = sorted(pages_dir.glob("*.tex"))
    actual_names = {path.name for path in files}
    counts["page_files"] = len(files)
    if not partial:
        for name in sorted(expected_names - actual_names):
            errors.append(f"missing page file: pages/{name}")
    for name in sorted(actual_names - expected_names):
        errors.append(f"unexpected page file: pages/{name}")

    page_bytes: list[bytes] = []
    existing_scans: set[int] = set()
    for path in files:
        match = PAGE_RE.fullmatch(path.name)
        if not match:
            continue
        scan = int(match.group(1))
        existing_scans.add(scan)
        data = path.read_bytes()
        page_bytes.append(data)
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.name}: invalid UTF-8: {exc}")
            continue
        errors.extend(tex_structure(text, f"pages/{path.name}"))
        scan_macros = re.findall(r"\\scanpage\{(\d+)\}", without_comments(text))
        if scan_macros != [str(scan)]:
            errors.append(f"{path.name}: expected one scanpage{{{scan}}}, got {scan_macros}")
        if not text.strip():
            errors.append(f"{path.name}: empty page")

    combined = root / "MPL_133_transcription.tex"
    if not combined.is_file():
        if not partial:
            errors.append("missing MPL_133_transcription.tex")
    else:
        if combined.read_bytes() != b"".join(page_bytes):
            errors.append("combined transcription is not exact concatenation of sorted page files")
        try:
            combined_text = combined.read_text(encoding="utf-8")
            live = without_comments(combined_text).lstrip()
            if not re.match(r"\\cotefile\{133\}\s*\\scanpage\{2\}", live):
                errors.append("combined transcription must start with cotefile{133} then scanpage{2}")
            if re.findall(r"\\cotefile\{([^}]+)\}", live) != ["133"]:
                errors.append("combined transcription should contain exactly one cotefile{133}")
        except UnicodeDecodeError as exc:
            errors.append(f"combined transcription: invalid UTF-8: {exc}")

    inventory = root / "MPL_133_inventory.csv"
    row_scans: Counter[int] = Counter()
    if not inventory.is_file():
        errors.append("missing MPL_133_inventory.csv")
    else:
        with inventory.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if tuple(reader.fieldnames or ()) != EXPECTED_COLUMNS:
                errors.append(f"inventory columns differ from required columns: {reader.fieldnames}")
            keys: set[tuple[str, str, str]] = set()
            for line, row in enumerate(reader, 2):
                try:
                    scan = int(row.get("scan", ""))
                except (TypeError, ValueError):
                    errors.append(f"inventory:{line}: invalid scan")
                    continue
                row_scans[scan] += 1
                if scan not in EXPECTED_SCANS:
                    errors.append(f"inventory:{line}: unexpected scan {scan}")
                if str(row.get("cote", "")).strip() != "133":
                    errors.append(f"inventory:{line}: cote is not 133")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"inventory:{line}: invalid sheet_kind {row.get('sheet_kind')!r}")
                if row.get("kind") not in ELEMENT_KINDS:
                    errors.append(f"inventory:{line}: invalid kind {row.get('kind')!r}")
                if row.get("transcribed") != "yes":
                    errors.append(f"inventory:{line}: transcribed must be exactly yes")
                for field in ("element", "position", "first_words_or_objects"):
                    if not str(row.get(field) or "").strip():
                        errors.append(f"inventory:{line}: empty {field}")
                key = (str(row.get("cote")), str(scan), str(row.get("element")))
                if key in keys:
                    errors.append(f"inventory:{line}: duplicate per-scan element identifier {key[2]}")
                keys.add(key)
    required_scans = existing_scans if partial else set(EXPECTED_SCANS)
    for scan in sorted(required_scans - set(row_scans)):
        errors.append(f"inventory: no rows for scan {scan:03d}")
    counts["inventory_elements"] = sum(row_scans.values())
    counts["inventory_scans"] = len(row_scans)

    progress = root / "progress.log"
    if not progress.is_file():
        errors.append("missing progress.log")
    else:
        log = progress.read_text(encoding="utf-8")
        lines = log.splitlines()
        if not lines or not DATE_RE.fullmatch(lines[0]):
            errors.append("progress.log: first line is not a UTC timestamp in the required format")
        done = {int(x) for x in re.findall(r"^133 scan (\d{3}) done \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$", log, re.M)}
        audited = {int(x) for x in re.findall(r"^scan (\d{3}) audited \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$", log, re.M)}
        for scan in sorted(required_scans - done):
            errors.append(f"progress.log: no done timestamp for scan {scan:03d}")
        if not partial:
            for scan in sorted(set(EXPECTED_SCANS) - audited):
                errors.append(f"progress.log: no audit timestamp for scan {scan:03d}")
        counts["logged_done"] = len(done)
        counts["logged_audited"] = len(audited)
        freeze_lines = [(i, s) for i, s in enumerate(lines) if s.startswith("transcription frozen ")]
        context_lines = [(i, s) for i, s in enumerate(lines) if s.startswith("context opened ")]
        if not partial and not freeze_lines:
            errors.append("progress.log: no transcription frozen line")
        if freeze_lines:
            if len(freeze_lines) != 1:
                errors.append("progress.log: expected one transcription frozen event")
            freeze_index, freeze_line = freeze_lines[0]
            if not DATE_RE.fullmatch(freeze_line.removeprefix("transcription frozen ")):
                errors.append("progress.log: invalid freeze timestamp")
            for i, line in enumerate(lines):
                if re.match(r"(?:133 scan \d{3} done|scan \d{3} audited) ", line) and i > freeze_index:
                    warnings.append("progress.log: a done/audit event follows the freeze; verify intended chronology")
                    break
            if any(i <= freeze_index for i, _ in context_lines):
                errors.append("progress.log: context opened before or at transcription freeze")
        if not partial and not context_lines:
            errors.append("progress.log: no context opened line")
        for _, line in context_lines:
            if not DATE_RE.fullmatch(line.removeprefix("context opened ")):
                errors.append("progress.log: invalid context-open timestamp")
        hashes, hash_problems = log_hashes(log)
        errors.extend(hash_problems)
        hash_targets = [*(f"pages/{path.name}" for path in files), "MPL_133_transcription.tex"]
        if not partial or freeze_lines:
            for name in hash_targets:
                target = root / name
                if not target.is_file():
                    continue
                if name not in hashes:
                    errors.append(f"progress.log: missing frozen SHA-256 for {name}")
                elif hashlib.sha256(target.read_bytes()).hexdigest() != hashes[name]:
                    errors.append(f"frozen SHA-256 mismatch: {name}")
        counts["logged_hashes"] = len(hashes)
        if not partial and not re.search(r"hash(?:es)?[^\n]*(?:unchanged|verified)|(?:unchanged|verified)[^\n]*hash(?:es)?", log, re.I):
            errors.append("progress.log: no final statement that frozen hashes are unchanged/verified")

    for name in ("MPL_133_doubts.md", "MPL_133_notes.md"):
        target = root / name
        if not target.is_file() and not partial:
            errors.append(f"missing {name}")
        elif target.is_file() and not target.stat().st_size:
            errors.append(f"empty {name}")
    return {
        "ok": not errors,
        "mode": "partial" if partial else "final",
        "scope": "Mechanical consistency only; no visual, linguistic, or mathematical accuracy is assessed.",
        "root": str(root), "counts": counts, "errors": errors, "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true", help="Check existing work without requiring completion or freeze.")
    args = parser.parse_args()
    result = validate(args.root.resolve(), args.partial)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
