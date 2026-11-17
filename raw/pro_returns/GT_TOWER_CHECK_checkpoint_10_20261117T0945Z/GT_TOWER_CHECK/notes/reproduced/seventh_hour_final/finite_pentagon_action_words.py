#!/usr/bin/env python3
"""Literal braid identities used by the finite PaB/sphere construction.
No GT or finite-shadow membership is inferred by this word certificate.
"""
import json
from pathlib import Path

def red(w):
 out=[]
 for a in w:
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 return tuple(out)
def inv(w):return tuple(-a for a in reversed(w))
def sub(w,g):return red(a for i in w for a in (g[i-1] if i>0 else inv(g[-i-1])))
def compose(g,h):return tuple(sub(w,g) for w in h)
def braid(w,n):
 g=tuple((i,) for i in range(1,n+1))
 for a in w:
  i=abs(a);h=[(j,) for j in range(1,n+1)]
  if a>0:h[i-1]=(i,i+1,-i);h[i]=(i,)
  else:h[i-1]=(i+1,);h[i]=(-i-1,i,i+1)
  g=compose(g,h)
 return g
def equal(a,b,n):assert braid(a,n)==braid(b,n),(n,a,b)
def A(i,j):return tuple(range(j-1,i,-1))+(i,i)+tuple(-k for k in range(i+1,j))
def block(r,s,shift=0):return tuple(k+shift for i in range(r,0,-1) for k in range(i,i+s))
def dbl(r,s,shift=0):return block(r,s,shift)+block(s,r,shift)
rows=[(A(1,2),A(2,3)+A(2,4)),(A(1,3)+A(2,3),A(3,4)),(A(2,3),A(3,4)),(A(1,2)+A(1,3),A(2,4)+A(3,4)),(A(1,2),A(2,3))]
for r,(a,b,c) in [(0,(1,1,2)),(1,(2,1,1)),(3,(1,2,1))]:
 equal(rows[r][0],dbl(a,b),4);equal(rows[r][1],dbl(b,c,a),4)
print('PASS all three actual strand doublings give exactly the five-point pairs in FPA.10')
records=[]
for n in range(2,11):
 z=tuple(range(1,n))*n;prefix=tuple(range(1,n-1))*(n-1)
 y=tuple(range(n-1,1,-1))+(1,1)+tuple(range(2,n))
 delta=tuple(k for j in range(n-1,0,-1) for k in range(1,j+1))
 sphere=tuple(range(1,n-1))+(n-1,n-1)+tuple(range(n-2,0,-1))
 equal(z,prefix+y,n);equal(delta+y+inv(delta),sphere,n)
 # Every binary block decomposition gives the stated commuting product.
 for a in range(1,n):
  b=n-a;za=tuple(range(1,a))*a;zb=tuple(k+a for k in tuple(range(1,b))*b);t=dbl(a,b)
  equal(z,za+zb+t,n);equal(za+t,t+za,n);equal(zb+t,t+zb,n)
 labels=list(range(n));cross={(i,j):0 for i in range(n) for j in range(i+1,n)}
 for i in z:
  a,b=sorted((labels[i-1],labels[i]));cross[a,b]+=1;labels[i-1],labels[i]=labels[i],labels[i-1]
 assert labels==list(range(n)) and set(cross.values())=={2}
 records.append({'n':n,'full_twist':z,'prefix_full_twist':prefix,'last_strand_sphere_word':y,'half_twist':delta,'sphere_relator':sphere,'binary_splits':n-1})
print('PASS every full-twist decomposition, commuting block factor and sphere-relator conjugacy for n=2..10')
print('PASS every central full twist has abelian coordinate1 on every pure pair generator')
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Faithful discrete Artin word checks for the finite PaB pentagon insertions and both sphere quotient relations; no shadow census',
 'pentagon_evaluation_pairs':rows,'sphere_and_twist_records':records},indent=2)+'\n')
