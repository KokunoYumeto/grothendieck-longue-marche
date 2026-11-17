#!/usr/bin/env python3
"""Create an immutable checkpoint or final ZIP from the work directory.

No network or Library operations are performed. User-supplied source files,
images, caches and other ZIP archives are excluded. The output never overwrites
an existing file, including an earlier checkpoint.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

PREFIX = "MPL_93_221-236+161-5"
EXCLUDED_DIRS = {
    "__pycache__", ".git", ".pytest_cache", "upload", "uploads", "scans",
    "context", "rendered", "renders", "render", "tmp", "temp", ".venv",
    "node_modules", "hua_project", "same_cote_93",
}
EXCLUDED_SUFFIXES = {
    ".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar", ".jpg",
    ".jpeg", ".png", ".gif", ".tif", ".tiff", ".webp", ".bmp", ".pyc",
    ".pyo", ".aux", ".out", ".toc", ".synctex", ".fls", ".fdb_latexmk",
}


def excluded(relative: Path) -> bool:
    lower_parts = tuple(part.lower() for part in relative.parts)
    if any(part in EXCLUDED_DIRS for part in lower_parts[:-1]):
        return True
    if relative.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    name = relative.name.lower()
    if relative.as_posix().lower() == "notes/results_state.md":
        return True
    if name in {"93.pdf", "161-5.pdf"}:
        return True
    if name.startswith("prompt(") or name == "prompt.md":
        return True
    if name.endswith(".tmp") or name.startswith(".~"):
        return True
    # Original source archives are excluded by suffix; these directory-name
    # guards also protect against accidentally placing extracted copies here.
    if any(part.startswith(PREFIX.lower() + "_scans") or part.startswith(PREFIX.lower() + "_context") for part in lower_parts):
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Destination ZIP path (must not exist)")
    parser.add_argument("--workdir", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--list-only", action="store_true", help="List included relative paths without reading their bytes or making a ZIP")
    args = parser.parse_args()
    work = args.workdir.resolve()
    output = args.output.absolute()
    if not work.is_dir():
        parser.error(f"Work directory does not exist: {work}")
    if output.suffix.lower() != ".zip":
        parser.error("Output filename must end in .zip")
    if output.exists():
        parser.error(f"Refusing to overwrite an existing ZIP: {output}")
    included = []
    skipped_symlinks = []
    for directory, dirs, names in os.walk(work, followlinks=False):
        parent = Path(directory)
        dirs[:] = sorted(d for d in dirs if not excluded(parent.relative_to(work) / d / "_") and not (parent / d).is_symlink())
        for name in sorted(names):
            path = parent / name
            relative = path.relative_to(work)
            if excluded(relative) or path.absolute() == output:
                continue
            if path.is_symlink():
                skipped_symlinks.append(relative.as_posix())
                continue
            if path.is_file():
                included.append((path, relative.as_posix()))
    included.sort(key=lambda pair: pair[1])
    if args.list_only:
        print("\n".join(relative for _, relative in included))
        return 0
    if not included:
        parser.error("No eligible files to package")
    output.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with ZipFile(output, "x", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            created = True
            for path, relative in included:
                archive.write(path, arcname=relative)
        with ZipFile(output) as archive:
            damaged = archive.testzip()
            if damaged:
                raise OSError(f"ZIP CRC check failed for {damaged}")
        digest = hashlib.sha256(output.read_bytes()).hexdigest()
    except Exception:
        # Never leave a half-written archive that could be mistaken for a
        # completed checkpoint. Only this newly created output is removed.
        if created and output.exists():
            output.unlink()
        raise
    print(json.dumps({
        "output": str(output),
        "files": len(included),
        "size_bytes": output.stat().st_size,
        "sha256": digest,
        "skipped_symlinks": skipped_symlinks,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
