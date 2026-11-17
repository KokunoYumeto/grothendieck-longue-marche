#!/usr/bin/env python3
"""Prime-three Heisenberg and local obstruction certificates for original A44 exponents."""
import itertools
import sympy as s

x,zeta=s.symbols('x zeta')
phi=zeta*zeta+zeta+1
theta=(1-zeta*x)*(1-zeta*zeta*x)**2
def red(expr):
    return s.rem(s.Poly(s.expand(expr),zeta,domain=s.QQ.poly_ring(x)),
                 s.Poly(phi,zeta,domain=s.QQ.poly_ring(x))).as_expr().expand()
assert red(theta.subs(x,zeta*x)*(1-x**3)-theta*(1-x)**3)==0
assert red(theta.subs(zeta,zeta**2)*(1-zeta**2*x)**3-theta**2)==0
print('PASS: cubic Kummer identity and explicit cyclotomic descent')

def mul(g,h):
    a,b,c,l=g; aa,bb,cc,ll=h
    return ((a+l*aa)%3,(b+l*bb)%3,(c+l*l*cc+a*l*bb)%3,l*ll%3)
def inv(g):
    a,b,c,l=g; j=pow(l,-1,3)
    return (-j*a%3,-j*b%3,j*j*(a*b-c)%3,j)
G=set(itertools.product(range(3),range(3),range(3),range(1,3)))
H={g for g in G if g[3]==1}
Z={(0,0,c,1) for c in range(3)}
comm=lambda g,h:mul(mul(mul(g,h),inv(g)),inv(h))
assert len(G)==54 and len(H)==27
assert {comm(g,h) for g in G for h in G}==H
assert {comm(g,h) for g in H for h in H}==Z
assert all(mul(z,g)==mul(g,z) for z in Z for g in G)
print('PASS: order54; derived subgroup H3 order27; center of H3 order3')

for q in range(1,27,9):
    assert ((q*q-1)//3)*pow(8,-1,3)%3==0
    for a in range(0,9,3):
        for c in range(9):
            if c%3==0:
                continue
            for u in range(9):
                residue=24*(c-q*a*u)+(q*q-1)*u*(24*23//2)
                assert residue%3==0 and residue%9!=0
print('PASS: eta(F)=0 mod3 for q=1 mod9; every allowed third residue has v3 exactly1')

for k in range(1,1000001):
    q=72*k+1
    if not s.isprime(q):
        continue
    if pow(q-2,(q-1)//24,q)!=1 or pow(3,(q-1)//3,q)!=1:
        continue
    zz=pow(int(s.primitive_root(q)),(q-1)//3,q)
    xx=int(s.nthroot_mod(3,3,q))
    value=(1-zz*xx)*pow((1-zz*zz*xx)%q,2,q)%q
    symbol=pow(value,(q-1)//3,q)
    if symbol==1:
        continue
    yy=int(s.nthroot_mod(q-2,24,q))
    assert pow(yy,24,q)==q-2 and pow(xx,3,q)==3
    assert zz!=1 and pow(zz,3,q)==1 and q%72==1
    for lam in (1,2):
        for j in range(3):
            zz1=pow(zz,lam,q); xx1=xx*pow(zz,j,q)%q
            val=(1-zz1*xx1)*pow((1-zz1*zz1*xx1)%q,2,q)%q
            assert pow(val,(q-1)//3,q)!=1
    print('Small prime q =',q,'(not the actual first A44 prime q0)')
    print('zeta3 =',zz,'; x =',xx,'; (-2)^(1/24) =',yy)
    print('theta =',value,'; theta^((q-1)/3) =',symbol)
    print('PASS: modulus72 radical and nonzero-center conditions; all6 choices give nonzero test')
    break
else:
    raise AssertionError('No finite-field certificate in declared search range')
