#!/usr/bin/env python3
"""Package deliverables; never upload, schedule, or overwrite an archive.

All regular files beneath the package root are included except caches,
original attachments, source-material directories, and embedded ZIP archives.
ZIP entries are relative to the package root, without an enclosing directory.
Symlinks are rejected rather than followed.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


EXCLUDED_DIRECTORIES = {
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".git",
    "scans", "upload", "context", "sources", "attachments",
}
EXCLUDED_FILENAMES = {
    "MPL_60_002-035_scans.zip", "MPL_60_002-035_context.zip",
    "PROMPT(20261115-232405).md",
    "Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf",
    "MPL_16+47+54+44_doubts.md", "MPL_16+47+54+44_notes.md",
    "MPL_16+47+54+44_transcription.tex", "RESULTS_STATE.md",
    ".DS_Store",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="deliverable directory")
    parser.add_argument("output", type=Path, help="new ZIP outside the deliverable directory")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    if not root.is_dir():
        parser.error("package root must be an existing directory")
    if output.is_relative_to(root):
        parser.error("ZIP output must be outside the deliverable directory")
    if output.suffix.lower() != ".zip":
        parser.error("output filename must end in .zip")
    if output.exists():
        parser.error("output exists; archives are never overwritten")
    if not output.parent.is_dir():
        parser.error("output parent directory must already exist")

    selected: list[tuple[Path, str]] = []
    excluded: list[str] = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRECTORIES for part in relative.parts):
            if path.is_file():
                excluded.append(relative.as_posix())
            continue
        if path.is_symlink():
            parser.error(f"symlink encountered; inspect before packaging: {relative}")
        if not path.is_file():
            continue
        if (path.name in EXCLUDED_FILENAMES or path.suffix.lower() in {".pyc", ".pyo", ".zip"}
                or path.name.startswith("MPL_60_002-035_60_scan") and path.suffix.lower() in {".jpg", ".jpeg", ".png"}):
            excluded.append(relative.as_posix())
            continue
        selected.append((path, relative.as_posix()))
    if not selected:
        parser.error("no deliverable files to package")

    try:
        with ZipFile(output, mode="x", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for path, relative in selected:
                archive.write(path, relative)
        with ZipFile(output) as archive:
            bad = archive.testzip()
            if bad is not None:
                raise RuntimeError(f"ZIP CRC failure: {bad}")
    except Exception:
        print(f"Packaging failed; inspect any incomplete output at {output}", file=sys.stderr)
        raise
    print(f"Created: {output}")
    print(f"Files: {len(selected)}")
    print(f"Bytes: {output.stat().st_size}")
    if excluded:
        print("Excluded source/cache/archive paths:")
        for relative in excluded:
            print(f"  {relative}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
