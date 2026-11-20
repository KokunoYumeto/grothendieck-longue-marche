"""Create one due checkpoint; this script never uploads it.

Usage: python checkpoint.py NUMBER UTC_DUE_TIME ["optional work-state string"]
Example time: 2026-11-20T15:47:47Z. Invoke no more than 60 seconds before due.
The archive is created exclusively: an earlier checkpoint is never overwritten.
"""

import argparse
import csv
import hashlib
import re
import time
import zipfile
from datetime import datetime, timezone

from workflow import ROOT, log, now


CHECKPOINT_PATTERN = re.compile(r"SP67_C13_136_checkpoint_\d+\.zip\Z")
HISTORY_FIELDS = ("checkpoint_name", "size_bytes", "sha256")
EXCLUDED_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".tif", ".tiff", ".bmp",
    ".svg", ".avif", ".heic", ".heif", ".ico", ".jp2", ".jxl",
    ".ppm", ".pgm", ".pbm", ".pnm", ".zip", ".pyc",
}


def previous_checkpoint_inventory(current_name):
    """Retain older names even after recovery leaves their bytes elsewhere."""
    history = ROOT / "checkpoint_history.tsv"
    entries = {}
    if history.is_file():
        with history.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            if tuple(reader.fieldnames or ()) != HISTORY_FIELDS:
                raise ValueError("Unexpected checkpoint_history.tsv schema; refusing to replace it")
            for row in reader:
                name = row["checkpoint_name"]
                if not CHECKPOINT_PATTERN.fullmatch(name):
                    raise ValueError("Invalid checkpoint name in checkpoint_history.tsv")
                if name != current_name:
                    entries[name] = row
    for path in sorted(ROOT.parent.glob("SP67_C13_136_checkpoint_*.zip")):
        if not path.is_file() or path.name == current_name:
            continue
        if not CHECKPOINT_PATTERN.fullmatch(path.name):
            continue
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
        entries[path.name] = {
            "checkpoint_name": path.name,
            "size_bytes": str(path.stat().st_size),
            "sha256": digest.hexdigest(),
        }
    rows = [entries[name] for name in sorted(entries)]
    with history.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=HISTORY_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    return [row["checkpoint_name"] for row in rows]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("number", type=int)
    parser.add_argument("due", help="ISO timestamp, interpreted as UTC if no offset is supplied")
    parser.add_argument("state", nargs="?", help="optional truthful description of the current work state")
    args = parser.parse_args()
    if args.number < 1:
        parser.error("checkpoint number must be positive")
    try:
        due = datetime.fromisoformat(args.due.replace("Z", "+00:00"))
    except ValueError:
        parser.error("due must be an ISO timestamp")
    due = due.replace(tzinfo=timezone.utc) if due.tzinfo is None else due.astimezone(timezone.utc)
    name = f"SP67_C13_136_checkpoint_{args.number:02d}.zip"
    target = ROOT.parent / name
    if target.exists():
        raise FileExistsError(f"Checkpoint already exists; refusing to overwrite: {target}")
    remaining = (due - datetime.now(timezone.utc)).total_seconds()
    if remaining > 60:
        parser.error("invoke at most 60 seconds before due; no long blocking wait is performed")
    if remaining > 0:
        time.sleep(remaining)
    previous = previous_checkpoint_inventory(name)
    if args.state is None:
        count = len(list((ROOT / "pages").glob("136_scan*.tex")))
        state = f"{count} consolidated page files present; no further state supplied"
    else:
        state = args.state.replace("\r", " ").replace("\n", " ").strip()
    prior_names = ", ".join(previous) or "none"
    log(f"checkpoint {args.number:02d} snapshot {now()} {name}; {state}; previous checkpoints: {prior_names}")
    with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(ROOT.rglob("*")):
            if (path.is_file() and "__pycache__" not in path.parts
                    and path.suffix.lower() not in EXCLUDED_SUFFIXES):
                archive.write(path, path.relative_to(ROOT))
    print(target)


if __name__ == "__main__":
    main()
