#!/usr/bin/env python3
"""Clarify foreground-source metadata from the completed visual reading.

This touches inventory metadata only, never the frozen page/combined files.
Mirrored show-through is evidence of paper reuse, not foreground typed text.
"""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib

root=Path(__file__).resolve().parent.parent
manifest=root/'records/frozen_hashes.sha256'
frozen=[row.split('  ',1) for row in manifest.read_text().splitlines()]
for digest,name in frozen:assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
typed=set(range(5,50,2))
changes=[]
for scan in range(2,50):
 p=root/'records'/f'scan{scan:03}.json';d=json.loads(p.read_text())
 target='reused_typed' if scan in typed else 'cover' if scan==46 else 'text'
 initial=d.get('sheet_kind','text')
 if initial!=target:
  d['sheet_kind_initial']=initial
  d['sheet_kind']=target
  d['classification_note']='Final metadata convention: classify the visible foreground source. Handwritten subject notes remain text even when mirrored reverse-side typing shows through; the heading-only scan046 is a title sheet (cover). This uses the recorded visual reading and does not alter frozen text.'
  p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
  changes.append([scan,initial,target])
p=root/'MPL_33_002-049_inventory.csv'
with p.open(newline='') as f:
 reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
for row in rows:
 scan=int(row['scan']);row['sheet_kind']='reused_typed' if scan in typed else 'cover' if scan==46 else 'text'
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
for digest,name in frozen:assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
with (root/'progress.log').open('a') as f:
 f.write('inventory foreground classification clarified '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+' — mirrored show-through separated from foreground sources; 24 text, 23 reused_typed, 1 title sheet (cover); all 49 frozen hashes unchanged\n')
(root/'records/inventory_classification_clarification.json').write_text(json.dumps({'changes':changes,'frozen_hashes_unchanged':49},indent=2)+'\n')
print('Inventory metadata clarified; 24 text, 23 reused_typed, 1 title sheet; 49 frozen files unchanged.')
