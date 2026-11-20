#!/usr/bin/env python3
"""Record the reader's completed image audit of one page.

Use only after the reader has actually reread the specified scan and recorded
any corrections. This helper makes no reading decisions and performs no image
audit. It preserves the supplied note, rebuilds aggregates from current data,
and appends an actual UTC audit timestamp. No page file is edited.

Supply the note with --note, --note-file, or standard input, for example:
    python scripts/audit_page.py 017 < /absolute/path/audit_note.txt
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCANS = (17, 18, 20, 22, 25, 27, 28, 29, 33, 34, 36, 38, 40,
         41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52)


def check_progress(log: str, scan: int) -> None:
    if scan not in SCANS:
        raise ValueError(f"Unknown scan: {scan}")
    if re.search(r"^transcription frozen\b", log, re.MULTILINE):
        raise ValueError("The transcription is frozen; audit recording is closed")
    done = [int(n) for n in re.findall(r"^scan (\d+) done .+ cote 16$", log, re.MULTILINE)]
    audited = [int(n) for n in re.findall(r"^scan (\d+) audited .+$", log, re.MULTILINE)]
    if done != list(SCANS):
        raise ValueError("All 25 first readings must be recorded once, in order, before the second pass")
    if audited != list(SCANS[:len(audited)]):
        raise ValueError("Existing audit log has duplicate or out-of-order scans")
    if scan in audited:
        raise ValueError(f"Scan {scan:03} already has an audit entry")
    if len(audited) == len(SCANS) or SCANS[len(audited)] != scan:
        expected = SCANS[len(audited)] if len(audited) < len(SCANS) else None
        raise ValueError(f"The next scan for the second pass is {expected}, not {scan}")


def record_audit(scan: int, note: str) -> str:
    if not note.strip():
        raise ValueError("An audit note is required")
    log_path = ROOT / "progress.log"
    check_progress(log_path.read_text(encoding="utf-8"), scan)
    path = ROOT / "scripts" / "records" / f"{scan:03}.json"
    original = path.read_bytes()
    record_data = json.loads(original)
    if record_data.get("scan") != scan:
        raise ValueError("Page record scan does not match the requested scan")
    existing_notes = record_data.get("audit_notes", [])
    if not isinstance(existing_notes, list):
        raise ValueError("audit_notes must be a list; existing data was left unchanged")
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    record_data["audit_notes"] = existing_notes + [{"utc": stamp, "note": note.rstrip("\r\n")}]
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                         prefix=".audit_", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(record_data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        if path.read_bytes() != original:
            raise ValueError("Page record changed concurrently; no audit was committed")
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    # The existing renderer reads current page files without changing them.
    # On a renderer error the supplied note remains saved, and no audited line
    # is appended. Repair/rebuild before retrying; no decision is discarded.
    import record
    record.build()
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"scan {scan:03} audited {stamp}\n")
        handle.flush()
        os.fsync(handle.fileno())
    return stamp


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("scan", type=int)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--note", help="The reader's completed-audit note")
    group.add_argument("--note-file", type=Path, help="UTF-8 text file containing the note")
    args = parser.parse_args()
    try:
        note = args.note if args.note is not None else args.note_file.read_text(encoding="utf-8") if args.note_file is not None else sys.stdin.read()
        stamp = record_audit(args.scan, note)
    except (OSError, ValueError, TypeError) as exc:
        print(f"Audit was not logged: {exc}", file=sys.stderr)
        return 1
    print(f"Recorded the supplied audit of scan {args.scan:03}: {stamp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
