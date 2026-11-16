#!/usr/bin/env python3
"""Create the requested hourly archive without overwriting earlier checkpoints."""
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import sys

root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1])
out=Path(sys.argv[2]).resolve()
out.mkdir(parents=True,exist_ok=True)
name=f'MPL_11_043-058+56_checkpoint_{number:02}.zip'
target=out/name
if target.exists():
    raise SystemExit('Checkpoint already exists; refusing overwrite')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'checkpoint {number:02} created {stamp}\n')
with ZipFile(target,'x',ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts:
            z.write(p,p.relative_to(root))
with ZipFile(target) as z:
    assert z.testzip() is None
    print(f'{target}: {len(z.namelist())} files')
