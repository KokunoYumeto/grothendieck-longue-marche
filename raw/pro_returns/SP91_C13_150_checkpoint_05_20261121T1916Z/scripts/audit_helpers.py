"""Bookkeeping for explicit main-reader image adjudications.

The main reader supplies every decision and its observed image evidence. This
module never infers a reading, normalizes a string, or changes a page file.
Choosing 'first' or 'second' copies that complete recorded string verbatim.
Choosing 'explicit' requires a complete final box reading from the main reader.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
HEADERS = ['box', 'first', 'second', 'final', 'changed', 'evidence', 'crop',
           'box_pixels', 'confidence', 'change_ids']


def adjudicate(scan, decisions):
    scan = f'{int(scan):03}'
    stem = '150_scan' + scan
    comparison = json.loads((ROOT / 'second' / (stem + '_comparison.json')).read_text())
    differences = {r['box']: r for r in comparison if r['different']}
    with (ROOT / 'second' / (stem + '_boxes.tsv')).open() as f:
        boxes = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
    journal_path = ROOT / 'second' / (stem + '_root_decisions.json')
    journal = json.loads(journal_path.read_text()) if journal_path.exists() else {}
    for decision in decisions:
        box = decision['box']
        assert box in differences, ('Not a compared difference', scan, box)
        assert box not in journal, ('Already adjudicated; revise explicitly', scan, box)
        assert decision['evidence'].strip(), ('Missing observed evidence', scan, box)
        assert decision['confidence'] in ['high', 'medium', 'low']
        assert decision['changed'] in ['yes', 'no']
        choice = decision['choice']
        assert choice in ['first', 'second', 'explicit']
        final = differences[box][choice] if choice != 'explicit' else decision['final']
        assert final.strip(), ('Missing final box reading', scan, box)
        crop = f'crops/{stem}_second_{box}.png'
        assert (ROOT / crop).exists(), crop
        ids = decision.get('change_ids', '')
        assert decision['changed'] == 'no' or ids.strip(), ('Changed page place needs a change-record ID', scan, box)
        b = boxes[box]
        journal[box] = {
            'box': box,
            'first': differences[box]['first'],
            'second': differences[box]['second'],
            'final': final,
            'changed': decision['changed'],
            'evidence': decision['evidence'],
            'crop': crop,
            'box_pixels': str([int(b[k]) for k in ['x0', 'y0', 'x1', 'y1']]),
            'confidence': decision['confidence'],
            'change_ids': ids,
            'choice': choice,
            'observed_and_decided_at': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        }
    journal_path.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + '\n')
    with (ROOT / 'second' / (stem + '_adjudication.tsv')).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS, delimiter='\t', extrasaction='ignore')
        writer.writeheader()
        for row in comparison:
            if row['box'] in journal:
                writer.writerow(journal[row['box']])
    print(json.dumps({'scan': scan, 'adjudicated': len(journal),
                      'differences': len(differences),
                      'remaining': [box for box in differences if box not in journal]}))
