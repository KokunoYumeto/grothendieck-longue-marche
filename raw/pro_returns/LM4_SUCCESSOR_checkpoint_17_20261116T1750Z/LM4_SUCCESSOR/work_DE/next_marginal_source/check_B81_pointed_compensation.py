#!/usr/bin/env python3
"""Bounded actual pointed-action convention check for B81's original8-strand paths."""
from pathlib import Path
import json
from weighted_stallings import WeightedFold
H=Path(__file__).resolve().parent
D=json.loads((H/'tangent_bundle_fiber_data.json').read_text())

def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(int(x))
 return tuple(a)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[x] if x>0 else inv(A[-x])))
def art(w):
 A={i:(i,) for i in range(1,9)}
 for g in w:
  i=abs(g);a,b=A[i],A[i+1]
  A[i],A[i+1]=(red(a+b+inv(a)),a) if g>0 else (b,red(inv(b)+a+b))
 return A

def conjugator(A):
 w=list(A[8]);q=[]
 while len(w)>1 and w[0]==-w[-1]:q.append(w.pop(0));w.pop()
 assert w==[8]
 return red(x for x in q if abs(x)!=8)
def pointed(A):
 q=conjugator(A)
 return {i:red(inv(q)+tuple(x for x in A[i] if abs(x)!=8)+q) for i in range(1,8)}
C={i+1:inv(conjugator(art(w))) for i,w in enumerate(D['standard_pure_generators'])}
for i,w in enumerate(D['standard_pure_generators'],1):
 assert conjugator(art(tuple(reversed(w))))==(i,)
fold=WeightedFold([C[i] for i in range(1,8)]);Ci={i:fold.rewrite((i,)) for i in range(1,8)}
assert all(w is not None for w in Ci.values())
for i in range(1,8):assert sub(C[i],Ci)==(i,) and sub(Ci[i],C)==(i,)
oldinv={int(k):{int(j):tuple(v) for j,v in a.items()} for k,a in D['old_inverse_actions'].items()}
old={int(k):{int(j):tuple(v) for j,v in a.items()} for k,a in D['old_actions'].items()}
results=[]
for k,w in enumerate(D['source_braids'][:6]):
 P=pointed(art(tuple(reversed(w))));Pb=pointed(art(tuple(-x for x in w)))
 row={'index':k,'pull_equalities':[sub(Pb[j],C)==sub(C[j],old[k]) for j in range(1,8)],'push_equalities':[sub(P[j],C)==sub(C[j],old[k]) for j in range(1,8)]}
 assert all(row['pull_equalities'])
 inverse_equalities=[sub(P[j],C)==sub(C[j],oldinv[k]) for j in range(1,8)]
 assert all(inverse_equalities);row['inverse_equalities']=inverse_equalities
 results.append(row)
 print(k,'pull',row['pull_equalities'],'push',row['push_equalities'],flush=True)
fiber_checks=[]
for k,w in enumerate(D['source_braids'][6:],6):
 geometric=conjugator(art(tuple(reversed(w))))
 stored=tuple(D['new_fiber_words'][str(k)])
 assert sub(geometric,C)==stored
 fiber_checks.append({'index':k,'actual_positive_cut_word':list(geometric),'stored_word':list(stored)})
print('PASS: all84 old/inverse action comparisons, four source meridians and14 Nielsen inverse compositions.')
(H/'B81_pointed_compensation.json').write_text(json.dumps({'basis_C_actual_cut_to_old_inverse_push':{str(k):list(v) for k,v in C.items()},'inverse_basis_C':{str(k):list(v) for k,v in Ci.items()},'source_meridian_checks':fiber_checks,'results':results,'scope':'bounded calibration; requires the standard source loops to be the actual positive top-cut meridians'},indent=2)+'\n')
