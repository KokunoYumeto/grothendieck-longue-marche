#!/usr/bin/env python3
"""Exact BCH identities and mod-3 origin labels for B.9."""
from fractions import Fraction as Q
from itertools import product

def mul(a,b):
    u,v,w=a
    U,V,W=b
    return (u+U,v+V,w+W+Q(9,2)*(u*V-v*U))

def action(q,a):
    u,v,w=a
    return (q*u,q*v,q*q*w)

def swap(a):
    u,v,w=a
    return (v,u,-w)

def f(q):
    return Q(q*q-1,24)

def origin(d,q,k):
    if d == 'P': return (Q(k),Q(0),Q(0))
    if d == 'Q': return (Q(0),Q(k),f(q))
    if d == 'O': return (Q(-k),Q(-k),f(q)/2)
    raise ValueError(d)

vals=(-2,-1,0,1,2)
elems=list(product(vals,repeat=3))
for a,b in product(elems,repeat=2):
    assert swap(mul(a,b)) == mul(swap(a),swap(b))
for q,r,k,l,d in product((5,7,11,13),(5,7,11,13),vals,vals,('P','Q','O')):
    assert f(q*r) == f(q)+q*q*f(r)
    assert origin(d,q*r,k+q*l) == mul(origin(d,q,k),action(q,origin(d,r,l)))
print('BCH coordinate interchange is a group automorphism: PASS (15625 pairs)')
print('All three exact cusp cocycle identities: PASS (1200 cases)')

# The affine interchange sends P to Q, Q to P, and fixes O.
for q in (5,7,11,13):
    for d,e in (('P','Q'),('Q','P'),('O','O')):
        im=mul(swap(origin(d,q,0)),(Q(0),Q(0),f(q)))
        assert im == origin(e,q,0)
print('Affine arithmetic interchange P<->Q, O fixed: PASS')

def mod3(a):
    return (a.numerator*pow(a.denominator,-1,3))%3

delta=Q(7*7-1,3)
labels=[mod3(origin(d,7,0)[2]/delta) for d in ('P','Q','O')]
assert labels == [0,2,1]
print('P,Q,O origin labels relative to (chi^2-1)/3:', labels)
assert len(set(labels))==3
print('Three inherited central cusp origins are distinct: PASS')
