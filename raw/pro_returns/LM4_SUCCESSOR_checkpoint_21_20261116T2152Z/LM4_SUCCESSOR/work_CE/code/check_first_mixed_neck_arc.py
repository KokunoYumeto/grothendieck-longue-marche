#!/usr/bin/env python3
"""Exact radical bounds for the actual first mixed-neck vanishing arcs.

No numerical braid approximation is used. The geometric ray and branch
exclusion arguments are given in first_mixed_neck_radial_arcs_21h.txt.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    p=[x*y for x in a for y in b];return min(p),max(p)
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def rat(x):return (F(x),F(x))
def root(a):
    assert a[0]>=0
    def bound(x,upper):
        lo=F(0);hi=max(F(1),x)
        for _ in range(80):
            mid=(lo+hi)/2
            if mid*mid<=x:lo=mid
            else:hi=mid
        assert lo*lo<=x<=hi*hi
        return hi if upper else lo
    return bound(a[0],False),bound(a[1],True)
r5=root(rat(5));ir5=div(rat(1),r5)
c1=root(add(rat(1),mul(rat(2),ir5)))
c2=root(sub(rat(1),mul(rat(2),ir5)))
y=div(add(c1,c2),rat(2));delta=div(sub(c1,c2),rat(2))
l1=div(sub(rat(5),r5),rat(4));l2=div(add(rat(5),r5),rat(4))
positions={
 'A2':mul(l2,delta),
 'A4':mul(l1,add(y,c1)),
 'A3':mul(l2,add(y,c2)),
 'branch_upper':add(y,root(add(rat(1),mul(y,y)))),
 'B1':div(rat(1),mul(l1,delta)),
}
targets={'A2':(95,96),'A4':(153,155),'A3':(212,214),
         'branch_upper':(216,217),'B1':(275,276)}
for name,b in positions.items():
    lo,hi=targets[name]
    assert F(lo,100)<b[0]<b[1]<F(hi,100),(name,b)
    print('PASS exact position interval',name,lo,hi,'/100')
assert y[0]>delta[1]>0
assert c2[1]<y[0]<y[1]<c1[0]
x2=div(add(rat(3),r5),rat(10))
assert x2[0]>0
critical_identity=sub(div(rat(1),mul(l1,l2)),mul(delta,delta))
assert max(x2[0],critical_identity[0])<=min(x2[1],critical_identity[1])
# The equality itself follows exactly from lambda1*lambda2=5/4 and
# delta^2=(1-1/sqrt(5))/2; record these symbolic expressions, not the
# mere interval overlap, as the proof of the identity.
out={'status':'PASS','producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'intervals':{k:[str(x) for x in v] for k,v in positions.items()},
 'rational_target_intervals':targets,
 'vertical_order':['A2','A4','A3','branch_upper','B1'],
 'critical_real_part_squared':'(3+sqrt(5))/10',
 'exact_identity_proof':['lambda1*lambda2=5/4','delta^2=(1-1/sqrt(5))/2',
  '1/(lambda1*lambda2)-delta^2=(3+sqrt(5))/10'],
 'geometric_scope':'One exact radial vanishing arc in each region; no simultaneous edge quotient or all-neck gluing.'}
(ROOT/'work_CE/next_symmetric_nodes/first_mixed_neck_arc.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS selected strip, branch-ray obstruction y0>delta, and positive critical real part')
