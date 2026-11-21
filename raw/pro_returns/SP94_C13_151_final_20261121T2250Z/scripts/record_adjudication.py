"""Apply explicitly written main-reader decisions to a comparison table.

The decision JSON is a record of manual crop inspection, never an inferred
reading. This helper performs no recognition or textual adjudication.
"""
from pathlib import Path
import csv
import json
import sys

WORK = Path(__file__).resolve().parents[1]
page = sys.argv[1]
path = WORK / 'second' / (page + '_comparison.tsv')
decision_path = WORK / 'audit' / (page + '_adjudication.json')
decisions = json.loads(decision_path.read_text())
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
assert set(decisions).issubset({r['box'] for r in rows})
for row in rows:
    if row['same_tokens'] == 'yes':
        continue
    assert row['box'] in decisions, (page, row['box'], 'no manual decision')
    d = decisions[row['box']]
    assert d['decision'] and d['decision'] != 'PENDING'
    assert d['changed'] in ('yes', 'no')
    assert d['evidence'].strip()
    for key in ('decision', 'changed', 'evidence'):
        row[key] = d[key]
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)
print(page, sum(r['same_tokens'] == 'no' for r in rows), 'manual decisions recorded')
