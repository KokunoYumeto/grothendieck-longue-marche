#!/usr/bin/env python3
"""Structural checks, ordered assembly, and a SHA-256 freeze for MPL_67_002-052.

This utility reads deliverable text only when explicitly invoked. It does not
read source images or context, perform OCR, assess readings, or create audit
events. A successful structural check does not certify diplomatic completeness.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import sys

PACKAGE = "MPL_67_002-052"
SCANS = tuple(n for n in range(2, 53) if n not in {15, 22, 23, 47, 52})
HEADER = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note",
                 "insertion", "deletion"}
CHECK_HEADER = ["statement_id", "date", "who_model_effort_run", "type", "outcome"]
PAGE_RE = re.compile(r"MPL_67_002-052_67_scan(\d{3})\.tex")
DEFAULT_ROOT = Path(__file__).resolve().parent.parent


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_path(root: Path, scan: int) -> Path:
    return root / "pages" / f"{PACKAGE}_67_scan{scan:03d}.tex"


def combined_path(root: Path) -> Path:
    return root / f"{PACKAGE}_transcription.tex"


def manifest_path(root: Path) -> Path:
    return root / "records" / "transcription.sha256"


def inventory_errors(root: Path, scans: set[int]) -> list[str]:
    errors: list[str] = []
    path = root / f"{PACKAGE}_inventory.csv"
    if not path.is_file():
        return [f"Missing {path.name}"]
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != HEADER:
            return [f"Inventory columns differ from required header: {reader.fieldnames!r}"]
        seen: set[int] = set()
        for rownum, row in enumerate(reader, 2):
            prefix = f"Inventory row {rownum}: "
            if row.get("cote") != "67":
                errors.append(prefix + "cote must be 67")
            try:
                scan = int(row.get("scan", ""))
            except (TypeError, ValueError):
                errors.append(prefix + "invalid scan")
                continue
            seen.add(scan)
            if scan not in scans:
                errors.append(prefix + f"no corresponding completed page for scan {scan}")
            if row.get("sheet_kind") not in SHEET_KINDS:
                errors.append(prefix + "unknown sheet_kind")
            if row.get("kind") not in ELEMENT_KINDS:
                errors.append(prefix + "unknown element kind")
            if row.get("transcribed") != "yes":
                errors.append(prefix + "transcribed must be yes")
            for key in ("element", "position", "first_words_or_objects"):
                if not row.get(key):
                    errors.append(prefix + f"empty {key}")
            if None in row:
                errors.append(prefix + "extra CSV fields")
        for scan in sorted(scans - seen):
            errors.append(f"No inventory rows for scan {scan:03d}")
    return errors


def validate(root: Path, *, partial: bool = False, final: bool = False,
             require_combined: bool = False) -> list[str]:
    errors: list[str] = []
    scans: set[int] = set()
    for path in sorted((root / "pages").glob("*.tex")):
        match = PAGE_RE.fullmatch(path.name)
        if not match:
            errors.append(f"Unexpected page filename: {path.name}")
            continue
        scan = int(match.group(1))
        scans.add(scan)
        if scan not in SCANS:
            errors.append(f"Unexpected scan page: {scan:03d}")
        content = path.read_text(encoding="utf-8")
        markers = re.findall(r"\\scanpage\{(\d+)\}", content)
        if markers != [str(scan)]:
            errors.append(f"Incorrect scanpage marker(s) in {path.name}: {markers!r}")
        if not content.strip():
            errors.append(f"Empty page: {path.name}")
        if re.search(r"\\(?:documentclass|begin\{document\})", content):
            errors.append(f"Unexpected document wrapper: {path.name}")
    if not partial and scans != set(SCANS):
        errors.append("Missing pages: " + ", ".join(f"{n:03d}" for n in sorted(set(SCANS)-scans)))
    if partial and scans:
        prefix = set(SCANS[:len(scans)])
        if scans != prefix:
            errors.append("Completed pages do not form an ascending prefix of the required scans")
    errors.extend(inventory_errors(root, scans))
    required = ["progress.log", f"{PACKAGE}_doubts.md", "CHECK_EVENTS.tsv"]
    if final:
        required += [f"{PACKAGE}_notes.md", "records/transcription.sha256"]
    for name in required:
        path = root / name
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty required file: {name}")
    check_events = root / "CHECK_EVENTS.tsv"
    if check_events.is_file():
        with check_events.open(newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle, delimiter="\t")
            actual_header = next(reader, [])
            if actual_header != CHECK_HEADER:
                errors.append(f"Unexpected CHECK_EVENTS.tsv header: {actual_header!r}")
            for rownum, row in enumerate(reader, 2):
                if len(row) != len(CHECK_HEADER):
                    errors.append(f"CHECK_EVENTS.tsv row {rownum} has {len(row)} columns")
    if scans and 2 in scans:
        first = page_path(root, 2).read_text(encoding="utf-8")
        if not re.match(r"\s*\\cotefile\{67\}\s*\\scanpage\{2\}", first):
            errors.append("The first page must start with cotefile{67} followed by scanpage{2}")
    if require_combined or final:
        combined = combined_path(root)
        if not combined.is_file():
            errors.append(f"Missing {combined.name}")
        elif scans == set(SCANS):
            expected = b"".join(page_path(root, n).read_bytes() for n in SCANS)
            if combined.read_bytes() != expected:
                errors.append("Combined transcription differs from exact ordered concatenation of page files")
    return errors


def require_valid(root: Path, **kwargs: bool) -> None:
    errors = validate(root, **kwargs)
    if errors:
        raise ValueError("\n".join(errors))


def assemble(root: Path) -> None:
    if manifest_path(root).exists():
        raise ValueError("A freeze manifest already exists; assembly is blocked")
    require_valid(root)
    combined_path(root).write_bytes(b"".join(page_path(root, n).read_bytes() for n in SCANS))
    print(f"Assembled {len(SCANS)} pages: {combined_path(root)}")


def freeze(root: Path) -> None:
    require_valid(root, require_combined=True)
    manifest = manifest_path(root)
    if manifest.exists():
        raise ValueError("Freeze manifest already exists; use verify-freeze")
    log = root / "progress.log"
    log_text = log.read_text(encoding="utf-8")
    if "context opened " in log_text:
        raise ValueError("The log already records opening the context")
    audited = set(int(n) for n in re.findall(r"^scan (\d{3}) audited ", log_text, re.MULTILINE))
    missing = set(SCANS) - audited
    if missing:
        raise ValueError("Missing reader-recorded audit events: " + ", ".join(f"{n:03d}" for n in sorted(missing)))
    files = [page_path(root, n) for n in SCANS] + [combined_path(root)]
    lines = [f"{sha256(path)}  {path.relative_to(root).as_posix()}" for path in files]
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    with log.open("a", encoding="utf-8") as handle:
        for line in lines:
            handle.write("sha256 " + line + "\n")
        handle.write("transcription frozen " + utc() + "\n")
    print(f"Frozen {len(files)} files; source page files were not changed")


def verify_freeze(root: Path, *, record: bool = False) -> None:
    manifest = manifest_path(root)
    expected_paths = {page_path(root, n).relative_to(root).as_posix() for n in SCANS}
    expected_paths.add(combined_path(root).relative_to(root).as_posix())
    actual_paths: set[str] = set()
    errors: list[str] = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        actual_paths.add(relative)
        if relative not in expected_paths:
            errors.append(f"Unexpected manifest path: {relative}")
            continue
        path = root / relative
        if not path.is_file() or sha256(path) != digest:
            errors.append(f"Hash mismatch: {relative}")
    if actual_paths != expected_paths:
        errors.append("Manifest does not contain exactly the 46 pages and combined transcription")
    if errors:
        raise ValueError("\n".join(errors))
    if record:
        with (root / "progress.log").open("a", encoding="utf-8") as handle:
            handle.write("frozen hashes unchanged " + utc() + "\n")
    print("All 47 frozen SHA-256 hashes are unchanged")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "assemble", "freeze", "verify-freeze"))
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--partial", action="store_true", help="Validate completed ascending prefix only")
    parser.add_argument("--final", action="store_true", help="Require research notes, combined file, and freeze manifest")
    parser.add_argument("--record", action="store_true", help="Record a successful hash verification in progress.log")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "validate":
            require_valid(root, partial=args.partial, final=args.final)
            print("Structural validation passed; reading accuracy was not assessed")
        elif args.command == "assemble":
            assemble(root)
        elif args.command == "freeze":
            freeze(root)
        else:
            verify_freeze(root, record=args.record)
    except (OSError, ValueError, csv.Error) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
