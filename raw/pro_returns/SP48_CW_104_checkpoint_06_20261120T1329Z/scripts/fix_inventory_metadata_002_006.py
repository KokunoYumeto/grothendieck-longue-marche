from pathlib import Path
from datetime import datetime, timezone
import json, csv, hashlib

out = Path(__file__).resolve().parents[1]
receipt = out / 'records/inventory_metadata_correction_002_006.json'
assert not receipt.exists(), 'This metadata correction has already run'
audit = json.loads((out/'records/inventory_order_audit_002_007.json').read_text())
page_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (out/'pages').glob('*.tex')}
changes = []

p = out/'records/scan002/decision.json'
d = json.loads(p.read_text())
row = next(x for x in d['inventory'] if x['element']=='E25')
assert row['kind']=='margin note' and 'archive' in row['hand']
before = dict(row)
row['kind']='text'
row['classification_note']='Archival digit retained as a TeX comment; this inventory kind is text, with its original unestablished archive-hand attribution.'
p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')
changes.append(dict(scan=2, action='archive digit kind normalized to text', before=before, after=row))

p = out/'records/scan006/decision.json'
d = json.loads(p.read_text())
before = d['inventory']
by_name = {x['element']:x for x in before}
a = next(x for x in audit['scans'] if x['scan']==6)['suggested_row_order']
order = [x['element'] for x in a['order_for_all_located_rows']]
for entry in a['insert_four_unlocated_rows_using_parent_constraints']:
    order.insert(order.index(entry['parent'])+1, entry['element'])
assert len(order)==len(before)==51 and set(order)==set(by_name)
d['inventory']=[by_name[name] for name in order]
d['inventory_order_note']='Supplemental marks are interleaved by recorded coordinates. Four marks without exact coordinates are grouped immediately with their recorded parent element; their cross-column pixel order is not asserted. No image was reopened and no transcription was changed.'
p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')
changes.append(dict(scan=6, action='late-added marks moved to their physical parent groups',
                    before=before, after_order=order, limitation=d['inventory_order_note']))

# Regenerate only the inventory, preserving pending current-page mathematical events.
fields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
rows=[]
for p in sorted((out/'records').glob('scan*/decision.json')):
    d=json.loads(p.read_text())
    for element in d['inventory']:
        rows.append({'scan':str(d['scan']), **{k:element.get(k,'') for k in fields if k!='scan'}})
with (out/'SP48_CW_104_inventory.csv').open('w', newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields)
    w.writeheader(); w.writerows(rows)
assert page_hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (out/'pages').glob('*.tex')}
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
receipt.write_text(json.dumps(dict(date=stamp,scope='Inventory metadata only; text-only audit; no source-image review or mathematical check',changes=changes,page_hashes_unchanged=page_hashes),ensure_ascii=False,indent=2)+'\n')
with (out/'progress.log').open('a') as f:
    f.write(f'Inventory metadata corrected {stamp}: scan002 archive kind; scan006 late-added mark order by recorded coordinates/parent groups. All seven page hashes unchanged; pending scan009 CHECK_EVENTS preserved.\n')
print('Corrected inventory metadata; 270 rows; all seven page hashes unchanged.')
