#!/usr/bin/env python3
"""Archive all work products, excluding source materials and temporary files.

Usage: python scripts/make_zip.py OUTPUT.zip [--root WORK_DIRECTORY]
OUTPUT must be outside WORK_DIRECTORY and must not already exist. The same
script supports final archives and uniquely numbered hourly checkpoints.
It never reads input archives or uses OCR.
"""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path


EXCLUDED_DIRECTORIES = {
    "__pycache__", ".cache", ".git", ".pytest_cache", ".mypy_cache",
    "node_modules", "tmp", "temp", "temporary", "scans", "context",
    "sources", "source", "images", "upload", "uploads", "qa_renders",
    "renders", "crops", "MPL_105_context", "MPL_105_scans",
}
EXCLUDED_SUFFIXES = {
    ".zip", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif",
    ".tiff", ".bmp", ".avif", ".heic", ".pyc", ".pyo", ".tmp",
    ".temp", ".part", ".swp", ".swo", ".aux", ".toc", ".out",
    ".synctex", ".fdb_latexmk", ".fls",
}


def excluded(relative: Path) -> bool:
    if any(part in EXCLUDED_DIRECTORIES for part in relative.parts[:-1]):
        return True
    name = relative.name
    if name in {".DS_Store", "Thumbs.db"} or name.startswith(".~") or name.endswith("~"):
        return True
    if any(suffix.lower() in EXCLUDED_SUFFIXES for suffix in relative.suffixes):
        return True
    # The known supplied source PDF, if accidentally copied into the work tree.
    return name == "105.pdf"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    if not root.is_dir():
        parser.error(f"Work directory does not exist: {root}")
    if output.is_relative_to(root):
        parser.error("Output must be outside the work directory")
    if output.suffix.lower() != ".zip":
        parser.error("Output filename must end in .zip")
    if output.exists():
        parser.error("Output already exists; refusing to overwrite an earlier archive")
    members: list[tuple[Path, Path]] = []
    omitted: list[str] = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if path.is_symlink():
            omitted.append(relative.as_posix())
            continue
        if not path.is_file():
            continue
        if excluded(relative):
            omitted.append(relative.as_posix())
            continue
        members.append((path, relative))
    if not members:
        parser.error("No eligible work files to archive")
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path, relative in members:
                archive.write(path, relative.as_posix())
    except Exception:
        # A partial archive is not a completed checkpoint. Preserve its bytes for
        # diagnosis without leaving a misleadingly complete .zip filename.
        if output.exists():
            output.rename(output.with_suffix(output.suffix + ".incomplete"))
        raise
    print(json.dumps({
        "output": str(output), "files": len(members),
        "size_bytes": output.stat().st_size, "omitted": omitted,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
