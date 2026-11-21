"""Expand explicit main-reader choices into full literal adjudication records.

This does not choose a reading. The input must contain an individual selection,
visual evidence, and changed flag for every differing box after crop inspection.
"""
from pathlib import Path
import csv,json,sys
ROOT=Path(__file__).resolve().parents[1]
scan=int(sys.argv[1]); path=Path(sys.argv[2]); stem=f'147_scan{scan}'
choices=json.loads(path.read_text())
with (ROOT/'second'/f'{stem}_comparison.tsv').open() as f:
    comparisons={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
out=[]
assert len({c['box'] for c in choices})==len(choices)
assert {b for b,r in comparisons.items() if r['equal']=='no'}<={c['box'] for c in choices}
for c in choices:
    assert c['selection'] in ('first','second','literal')
    assert c['changed'] in ('yes','no') and c['evidence'].strip()
    final=c['final'] if c['selection']=='literal' else comparisons[c['box']][c['selection']]
    item={'box':c['box'],'final':final,'evidence':c['evidence'],'changed':c['changed']}
    if c.get('crop'): item['crop']=c['crop']
    out.append(item)
destination=ROOT/'review'/f'{stem}_root_plan.json'
assert not destination.exists()
destination.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(destination)
