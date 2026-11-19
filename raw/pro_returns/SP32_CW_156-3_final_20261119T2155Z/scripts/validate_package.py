#!/usr/bin/env python3
"""Structural checks for SP32_CW_156-3; never judges or edits a reading.

Usage:
    python scripts/validate_package.py [WORKDIR] [--hash-manifest PATH] [--final]

An optional manifest may be a sha256sum-style text file, a TSV with path/file
and sha256/hash columns, or a JSON mapping of relative paths to SHA-256 values
(optionally beneath a top-level "files" or "sha256" key).
Every supplied hash manifest must cover all 16 pages and the combined fragment.
The optional --final gate also requires a manifest, all 16 per-page audit-record
files, and at least one CHECK_EVENTS data row; it does not certify their content.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

STEM = "SP32_CW_156-3"
SCANS = list(range(26, 42))
HEADERS = {
    f"{STEM}_collation.tsv": (
        "folder", "their_page", "our_scan", "line", "their_reading",
        "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
        "confidence",
    ),
    f"{STEM}_inventory.csv": (
        "scan", "sheet_kind", "hand", "element", "kind", "position",
        "first_words_or_objects", "transcribed",
    ),
    "CHECK_EVENTS.tsv": ("statement_id", "date", "who", "type", "outcome"),
}
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)",
    "deletion state", "insertion or placement",
    "abbreviation expanded or spelling modernised", "readable ink left as \\ill{}",
    "drawing or diagram", "other",
}
INVENTORY_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover",
}


def expected_page(scan: int) -> str:
    folder = "J156-3-04" if scan <= 33 else "J156-3-05"
    return f"pages/{folder}_156-3_scan{scan:03d}.tex"


def without_comments(text: str) -> str:
    """Remove unescaped TeX comments, preserving character/line positions."""
    out = []
    for line in text.splitlines(keepends=True):
        cut = None
        for pos, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            j = pos - 1
            while j >= 0 and line[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                cut = pos
                break
        if cut is not None:
            line = line[:cut] + " " * (len(line[cut:].rstrip("\r\n"))) + (
                "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
            )
        out.append(line)
    return "".join(out)


def structural_warnings(text: str) -> list[str]:
    """Conservative lexical checks; TeX is not parsed or expanded."""
    clean = without_comments(text)
    messages = []
    braces = []
    line = 1
    pos = 0
    while pos < len(clean):
        char = clean[pos]
        if char == "\n":
            line += 1
            pos += 1
            continue
        if char == "\\":
            # Skip escaped punctuation, including literal braces, and commands.
            m = re.match(r"\\(?:[A-Za-z@]+\*?|.)", clean[pos:])
            if m:
                token = m.group()
                pos += len(token)
                if token in (r"\verb", r"\verb*") and pos < len(clean):
                    delimiter = clean[pos]
                    end = clean.find(delimiter, pos + 1)
                    if end != -1:
                        line += clean[pos:end + 1].count("\n")
                        pos = end + 1
                continue
        if char == "{":
            braces.append(line)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                messages.append(f"line {line}: unmatched closing brace")
        pos += 1
    messages.extend(f"line {n}: unclosed opening brace" for n in braces)
    stack = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
        action, env = match.groups()
        at = clean.count("\n", 0, match.start()) + 1
        if action == "begin":
            stack.append((env, at))
        elif not stack:
            messages.append(f"line {at}: unmatched end of environment {env}")
        elif stack[-1][0] != env:
            messages.append(f"line {at}: environment {env} closes while {stack[-1][0]} is open")
        else:
            stack.pop()
    messages.extend(f"line {at}: unclosed environment {env}" for env, at in stack)
    return messages


def read_manifest(path: Path) -> dict[str, str]:
    raw = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".json" or raw.lstrip().startswith("{"):
        obj = json.loads(raw)
        obj = obj.get("files", obj.get("sha256", obj))
        if isinstance(obj, list):
            return {
                str(row.get("path", row.get("file"))): str(row.get("sha256", row.get("hash")))
                for row in obj
            }
        return {
            str(k): str(v.get("sha256", v.get("hash")) if isinstance(v, dict) else v)
            for k, v in obj.items()
        }
    lines = [line for line in raw.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    if not lines:
        raise ValueError("empty hash manifest")
    first = [v.lower() for v in lines[0].split("\t")]
    if any(v in first for v in ("path", "file", "filename")) and any(v in first for v in ("sha256", "hash")):
        rows = csv.DictReader(lines, delimiter="\t")
        names = {n.lower(): n for n in rows.fieldnames or []}
        pkey = next(names[k] for k in ("path", "file", "filename") if k in names)
        hkey = next(names[k] for k in ("sha256", "hash") if k in names)
        return {row[pkey]: row[hkey] for row in rows}
    result = {}
    for line in lines:
        m = re.fullmatch(r"\s*([0-9a-fA-F]{64})[ \t]+\*?(.+?)\s*", line)
        if m:
            digest, name = m.groups()
        else:
            m = re.fullmatch(r"(.+?)\t([0-9a-fA-F]{64})", line)
            if not m:
                raise ValueError("unrecognized hash-manifest row")
            name, digest = m.groups()
        result[name] = digest
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("workdir", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--hash-manifest", type=Path)
    parser.add_argument("--warnings-as-errors", action="store_true")
    parser.add_argument("--final", action="store_true", help="require freeze/audit/event completion metadata")
    args = parser.parse_args()
    root = args.workdir.resolve()
    errors, warnings = [], []
    required = [
        f"{STEM}_transcription.tex", f"{STEM}_changes.md", f"{STEM}_collation.tsv",
        f"{STEM}_doubts.md", f"{STEM}_inventory.csv", f"{STEM}_notes.md",
        "progress.log", "CHECK_EVENTS.tsv",
    ] + [expected_page(n) for n in SCANS]
    if args.final:
        required.extend(f"records/audit{n:03d}.json" for n in SCANS)
        if not args.hash_manifest:
            errors.append("--final requires --hash-manifest")
    for rel in required:
        p = root / rel
        if not p.is_file():
            errors.append(f"missing file: {rel}")
        elif p.stat().st_size == 0:
            errors.append(f"empty file: {rel}")

    for rel, columns in HEADERS.items():
        path = root / rel
        if not path.is_file():
            continue
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="," if path.suffix == ".csv" else "\t")
            if tuple(reader.fieldnames or ()) != columns:
                errors.append(f"{rel}: header does not match required schema")
                continue
            seen_scans = set()
            row_count = 0
            for number, row in enumerate(reader, 2):
                row_count += 1
                if None in row or any(v is None for v in row.values()):
                    errors.append(f"{rel}:{number}: wrong field count")
                    continue
                if rel.endswith("_inventory.csv"):
                    try:
                        scan = int(row["scan"])
                    except ValueError:
                        errors.append(f"{rel}:{number}: nonnumeric scan")
                        continue
                    seen_scans.add(scan)
                    if scan not in SCANS:
                        errors.append(f"{rel}:{number}: out-of-range scan")
                    if row["transcribed"].strip().lower() != "yes":
                        errors.append(f"{rel}:{number}: transcribed is not yes")
                    if row["kind"] not in INVENTORY_KINDS:
                        errors.append(f"{rel}:{number}: unrecognized element kind")
                    if row["sheet_kind"] not in SHEET_KINDS:
                        errors.append(f"{rel}:{number}: unrecognized sheet kind")
                if rel.endswith("_collation.tsv"):
                    try:
                        scan = int(row["our_scan"])
                        their = int(row["their_page"])
                        if scan not in SCANS or their != scan - 1:
                            errors.append(f"{rel}:{number}: scan/page mapping mismatch")
                        folder = "J156-3-04" if scan <= 33 else "J156-3-05"
                        if row["folder"] != folder:
                            errors.append(f"{rel}:{number}: folder mapping mismatch")
                    except ValueError:
                        errors.append(f"{rel}:{number}: nonnumeric scan/page")
                    if row["kind"] not in COLLATION_KINDS:
                        errors.append(f"{rel}:{number}: unrecognized difference kind")
                    if row["confidence"].strip().lower() not in {"high", "medium", "low"}:
                        errors.append(f"{rel}:{number}: invalid confidence")
            if rel.endswith("_inventory.csv") and seen_scans != set(SCANS):
                errors.append(f"{rel}: does not cover all 16 scans")
            if args.final and rel == "CHECK_EVENTS.tsv" and row_count == 0:
                errors.append("CHECK_EVENTS.tsv: no data rows at finalization")

    marker = re.compile(r"\\scanpage\s*\{\s*(\d+)\s*\}")
    cote_marker = re.compile(r"\\cotefile\s*\{([^{}]*)\}")
    for n in SCANS:
        rel = expected_page(n)
        p = root / rel
        if not p.is_file():
            continue
        data = p.read_text(encoding="utf-8")
        clean = without_comments(data)
        if [int(x) for x in marker.findall(clean)] != [n]:
            errors.append(f"{rel}: expected exactly one scanpage marker for scan {n}")
        if n == SCANS[0] and [value.strip() for value in cote_marker.findall(clean)] != ["156-3"]:
            errors.append(f"{rel}: expected exactly one cotefile marker for 156-3 at the first page")
        warnings.extend(f"{rel}: {w}" for w in structural_warnings(data))
    combined = root / f"{STEM}_transcription.tex"
    if combined.is_file():
        data = combined.read_text(encoding="utf-8")
        if [int(x) for x in marker.findall(without_comments(data))] != SCANS:
            errors.append(f"{combined.name}: scanpage markers are not exactly 26 through 41 in order")
        if [value.strip() for value in cote_marker.findall(without_comments(data))] != ["156-3"]:
            errors.append(f"{combined.name}: expected exactly one cotefile marker for 156-3")
        warnings.extend(f"{combined.name}: {w}" for w in structural_warnings(data))
        for n in SCANS:
            p = root / expected_page(n)
            if p.is_file() and p.read_text(encoding="utf-8").strip() not in data:
                warnings.append(f"{combined.name}: scan {n} page fragment is not included verbatim")
    if args.hash_manifest:
        manifest_path = args.hash_manifest
        if not manifest_path.is_absolute():
            manifest_path = root / manifest_path
        try:
            manifest = read_manifest(manifest_path)
            expected_frozen = {expected_page(n) for n in SCANS} | {f"{STEM}_transcription.tex"}
            covered_frozen = set()
            for rel, expected in manifest.items():
                p = (root / rel).resolve()
                if not p.is_relative_to(root):
                    errors.append("hash manifest contains a path outside the work directory")
                    continue
                covered_frozen.add(p.relative_to(root).as_posix())
                if not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
                    errors.append(f"hash manifest: invalid digest for {rel}")
                elif not p.is_file():
                    errors.append(f"hash manifest: missing file {rel}")
                elif hashlib.sha256(p.read_bytes()).hexdigest() != expected.lower():
                    errors.append(f"hash mismatch: {rel}")
            for missing in sorted(expected_frozen - covered_frozen):
                errors.append(f"hash manifest does not cover required frozen file: {missing}")
            print(f"Hash manifest entries checked: {len(manifest)}")
        except (OSError, ValueError, TypeError, StopIteration, AttributeError) as exc:
            errors.append(f"cannot read hash manifest: {exc}")
    for item in errors:
        print("ERROR:", item)
    for item in warnings:
        print("WARNING:", item)
    print(f"Structural validation: {len(errors)} errors; {len(warnings)} warnings.")
    print("No handwriting, mathematics, or witness-reading correctness is certified by this script.")
    return 1 if errors or (warnings and args.warnings_as_errors) else 0


if __name__ == "__main__":
    sys.exit(main())
