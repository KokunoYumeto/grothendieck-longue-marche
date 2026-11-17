#!/usr/bin/env python3
"""Create one hourly, non-overwriting ZIP checkpoint when explicitly invoked.

This is an archive builder, not a scheduler or an uploader. It never opens the
scan/context archives, interprets text, or modifies transcription deliverables.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

PREFIX = "MPL_12_099-149"
FIRST_DUE = datetime(2026, 11, 17, 20, 43, 18, tzinfo=timezone.utc)
HOUR = timedelta(hours=1)
EXCLUDED_DIRS = {
    "input", "inputs", "upload", "uploads", "scans", "scan", "images",
    "crops", "crop", "context", "contexts", "hua_project", "checkpoints", "__pycache__",
    ".git", ".pytest_cache", ".mypy_cache", ".venv", "venv", "node_modules",
}
EXCLUDED_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff", ".bmp",
    ".heic", ".avif", ".svg", ".zip", ".pyc", ".pyo",
}
ARCHIVE_NAME = re.compile(re.escape(PREFIX) + r"_checkpoint_(\d{2,})\.zip$")
SOURCE_BASENAMES = {
    "MPL_16+47+54+44_doubts.md", "MPL_16+47+54+44_notes.md",
    "MPL_16+47+54+44_transcription.tex",
    "Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf", "RESULTS_STATE.md",
}


def stamp(value: datetime) -> str:
    return value.strftime("%Y-%m-%d %H:%M:%S UTC")


def included(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    if any(part.lower() in EXCLUDED_DIRS for part in relative.parts[:-1]):
        return False
    if any("context" in part.lower() or "scans" in part.lower() for part in relative.parts[:-1]):
        return False
    if path.name in SOURCE_BASENAMES:
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    if path.name.startswith("PROMPT(") and path.suffix.lower() == ".md":
        return False
    return True


def previous_checkpoints(directory: Path) -> list[tuple[int, Path]]:
    entries = []
    if directory.exists():
        for path in directory.iterdir():
            match = ARCHIVE_NAME.fullmatch(path.name)
            if match and path.is_file():
                entries.append((int(match.group(1)), path))
    entries.sort()
    if entries and [n for n, _ in entries] != list(range(1, entries[-1][0] + 1)):
        raise RuntimeError("Existing checkpoint numbers are not consecutive; no archive was created")
    return entries


def creation_time(path: Path) -> datetime:
    with zipfile.ZipFile(path) as archive:
        comment = archive.comment.decode("ascii")
    match = re.search(r"created_utc=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC)", comment)
    if match:
        return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    # Support an earlier checkpoint created outside this script without reading
    # any archived page bytes. Upload xattrs do not change file modification time.
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)


def create(root: Path, destination: Path) -> dict:
    root, destination = root.resolve(), destination.resolve()
    if not root.is_dir():
        raise RuntimeError("Bundle directory does not exist")
    if destination == root or root in destination.parents:
        raise RuntimeError("Checkpoint output directory must be outside the bundle")
    now = datetime.now(timezone.utc)
    previous = previous_checkpoints(destination)
    number = previous[-1][0] + 1 if previous else 1
    earliest = FIRST_DUE
    if previous:
        earliest = max(earliest, creation_time(previous[-1][1]) + HOUR)
    if now < earliest:
        raise RuntimeError(f"Next hourly checkpoint is not due before {stamp(earliest)}")

    candidates = []
    for path in sorted(root.rglob("*")):
        if not included(path, root):
            continue
        if path.is_symlink():
            raise RuntimeError(f"Symlink refused: {path.relative_to(root).as_posix()}")
        if path.is_file():
            stat = path.stat()
            candidates.append((path, stat.st_size, stat.st_mtime_ns))
    if not candidates:
        raise RuntimeError("No eligible deliverables or records to checkpoint")

    destination.mkdir(parents=True, exist_ok=True)
    final = destination / f"{PREFIX}_checkpoint_{number:02d}.zip"
    if final.exists():
        raise RuntimeError("Checkpoint target already exists; overwriting is forbidden")
    descriptor, temporary_name = tempfile.mkstemp(prefix=".checkpoint_build_", suffix=".zip", dir=destination)
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            archive.comment = (
                f"{PREFIX}; checkpoint={number:02d}; created_utc={stamp(now)}; "
                "complete work bundle; supplied inputs excluded"
            ).encode("ascii")
            for path, _, _ in candidates:
                archive.write(path, arcname=path.relative_to(root).as_posix())
        for path, size, modified in candidates:
            current = path.stat()
            if (current.st_size, current.st_mtime_ns) != (size, modified):
                raise RuntimeError("A work file changed during checkpoint creation; partial archive discarded")
        with zipfile.ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise RuntimeError("Checkpoint ZIP failed its CRC check")
        # Atomic publication with exclusive creation; unlike rename/replace,
        # link cannot overwrite an existing checkpoint of the same number.
        os.link(temporary, final)
        digest = hashlib.sha256(final.read_bytes()).hexdigest()
    finally:
        temporary.unlink(missing_ok=True)
    return {
        "checkpoint": number,
        "path": str(final),
        "created_utc": stamp(now),
        "next_due_utc": stamp(now + HOUR),
        "included_files": len(candidates),
        "size_bytes": final.stat().st_size,
        "sha256": digest,
        "uploaded": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output-directory", type=Path)
    args = parser.parse_args()
    destination = args.output_directory or args.root.resolve().parent / "checkpoints"
    try:
        result = create(args.root, destination)
    except (OSError, RuntimeError, ValueError, zipfile.BadZipFile) as error:
        print(json.dumps({"created": False, "error": str(error)}))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
