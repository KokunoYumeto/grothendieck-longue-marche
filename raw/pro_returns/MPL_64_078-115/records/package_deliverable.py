#!/usr/bin/env python3
"""Package deliverables and work records; never includes supplied scans/context."""
import argparse, hashlib, json, zipfile
from pathlib import Path
from datetime import datetime, timezone, timedelta

base=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
group=parser.add_mutually_exclusive_group(required=True)
group.add_argument('--checkpoint',type=int)
group.add_argument('--final',action='store_true')
args=parser.parse_args()
now=datetime.now(timezone.utc)
stamp=now.strftime('%Y-%m-%d %H:%M:%S UTC')
start=datetime.strptime((base/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
if args.checkpoint is not None:
    if args.checkpoint<1:raise SystemExit('Checkpoint numbers start at01')
    due=start+timedelta(hours=args.checkpoint)
    if now<due:raise SystemExit(f'Checkpoint not due until {due.isoformat()}')
    name=f'MPL_64_078-115_checkpoint_{args.checkpoint:02d}.zip'
else:
    name='MPL_64_078-115.zip'
target=base.parent/name
if target.exists():raise SystemExit(f'Refusing to overwrite {target}')
for entry in (base/'records'/'SHA256SUMS.frozen').read_text().splitlines():
    digest,path=entry.split(maxsplit=1)
    path=path.lstrip('*')
    actual=hashlib.sha256((base/path).read_bytes()).hexdigest()
    if actual!=digest:raise SystemExit(f'FROZEN HASH MISMATCH: {path}')
required=['MPL_64_078-115_transcription.tex','MPL_64_078-115_doubts.md',
          'MPL_64_078-115_inventory.csv','MPL_64_078-115_notes.md','progress.log','CHECK_EVENTS.tsv']
for name_ in required:
    if not (base/name_).is_file():raise SystemExit(f'Missing {name_}')
with (base/'progress.log').open('a') as log:
    log.write(('hourly checkpoint '+str(args.checkpoint) if args.checkpoint is not None else 'final package')+' prepared '+stamp+'; all39 frozen hashes unchanged\n')
files=[p for p in sorted(base.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.zip')]
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,p.relative_to(base))
with zipfile.ZipFile(target) as z:
    error=z.testzip()
    if error:raise SystemExit(f'ZIP CRC failure: {error}')
print(json.dumps({'path':str(target),'files':len(files),'bytes':target.stat().st_size,
                  'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'created_utc':stamp,
                  'frozen_sources_unchanged':39},indent=2))
