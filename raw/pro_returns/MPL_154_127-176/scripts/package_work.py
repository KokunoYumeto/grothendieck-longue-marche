#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import argparse,zipfile,hashlib
p=argparse.ArgumentParser();p.add_argument('--checkpoint',type=int);p.add_argument('--final',action='store_true');a=p.parse_args()
r=Path(__file__).resolve().parents[1]
if bool(a.checkpoint)==bool(a.final):p.error('Choose checkpoint number or final')
name=f'MPL_154_127-176_checkpoint_{a.checkpoint:02d}.zip' if a.checkpoint else 'MPL_154_127-176.zip'
out=r.parent/name
if out.exists():raise SystemExit(f'Refusing to overwrite {out}')
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (r/'progress.log').open('a') as f:f.write(f'{name} packaging {t}\n')
files=[q for q in r.rglob('*') if q.is_file() and '__pycache__' not in q.parts and q.suffix not in {'.pyc','.zip'}]
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for q in sorted(files):z.write(q,q.relative_to(r))
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(files)
print(f'{out}\n{len(files)} files; {out.stat().st_size} bytes; SHA256 {hashlib.sha256(out.read_bytes()).hexdigest()}')
