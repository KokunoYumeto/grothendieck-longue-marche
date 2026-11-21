from pathlib import Path
from datetime import datetime,timezone
import json,zipfile,sys
root=Path(__file__).resolve().parents[1]
log=root/'progress.log'
start=datetime.strptime(log.read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
state=root/'work/checkpoints.json'
s=json.loads(state.read_text()) if state.exists() else []
last=datetime.fromisoformat(s[-1]['created_at']) if s else start
elapsed=(now-last).total_seconds()
if elapsed < 2700:
 print(json.dumps({'due':False,'seconds_until_due':round(2700-elapsed)}));raise SystemExit
n=len(s)+1
out=root.parent/'deliveries'/f'SP81_C13_147+148_checkpoint_{n:02d}.zip';out.parent.mkdir(exist_ok=True)
assert not out.exists()
files=[p for p in root.rglob('*') if p.is_file() and not any(part=='__pycache__' for part in p.parts) and 'packets' not in p.relative_to(root).parts]
# Packets reproduce attached witnesses/rules, so they are excluded with source materials.
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(files):z.write(p,p.relative_to(root).as_posix())
s.append({'number':n,'file':out.name,'created_at':now.isoformat(),'file_count':len(files),'library_file_id':None})
state.write_text(json.dumps(s,indent=2)+'\n')
with log.open('a') as f:f.write(f'checkpoint {n:02d} created {now.strftime("%Y-%m-%d %H:%M:%S UTC")} {out.name}: {len(files)} files; durable save pending\n')
print(json.dumps({'due':True,'file':str(out),'bytes':out.stat().st_size,'number':n}))
