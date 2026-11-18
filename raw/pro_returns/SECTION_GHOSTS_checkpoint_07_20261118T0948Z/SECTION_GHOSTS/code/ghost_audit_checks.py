#!/usr/bin/env python3
"""Independent finite checks supporting the arithmetic ghost audit.

These are checks of polynomial identities, precision inequalities, and
finite models. They do not execute the enormous A.44 prime recursion,
certify an infinite branch, or replace any global cohomology proof.
"""
from fractions import Fraction
from math import factorial, gcd
import sympy as sp


def vp(n, p):
    assert n != 0
    n = abs(int(n))
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


print("SECTION_GHOSTS independent arithmetic audit")
print("1. Restricted valuation quotient used in A.101")
assert factorial(4) % 5 == 4
assert all(factorial(j + 4) % 5 == 0 for j in range(1, 101))
print("PASS: n_0 = 24 = 4 mod 5; n_j = 0 mod 5 for 1 <= j <= 100.")
print("The all-j tail assertion follows because 5 divides (j+4)! for j>=1.")

print("2. Kummer-kernel commutator arithmetic")
for h in (24, 48, 72, 120, 240, 720, 5040):
    common = h // 2
    for u in range(1, h):
        if gcd(u, h) == 1:
            common = gcd(common, u - 1)
    assert common == 2
print("PASS: gcd(h/2, {u-1: u unit mod h})=2 at seven sample moduli.")
print("The proof for all 24|h uses oddness and the multiplier -1.")

print("3. Character-sum lower-bound polynomial")
m = sp.symbols("m", integer=True, positive=True)
T = (m + 1) ** 2
bound = sp.expand(T*T - (m-1)*(m-2)*T - 3*m + 1)
assert sp.expand(bound - m*m*(5*m + 9)) == 0
print("PASS: bound at T=(m+1)^2 equals m^2(5m+9).")

print("4. Newton precision inequalities, including p=2,3")
checks = 0
for j in range(0, 25):
    old, new, later = factorial(j+4), factorial(j+5), factorial(j+6)
    for p in list(sp.primerange(2, j+7)):
        if new % p != 0:
            continue
        H = 2*vp(new, p) + j + 3
        assert H > 2*vp(old, p)
        assert H - vp(old, p) >= vp(new, p)
        L = 2*vp(later, p) + j + 4
        assert L > 2*vp(new, p)
        checks += 1
print(f"PASS: {checks} pairs (stage, coefficient prime).")

print("5. Direct tame-residue calculation from the third cochains")
q, a, b, h, A, B, H, x, e, zeta = sp.symbols("q a b h A B H x e zeta")
choose2 = lambda value: value*(value-1)/2
def WD(ag, bg, cg, chi, ah, bh, ch, eps, eta):
    return -(ag+eps)*chi**2*ch - choose2(ag)*chi*bh
def WF(ag, bg, cg, chi, ah, bh, ch, eps, eta):
    return (bg+eps)*chi**2*(ah*bh-ch)+choose2(bg)*chi*ah-eta*chi*bh
mv, nv, tv, alpha, beta, gamma, j = sp.symbols(
    "m n t alpha beta gamma j", integer=True)
eps=(q-1)/2
eta=(q*q-1)/24
def tame_residue(cochain):
    ft=cochain(alpha,beta,gamma,q,mv,nv,tv,eps,eta)
    tqf=cochain(q*mv,q*nv,q*tv+choose2(q)*mv*nv,1,
                alpha,beta,gamma,0,0)
    jt=cochain(j*mv,j*nv,j*tv+choose2(j)*mv*nv,1,
               mv,nv,tv,0,0)
    return sp.expand((ft-tqf-sp.summation(jt,(j,1,q-1)))/q)
Bq=lambda zz:(q-1)*((2*q-1)*zz**2-3*zz)/12
zd=(mv*gamma-q*(alpha+eps)*tv-nv*choose2(alpha)
    +beta*choose2(q*mv)/q+eps*mv*tv+nv*Bq(mv))
zf=(nv*(gamma-alpha*beta)+q*(beta+eps)*(mv*nv-tv)
    +mv*choose2(beta)-eta*nv-alpha*choose2(q*nv)/q
    -eps*(mv*nv**2-nv*tv)-mv*Bq(nv))
assert sp.expand(tame_residue(WD)-zd)==0
assert sp.expand(tame_residue(WF)-zf)==0
print("PASS: both exact continuous-cochain residue polynomials.")

