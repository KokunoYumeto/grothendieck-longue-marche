"""Create scheduled checkpoint or final archive; never nest a checkpoint archive."""
from pathlib import Path
from datetime import datetime,timezone
from zipfile import ZipFile,ZIP_DEFLATED
import json,argparse,hashlib
W=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('mode',choices=['due','checkpoint','final']);a=p.parse_args()
state=json.loads((W/'state.json').read_text());now=datetime.now(timezone.utc)
last=datetime.strptime(state['last_checkpoint_utc'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
elapsed=(now-last).total_seconds()
if a.mode=='due':
    print(json.dumps({'elapsed_minutes':round(elapsed/60,1),'due':elapsed>=2700,'next_number':state['checkpoint_number']+1}));raise SystemExit
if a.mode=='checkpoint' and elapsed<2700:raise SystemExit('Checkpoint not due; no archive created.')
if a.mode=='final':
    assert len(state['done'])==27,'Final archive requires all 27 pages.'
    frozen=json.loads((W/'records/frozen_sha256.json').read_text())
    for rel,digest in frozen['files'].items():
        assert hashlib.sha256((W/rel).read_bytes()).hexdigest()==digest,'Frozen file changed: '+rel
    assert 'frozen hashes checked unchanged' in (W/'progress.log').read_text(),'Final recheck must be logged.'
out=W.parent/'deliverables';out.mkdir(exist_ok=True)
num=state['checkpoint_number']+1
name=f'SP49_CW_109_checkpoint_{num:02}.zip' if a.mode=='checkpoint' else 'SP49_CW_109.zip'
dest=out/name
if dest.exists():raise SystemExit('Refusing to overwrite existing archive.')
files=[]
for f in sorted(W.rglob('*')):
    if not f.is_file():continue
    rel=f.relative_to(W)
    if rel.parts[0]=='inputs' or '__pycache__' in rel.parts or f.suffix=='.zip':continue
    files.append((f,rel))
manifest=W/'records'/('checkpoint_'+str(num).zfill(2)+'_file_list.txt' if a.mode=='checkpoint' else 'final_file_list.txt')
manifest.write_text('\n'.join(str(r) for _,r in files)+'\n'+str(manifest.relative_to(W))+'\n')
if not any(f==manifest for f,_ in files):files.append((manifest,manifest.relative_to(W)))
with ZipFile(dest,'x',ZIP_DEFLATED,compresslevel=6) as z:
    for f,rel in files:z.write(f,rel)
print(json.dumps({'file':str(dest),'size_bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'files':len(files),'utc':now.strftime('%Y-%m-%d %H:%M:%S UTC'),'checkpoint_number':num if a.mode=='checkpoint' else None}))
