#!/usr/bin/env python3
"""Create a new, image-free checkpoint or final SP71_C13_142 ZIP.

No manuscript reading, recognition, TeX compilation, or report generation is
performed. All eligible deliverables and documentation under the work root are
included, including this helper. Original sources, images, caches and every
existing ZIP are excluded. Existing output names are never overwritten.

Examples (run only when the root reader decides packaging is due):
    python -B scripts/package_bundle.py --checkpoint 1
    python -B scripts/package_bundle.py --final
    python -B scripts/package_bundle.py --checkpoint 1 --list

--list examines paths and metadata only and never creates an archive. Scheduling
and persistent saving are deliberately left to the root reader.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


PREFIX = "SP71_C13_142"
EXCLUDED_SUFFIXES = {
    ".zip", ".tar", ".tgz", ".gz", ".bz2", ".xz", ".7z", ".rar",
    ".jpg", ".jpeg", ".jpe", ".jfif", ".jp2", ".j2k", ".jxl", ".png",
    ".gif", ".tif", ".tiff", ".bmp", ".webp", ".svg", ".pdf", ".ps",
    ".eps", ".heic", ".heif", ".avif", ".ppm", ".pgm", ".pbm", ".pnm",
    ".ico", ".raw", ".dng", ".psd", ".xcf", ".pyc", ".pyo",
    ".aux", ".out", ".synctex", ".fls", ".fdb_latexmk", ".tmp", ".part",
}
EXCLUDED_COMPONENTS = {
    "source", "sources", "upload", "uploads", "hua", "witnesses", "scans",
    "images", "crops", "halves", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".git", "node_modules", ".venv", "venv",
}
EXCLUDED_FILENAMES = {"marks.tsv", "preamble.tex", ".ds_store", "thumbs.db"}


def exclusion_reason(relative: str) -> str | None:
    path = PurePosixPath(relative)
    parts = tuple(p.lower() for p in path.parts)
    if path.is_absolute() or ".." in path.parts:
        return "unsafe relative path"
    if any(p in EXCLUDED_COMPONENTS for p in parts):
        return "source, image, or cache directory"
    if any(p.endswith(("_scans", "_texts")) for p in parts):
        return "original attachment directory"
    if any(p.startswith(".") for p in parts):
        return "hidden metadata or temporary path"
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return "archive, image, cache, or temporary file"
    if path.name.lower() in EXCLUDED_FILENAMES or path.name.lower().startswith("hua_"):
        return "original witness/source text"
    if path.name.upper().startswith("PROMPT(") and path.suffix.lower() == ".md":
        return "original prompt attachment"
    return None


def scan_tree(root: Path):
    """Return sorted regular files and exclusions without opening any content."""
    included = []
    excluded = []
    for directory, dirnames, filenames in os.walk(root, followlinks=False):
        base = Path(directory)
        keep_dirs = []
        for name in sorted(dirnames):
            path = base / name
            relative = path.relative_to(root).as_posix()
            reason = "symbolic link" if path.is_symlink() else exclusion_reason(relative)
            if reason:
                excluded.append((relative + "/", reason))
            else:
                keep_dirs.append(name)
        dirnames[:] = keep_dirs
        for name in sorted(filenames):
            path = base / name
            relative = path.relative_to(root).as_posix()
            reason = "symbolic link" if path.is_symlink() else exclusion_reason(relative)
            if not reason and not path.is_file():
                reason = "not a regular file"
            if reason:
                excluded.append((relative, reason))
            else:
                included.append((relative, path))
    return sorted(included), sorted(excluded)


def identity(path: Path):
    stat = path.stat()
    return stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns


def create_bundle(root: Path, destination: Path):
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Refusing to overwrite existing output: {destination}")
    included, excluded = scan_tree(root)
    if not included:
        raise RuntimeError("No eligible deliverables or documentation found")
    # Snapshot the source set and fail if a concurrent page save changes it.
    before = {relative: identity(path) for relative, path in included}
    payloads = []
    for relative, path in included:
        data = path.read_bytes()
        if identity(path) != before[relative] or len(data) != before[relative][2]:
            raise RuntimeError(f"File changed while being packaged: {relative}; retry after the save finishes")
        payloads.append((relative, data))
    current, _ = scan_tree(root)
    if [x[0] for x in current] != [x[0] for x in included]:
        raise RuntimeError("Eligible file set changed while being packaged; retry after the save finishes")
    for relative, path in current:
        if identity(path) != before[relative]:
            raise RuntimeError(f"File changed while being packaged: {relative}; retry after the save finishes")
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.building-", suffix=".tmp", dir=destination.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w+b") as handle:
            with zipfile.ZipFile(handle, mode="w", compression=zipfile.ZIP_DEFLATED,
                                 compresslevel=9, allowZip64=True) as archive:
                for relative, data in payloads:
                    info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.create_system = 3
                    info.external_attr = (0o100644 << 16)
                    archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
            handle.flush()
            os.fsync(handle.fileno())
        with zipfile.ZipFile(temporary) as archive:
            bad_crc = archive.testzip()
            if bad_crc:
                raise RuntimeError(f"ZIP integrity failure: {bad_crc}")
            if archive.namelist() != [relative for relative, _ in payloads]:
                raise RuntimeError("ZIP file ordering or membership mismatch")
        # Atomic publication fails if the destination exists. No overwrite or
        # rename operation is used on a previous checkpoint.
        os.link(temporary, destination)
    finally:
        # Only the private temporary file from this invocation is removed.
        temporary.unlink(missing_ok=True)
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    print(f"Created: {destination}")
    print(f"Included files: {len(payloads)}; excluded paths: {len(excluded)}")
    print(f"Uncompressed bytes: {sum(len(data) for _, data in payloads)}")
    print(f"ZIP bytes: {destination.stat().st_size}")
    print(f"SHA-256: {digest}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    kind = parser.add_mutually_exclusive_group(required=True)
    kind.add_argument("--checkpoint", type=int, metavar="NN")
    kind.add_argument("--final", action="store_true")
    parser.add_argument("--output-dir", type=Path,
                        help="Output directory; defaults to the work root's parent")
    parser.add_argument("--list", action="store_true", help="List paths only; do not create any ZIP")
    args = parser.parse_args()
    if args.checkpoint is not None and args.checkpoint < 1:
        parser.error("checkpoint number must be positive")
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"work root is not a directory: {root}")
    filename = (f"{PREFIX}_checkpoint_{args.checkpoint:02d}.zip"
                if args.checkpoint is not None else f"{PREFIX}.zip")
    destination = (args.output_dir or root.parent).resolve() / filename
    if args.list:
        included, excluded = scan_tree(root)
        print(f"Would create: {destination}")
        print(f"Output already exists: {'yes' if destination.exists() or destination.is_symlink() else 'no'}")
        for relative, _ in included:
            print(f"INCLUDE {relative}")
        for relative, reason in excluded:
            print(f"EXCLUDE {relative}: {reason}")
        print(f"Eligible files: {len(included)}; excluded paths: {len(excluded)}; no ZIP created")
        return 0
    try:
        create_bundle(root, destination)
    except (OSError, RuntimeError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
