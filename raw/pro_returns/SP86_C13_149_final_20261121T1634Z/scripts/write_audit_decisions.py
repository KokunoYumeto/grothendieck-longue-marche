"""Store explicit root crop decisions supplied on stdin; never infer a reading.

The root supplies one decision for every differing box after viewing its crop.
An entry with keep_first=true explicitly retains the written first reading.
Transcription/review corrections must already have been made separately.
"""
from pathlib import Path
import csv
import json
import sys

BASE = Path(__file__).resolve().parents[1]


def main(payload):
    page = payload['page']
    path = BASE / 'reviews' / f'{page}.json'
    report = json.loads(path.read_text())
    assert not report.get('audit', {}).get('completed_utc')
    with (BASE / 'second' / f'{page}_comparison.tsv').open() as f:
        comparisons = {r['box']: r for r in csv.DictReader(f, delimiter='\t')
                       if r['different'] == 'yes'}
    with (BASE / 'second' / f'{page}_boxes.tsv').open() as f:
        boxes = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
    choices = payload['decisions']
    assert set(choices) == set(comparisons), 'Supply exactly every differing box'
    viewed = payload['root_viewed']
    records = []
    for box, entry in comparisons.items():
        choice = choices[box]
        assert choice['decision'] and choice['evidence']
        crop = f'crops/{page}_{box}_second.png'
        assert crop in viewed and (BASE / crop).is_file()
        final = entry['first'] if choice.get('keep_first') else choice['final']
        assert final and isinstance(choice['changed'], bool)
        if choice.get('keep_first'):
            assert not choice['changed']
        records.append({
            'box': box, 'first': entry['first'], 'second': entry['second'],
            'final': final, 'decision': choice['decision'],
            'evidence': choice['evidence'], 'crop': crop,
            'coords': [int(boxes[box][k]) for k in ['x0', 'y0', 'x1', 'y1']],
            'changed': choice['changed'], 'place': choice.get('place', box)
        })
    report['audit_adjudications'] = records
    report['audit_root_viewed'] = viewed
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'page': page, 'root_decisions_written': len(records)}))


if __name__ == '__main__':
    main(json.load(sys.stdin))
