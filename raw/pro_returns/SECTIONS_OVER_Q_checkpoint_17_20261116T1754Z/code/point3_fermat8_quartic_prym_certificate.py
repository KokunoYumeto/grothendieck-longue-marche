#!/usr/bin/env python3
"""Exact local counts and divisor tests for the three remaining N8 factors."""
from pathlib import Path
from math import gcd, comb
from fractions import Fraction
import json
import sympy as sp

BASE=Path(__file__).resolve().parent
T=sp.symbols("T")
primes=[5,7,11,13,17,19,23,29,31]
families=[(-12,1,Fraction(-1,2)),(18,1,Fraction(1,3)),(3,-2,Fraction(1))]

def legendre(a,p):
    a%=p
    return 0 if not a else 1 if pow(a,(p-1)//2,p)==1 else -1

def valuation(a,p):
    e=0
    while a%p==0:
        e+=1;a//=p
    return e

def counts(A,B,p):
    d=next(d for d in range(2,p) if legendre(d,p)==-1)
    def mul(a,b):
        return ((a[0]*b[0]+d*a[1]*b[1])%p,
                (a[0]*b[1]+a[1]*b[0])%p)
    def power(a,n):
        ans=(1,0)
        while n:
            if n&1:ans=mul(ans,a)
            a=mul(a,a);n//=2
        return ans
    g=gcd(4,p-1)
    n1=1
    e1=1
    for z in range(p):
        f=(A*z**3+B*z)%p
        n1+=1 if f==0 else g if pow(f,(p-1)//g,p)==1 else 0
        e1+=1+legendre(f,p)
    n2=1
    e2=1
    for a in range(p):
        for b in range(p):
            zz=(a,b)
            z3=mul(mul(zz,zz),zz)
            ff=((A*z3[0]+B*a)%p,(A*z3[1]+B*b)%p)
            n2+=1 if ff==(0,0) else 4 if power(ff,(p*p-1)//4)==(1,0) else 0
            e2+=1+legendre(ff[0]**2-d*ff[1]**2,p)
    trE=p+1-e1
    assert p*p+1-e2==trE*trE-2*p
    trA=(p+1-n1)-trE
    trA2=(p*p+1-n2)-(trE*trE-2*p)
    a2=(trA*trA-trA2)//2
    fp=T**4-trA*T**3+a2*T**2-p*trA*T+p*p
    return {"p":p,"quartic_count":n1,"quartic_quadratic_count":n2,
            "elliptic_count":e1,"elliptic_quadratic_count":e2,
            "prym_frobenius":str(fp),"prym_order":int(fp.subs(T,1)),
            "irreducible":sp.Poly(fp,T).is_irreducible}

def conv(a,b,n,p):
    out=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<n:out[i+j]=(out[i+j]+x*y)%p
    return out

def rank_mod(a,p):
    a=[r[:] for r in a]
    rank=0
    for j in range(len(a[0])):
        k=next((k for k in range(rank,len(a)) if a[k][j]%p),None)
        if k is None:continue
        a[rank],a[k]=a[k],a[rank]
        iv=pow(a[rank][j],-1,p)
        a[rank]=[x*iv%p for x in a[rank]]
        for k in range(len(a)):
            if k!=rank:
                c=a[k][j]
                if c:a[k]=[(x-c*y)%p for x,y in zip(a[k],a[rank])]
        rank+=1
        if rank==len(a[0]):break
    return rank

def divisor_test(A,B,z0,n,p=101):
    # N(z,w)/(z-z0)^n has no poles except possibly order n at Q=(z0,-1)
    # and a zero of order n at P=(z0,1), precisely when these jets vanish.
    N=2*n
    z0m=(z0.numerator*pow(z0.denominator,-1,p))%p
    ff=[(A*comb(3,k)*pow(z0m,3-k,p)+(B*z0m if k==0 else B if k==1 else 0))%p
        if k<=3 else 0 for k in range(N)]
    assert ff[0]==1
    w=[1]
    for k in range(1,N):
        w2=conv(w,w,k+1,p)
        w4=conv(w2,w2,k+1,p)
        w.append((ff[k]-w4[k])*pow(4,-1,p)%p)
    wp=[[1]+[0]*(N-1)]
    for b in range(1,4):wp.append(conv(wp[-1],w,N,p))
    basis=[(a,b) for b in range(4) for a in range(max(0,(4*n-3*b)//4+1))]
    columns=[]
    for a,b in basis:
        za=[comb(a,k)*pow(z0m,a-k,p)%p if k<=a else 0 for k in range(N)]
        jet=conv(za,wp[b],N,p)
        real={0:1,1:0,2:-1,3:0}[b]
        imag={0:0,1:1,2:0,3:-1}[b]
        columns.append(jet+[real*x%p for x in jet[:n]]
                       +[imag*x%p for x in jet[:n]])
    matrix=[[c[i] for c in columns] for i in range(4*n)]
    rr=rank_mod(matrix,p)
    return {"torsion_exponent_test":n,"jet_prime":p,"basis":basis,
            "matrix_rows":4*n,"matrix_columns":len(basis),"rank":rr,
            "no_principal_multiple":rr==len(basis)}

out=[]
for A,B,z0 in families:
    assert A*z0**3+B*z0==1
    rows=[counts(A,B,p) for p in primes]
    ells=set()
    for r in rows:ells.update(sp.factorint(r["prym_order"]))
    torsion_bound=1
    for ell in ells:
        exponent=min(valuation(r["prym_order"],ell) for r in rows if r["p"]!=ell)
        torsion_bound*=ell**exponent
    test=divisor_test(A,B,z0,torsion_bound) if torsion_bound<=64 else None
    assert torsion_bound == 2
    assert test["no_principal_multiple"]
    chosen_p = 13 if (A,B)==(3,-2) else 5
    chosen = next(row for row in rows if row["p"] == chosen_p)
    assert chosen["irreducible"]
    expected = T**4-24*T**2+169 if chosen_p==13 else T**4+8*T**2+25
    assert sp.sympify(chosen["prym_frobenius"]) == expected
    data={"A":A,"B":B,"point_z":str(z0),"point_w":1,
          "finite_field_rows":rows,"torsion_order_bound":torsion_bound,
          "divisor_test":test}
    out.append(data)
    print("CURVE w^4 =",A,"z^3 +",B,"z; P =",z0,1)
    print("PRYM ORDERS",[(r["p"],r["prym_order"]) for r in rows])
    print("TORSION ORDER BOUND",torsion_bound)
    print("DIVISOR TEST",test)
    print("EULER POLYNOMIALS",[(r["p"],r["prym_frobenius"]) for r in rows])

u,v,z,w=sp.symbols("u v z w")
rel=3*u**8-2*v**8-1
maps=[
    (-12,1,-u**4/2,u*v**2,-u**4/2),
    (18,1,v**4/3,u**2*v,v**4/3),
    (3,-2,u**4/v**4,u/v**3,-u**4/v**12),
]
for A,B,zz,ww,mult in maps:
    assert sp.cancel(ww**4-A*zz**3-B*zz-mult*rel)==0
print("PASS: three actual cyclic-eight plane-quartic maps")
(BASE/"point3_fermat8_quartic_prym_certificate_data.json").write_text(
    json.dumps(out,indent=2)+"\n")
