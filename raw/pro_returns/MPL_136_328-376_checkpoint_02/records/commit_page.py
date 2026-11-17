"""Append a visually completed page's inventory and reading ledger, then timestamp it.

Input is JSON on stdin. This script does not inspect or recognize images.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys

root = Path(__file__).resolve().parents[1]
data = json.load(sys.stdin)
scan = int(data['scan'])
page = root / 'pages' / f'MPL_136_328-376_136_scan{scan:03}.tex'
assert page.exists(), page
assert f'\\scanpage{{{scan}}}' in page.read_text(encoding='utf-8')
with (root / 'MPL_136_328-376_inventory.csv').open('a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i, row in enumerate(data['elements'], 1):
        kind, position, opening = row
        writer.writerow([136, scan, data.get('sheet_kind', 'text'), f'{scan}.{i:02}', kind, position, opening, 'yes'])
ledger = root / 'records' / 'reading_ledger.jsonl'
with ledger.open('a', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False) + '\n')
doubts = root / 'MPL_136_328-376_doubts.md'
s = doubts.read_text(encoding='utf-8')
newrows = ''.join('| 136 | ' + str(scan) + ' | ' + ' | '.join(str(x).replace('|','\\|').replace('\n',' ') for x in row) + ' |\n' for row in data.get('doubts', []))
s = s.replace('\n# Abbreviations\n', newrows + '\n# Abbreviations\n')
newabbr = ''.join('| ' + str(a).replace('|','\\|') + ' | ' + str(b).replace('|','\\|') + ' | ' + str(scan) + ' |\n' for a,b in data.get('abbreviations', []))
s = s.replace('\n# Legibility and limitations\n', newabbr + '\n# Legibility and limitations\n')
newnotation = ''.join('| ' + ' | '.join(str(x).replace('|','\\|') for x in row) + ' |\n' for row in data.get('notation', []))
s = s.replace('\n# Doubts\n', newnotation + '\n# Doubts\n')
doubts.write_text(s, encoding='utf-8')
with (root/'progress.log').open('a',encoding='utf-8') as f:
    f.write(f'136 scan {scan:03} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
print(f'Saved scan {scan}: {len(data["elements"])} inventory elements; {len(data.get("doubts", []))} ledger entries.')
