#!/usr/bin/env python3
"""Package all current deliverables without reading or interpreting their text.

Does not schedule checkpoints or upload anything. The caller must invoke it
only when the requested hourly checkpoint is due, or for the final delivery.
The first checkpoint is due 2026-11-15 13:11:41 UTC.

Example (from the package directory, only after the checkpoint is due):
    python records/package_deliverables.py \
      /workspace/scratch/390184a42c26/MPL_15_195-228+18_002-017_checkpoint_01.zip

The output must be outside the package directory. Existing files are never
overwritten. ZIP members are package-relative (pages/, records/, etc.).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile


PREFIX = "MPL_15_195-228+18_002-017"
EXCLUDED_DIRS = {"__pycache__", "scans", "context", "upload", "uploads", "inputs"}
SUPPLIED_NAMES = {
    f"{PREFIX}_scans.zip", f"{PREFIX}_context.zip",
    "PROMPT(20261115-121056).md",
    "MPL_16+47+54+44_doubts.md", "MPL_16+47+54+44_notes.md",
    "MPL_16+47+54+44_transcription.tex",
    "Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf",
}
SCAN_IMAGE = re.compile(re.escape(PREFIX) + r"_(?:15|18)_scan\d{3}(?:_[ab])?\.(?:jpe?g|png|tiff?)$", re.I)


def excluded(relative: Path) -> bool:
    return (
        any(part in EXCLUDED_DIRS for part in relative.parts)
        or relative.suffix.lower() in {".pyc", ".pyo"}
        or relative.name in SUPPLIED_NAMES
        or relative.as_posix() == "notes/RESULTS_STATE.md"
        or bool(SCAN_IMAGE.fullmatch(relative.name))
    )


def signature(path: Path):
    info = path.stat()
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output", type=Path, help="new ZIP path, outside the package directory")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    output = args.output.absolute()
    output.parent.mkdir(parents=True, exist_ok=True)
    output = output.parent.resolve() / output.name
    if output == root or root in output.parents:
        parser.error("output must be outside the package directory")
    if output.exists() or output.is_symlink():
        parser.error(f"refusing to overwrite existing output: {output}")
    if output.suffix.lower() != ".zip":
        parser.error("output must have a .zip extension")

    selected = []
    omitted = []
    for directory, dirs, names in os.walk(root, followlinks=False):
        parent = Path(directory)
        for name in list(dirs):
            child = parent / name
            relative = child.relative_to(root)
            if excluded(relative):
                dirs.remove(name)
                omitted.append(relative.as_posix() + "/")
            elif child.is_symlink():
                parser.error(f"refusing directory symlink in deliverables: {relative}")
        for name in names:
            path = parent / name
            relative = path.relative_to(root)
            if excluded(relative):
                omitted.append(relative.as_posix())
                continue
            if path.is_symlink():
                parser.error(f"refusing file symlink in deliverables: {relative}")
            if not stat.S_ISREG(path.stat().st_mode):
                parser.error(f"refusing non-regular file in deliverables: {relative}")
            selected.append((relative.as_posix(), path, signature(path)))
    selected.sort()
    if not selected:
        parser.error("no deliverable files found")

    descriptor, temporary_name = tempfile.mkstemp(prefix=".mpl_zip_", suffix=".tmp", dir=output.parent)
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", compression=ZIP_DEFLATED, compresslevel=9, allowZip64=True) as archive:
            for name, path, initial_signature in selected:
                if signature(path) != initial_signature:
                    raise RuntimeError(f"file changed before packaging: {name}")
                archive.write(path, arcname=name)
                if signature(path) != initial_signature:
                    raise RuntimeError(f"file changed during packaging: {name}")
        for name, path, initial_signature in selected:
            if signature(path) != initial_signature:
                raise RuntimeError(f"file changed while snapshot was being assembled: {name}")
        # Validate ZIP integrity before making the requested filename visible.
        with ZipFile(temporary, "r") as archive:
            bad = archive.testzip()
            if bad is not None:
                raise RuntimeError(f"ZIP CRC verification failed: {bad}")
            if archive.namelist() != [name for name, _, _ in selected]:
                raise RuntimeError("ZIP member list differs from selected deliverable files")
        with temporary.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        # A hard link atomically publishes the completed file and fails if the
        # requested output already exists; it never replaces an older snapshot.
        os.link(temporary, output)
        print(json.dumps({
            "archive": str(output),
            "files": len(selected),
            "bytes": output.stat().st_size,
            "sha256": digest,
            "excluded_paths": sorted(omitted),
            "overwrote_existing_file": False,
        }, ensure_ascii=False, indent=2))
    finally:
        temporary.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
