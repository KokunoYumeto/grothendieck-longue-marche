"""Create a full work checkpoint only when the 45-minute interval is due."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,zipfile,sys
OUT=Path(__file__).resolve().parents[1]; ROOT=OUT.parent
state_path=OUT/'checkpoint_state.json'
state=json.loads(state_path.read_text())
now=datetime.now(timezone.utc)
last=datetime.strptime(state['last_checkpoint_utc'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
due=last+timedelta(minutes=45)
if now<due:
    print(json.dumps({'due':False,'next_due_utc':due.strftime('%Y-%m-%d %H:%M:%S UTC'),'seconds_remaining':round((due-now).total_seconds())}));sys.exit()
if len(sys.argv)<2 or sys.argv[1]!='create':
    print(json.dumps({'due':True,'next_number':state['next_number']}));sys.exit()
n=state['next_number']; name=f'SP53_CW_156-6_checkpoint_{n:02}.zip'
dest=ROOT/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
assert not dest.exists(), 'Checkpoint names may never be reused'
stamp=now.strftime('%Y-%m-%d %H:%M:%S UTC')
with (OUT/'progress.log').open('a') as f:f.write(f'checkpoint {n:02} created {stamp}: {name}\n')
state.update(last_checkpoint_utc=stamp,next_number=n+1)
state_path.write_text(json.dumps(state,indent=2)+'\n')
files=[p for p in sorted(OUT.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
(OUT/'CHECKPOINT_FILES.txt').write_text('\n'.join(str(p.relative_to(OUT)) for p in files)+'\n')
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(OUT.rglob('*')):
        if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:z.write(p,p.relative_to(OUT))
print(json.dumps({'due':True,'created':str(dest),'bytes':dest.stat().st_size,'number':n}))
