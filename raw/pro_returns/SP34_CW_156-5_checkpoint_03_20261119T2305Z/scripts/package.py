#!/usr/bin/env python3
"""Package complete current work, excluding original material and older ZIPs."""
from pathlib import Path
import argparse,zipfile,datetime,json
O=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--checkpoint',action='store_true');a=p.parse_args()
statefile=O/'documentation/run.json';s=json.loads(statefile.read_text());now=datetime.datetime.now(datetime.timezone.utc)
if a.checkpoint:
    last=datetime.datetime.fromisoformat(s['last_checkpoint_utc'].replace('Z','+00:00'))
    if (now-last).total_seconds()<2700:raise SystemExit('Checkpoint not due; no archive written.')
    n=s['checkpoint_number']+1;name=f'SP34_CW_156-5_checkpoint_{n:02}.zip'
    s['checkpoint_number']=n;s['last_checkpoint_utc']=now.isoformat(timespec='seconds').replace('+00:00','Z')
    statefile.write_text(json.dumps(s,indent=2)+'\n')
    with (O/'progress.log').open('a') as f:f.write('checkpoint '+name+' prepared '+s['last_checkpoint_utc']+'\n')
else:name='SP34_CW_156-5.zip'
dest=O.parent/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
if a.checkpoint and dest.exists():raise SystemExit('Refusing to overwrite an earlier checkpoint')
with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for f in sorted(O.rglob('*')):
        if f.is_file() and f.suffix.lower() not in {'.zip','.jpg','.jpeg','.png'} and '__pycache__' not in f.parts:
            z.write(f,f.relative_to(O))
print(dest)
