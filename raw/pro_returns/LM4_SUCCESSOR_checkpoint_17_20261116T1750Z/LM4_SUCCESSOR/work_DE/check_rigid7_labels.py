"""Exact permutation checks for the rigid seven-point family in B.56."""
from pathlib import Path
import importlib.util,itertools,json
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('cr',ROOT/'code'/'crossratio_495.py');cr=importlib.util.module_from_spec(spec);spec.loader.exec_module(cr)
group=cr.tetra_group();T=[tuple(group.index(cr.mm(a,b)) for b in group) for a in group]
assert len(set(T))==12
# Cyclic coordinate w->w^1 multiplies both pentagons by w.
d=list(range(12))
for cyc in [[1,5,11,8,3],[4,6,10,9,7]]:
 for i,j in zip(cyc,cyc[1:]+cyc[:1]):d[i]=j
d=tuple(d)
def comp(p,q):return tuple(p[q[i]] for i in range(12))
one=tuple(range(12));A={one};todo=[one]
for a in todo:
 for b in T+[d]:
  c=comp(a,b)
  if c not in A:A.add(c);todo.append(c)
assert len(A)==60
S=frozenset([0,1,2,3,5,8,11])
def image(g,S):return frozenset(g[i] for i in S)
TS={image(g,S) for g in T};AS={image(g,S) for g in A}
assert TS==AS and len(TS)==12
stab=[g for g in A if image(g,S)==S];assert len(stab)==5
pole=frozenset([0,2]);pent=S-pole
pents={image(g,pent) for g in A}
sixes={image(g,pent|{p}) for g in A for p in pole}
assert len(pents)==12 and len(sixes)==24
assert all(any(X<=Y for Y in TS) for X in pents|sixes)
print('Exact tetrahedral permutation group order:',len(T))
print('Exact generated icosahedral permutation group order:',len(A))
print('Rigid seven-point subsets:12; one regular T orbit; A5 stabilizer order5')
print('Rigid five-point subsets:12; rigid six-point subsets:24; each contained in a rigid seven-point subset')
print('ALL EXACT LABEL CHECKS PASS')
(Path(__file__).resolve().parent/'rigid7_subsets.json').write_text(json.dumps({'T_permutations':T,'D_permutation':d,'rigid7':sorted([sorted(i+1 for i in s) for s in TS]),'rigid5':sorted([sorted(i+1 for i in s) for s in pents]),'rigid6':sorted([sorted(i+1 for i in s) for s in sixes])},indent=2)+'\n')
