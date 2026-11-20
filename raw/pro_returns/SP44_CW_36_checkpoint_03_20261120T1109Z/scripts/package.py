"""Package all current deliverables and work records, without source attachments.

Packets contain copies of supplied witnesses and are reproducible by
prepare_packets.py, so they are excluded. The checkpoint interval is enforced.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, zipfile, hashlib

p=argparse.ArgumentParser();p.add_argument('--final',action='store_true');a=p.parse_args()
out=Path(__file__).resolve().parents[1]; root=out.parent
now=datetime.now(timezone.utc)
state=out/'checkpoint_index.json'
history=json.loads(state.read_text()) if state.exists() else []
start=datetime.fromisoformat((out/'progress.log').read_text().splitlines()[0].replace('Z','+00:00'))
last=datetime.fromisoformat(history[-1]['utc']) if history else start
if not a.final and (now-last).total_seconds()<2700:
    raise SystemExit(f'Not due; {(2700-(now-last).total_seconds()):.0f} seconds remain')
name='SP44_CW_36.zip' if a.final else f'SP44_CW_36_checkpoint_{len(history)+1:02d}.zip'
dest=root/name
if dest.exists(): raise SystemExit('Refusing overwrite '+str(dest))
files=[f for f in sorted(out.rglob('*')) if f.is_file() and 'packets' not in f.relative_to(out).parts and '__pycache__' not in f.parts and f.suffix!='.zip']
if not a.final:
    history.append({'name':name,'utc':now.isoformat(),'file_count':len(files),'library_file_id':None})
    state.write_text(json.dumps(history,indent=2))
    if state not in files: files.append(state)
with (out/'progress.log').open('a') as f: f.write(('final archive' if a.final else 'checkpoint')+' '+name+' '+now.isoformat()+'\n')
with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for f in files: z.write(f,f.relative_to(out))
print(json.dumps({'path':str(dest),'size_bytes':dest.stat().st_size,'files':len(files),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
