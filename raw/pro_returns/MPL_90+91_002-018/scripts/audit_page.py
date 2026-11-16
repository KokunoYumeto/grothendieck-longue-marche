#!/usr/bin/env python3
"""Record the sole reader's completed image audit and rebuild derived files."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,csv
root=Path(__file__).resolve().parents[1]
cote,scan=map(int,sys.argv[1:3])
stem=f'MPL_90+91_002-018_{cote}_scan{scan:03d}'
p=root/'records'/f'{stem}.json'
r=json.loads(p.read_text())
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
assert 'audited_utc' not in r, 'Audit already logged; use a reconciliation note for a subsequent check.'
r['audited_utc']=now
if len(sys.argv)>3:r['audit_note']=sys.argv[3]
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
records=[json.loads(p.read_text()) for p in sorted((root/'records').glob('MPL_*.json'))]
with (root/'MPL_90+91_002-018_inventory.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
 for rec in records:
  for i,el in enumerate(rec['elements'],1):w.writerow([rec['cote'],rec['scan'],rec['sheet_kind'],f'E{i:02}',*el,'yes'])
(root/'MPL_90+91_002-018_transcription.tex').write_text(''.join(p.read_text() for p in sorted((root/'pages').glob('*.tex'))))
with (root/'progress.log').open('a') as f:f.write(f'{cote} scan {scan:03d} audited {now}\n')
print(f'{cote} scan {scan:03d} audited {now}')
