#!/usr/bin/env python3
"""Package allowed regular output files without overwriting an existing ZIP.

Usage:
    python package_deliverable.py OUT_DIR ZIP_PATH

Archive member paths are relative to OUT_DIR.  This helper excludes __pycache__
and input/inputs/scan/scans/witness/witnesses directories at any depth (case
insensitive); .pyc and .zip files; known image formats; and PDF scan documents.
It excludes symlinks and other nonregular filesystem entries.  Files are included
in sorted path order.  Source files and logs are never modified.

The file-type exclusion is extension based, not a provenance or content audit.
No TeX is compiled, no scripts are executed, and no existing archive is replaced.
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
from pathlib import Path
import stat
import sys
import zipfile


EXCLUDED_DIRECTORIES = {
    "__pycache__", "input", "inputs", "scan", "scans", "witness", "witnesses",
}
IMAGE_SUFFIXES = {
    ".ai", ".apng", ".arw", ".avif", ".bmp", ".cr2", ".cr3", ".cur",
    ".dib", ".dng", ".emf", ".eps", ".exr", ".gif", ".hdr", ".heic",
    ".heif", ".icns", ".ico", ".j2c", ".j2k", ".jfi", ".jfif", ".jif",
    ".jp2", ".jpe", ".jpeg", ".jpf", ".jpg", ".jpm", ".jpx", ".jxl",
    ".mj2", ".nef", ".nrw", ".orf", ".pbm", ".pcx", ".pef", ".pgm",
    ".png", ".pnm", ".ppm", ".psd", ".ras", ".raw", ".rw2", ".sgi",
    ".srw", ".svg", ".svgz", ".tga", ".tif", ".tiff", ".wbmp",
    ".webp", ".wmf", ".xbm", ".xcf", ".xpm",
}
EXCLUDED_SUFFIXES = IMAGE_SUFFIXES | {".pdf", ".pyc", ".zip"}


def collect_files(output_dir: Path) -> tuple[list[Path], dict[str, int]]:
    """Enumerate paths and metadata only; packaging reads the selected bytes."""
    files: list[Path] = []
    excluded: collections.Counter[str] = collections.Counter()

    def walk_error(error: OSError) -> None:
        raise error

    for current, directory_names, file_names in os.walk(
        output_dir, topdown=True, followlinks=False, onerror=walk_error
    ):
        parent = Path(current)
        kept_directories = []
        for name in sorted(directory_names):
            path = parent / name
            if name.casefold() in EXCLUDED_DIRECTORIES:
                excluded["excluded_directories"] += 1
            elif path.is_symlink():
                excluded["symlinks"] += 1
            else:
                kept_directories.append(name)
        directory_names[:] = kept_directories

        for name in sorted(file_names):
            path = parent / name
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                excluded["symlinks"] += 1
            elif not stat.S_ISREG(mode):
                excluded["nonregular_entries"] += 1
            elif path.suffix.casefold() in EXCLUDED_SUFFIXES:
                excluded["excluded_file_extensions"] += 1
            else:
                files.append(path)

    files.sort(key=lambda path: path.relative_to(output_dir).as_posix())
    return files, dict(sorted(excluded.items()))


def package(output_dir: Path, archive_path: Path) -> dict[str, object]:
    output_dir = output_dir.expanduser().resolve(strict=True)
    archive_path = archive_path.expanduser().absolute()
    if not output_dir.is_dir():
        raise ValueError("OUT_DIR must be a directory.")
    if archive_path.suffix.casefold() != ".zip":
        raise ValueError("ZIP_PATH must have a .zip extension.")
    # lexists also catches dangling symlinks.  Exclusive creation below provides
    # the actual no-overwrite guarantee if another process creates the path.
    if os.path.lexists(archive_path):
        raise FileExistsError(f"Refusing to overwrite existing ZIP path: {archive_path}")

    files, excluded = collect_files(output_dir)
    if not files:
        raise ValueError("No eligible regular files were found; no ZIP was created.")
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with archive_path.open("xb") as output_stream:
            created = True
            with zipfile.ZipFile(
                output_stream,
                mode="w",
                compression=zipfile.ZIP_DEFLATED,
                compresslevel=9,
                allowZip64=True,
                strict_timestamps=False,
            ) as archive:
                for path in files:
                    # Do not follow a symlink substituted after enumeration.
                    if not stat.S_ISREG(path.lstat().st_mode):
                        raise ValueError(f"Selected path is no longer a regular file: {path}")
                    archive.write(path, arcname=path.relative_to(output_dir).as_posix())
    except BaseException:
        if created:
            try:
                archive_path.unlink()
            except OSError:
                pass
        raise

    return {
        "archive": str(archive_path),
        "output_directory": str(output_dir),
        "included_regular_files": len(files),
        "excluded": excluded,
        "archive_bytes": archive_path.stat().st_size,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output_dir", type=Path, help="Directory containing the output files to package.")
    parser.add_argument("zip_path", type=Path, help="New .zip path; an existing path is never overwritten.")
    args = parser.parse_args()
    try:
        report = package(args.output_dir, args.zip_path)
    except (OSError, ValueError, zipfile.BadZipFile, RuntimeError) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
