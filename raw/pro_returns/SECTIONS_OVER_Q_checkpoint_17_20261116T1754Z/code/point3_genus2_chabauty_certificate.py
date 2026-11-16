#!/usr/bin/env python3
"""Exact arithmetic certificate for A189, using only local rational arithmetic.

The proof supplies the all-coefficient convergence estimates and the
Neron/formal-group comparison.  This certificate checks the literal
Mumford divisors, doubling functions, valuations, and finite truncations.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as S

BASE = Path(__file__).resolve().parent
x = S.symbols('x')
f = S.Poly(x**5-54*x, x, domain=S.QQ)


def rat(a):
    return Q(int(a.p), int(a.q)) if isinstance(a,S.Rational) else Q(a)


def vp(a):
    a=rat(a)
    if not a:
        return 10**9
    n,d=a.numerator,a.denominator
    r=0
    while n%2==0:
        n//=2
        r+=1
    while d%2==0:
        d//=2
        r-=1
    return r


def mod_unit(a,m):
    a=rat(a)
    assert a.denominator%2
    return a.numerator*pow(a.denominator,-1,m)%m


def double(U,V):
    assert (f-V*V).rem(U).is_zero
    A=(f-V*V).exquo(U)
    inv=S.invert(2*V,U)
    L=V+U*(A*inv).rem(U)
    assert (L-V).rem(U).is_zero
    R=(f-L*L).exquo(U*U)
    Un=R.monic()
    Vn=(-L).rem(Un)
    assert Un.degree()==2 and Vn.degree()<=1
    assert (f-Vn*Vn).rem(Un).is_zero
    assert f-L*L==R.LC()*U*U*Un
    return Un,Vn,L,R.LC()


def reciprocal_sqrt_coefficients(c,limit):
    """b(t)^2 f(c+t)=f(c); use 2 f b'+f' b=0 exactly."""
    F=rat(f.eval(S.Rational(c.numerator,c.denominator)))
    A=[Q(1)]+[rat(f.diff((x,i)).eval(S.Rational(c.numerator,c.denominator))) /
                 (F*int(S.factorial(i))) for i in range(1,6)]
    b=[Q(1)]
    for n in range(1,limit+1):
        b.append(-sum((2*n-i)*A[i]*b[n-i]
                      for i in range(1,min(n,5)+1))/(2*n))
        assert vp(b[-1]) >= 1-2*n
    return b


U2=S.Poly((x-3)**2,x,domain=S.QQ)
V2=S.Poly((39*x-99)/2,x,domain=S.QQ)
assert V2.eval(3)==9 and V2.diff().eval(3)==f.diff().eval(3)/18
U4,V4,L4,k4=double(U2,V2)
assert U4==S.Poly(x**2-S.Rational(5132754,769129)*x+
                      S.Rational(10169721,769129),x)
assert V4==S.Poly((44708953611*x-121694660451)/2698104532,x)
U8,V8,L8,k8=double(U4,V4)
den=16459917593113792410798392089
assert U8==S.Poly(x*x+S.Rational(21417625950097970853055914846,den)*x+
                       S.Rational(308227194535288413050444696841,den),x)
c=rat(-U8.nth(1)/2)
d=c*c-rat(U8.nth(0))
F=rat(f.eval(S.Rational(c.numerator,c.denominator)))
vc=rat(V8.eval(S.Rational(c.numerator,c.denominator)))
slope=rat(V8.nth(1))
assert mod_unit(c,4)==1
assert (vp(c),vp(d),vp(F),vp(vc),vp(slope))==(0,6,0,2,-3)
sqrt_ratio=F/(slope*slope*d)
assert vp(sqrt_ratio-1)==4
assert mod_unit(d/Q(64),8)==3
print('PASS: the two exact doubling functions give 4D and 8D by their literal divisor identities')
print('8D CENTRE MOD256',mod_unit(c,256))
print('VALUATIONS c,d,f(c),V(c),V_slope',tuple(vp(t) for t in (c,d,F,vc,slope)))
print('v2(f(c)/(V_slope^2*d)-1)',vp(sqrt_ratio-1))

b=reciprocal_sqrt_coefficients(c,14)
Ssum=sum(b[2*j]*d**j/Q(2*j+1) for j in range(7))
Nsum=sum(b[2*j+1]*d**(j+1)/Q(2*j+3) for j in range(7))
assert vp(Ssum-1)>=2
assert vp(Nsum)>=4
rho=c+Nsum/Ssum
assert mod_unit(rho,4)==1
print('PASS: fourteen exact reciprocal-square-root coefficients satisfy the proved bound')
print('SYMMETRIC SLOPE MOD4096',mod_unit(rho,4096),'MOD4',mod_unit(rho,4))

a=reciprocal_sqrt_coefficients(Q(3),18)
tested=0
for e in range(3,11):
    for odd in range(1,32,2):
        h=Q(2**e*odd)
        I1=sum(a[n]*h**(n+1)/Q(n+1) for n in range(len(a)))
        extra=sum(a[n]*h**(n+2)/Q(n+2) for n in range(len(a)))
        assert vp(I1)==e
        assert vp(extra/I1)==e-1
        assert mod_unit(3+extra/I1,4)==3
        tested+=1
print('PASS:',tested,'literal small-disc integral truncations have nonzero first integral and slope3 mod4')

# Every ordinary Q2 solution has odd u,v; the finite power residues
# used in the proof are exact consequences of the eighth-power map.
assert {pow(u,8,32) for u in range(1,32,2)}=={1}
for u in range(1,32,2):
    for v in range(1,32,2):
        if (3*pow(u,8)-2*pow(v,8)-1)%32==0:
            X=3*u*u*pow(v*v,-1,8)%8
            assert X==3
print('PASS: all unit eighth-power residues give the exact genus-two disc x=3 mod8')

data={
    'f':str(f.as_expr()),
    'U2':str(U2.as_expr()),'V2':str(V2.as_expr()),
    'U4':str(U4.as_expr()),'V4':str(V4.as_expr()),
    'L4':str(L4.as_expr()),'leading_factor4':str(k4),
    'U8':str(U8.as_expr()),'V8':str(V8.as_expr()),
    'L8':str(L8.as_expr()),'leading_factor8':str(k8),
    'centre':str(c),'delta_squared':str(d),
    'valuations':[vp(t) for t in (c,d,F,vc,slope)],
    'sqrt_ratio_minus_one_valuation':vp(sqrt_ratio-1),
    'symmetric_slope_mod4096':mod_unit(rho,4096),
    'small_disc_tests':tested,
}
(BASE/'point3_genus2_chabauty_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: A189 exact arithmetic; all infinite tails and section maps are proved in the accompanying source')
