"""Write exact audit rows from the main reader's explicit visual decisions.

This helper makes no reading decisions and does not edit a transcription. Each
unequal box must have an explicit choice, visual evidence and reviewed flag in
the supplied JSON. The complete first and independent readings are preserved.
"""
from pathlib import Path
import csv
import json
import re
import sys

OUT = Path(__file__).resolve().parents[1]
page, decision_path = sys.argv[1:3]
comparisons = json.loads((OUT / 'second' / f'{page}_comparison.json').read_text())
differences = {r['box']: r for r in comparisons if not r['same_tokens']}
decisions = json.loads(Path(decision_path).read_text())
if set(decisions) != set(differences):
    raise ValueError('Explicit decisions must cover exactly every unequal box')

def tokens(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]', s)

rows = []
for box, comparison in differences.items():
    d = decisions[box]
    if d.get('viewed') is not True or not d.get('evidence', '').strip():
        raise ValueError('Missing actual main-reader crop review: ' + box)
    choice = d['choice']
    if choice == 'keep_first':
        final = comparison['first']
    elif choice == 'take_second':
        final = comparison['second']
    elif choice == 'reading':
        final = d['reading']
    else:
        raise ValueError('Unknown explicit choice: ' + choice)
    crop = d.get('crop', f'crops/{page}_second_{box}.png')
    if not (OUT / crop).is_file():
        raise ValueError('Missing crop: ' + crop)
    rows.append(dict(box=box, first=comparison['first'], second=comparison['second'],
                     final=final, changed='yes' if tokens(final) != tokens(comparison['first']) else 'no',
                     evidence=d['evidence'], crop=crop, main_reader_reviewed='yes'))
target = OUT / 'second' / f'{page}_adjudication.tsv'
with target.open('w', newline='') as f:
    fields = ['box', 'first', 'second', 'final', 'changed', 'evidence', 'crop', 'main_reader_reviewed']
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    w.writeheader()
    w.writerows(rows)
print(json.dumps({'page': page, 'adjudicated_boxes': len(rows),
                  'changed_boxes': sum(r['changed'] == 'yes' for r in rows)}))
