#!/usr/bin/env python3
"""Exact finite maps in E.65; independent standard-library certificate.

The program checks matrix identities and finite characters only.  It does
not decide the restriction of the resulting character to full profinite GT.
"""
from itertools import product
from pathlib import Path
from collections import Counter
import json
import time

START = time.monotonic()
HERE = Path(__file__).resolve().parent


def mul(a, b, n):
    return ((a[0]*b[0]+a[1]*b[2]) % n,
            (a[0]*b[1]+a[1]*b[3]) % n,
            (a[2]*b[0]+a[3]*b[2]) % n,
            (a[2]*b[1]+a[3]*b[3]) % n)


def inv(a, n):
    d = pow((a[0]*a[3]-a[1]*a[2]) % n, -1, n)
    return tuple(d*x % n for x in (a[3], -a[1], -a[2], a[0]))


def conj(a, b, n):
    return mul(mul(a, b, n), inv(a, n), n)


def power(a, k, n):
    if k < 0:
        return power(inv(a, n), -k, n)
    out = (1, 0, 0, 1)
    while k:
        if k & 1:
            out = mul(out, a, n)
        a = mul(a, a, n)
        k //= 2
    return out


def reduce(a, n):
    return tuple(x % n for x in a)


I = (1, 0, 0, 1)
U = (1, 1, 0, 1)
L = (1, 0, -1, 1)
S = mul(U, mul(L, U, 12), 12)
Rplus = mul(U, L, 12)
R = tuple(-x % 12 for x in Rplus)
assert power(R, 3, 12) == I
assert power(Rplus, 3, 12) == tuple(-x % 12 for x in I)
assert mul(S, R, 12) == power(U, -1, 12)

covariances = []
for rho in range(12):
    f = (1, -8*rho % 12, -8*rho % 12, (1+64*rho*rho) % 12)
    v = power(U, 8*rho, 12)
    assert conj(v, S, 12) == mul(S, f, 12)
    assert conj(v, R, 12) == mul(inv(f, 12), R, 12)
    assert conj(v, reduce(L, 12), 12) == conj(inv(f, 12), reduce(L, 12), 12)
    assert reduce(v, 4) == I
    covariances.append({'rho_mod12': rho, 'f': f, 'V': v})

V4 = {I, (1, 2, 0, 1), (1, 0, 2, 1), (1, 2, 2, 1)}
assert {a for a in V4 if conj(a, reduce(R, 4), 4) == reduce(R, 4)} == {I}
assert all(mul(a, b, 4) in V4 for a in V4 for b in V4)

GL = [a for a in product(range(3), repeat=4)
      if (a[0]*a[3]-a[1]*a[2]) % 3]
SL = [a for a in GL if (a[0]*a[3]-a[1]*a[2]) % 3 == 1]
r, s = reduce(R, 3), reduce(S, 3)
C3 = [a for a in SL if conj(a, r, 3) == r]
C2 = [a for a in SL if conj(a, s, 3) == s]
assert len(GL) == 48 and len(SL) == 24
assert len(C3) == 6 and len(C2) == 4
assert set(C3) == {mul(power(r, a, 3), power(reduce((-1, 0, 0, -1), 3), b, 3), 3)
                   for a in range(3) for b in range(2)}
assert set(C2) == {power(s, a, 3) for a in range(4)}


def epsilon3(a):
    av = ((a[0]-a[1]) % 3, (a[2]-a[3]) % 3)
    assert av in {(1, 2), (2, 1)}
    return int(av == (2, 1))


def epsilon2(a):
    return next(j % 2 for j in range(4) if power(s, j, 3) == a)


pairs = list(product(C3, C2))
bits = lambda p: epsilon3(p[0]) ^ epsilon2(p[1])
for a, b in product(pairs, repeat=2):
    ab = (mul(a[0], b[0], 3), mul(a[1], b[1], 3))
    assert bits(ab) == (bits(a) ^ bits(b))
N3 = [a for a in GL if conj(a, r, 3) in {r, power(r, 2, 3)}]
N2 = [a for a in GL if conj(a, s, 3) in {s, power(s, 3, 3)}]
assert len(N3) == 12 and len(N2) == 16
for n, a in product(N3, C3):
    assert epsilon3(conj(n, a, 3)) == epsilon3(a)
for n, a in product(N2, C2):
    assert epsilon2(conj(n, a, 3)) == epsilon2(a)
assert epsilon3(reduce((-1, 0, 0, -1), 3)) == 1
assert epsilon2(I) == 0

# Integral free class-two convention (a,b,c) = x^a y^b [x,y]^c.
def hmul(p, q):
    a, b, c = p
    d, e, f = q
    return a+d, b+e, c+f-b*d


def hinv(p):
    a, b, c = p
    return -a, -b, -c-a*b


def theta(p):
    a, b, c = p
    return b, a, -c-a*b


class_two = 0
for rho, d in product(range(-12, 13), repeat=2):
    h = (rho, rho, d)
    f = hmul(hinv(theta(h)), h)
    assert f == (0, 0, rho*rho+2*d)
    if f == (0, 0, 0):
        assert rho % 2 == 0
    class_two += 1

# Actual splitting-field law of X^4-3/4, with z=r0, i=i:
# (a,b): z -> i^a z, i -> (-1)^b i.
D8 = list(product(range(4), range(2)))
dmul = lambda g, h: ((g[0] + (-1)**g[1]*h[0]) % 4, (g[1]+h[1]) % 2)
dab = lambda g: (g[0] % 2, g[1])
common = [(g, h) for g, h in product(D8, repeat=2) if dab(g) == dab(h)]
ddelta = lambda p: ((p[0][0]-p[1][0]) % 4)//2
assert len(common) == 16
for p, q in product(common, repeat=2):
    pq = (dmul(p[0], q[0]), dmul(p[1], q[1]))
    assert ddelta(pq) == (ddelta(p) ^ ddelta(q))
assert sum(ddelta(p) == 0 for p in common) == 8
assert all(ddelta((g, g)) == 0 for g in D8)

out = {
    'status': 'PASS_EXACT_CM_PARITY_CHARACTER_MAPS',
    'source_scope': 'multiplier-one full gentle pairs; no full-GT image assertion',
    'R_order_three': R, 'Rplus_order_six': Rplus,
    'line': [1, 2],
    'covariance': 'Ad(V)(S)=S q(f), Ad(V)(R)=q(f)^(-1)R, V=U^(8 rho)',
    'all_mod12_covariances': covariances,
    'GL2_F3_order': len(GL), 'SL2_F3_order': len(SL),
    'Eisenstein_norm_one_Cartan': C3,
    'Gaussian_norm_one_Cartan': C2,
    'Cartan_pair_order': len(pairs),
    'missing_parity_counts': dict(Counter(bits(p) for p in pairs)),
    'all_Cartan_pair_products_checked': len(pairs)**2,
    'normalizer_orders': [len(N3), len(N2)],
    'all_normalizer_character_invariance_checks': len(N3)*len(C3)+len(N2)*len(C2),
    'integral_class_two_checks': class_two,
    'D8_fibre_product_order': len(common),
    'D8_difference_character_products_checked': len(common)**2,
    'E58_bits': [1, 0],
    'full_GT_restriction': 'NOT_DECIDED',
    'seconds': round(time.monotonic()-START, 6),
}
(HERE/'a_cm_parity_character.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
