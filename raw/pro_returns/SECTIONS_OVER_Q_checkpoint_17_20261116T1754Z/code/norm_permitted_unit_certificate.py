from math import isqrt
from fractions import Fraction
from itertools import product
from pathlib import Path
import sympy as sp

q=22441
roots=[4048,8110,10283]
c=4048
H=c**3-3
D=H//q
assert all(q%d for d in range(2,isqrt(q)+1))
assert q%24==1 and (q-1)%3==0 and (q-1)%9!=0
assert H==q*2955829 and H%(q*q)!=0
assert len(set(roots))==3 and all(pow(a,3,q)==3 for a in roots)
assert pow(q-2,(q-1)//24,q)==1
assert all(pow((1-a)%q,(q-1)//3,q)==1 for a in roots)
print('Prime q:',q,'; roots of 3:',roots,'; q mod 72:',q%72)
print('H=c^3-3:',H,'=',q,'*',D)
print('Full B24 and all pre-repair beta0 cube radicals split: passed')

# Norms are computed from the exact multiplication matrix in Q[alpha]/(alpha^3-3).
x=sp.Symbol('x')
f=x**3-3
def coeffs(p):
    r=sp.Poly(sp.rem(sp.expand(p),f,x),x)
    return [r.nth(i) for i in range(3)]
def norm(p):
    mat=sp.Matrix.hstack(*[sp.Matrix(coeffs(p*x**j)) for j in range(3)])
    return sp.factor(mat.det())
u=sp.rem((c-x)**3,f,x)/H
beta=sp.rem((1-x)*sp.rem((c-x)**3,f,x),f,x)/H
assert norm(c-x)==H and norm(u)==1 and norm(beta)==-2
print('beta numerator coefficients:',coeffs(beta*H),'; denominator:',H)
print('Exact norms N(c-alpha)=H, N(u)=1, N(beta)=-2: passed')

# Actual q-adic unit characters of beta; one extra Hensel digit suffices.
zeta=2026
assert pow(zeta,3,q)==1 and zeta!=1
char_to_log={pow(zeta,j,q):j for j in range(3)}
unit_logs=[]
valuation_vector=[]
alpha_logs=[]
for a in roots:
    correction=(-(a**3-3)//q)*pow(3*a*a,-1,q)%q
    lift=a+q*correction
    assert (lift**3-3)%(q*q)==0
    if a==c:
        assert (c-lift)%q==0 and (c-lift)%(q*q)!=0
        local_c=(c-lift)//q
        val=2
    else:
        local_c=c-lift
        val=-1
    beta_unit=(1-lift)*pow(local_c,3,q)*pow(D,-1,q)%q
    symbol=pow(beta_unit,(q-1)//3,q)
    assert symbol==pow(pow(D,-1,q),(q-1)//3,q)
    unit_logs.append(char_to_log[symbol])
    valuation_vector.append(val)
    alpha_logs.append(char_to_log[pow(a,(q-1)//3,q)])
assert valuation_vector==[2,-1,-1]
assert len(set(unit_logs))==1
assert len(set(alpha_logs))==3
print('Valuations:',valuation_vector)
print('Unit cubic logarithms:',unit_logs,'; alpha cubic logarithms:',alpha_logs)
print('Root-ratio cubic characters:',[pow(a*pow(roots[0],-1,q)%q,(q-1)//3,q) for a in roots])

# e is any 3-adic unit, k any integral q-valuation, x,y are Q0,R unit classes.
checked=0
for e,k,xlog,ylog in product([1,2],range(3),range(3),range(3)):
    residues=[(t*(e*xlog+a)-e*k*(z+e*ylog))%3 for t,a,z in zip(valuation_vector,alpha_logs,unit_logs)]
    assert any(residues)
    # Pairwise differences remove every rational choice exactly.
    for i in range(3):
        for j in range(3):
            assert (residues[i]-residues[j]+alpha_logs[i]-alpha_logs[j])%3==0
    checked+=1
print('All e,k,x,y residue choices excluded:',checked)

# The canonical two-adic divisor is retained: H odd and c even imply u is a unit
# at every prime over2. The unique linear root is3 mod8; beta0 has valuation1.
assert H%2==1 and c%2==0
assert pow(3,3,8)==3 and (1-3)%4==2
print('Canonical two-adic divisor retained by u: passed')
print('All A.103 exact identities passed. No obstruction for the underlying rational pair is asserted.')
