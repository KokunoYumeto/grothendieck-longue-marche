#!/usr/bin/env python3
"""Create only the named final ZIP, after validation; default is a file-list preview.

This script never creates a checkpoint, changes a deliverable, or overwrites an
existing archive. Complete the research notes and final progress-log hash check
before running with --write.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True
from package_integrity import PREFIX, package_members, zip_checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true", help="Validate, then create the final ZIP exclusively.")
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root.parent / f"{PREFIX}.zip").resolve()
    if output.name != f"{PREFIX}.zip" or output.is_relative_to(root):
        parser.error("Output must be named MPL_138_001-045.zip and reside outside the work directory.")
    included, excluded = package_members(root)
    if not args.write:
        print(json.dumps({"mode": "preview_only", "output": str(output), "included": included, "excluded": excluded}, indent=2))
        return 0
    if output.exists():
        parser.error("Output already exists; the final packager never overwrites an archive.")
    check = subprocess.run(
        [sys.executable, "-B", str(root / "scripts" / "validate_package.py"), str(root), "--json"],
        capture_output=True, text=True, check=False,
    )
    if check.returncode:
        print(check.stdout, end="")
        print(check.stderr, end="", file=sys.stderr)
        return check.returncode
    output.parent.mkdir(parents=True, exist_ok=True)
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".mpl-final-", suffix=".zip", dir=output.parent, delete=False) as temp:
            temp_name = Path(temp.name)
        with zipfile.ZipFile(temp_name, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name in included:
                archive.write(root / name, name)
        verification = zip_checks(root, temp_name)
        if not verification["ok"]:
            print(json.dumps(verification, indent=2))
            return 1
        # A same-filesystem hard link installs the finished archive without an overwrite race.
        os.link(temp_name, output)
        print(json.dumps({"ok": True, "output": str(output), "bytes": output.stat().st_size,
                          "members": len(included), "frozen_hashes_verified": verification["zip_frozen_hashes_verified"],
                          "excluded": excluded}, indent=2))
        return 0
    finally:
        if temp_name is not None:
            temp_name.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
