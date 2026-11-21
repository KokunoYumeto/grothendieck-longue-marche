"""Close an image-only second reading after the main reader adjudicates it.

This script does not decide readings. The main reader must inspect each differing
box and supply <page>_adjudications.json, with one entry for every nonidentical box:
box, final, outcome, evidence, crop, changed. Any transcription/log corrections
must already have been made. Identical boxes remain documented in comparison.json.
"""
from pathlib import Path
import json, sys
from aggregate import W, now, aggregate, write_tsv

page = sys.argv[1]
base = W / 'second'
comparison = json.loads((base / f'{page}_comparison.json').read_text())
adjudications = json.loads((base / f'{page}_adjudications.json').read_text())
expected = [r['box'] for r in comparison if not r['token_equal']]
if [r['box'] for r in adjudications] != expected:
    raise ValueError('Every differing box must be adjudicated, in order: ' + page)
for r in adjudications:
    for field in ('final', 'outcome', 'evidence', 'crop', 'changed'):
        if field not in r:
            raise ValueError(f'{page} {r["box"]}: missing {field}')
    if not (W / r['crop']).exists():
        raise ValueError('Adjudication crop is missing: ' + r['crop'])

report_path = W / 'reports' / page / 'report.json'
report = json.loads(report_path.read_text())
if not report.get('main_reviewed'):
    raise ValueError('First reading has not been finalized')
if report.get('audited_utc'):
    raise ValueError('Audit already finalized; do not duplicate its progress entry')
assignment = json.loads((base / f'{page}_assignment.json').read_text())
if assignment['reader'] == report['reader']:
    raise ValueError('The independent reader also performed this page first reading')

by_box = {r['box']: r for r in adjudications}
rows = []
for r in comparison:
    a = by_box.get(r['box'])
    rows.append(dict(box=r['box'], first=r['first'], second=r['second'],
        final=a['final'] if a else r['first'],
        outcome=a['outcome'] if a else 'Token-identical independent reading',
        evidence=a['evidence'] if a else 'Both independently written token streams agree.',
        crop=a['crop'] if a else f'crops/{page}_second_{r["box"]}.png',
        changed='yes' if a and a['changed'] else 'no'))
write_tsv(base / f'{page}_adjudicated.tsv',
          ['box', 'first', 'second', 'final', 'outcome', 'evidence', 'crop', 'changed'], rows)
stamp = now()
report['audited_utc'] = stamp
report['second_reader'] = assignment['reader']
report['audit_counts'] = dict(boxes=len(comparison),
    differing_boxes=len(expected),
    token_edit_spans=sum(len(r['differences']) for r in comparison),
    changed_boxes=sum(bool(r['changed']) for r in adjudications))
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
scan = page.split('_scan')[1]
with (W / 'progress.log').open('a') as f:
    f.write(f'scan {scan} audited {stamp}: {len(comparison)} boxes read, '
            f'{len(expected)} differences, '
            f'{report["audit_counts"]["changed_boxes"]} changed\n')
aggregate()
print(page, report['audit_counts'])
