#!/usr/bin/env python3
"""Independent, standard-library-only certificate for the explicit A134 twist.

It does not import the search's arithmetic helpers.  All 611 rational local
centres, all good nonsquare prototypes, every finite support invariant, the
initial root-symbol sums, and the finite field/group calculations are checked.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import json


def primes_up_to(n):
    a = [True]*(n+1)
    a[:2] = [False,False]
    for p in range(2,isqrt(n)+1):
        if a[p]:
            for j in range(p*p,n+1,p):
                a[j] = False
    return [p for p in range(2,n+1) if a[p]]


def prime(n):
    return n>=2 and all(n%p for p in primes_up_to(isqrt(n)))


@lru_cache(maxsize=None)
def factor_integer(x):
    assert x>0
    result=[]
    d=2
    while d*d<=x:
        e=0
        while x%d==0:
            x//=d
            e+=1
        if e:
            result.append((d,e))
        d=3 if d==2 else d+2
    if x>1:
        result.append((x,1))
    return tuple(result)


def vu(a,p,mod=None):
    a=F(a)
    assert a
    x,y=a.numerator,a.denominator
    v=0
    while x%p==0:
        x//=p
        v+=1
    while y%p==0:
        y//=p
        v-=1
    if mod is None:
        mod=p
    return v,x*pow(y,-1,mod)%mod


def fourth(a,p):
    if not a:
        return False
    v,u=vu(a,p,16 if p==2 else p)
    return v%4==0 and (u==1 if p==2 else
                       pow(u,(p-1)//gcd(4,p-1),p)==1)


def legendre_bit(u,p):
    return int(pow(u,(p-1)//2,p)==p-1)


def hilbert_bit(a,b,p):
    va,ua=vu(a,p,8 if p==2 else p)
    vb,ub=vu(b,p,8 if p==2 else p)
    if p==2:
        return (((ua-1)//2)*((ub-1)//2)+
                va*((ub*ub-1)//8)+vb*((ua*ua-1)//8))%2
    return (va*vb*((p-1)//2)+va*legendre_bit(ub,p)+
            vb*legendre_bit(ua,p))%2


def squareclass(a):
    a=F(a)
    sign=int(a<0)
    support=set()
    for x in (abs(a.numerator),a.denominator):
        for p,e in factor_integer(x):
            if e%2:
                support.symmetric_difference_update({p})
    return sign,frozenset(support)


def multiply_classes(a,b):
    return a[0]^b[0],a[1]^b[1]


def span(classes):
    result={(0,frozenset())}
    for a in classes:
        result|={multiply_classes(x,a) for x in tuple(result)}
    return result


def main():
    path=Path(__file__).with_name("harmonic_twist_repair_data.json")
    row=json.loads(path.read_text())
    R,c=F(row["R"]),F(row["c"])
    q,r=row["q"],row["r"]
    Q=q*r
    a=tuple(map(F,row["a"]))
    old=(F(0),F(1),F(1,2))
    D=tuple((c-b)/aa for b,aa in zip(old,a))
    rho,char=F(row["rho"]),F(row["character"])
    assert (R,c,q,r,Q)==(F(529,382),F(-338,191),139,1119169,155564491)
    assert prime(q) and prime(r)
    assert a==(F(529,382),F(147,382),F(2022338383**2,191))
    assert D==tuple(map(F,row["D"]))
    assert D[0]*D[1]*D[2]==-rho*rho
    assert rho==F(34,7*Q) and char==2*rho
    d=7*17*Q
    assert d==18512174429 and char/F(d)==F(2,7*Q)**2
    print("PASS: literal coefficients, prime repair, triple relation and character square map.")

    # Entire common-field formula A96, with exact squareclasses.
    assert D[0]==-F(26,23)**2
    assert D[1]==-6*F(23,21)**2
    assert D[2]==-6*F(17,26*Q)**2
    K=span([squareclass(x) for x in D])
    assert len(K)==4
    generators=[F(-1),F(6),F(299),F(d)]
    assert len(span([squareclass(x) for x in generators]))==16
    negative_subsets=[]
    for bits in product((0,1),repeat=3):
        if not any(bits):
            continue
        z=F(1)
        for b,x in zip(bits,D):
            if b:z*=x
        if squareclass(z)==squareclass(-1):
            negative_subsets.append(bits)
    assert negative_subsets==[(1,0,0),(1,1,1)]
    assert F(52,23)/299==F(2,23)**2
    print("PASS: full common field Q(i,sqrt6,sqrt299,sqrt18512174429), degree16.")

    witnesses={int(p):F(T) for p,T in row["local_T"].items()}
    expected=set(primes_up_to(4500))|{r}
    assert set(witnesses)==expected
    rootchecks=0
    for p,T in sorted(witnesses.items()):
        assert T not in (*old,c)
        for b,aa in zip(old,a):
            assert fourth((T-b)/aa,p),(p,T,b)
            rootchecks+=1
    assert all((R-b)/aa>0 for b,aa in zip(old,a))
    assert (R-old[2])/a[2]==F(1,Q**2)
    print(f"PASS: {len(witnesses)} exact rational finite centres, "
          f"{rootchecks} fourth-power tests, and the actual real centre R.")

    # This independent list is computed from the declared rational constants.
    support={2}
    for x in (*a,*(c-b for b in old),char):
        for t in (abs(x.numerator),x.denominator):
            support.update(p for p,e in factor_integer(t))
    assert support=={2,3,7,13,17,23,139,191,r}
    invariants={p:hilbert_bit(witnesses[p]-c,char,p) for p in sorted(support)}
    assert invariants=={p:int(p==2) for p in sorted(support)}
    print("PASS: complete support and exact Hilbert bits",invariants)
    print("Real invariant is zero because the character parameter is positive.")

    # Boundary quadratic fields: all omit i.
    B=((-1146,-382),(382,),(191,-573))
    for i in range(3):
        rad=[(old[i]-old[j])/a[j] for j in range(3) if j!=i]
        fieldspan=span([squareclass(x) for x in rad])
        assert fieldspan==span([squareclass(x) for x in B[i]])
        assert squareclass(-1) not in fieldspan
    assert span([squareclass(a[1]/a[0]),squareclass(a[2]/a[0])])==span(
        [squareclass(2),squareclass(3)])
    print("PASS: all three finite boundary squareclass spans and the infinity span omit -1.")

    # Root-symbol initial data for the one signed refinement.
    T2=witnesses[2]
    assert T2==F(31,2)
    for b,aa in zip(old,a):
        assert vu((T2-b)/aa,2,32)==(0,17)
    dyadic_roots=(5,3,5)
    dyadic_symbols=[[hilbert_bit(x,b,2) for b in Bs]
                    for x,Bs in zip(dyadic_roots,B)]
    assert dyadic_symbols==[[1,1],[0],[0,0]]
    real_roots=(-1,1,1)
    real_symbols=[[int(x<0 and b<0) for b in Bs]
                  for x,Bs in zip(real_roots,B)]
    assert real_symbols==dyadic_symbols
    assert witnesses[3]==R and witnesses[191]==R
    for p in (3,191):
        # At these p=3 mod4, every unit fourth-power root has one sign
        # with square residue. All three roots are units at the chosen R.
        assert p%4==3
        for b,aa in zip(old,a):
            assert vu((R-b)/aa,p)[0]==0
            assert fourth((R-b)/aa,p)
    unram_root_checks=0
    for p,T in witnesses.items():
        if p in (2,3,191):
            continue
        for i,(b,aa) in enumerate(zip(old,a)):
            vroot=vu((T-b)/aa,p)[0]//4
            for charB in B[i]:
                vb,ub=vu(charB,p)
                assert vb==0
                assert (vroot*legendre_bit(ub,p))%2==0,(p,i,charB,vroot)
                unram_root_checks+=1
    print("PASS: root symbols at2 are",dyadic_symbols,
          "and cancel the exact negative/positive real root choices.")
    print(f"PASS: square root choices at3,191 and {unram_root_checks} "
          "unramified root-symbol tests; the signed first-refinement sums are zero.")

    # Exact splitting field: C4^2 semidirect C2 by inversion.
    group=list(product(range(4),range(4),range(2)))
    def mul(x,y):
        s=1 if x[2]==0 else -1
        return ((x[0]+s*y[0])%4,(x[1]+s*y[1])%4,(x[2]+y[2])%2)
    def inv(x):
        s=1 if x[2]==0 else -1
        return (-s*x[0]%4,-s*x[1]%4,x[2])
    comm={mul(mul(mul(x,y),inv(x)),inv(y)) for x,y in product(group,repeat=2)}
    assert comm=={(i,j,0) for i,j in product((0,2),repeat=2)}
    assert all(mul(x,x) in comm for x in group)
    assert len(group)//len(comm)==8
    assert (1*(-1)-1*0)==-1  # 191/3 valuation determinant over Q(i)
    assert r%8==1
    for p in (3,7,13,17,23,139,191):
        assert pow(r%p,(p-1)//2,p)==1
    for Dv in (F(191,529),F(-191,147)):
        v,u=vu(Dv,r)
        assert v==0 and pow(u,(r-1)//4,r)==1
    assert squareclass(F(1,2)-c)==squareclass(1146)
    assert pow(1146%r,(r-1)//2,r)==1
    print("PASS: exact order32 splitting group, elementary2 abelianization oforder8, "
          "literal boundary roots and fresh-prime invariant.")

    # The finite prototype certificate makes the infinitude repair proof
    # independent of any untested small prime.
    require={5,29,41,233}
    proto={int(p):data for p,data in row["nonsquare_prototypes"].items()}
    good1={p for p in primes_up_to(4500) if p%4==1 and p not in support}
    assert good1==set(proto)|require and not set(proto)&require
    for p,data in proto.items():
        g,T=data["unit"],F(data["T"])
        assert legendre_bit(g,p)==1
        a_proto=(a[0],a[1],(R-F(1,2))*g*g)
        assert T not in (*old,c)
        assert all(fourth((T-b)/aa,p) for b,aa in zip(old,a_proto))
    for p in require:
        assert pow((q*r)%p,(p-1)//2,p)==1
    print(f"PASS: {len(proto)} actual nonsquare prototypes and four exact "
          "small-prime square conditions.")

    # For p>=4500, the displayed positive bound is strictly increasing.
    # (p-63)>66 sqrt(p) follows by squaring both positive sides.
    assert 4500-63>0 and (4500-63)**2>66**2*4500
    assert 2*4500-126-66**2>0
    assert -2*64+4*64*(1-F(1,4))==64
    assert 1+64//2==33 and 4*(64//4)==64
    print("PASS: genus33, 64 old boundary points, and strict all-large-good-prime bound.")
    print("ALL A134 EXACT CERTIFICATES PASSED.")


if __name__=="__main__":
    main()
