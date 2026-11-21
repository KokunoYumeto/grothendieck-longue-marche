#!/usr/bin/env python3
"""Record a completed visual adjudication; never infer or change a reading."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, subprocess, sys

root = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
page = f'147_scan{scan:03}'
record_path = root/'reviewed'/f'{page}.json'
record = json.loads(record_path.read_text())
assert not record.get('audit_complete'), 'Audit already recorded'
comparison = json.loads((root/'second'/f'{page}_comparison.json').read_text())
metadata = json.loads((root/'second'/f'{page}_comparison_metadata.json').read_text())
for which in ('first', 'second'):
    reading_path = root/'second'/f'{page}_{which}.tsv'
    assert hashlib.sha256(reading_path.read_bytes()).hexdigest() == metadata['files'][which]['sha256'], 'A written reading changed after comparison'
start = json.loads((root/'workflow'/'blind_audit_start.json').read_text())
frozen = next(r for r in start['pages'] if r['scan'] == scan)
assert hashlib.sha256((root/'second'/f'{page}_boxes.tsv').read_bytes()).hexdigest() == frozen['boxes_sha256'], 'The blind box list changed'
adjudications = json.loads((root/'second'/f'{page}_adjudications.json').read_text())
assert {r['box'] for r in comparison} == {r['box'] for r in adjudications}, 'Every differing box needs exactly one adjudication'
assert len(adjudications) == len({r['box'] for r in adjudications}), 'Duplicate box'
comp = {r['box']: r for r in comparison}
for row in adjudications:
    assert row.get('root_viewed') is True, row['box']
    assert row.get('evidence') and row.get('final'), row['box']
    assert isinstance(row.get('changed'), bool), row['box']
    assert (root/'crops'/row['crop']).is_file(), row['box']
    assert row['first'] == comp[row['box']]['first'], row['box']
    assert row['second'] == comp[row['box']]['second'], row['box']
first = list(csv.DictReader((root/'second'/f'{page}_first.tsv').open(), delimiter='\t'))
second = list(csv.DictReader((root/'second'/f'{page}_second.tsv').open(), delimiter='\t'))
assert [r['box'] for r in first] == [r['box'] for r in second]
auditor = json.loads((root/'audit_returns'/f'{page}.json').read_text())
assert set(auditor['boxes_read']) == {r['box'] for r in first}
for crop in auditor['crops']:
    assert (root/'crops'/Path(crop).name).is_file(), crop
changed = [r for r in adjudications if r['changed']]
record['audit_complete'] = True
record['audit_summary'] = (f"Independent reader {auditor['reader']} wrote {len(first)} box readings before comparison. "
    f"The token comparison found {len(comparison)} differing boxes. The main reader examined each on its crop; "
    f"{len(changed)} boxes required a transcription change. Equivalent TeX encodings and retained uncertainties "
    "are explained in the box-level adjudications.")
record['audit_changes'] = changed
record['auditor'] = auditor['reader']
record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'scan {scan:03} audited {now}: {len(first)} boxes read, {len(comparison)} differences, {len(changed)} changed\n')
state_path = root/'run_state.json'
state = json.loads(state_path.read_text())
state['audited_scans'] = sorted(json.loads(p.read_text())['scan'] for p in (root/'reviewed').glob('*.json') if json.loads(p.read_text()).get('audit_complete'))
state['audit_approved_count'] = len(state['audited_scans'])
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2)+'\n')
subprocess.run([sys.executable, str(root/'scripts/build_deliverables.py')], check=True)
print(json.dumps({'scan':scan,'boxes':len(first),'different_boxes':len(comparison),'changed_boxes':len(changed)}))
