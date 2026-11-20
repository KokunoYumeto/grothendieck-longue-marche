"""Merge a separately adjudicated full second reading; never perform image inference."""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, subprocess

root = Path(__file__).resolve().parents[1]
page = sys.argv[1]
record_path = root / 'state' / f'{page}_accepted.json'
record = json.loads(record_path.read_text())
audit = json.loads((root / 'audits' / f'{page}.json').read_text())
review = json.loads((root / 'state' / f'{page}_audit_main_review.json').read_text())
if not review.get('approved'):
    raise SystemExit('Main-reader audit adjudication is required.')
first = str(record['reader']).split('/')[-1]
second = str(audit['auditor']).split('/')[-1]
if audit.get('page') != page or str(audit.get('first_reader', '')).split('/')[-1] != first:
    raise SystemExit('Audit page or first-reader identity does not match the accepted record.')
if first == second:
    raise SystemExit('The second reader must differ from the first.')
if record.get('audited_at'):
    raise SystemExit('Audit already accepted; do not duplicate its progress event.')
for finding in audit.get('findings', []):
    category = finding.get('error_category')
    if not isinstance(category, int) or isinstance(category, bool) or not 1 <= category <= 10:
        raise SystemExit('Audit error_category must be an integer from 1 to 10 before integration: '
                         + str(finding.get('id')))

changes = {c['id']: c for c in record.get('changes', [])}
for update in audit.get('comparison_updates', []):
    target = update.get('id')
    if target not in changes:
        raise SystemExit('A comparison update must revise an existing row: ' + str(target))
    category = update.get('error_category', changes[target].get('error_category'))
    if not isinstance(category, int) or isinstance(category, bool) or not 1 <= category <= 10:
        raise SystemExit('Invalid category in comparison update: ' + str(target))
    changes[target].update(update)
for finding in audit.get('findings', []):
    target = finding.get('existing_change_id') or finding['id']
    old = changes.get(target, {})
    merged = dict(old)
    merged.update({k: v for k, v in finding.items()
                   if k not in {'before', 'existing_change_id', 'page'}})
    merged['id'] = target
    changes[target] = merged
record['changes'] = list(changes.values())
marks = {m['id']: m for m in record.get('marks', [])}
for mark in audit.get('marks_updates', []):
    if mark['id'] not in marks:
        raise SystemExit('Audit tried to introduce an unknown source mark.')
    marks[mark['id']] = mark
record['marks'] = list(marks.values())
for mark in record['marks']:
    if isinstance(mark.get('crop'), dict):
        mark['crop'] = mark['crop'].get('path', '') + ' ' + str(mark['crop'].get('box', ''))
inventory = {e['element']: e for e in record.get('inventory', [])}
for element in audit.get('inventory_updates', []):
    inventory[element['element']] = element
inventory_order = audit.get('inventory_order')
if inventory_order is not None:
    if len(inventory_order) != len(inventory) or set(inventory_order) != set(inventory):
        raise SystemExit('Explicit audit inventory order must name every element exactly once.')
    record['inventory'] = [inventory[element] for element in inventory_order]
else:
    record['inventory'] = list(inventory.values())
record['remaining_doubts'] = audit['remaining_doubts']
record['audit_notes'] = audit.get('notes', '')
record['audit_main_review'] = review
record['auditor'] = audit['auditor']
record['audited_at'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
for event in audit.get('check_events', []):
    event = dict(event)
    event.setdefault('date', record['audited_at'].split(' ')[0])
    event.setdefault('who', 'GPT-6 Astra Pro; effort not exposed; ' + audit['auditor'] + '; independent second reading, SP73_C13_142+143 run')
    record.setdefault('check_events', []).append(event)
for key in ('notation', 'hand_log'):
    record.setdefault(key, []).extend(audit.get(key, []))
record.setdefault('crop_boxes', {}).update(audit.get('crop_boxes', {}))
(root / 'pages' / f'{page}.tex').write_text((root / 'audits' / f'{page}.tex').read_text())
record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2))
subprocess.run([sys.executable, str(root / 'scripts' / 'build_reports.py')], check=True)
cote, scan = page.split('_scan')
with (root / 'progress.log').open('a') as stream:
    stream.write(f'scan {scan} audited {record["audited_at"]} cote {cote}\n')
print('Accepted second reading of ' + page)
