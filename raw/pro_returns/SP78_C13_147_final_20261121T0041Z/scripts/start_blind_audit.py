#!/usr/bin/env python3
"""Record the finished first-pass inputs before any independent second reading."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

root = Path(__file__).resolve().parents[1]
state = json.loads((root/'run_state.json').read_text())
manifest = root/'workflow'/'blind_audit_start.json'
assert not manifest.exists(), 'The start of the blind audit has already been recorded'
records = []
for scan in state['scope']:
    page = f'147_scan{scan:03}'
    report = json.loads((root/'reviewed'/f'{page}.json').read_text())
    assert report.get('root_review_complete'), page
    assert (root/'pages'/f'{page}.tex').is_file(), page
    assert not (root/'second'/f'{page}_second.tsv').exists(), 'A second reading preceded the complete first pass'
    first = root/'second'/f'{page}_first.tsv'
    boxes = root/'second'/f'{page}_boxes.tsv'
    first_rows = list(csv.DictReader(first.open(), delimiter='\t'))
    box_rows = list(csv.DictReader(boxes.open(), delimiter='\t'))
    assert [r['box'] for r in first_rows] == [r['box'] for r in box_rows], page
    records.append({'scan':scan,'first_reader':state['first_assignments'][str(scan)],
        'boxes':len(box_rows),'first_sha256':hashlib.sha256(first.read_bytes()).hexdigest(),
        'boxes_sha256':hashlib.sha256(boxes.read_bytes()).hexdigest(),
        'page_sha256':hashlib.sha256((root/'pages'/f'{page}.tex').read_bytes()).hexdigest()})
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest.write_text(json.dumps({'all_first_readings_completed_utc':now,'pages':records},indent=2)+'\n')
with (root/'progress.log').open('a') as f:
    f.write(f'all {len(records)} first readings complete {now}; independent blind reading may now begin\n')
print(json.dumps({'pages':len(records),'boxes':sum(r['boxes'] for r in records),'recorded_utc':now}))
