#!/usr/bin/env python3
"""Exact homology detector for the central ambiguity in the S2 origami map.

Columns use the symplectic basis (e1,f1,e2,f2).  The transvection is
T_v(w)=w+<v,w>v.  All relations are checked over Z before reduction.
"""
import sympy as s

J=s.diag(s.Matrix([[0,1],[-1,0]]),s.Matrix([[0,1],[-1,0]]))
I=s.eye(4)
basis=[I[:,i] for i in range(4)]
vectors=[basis[0],basis[1],basis[0]-basis[2],basis[3],basis[2]]
twists=[I+v*v.T*J for v in vectors]
for T in twists:
    assert T.T*J*T==J
for i in range(5):
    for j in range(i+1,5):
        if j==i+1:
            assert twists[i]*twists[j]*twists[i]==twists[j]*twists[i]*twists[j]
        else:
            assert twists[i]*twists[j]==twists[j]*twists[i]

T1,T2,T3,T4,T5=twists
hyper=T1*T2*T3*T4*T5**2*T4*T3*T2*T1
assert hyper==-I
assert (T1*T2*T3*T4*T5)**6==I
X=T1**2*T3*T5**2
Y=T2*T4
assert (X-I)**2==s.zeros(4)
assert (Y-I)**2==s.zeros(4)
print('PASS: five integral symplectic transvections satisfy the chain braid relations.')
print('PASS: the genus-two hyperelliptic word acts by -I; the length-five product has sixth power I.')
print('X = alpha1^2 alpha3 alpha5^2:')
print(X)
print('Y = alpha2 alpha4:')
print(Y)
print('PASS: (X-I)^2=(Y-I)^2=0 over Z.')

z=s.Symbol('z')
positive=s.Poly((z-1)**4,z, modulus=3)
negative=s.Poly((z+1)**4,z, modulus=3)
assert positive!=negative
for label,M in [('X',X),('Y',Y)]:
    for lam in [1,2]:
        A=(M**lam).applyfunc(lambda a:int(a)%3)
        B=(-A).applyfunc(lambda a:int(a)%3)
        assert s.Poly(A.charpoly(z).as_expr(),z,modulus=3)==positive
        assert s.Poly(B.charpoly(z).as_expr(),z,modulus=3)==negative
        assert A.trace()%3==1 and B.trace()%3==2
        print(f'PASS: {label}^{lam} modulo3 has trace1; its hyperelliptic translate has trace2.')
print('Characteristic polynomials over F3:',positive.as_expr(),negative.as_expr())
print('PASS: multiplication by the hyperelliptic involution changes each required conjugacy class.')
print('This certifies only the central-ambiguity detector. The actual GT comparison is proved separately.')
