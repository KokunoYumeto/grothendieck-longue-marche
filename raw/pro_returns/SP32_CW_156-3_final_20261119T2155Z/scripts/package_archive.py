#!/usr/bin/env python3
"""Package authored work; never include source attachments or nested checkpoints.

Usage:
    python scripts/package_archive.py WORKDIR OUTPUT.zip [--dry-run]

OUTPUT must be outside WORKDIR. Existing outputs are never overwritten. This
script does not choose checkpoint times or upload files; the reader does that.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import zipfile
from pathlib import Path

STEM = "SP32_CW_156-3"
INPUT_FOLDERS = {
    "upload", "source", f"{STEM}_context", f"{STEM}_scans",
    f"{STEM}_witnesses", f"{STEM}_sweep3",
}
TEMP_FOLDERS = {"__pycache__", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
TEMP_SUFFIXES = {
    ".aux", ".bbl", ".bcf", ".blg", ".fdb_latexmk", ".fls", ".lof", ".lot",
    ".nav", ".out", ".snm", ".toc", ".vrb", ".xdv", ".pyc", ".pyo", ".tmp",
}


def skip_reason(path: Path, relative: Path) -> str | None:
    if any(p in INPUT_FOLDERS for p in relative.parts):
        return "source-attachment directory"
    if any(p in TEMP_FOLDERS for p in relative.parts):
        return "temporary directory"
    name = path.name
    if re.search(r"checkpoint.*\.zip$", name, re.IGNORECASE):
        return "checkpoint archive"
    if name in {f"{STEM}.zip", "PROMPT(20261119-202125).md"}:
        return "input attachment or self archive"
    if re.fullmatch(re.escape(STEM) + r"_(?:context|scans|witnesses|sweep3)\.zip", name):
        return "source attachment archive"
    if re.fullmatch(r"J156-3-0[45]_156-3_scan\d{3}(?:_[ab])?\.jpg", name):
        return "original scan image"
    if path.suffix.lower() in TEMP_SUFFIXES or name.endswith((".synctex.gz", ".run.xml", "~")):
        return "temporary compiler/editor output"
    if path.suffix.lower() == ".log" and path.with_suffix(".tex").exists():
        return "LaTeX compiler log"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("workdir", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root, output = args.workdir.resolve(), args.output.resolve()
    if not root.is_dir():
        parser.error("WORKDIR is not a directory")
    if output.is_relative_to(root):
        parser.error("OUTPUT must be outside WORKDIR")
    if output.suffix.lower() != ".zip":
        parser.error("OUTPUT must end in .zip")
    if output.exists():
        parser.error("refusing to overwrite an existing archive")
    selected, skipped = [], []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if path.is_symlink():
            parser.error(f"refusing symbolic link inside work directory: {rel}")
        if not path.is_file():
            continue
        reason = skip_reason(path, rel)
        if reason:
            skipped.append((rel, reason))
        else:
            selected.append((path, rel))
    if not selected:
        parser.error("no files selected")
    print(f"Selected {len(selected)} files; excluded {len(skipped)} source/temporary/archive files.")
    for rel, reason in skipped:
        print(f"Excluded {rel}: {reason}")
    if args.dry_run:
        for _, rel in selected:
            print(rel.as_posix())
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation makes the no-overwrite rule hold even under a race.
    fd = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb") as handle:
            with zipfile.ZipFile(handle, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
                for path, rel in selected:
                    archive.write(path, arcname=rel.as_posix())
        with zipfile.ZipFile(output) as archive:
            bad = archive.testzip()
            if bad:
                raise RuntimeError(f"ZIP integrity check failed for {bad}")
            if len(archive.infolist()) != len(selected):
                raise RuntimeError("ZIP file-count mismatch")
    except BaseException:
        # Leave a failed archive in place rather than silently overwrite or
        # delete a checkpoint. The caller can diagnose and choose a new name.
        print(f"Archive operation failed; inspect {output}", file=sys.stderr)
        raise
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    print(f"Created {output}")
    print(f"Bytes: {output.stat().st_size}; SHA-256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
