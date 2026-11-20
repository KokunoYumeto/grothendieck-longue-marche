"""Record root's completed crop adjudications; never decide readings automatically."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys, subprocess

root = Path(__file__).resolve().parents[1]
page = sys.argv[1]
manifest = json.loads((root / 'work/manifest.json').read_text())
assert all((root / 'work' / (m['page'] + '_final.json')).exists() for m in manifest), 'All first readings must precede audits.'
comparison = json.loads((root / 'second' / (page + '_comparison.json')).read_text())
review = json.loads((root / 'work' / (page + '_audit_decisions.json')).read_text())
report_path = root / 'work' / (page + '_final.json')
report = json.loads(report_path.read_text())
assert not report.get('audit'), 'Do not duplicate an audit event.'
assert review['reader'] != report['reader'], 'Second reader must be independent.'
diffs = {d['box']: d for d in comparison['differences']}
decisions = {d['box']: d for d in review['adjudications']}
assert len(decisions) == len(review['adjudications'])
assert set(decisions) == set(diffs), 'Every token-different box needs a decision.'
views = (root / 'work/root_views.tsv').read_text()
for box, d in decisions.items():
    assert d['first'] == diffs[box]['first'] and d['second'] == diffs[box]['second']
    assert d['confidence'] in ('high', 'medium', 'low')
    assert isinstance(d['changed'], bool)
    assert (root / 'crops' / d['crop']).is_file()
    assert d['crop'] in views, 'Root must view each disagreement crop.'
    assert d['evidence'].strip() and d['final'].strip()
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report['audit_changes'] = review['adjudications']
report['audit'] = dict(reader=review['reader'], audited_at=stamp, boxes=comparison['boxes'],
                       different_boxes=len(diffs), changed_boxes=sum(d['changed'] for d in decisions.values()))
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
fields = ['box', 'first', 'second', 'final', 'changed', 'evidence', 'crop', 'confidence']
with (root / 'second' / (page + '_adjudications.tsv')).open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', extrasaction='ignore')
    w.writeheader(); w.writerows(review['adjudications'])
subprocess.run([sys.executable, str(root / 'scripts/build_deliverables.py')], check=True)
scan = page.split('_scan')[1]
with (root / 'progress.log').open('a') as f:
    f.write(f'scan {scan} audited {stamp}: {comparison["boxes"]} boxes read, {len(diffs)} differences, {report["audit"]["changed_boxes"]} changed\n')
print(json.dumps({'page': page, **report['audit']}))
