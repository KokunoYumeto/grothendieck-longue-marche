#!/usr/bin/env python3
"""Archive the complete deliverable tree, never the supplied inputs or caches."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = ROOT.name
p = argparse.ArgumentParser()
p.add_argument('--checkpoint', type=int)
p.add_argument('--final', action='store_true')
args = p.parse_args()
assert bool(args.checkpoint) != bool(args.final), 'Choose checkpoint number or final.'
suffix = f'_checkpoint_{args.checkpoint:02d}' if args.checkpoint else ''
out = ROOT.parent / f'{NAME}{suffix}.zip'
assert not out.exists(), f'Refusing to overwrite {out}'
now = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
kind = f'checkpoint {args.checkpoint:02d}' if args.checkpoint else 'final archive'
with (ROOT / 'progress.log').open('a') as f:
    f.write(f'{kind} assembled {now}\n')
files = sorted(q for q in ROOT.rglob('*') if q.is_file() and '__pycache__' not in q.parts and q.suffix != '.pyc')
for q in files:
    assert not any(x in q.relative_to(ROOT).parts for x in ('scans', 'upload', 'context', 'view', 'texqa-cache'))
with zipfile.ZipFile(out, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for q in files:
        z.write(q, q.relative_to(ROOT).as_posix())
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files)
    names = z.namelist()
    page_names = [n for n in names if n.startswith('pages/') and n.endswith('.tex')]
    assert len(page_names) == 44
print(json.dumps({'archive': str(out), 'assembled_utc': now, 'members': len(files), 'page_files': len(page_names), 'bytes': out.stat().st_size, 'sha256': hashlib.sha256(out.read_bytes()).hexdigest()}, indent=2))
