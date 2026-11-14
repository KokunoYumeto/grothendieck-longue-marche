#!/usr/bin/env python3
"""Exact uniform ell-primary theta packet bounds for the unresolved F4 pair.

P16=X4-2X3+X2-32X+256. For each ell find m with P mod ell | X^m-1,
then give B(X) modulo ell^(e+1) satisfying
 (X^m-1)B(X)=ell^e mod(P,ell^(e+1)).
The factor 1+ell*R is an ell-adic unit, so every ell-primary point fixed
by Frobenius^m is killed by ell^e. A.C2.12 applies because m splits J[ell].
No actual existence at the upper bound is inferred.
"""
from pathlib import Path
from itertools import permutations
from math import lcm
import json
import sympy as sp

X=sp.symbols('X');P=sp.Poly(X**4-2*X**3+X**2-32*X+256,X)
M=[[0,0,0,-256],[1,0,0,32],[0,1,0,-1],[0,0,1,2]]
I=[[int(i==j) for j in range(4)] for i in range(4)]

def mm(a,b,q):return [[sum(a[i][k]*b[k][j] for k in range(4))%q for j in range(4)] for i in range(4)]
def mp(n,q):
    r=[row[:] for row in I];a=[[v%q for v in row] for row in M]
    while n:
        if n&1:r=mm(r,a,q)
        a=mm(a,a,q);n>>=1
    return r

def det(a):
    n=len(a);out=0
    for perm in permutations(range(n)):
        v=1
        for i in range(n):v*=a[i][perm[i]]
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        out+=(-1 if inv%2 else 1)*v
    return out

def val(a,ell,cap):
    if not a:return cap
    r=0
    while a%ell==0:a//=ell;r+=1
    return r

def ppow(n,f,ell):
    r=sp.Poly(1,X,modulus=ell);a=sp.Poly(X,X,modulus=ell)
    while n:
        if n&1:r=(r*a).rem(f)
        a=(a*a).rem(f);n>>=1
    return r

def packet(ell,forced_m=None):
    factors=sp.factor_list(P,modulus=ell)[1];orders=[]
    for f,multiplicity in factors:
        f=sp.Poly(f,X,modulus=ell);o=ell**f.degree()-1
        for prime in sp.factorint(o):
            while o%prime==0 and ppow(o//prime,f,ell)==sp.Poly(1,X,modulus=ell):o//=prime
        power=1
        while power<multiplicity:power*=ell
        orders.append(o*power)
    m=lcm(*orders)
    if forced_m is not None:
        assert forced_m%m==0
        m=forced_m
    assert ppow(m,sp.Poly(P,X,modulus=ell),ell)==sp.Poly(1,X,modulus=ell)
    precision=24;q=ell**precision;A=mp(m,q)
    for i in range(4):A[i][i]=(A[i][i]-1)%q
    determinant=det(A)%q;vd=val(determinant,ell,precision);assert vd<precision
    adj=[]
    for i in range(4):
        a=[[A[r][c] for c in range(4) if c!=i] for r in range(1,4)]
        adj.append(((-1)**i*det(a))%q)
    va=min(val(c,ell,precision) for c in adj);e=vd-va;assert e>=1 and precision>=vd+e+1
    small=ell**(e+1);inv=pow(determinant//ell**vd,-1,small)
    coeff=[(c//ell**va*inv)%small for c in adj]
    B=mp(m,small)
    for i in range(4):B[i][i]=(B[i][i]-1)%small
    result=[sum(B[i][j]*coeff[j] for j in range(4))%small for i in range(4)]
    assert result==[ell**e,0,0,0]
    return {'ell':ell,'torsion_splitting_exponent_m':m,'determinant_valuation':vd,'adjugate_column_minimum_valuation':va,'theta_exponent_bound':e,'theta_order_divides':ell**e,'certificate_modulus':small,'B_coefficients_ascending':coeff,'checked_remainder':result}

def main():
    rows=[packet(ell) for ell in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]]
    out={'status':'PASS','frobenius_polynomial_coefficients_ascending':[256,-32,1,-2,1],'field_size':16,'curves':'geometricF4modulikeys203 and302','packets':rows,'scope':'Upper bounds only. Entire-primary theta emptiness additionally requires a complete empty theta_n test at n=ell^e.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    for r in rows:print(r['ell'],r['torsion_splitting_exponent_m'],r['theta_order_divides'],r['B_coefficients_ascending'],flush=True)
if __name__=='__main__':main()
