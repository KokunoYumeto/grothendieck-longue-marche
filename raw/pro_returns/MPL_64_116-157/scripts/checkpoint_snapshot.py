#!/usr/bin/env python3
"""Create one hourly checkpoint without interpreting any manuscript content."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import zipfile

p=argparse.ArgumentParser()
p.add_argument('--number',type=int,required=True)
p.add_argument('--not-before',required=True,help='UTC ISO timestamp, e.g. 2026-11-17T23:28:39+00:00')
a=p.parse_args()
now=datetime.now(timezone.utc)
due=datetime.fromisoformat(a.not_before)
if now<due:raise SystemExit('Refusing to checkpoint before the hourly boundary.')
workspace=Path(__file__).resolve().parents[2]
root=workspace/'MPL_64_116-157_work'
out=workspace/f'MPL_64_116-157_checkpoint_{a.number:02d}.zip'
if out.exists():raise SystemExit('Refusing to overwrite an earlier checkpoint.')
with (root/'progress.log').open('a',encoding='utf-8') as h:
 h.write(f'checkpoint {a.number:02d} snapshot created {now:%Y-%m-%d %H:%M:%S UTC}; complete written deliverables and work documentation; source scans, supplied archives, context sources and earlier checkpoints excluded.\n')
count=0
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in sorted(root.rglob('*')):
  if not f.is_file() or '__pycache__' in f.parts or f.suffix.lower() in {'.zip','.pyc','.pdf','.jpg','.jpeg','.png','.fmt','.aux'}:continue
  z.write(f,f.relative_to(root));count+=1
 qa=workspace/'MPL_64_116-157_qa'
 for f in sorted(qa.rglob('*')):
  if not f.is_file():continue
  rel=f.relative_to(qa)
  if f.name in {'compile_harness.py','dummy_fragment.tex','HARNESS_ASSUMPTIONS.txt','compile.stdout.txt','compile.stderr.txt','main.log'}:
   z.write(f,Path('documentation/qa')/rel);count+=1
print(f'Checkpoint: {out}\nFiles: {count}\nBytes: {out.stat().st_size}')
