#!/usr/bin/env python3
"""Create one hourly checkpoint ZIP after its due time; never upload or overwrite."""
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
import zipfile


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--number", type=int, required=True)
    args = parser.parse_args()
    if args.number < 1:
        parser.error("checkpoint number must be positive")
    root = Path(__file__).resolve().parent.parent
    log = root / "progress.log"
    first_line = log.read_text(encoding="utf-8").splitlines()[0]
    started = datetime.strptime(first_line, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    due = started + timedelta(hours=args.number)
    now = datetime.now(timezone.utc)
    if now < due:
        parser.error("checkpoint is not due until " + due.strftime("%Y-%m-%d %H:%M:%S UTC"))
    archive = root.parent / f"MPL_67_002-052_checkpoint_{args.number:02d}.zip"
    if archive.exists():
        parser.error("checkpoint already exists; earlier checkpoints must never be overwritten")
    if not (root / "CHECK_EVENTS.tsv").is_file():
        parser.error("CHECK_EVENTS.tsv is required in every checkpoint")
    with log.open("a", encoding="utf-8") as stream:
        stream.write(f"checkpoint {args.number:02d} snapshot cutoff " + now.strftime("%Y-%m-%d %H:%M:%S UTC") + "\n")
    paths = sorted(p for p in root.rglob("*") if p.is_file()
                   and "__pycache__" not in p.parts and p.suffix != ".pyc"
                   and not p.name.endswith(".zip"))
    with zipfile.ZipFile(archive, mode="x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
        for path in paths:
            zipped.write(path, path.relative_to(root))
    with log.open("a", encoding="utf-8") as stream:
        stream.write(f"checkpoint {args.number:02d} archive created " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC") + "\n")
    print(str(archive))
    print(f"members={len(paths)} bytes={archive.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
