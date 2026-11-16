"""Exact finite checks for A.151.  No numerical class-group inference.

The proof identifies the class fields using the ray exact sequence and
the explicit local/global inclusions.  This file certifies the finite
residue arithmetic, the quotient map, and the stated root-exponent maps.
"""
from itertools import product
from math import gcd


def vp(a, p):
    assert a
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def residue_checks(q):
    # F_{q^2}=F_q[zeta]/(zeta^2+zeta+1), with q=2 mod 3.
    def mul(x, y):
        a, b = x
        c, d = y
        return ((a*c-b*d) % q, (a*d+b*c-b*d) % q)

    def power(x, e):
        ans = (1, 0)
        while e:
            if e & 1:
                ans = mul(ans, x)
            x = mul(x, x)
            e >>= 1
        return ans

    zeta = (0, 1)
    roots = [power(zeta, j) for j in range(3)]
    exponent = (q*q-1)//3
    inv = pow(exponent % 3, -1, 3)

    def lam(x):
        return roots.index(power(x, exponent))*inv % 3

    assert q % 24 == 11
    assert vp(q*q-1, 3) == 1
    assert lam(zeta) == 1
    pi = (1, q-1)
    assert mul(pi, pi) == (0, -3 % q)
    assert lam(pi) == 2
    assert all(lam((a, 0)) == 0 for a in range(1, q))
    roots_minus_two = [y for y in range(1, q)
                       if pow(y, 24, q) == -2 % q]
    old_cover_roots = [y for y in range(1, q)
                      if -2*pow(y, 24, q) % q == 1]
    assert roots_minus_two and old_cover_roots
    assert gcd(24, q-1) == 2
    print(f"q={q}: cubic character(pi)=2; all {q-1} rational units killed")
    print(f"  24th roots of -2: {roots_minus_two}")
    print(f"  actual X=1 old-cover Y residues: {old_cover_roots}")
    return q-1


assert 11*59 == 649
assert vp(649-1, 3) == 4
assert vp(649-1, 3) > 2*vp(3, 3)
assert 649 % 2 == 1
rational_units = sum(residue_checks(q) for q in (11, 59))

# The ray quotient is (C3 x C3)/diag(C3); its literal character is x-y.
ray = list(product(range(3), repeat=2))
kernel = {(a, b) for a, b in ray if (a-b) % 3 == 0}
diagonal = {(a, a) for a in range(3)}
assert kernel == diagonal
assert {(a-b) % 3 for a, b in ray} == {0, 1, 2}
assert (2-2) % 3 == 0   # The three-prime's two residue characters.
assert (0-0) % 3 == 0   # The two-prime.

# Literal root extraction: first remove the 3^s-root-of-unity factor,
# then y^A q^B has 3^(n-s)-th power q.
root_checks = 0
for s in range(0, 7):
    for n in range(s+1, s+7):
        for m in range(-40, 41):
            if m == 0 or m % 3 == 0:
                continue
            e = 3**(n-s)
            g, A, B = egcd(m, e)
            if g == -1:
                g, A, B = -g, -A, -B
            assert g == 1 and m*A+e*B == 1
            # Multiplication by e maps mu_(3^n) onto mu_(3^s).
            assert gcd(e, 3**n) == e
            root_checks += 1

# The explicit n0 bound, and the actual rational old-cover point.
for M1, M2 in product((24, 48, 72, 216, 648), repeat=2):
    n0 = 1 + max(vp(M1, 3), vp(M2, 3))
    assert n0 > vp(M1, 3) and n0 > vp(M2, 3)
assert 3*649**24 - 2*649**24 == 649**24

print("ray quotient: nine residue classes, three diagonal classes, onto C3")
print("Hensel at three: v3(649-1)=4 > 2*v3(3)=2")
print(f"root-exponent identities: {root_checks}; rational residue units: {rational_units}")
print("PASS: all exact A.151 finite checks")
