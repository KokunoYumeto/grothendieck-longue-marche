#!/usr/bin/env python3
"""Create a new full checkpoint only when the 45-minute interval has elapsed."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import json, zipfile, hashlib
b=Path(__file__).resolve().parent.parent.parent; out=b/'out'; meta=b/'work/checkpoint_state.json'
start=datetime.strptime((out/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
durable_state=out/'records/checkpoint_schedule.json'
state=json.loads(meta.read_text()) if meta.exists() else (json.loads(durable_state.read_text()) if durable_state.exists() else {'last':start.isoformat(),'count':0,'files':[]})
now=datetime.now(timezone.utc); elapsed=(now-datetime.fromisoformat(state['last'])).total_seconds()
if elapsed<2700:
    print(json.dumps({'due':False,'seconds_until_due':round(2700-elapsed)}));raise SystemExit(0)
nn=state['count']+1; dest=b/'deliverables'/f'SP54_CW_57+63_checkpoint_{nn:02d}.zip';dest.parent.mkdir(exist_ok=True)
if dest.exists():raise SystemExit('Checkpoint path already exists; refusing to overwrite.')
with (out/'progress.log').open('a') as f:f.write('checkpoint '+dest.name+' '+now.strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
state['last']=now.isoformat();state['count']=nn;state['files'].append(str(dest));durable_state.write_text(json.dumps(state,indent=2))
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(out.rglob('*')):
        if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:z.write(p,p.relative_to(out))
meta.write_text(json.dumps(state,indent=2))
print(json.dumps({'due':True,'file':str(dest),'size_bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
