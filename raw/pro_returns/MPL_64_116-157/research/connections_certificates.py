#!/usr/bin/env python3
"""Independent S/H mathematical certificates; no manuscript input or image access.
Run: python connections_certificates.py
Requires SymPy. Extracted from connections_hua.md on 2026-11-17.
"""

# Certificate C1
import sympy as s
x, u = s.symbols('x u')
q = x*(x-1)*(x-u)
R = x*(x-1)/(2*(x-u))
lhs = u*(1-u)*s.Rational(3,4)/(x-u)**2 + (1-2*u)/(2*(x-u)) - s.Rational(1,4)
assert s.factor(lhs-(s.diff(R,x)-R*s.diff(q,x)/(2*q))) == 0
P = (1-2*u)/(u*(1-u))
Q = -1/(4*u*(1-u))
assert s.factor(2*Q-s.diff(P,u)-P**2/2) == (u**2-u+1)/(2*u**2*(u-1)**2)
print('C1 PASS: exact differential residual 0; Schwarzian', s.factor(2*Q-s.diff(P,u)-P**2/2))

# Certificate C2
red = lambda f: s.cancel(f, modulus=3)
A = s.Matrix([[0,1],[1/(4*u*(1-u)),-P]]).applyfunc(red)
B = s.eye(2)
for _ in range(3):
    B = (B.diff(u)-A*B).applyfunc(red)
assert (B*B).applyfunc(red) == s.zeros(2)
expected = s.Matrix([[-u-1,(u+1)**2],[-1,u+1]])/(u**2*(u-1)**2)
assert (B-expected).applyfunc(red) == s.zeros(2)
assert B[1,0] != 0
# Review-response check: de Rham coefficient columns use the dual connection.
BdR = s.eye(2)
for _ in range(3):
    BdR = (BdR.diff(u)+A.T*BdR).applyfunc(red)
assert (BdR+B.T).applyfunc(red) == s.zeros(2)
assert (BdR*BdR).applyfunc(red) == s.zeros(2)
print('C2 PASS: nonzero period/solution p-curvature modulo 3 =', B); print('C2 square =', (B*B).applyfunc(red)); print('C2 DUAL CHECK PASS: de Rham p-curvature is negative transpose and square-zero')

# Certificate C3
a = s.Matrix([[1,1],[0,1]])
b = s.Matrix([[1,0],[-1,1]])
assert a*b*a == b*a*b
assert (a*b)**3 == -s.eye(2)
assert (a*b)**6 == s.eye(2)
print('C3 PASS: braid relation, full twist maps to -I, central square maps to I')

# Certificate C4
from itertools import product
p = 5
points = [None,0,1,2,3,4]  # None denotes infinity
pairs = {frozenset([None,0]),frozenset([1,4]),frozenset([2,3])}
perms, paired = set(), set()
for a,b,c,d in product(range(p), repeat=4):
    if (a*d-b*c) % p == 0:
        continue
    def act(x):
        num,den = (a,c) if x is None else ((a*x+b)%p,(c*x+d)%p)
        return None if den == 0 else num*pow(den,-1,p)%p
    perm = tuple(act(x) for x in points)
    perms.add(perm)
    if {frozenset(act(x) for x in pair) for pair in pairs} == pairs:
        paired.add(perm)
assert len(perms) == 120
assert len(paired) == 24
print('C4 PASS: unpaired symmetries',len(perms),'paired symmetries',len(paired))
print('ALL FOUR CERTIFICATES PASS')
