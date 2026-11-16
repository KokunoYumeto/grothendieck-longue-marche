"""Exact finite verification of the geometric group in LM8_PUSH D.8.
No arithmetic Galois-cohomology assertion is inferred from enumeration.
"""
from itertools import product
import json
from pathlib import Path
A=((0,4),(1,4))
def add(x,y):return tuple((a+b)%5 for a,b in zip(x,y))
def neg(x):return tuple(-a%5 for a in x)
def mv(x):return ((4*x[1])%5,(x[0]+4*x[1])%5)
def act(k,x):
 for _ in range(k%3):x=mv(x)
 return x
def mul(x,y):return (add(x[0],act(x[1],y[0])),(x[1]+y[1])%3)
def inv(x):return (neg(act(-x[1],x[0])),-x[1]%3)
def power(x,n):
 out=((0,0),0)
 for _ in range(n):out=mul(out,x)
 return out
def comm(x,y):return mul(mul(mul(x,y),inv(x)),inv(y))
def generated(xs):
 ret={((0,0),0)};todo=list(ret)
 while todo:
  x=todo.pop()
  for y in xs:
   z=mul(x,y)
   if z not in ret:ret.add(z);todo.append(z)
 return ret
G=list(product(list(product(range(5),repeat=2)),range(3)))
x=((0,0),1);y=((1,0),1);z=inv(mul(x,y))
assert len(generated([x,y]))==75
assert all(power(t,3)==((0,0),0) for t in (x,y,z))
assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a in G for b in G for c in G)
R=set(G);sizes=[len(R)]
while True:
 R1=generated([comm(a,b) for a in G for b in R]);sizes.append(len(R1))
 if R1==R:break
 R=R1
assert R=={(v,0) for v in product(range(5),repeat=2)}
phi=lambda t:(neg(t[0]),t[1])
assert all(phi(mul(a,b))==mul(phi(a),phi(b)) for a in G for b in G)
assert all(phi(phi(a))==a for a in G)
assert not any(all(mul(mul(inv(w),a),w)==phi(a) for a in G) for w in G)
conjs={}
for name,t in [('x',x),('y',y),('xy',mul(x,y))]:
 ws=[w for w in R if mul(mul(inv(w),t),w)==phi(t)]
 assert len(ws)==1
 conjs[name]=ws[0]
 assert mul(ws[0],phi(ws[0]))==((0,0),0)
# The norm operator is zero and tau-1 is bijective on the kernel.
assert all(add(add(v,mv(v)),mv(mv(v)))==(0,0) for v in product(range(5),repeat=2))
assert len({add(mv(v),neg(v)) for v in product(range(5),repeat=2)})==25
out={'group_order':75,'generators':{'x':x,'y':y,'z':z},
 'peripheral_orders':[3,3,3],'lower_central_orders':sizes,
 'nilpotent_residual_order':len(R),'matrix_of_deck_action':A,
 'deck_norm_zero':True,'deck_minus_one_bijective':True,
 'beta_minus_one_outer_involution':True,'unique_translation_conjugators':conjs,
 'scope':'finite geometric group only; arithmetic fibre proof is D.8'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
