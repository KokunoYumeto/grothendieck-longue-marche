#!/usr/bin/env python3
"""Exact finite checks for A.111, with actual Q2 power tests.

The source r may be an actual Q2 square root rather than rational.  Its
squareclass is computed from the valuation and the unit modulo32 of r^2.
Both choices of its sign are checked.  This is a finite certificate; the
unbounded valuation proof is retained in the TeX statement.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
import sympy as sp


def vu(x, modulus=32):
    x = Q(x)
    assert x
    n, d = x.numerator, x.denominator
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    while d % 2 == 0:
        d //= 2
        e -= 1
    return e, n * pow(d, -1, modulus) % modulus


def square(x):
    if not x:
        return True
    e, u = vu(x)
    return e % 2 == 0 and u % 8 == 1


def fourth(x):
    if not x:
        return False
    e, u = vu(x)
    return e % 4 == 0 and u % 16 == 1


def hilbert(a, b):
    ea, ua = vu(a, 8)
    eb, ub = vu(b, 8)
    return (((ua - 1) // 2) * ((ub - 1) // 2)
            + ea * ((ub * ub - 1) // 8)
            + eb * ((ua * ua - 1) // 8)) % 2


def F(x):
    return x * (x - 1) * (x - Q(1, 2))


def old_point(R, T):
    return all(T != c and fourth((T-c)/(R-c))
               for c in (Q(0), Q(1), Q(1, 2)))


def sqrt_squareclass(D):
    e, u = vu(D, 32)
    assert e % 2 == 0 and u % 8 == 1
    # Each entry is one actual square-root unit class modulo8.  Lifting
    # that class to a root is Hensel's square-root criterion.
    root_unit = {1: 1, 9: 3, 17: 7, 25: 5}[u]
    assert root_unit * root_unit % 32 == u
    return Q(2)**(e//2) * root_unit


def transform(z, which):
    return 1-z if which == 1 else 1/(2*z)


def normalize(R, T, c, r):
    moves = []
    e = vu(R)[0]
    if e == 0:
        moves = [1]
    elif e <= -2:
        moves = [2]
    elif e == -1:
        moves = [2, 1]
    for move in moves:
        if move == 2:
            r *= (R/c)**2
        R, T, c = (transform(x, move) for x in (R, T, c))
    assert vu(R)[0] >= 1
    return R, T, c, r, tuple(moves)


# Literal rational-function and norm identities.
t, R, c, a, X = sp.symbols("t R c a X")
FF = lambda z: z*(z-1)*(z-sp.Rational(1, 2))
assert sp.cancel(FF(1-t)+FF(t)) == 0
assert sp.cancel(FF(1/(2*t))-FF(t)/(4*t**4)) == 0
assert sp.cancel(((1/(2*t)-1/(2*c))/(1/(2*R)-1/(2*c)))
                 - ((t-c)/(R-c))*R/t) == 0
assert sp.expand((X*X+a)**2-2*a*X*X-X**4-a*a) == 0
assert sp.expand((1+a)**2-2*a-1-a*a) == 0

old_points = 0
sources = 0
symbol_checks = 0
cases = Counter()
moves_seen = Counter()
R_values = sorted({Q(2)**e * u for e, u in
                   product(range(-3, 8), (1, 3, 5, 7, 11, 15))}
                  - {Q(0), Q(1), Q(1, 2)})
X_values = [Q(2)**e*u for e, u in
            product(range(-2, 3), (1, 3, 5, 7))]
c_values = sorted({sign*Q(2)**e*u for sign, e, u in
                   product((-1, 1), range(-3, 8), (1, 3, 5, 7, 11, 15))}
                  - {Q(0), Q(1), Q(1, 2)})

for R in R_values:
    for X in X_values:
        T = R*X**4
        if not old_point(R, T):
            continue
        old_points += 1
        for c in c_values:
            if c in (R, T):
                continue
            D = -F(c)/F(R)
            if not square(D):
                continue
            sources += 1
            r0 = sqrt_squareclass(D)
            for sign in (-1, 1):
                r = sign*r0
                f = (T-c)/(R-c)
                assert hilbert(f, 2*r) == 0, (R, T, c, D, r, f)
                RR, TT, cc, rr, moves = normalize(R, T, c, r)
                moves_seen[moves] += 1
                assert old_point(RR, TT)
                ff = (TT-cc)/(RR-cc)
                assert hilbert(ff, 2*rr) == hilbert(f, 2*r)
                e, eT, k = vu(RR)[0], vu(TT)[0], vu(cc)[0]
                assert eT > 0 and (eT-e) % 4 == 0
                if TT != RR:
                    assert vu(TT-RR)[0] >= 4
                if k <= 0:
                    cases["c nonpositive valuation"] += 1
                    assert square(ff)
                elif e <= 3:
                    cases["shallow R"] += 1
                    assert eT == e
                    assert square(ff)
                elif k >= 4:
                    cases["two deep coordinates"] += 1
                    GG = lambda z: (1-z)*(1-2*z)
                    ratio = GG(cc)/GG(RR)
                    assert vu(ratio, 16) == (0, 1)
                    assert square(-cc/RR)
                else:
                    assert (k-e) % 2 == 0
                    assert vu(ff, 4) == (0, 1)
                    if square(ff):
                        cases["remaining square"] += 1
                    else:
                        cases["remaining nonsquare unit"] += 1
                        assert vu(ff-1)[0] == 2
                        assert (1+(k-e)//2) % 2 == 0
                        assert vu(2*rr)[0] % 2 == 0
                symbol_checks += 1

# Exact examples of the two exceptional valuation patterns that the proof
# handles by even v2(2r), rather than by saying f is a square.
exceptional = []
for R, T, c in ((Q(16), Q(256), Q(12)),
                (Q(32), Q(512), Q(56))):
    assert old_point(R, T)
    D = -F(c)/F(R)
    assert square(D)
    r = sqrt_squareclass(D)
    f = (T-c)/(R-c)
    assert not square(f) and vu(f-1)[0] == 2
    assert vu(2*r)[0] % 2 == 0 and hilbert(f, 2*r) == 0
    exceptional.append((R, T, c, f, vu(2*r)[0]))

assert all(cases[k] for k in (
    "shallow R", "two deep coordinates", "remaining nonsquare unit",
    "c nonpositive valuation"))
assert set(moves_seen) == {(), (1,), (2,), (2, 1)}

print("A.111 harmonic dyadic norm certificate: all checks passed.")
print("The D4 coordinate identities and both explicit norm identities are exact.")
print(f"Actual old local fourth-power points: {old_points}.")
print(f"Locally soluble negative-triple sources: {sources}.")
print(f"Quaternion evaluations, checking both root signs: {symbol_checks}.")
print("Proof cases:", dict(cases))
print("All normalization paths were checked:", dict(moves_seen))
print("The two nonsquare-f exceptions (R,T,c,f,v2(2r)):")
for row in exceptional:
    print(" ", tuple(str(x) for x in row))
print("Every computed symbol is zero. The unbounded assertion is proved in A.111.")
