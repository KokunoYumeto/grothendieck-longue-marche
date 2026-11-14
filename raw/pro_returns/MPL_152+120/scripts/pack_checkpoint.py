#!/usr/bin/env python3
"""Package work-in-progress deliverables without any supplied source archives."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Destination ZIP filename")
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parents[1],
                        help="Working deliverables directory (default: parent of scripts)")
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".writing")
    files = sorted(p for p in root.rglob("*")
                   if p.is_file() and not p.is_symlink()
                   and p.suffix.lower() != ".zip"
                   and "__pycache__" not in p.parts
                   and p.resolve() not in {output, temporary})
    if not files:
        raise SystemExit("Refusing to produce an empty checkpoint")
    try:
        with ZipFile(temporary, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for path in files:
                archive.write(path, path.relative_to(root).as_posix())
        with ZipFile(temporary) as archive:
            bad = archive.testzip()
            if bad:
                raise RuntimeError(f"ZIP integrity check failed: {bad}")
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(f"Created {output}: {len(files)} files, {output.stat().st_size} bytes")


if __name__ == "__main__":
    main()
