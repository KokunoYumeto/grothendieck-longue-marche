#!/usr/bin/env python3
"""Exact rational PL certificate for the four-point modular-topos comparison."""
from fractions import Fraction as F
from pathlib import Path
import json

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def matrix(u,v): return ((u[0],v[0]),(u[1],v[1]))
def inv(m):
    d=m[0][0]*m[1][1]-m[0][1]*m[1][0]
    return ((m[1][1]/d,-m[0][1]/d),(-m[1][0]/d,m[0][0]/d))
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                             for j in range(2)) for i in range(2))
def mv(m,v): return tuple(sum(m[i][j]*v[j] for j in range(2)) for i in range(2))
def affine(m,b,x): return tuple(y+z for y,z in zip(mv(m,x),b))

c=(F(2),F(2)); d=(F(5,2),F(2))
vs=[(F(3),F(2)),(F(2),F(3)),(F(1),F(2)),(F(2),F(1))]
cert=[]
for i in range(4):
    a,b=vs[i],vs[(i+1)%4]
    old=matrix(sub(a,c),sub(b,c));new=matrix(sub(a,d),sub(b,d))
    m=mm(new,inv(old));offset=sub(d,mv(m,c))
    jac=m[0][0]*m[1][1]-m[0][1]*m[1][0]
    assert jac>0
    for x,y in [(c,d),(a,a),(b,b)]:assert affine(m,offset,x)==y
    assert mm(inv(m),m)==((F(1),F(0)),(F(0),F(1)))
    cert.append({'triangle':[c,a,b],'matrix':m,'translation':offset,'Jacobian':jac})

orbit=[]
x=F(2)
for n in range(21):
    assert x==3-F(1,2)**n
    orbit.append((n,x))
    x=x/2+F(3,2)
assert len(set(x for _,x in orbit))==len(orbit)
# The support is |x-2|+|y-2| <= 1. The marked points 0,1 and i are outside it.
fixed=[(0,0),(1,0),(0,1)]
assert all(abs(x-2)+abs(y-2)>1 for x,y in fixed)

def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x
data=enc({'centre':c,'centre_image':d,'triangles':cert,
          'fixed_points':fixed,'centre_orbit':orbit,
          'assertions':'All four Jacobians positive; boundary identity; rational inverse; 21 exact distinct iterates.'})
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
