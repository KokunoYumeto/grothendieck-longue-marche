#!/usr/bin/env python3
"""Package current deliverables/work records, never supplied sources or scans."""
from pathlib import Path
import datetime, sys, zipfile
root=Path(__file__).resolve().parents[1]
mode=sys.argv[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if mode=='checkpoint':
    number=int(sys.argv[2])
    target=root.parent/f'{root.name}_checkpoint_{number:02d}.zip'
    message=f'hourly checkpoint {number:02d} packaged {stamp}'
elif mode=='final':
    target=root.parent/f'{root.name}.zip'
    message=f'final package created {stamp}'
else: raise SystemExit('Use checkpoint NN or final')
if target.exists(): raise SystemExit(f'Refusing to overwrite {target}')
with (root/'progress.log').open('a') as f: f.write(message+'\n')
files=[p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.zip'}]
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED) as z:
    for path in files: z.write(path,path.relative_to(root.parent))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
print(f'{target}\n{len(files)} files; {target.stat().st_size} bytes; CRC check passed')
