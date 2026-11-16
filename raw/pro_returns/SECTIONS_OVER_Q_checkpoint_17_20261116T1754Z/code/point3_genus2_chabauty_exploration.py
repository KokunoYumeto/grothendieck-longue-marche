"""Local exact exploration; this file does not assert a Chabauty theorem.

Rational Mumford arithmetic on y^2=x^5-54x, followed by valuations
of multiples of [(3,9)-infinity].  Kept separate from certified A186.
"""

from fractions import Fraction
import sympy as S

x = S.symbols("x")
f = S.Poly(x**5 - 54*x, x, domain=S.QQ)
one = S.Poly(1, x, domain=S.QQ)
zero = S.Poly(0, x, domain=S.QQ)


def poly(a):
    return S.Poly(a, x, domain=S.QQ)


def reduced(u, v):
    u = u.monic()
    v = v.rem(u)
    assert (f-v*v).rem(u).is_zero
    while u.degree() > 2:
        un = (f-v*v).exquo(u).monic()
        v = (-v).rem(un)
        u = un
    assert u.degree() <= 2
    assert (f-v*v).rem(u).is_zero
    return u, v


def add(D, E):
    u1,v1 = D
    u2,v2 = E
    if u1.degree() == 0:
        return E
    if u2.degree() == 0:
        return D
    a,b,d0 = S.gcdex(u1,u2)
    if (v1+v2).is_zero:
        c,e,d = one/d0.LC(),zero,d0.monic()
    else:
        c,e,d = S.gcdex(d0,v1+v2)
    s1,s2,s3 = c*a,c*b,e
    assert s1*u1+s2*u2+s3*(v1+v2) == d
    u = (u1*u2).exquo(d*d)
    v = (s1*u1*v2+s2*u2*v1+s3*(v1*v2+f)).exquo(d).rem(u)
    return reduced(u,v)


def neg(D):
    return D[0], -D[1]


def mul(n,D):
    if n < 0:
        return mul(-n,neg(D))
    R=(one,zero)
    while n:
        if n&1:
            R=add(R,D)
        D=add(D,D)
        n >>= 1
    return R


def vp(a,p=2):
    a=Fraction(a)
    if not a:
        return None
    r=0
    n,d=a.numerator,a.denominator
    while n%p==0:
        n//=p
        r+=1
    while d%p==0:
        d//=p
        r-=1
    return r


if __name__ == "__main__":
    P=(poly(x-3),poly(9))
    assert add(P,neg(P)) == (one,zero)
    for n in range(1,5):
        assert add(mul(n,P),P)==mul(n+1,P)
    for odd in (1,3,5,7,15):
        D=mul(odd,P)
        for k in range(6):
            print(odd*2**k,
                  "u valuations",[vp(c) for c in D[0].all_coeffs()],
                  "v valuations",[vp(c) for c in D[1].all_coeffs()],
                  flush=True)
            D=add(D,D)
