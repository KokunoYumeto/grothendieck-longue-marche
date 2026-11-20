"""Write root-authored crop decisions without altering either recorded reading.

The input JSON is a list of decisions, one per differing box (and optionally
equal boxes). Every decision must supply its own visual evidence and final
reading. This script supplies no palaeographic decisions or default outcomes.
"""
from pathlib import Path
import csv, hashlib, json, sys

ROOT = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
plan_path = Path(sys.argv[2])
stem = f'147_scan{scan}'
plan = json.loads(plan_path.read_text())
with (ROOT/'second'/f'{stem}_comparison.tsv').open() as f:
    comparisons = {r['box']:r for r in csv.DictReader(f, delimiter='\t')}
meta = json.loads((ROOT/'second'/f'{stem}_comparison_meta.json').read_text())
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in meta['sha256'].items())
ids = [r['box'] for r in plan]
assert len(ids)==len(set(ids)), 'Duplicate root decision.'
assert {k for k,v in comparisons.items() if v['equal']=='no'}<=set(ids)
assert set(ids)<=set(comparisons)
rows=[]
for decision in plan:
    original=comparisons[decision['box']]
    assert decision['final'].strip() and decision['evidence'].strip()
    assert decision['changed'] in ('yes','no')
    crop=decision.get('crop',f'crops/{stem}_second_{decision["box"]}.jpg')
    assert (ROOT/crop).is_file(), crop
    rows.append(dict(box=decision['box'],first=original['first'],second=original['second'],
                     final=decision['final'],evidence=decision['evidence'],
                     changed=decision['changed'],crop=crop))
destination=ROOT/'second'/f'{stem}_adjudications.tsv'
assert not destination.exists(), 'Adjudication output already exists.'
with destination.open('w') as f:
    writer=csv.DictWriter(f,fieldnames=['box','first','second','final','evidence','changed','crop'],delimiter='\t')
    writer.writeheader();writer.writerows(rows)
print(destination)
