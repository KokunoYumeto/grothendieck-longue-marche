"""Write a manually read page and its manually enumerated inventory/doubts."""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.load(sys.stdin)
scan = int(data['scan'])
path = ROOT / 'pages' / f'MPL_12_099-149_12_scan{scan:03d}.tex'
if path.exists():
    raise SystemExit(f'Refusing to overwrite completed page: {path}')
path.write_text(data['text'].rstrip() + '\n', encoding='utf-8')
with (ROOT/'MPL_12_099-149_inventory.csv').open('a', newline='', encoding='utf-8') as f:
    writer=csv.writer(f)
    for i,row in enumerate(data['elements'],1):
        kind,position,opening=row
        writer.writerow(['12',f'{scan:03d}',data.get('sheet_kind','text'),f'{scan:03d}.{i:02d}',kind,position,opening,'yes'])
doubts=ROOT/'MPL_12_099-149_doubts.md'
content=doubts.read_text()
rows=[]
for where,reading,alternatives,confidence in data.get('doubts',[]):
    vals=['12',f'{scan:03d}',where,reading,alternatives,confidence]
    vals=[str(v).replace('|','&#124;').replace('\n',' ') for v in vals]
    rows.append('| '+' | '.join(vals)+' |')
if rows:
    content=content.replace('\n## Abbreviations','\n'+'\n'.join(rows)+'\n\n## Abbreviations')
for visible,latex,observation in data.get('notation',[]):
    content=content.replace('\n## Doubt register','\n| '+visible.replace('|','&#124;')+' | `'+latex.replace('|','&#124;')+'` | '+observation.replace('|','&#124;')+' |\n\n## Doubt register')
if data.get('abbreviations'):
    content=content.replace('To be accumulated from the actual readings.', 'Abbreviations are retained unexpanded in the transcription.')
    content=content.replace('\n## Legibility and limits','\n'+'\n'.join('- '+s for s in data['abbreviations'])+'\n\n## Legibility and limits')
doubts.write_text(content)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'12 scan {scan:03d} done {stamp}\n')
print(f'{path.name}: {len(data["elements"])} inventory elements; {stamp}')
