#!/usr/bin/env python3
"""Validate the completed output tree and optionally create its final ZIP.

Without --create this is a read-only readiness check. With --create it runs the
full structural validator, then creates SP33_CW_156-5.zip with the contents of
out/ at the archive root. All .zip files are omitted. Existing archives are
never overwritten. No source, record, page, or log is modified.

This utility verifies structure and frozen-transcription hashes, not manuscript
accuracy or the substantive truth/completeness of research and check events.
The caller must still record the final unchanged-hash check in progress.log.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from make_checkpoint import create_archive, utc_text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--create", action="store_true", help="Create the final ZIP only after full structural validation succeeds")
    args = parser.parse_args()
    root = args.out.resolve()
    destination = (args.archive or root.parent / "deliverables" / "SP33_CW_156-5.zip").resolve()
    if destination.name != "SP33_CW_156-5.zip":
        parser.error("The requested final archive filename is SP33_CW_156-5.zip")
    if destination == root or destination.is_relative_to(root):
        parser.error("The final archive must be outside the output tree")
    result = subprocess.run(
        [sys.executable, str(root / "scripts" / "validate_package.py"), str(root), "--json"],
        capture_output=True, text=True, check=False,
    )
    try:
        validation = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(result.stderr or result.stdout, file=sys.stderr)
        return result.returncode or 2
    report = {"archive": str(destination), "created": False, "validation": validation}
    if result.returncode or not validation.get("passed"):
        print(json.dumps(report, indent=2))
        return 1
    if args.create:
        now = datetime.now(timezone.utc)
        try:
            count, size = create_archive(root, destination, {"type": "final", "created_utc": utc_text(now)})
        except (ValueError, OSError, RuntimeError) as exc:
            parser.exit(2, str(exc) + "\n")
        report.update(created=True, created_utc=utc_text(now), files=count, bytes=size)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
