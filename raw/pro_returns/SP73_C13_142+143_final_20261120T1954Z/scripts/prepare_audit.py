"""Prepare one independent second reading after all first readings are accepted."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import sys

root = Path(__file__).resolve().parents[1]
page, auditor = sys.argv[1:3]
auditor = auditor.split('/')[-1]
pages = [f'142_scan{n:03}' for n in
         [101,102,103,104,106,108,109,110,111,112,113,114,115,116,117,118,120,121]]
pages += [f'143_scan{n:03}' for n in range(2,8)]
records = {}
for name in pages:
    p = root / 'state' / f'{name}_accepted.json'
    if not p.exists():
        raise SystemExit('All 24 first readings must be accepted before any audit.')
    records[name] = json.loads(p.read_text())
    if not records[name].get('main_review', {}).get('approved'):
        raise SystemExit('A first reading lacks main-reader approval: ' + name)

record = records[page]
if record['reader'].split('/')[-1] == auditor:
    raise SystemExit('Second reader must differ from first reader.')
assignments_path = root / 'state' / 'assignments.tsv'
with assignments_path.open(newline='') as stream:
    assignments = list(csv.DictReader(stream, delimiter='\t'))
unassigned = [row['page'] for row in assignments if not row['second_reader']]
if not unassigned or unassigned[0] != page:
    raise SystemExit('Assign audits in the supplied page order.')
packet_path = root / 'state' / f'{page}_audit_packet.json'
if packet_path.exists():
    raise SystemExit('Audit packet already exists; do not duplicate assignment.')
packet = json.loads((root / 'state' / f'{page}_packet.json').read_text())
crop_index = dict(record.get('crop_boxes', {}))
for evidence in record.get('changes', []) + record.get('marks', []):
    crop, box = evidence.get('crop'), evidence.get('box')
    if crop and crop != 'page' and isinstance(box, list) and len(box) == 4:
        if crop in crop_index and crop_index[crop] != box:
            raise SystemExit('Conflicting evidence box: ' + crop)
        crop_index[crop] = box
packet.update({
    'auditor': auditor,
    'first_reader': record['reader'],
    'consolidated_text': str(root / 'pages' / f'{page}.tex'),
    'notation': (root / 'state' / 'notation.md').read_text(),
    'existing_crop_index': crop_index,
    'change_id_index': [{k: change.get(k) for k in ('id','place','crop','box')}
                        for change in record.get('changes', [])],
    'inventory': record.get('inventory', []),
    'current_mark_decisions': record.get('marks', []),
    'current_remaining_doubts': record.get('remaining_doubts', []),
    'instructions': str(root / 'state' / 'audit_instructions.md'),
})
packet_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2))
for row in assignments:
    if row['page'] == page:
        row['second_reader'] = auditor
with assignments_path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=['page','first_reader','second_reader'], delimiter='\t')
    writer.writeheader()
    writer.writerows(assignments)
with (root / 'progress.log').open('a') as stream:
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    stream.write(f'audit assigned {page} to {auditor} {stamp}\n')
print(packet_path)
