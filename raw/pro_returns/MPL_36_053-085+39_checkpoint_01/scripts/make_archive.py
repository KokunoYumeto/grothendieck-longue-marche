#!/usr/bin/env python3
"""Create a new, complete work archive without source scans or attachments.

This utility is deliberately unscheduled. Invoke it only when a checkpoint is
due or when the final deliverable is ready. The output must be outside work.
Existing archive paths are never replaced. Page prose is copied as opaque bytes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
import zipfile


IMAGE_SUFFIXES = {
    ".avif", ".bmp", ".dib", ".eps", ".gif", ".heic", ".heif", ".ico",
    ".jfif", ".jp2", ".jpeg", ".jpg", ".jxl", ".pbm", ".pcx", ".pgm",
    ".png", ".pnm", ".ppm", ".psd", ".raw", ".svg", ".tif", ".tiff",
    ".webp",
}
SOURCE_DIRECTORIES = {"upload", "uploads", "attachments", "scans", "context"}
ATTACHED_FILES = {
    "MPL_36_053-085+39_scans.zip",
    "MPL_36_053-085+39_context.zip",
    "PROMPT(20261116-154459).md",
}


def excluded(relative: Path) -> bool:
    return (
        "__pycache__" in relative.parts
        or relative.suffix.lower() in IMAGE_SUFFIXES
        or relative.suffix.lower() in {".pyc", ".pyo"}
        or relative.parts[0] in SOURCE_DIRECTORIES
        or relative.name in ATTACHED_FILES
    )


def collect_files(root: Path) -> tuple[list[Path], int]:
    files: list[Path] = []
    skipped = 0
    for directory, dirnames, filenames in os.walk(root, followlinks=False):
        here = Path(directory)
        retained_dirs: list[str] = []
        for name in sorted(dirnames):
            candidate = here / name
            if candidate.is_symlink() or excluded(candidate.relative_to(root)):
                skipped += 1
            else:
                retained_dirs.append(name)
        dirnames[:] = retained_dirs
        for name in sorted(filenames):
            candidate = here / name
            if candidate.is_symlink() or excluded(candidate.relative_to(root)):
                skipped += 1
                continue
            if not candidate.is_file():
                raise RuntimeError(f"Unsupported nonregular file: {candidate}")
            files.append(candidate)
    return sorted(files), skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New archive path outside work")
    parser.add_argument(
        "--work", type=Path, default=Path(__file__).resolve().parent.parent,
        help="Work directory; defaults to this script's parent work directory",
    )
    args = parser.parse_args()
    root = args.work.resolve(strict=True)
    if not root.is_dir():
        parser.error("--work must be a directory")
    output = args.output.absolute()
    output.parent.mkdir(parents=True, exist_ok=True)
    output = output.parent.resolve() / output.name
    if output.is_relative_to(root):
        parser.error("output must be outside the work directory")
    if output.suffix.lower() != ".zip":
        parser.error("output must have a .zip extension")
    if os.path.lexists(output):
        parser.error(f"Refusing to overwrite existing path: {output}")
    files, skipped = collect_files(root)
    if not files:
        parser.error("work directory contains no eligible files")
    with tempfile.TemporaryDirectory(prefix=".archive-build-", dir=output.parent) as temporary:
        staging = Path(temporary) / "archive.zip"
        with zipfile.ZipFile(staging, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for source in files:
                before = source.stat()
                archive.write(source, arcname=source.relative_to(root).as_posix())
                after = source.stat()
                if (before.st_size, before.st_mtime_ns, before.st_ino) != (
                    after.st_size, after.st_mtime_ns, after.st_ino
                ):
                    raise RuntimeError(f"File changed while being archived: {source}")
        # Linking installs the complete archive atomically and fails if the
        # destination was created by another process after the earlier check.
        os.link(staging, output)
    digest = hashlib.sha256()
    with output.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    print(json.dumps({
        "archive": str(output), "files": len(files), "excluded_entries": skipped,
        "size_bytes": output.stat().st_size, "sha256": digest.hexdigest(),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
