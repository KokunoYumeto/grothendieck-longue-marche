#!/usr/bin/env python3
"""Record a manually read page. Input JSON is supplied by the sole reader."""
from pathlib import Path
from datetime import datetime, timezone
import json, csv, sys

root=Path(__file__).resolve().parents[1]
data=json.load(sys.stdin)
cote,scan=int(data['cote']),int(data['scan'])
stem=f'MPL_90+91_002-018_{cote}_scan{scan:03}'
page=root/'pages'/f'{stem}.tex'
assert page.is_file()
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
data['completed_utc']=now
(root/'records'/f'{stem}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
records=[json.loads(p.read_text()) for p in sorted((root/'records').glob('MPL_*.json'))]
with (root/'MPL_90+91_002-018_inventory.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f)
    w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
    for r in records:
        for i,el in enumerate(r['elements'],1):
            w.writerow([r['cote'],r['scan'],r['sheet_kind'],f'E{i:02}',*el,'yes'])
combined=''.join(p.read_text() for p in sorted((root/'pages').glob('*.tex')))
(root/'MPL_90+91_002-018_transcription.tex').write_text(combined,encoding='utf-8')
with (root/'progress.log').open('a',encoding='utf-8') as f:
    f.write(f'{cote} scan {scan:03} done {now}\n')
with (root/'records'/'reading_notes.md').open('a',encoding='utf-8') as f:
    f.write(f"\n## {cote} scan {scan:03}\n\n{data.get('notes','')}\n")
print(f'{cote} scan {scan:03} recorded at {now}; {len(records)} pages completed.')
