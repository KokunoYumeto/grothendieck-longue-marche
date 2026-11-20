#!/usr/bin/env python3
"""Build a timed checkpoint or final archive; no source images/witnesses."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,sys,zipfile
root=Path(__file__).resolve().parents[1]
dest=root.parent/'deliverables'
dest.mkdir(exist_ok=True)
statepath=root/'run_state.json'
state=json.loads(statepath.read_text())
now=datetime.now(timezone.utc)
mode=sys.argv[1] if len(sys.argv)>1 else 'status'
due=datetime.fromisoformat(state['last_checkpoint_utc'])+timedelta(minutes=45)
if mode=='status':
    print(json.dumps({'current_utc':now.isoformat(timespec='seconds'),'checkpoint_due_utc':due.isoformat(timespec='seconds'),'seconds_until_due':round((due-now).total_seconds()),'completed_scans':state['completed_scans']},ensure_ascii=False));sys.exit()
if mode=='checkpoint':
    assert now>=due,'No checkpoint before the 45-minute interval.'
    state['checkpoint_number']+=1
    name=f"SP39_CW_75_checkpoint_{state['checkpoint_number']:02}.zip"
    state['last_checkpoint_utc']=now.isoformat(timespec='seconds')
    statepath.write_text(json.dumps(state,indent=2)+'\n')
elif mode=='final':name='SP39_CW_75.zip'
else:raise ValueError(mode)
target=dest/name
assert not target.exists(), 'Never overwrite a checkpoint or an already-created final ZIP.'
with (root/'progress.log').open('a') as f:f.write(mode+' archive prepared '+now.isoformat(timespec='seconds')+' '+name+'\n')
paths=[p for p in sorted(root.rglob('*')) if p.is_file() and not any(x in p.parts for x in ['__pycache__']) and p.suffix not in {'.zip','.png','.jpg','.jpeg','.pdf'} and p != root/'PREAMBLE.tex']
manifest=root/'PACKAGE_CONTENTS.tsv'
manifest.write_text('path\tsize_bytes\tsha256\n'+'\n'.join(f'{p.relative_to(root)}\t{p.stat().st_size}\t{hashlib.sha256(p.read_bytes()).hexdigest()}' for p in paths if p!=manifest)+'\n')
paths=[p for p in paths if p!=manifest]+[manifest]
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in paths:z.write(p,p.relative_to(root))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
print(json.dumps({'file':str(target),'size_bytes':target.stat().st_size,'entries':len(paths),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False))
