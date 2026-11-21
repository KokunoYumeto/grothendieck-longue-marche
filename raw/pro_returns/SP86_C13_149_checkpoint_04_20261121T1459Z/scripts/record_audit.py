"""Record root's completed crop adjudications; never decide readings by script."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import sys
import assemble
from audit_compare import read_tsv, reader_name, utc_datetime

BASE = Path(__file__).resolve().parents[1]

def record(page):
    report_path = BASE / 'reviews' / f'{page}.json'
    report = json.loads(report_path.read_text())
    assert not report.get('audit', {}).get('completed_utc'), 'Already audited'
    reader = json.loads((BASE / 'second' / f'{page}_reader.json').read_text())
    assert reader_name(reader['reader']) != reader_name(report['reader'])
    manifest = json.loads((BASE / 'second' / 'input_manifest.json').read_text())['pages'][page]
    comparison_meta = json.loads((BASE / 'second' / f'{page}_comparison.json').read_text())
    for suffix in ['boxes', 'first', 'second']:
        actual = hashlib.sha256((BASE / 'second' / f'{page}_{suffix}.tsv').read_bytes()).hexdigest()
        expected = comparison_meta['second_sha256'] if suffix == 'second' else manifest[suffix + '_sha256']
        assert actual == expected, f'{page}: immutable {suffix} changed after reading/comparison'
    assert reader['completed_utc'] == comparison_meta['reader_completed_utc']
    assert utc_datetime(reader['completed_utc']) <= utc_datetime(comparison_meta['compared_utc'])
    comparison = read_tsv(BASE / 'second' / f'{page}_comparison.tsv')
    boxes = {x['box']: x for x in read_tsv(BASE / 'second' / f'{page}_boxes.tsv')}
    decisions = {x['box']: x for x in report['audit_adjudications']}
    different = {x['box'] for x in comparison if x['different'] == 'yes'}
    assert set(decisions) == different, 'Every and only differing box must have a root decision'
    viewed = set(report['audit_root_viewed'])
    rows = []
    for entry in comparison:
        box = entry['box']
        if box in different:
            decision = decisions[box]
            assert decision['crop'] in viewed
            assert (BASE / decision['crop']).exists()
            assert decision['evidence'] and decision['final'] and decision['decision']
            assert isinstance(decision['changed'], bool)
            row = {**entry, **decision}
        else:
            row = {**entry, 'final': entry['first'], 'decision': 'same token reading',
                   'evidence': 'The written first and second readings have identical token sequences.',
                   'crop': '', 'changed': False}
        row['coordinates'] = ','.join(boxes[box][key] for key in ['x0', 'y0', 'x1', 'y1'])
        rows.append(row)
    assemble.write_tsv(BASE / 'second' / f'{page}_adjudication.tsv',
                       ['box', 'first', 'second', 'final', 'decision', 'evidence', 'crop', 'coordinates', 'changed'], rows)
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    changed = sum(row['changed'] for row in rows)
    report['audit'] = {'reader': reader_name(reader['reader']), 'completed_utc': stamp,
                       'reader_completed_utc': reader['completed_utc'], 'boxes': len(rows),
                       'differences': len(different), 'changed_boxes': changed}
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    with (BASE / 'progress.log').open('a') as log:
        log.write(f"scan {report['scan']:03d} audited {stamp}: {len(rows)} boxes read, {len(different)} differences, {changed} changed\n")
    assemble.build()
    print(json.dumps({'page': page, **report['audit']}))

if __name__ == '__main__':
    record(sys.argv[1])
