#!/usr/bin/env python3
"""Validate and package final deliverables, excluding supplied source material."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from validate_package import PREFIX, validate

EXCLUDED_DIRS = {"upload", "uploads", "scans", "context", "same_cote_33", "__pycache__", ".git"}
EXCLUDED_NAMES = {"PROMPT(3).md", f"{PREFIX}_scans.zip", f"{PREFIX}_context.zip"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root.parent / f"{PREFIX}.zip").resolve()
    result = validate(root, final=True)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["ok"]:
        print("No ZIP created: resolve structural validation errors first.")
        return 1
    if output.exists():
        print(f"No ZIP created: output already exists: {output}")
        return 1
    files = []
    excluded = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if path.is_symlink():
            raise ValueError(f"Refusing symlink: {rel}")
        if (any(part in EXCLUDED_DIRS or part.startswith(".") for part in rel.parts)
                or path.name in EXCLUDED_NAMES
                or path.suffix.lower() in {".zip", ".pyc"}
                or re.fullmatch(r"MPL_33_002-049_33_scan\d{3}(?:_[ab])?\.jpg", path.name)
                or path == output):
            excluded.append(rel.as_posix())
            continue
        files.append((path, rel.as_posix()))
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "x", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path, rel in files:
            archive.write(path, arcname=rel)
    with ZipFile(output) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"ZIP integrity check failed: {bad}")
    print(json.dumps({"zip": str(output), "files": len(files), "bytes": output.stat().st_size,
                      "excluded": excluded}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
