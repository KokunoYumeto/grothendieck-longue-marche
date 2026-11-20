"""Create a fresh numbered checkpoint only after a 45-minute interval."""
from pathlib import Path
from datetime import datetime,timezone
from zipfile import ZipFile,ZIP_DEFLATED
import json
root=Path(__file__).resolve().parents[1];base=root.parent
statefile=root/'records/checkpoint_state.json'
now=datetime.now(timezone.utc)
state=json.loads(statefile.read_text()) if statefile.exists() else {'number':0,'last_time':(root/'progress.log').read_text().splitlines()[0]}
last=datetime.strptime(state['last_time'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
seconds=(now-last).total_seconds()
if seconds<2700:
    print(json.dumps({'due':False,'remaining_seconds':round(2700-seconds)}));raise SystemExit
n=state['number']+1;name=f'SP51_CW_134-2_checkpoint_{n:02}.zip';dest=base/'deliverables'/name
dest.parent.mkdir(exist_ok=True)
if dest.exists():raise FileExistsError(dest)
stamp=now.strftime('%Y-%m-%d %H:%M:%S UTC')
state.update(number=n,last_time=stamp,filename=name)
statefile.write_text(json.dumps(state,indent=2)+'\n')
with (root/'progress.log').open('a') as f:f.write(f'checkpoint {n:02} prepared {stamp} {name}\n')
files=sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip')
(root/'records/checkpoint_files.txt').write_text('\n'.join(str(p.relative_to(root)) for p in files)+'\n')
with ZipFile(dest,'x',ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip':z.write(p,p.relative_to(root))
print(json.dumps({'due':True,'path':str(dest),'bytes':dest.stat().st_size,'number':n}))
