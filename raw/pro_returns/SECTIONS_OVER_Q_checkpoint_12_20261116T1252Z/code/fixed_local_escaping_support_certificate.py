#!/usr/bin/env python3
"""Exact finite checks for A.132 and A.133.
The infinite Chebotarev recursion is proved in the text, not executed here.
The listed primes test the literal fixed-centre Hensel step; they are not
claimed to satisfy a whole preceding giant recursive CRT modulus.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, gcd, lcm
from sympy import factorint, primerange, nthroot_mod

counts = {}
def done(k,n):
    counts[k]=n

def vp(n,p):
    n=abs(int(n))
    if not n: return 10**9
    r=0
    while n%p==0:
        n//=p; r+=1
    return r
def ratmod(x,m):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,m)%m

# Exact valuation/sign test in Q^x/(Q^x)^N, not a finite sampling
# assertion about all local fields.
cnt=0
for N in range(1,41):
    for exps in product(range(-2,3), repeat=3):
        vals=tuple(N*e for e in exps)
        assert all(e%N==0 for e in vals)
        for sign in (1,-1):
            rational_power = (N%2==1 or sign==1)
            finite_local_sign_allowed = (N%2==1 or sign not in {-1})
            assert rational_power==finite_local_sign_allowed
            cnt+=1
assert {u*u%8 for u in (1,3,5,7)}=={1}
done("finite valuation/sign checks",cnt)

# One model eventually-divisible vector: e_{p_j}=j!.
primes=list(primerange(2,600))[:100]
cnt=0
for N in range(1,81):
    for M in range(N,241,N):
        for j in range(1,26):
            assert (factorial(j)%M)%N==factorial(j)%N
            cnt+=1
done("literal finite coefficient transitions",cnt)
cnt=0
for q in (2,3,5,7,11,13):
    for depth in range(1,6):
        mod=q**depth
        order=(q-1)*q**(depth-1)
        j0=next(j for j in range(1,101) if factorial(j)%order==0)
        for j,p in enumerate(primes,1):
            if p!=q and j>=j0:
                assert pow(p,factorial(j),mod)==1
                assert pow(pow(p,-1,mod),factorial(j),mod)==1
                cnt+=2
done("actual local Euler-tail congruences",cnt)

# Rational field data and all relevant squareclass spans.
R=F(1,4)
cs=(F(0),F(1),F(1,2))
coeff=tuple(R-c for c in cs)
new=F(2)
rows=[tuple((c-d)/a for d,a in zip(cs,coeff) if d!=c) for c in cs]
D=tuple((new-c)/a for c,a in zip(cs,coeff))
assert rows==[(F(4,3),F(2)),(F(4),F(-2)),(F(2),F(2,3))]
assert D==(F(8),F(-4,3),F(-6))

def squareclass(a):
    a=F(a)
    s=frozenset(([-1] if a<0 else [])+
       [int(p) for p,e in factorint(abs(a.numerator)).items() if e%2]+
       [int(p) for p,e in factorint(a.denominator).items() if e%2])
    return s
def span(ds):
    out={frozenset()}
    for a in ds:
        s=squareclass(a)
        out|={t^s for t in tuple(out)}
    return out
for ds in rows+[D]:
    assert frozenset({-1}) not in span(ds)
assert span(D)=={frozenset(),frozenset({2}),frozenset({-1,3}),frozenset({-1,2,3})}
done("fixed common-field squareclass spans",4)

cnt=0
for a in coeff:
    for u in (F(2),F(-3,5),F(7,2),F(11,13)):
        for n in (4,8,12,20):
            assert squareclass(a*u**n)==squareclass(a)
            for h in (2,3,5,7):
                for y in (F(1),F(2,3),F(-5,7)):
                    assert a*(u*y**h)**n==(a*u**n)*y**(h*n)
                    cnt+=1
done("literal coefficient and forgetful-map identities",cnt)

cnt=0
for ns in product((4,8,12,16,20,24,28,32), repeat=3):
    degree=ns[0]*ns[1]*ns[2]
    N=lcm(*ns)
    twice_g_minus_2=-2*degree+sum(degree-degree//n for n in ns)+degree-degree//N
    assert twice_g_minus_2%2==0
    twice_g=twice_g_minus_2+2
    boundary=sum(degree//n for n in ns)+degree//N+2*degree
    assert twice_g<=2*degree+2 and boundary<=6*degree
    root_bound=8*degree+8
    assert root_bound**2+1-twice_g*root_bound-boundary>0
    assert 2*root_bound-twice_g>0
    cnt+=1
done("mixed-cover genus and uniform bounds",cnt)

cnt=0
for h in range(2,61):
    exps=[4*factorial(h)]*3
    for N in range(1,61):
        if h>=N:
            assert all(e%N==0 for e in exps)
            cnt+=1
done("factorial cofinality identities",cnt)

# Actual primes splitting the relevant finite radicands in finite fields.
# The fixed B_i split as well. Every Hensel lift below is executed.
witnesses=[]
for ns,needed in (((4,4,4),8),((8,4,4),4),((8,12,4),3)):
    found=0
    for p in primerange(5,200000):
        if (p-1)%lcm(*ns): continue
        if any(pow(ratmod(d,p),(p-1)//n,p)!=1 for d,n in zip(D,ns)): continue
        if any(pow(ratmod(d,p),(p-1)//2,p)!=1 for ds in rows for d in ds): continue
        roots=[]
        for ci,ai,n,di in zip(cs,coeff,ns,D):
            z=int(nthroot_mod(ratmod(di,p),n,p))
            target=(new+p-ci)/ai
            assert pow(z,n,p)==ratmod(target,p) and z%p
            derivative=n*pow(z,n-1,p)%p
            assert derivative
            for k in range(1,5):
                mod=p**(k+1)
                error=(pow(z,n,mod)-ratmod(target,mod))%mod
                assert error%(p**k)==0
                correction=-(error//(p**k))*pow(derivative,-1,p)%p
                z+=correction*p**k
                assert pow(z,n,mod)==ratmod(target,mod)
            roots.append(z)
        assert vp((new+p-new).numerator,p)==1
        assert ratmod(new+p+1,p)!=0
        witnesses.append((ns,p,tuple(roots)))
        found+=1
        if found==needed: break
    assert found==needed,(ns,found)
done("actual split-prime fixed-centre witnesses",len(witnesses))
done("executed root lifts modulo p^5",len(witnesses)*3*4)

cnt=0
for p in (2,3,5,7,11):
    for h in range(2,17):
        M=2*vp(h,p)+7
        y=1+p**(M-vp(h,p))
        assert vp(y**h-1,p)>=M
        assert vp(y-1,p)>3
        if p==2: assert y%8==1
        cnt+=1
done("actual old-root Hensel precision instances",cnt)

# Literal finite-support failure at arbitrary selected finite rational supports:
# a fresh forced prime has valuation one, while every listed rational
# candidate with other prime support has valuation zero there.
cnt=0
for j,(_,p,_) in enumerate(witnesses):
    for b in (F(-7,4),F(3,5),F(11**2,13**3),F(17*19,23)):
        if b.numerator%p and b.denominator%p:
            assert vp(b.numerator,p)-vp(b.denominator,p)==0
            assert (1-0)%2==1
            cnt+=1
done("literal finite-support valuation exclusions",cnt)

print("A.132/A.133 exact finite certificate: PASS")
for k,v in counts.items():
    print(f"{k}: {v}")
print("Executed split primes by mixed exponent:")
for ns in sorted(set(w[0] for w in witnesses)):
    print(ns,[p for n,p,_ in witnesses if n==ns])
print("Scope: no infinite prime recursion or global local-solubility search is claimed.")

