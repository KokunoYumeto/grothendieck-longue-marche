"""Record a completed, image-adjudicated blind audit. Never edits transcription."""
from pathlib import Path
import csv, datetime, hashlib, json, sys

ROOT = Path(__file__).resolve().parents[1]
page = sys.argv[1]
record_path = ROOT/'records'/f'{page}.json'
d = json.loads(record_path.read_text())
assert d.get('root_reviewed') and not d.get('audited'), 'First review required; audit must not be logged twice.'
c = json.loads((ROOT/'second'/f'{page}_comparison.json').read_text())
a = json.loads((ROOT/'second'/f'{page}_adjudications.json').read_text())
assert a['page'] == page
assert a['reader'] != d['reader'], 'Blind reader must differ from first reader.'
assignments = {x['page']: x for x in csv.DictReader((ROOT/'reader_assignments.tsv').open(), delimiter='\t')}
assignment = assignments[page]
assert a['reader'].removeprefix('/root/') == assignment['second_reader'], 'Audit reader must match the recorded canonical assignment.'
assert assignment['second_reader'] != assignment['first_reader'], 'The two readers must be different people, not merely different display strings.'
assert a['root_reviewed'], 'Root crop adjudication required.'
by_box = {x['box']: x for x in a['adjudications']}
assert len(by_box) == len(a['adjudications'])
differing = {x['box']: x for x in c['results'] if not x['identical_tokens']}
assert set(by_box) == set(differing), 'Every differing box, including macro differences, requires adjudication.'
for box, r in differing.items():
    x = by_box[box]
    assert x['first'] == r['first'] and x['second'] == r['second'], f'Readings must be preserved: {box}'
    assert x['root_viewed'] and x['evidence'] and x['final'], f'Incomplete crop decision: {box}'
    assert (ROOT/x['crop']).exists(), f'Missing audit crop: {box}'
    assert x['token_difference_count'] == len(r['token_differences']), f'Unaccounted token differences: {box}'
    assert isinstance(x['changed'], bool)
manifest = ROOT/'second'/'first_reading_hashes.tsv'
assert manifest.exists(), 'Seal first readings before giving any page to blind readers.'
for row in csv.DictReader(manifest.open(), delimiter='\t'):
    if row['page'] == page:
        assert hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest() == row['sha256'], 'First readings/boxes changed after audit began.'
d['audited'] = True
d['audit_reader'] = a['reader']
d['audit_boxes'] = c['boxes']
d['audit_differing_boxes'] = c['differing_boxes']
d['audit_token_difference_runs'] = sum(len(x['token_differences']) for x in c['results'])
d['audit_changed_boxes'] = sum(x['changed'] for x in by_box.values())
d['audit_changes'] = [x for x in by_box.values() if x['changed']]
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['audit_utc'] = now
record_path.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')
with (ROOT/'progress.log').open('a') as f:
    f.write(f"scan {int(d['scan']):03} audited {now}: {c['boxes']} boxes read, {d['audit_token_difference_runs']} differences, {d['audit_changed_boxes']} changed; cote {d['cote']}; {c['differing_boxes']} differing boxes; differences count token runs; changed count adjudicated boxes\n")
print(page, 'audit finalized')
