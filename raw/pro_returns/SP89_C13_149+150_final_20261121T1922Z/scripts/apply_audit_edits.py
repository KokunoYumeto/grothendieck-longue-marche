"""Apply only explicitly specified main-reader edits after crop adjudication.

Input: second/PAGE_edits.json, with source_replacements, report_updates,
report_appends, and report_removals. This script never selects a reading or
sets collation flags. It preserves the independently written first/second TSVs.
"""
from pathlib import Path
import datetime
import hashlib
import json
import sys

W = Path(__file__).resolve().parents[1]
page = sys.argv[1]
S = W / 'second'
receipt_path = S / f'{page}_edits_receipt.json'
if receipt_path.exists():
    raise RuntimeError('Explicit edits were already applied; do not repeat')
edits = json.loads((S / f'{page}_edits.json').read_text())
decisions = json.loads((S / f'{page}_root_decisions.json').read_text())
comparison = json.loads((S / f'{page}_comparison.json').read_text())
by_box = {x['box']: x for x in comparison}
changed = [x for x in decisions if x['decision'] == 'revise']
source_path = W / 'pages' / f'{page}.tex'
report_path = W / 'reports' / page / 'report.json'
before = source_path.read_text()
after = before
report = json.loads(report_path.read_text())
if report.get('audited_utc'):
    raise RuntimeError('Audit was already finalized')

for replacement in edits.get('source_replacements', []):
    old, new = replacement['old'], replacement['new']
    count = replacement.get('count', 1)
    if not old or after.count(old) != count:
        raise ValueError('Exact source-replacement count does not match')
    after = after.replace(old, new)

def matches(row, selector):
    return all(row.get(k) == v for k, v in selector.items())

for update in edits.get('report_updates', []):
    targets = [x for x in report[update['collection']] if matches(x, update['match'])]
    if len(targets) != 1:
        raise ValueError('A report update must identify exactly one row')
    targets[0].update(update['set'])
for removal in edits.get('report_removals', []):
    rows = report[removal['collection']]
    targets = [x for x in rows if matches(x, removal['match'])]
    if len(targets) != 1:
        raise ValueError('A report removal must identify exactly one row')
    rows.remove(targets[0])
for collection, additions in edits.get('report_appends', {}).items():
    report.setdefault(collection, []).extend(additions)

if changed and before == after:
    raise ValueError('A revised source reading requires an actual page edit')
if not changed and before != after:
    raise ValueError('Source edits require explicit revised-box decisions')
report['audit_changes'] = [
    dict(place=d['box'], first=by_box[d['box']]['first'],
         second=by_box[d['box']]['second'], final=d['final'],
         evidence=d['evidence'],
         crop=d.get('crop', f'crops/{page}_second_{d["box"]}.png'))
    for d in changed
]
receipt = dict(
    page=page,
    applied_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source_before_sha256=hashlib.sha256(before.encode()).hexdigest(),
    source_after_sha256=hashlib.sha256(after.encode()).hexdigest(),
    revised_boxes=[x['box'] for x in changed],
    source_replacements=len(edits.get('source_replacements', [])),
    report_updates=len(edits.get('report_updates', [])),
)
source_path.write_text(after)
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
print(page, len(changed), 'revised boxes applied; original readings preserved')
