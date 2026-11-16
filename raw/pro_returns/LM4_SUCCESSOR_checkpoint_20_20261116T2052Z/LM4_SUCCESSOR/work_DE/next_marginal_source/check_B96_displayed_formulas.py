#!/usr/bin/env python3
"""Check B96's four displayed source words and exact diagonal signs."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
S=json.loads((P/'symmetric_full_source_data.json').read_text())
O=json.loads((P/'symmetric_odd_old_translate.json').read_text())
D=json.loads((P/'symmetric_paired_fox_data.json').read_text())
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
qs=[[-5],[-5,-2,5,2,5,-10],
    [-13,-12,-1,-5,-2,5,2,5,-10,-6,10,6,9,10,-11,-10,-9],
    [-1,2,4,5,6,-7,-6,-5,-4]]
for q,c,k in zip(qs,[2,6,8,3],[0,8,12,16]):
    rho=red(tuple(q)+(c,)+inv(q))
    actual=next(x for x in S['source_peripheral_generators'] if x['sheet']==1 and x['critical_index']==k)
    assert rho==tuple(actual['positive_source_word_F13'])
    print('PASS displayed second-sheet word',k)
for r in O['rows']:
    if not r['neutral']:continue
    witness=[w for w in r['actual_source_zero_witnesses'] if not w['left_coefficient_R']]
    assert len(witness)==1
    expected=-1 if r['node_index'][0] in [0,12] else 1
    assert witness[0]['power']==expected
    print('PASS literal diagonal sign',r['direction'],r['node_index'],expected)
branch=next(x for x in S['old_source_generators'] if x['name']=='branch_square')
A={int(k):tuple(v) for k,v in D['old_actions'][1]['geometric_push_paired'].items()}
B={int(k):tuple(v) for k,v in branch['source_push_F21'].items()}
assert branch['h_paired']==[-1]
for j in range(1,22):assert B[j]==red((1,)+sub(A[j],A)+(-1,))
print('PASS displayed branch-square formula Inn(p1)*alpha_b^2 on all21 generators.')
