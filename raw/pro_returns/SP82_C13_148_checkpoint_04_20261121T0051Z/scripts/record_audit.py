"""Format explicitly entered main-reader adjudications of blind differences.

This script chooses no reading and edits no transcription. Before using it,
the main reader must view every differing box and enter an adjudication.
"""
from pathlib import Path
import csv
import json
import sys
import assemble

OUT = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
stem = OUT / 'second' / f'148_scan{n:03d}'

def read_tsv(suffix):
    with Path(str(stem)+suffix).open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

comparisons = read_tsv('_comparison.tsv')
boxes = {r['box']:r for r in read_tsv('_boxes.tsv')}
entered = json.loads(Path(str(stem)+'_adjudications.json').read_text())
assert len({r['box'] for r in entered}) == len(entered)
decisions = {r['box']:r for r in entered}
different = {r['box'] for r in comparisons if r['different']=='yes'}
assert set(decisions) == different, ('Every literal difference requires a decision',different-set(decisions),set(decisions)-different)
rows = []
changes = []
for c in comparisons:
    box = c['box']
    rect = [int(boxes[box][k]) for k in ('x0','y0','x1','y1')]
    if c['different']=='no':
        rows.append(dict(box=box,first=c['first'],second=c['second'],final=c['first'],changed='no',ink='Literal token match; no difference to adjudicate.',crop='',pixels=str(tuple(rect)),confidence=''))
        continue
    d = decisions[box]
    assert d.get('viewed_by_main') is True, ('Unviewed difference',box)
    assert d['choice'] in ('first','second','revised')
    final = c[d['choice']] if d['choice']!='revised' else d['final']
    assert d['confidence'] in ('high','medium','low') and d['ink'].strip()
    crop = d.get('crop',f'crops/second/148_scan{n:03d}/{box}.png')
    assert (OUT/crop).is_file(), ('Missing audit crop',crop)
    changed = assemble.tokenise(final)!=assemble.tokenise(c['first'])
    row = dict(box=box,first=c['first'],second=c['second'],final=final,changed='yes' if changed else 'no',ink=d['ink'],crop=crop,pixels=str(tuple(rect)),confidence=d['confidence'])
    rows.append(row)
    if changed:
        changes.append(dict(row,pixels=rect))
assemble.write_tsv(Path(str(stem)+'_adjudication.tsv'),['box','first','second','final','changed','ink','crop','pixels','confidence'],rows)
rp=OUT/'reviews'/f'148_scan{n:03d}.json'
p=json.loads(rp.read_text())
assert not p.get('second_audit'), 'An audit has already been recorded; do not silently replace it.'
p['second_audit']=dict(boxes=len(comparisons),differences=len(different),changed=len(changes),changes=changes,reader='GPT-6 Astra Pro; effort not exposed; run SP82_C13_148-20261120',adjudicated_utc=assemble.now())
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
assemble.rebuild()
with (OUT/'progress.log').open('a') as f:
    f.write(f'scan {n:03d} audited {assemble.now()}: {len(comparisons)} boxes read, {len(different)} differences, {len(changes)} changed\n')
print(json.dumps({'scan':n,'boxes':len(comparisons),'differences':len(different),'changed':len(changes)}))
