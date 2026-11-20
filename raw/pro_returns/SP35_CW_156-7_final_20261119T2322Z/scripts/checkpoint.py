#!/usr/bin/env python3
"""Create a cumulative checkpoint only when its 45-minute interval is due."""
from pathlib import Path
from datetime import datetime,timezone
import zipfile,json,csv
root=Path(__file__).resolve().parents[1];dest=root.parent/'deliverables';dest.mkdir(exist_ok=True)
now=datetime.now(timezone.utc);started=datetime.strptime((root/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
reg=root/'records/checkpoints.tsv'
rows=[]
if reg.exists():
 with reg.open() as f:rows=list(csv.DictReader(f,delimiter='\t'))
last=datetime.fromisoformat(rows[-1]['created_utc']) if rows else started
if (now-last).total_seconds()<2700:
 print(json.dumps({'due':False,'seconds_until_due':round(2700-(now-last).total_seconds())}));raise SystemExit(0)
n=len(rows)+1;name=f'SP35_CW_156-7_checkpoint_{n:02d}.zip';archive=dest/name
if archive.exists():raise SystemExit('Refusing to overwrite checkpoint')
rows.append({'number':str(n),'filename':name,'created_utc':now.isoformat(),'library_file_id':'pending save'})
with reg.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['number','filename','created_utc','library_file_id'],delimiter='\t');w.writeheader();w.writerows(rows)
with (root/'progress.log').open('a') as f:f.write(f'checkpoint {n:02d} created {now.strftime("%Y-%m-%d %H:%M:%S UTC")} {name}\n')
files=[p for p in sorted(root.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:z.write(p,p.relative_to(root))
print(json.dumps({'due':True,'archive':str(archive),'bytes':archive.stat().st_size,'files':len(files),'checkpoint':n}))
