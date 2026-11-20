"""Commit a fully adjudicated page and rebuild cumulative records."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,importlib.util
out=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);d=out/f'records/scan{n:03d}/decision.json'
decision=json.loads(d.read_text())
folder='H104-01' if n<10 else 'H104-02'
p=out/f'pages/{folder}_104_scan{n:03d}.tex'
if not p.exists():raise RuntimeError('No consolidated page file')
for reader in 'ABC':
    r=out/f'records/scan{n:03d}/reader_{reader}'
    for f in ['reading.tex','report.json','read_log.md']:
        if not (r/f).exists():raise RuntimeError(f'Missing {reader}/{f}')
if not decision.get('main_adjudication_complete'):raise RuntimeError('Main adjudication not complete')
if any(x.get('transcribed')!='yes' for x in decision['inventory']):raise RuntimeError('Incomplete inventory')
allowed_sheets={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
allowed_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
for x in decision['inventory']:
    if x['sheet_kind'] not in allowed_sheets or x['kind'] not in allowed_kinds:raise RuntimeError('Invalid inventory vocabulary')
allowed_collation={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
for x in decision.get('issues',[]):
    if x['confidence'] not in {'high','medium','low'}:raise RuntimeError('Invalid confidence')
    if x.get('diff_H') and x['kind'] not in allowed_collation:raise RuntimeError('Invalid collation kind: '+x['kind'])
    if set(x.get('readers',{}))!={'A','B','C'}:raise RuntimeError('Issue lacks three recorded readings: '+x['id'])
    if x.get('diff_C') or x.get('diff_H'):
        if not x.get('crop'):raise RuntimeError('Changed locus lacks main crop reference: '+x['id'])
    for crop in x.get('crop','').split(';'):
        crop=crop.strip()
        if crop and not (out/crop).exists():raise RuntimeError('Missing adjudication crop: '+crop)
if n>2 and f'scan {n-1:03d} done ' not in (out/'progress.log').read_text():raise RuntimeError('Previous scan not committed')
if f'scan {n:03d} done ' in (out/'progress.log').read_text():raise RuntimeError('Page already committed')
spec=importlib.util.spec_from_file_location('builder',out/'scripts/build_records.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
result=mod.build()
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (out/'progress.log').open('a') as f:f.write(f'scan {n:03d} done {now}\n')
print(json.dumps(result))
