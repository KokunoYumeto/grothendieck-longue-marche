#!/usr/bin/env python3
"""Mechanical assembly, validation, freezing, and packaging.

This script neither reads images nor certifies a visual transcription or audit.
Run commands explicitly; it does not schedule or upload checkpoints.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

STEM = "MPL_58_020-067"
SCANS = tuple(n for n in range(20, 68) if n not in {29, 45, 55, 64})
HEADER = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
EXCLUDED_DIRS = {
    ".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "node_modules", "scans", "upload", "context", "sources", "input", "inputs",
}


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def pages(root: Path) -> list[Path]:
    return [root / "pages" / f"{STEM}_58_scan{n:03d}.tex" for n in SCANS]


def combined(root: Path) -> Path:
    return root / f"{STEM}_transcription.tex"


def manifest(root: Path) -> Path:
    return root / "records" / "frozen_sha256.json"


def check_pages(root: Path) -> list[Path]:
    expected = pages(root)
    missing = [str(p.relative_to(root)) for p in expected if not p.is_file()]
    unexpected = sorted(
        str(p.relative_to(root))
        for p in (root / "pages").glob("*.tex") if p not in expected
    )
    if missing or unexpected:
        raise ValueError(f"Page-file mismatch: missing={missing}; unexpected={unexpected}")
    empty = [str(p.relative_to(root)) for p in expected if p.stat().st_size == 0]
    if empty:
        raise ValueError(f"Empty page files: {empty}")
    return expected


def assembled_bytes(root: Path) -> bytes:
    # Byte-for-byte concatenation: no newline, header, or content is inserted.
    return b"".join(p.read_bytes() for p in check_pages(root))


def validate(root: Path) -> dict:
    expected = assembled_bytes(root)
    actual = combined(root).read_bytes()
    if actual != expected:
        raise ValueError("Combined fragment differs from exact ordered concatenation")
    inventory = root / f"{STEM}_inventory.csv"
    with inventory.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADER:
            raise ValueError(f"Inventory header must be exactly {HEADER!r}")
        rows = list(reader)
    seen: set[int] = set()
    identities: set[tuple[str, int, str]] = set()
    for line, row in enumerate(rows, start=2):
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"Malformed CSV field count on line {line}")
        if row["cote"] != "58":
            raise ValueError(f"Unexpected cote on inventory line {line}")
        try:
            scan = int(row["scan"])
        except ValueError as e:
            raise ValueError(f"Invalid scan on inventory line {line}") from e
        if scan not in SCANS:
            raise ValueError(f"Unexpected scan {scan} on inventory line {line}")
        if row["transcribed"] != "yes":
            raise ValueError(f"transcribed is not exactly yes on inventory line {line}")
        if row["sheet_kind"] not in SHEET_KINDS:
            raise ValueError(f"Invalid sheet_kind on inventory line {line}")
        if row["kind"] not in ELEMENT_KINDS:
            raise ValueError(f"Invalid kind on inventory line {line}")
        if not row["element"]:
            raise ValueError(f"Empty element identifier on inventory line {line}")
        identity = (row["cote"], scan, row["element"])
        if identity in identities:
            raise ValueError(f"Duplicate element identifier on inventory line {line}")
        identities.add(identity)
        seen.add(scan)
    if seen != set(SCANS):
        raise ValueError(f"Inventory missing scans: {sorted(set(SCANS) - seen)}")
    return {"page_files": len(SCANS), "inventory_rows": len(rows), "combined_bytes": len(actual)}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def freeze(root: Path, append_log: bool) -> dict:
    result = validate(root)
    destination = manifest(root)
    if destination.exists():
        raise ValueError("Freeze manifest already exists; use verify, never overwrite the freeze")
    frozen_at = utc()
    hashes = {
        str(p.relative_to(root)): sha256(p)
        for p in [*pages(root), combined(root)]
    }
    data = {"frozen_at": frozen_at, "algorithm": "SHA-256", "files": hashes}
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation also guards against accidental concurrent refreezing.
    with destination.open("x", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    if append_log:
        with (root / "progress.log").open("a", encoding="utf-8") as f:
            for name, digest in hashes.items():
                f.write(f"SHA-256 {digest}  {name}\n")
            f.write(f"transcription frozen {frozen_at}\n")
    return {**result, "frozen_at": frozen_at, "manifest": str(destination), "log_appended": append_log}


def verify(root: Path, append_log: bool) -> dict:
    result = validate(root)
    data = json.loads(manifest(root).read_text(encoding="utf-8"))
    expected_names = {str(p.relative_to(root)) for p in [*pages(root), combined(root)]}
    if data.get("algorithm") != "SHA-256" or set(data.get("files", {})) != expected_names:
        raise ValueError("Freeze manifest has an unexpected algorithm or file set")
    differences = []
    for name, old_hash in data["files"].items():
        path = root / name
        if not path.is_file() or sha256(path) != old_hash:
            differences.append(name)
    if differences:
        raise ValueError(f"Frozen files changed or disappeared: {differences}")
    checked_at = utc()
    if append_log:
        with (root / "progress.log").open("a", encoding="utf-8") as f:
            f.write(f"frozen SHA-256 hashes unchanged ({len(expected_names)} files) {checked_at}\n")
    return {**result, "frozen_hashes_unchanged": len(expected_names), "verified_at": checked_at}


def pack(root: Path, output: Path, checkpoint: int | None) -> dict:
    root = root.resolve()
    output = output.resolve()
    if checkpoint is not None and checkpoint < 1:
        raise ValueError("Checkpoint number must be positive")
    required_name = (
        f"{STEM}_checkpoint_{checkpoint:02d}.zip"
        if checkpoint is not None else f"{STEM}.zip"
    )
    if output.name != required_name:
        raise ValueError(f"Output filename must be {required_name}")
    if output.exists():
        raise ValueError("Output ZIP already exists; existing ZIPs are never overwritten")
    if checkpoint is None:
        verify(root, append_log=False)
        required = [
            root / f"{STEM}_doubts.md", root / f"{STEM}_notes.md", root / "progress.log",
        ]
        absent = [str(p.relative_to(root)) for p in required if not p.is_file()]
        if absent:
            raise ValueError(f"Missing final deliverables: {absent}")
    selected: list[Path] = []
    excluded: list[str] = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if path.is_symlink():
            raise ValueError(f"Refusing symlink in work directory: {rel}")
        if not path.is_file():
            continue
        if (any(part in EXCLUDED_DIRS for part in rel.parts)
                or path.suffix.lower() in {".zip", ".pyc", ".pyo"}
                or re.fullmatch(r"MPL_58_020-067_58_scan\d+(?:_[ab])?\.jpe?g", path.name)):
            excluded.append(str(rel))
            continue
        selected.append(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for path in selected:
                z.write(path, arcname=str(path.relative_to(root)))
    except Exception:
        if output.exists():
            output.unlink()
        raise
    return {
        "zip": str(output), "members": len(selected), "bytes": output.stat().st_size,
        "sha256": sha256(output), "excluded": excluded,
        "warning": "No upload, scheduling, visual audit, or editorial completeness certification was performed.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="Check all expected page filenames and nonempty files")
    sub.add_parser("assemble", help="Write exact ordered byte concatenation; refuses a frozen transcription")
    sub.add_parser("validate", help="Check filenames, exact concatenation, and inventory structure/coverage")
    for command in ("freeze", "verify"):
        p = sub.add_parser(command)
        p.add_argument("--append-log", action="store_true", help="Explicitly append this operation's result to progress.log")
    p = sub.add_parser("zip", help="Create final or explicitly numbered hourly-checkpoint ZIP; no upload")
    p.add_argument("output", type=Path)
    p.add_argument("--checkpoint", type=int, default=None)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "check":
            result = {"page_files": len(check_pages(root))}
        elif args.command == "assemble":
            if manifest(root).exists():
                raise ValueError("Transcription is frozen; assembly is disabled")
            content = assembled_bytes(root)
            combined(root).write_bytes(content)
            result = {"combined": str(combined(root)), "bytes": len(content)}
        elif args.command == "validate":
            result = validate(root)
        elif args.command == "freeze":
            result = freeze(root, args.append_log)
        elif args.command == "verify":
            result = verify(root, args.append_log)
        else:
            result = pack(root, args.output, args.checkpoint)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, csv.Error, json.JSONDecodeError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
