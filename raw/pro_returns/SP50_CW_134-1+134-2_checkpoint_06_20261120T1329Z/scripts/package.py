from pathlib import Path
from datetime import datetime,timezone
import argparse,json,zipfile,hashlib,csv
O=Path(__file__).resolve().parents[1];P='SP50_CW_134-1+134-2'
p=argparse.ArgumentParser();p.add_argument('--checkpoint',action='store_true');p.add_argument('--final',action='store_true');a=p.parse_args()
assert a.checkpoint!=a.final
s=json.loads((O/'state.json').read_text());now=datetime.now(timezone.utc);fmt='%Y-%m-%d %H:%M:%S UTC'
if a.checkpoint:
    elapsed=(now-datetime.strptime(s['last_checkpoint_utc'],fmt).replace(tzinfo=timezone.utc)).total_seconds()
    if elapsed<2700:
        print(json.dumps({'due':False,'seconds_until_due':round(2700-elapsed)}));raise SystemExit(0)
    name=f"{P}_checkpoint_{s['next_checkpoint']:02d}.zip"
else:
    assert len(s['completed'])==29,'Not all pages complete'
    name=P+'.zip'
dest=O.parent/'deliveries'/name;dest.parent.mkdir(exist_ok=True)
assert not dest.exists(),'Never overwrite a checkpoint or final ZIP'
with (O/'progress.log').open('a') as f:f.write(('checkpoint archive created ' if a.checkpoint else 'final archive prepared ')+now.strftime(fmt)+' '+name+'\n')
files=sorted(f for f in O.rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc' and f.name!='PACKAGE_MANIFEST.tsv')
snapshot={}
for q in files:
    for attempt in range(3):
        before=q.stat();data=q.read_bytes();after=q.stat()
        if before.st_size==after.st_size==len(data) and before.st_mtime_ns==after.st_mtime_ns:break
    else:raise RuntimeError('File is changing during checkpoint: '+str(q))
    snapshot[str(q.relative_to(O))]=data
with (O/'PACKAGE_MANIFEST.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['path','bytes','sha256'])
    for name,data in snapshot.items():w.writerow([name,len(data),hashlib.sha256(data).hexdigest()])
snapshot['PACKAGE_MANIFEST.tsv']=(O/'PACKAGE_MANIFEST.tsv').read_bytes()
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for name,data in snapshot.items():z.writestr(name,data)
print(json.dumps({'due':True,'path':str(dest),'bytes':dest.stat().st_size,'created_utc':now.strftime(fmt),'checkpoint_number':s['next_checkpoint'] if a.checkpoint else None}))
