#!/usr/bin/env python3
"""Exact64 diagonal units after E-augmentation of the retained-deck matrix.

The output verifies the finite input to the separated-augmentation-filtration
proof.  It does not invert any augmentation-one nonunit candidate.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
path=P/'symmetric_retained_deck_module.json'
raw=path.read_bytes();data=json.loads(raw)

def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]

start=time.monotonic();rows=[]
for col in data['columns']:
    aug=defaultdict(int)
    for x in col['terms']:
        r=x['row'];a=x['G_coefficient']
        row=(r['A_slot'],r['B_slot'],tuple(r['relative_retained_word']))
        add(aug,(row,tuple(a['retained_word'])),x['coefficient'])
    assert len(aug)==1,('augmentation not a single monomial',col['node_index'],dict(aug))
    (row,t),sign=next(iter(aug.items()))
    assert sign in (-1,1)
    rows.append({'raw_seed_column':col['raw_seed_column'],'node_index':col['node_index'],
                 'pivot_row':{'A_slot':row[0],'B_slot':row[1],'relative_retained_word':row[2]},
                 'diagonal_unit_lift':{'coefficient':sign,'A_word':[],'B_word':[],'retained_word':t},
                 'augmented_column':{'row':row,'retained_word':t,'coefficient':sign}})
assert len(rows)==64
allrows=[tuple((r['pivot_row']['A_slot'],r['pivot_row']['B_slot'],tuple(r['pivot_row']['relative_retained_word']))) for r in rows]
slotpairs=[(r['pivot_row']['A_slot'],r['pivot_row']['B_slot']) for r in rows]
assert len(set(allrows))==64 and len(set(slotpairs))==64
As={a for a,b in slotpairs};Bs={b for a,b in slotpairs}
assert len(As)==len(Bs)==8 and set(slotpairs)=={(a,b) for a in As for b in Bs}

# Independently form the selected64x64 augmented matrix; it is diagonal
# in the column-labelled pivot-row order, with the recorded monomial units.
rowpos={row:i for i,row in enumerate(allrows)}
matrix={}
for j,col in enumerate(data['columns']):
    for x in col['terms']:
        r=x['row'];row=(r['A_slot'],r['B_slot'],tuple(r['relative_retained_word']))
        if row not in rowpos:continue
        i=rowpos[row];t=tuple(x['G_coefficient']['retained_word'])
        d=matrix.setdefault((i,j),defaultdict(int));add(d,t,x['coefficient'])
matrix={ij:dict(v) for ij,v in matrix.items() if v}
assert len(matrix)==64
for (i,j),v in matrix.items():
    assert i==j
    u=rows[i]['diagonal_unit_lift']
    assert v=={tuple(u['retained_word']):u['coefficient']}

out={'scope':__doc__,'input_sha256':{str(path.relative_to(ROOT)):hashlib.sha256(raw).hexdigest()},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'pivots':rows,'A_slots':sorted(As),'B_slots':sorted(Bs),
     'exact_matrix_statement':'The selected64x64 matrix equals D+M, D the recorded diagonal G-units, M in I_E Z[G].',
     'independence_proof_gate':'Separated powers of I_E Z[G]; supplied by residual finite p separation and nilpotence over Z/p^k.',
     'excluded_inference':'No coefficient with augmentation1 is asserted invertible.',
     'elapsed_seconds':time.monotonic()-start}
(P/'symmetric_G_augmentation_pivots.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:
    print('PASS G-augmentation unit',r['raw_seed_column'],r['node_index'],r['pivot_row'],r['diagonal_unit_lift'])
print('PASS all64 distinct pivot rows and every ordered8x8 physical slot pair exactly once; selected augmented matrix diagonal; elapsed',round(out['elapsed_seconds'],3))
