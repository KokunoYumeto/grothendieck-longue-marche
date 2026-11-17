#!/usr/bin/env python3
"""Literal zero-action pair and one bounded exact source-word membership gate."""
from pathlib import Path
import json
import sys
import time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
sys.path.insert(0,str(P))
from weighted_stallings import WeightedFold, substitute
A=json.loads((P/'w_source_adapted_basis.json').read_text())
D=json.loads((P/'w_fourth_strip_correction.json').read_text())
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return r
def inv(w):return[-x for x in w[::-1]]
def sub(w,a):return red(y for x in w for y in(a[str(abs(x))]if x>0 else inv(a[str(abs(x))])))
def cj(h,w):return red(h+w+inv(h))
Z=[-10,-12,1,12,10]
d=[11]
h=inv(Z)+d
for w in (d,Z):
    assert sub(w,A['actions_in_new']['0'])==cj(h,w)
    assert sub(w,A['inverse_actions_in_new']['0'])==cj(inv(h),w)
assert A['actions_in_new']['0']['10']==[10]
print('PASS actual zero action and inverse restrict on<d,Zprime> to Inn(Zprime^-1 d) and inverse.')
print('PASS zero action fixes a literally; Zprime=a^-1 b^-1 z b a.')
rows=D['source_generators']
started=time.monotonic()
fold=WeightedFold([tuple(r['word']) for r in rows],allow_relations=True)
answer=fold.rewrite(tuple(Z))
if answer is not None:
    assert substitute(answer,{i+1:tuple(r['word']) for i,r in enumerate(rows)})==tuple(Z)
elapsed=time.monotonic()-started
print('Specific target membership in the169 certified source words:',answer is not None)
print('Elapsed seconds:',round(elapsed,6))
print('A negative result is only for this finitely generated subgroup; whole H membership remains open.')
out={'target':Z,'source_count':len(rows),'exact_expression':answer,
     'elapsed_seconds':elapsed,'pair_inner':h,'literal_pair_checks':'PASS',
     'scope':'One exact source-subgroup membership test. Failure is not nonmembership in whole H.'}
(ROOT/'work_CE/w_zero_pair_source_membership.json').write_text(json.dumps(out,indent=2)+'\n')
