"""Create a full checkpoint ZIP only when 45 minutes have elapsed.
Upload it with the Library helper in the same work session. Prior ZIPs remain outside this tree.
"""
from pathlib import Path
from datetime import datetime,timezone
import zipfile,json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'deliveries'
OUT.mkdir(exist_ok=True)
LOG=ROOT/'progress.log'
now=datetime.now(timezone.utc)
ts=now.strftime('%Y-%m-%d %H:%M:%S UTC')
state=ROOT/'records/checkpoints.json'
history=json.loads(state.read_text()) if state.exists() else []
start=LOG.read_text().splitlines()[0]
first=datetime.strptime(start,'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
elapsed=(now-first).total_seconds()
due_seconds=2700*(len(history)+1)
if elapsed<due_seconds:
    print(json.dumps({'checkpoint_due':False,'seconds_until_due':round(due_seconds-elapsed)}))
else:
    name=f'SP47_CW_103_checkpoint_{len(history)+1:02}.zip'
    target=OUT/name
    if target.exists():raise SystemExit('Refusing to overwrite checkpoint')
    history.append({'filename':name,'utc':ts,'library_status':'pending upload'})
    state.write_text(json.dumps(history,indent=2))
    with LOG.open('a') as f:f.write(f'checkpoint {name} created {ts}\n')
    with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:z.write(p,p.relative_to(ROOT))
    print(json.dumps({'checkpoint_due':True,'path':str(target),'size':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}))
