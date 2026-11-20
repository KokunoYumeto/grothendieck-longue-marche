"""At each 45-minute boundary package current work, excluding inputs and prior ZIPs."""
from pathlib import Path
from datetime import datetime,timezone
import csv, zipfile, json

OUT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
start=datetime.strptime((OUT/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
history=OUT/'checkpoint_history.tsv'
records=list(csv.DictReader(history.open(),delimiter='\t')) if history.exists() else []
last=datetime.fromisoformat(records[-1]['created_utc']) if records else start
due=(now-last).total_seconds()>=2700
if not due:
    print(json.dumps({'due':False,'seconds_until_due':round(2700-(now-last).total_seconds())}))
else:
    name=f'SP48_CW_104_checkpoint_{len(records)+1:02d}.zip'
    target=OUT.parent/'checkpoints'/name;target.parent.mkdir(exist_ok=True)
    if target.exists(): raise RuntimeError('Refusing to overwrite a checkpoint')
    with history.open('a',newline='') as f:
        w=csv.writer(f,delimiter='\t')
        if not records: w.writerow(['filename','created_utc'])
        w.writerow([name,now.isoformat()])
    with (OUT/'progress.log').open('a') as f:f.write(f'checkpoint {name} created {now:%Y-%m-%d %H:%M:%S UTC}\n')
    paths=[p for p in sorted(OUT.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
    with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in paths:z.write(p,p.relative_to(OUT))
    print(json.dumps({'due':True,'file':str(target),'bytes':target.stat().st_size,'entries':len(paths)}))
