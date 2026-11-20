"""Checkpoint/final packaging; excludes source attachments and reproducible halves."""
from pathlib import Path
from datetime import datetime, timezone
import zipfile, hashlib, csv, sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parents[1]/'deliverables'
OUT.mkdir(exist_ok=True)
mode=sys.argv[1]
now=datetime.now(timezone.utc)
def utc():return now.strftime('%Y-%m-%d %H:%M:%S UTC')
if mode=='checkpoint':
    previous=sorted(OUT.glob('SP79_C13_147_checkpoint_*.zip'))
    num=len(previous)+1
    start=datetime.strptime((ROOT/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    if (now-start).total_seconds()<45*60*num:
        raise SystemExit('Checkpoint interval has not elapsed; no checkpoint made.')
    name=f'SP79_C13_147_checkpoint_{num:02d}.zip'
else:
    assert mode=='final'
    name='SP79_C13_147.zip'
with (ROOT/'progress.log').open('a') as f:f.write(f'{mode} package {name} {utc()}\n')
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT)
    if 'packets' in rel.parts or '__pycache__' in rel.parts:continue
    if p.name=='governing_instructions.md' or p.suffix=='.zip':continue
    if p.name=='PACKAGE_MANIFEST.tsv':continue
    files.append(p)
# Each included file is read once into this snapshot.  Hashes and ZIP entries
# then use the same bytes, even if a page reader finishes a newer draft while
# packaging is in progress.
snapshot={}
for p in files:
    for attempt in range(3):
        before=p.stat()
        data=p.read_bytes()
        after=p.stat()
        if (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns) and len(data)==after.st_size:
            break
    else:
        raise SystemExit(f'File changed during snapshot: {p}')
    snapshot[str(p.relative_to(ROOT))]=data
with (ROOT/'PACKAGE_MANIFEST.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['path','bytes','sha256'])
    for rel,data in snapshot.items():w.writerow([rel,len(data),hashlib.sha256(data).hexdigest()])
snapshot['PACKAGE_MANIFEST.tsv']=(ROOT/'PACKAGE_MANIFEST.tsv').read_bytes()
target=OUT/name
if mode=='checkpoint' and target.exists():raise SystemExit('Refusing to overwrite earlier checkpoint')
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for rel,data in snapshot.items():z.writestr(rel,data)
print(target)
print('bytes',target.stat().st_size,'files',len(snapshot))
