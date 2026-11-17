"""Exact checks on the explicitly listed icosahedral braid words.

No floating point arithmetic.  Artin's faithful action verifies the two
periodicity equations in B_12.  The action after the sphere relation verifies
the triangle relation in the outer automorphism group, and permutations
verify the full order of its image.  The central double cover then has 120
elements by the standard exact sphere-braid sequence cited in the paper.
"""
import json,itertools
from pathlib import Path

def reduce(w):
 out=[]
 for a in w:
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 return tuple(out)
def inv(w):return tuple(-a for a in reversed(w))
def mul(*ws):return reduce(itertools.chain.from_iterable(ws))
def substitute(w,images):return mul(*(images[a-1] if a>0 else inv(images[-a-1]) for a in w))
def action(w,n=12):
 images=[(i+1,) for i in range(n)]
 for a in w:
  i=abs(a)-1;u,v=images[i:i+2]
  if a>0:images[i:i+2]=[mul(u,v,inv(u)),u]
  else:images[i:i+2]=[v,mul(inv(v),u,v)]
 return images
def permutation(w,n=12):
 p=list(range(n))
 for a in w:i=abs(a)-1;p[i],p[i+1]=p[i+1],p[i]
 return tuple(p)
def compose(p,q):return tuple(p[i] for i in q)
def generated(perms):
 one=tuple(range(len(perms[0])));seen={one};todo=[one]
 for p in todo:
  for q in perms:
   r=compose(p,q)
   if r not in seen:seen.add(r);todo.append(r)
 return seen
def order(p):
 q=tuple(range(len(p)))
 for i in range(1,1000):
  q=compose(q,p)
  if q==tuple(range(len(p))):return i
 raise AssertionError('order bound')
def sphere_action(w):
 images=action(w);quotient=[(i,) for i in range(1,12)]+[tuple(range(-11,0))]
 return [substitute(a,quotient) for a in images[:11]]
def inner_witness(images):
 w=images[0];u=[]
 while len(w)>1 and w[0]==-w[-1]:u.append(w[0]);w=w[1:-1]
 assert w==(1,),('first generator is not conjugate to itself',w)
 for k in range(-max(map(len,images)),max(map(len,images))+1):
  v=mul(u,((1,)*k if k>=0 else (-1,)*(-k)))
  if all(mul(v,(i+1,),inv(v))==im for i,im in enumerate(images)):return v
 raise AssertionError('not inner')

p=Path(__file__).resolve().parents[1]
d=json.loads((p/'data'/'icosahedral_braids.json').read_text())
b2,b3=d['beta2'],d['beta3']
twist=list(range(1,12))*12
expected=action(twist)
garside=[i for k in range(11,0,-1) for i in range(1,k+1)]
assert action(b2)==action(garside)
assert action(b2*2)==expected
assert action(b3*3)==expected
print('PASS exact faithful Artin action: beta2^2 = beta3^3 = Delta_12^2')
p2,p3=permutation(b2),permutation(b3)
ps=generated([p2,p3]);assert len(ps)==60
assert order(p2)==2 and order(p3)==3
a=b2+list(inv(b3));pa=permutation(a);assert order(pa)==5
last_sphere_relator=list(range(11,1,-1))+[1,1]+list(range(2,12))
assert action(a*5)==action(twist+list(inv(last_sphere_relator)))
print('PASS exact B_12 identity: (beta2 beta3^-1)^5 = Delta_12^2 R_last^-1')
print('PASS exact permutation enumeration: generated group order 60; orders 2,3,5')
witness=inner_witness(sphere_action(a*5))
print('PASS sphere outer action: (beta2 beta3^-1)^5 = 1; inner witness:',list(witness))
# The triangle presentation has order 60, already checked independently by
# check_icosahedral_groups.py.  The order-60 permutation quotient proves
# equality, rather than only an upper bound, for the sphere mapping-class image.
print('PASS mapping-class image is A5; sphere-braid inverse image has order120')
print('beta2 =',' '.join(map(str,b2)))
print('beta3 =',' '.join(map(str,b3)))
