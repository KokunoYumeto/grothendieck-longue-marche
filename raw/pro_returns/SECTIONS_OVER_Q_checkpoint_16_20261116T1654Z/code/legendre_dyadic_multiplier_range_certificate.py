#!/usr/bin/env python3
"""Exact local-model and finite-group audit for A.94."""

from fractions import Fraction
from itertools import product


def vp(a, p):
    a = Fraction(a)
    if not a:
        return float("inf")
    n, d, v = abs(a.numerator), a.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def invs(a, b):
    return (16*(a*a-a*b+b*b),
            32*(a+b)*(2*a-b)*(a-2*b),
            16*a*a*b*b*(a-b)**2)


models = 0
twists = 0
resolvents = 0
for u in range(-255, 256, 2):
    for h in (1, 3):
        for t in (2**h*u, 1-2**h*u):
            c4, c6, delta = invs(1, t)
            assert vp(c4, 2) == 4 and vp(delta, 2) == 4+2*h
            if h == 1:
                assert vp(c6, 2) >= 7 and (c4//16) % 4 == 3
                assert vp(4*t*(1-t), 2) == 3
                resolvents += 1
            else:
                assert vp(c6, 2) == 6
            models += 1
        c4, c6, delta = invs(2**(h+1), 2*u)
        assert vp(c4, 2) == 6 and vp(delta, 2) == 10+2*h
        if h == 1:
            assert vp(c6, 2) >= 10 and (c4//64) % 4 == 3
            t = Fraction(u, 2)
            assert vp(4*t*(1-t), 2) == 0
            resolvents += 1
        else:
            assert vp(c6, 2) == 9
        models += 1
    # The literal quadratic two-twist at contact-infinity orderone.
    c4, c6, delta = invs(2, u)
    assert vp(c4, 2) == 4 and vp(c6, 2) >= 7 and vp(delta, 2) == 6
    assert (c4//16) % 4 == 3
    # Its further two-twist has the minimal triple used to exclude conductor64.
    assert (vp(4*c4, 2), vp(64*delta, 2)) == (6, 12)
    assert ((4*c4)//64) % 4 == 3
    twists += 1

# The algebraic minimality lemma for integral Weierstrass equations.
weierstrass = 0
for a1, a2, a3, a4 in product(range(4), repeat=4):
    b2, b4 = a1*a1+4*a2, a1*a3+2*a4
    c4 = b2*b2-24*b4
    assert c4 % 2 == 1 if a1 % 2 else c4 % 16 == 0
    weierstrass += 1

odd = range(1, 1024, 2)
assert {pow(a, 3, 1024) for a in odd} == set(odd)


def mm(a, b, p):
    return ((a[0]*b[0]+a[1]*b[2]) % p,
            (a[0]*b[1]+a[1]*b[3]) % p,
            (a[2]*b[0]+a[3]*b[2]) % p,
            (a[2]*b[1]+a[3]*b[3]) % p)


sl2 = [a for a in product(range(3), repeat=4)
       if (a[0]*a[3]-a[1]*a[2]) % 3 == 1]
lines = ((1, 0), (0, 1), (1, 1), (2, 1))


def line_image(a, v):
    x, y = (a[0]*v[0]+a[1]*v[1]) % 3, (a[2]*v[0]+a[3]*v[1]) % 3
    if y == 0:
        return 0
    x = x*pow(y, -1, 3) % 3
    return (1, 2, 3)[x]


def partition(a, b, c, d):
    return frozenset((frozenset((a, b)), frozenset((c, d))))


partitions = (partition(0, 1, 2, 3), partition(0, 2, 1, 3), partition(0, 3, 1, 2))
kernel = []
images = set()
for a in sl2:
    perm = [line_image(a, v) for v in lines]
    image = tuple(partitions.index(frozenset(frozenset(perm[j] for j in pair)
                                           for pair in part))
                  for part in partitions)
    images.add(image)
    if image == (0, 1, 2):
        kernel.append(a)
assert len(sl2) == 24 and len(kernel) == 8 and len(images) == 3
identity = (1, 0, 0, 1)
orders = []
for a in kernel:
    b = identity
    for n in range(1, 9):
        b = mm(b, a, 3)
        if b == identity:
            orders.append(n)
            break
assert sorted(orders) == [1, 2, 4, 4, 4, 4, 4, 4]

# The common good reduction and the actual coefficient-seven centralizer.
affine_points = [(x, y) for x, y in product(range(2), repeat=2)
                 if (y*y+x*y-x*x*x-x) % 2 == 0]
assert affine_points == [(0, 0), (1, 0), (1, 1)]
trace, determinant = -1, 2
assert 2+1-(len(affine_points)+1) == trace
assert trace*trace-4*determinant == -7
M = (0, -2 % 7, 1, -1 % 7)
centralizer = [a for a in product(range(7), repeat=4)
               if (a[0]*a[3]-a[1]*a[2]) % 7 != 0 and mm(a, M, 7) == mm(M, a, 7)]
dets = {(a[0]*a[3]-a[1]*a[2]) % 7 for a in centralizer}
assert len(centralizer) == 42 and dets == {1, 2, 4}

print("A.94 exact certificate: all checks passed.")
print(f"Minimal-invariant rows: {models}; explicit two-twist/conductor-residue checks: {twists}.")
print(f"Integral Weierstrass c4-divisibility checks: {weierstrass}; cubic-resolvent valuation checks: {resolvents}.")
print("Cubing permutes all512 odd units modulo2^10.")
print("Actual SL2(F3) pair-partition action: imageorder3, kernelorder8, elementorders1,2,4,4,4,4,4,4.")
print("The common good F2 curve has4points; Frobenius trace−1, determinant2, discriminant−7.")
print("Literal invertible Frobenius centralizer modulo7:42matrices, determinant set{1,2,4}.")
print("The source-specific inertia and conductor criteria remain proof inputs; these finite checks audit their exact model data.")
