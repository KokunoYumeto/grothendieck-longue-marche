#!/usr/bin/env python3
"""E.64 independent residue, polynomial and norm certificates; standard library."""
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
records = [
    json.loads(line) for line in
    (HERE / "e_complex_norm_criterion_gp.out").read_text().splitlines()
    if line.startswith("{")
]
assert records[-1]["status"] == "PASS"
primes = [r for r in records if r["type"] == "prime"]


class FiniteField:
    def __init__(self, p, polynomial):
        self.p = p
        self.modulus = tuple(int(Q(c)) % p for c in polynomial)
        assert self.modulus[-1] == 1
        self.degree = len(self.modulus) - 1
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)

    def value(self, polynomial):
        a = [int(Q(c).numerator * pow(Q(c).denominator, -1, self.p)) % self.p
             for c in polynomial]
        a += [0] * max(0, self.degree - len(a))
        for k in range(len(a) - 1, self.degree - 1, -1):
            q = a[k] % self.p
            for j in range(self.degree):
                a[k - self.degree + j] -= q * self.modulus[j]
        return tuple(x % self.p for x in a[:self.degree])

    def add(self, a, b):
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def scale(self, a, c):
        return tuple(x * c % self.p for x in a)

    def mul(self, a, b):
        q = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                q[i + j] += x * y
        return self.value(q)

    def power(self, a, n):
        r = self.one
        while n:
            if n & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            n >>= 1
        return r


finite_norms = 0
residue_certificates = []
for rec in primes:
    p, f = rec["p"], rec["f"]
    field = FiniteField(p, rec["residue_modulus"])
    assert field.degree == f
    b = field.value(rec["residue_polynomial"])
    z = field.value(rec["zeta_polynomial"])
    b3, b6 = field.power(b, 3), field.power(b, 6)
    assert field.add(field.add(b6, field.scale(b3, 17)),
                     field.scale(field.one, 289)) == field.zero
    assert field.scale(z, 17) == b3
    assert field.power(z, 3) == field.one and z != field.one
    symbol = field.power(b, (p ** f - 1) // 3)
    assert symbol == field.power(z, rec["symbol"])
    expected = [[1, 1]] * 3 if rec["symbol"] == 0 else [[1, 3]]
    assert rec["relative_degrees"] == expected
    det = 1
    for i, row in enumerate(rec["hnf"]):
        assert all(row[j] == 0 for j in range(i))
        det *= row[i]
    assert det == p ** f

    def cmul(a, c):
        out = [field.zero] * 5
        for i in range(3):
            for j in range(3):
                out[i + j] = field.add(out[i + j], field.mul(a[i], c[j]))
        for i in (4, 3):
            out[i - 3] = field.add(out[i - 3], field.mul(out[i], b))
        return out[:3]

    for aa, bb, cc in product((-1, 0, 1), repeat=3):
        if (aa, bb, cc) == (0, 0, 0):
            continue
        v = [field.scale(field.one, a) for a in (aa, bb, cc)]
        sv = [v[0], field.mul(v[1], z), field.mul(v[2], field.power(z, 2))]
        s2v = [v[0], field.mul(v[1], field.power(z, 2)), field.mul(v[2], z)]
        norm = cmul(cmul(v, sv), s2v)
        formula = field.add(field.add(field.scale(field.one, aa ** 3),
                                      field.scale(b, bb ** 3 - 3 * aa * bb * cc)),
                            field.scale(field.power(b, 2), cc ** 3))
        assert norm == [formula, field.zero, field.zero]
        finite_norms += 1
    residue_certificates.append({
        "p": p, "index": rec["index"], "f": f, "symbol": rec["symbol"],
        "relative_degrees": rec["relative_degrees"],
    })

# Exact Eisenstein polynomial identity in every one of six tested layers.
eisenstein = []
for d in range(1, 7):
    n = 3 ** d
    coeffs = [comb(2 * n, j) * (-1) ** (2 * n - j)
              + (17 * comb(n, j) * (-1) ** (n - j) if j <= n else 0)
              + (289 if j == 0 else 0)
              for j in range(2 * n + 1)]
    assert coeffs[-1] == 1 and coeffs[0] == 273
    assert coeffs[0] % 9 != 0 and all(c % 3 == 0 for c in coeffs[:-1])
    eisenstein.append({"d": d, "degree": 2 * n, "constant": coeffs[0]})

# Exact characteristic-zero automorphism and norm checks in L2.
modulus = [Q(0)] * 19
modulus[0], modulus[9], modulus[18] = Q(289), Q(17), Q(1)


def red(a):
    a = list(map(Q, a))
    a += [Q(0)] * max(0, 18 - len(a))
    for k in range(len(a) - 1, 17, -1):
        a[k - 18] -= 289 * a[k]
        a[k - 9] -= 17 * a[k]
    return tuple(a[:18])


def mul(a, b):
    out = [Q(0)] * 35
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return red(out)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, n):
    return tuple(x * n for x in a)


one = red([1])
theta = red([0, 1])
zeta = red([0] * 9 + [Q(1, 17)])
image = mul(zeta, theta)
powers = [one]
for i in range(1, 18):
    powers.append(mul(powers[-1], image))


def sigma(a):
    out = red([])
    for c, power in zip(a, powers):
        out = add(out, scale(power, c))
    return out


assert mul(mul(zeta, zeta), zeta) == one
exact_norms = 0
for aa, bb, cc in product((-2, -1, 0, 1, 2), repeat=3):
    if (aa, bb, cc) == (0, 0, 0):
        continue
    v = add(add(scale(one, aa), scale(theta, bb)),
            scale(mul(theta, theta), cc))
    sv, s2v = sigma(v), sigma(sigma(v))
    assert sigma(s2v) == v
    norm = mul(mul(v, sv), s2v)
    base_b = mul(mul(theta, theta), theta)
    formula = add(add(scale(one, aa ** 3),
                      scale(base_b, bb ** 3 - 3 * aa * bb * cc)),
                  scale(mul(base_b, base_b), cc ** 3))
    assert norm == formula
    # For the literal Hilbert90 ratio sigma(v)/v, this is the
    # cleared-denominator identity N(sigma(v)) = N(v).
    assert mul(mul(sv, s2v), v) == norm
    exact_norms += 1

ff17 = FiniteField(17, [1, 1, 1])
units17 = [v for v in product(range(17), repeat=2) if v != (0, 0)]
cubes17 = {ff17.power(v, 3) for v in units17}
assert len(cubes17) == 96
z17 = ff17.value([0, 1])
assert [ff17.power(ff17.power(z17, k), 96) for k in (2, 2, 1)] == [ff17.one] * 3
u_rec = next(r for r in records if r["type"] == "units")
assert u_rec["residue_exponents"] == [2, 2, 1]
assert u_rec["ambiguous_order"] == 9 * 3

out = {
    "status": "PASS",
    "prime_records": len(primes),
    "split_records": sum(r["symbol"] == 0 for r in primes),
    "inert_records": sum(r["symbol"] != 0 for r in primes),
    "independent_finite_norm_identities": finite_norms,
    "exact_characteristic_zero_norm_identities": exact_norms,
    "eisenstein_checks": eisenstein,
    "unit_residue_exponents": [2, 2, 1],
    "seventeen_cube_image_size": len(cubes17),
    "ambiguous_fixed_class_order": 27,
    "residue_certificates": residue_certificates,
}
(HERE / "e_complex_norm_criterion.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
