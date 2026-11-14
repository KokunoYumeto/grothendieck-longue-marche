#!/usr/bin/env python3
"""Exact finite unramified-ring certificates for F.28--F.29.

All calculations use Z/5^k[X]/(F), where F modulo 5 is verified
irreducible.  No numerical complex or 5-adic approximations are used.
"""
from itertools import product
import sympy as sp


class Ring:
    def __init__(self, polynomial, precision):
        self.f = tuple(polynomial)  # coefficients below the monic term
        self.d = len(self.f)
        self.k = precision
        self.mod = 5**precision
        self.zero = (0,)*self.d
        self.one = (1,)+(0,)*(self.d-1)

    def add(self, a, b):
        return tuple((x+y) % self.mod for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x % self.mod for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def scale(self, c, a):
        return tuple(c*x % self.mod for x in a)

    def mul(self, a, b):
        out = [0]*(2*self.d-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x*y
        for i in range(len(out)-1, self.d-1, -1):
            for j, f in enumerate(self.f):
                out[i-self.d+j] -= out[i]*f
        return tuple(x % self.mod for x in out[:self.d])

    def pow(self, a, n):
        result = self.one
        while n:
            if n & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            n //= 2
        return result

    def inverse(self, a):
        assert any(x % 5 for x in a)
        exponent = (5**self.d-1)*5**(self.k-1)
        result = self.pow(a, exponent-1)
        assert self.mul(a, result) == self.one
        return result


def hensel_root(f, root, exponent, target, precision):
    value = tuple(root)
    field = Ring(f, 1)
    for k in range(1, precision):
        ring = Ring(f, k+1)
        error = ring.sub(ring.pow(value, exponent),
                         ring.scale(target, ring.one))
        assert all(x % 5**k == 0 for x in error)
        residue = tuple(x//5**k % 5 for x in error)
        derivative = field.scale(exponent,
                                 field.pow(tuple(x % 5 for x in value),
                                           exponent-1))
        correction = field.neg(field.mul(residue, field.inverse(derivative)))
        value = tuple((x+5**k*c) % 5**(k+1)
                      for x, c in zip(value, correction))
        assert ring.pow(value, exponent) == ring.scale(target, ring.one)
    return value


def valuation(x):
    assert x
    n = 0
    while x % 5 == 0:
        n += 1
        x //= 5
    return n


def choose_residues(f, m):
    ring = Ring(f, 1)
    values = list(product(range(5), repeat=ring.d))
    roots = [a for a in values if ring.pow(a, m) == ring.scale(2, ring.one)]
    primitive = [a for a in values if ring.pow(a, m) == ring.one
                 and all(ring.pow(a, m//int(p)) != ring.one
                         for p in sp.factorint(m))]
    assert len(roots) == m and len(primitive) == int(sp.totient(m))
    if m == 4:
        alpha = (0, 1, 0, 0)
        zeta = (2, 0, 0, 0)
    else:
        alpha, zeta = roots[0], primitive[0]
    assert alpha in roots and zeta in primitive
    return alpha, zeta


def compute_depth(f, m):
    alpha0, zeta0 = choose_residues(f, m)
    d = len(f)
    residue_order = 5**d-1
    for precision in range(2, 9):
        ring = Ring(f, precision)
        alpha = hensel_root(f, alpha0, m, 2, precision)
        zeta = hensel_root(f, zeta0, m, 1, precision)
        denominator = ring.sub(alpha, ring.one)
        denominator_inv = ring.inverse(denominator)
        depths = []
        for j in range(1, m):
            numerator = ring.sub(ring.mul(ring.pow(zeta, j), alpha),
                                 ring.one)
            ratio = ring.mul(numerator, denominator_inv)
            error = ring.sub(ring.pow(ratio, residue_order), ring.one)
            vals = [valuation(x) for x in error if x]
            if not vals:
                break
            v = min(vals)
            assert v >= 1
            depths.append(v-1)
        if len(depths) == m-1:
            return 1+max(depths), depths, precision
    raise AssertionError("The specified finite examples did not terminate.")


X = sp.symbols("X")
examples = [(2, (-2, 0)), (3, (-2, 0)),
            (4, (-2, 0, 0, 0)), (6, (-2, 0))]
print("Cyclic-cover finite obstructions at the tripod point 2")
for m, f in examples:
    polynomial = X**len(f)+sum(c*X**i for i, c in enumerate(f))
    assert sp.Poly(polynomial, X, modulus=5).is_irreducible
    d = len(f)
    assert (5**d-1) % (4*m) == 0
    n, e, precision = compute_depth(f, m)
    order = m*5**(n*(m+1))
    print(f"m={m}, unramified degree={d}, F={polynomial}")
    print(f"  exact divisibilities e_j={e}, n_m={n}; checked modulo 5^{precision}")
    print(f"  finite quotient order={order}, vector rank={m+1}, exponent=5^{n}")

ring = Ring((-2, 0, 0, 0), 2)
alpha = (0, 1, 0, 0)
i = (7, 0, 0, 0)
assert ring.pow(alpha, 4) == ring.scale(2, ring.one)
assert ring.pow(i, 2) == ring.neg(ring.one)
log_coefficients = []
for j in range(4):
    unit = ring.sub(alpha, ring.pow(i, j))
    error = ring.sub(ring.pow(unit, 624), ring.one)
    assert all(x % 5 == 0 for x in error)
    log_coefficients.append(tuple((x//5)*pow(624, -1, 5) % 5 for x in error))
expected = [(0, 0, 2, 1), (0, 0, 3, 2),
            (0, 0, 2, 4), (0, 0, 3, 3)]
assert log_coefficients == expected
print("Fourth-root cover: log(alpha-i^j)/5 modulo 5")
for j, row in enumerate(log_coefficients):
    print(" ", j, row)

# The conjugation permutation is e_j -> e_(j-1).
# Hence the coefficient at e_0 in its lambda-eigenspace is
# (1/4) sum_j lambda^(-j) b_j.
fourier = {}
for lam in (1, 2, 4, 3):
    fourier[lam] = tuple(sum(pow(lam, (-j) % 4, 5)*row[k]
                               for j, row in enumerate(log_coefficients))
                            *pow(4, -1, 5) % 5
                            for k in range(4))
assert fourier[2] == (0, 0, 0, 1)
assert fourier[4] == (0, 0, 2, 0)
print("Fourier eigenprojections (lambda mod 5 -> coefficient vector):")
for lam, row in fourier.items():
    print(" ", lam, row)
print("  lambda=i and lambda=-1 are nonzero and are distinct eigenspaces.")
print("  Their pure-inner Johnson directions are linearly independent.")
print("PASS: every exact unramified-ring certificate succeeded.")
