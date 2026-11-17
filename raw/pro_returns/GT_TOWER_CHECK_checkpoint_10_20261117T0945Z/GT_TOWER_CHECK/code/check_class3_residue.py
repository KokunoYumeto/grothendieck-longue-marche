#!/usr/bin/env python3
"""Exact symbolic verification of the class-three cochains and tame residues.

This checks polynomial identities over Q, retaining the integer-valued
binomial expressions in the mathematical proof. It does not assert a
global obstruction vanishes from finite computation.
"""
from sympy import symbols, expand, summation, sympify

a,b,h,A,B,H,x,eta = symbols('a b h A B H x eta')
C = lambda z: sympify(z)*(sympify(z)-1)/2
eps = (x-1)/2
canonical_D = h*x*A + C(a+1)*x*B + a*x*x*A*B-eps*x*x*H
canonical_F = h*x*B + a*C(x*B+1)-eps*x*x*H-eta*x*B
W_D = -(a+eps)*x*x*H-C(a)*x*B
W_F = (b+eps)*x*x*(A*B-H)+C(b)*x*A-eta*x*B
agh,bgh,hgh = a+x*A,b+x*B,h+x*x*H+a*x*B
delta_ha = x**3*H*A-hgh*agh+h*a
delta_hb_abinomb = (x**3*(H*B-A*C(B))
                    -(hgh*bgh-agh*C(bgh))+(h*b-a*C(b)))
assert expand(W_D-canonical_D-delta_ha)==0
assert expand(W_F-canonical_F-delta_hb_abinomb)==0
print('W_D = canonical Hall defect + delta(h*a): PASS')
print('W_F = canonical Hall defect + delta(h*b-a*binom(b,2)): PASS')

q,m,n,t,alpha,beta,gamma,j = symbols('q m n t alpha beta gamma j',integer=True)
e=(q-1)/2
e2=(q*q-1)/24
def wd(ag,bg,hg,ch,ah,bh,hh,eg,etg):
    return -(ag+eg)*ch**2*hh-C(ag)*ch*bh
def wf(ag,bg,hg,ch,ah,bh,hh,eg,etg):
    return (bg+eg)*ch**2*(ah*bh-hh)+C(bg)*ch*ah-etg*ch*bh
def residue(w):
    ft=w(alpha,beta,gamma,q,m,n,t,e,e2)
    tqf=w(q*m,q*n,q*t+C(q)*m*n,1,alpha,beta,gamma,0,0)
    jt=w(j*m,j*n,j*t+C(j)*m*n,1,m,n,t,0,0)
    return expand((ft-tqf-summation(jt,(j,1,q-1)))/q)
Bq=lambda z:(q-1)*((2*q-1)*z*z-3*z)/12
ZD=(m*gamma-q*(alpha+e)*t-n*C(alpha)+beta*C(q*m)/q
    +e*m*t+n*Bq(m))
ZF=(n*(gamma-alpha*beta)+q*(beta+e)*(m*n-t)+m*C(beta)-e2*n
    -alpha*C(q*n)/q-e*(m*n*n-n*t)-m*Bq(n))
assert expand(residue(wd)-ZD)==0
assert expand(residue(wf)-ZF)==0
print('q^(-1) tame relator of W_D equals A.46.5 Z_D: PASS')
print('q^(-1) tame relator of W_F equals A.46.5 Z_F: PASS')

for Q in [2,3,5,7,11,13]:
    for z in range(-30,31):
        lhs=sum(C(k*z) for k in range(1,Q))/Q
        rhs=Bq(z).subs(q,Q)
        assert expand(lhs-rhs)==0
print('Finite power-sum checks including q=2,3 and negative inertia: PASS')
print('All polynomial identities checked; no hypothetical global lift asserted.')
