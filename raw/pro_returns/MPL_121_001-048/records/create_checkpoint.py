#!/usr/bin/env python3
"""Create a fresh, complete checkpoint of this deliverable package.

Usage: python3 records/create_checkpoint.py LAST_SCAN
The input scans and context attachments are deliberately excluded.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile


PACKAGE_NAME = "MPL_121_001-048"
EXCLUDED_DIRECTORIES = {
    "__pycache__", "scans", "sources", "source", "upload", "context",
}
EXCLUDED_FILENAMES = {
    "MPL_121_001-048_scans.zip",
    "MPL_121_001-048_context.zip",
    "PROMPT(20261114-152157).md",
}
IMAGE_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".gif", ".webp",
    ".bmp", ".heic", ".heif", ".avif", ".ico", ".svg",
}


def scan_number(value: str) -> int:
    if not value.isdecimal() or not 1 <= int(value) <= 999:
        raise argparse.ArgumentTypeError("LAST_SCAN must be an integer from 1 to 999")
    return int(value)


def include_path(relative: Path) -> bool:
    return (
        not any(part in EXCLUDED_DIRECTORIES for part in relative.parts[:-1])
        and relative.name not in EXCLUDED_FILENAMES
        and relative.suffix.lower() not in IMAGE_SUFFIXES | {".pyc"}
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("last_scan", type=scan_number)
    args = parser.parse_args()

    package = Path(__file__).resolve().parents[1]
    if package.name != PACKAGE_NAME:
        raise SystemExit(f"Unexpected package directory: {package}")
    output = package.parent / f"{PACKAGE_NAME}_checkpoint_{args.last_scan:03d}.zip"

    files = []
    for path in sorted(package.rglob("*")):
        relative = path.relative_to(package)
        if not include_path(relative):
            continue
        if path.is_symlink():
            raise SystemExit(f"Refusing to archive a symbolic link: {relative}")
        if path.is_file():
            files.append((path, relative.as_posix()))

    if not files:
        raise SystemExit("The package contains no checkpoint files")

    # A new ZIP is constructed every time: deleted drafts and other removed
    # files cannot survive as old entries from an earlier archive.
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{output.stem}_", suffix=".tmp", dir=output.parent
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for path, archive_name in files:
                archive.write(path, arcname=archive_name)
        with ZipFile(temporary) as archive:
            damaged = archive.testzip()
            if damaged is not None:
                raise RuntimeError(f"Checkpoint verification failed: {damaged}")
            if archive.namelist() != [name for _, name in files]:
                raise RuntimeError("Checkpoint entry list differs from the input file list")
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)

    print(f"Checkpoint created: {output}")
    print(f"Files: {len(files)}")
    print(f"ZIP bytes: {output.stat().st_size}")


if __name__ == "__main__":
    main()
