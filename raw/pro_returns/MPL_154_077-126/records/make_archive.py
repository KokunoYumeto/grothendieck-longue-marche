#!/usr/bin/env python3
"""Archive all current deliverables and work records, without source images.

The ZIP stores paths relative to the package root. Existing archives are never
overwritten. Checkpoint cadence and successful persistent upload are the caller's
responsibility; this script neither marks work complete nor edits progress.log.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import zipfile


EXCLUDED_DIRS = {
    "__pycache__", ".git", ".venv", "venv", "upload", "uploads", "scans",
    "context", "sources", "attachments", "source_attachments",
}
EXCLUDED_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff", ".bmp",
    ".svg", ".heic", ".avif", ".zip", ".pyc", ".pyo",
}
EXCLUDED_NAMES = {
    "PROMPT(20261114-232512).md", "MPL_154_077-126_context.zip",
    "MPL_154_077-126_scans.zip", "Esquisse_cote119_copy1_API_transcription.tex",
    "STATEMENTS_WITH_STATUS.md", "RESULTS_STATE.md", "154.pdf",
}

# The QA driver can regenerate these binary/auxiliary files. Its logs and
# launcher output remain part of the research record and must stay in every
# checkpoint. Keep the small qa-texmf configuration/map tree as well.
QA_GENERATED_SUFFIXES = {
    ".fmt", ".pdf", ".dvi", ".xdv", ".aux", ".toc", ".lof", ".lot",
    ".nav", ".snm", ".vrb", ".fdb_latexmk", ".synctex",
}
QA_CACHE_DIRS = {"texmf-cache", "texmf-var", "qa-cache"}
QA_RECORD_SUFFIXES = {
    ".log", ".out", ".err", ".txt", ".md", ".rst", ".csv", ".tsv",
    ".json", ".jsonl", ".yaml", ".yml", ".py", ".sh", ".js", ".ts",
    ".tex", ".bib", ".cfg",
}


def is_generated_qa_cache(relative: Path) -> bool:
    """Classify by path and extension only; never inspect manuscript content."""
    if not relative.parts or relative.parts[0] != "records":
        return False
    if relative.suffix.lower() in QA_RECORD_SUFFIXES:
        return False
    if any(part in QA_CACHE_DIRS for part in relative.parts[1:-1]):
        return True
    if "qa-build" not in relative.parts[1:-1]:
        return False
    return (
        relative.suffix.lower() in QA_GENERATED_SUFFIXES
        or relative.name.lower().endswith(".synctex.gz")
    )


def archive_files(root: Path):
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if path.is_symlink():
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in EXCLUDED_SUFFIXES or path.name in EXCLUDED_NAMES:
            continue
        if is_generated_qa_cache(relative):
            continue
        yield path, relative.as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New ZIP path; it must not already exist")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    if not root.is_dir():
        parser.error(f"Package root is not a directory: {root}")
    if output.suffix.lower() != ".zip":
        parser.error("Output must have the .zip extension")
    if output.exists():
        parser.error(f"Refusing to overwrite existing archive: {output}")
    entries = list(archive_files(root))
    if not entries:
        parser.error("No eligible files found")
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path, name in entries:
                archive.write(path, name)
        with zipfile.ZipFile(output) as archive:
            bad_member = archive.testzip()
        if bad_member is not None:
            raise RuntimeError(f"ZIP integrity check failed for {bad_member}")
    except Exception as exc:
        print(f"Archive creation failed: {exc}", file=sys.stderr)
        print(f"Inspect any partial file before retrying: {output}", file=sys.stderr)
        return 1
    print(f"Created {output}")
    print(f"Files: {len(entries)}; ZIP bytes: {output.stat().st_size}")
    print("Source attachments, images, and generated TeX caches excluded; logs retained; archive CRC check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
