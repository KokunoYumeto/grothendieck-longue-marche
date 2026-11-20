#!/usr/bin/env python3
"""Create a new deliverable ZIP without replacing any existing archive.

Usage: python scripts/package_delivery.py /absolute/path/SP65_C13_16.zip

This script packages local files only. It performs no upload and does not
schedule or initiate checkpoints. Call it at the authorized checkpoint time
or when the final deliverable is ready. Archive paths are relative to the
deliverable directory, with no extra enclosing folder.
"""

from __future__ import annotations

import argparse
import os
import sys
import zipfile
from pathlib import Path


EXCLUDED_SUFFIXES = {
    ".zip", ".pyc", ".pyo", ".png", ".jpg", ".jpeg", ".jpe", ".jfif",
    ".gif", ".tif", ".tiff", ".bmp", ".webp", ".svg", ".svgz",
    ".heic", ".heif", ".avif", ".ico", ".icns", ".pnm", ".ppm",
    ".pgm", ".pbm", ".pam", ".psd", ".xcf", ".eps", ".ps", ".pdf",
}
EXCLUDED_DIRECTORIES = {
    "__pycache__", ".cache", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".git", ".ipynb_checkpoints", "node_modules",
}
EXCLUDED_NAMES = {".DS_Store", "Thumbs.db"}


def collect_files(root: Path):
    """Yield documented deliverables, scripts, and records in stable order."""
    for directory, subdirectories, names in os.walk(root, followlinks=False):
        parent = Path(directory)
        subdirectories[:] = sorted(
            name for name in subdirectories if name not in EXCLUDED_DIRECTORIES
        )
        for name in subdirectories:
            path = parent / name
            if path.is_symlink():
                raise ValueError(f"Refusing symlink directory: {path}")
        for name in sorted(names):
            path = parent / name
            if path.suffix.lower() in EXCLUDED_SUFFIXES or name in EXCLUDED_NAMES:
                continue
            if path.is_symlink():
                raise ValueError(f"Refusing symlink file: {path}")
            if path.is_file():
                yield path


def create_archive(root: Path, output: Path) -> tuple[int, int]:
    if not output.is_absolute():
        raise ValueError("The output path must be absolute")
    if output.suffix.lower() != ".zip":
        raise ValueError("The output filename must end in .zip")
    if not root.is_dir():
        raise ValueError(f"Deliverable directory does not exist: {root}")
    if not output.parent.is_dir():
        raise ValueError(f"Output directory does not exist: {output.parent}")
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"Refusing to overwrite: {output}")
    paths = list(collect_files(root))
    if not paths:
        raise ValueError("The deliverable directory contains no eligible files")
    # Exclusive creation is also enforced by the OS, after the explanatory check.
    with output.open("xb") as handle:
        try:
            with zipfile.ZipFile(handle, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
                for path in paths:
                    archive.write(path, path.relative_to(root).as_posix())
            handle.flush()
            os.fsync(handle.fileno())
        except BaseException:
            # Preserve an interrupted archive under its new name. This script
            # never deletes, renames, or overwrites an earlier checkpoint.
            raise
    with zipfile.ZipFile(output, "r") as archive:
        damaged = archive.testzip()
        if damaged is not None:
            raise ValueError(f"Created archive failed CRC verification: {damaged}")
    return len(paths), output.stat().st_size


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output", type=Path, help="Absolute path of a new ZIP; existing files are rejected")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Deliverable directory (default: parent of scripts)")
    args = parser.parse_args()
    try:
        count, size = create_archive(args.root.resolve(), args.output)
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"Archive creation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Created {args.output}: {count} files, {size:,} bytes; CRC verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
