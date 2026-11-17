#!/usr/bin/env python3
"""Create one complete deliverable archive; never copy inputs or prior ZIPs."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
parser.add_argument('--checkpoint', type=int)
parser.add_argument('--replace-final', action='store_true', help='Atomically repack this run’s final archive; never a checkpoint')
args = parser.parse_args()
root = args.root.resolve()
now = datetime.now(timezone.utc)
stamp = now.strftime('%Y-%m-%d %H:%M:%S UTC')
if args.checkpoint is not None:
    start = datetime.strptime((root/'progress.log').read_text().splitlines()[0], '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    if (now-start).total_seconds() < args.checkpoint*3600:
        raise SystemExit('Checkpoint not yet due; no archive created.')
    name = f'MPL_64_002-039_checkpoint_{args.checkpoint:02}.zip'
else:
    name = 'MPL_64_002-039.zip'
out = root.parent/name
replacing = out.exists()
if args.replace_final and args.checkpoint is not None:
    raise SystemExit('Checkpoints can never be overwritten.')
if replacing and not (args.replace_final and args.checkpoint is None):
    raise SystemExit(f'Refusing to overwrite {out}')
with (root/'progress.log').open('a') as handle:
    handle.write(f'archive {"repacked" if replacing else "created"} {name} {stamp}\n')
paths = sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.zip'})
pending = out.with_suffix(out.suffix+'.pending')
with zipfile.ZipFile(pending, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in paths:
        archive.write(path, path.relative_to(root).as_posix())
with zipfile.ZipFile(pending) as archive:
    assert archive.testzip() is None
pending.replace(out)
print(f'{out}\nfiles={len(paths)} bytes={out.stat().st_size}')
