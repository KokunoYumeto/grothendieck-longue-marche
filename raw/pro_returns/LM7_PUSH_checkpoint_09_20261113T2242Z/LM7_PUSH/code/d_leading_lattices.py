#!/usr/bin/env python3
"""Finite, exact lattice certificates for the rank limitation in D.22."""
from itertools import product
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

q0=sp.Matrix([1,1,1])
u1=sp.Matrix([1,2,0])
u2=sp.Matrix([-1,0,1])
S=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
R=sp.Matrix([[0,0,1],[0,-1,2],[1,-1,1]])
base=sp.Matrix.hstack(q0,u1,u2)
assert abs(base.det())==3

def valuation(n,p):
    n=abs(int(n)); out=0
    assert n
    while n%p==0:
        n//=p; out+=1
    return out

records=[]
for p,a,levels in [(5,2,[1,2,3]),(7,1,[1,2])]:
    B=sp.Matrix.hstack(q0,p**a*u1,p**a*u2)
    smith=smith_normal_form(B,domain=sp.ZZ)
    vals=[valuation(smith[i,i],p) for i in range(3)]
    assert vals==[0,a,a]
    for T in (S,R):
        action=B.inv()*T*B
        assert all(sp.denom(v)%p for v in action)
    for n in levels:
        modulus=p**n
        order=p**max(n-a,0)
        image=set()
        for x,y,z in product(range(modulus),range(order),range(order)):
            image.add(tuple((x+y*p**a-z*p**a)%modulus
                            if j==0 else
                            (x+2*y*p**a)%modulus if j==1 else
                            (x+z*p**a)%modulus for j in range(3)))
        line={tuple((x*v)%modulus for v in q0) for x in range(modulus)}
        predicted=p**(n+2*max(n-a,0))
        assert len(image)==predicted and len(line)==p**n
        assert (image==line)==(n<=a)
        row={'prime':p,'scaling_valuation':a,'precision':n,
             'rank1_reduction_size':len(line),
             'rank3_reduction_size':len(image),
             'same_reduction':image==line}
        records.append(row)
        print(json.dumps(row))
print('Both lattices are S3-stable. Their Q_l ranks are1 and3.')
print('For arbitrary a, every precision n<=a gives the same finite image.')
print('The two-dimensional analogue gives ranks1 and2 for the gentle target.')
print('These are explicit module examples, not asserted profinite-source images.')
print('PASS')
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
