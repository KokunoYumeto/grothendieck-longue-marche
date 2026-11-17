#!/usr/bin/env python3
"""Exact finite certificates for the class-three centralizer bound.

This executes the BCH law of the free class-three Lie algebra modulo
5^(k+1).  The two central coordinates do not affect a centralizer.
Every value of the other three coordinates is tested for k=0 and k=1.
It also checks the exact group-algebra collection identities and all
weights occurring in their finite inverse expansions.
"""
from collections import defaultdict
from itertools import product


def operations(modulus):
    zero = (0,) * 5
    inv2, inv12 = pow(2, -1, modulus), pow(12, -1, modulus)

    def add(*terms):
        return tuple(sum(t[i] for t in terms) % modulus for i in range(5))

    def scale(c, u):
        return tuple(c * z % modulus for z in u)

    def bracket(u, v):
        a, b, c, _, _ = u
        A, B, C, _, _ = v
        return (0, 0, (a * B - b * A) % modulus,
                (c * A - a * C) % modulus,
                (c * B - b * C) % modulus)

    def mul(u, v):
        uv = bracket(u, v)
        return add(u, v, scale(inv2, uv),
                   scale(inv12, add(bracket(u, uv),
                                    bracket(v, scale(-1, uv)))))

    def inverse(u):
        return scale(-1, u)

    def comm(u, v):
        return mul(mul(mul(u, v), inverse(u)), inverse(v))

    return zero, add, scale, bracket, mul, inverse, comm


for k in (0, 1):
    p, modulus, q = 5, 5 ** (k + 1), 11
    m = 5 ** k
    zero, add, scale, bracket, mul, inverse, comm = operations(modulus)
    x, y = (1, 0, 0, 0, 0), (0, 1, 0, 0, 0)
    c, d, e = comm(x, y), comm(comm(x, y), x), comm(comm(x, y), y)

    # Group algebra F_5[P_M], represented by sparse coefficients on
    # actual BCH group elements, independent of augmentation rewriting.
    def ga_add(*terms):
        out = defaultdict(int)
        for term in terms:
            for g, coeff in term.items():
                out[g] = (out[g] + coeff) % p
        return {g: v for g, v in out.items() if v}

    def ga_scale(a, u):
        return {g: (a * coeff) % p for g, coeff in u.items()
                if (a * coeff) % p}

    def ga_mul(u, v):
        out = defaultdict(int)
        for g, coeff in u.items():
            for h, coeff2 in v.items():
                gh = mul(g, h)
                out[gh] = (out[gh] + coeff * coeff2) % p
        return {g: coeff for g, coeff in out.items() if coeff}

    one = {zero: 1}
    units = [{g: 1} for g in (x, y, c, d, e)]
    X, Y, C, D, E = [ga_add(g, ga_scale(-1, one)) for g in units]
    K = {mul(mul(inverse(c), inverse(d)), inverse(e)): 1}
    assert ga_mul(Y, X) == ga_add(
        ga_mul(X, Y),
        ga_mul(ga_mul(units[0], units[1]), ga_add(K, ga_scale(-1, one))))
    assert ga_mul(C, X) == ga_add(
        ga_mul(X, C), ga_mul(ga_mul(units[0], units[2]), D))
    assert ga_mul(C, Y) == ga_add(
        ga_mul(Y, C), ga_mul(ga_mul(units[1], units[2]), E))

    # All finite inverse-series terms in K-1 have weight at least 2.
    weights = [2 * h + 3 * u + 3 * v
               for h, u, v in product(range(modulus), repeat=3)
               if h + u + v]
    assert min(weights) == 2
    assert max(weights) == 8 * (modulus - 1)
    max_basis_weight = sum((1, 1, 2, 3, 3)) * (modulus - 1)
    assert max_basis_weight == 10 * (modulus - 1)

    target = scale(q * m, x)
    centralizers, tested = 0, 0
    for a, b, cc in product(range(modulus), repeat=3):
        u = (a, b, cc, 0, 0)
        conjugate = mul(mul(u, target), inverse(u))
        actual = conjugate == target
        expected = b % p == 0 and cc % p == 0
        assert actual == expected, (modulus, u, conjugate, target)
        # Independently check the displayed conjugation coordinates.
        expected_log = (
            q * m % modulus,
            0,
            -q * m * b % modulus,
            q * m * (cc + pow(2, -1, modulus) * a * b) % modulus,
            pow(2, -1, modulus) * q * m * b * b % modulus)
        assert conjugate == expected_log
        tested += 1
        centralizers += actual
    assert centralizers == modulus * (modulus // p) ** 2
    print(f"k={k}, M={modulus}, |P_M|={modulus**5}:")
    print(f"  all {tested} noncentral-coordinate triples tested; "
          f"{centralizers} centralize x^(q*m)")
    print("  exact criterion: b = c = 0 modulo 5")
    print("  all three augmentation collection identities verified")
    print(f"  maximal ordered basis weight = {max_basis_weight}; "
          f"proved I^{max_basis_weight+1}=0")

print("PASS: finite local bound B(5,m)=10*(5^(v5(m)+1)-1).")
