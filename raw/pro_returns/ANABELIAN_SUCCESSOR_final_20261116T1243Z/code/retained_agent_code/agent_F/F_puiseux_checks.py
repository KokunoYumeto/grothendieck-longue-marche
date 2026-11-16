"""Exact finite checks for FF.22; the infinite identities are proved in TeX.

Standard-library only. All truncated coefficients are fractions, and no
floating-point arithmetic is used.
"""
from fractions import Fraction as Q

N = 13


def add(a, b):
    return [(a[i] if i < len(a) else Q(0))
            + (b[i] if i < len(b) else Q(0)) for i in range(N)]


def neg(a):
    return [-x for x in a]


def mul(a, b):
    c = [Q(0)] * N
    for i, x in enumerate(a[:N]):
        for j, y in enumerate(b[:N-i]):
            c[i+j] += x*y
    return c


def power(a, n):
    r = [Q(1)] + [Q(0)] * (N-1)
    for _ in range(n):
        r = mul(r, a)
    return r


def compose(a, b):
    assert not b[0]
    r = [Q(0)] * N
    for x in reversed(a[:N]):
        r = mul(r, b)
        r[0] += x
    return r


def binomial(alpha, scale=1):
    c = [Q(1)]
    for j in range(1, N):
        c.append(c[-1] * (alpha-j+1) * scale / j)
    return c


one = [Q(1)] + [Q(0)] * (N-1)
t = [Q(0), Q(1)] + [Q(0)] * (N-2)
s = add(t, mul(t, t))
r = [x/2 for x in add(binomial(Q(1, 2), 4), neg(one))]
assert compose(s, r) == t
assert compose(r, s) == t
print(f"Both inverse substitutions agree with t modulo t^{N}.")
print("Inverse coefficients through degree 8:", [str(x) for x in r[:9]])

ds = [1, 2, 3, 4, 6, 12]
count = 0
for d in ds:
    beta = binomial(Q(1, d))
    assert power(beta, d) == add(one, t)
    for e in ds:
        if d % e == 0:
            assert power(beta, d//e) == binomial(Q(1, e))
            count += 1
print(f"Checked {len(ds)} root equations and {count} compatibility identities exactly.")

# A rational function is represented by a pair (numerator, denominator).
minus_t_plus_one = add(one, neg(t))
t_minus_one = add(t, neg(one))
orbit_t = [(t, one), (one, t), (minus_t_plus_one, one),
           (one, minus_t_plus_one), (t_minus_one, t), (t, t_minus_one)]
differences = []
for numerator, denominator in orbit_t:
    cross_difference = add(mul(s, denominator), neg(numerator))
    assert any(cross_difference)
    differences.append([str(c) for c in cross_difference[:5]])
print("t+t^2 is outside the six-element anharmonic orbit of t.")
print("Six nonzero cross-multiplied differences through degree 4:")
for d in differences:
    print(d)
print("All checks passed; these finite checks do not replace the infinite proof.")
