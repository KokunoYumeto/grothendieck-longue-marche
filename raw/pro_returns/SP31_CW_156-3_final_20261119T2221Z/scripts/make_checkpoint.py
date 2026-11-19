#!/usr/bin/env python3
"""Create one immutable checkpoint ZIP; timing and external saving are caller's job.

Only files below --out are included. Prior archives, source input directories,
symlinks and Python bytecode caches are excluded. The archive contains paths
relative to --out. This script neither changes progress.log nor saves remotely.
It never overwrites an existing checkpoint and never creates an earlier number.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

PREFIX = "SP31_CW_156-3"
SOURCE_DIR_NAMES = {"source", "upload", "uploads", "attachments", "scans", "witnesses", "context", "sweep3"}


def excluded(relative: Path) -> bool:
    if relative.suffix.lower() == ".zip":
        return True
    for part in relative.parts:
        lower = part.lower()
        if lower in SOURCE_DIR_NAMES or lower == "__pycache__":
            return True
        if lower.startswith(PREFIX.lower() + "_") and lower.endswith(("_scans", "_witnesses", "_context", "_sweep3")):
            return True
    return relative.suffix.lower() in {".pyc", ".pyo"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dest", type=Path, required=True)
    parser.add_argument("--number", type=int, help="Omit to allocate the next number; specified number must be next.")
    args = parser.parse_args()
    out, dest = args.out.resolve(), args.dest.resolve()
    if not out.is_dir():
        parser.error(f"output directory does not exist: {out}")
    dest.mkdir(parents=True, exist_ok=True)
    pattern = re.compile(re.escape(PREFIX) + r"_checkpoint_(\d+)\.zip$")
    numbers = [int(m.group(1)) for p in dest.iterdir() if (m := pattern.fullmatch(p.name))]
    next_number = max(numbers, default=0) + 1
    number = next_number if args.number is None else args.number
    if number != next_number:
        parser.error(f"next checkpoint number must be {next_number:02d}; refusing {number:02d}")
    archive = dest / f"{PREFIX}_checkpoint_{number:02d}.zip"
    files = [p for p in sorted(out.rglob("*")) if p.is_file() and not p.is_symlink() and not excluded(p.relative_to(out))]
    # Symlinked ancestors are also prohibited: rglob implementations vary.
    files = [p for p in files if not any(parent.is_symlink() for parent in p.parents if parent != out and out in parent.parents)]
    if not files:
        parser.error("no deliverable or documentation files found")
    count, size = 0, 0
    # 'x' is exclusive creation; an earlier checkpoint can never be replaced.
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for path in files:
            data = path.read_bytes()
            rel = path.relative_to(out).as_posix()
            z.writestr(rel, data)
            count += 1
            size += len(data)
    print(json.dumps({"archive": str(archive), "number": number, "files": count, "uncompressed_bytes": size,
                      "archive_bytes": archive.stat().st_size, "sha256": hashlib.sha256(archive.read_bytes()).hexdigest()}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
