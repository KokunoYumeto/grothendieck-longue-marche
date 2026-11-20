from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile, ZIP_DEFLATED
import json,sys
root=Path(__file__).resolve().parents[1]
task=root.parent
now=datetime.now(timezone.utc)
state=root/'state/checkpoints.json'
saved=json.loads(state.read_text()) if state.exists() else []
start=datetime.strptime((root/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
last=datetime.fromisoformat(saved[-1]['created_at']) if saved else start
if (now-last).total_seconds()<2700:
    print(json.dumps({'due':False,'seconds_until_due':round(2700-(now-last).total_seconds())}));sys.exit(0)
number=len(saved)+1
name=f'SP73_C13_142+143_checkpoint_{number:02d}.zip'
dest=task/name
if dest.exists(): raise SystemExit('Never overwrite a checkpoint.')
files=[p for p in sorted(root.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
entry={'name':name,'created_at':now.isoformat(),'files':[str(p.relative_to(root)) for p in files]}
saved.append(entry);state.write_text(json.dumps(saved,indent=2))
with (root/'progress.log').open('a') as f:f.write(f'checkpoint {number:02d} created {now.strftime("%Y-%m-%d %H:%M:%S UTC")}\n')
files=[p for p in sorted(root.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
with ZipFile(dest,'x',compression=ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,p.relative_to(root))
print(json.dumps({'due':True,'path':str(dest),'bytes':dest.stat().st_size,'files':len(files)}))