u=sp.symbols("u")
positive=sp.expand(zd.subs({nv:0,tv:mv*u,beta:(q-1)*u}))
claimed=mv*(gamma-q*alpha*u)+(q*q-1)*u*choose2(mv)
assert sp.expand(positive-claimed)==0
print("PASS: Z_D=m(gamma-q alpha u)+(q^2-1)u binom(m,2).")

print("6. Denominators at the exceptional rational primes")
tests=0
for Q in (2,3,5,7,11,13):
    for z in range(-30,31):
        direct=sum(Fraction(jj*z*(jj*z-1),2) for jj in range(1,Q))/Q
        closed=Fraction((Q-1)*((2*Q-1)*z*z-3*z),12)
        assert direct==closed
        assert Q % direct.denominator==0
        tests+=1
print(f"PASS: {tests} exact B_q values; denominators divide q, hence are units at ell!=q.")

print("7. The coefficient-three first-failure residue")
tests=0
modulus=9
for q0 in range(1,81,9):
    for alpha0 in range(0,modulus,3):
        for gamma0 in range(modulus):
            if gamma0%3==0:
                continue
            for u0 in range(modulus):
                value=24*(gamma0-q0*alpha0*u0)+(q0*q0-1)*u0*276
                assert value%3==0 and value%9!=0
                tests+=1
print(f"PASS: {tests} residue combinations have valuation exactly one at 3 modulo 9.")

print("8. A.207 finite local data (no Selmer completeness claim)")
p=1129
assert sp.isprime(p)
assert pow(2,24,p)==276 and pow(56,24,p)==978
assert (3*276-2*978)%p==1
roots=[a0 for a0 in range(p) if pow(a0,4,p)==54]
assert roots==[16,430,699,1113]
rad=(-828*pow(1-828,3,p)*pow(24,-1,p))%p
sheets=[z for z in range(p) if pow(z,8,p)==rad]
assert sheets==[35,44,235,511,618,894,1085,1094]
bit_vectors=[]
for z in sheets:
    xx=(-6*z*z*pow(1-828,-1,p))%p
    yy=(-18*z*pow(1-828,-1,p))%p
    assert (yy*yy-xx**5+54*xx)%p==0
    bits="".join("0" if pow((xx-r)%p,(p-1)//2,p)==1 else "1" for r in roots)
    assert bits not in ("0000","1111")
    bit_vectors.append(bits)
print(f"PASS: all 8 local sheets yield {bit_vectors}.")
print("Their exclusion uses the separate global Selmer-image theorem, not established by this computation.")
print("ALL FINITE CHECKS PASSED.")

print("9. Two local tests select one of the 24 class-two lifts")
pins={(3*k % 8, 2*k % 3):k for k in range(24)}
assert len(pins)==24
assert set(pins)=={(i,j) for i in range(8) for j in range(3)}
print("PASS: k -> (k/3 mod8, k/8 mod3) is a bijection on Z/24.")
pinD=sp.expand(zd.subs({q:3,mv:1,nv:0,tv:u,beta:2*u}))
pinF=sp.expand(zf.subs({q:3,mv:1,nv:0,tv:u,beta:2*u}))
assert sp.expand(pinD-(gamma-3*alpha*u))==0
assert sp.expand(pinF+8*choose2(u+1))==0
v=sp.symbols("v")
pinD2=sp.expand(zd.subs({q:2,mv:0,nv:1,tv:-v,alpha:v}))
pinF2=sp.expand(zf.subs({q:2,mv:0,nv:1,tv:-v,alpha:v}))
assert sp.expand(pinD2-3*choose2(v+1))==0
assert sp.expand(pinF2-(gamma+beta*v-sp.Rational(1,8)))==0
print("PASS: exact residues at (q,ell)=(3,2) and (2,3), both coordinates.")

print("10. Two fresh-support normal forms")
positiveF=sp.expand(zf.subs({nv:0,tv:mv*u,beta:(q-1)*u}))
assert sp.expand(positiveF+(q*q-1)*mv*choose2(u+1))==0
negativeD=sp.expand(zd.subs({mv:0,tv:-nv*v,alpha:(q-1)*v}))
negativeF=sp.expand(zf.subs({mv:0,tv:-nv*v,alpha:(q-1)*v}))
assert sp.expand(negativeD-(q*q-1)*nv*choose2(v+1))==0
assert sp.expand(negativeF-(nv*(gamma+beta*v-(q*q-1)/24)
                           -(q*q-1)*v*choose2(nv)))==0
print("PASS: positive-A and positive-B support normal forms, including the eta correction.")
print("ALL FINITE CHECKS INCLUDING THE NEW CLASS-TWO PINNING PASSED.")
