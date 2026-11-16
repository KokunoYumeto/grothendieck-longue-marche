"""Exact class-four free-Lie calculation of B.55 over F7."""
import json
from pathlib import Path
from collections import defaultdict
P=Path(__file__).resolve().parents[1]
def add(*terms):
 d=defaultdict(int)
 for a in terms:
  for w,c in a.items():d[w]+=c
 return {w:c%7 for w,c in d.items() if c%7}
def scale(a,n):return {w:c*n%7 for w,c in a.items() if c*n%7}
def prod(a,b):
 d=defaultdict(int)
 for u,c in a.items():
  for v,e in b.items():d[u+v]+=c*e
 return {w:c%7 for w,c in d.items() if c%7}
def br(a,b):return add(prod(a,b),scale(prod(b,a),-1))
X={(0,):1};Y={(1,):1};Z=scale(add(X,Y),-1);C=br(X,Y);A=br(X,C);B=br(Y,C)
U=br(X,A);V=br(Y,A);W=br(Y,B);assert V==br(X,B)
seed=(scale(V,-1),V)
for a in range(7):
 for b in range(7):
  q=add(scale(A,a),scale(B,b))
  assert (br(q,X),br(q,Y))!=seed
print('PASS: the pants degree-three class is non-inner in the actual class-four exponent-seven target.')
data=json.loads((P/'data/resolvent_color_certificate.json').read_text())
for name in ['plus','minus']:
 weights=data['counts'][name]['incidence_weights'];n01=weights['01'];n02=weights['02'];n12=weights['12']
 dx=add(scale(U,-n02),scale(V,-n01-n02));dy=add(scale(V,n01+n12),scale(W,n12))
 innerx=add(scale(U,-n02),scale(V,n12));innery=add(scale(V,-n02),scale(W,n12))
 remainder=(add(dx,scale(innerx,-1)),add(dy,scale(innery,-1)))
 coeff=n01+n02+n12
 assert remainder==(scale(seed[0],coeff),scale(seed[1],coeff))
 assert coeff%7!=0
 print(name,'incidence',n01,n02,n12,'outer coefficient',coeff,'mod7',coeff%7,'PASS')
assert data['counts']['original']['coefficient']==0
for color in [X,Y,Z]:
 c=scale(color,5);assert not br(c,c)
print('PASS: original equal-color trace is zero, including the original cusp power5.')
