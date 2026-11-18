#!/usr/bin/env python3
"""Record a completed visual audit performed by the root reader; no OCR."""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.load(sys.stdin)
scan = int(data['scan'])
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if data.get('sheet_kind') or data.get('extra_elements'):
    p = root / 'MPL_93_047-091_inventory.csv'
    with p.open(newline='') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    for row in rows:
        if int(row['scan']) == scan and data.get('sheet_kind'):
            row['sheet_kind'] = data['sheet_kind']
    existing = [row for row in rows if int(row['scan']) == scan]
    for i, (kind, position, words) in enumerate(data.get('extra_elements', []), len(existing)+1):
        rows.append(dict(cote='93', scan=str(scan), sheet_kind=data.get('sheet_kind', existing[0]['sheet_kind']),
                         element=f'{scan:03d}.{i:02d}', kind=kind, position=position,
                         first_words_or_objects=words, transcribed='yes'))
    with p.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r:(int(r['scan']), r['element'])))
with (root / 'progress.log').open('a') as f:
    f.write(f'scan {scan:03d} audited {now}\n')
with (root / 'records' / 'visual_audit.md').open('a') as f:
    f.write(f'\n- Scan {scan:03d} — {now}: {data["note"]}\n')
pages = sorted((root / 'pages').glob('MPL_93_047-091_93_scan*.tex'))
(root / 'MPL_93_047-091_transcription.tex').write_bytes(b''.join(p.read_bytes() for p in pages))
print(f'Audit {scan:03d} recorded.')
