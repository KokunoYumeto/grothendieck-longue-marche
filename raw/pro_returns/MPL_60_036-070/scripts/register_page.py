#!/usr/bin/env python3
"""Register a manually read, saved page; no OCR or inference is performed."""
import csv, json, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
d=json.load(sys.stdin); scan=int(d['scan']); kind=d.get('sheet_kind','text')
page=root/'pages'/f'MPL_60_036-070_60_scan{scan:03}.tex'
assert page.is_file()
with (root/'MPL_60_036-070_inventory.csv').open('a',newline='',encoding='utf-8') as f:
    w=csv.writer(f)
    for i,e in enumerate(d['elements'],1):
        w.writerow([60,scan,kind,f'{scan:03}-{i:02}',*e,'yes'])
(root/'records'/f'scan{scan:03}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (root/'progress.log').open('a',encoding='utf-8') as f:
    f.write(f'60 scan {scan:03} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
pages=sorted((root/'pages').glob('MPL_60_036-070_60_scan*.tex'))
(root/'MPL_60_036-070_transcription.tex').write_bytes(b''.join(p.read_bytes() for p in pages))
print(f'Registered scan {scan:03}; {len(pages)} pages saved.')
