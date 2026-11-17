"""Package deliverables/work records, never supplied scans or context sources."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, zipfile, hashlib, json

ROOT=Path(__file__).resolve().parents[2]
DEL=ROOT/'deliverable'
PREFIX='MPL_108+112+113+114+115'
p=argparse.ArgumentParser()
p.add_argument('--checkpoint',type=int)
a=p.parse_args()
name=PREFIX+(f'_checkpoint_{a.checkpoint:02}' if a.checkpoint else '')+'.zip'
target=ROOT/name
if target.exists(): raise SystemExit('Refusing to overwrite existing archive: '+name)
when=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (DEL/'progress.log').open('a') as f:
    f.write(('checkpoint '+f'{a.checkpoint:02}'+' assembled ' if a.checkpoint else 'final archive assembled ')+when+'\n')
files=[]
for src in sorted(DEL.rglob('*')):
    if src.is_file() and '__pycache__' not in src.parts:
        files.append((src,str(src.relative_to(DEL))))
for src in sorted((ROOT/'library_helpers').glob('*.py')):
    files.append((src,'work_records/library_helpers/'+src.name))
for src in sorted(ROOT.glob('*.py')):
    files.append((src,'work_records/root_scripts/'+src.name))
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for src,arcname in files:z.write(src,arcname)
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    names=z.namelist()
    assert len(names)==len(set(names))
    assert not any(n.startswith(('upload/','context/','scans/')) for n in names)
print(json.dumps({'path':str(target),'files':len(files),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'time':when}))
