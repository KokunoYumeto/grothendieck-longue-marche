from pathlib import Path
import datetime,zipfile,json
OUT=Path(__file__).resolve().parents[1]
BASE=OUT.parent
now=datetime.datetime.now(datetime.timezone.utc)
log=OUT/'progress.log'
start=datetime.datetime.strptime(log.read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=datetime.timezone.utc)
record=OUT/'checkpoint_records.json'
records=json.loads(record.read_text()) if record.exists() else []
last=datetime.datetime.fromisoformat(records[-1]['utc']) if records else start
elapsed=(now-last).total_seconds()
if elapsed<2700:
 print(json.dumps({'checkpoint_due':False,'minutes_until':round((2700-elapsed)/60,1)}));raise SystemExit
n=len(records)+1;name=f'SP52_CW_156-4+156-6_checkpoint_{n:02d}.zip'
if (BASE/name).exists():raise SystemExit('Checkpoint filename already exists; never overwrite an earlier checkpoint.')
files=[p for p in OUT.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts and 'packets' not in p.parts and p != OUT/'PREAMBLE.tex']
rec={'number':n,'filename':name,'utc':now.isoformat(),'files':[str(p.relative_to(OUT)) for p in files],'status':'created; durable save pending'}
records.append(rec);record.write_text(json.dumps(records,indent=2))
with log.open('a') as f:f.write(f'checkpoint {n:02d} created {now.strftime("%Y-%m-%d %H:%M:%S UTC")}\n')
files=[p for p in OUT.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts and 'packets' not in p.parts and p != OUT/'PREAMBLE.tex']
with zipfile.ZipFile(BASE/name,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:z.write(p,p.relative_to(OUT))
print(json.dumps({'checkpoint_due':True,'file':str(BASE/name),'size':(BASE/name).stat().st_size,'number':n}))
