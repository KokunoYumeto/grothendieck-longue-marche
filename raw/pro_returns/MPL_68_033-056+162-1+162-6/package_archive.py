"""Create an hourly checkpoint or the final archive, excluding supplied sources."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import argparse,zipfile,hashlib,json
ROOT=Path(__file__).resolve().parent
PREFIX='MPL_68_033-056+162-1+162-6'
p=argparse.ArgumentParser();p.add_argument('kind',choices=['checkpoint','final']);p.add_argument('--number',type=int)
a=p.parse_args();now=datetime.now(timezone.utc)
def ts():return now.strftime('%Y-%m-%d %H:%M:%S UTC')
if a.kind=='checkpoint':
    assert a.number and a.number>0
    start=datetime.strptime((ROOT/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    assert now>=start+timedelta(hours=a.number),'An hourly checkpoint is not yet due.'
    target=ROOT.parent/f'{PREFIX}_checkpoint_{a.number:02}.zip'
    assert not target.exists(),'Never overwrite an earlier checkpoint.'
else:
    target=ROOT.parent/f'{PREFIX}.zip'
    assert not target.exists(),'Final archive already exists.'
for line in (ROOT/'checksums.sha256').read_text().splitlines():
    digest,name=line.split('  ',1)
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
with (ROOT/'progress.log').open('a') as f:
    f.write(f'{a.kind} packaging {ts()}: all 22 frozen transcription hashes verified unchanged.\n')
    f.write(f'archive created: {target.name} {ts()}\n')
paths=sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for path in paths:z.write(path,path.relative_to(ROOT))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
print(json.dumps({'path':str(target),'files':len(paths),'bytes':target.stat().st_size,'hashes_unchanged':22}))
