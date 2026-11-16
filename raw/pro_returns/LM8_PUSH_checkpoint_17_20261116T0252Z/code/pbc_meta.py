"""Independent metabelian character and weight-five certificates."""
import json,itertools
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import sympy as S

def add(*ps):
 d=defaultdict(int)
 for p in ps:
  for w,c in p.items():d[w]+=c
 return {w:c for w,c in d.items() if c}
def scale(p,n):return {w:n*c for w,c in p.items() if n*c}
def mul(p,q):
 d=defaultdict(int)
 for w,c in p.items():
  for v,e in q.items():d[w+v]+=c*e
 return {w:c for w,c in d.items() if c}
def br(p,q):return add(mul(p,q),scale(mul(q,p),-1))
def ly(w):return all(w<w[i:] for i in range(1,len(w)))
@lru_cache(None)
def lb(w):
 if len(w)==1:return {w:1}
 for i in range(1,len(w)):
  if ly(w[i:]):return br(lb(w[:i]),lb(w[i:]))
L5=[''.join(w) for w in itertools.product('xy',repeat=5) if ly(''.join(w))]
cols=[br({'x':1},lb(w)) for w in L5]+[br({'y':1},lb(w)) for w in L5]
rows=[''.join(w) for w in itertools.product('xy',repeat=6)]
mat=S.Matrix([[c.get(w,0) for c in cols] for w in rows])
ker=mat.nullspace()
x,y=S.symbols('x y')
def mbbr(v,w):
 a,b,r=v;c,d,t=w
 return (0,0,S.expand(a*d-b*c+(a*x+b*y)*t-(c*x+d*y)*r))
@lru_cache(None)
def mb(w):
 if w=='x':return (1,0,S.Integer(0))
 if w=='y':return (0,1,S.Integer(0))
 for i in range(1,len(w)):
  if ly(w[i:]):return mbbr(mb(w[:i]),mb(w[i:]))
qmeta=[]
for v in ker:
 qmeta.append(S.expand(sum((v[i+6]-v[i])*mb(w)[2] for i,w in enumerate(L5))))
qmatrix=S.Matrix([[q.coeff(x,i).coeff(y,3-i) for q in qmeta] for i in range(4)])
print('weight5 kernel dimension',len(ker),'metabelian image rank',qmatrix.rank(),flush=True)
print('weight5 normalized metabelian q',list(map(str,qmeta)),flush=True)
# Character group C6; primitive cubic roots have exponents 2,4, and -1 has exponent 3.
def b0(a,b):return -1 if a==b and a in (2,4) else 1
def g(a):return -1 if a in (2,4) else 1
def bg(a,b):return g(a)*g(b)*g((a+b)%6)
checks={}
for name,beta in [('beta0',b0),('beta_g',bg)]:
 sy=all(beta(a,b)==beta(b,a)==beta(b,(-a-b)%6) for a,b in itertools.product(range(6),repeat=2))
 boundary=all(beta(a,0)==beta(0,a)==beta(a,(-a)%6)==1 for a in range(6))
 failures=[(a,b,c) for a,b,c in itertools.product(range(6),repeat=3) if beta(a,b)*beta((a+b)%6,c)!=beta(b,c)*beta(a,(b+c)%6)]
 checks[name]={'S3':sy,'boundary':boundary,'cocycle_checks':216,'cocycle_failure_count':len(failures),'first_failure':failures[0] if failures else None}
assert checks['beta0']['S3'] and checks['beta_g']['S3']
assert b0(2,2)*b0(4,3)==-1 and b0(2,3)*b0(2,5)==1
assert not checks['beta_g']['cocycle_failure_count']
out={'lyndon_degree5':L5,'special_kernel_dimension':len(ker),'metabelian_image_rank':qmatrix.rank(),'kernel_basis':[[str(t) for t in v] for v in ker],'q_metabelian':list(map(str,qmeta)),'character_checks':checks,'lead6_witness':{'exponents':[2,2,3],'left':-1,'right':1}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
