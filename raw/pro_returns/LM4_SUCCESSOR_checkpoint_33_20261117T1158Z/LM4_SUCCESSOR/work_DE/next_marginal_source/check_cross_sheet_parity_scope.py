#!/usr/bin/env python3
"""Test the specific pivot-relative parity grading on the128 full columns.

This is a check of one tempting extension of the bounded pivot argument,
not a search over gradings or a finite quotient census.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
p=Path(__file__).resolve().parent/'odd_G_overlap.json'
raw=p.read_bytes();D=json.loads(raw);cols=D['columns']
colors={(x['augmented_row'][0],x['augmented_row'][1]):
        sum(abs(j)==1 for j in x['augmented_row'][2])%2 for x in cols[:64]}
rows=[]
for layer in (0,1):
    counts=Counter();mixed=[]
    for c in cols[64*layer:64*(layer+1)]:
        support=set()
        for term in c['terms']:
            r=term['row']
            v=(sum(abs(j)==1 for j in r['relative_retained_word'])+
               colors[r['A_slot'],r['B_slot']])%2
            counts[v]+=1;support.add(v)
        if len(support)>1:mixed.append(c['node'])
    rows.append({'layer':layer,'full_cell_color_counts':dict(counts),'mixed_columns':mixed})
    print('Layer',layer,'full cell colors',dict(counts),'mixed columns',len(mixed))
assert [len(x['mixed_columns']) for x in rows]==[39,64]
out={'input_sha256':hashlib.sha256(raw).hexdigest(),'rows':rows,
     'conclusion':'The pivot-relative y1-parity is not a homogeneous grading of these full columns.',
     'scope':'Only this specified grading is checked;the bounded128-column unit-pivot proof remains valid.'}
(p.parent/'cross_sheet_parity_scope.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact proposed-grading failure retained; no automatic all-orbit separation follows.')
