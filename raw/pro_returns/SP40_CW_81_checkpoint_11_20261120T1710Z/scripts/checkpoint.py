"""Create a complete non-overwriting checkpoint, only when its 45-minute interval is due."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import zipfile,json,hashlib
root=Path(__file__).resolve().parents[1]
base=root.parent
now=datetime.now(timezone.utc)
start=datetime.strptime((root/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
last=start
history=root/'checkpoint_history.json'
entries=json.loads(history.read_text()) if history.exists() else []
if entries:last=datetime.fromisoformat(entries[-1]['created_utc'])
if now-last<timedelta(minutes=45):
    print(json.dumps({'due':False,'next_due':(last+timedelta(minutes=45)).isoformat()}));raise SystemExit
num=len(entries)+1
name=f'SP40_CW_81_checkpoint_{num:02d}.zip'
dest=base/name
if dest.exists():raise RuntimeError('Refusing to overwrite a checkpoint')
entry={'name':name,'created_utc':now.isoformat(),'prior_checkpoints':[x['name'] for x in entries]}
entries.append(entry);history.write_text(json.dumps(entries,indent=2)+'\n')
with (root/'progress.log').open('a') as f:f.write(f'checkpoint {num:02d} created {now.strftime("%Y-%m-%d %H:%M:%S UTC")}\n')
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:z.write(p,p.relative_to(root))
print(json.dumps({'due':True,'file':str(dest),'size':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
