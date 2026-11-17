#!/usr/bin/env python3
"""Record one completed visual audit, only when the human/model reader invokes it.

This program does not inspect images and cannot perform or certify an audit.
Invoke it ONLY after personally reviewing the named page against its images and
making any necessary corrections/doubt marks. It appends exactly the requested
UTC audit record, and makes no changes to page files.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


PACKAGE = "MPL_136_282-327"
SCANS = tuple(n for n in range(282, 328) if n != 319)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scan", type=int, choices=SCANS,
                        help="scan whose visual audit the caller has just completed")
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.root.resolve()
    log_path = root / "progress.log"
    try:
        log = log_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot read progress.log: {exc}", file=sys.stderr)
        return 1
    if re.search(r"(?m)^(transcription frozen|context opened)\b", log):
        print("ERROR: refusing a new audit claim after freeze or context opening", file=sys.stderr)
        return 1
    completed = {int(n) for n in re.findall(r"(?m)^136 scan (\d+) done\b", log)}
    if completed != set(SCANS):
        print("ERROR: all 45 first-pass done records are required before final audits", file=sys.stderr)
        return 1
    missing_files = [n for n in SCANS
                     if not (root / "pages" / f"{PACKAGE}_136_scan{n}.tex").is_file()]
    if missing_files:
        print(f"ERROR: missing page files: {missing_files}", file=sys.stderr)
        return 1
    audited = [int(n) for n in re.findall(r"(?m)^scan (\d+) audited\b", log)]
    if args.scan in audited:
        print(f"ERROR: scan {args.scan} already has an audit record", file=sys.stderr)
        return 1
    if audited != list(SCANS[:len(audited)]):
        print("ERROR: existing audit records are not a sequential prefix", file=sys.stderr)
        return 1
    expected = SCANS[len(audited)] if len(audited) < len(SCANS) else None
    if args.scan != expected:
        print(f"ERROR: next sequential audit record is scan {expected}", file=sys.stderr)
        return 1
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"scan {args.scan} audited {stamp}\n"
    with log_path.open("a", encoding="utf-8") as stream:
        if log and not log.endswith("\n"):
            stream.write("\n")
        stream.write(line)
    print(line, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
