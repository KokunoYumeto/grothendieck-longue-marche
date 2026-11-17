#!/usr/bin/env python3
"""Exact radical identities and the order-500 arithmetic Heisenberg group."""
import itertools
import sympy as s

x, zeta = s.symbols('x zeta')
phi = zeta**4 + zeta**3 + zeta**2 + zeta + 1
theta = s.prod((1-zeta**i*x)**i for i in range(5))
def reduce_cyclotomic(expression):
    return s.rem(s.Poly(s.expand(expression), zeta, domain=s.QQ.poly_ring(x)),
                 s.Poly(phi, zeta, domain=s.QQ.poly_ring(x))).as_expr().expand()
assert reduce_cyclotomic(s.prod(1-zeta**i*x for i in range(5))-(1-x**5)) == 0
assert reduce_cyclotomic(theta.subs(x,zeta*x)*(1-x**5)-theta*(1-x)**5) == 0
print('PASS: norm and exact Kummer identity modulo Phi_5(zeta)')
for lam in range(1,5):
    k = pow(lam,-1,5)
    reindexed = [(k*j)%5 for j in range(5)]
    p_exp = [(reindexed[j]-k*j)//5 for j in range(5)]
    assert all(reindexed[j] == k*j+5*p_exp[j] for j in range(5))
    print('Descent lambda=%d: k=%d, P exponent vector=%s' % (lam,k,p_exp))

def mul(g,h):
    a,b,c,l = g
    aa,bb,cc,ll = h
    return ((a+l*aa)%5,(b+l*bb)%5,(c+l*l*cc+a*l*bb)%5,l*ll%5)
def inv(g):
    a,b,c,l = g
    j = pow(l,-1,5)
    return (-j*a%5,-j*b%5,j*j*(a*b-c)%5,j)
e=(0,0,0,1)
G=set(itertools.product(range(5),range(5),range(5),range(1,5)))
assert len(G)==500
for g in G:
    assert mul(g,inv(g))==mul(inv(g),g)==e
gens=[(1,0,0,1),(0,1,0,1),(0,0,0,2)]
def generated(generators):
    seen={e}; stack=[e]
    while stack:
        g=stack.pop()
        for h in generators:
            gh=mul(g,h)
            if gh not in seen:
                seen.add(gh); stack.append(gh)
    return seen
assert generated(gens)==G
commutators={mul(mul(mul(g,h),inv(g)),inv(h)) for g in G for h in G}
H={g for g in G if g[3]==1}
assert commutators==H
assert len(H)==125
Hcomm={mul(mul(mul(g,h),inv(g)),inv(h)) for g in H for h in H}
center={(0,0,c,1) for c in range(5)}
assert Hcomm==center
assert all(mul(z,h)==mul(h,z) for z in center for h in H)
for z in center-{e}:
    assert {mul(mul(g,z),inv(g)) for g in G} <= center-{e}
print('PASS: H5 semidirect F5^* has order500 and commutator subgroup H5 of order125')
print('PASS: [H5,H5]=Z of order5; all conjugates of nonzero Z remain nonzero Z')
print('PASS: maximal abelian quotient has order4, with the cyclotomic projection')
