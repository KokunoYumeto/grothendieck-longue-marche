#!/usr/bin/env python3
"""E.65: independent exact checks of the retained GP and local-ring outputs."""
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import json
from sympy import Matrix, Poly, symbols
from e_pure_norm_local import DVR

HERE = Path(__file__).resolve().parent
records = [json.loads(s) for s in
           (HERE / "e_pure_norm_fields_gp.out").read_text().splitlines()
           if s.startswith("{")]
assert records[-1]["status"] == "PASS"
local = json.loads((HERE / "e_pure_norm_local.json").read_text())
assert local["status"] == "PASS"


class FiniteField:
    def __init__(self, p, polynomial):
        self.p = p
        self.modulus = tuple(int(Q(c)) % p for c in polynomial)
        assert self.modulus[-1] == 1
        self.degree = len(self.modulus) - 1
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)

    def value(self, polynomial):
        a = [Q(c).numerator * pow(Q(c).denominator, -1, self.p) % self.p
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
        out = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x * y
        return self.value(out)

    def power(self, a, n):
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out


class RationalField:
    def __init__(self, polynomial):
        self.modulus = tuple(map(Q, polynomial))
        assert self.modulus[-1] == 1
        self.degree = len(self.modulus) - 1
        self.zero = (Q(0),) * self.degree
        self.one = (Q(1),) + (Q(0),) * (self.degree - 1)

    def value(self, polynomial):
        out = list(map(Q, polynomial))
        out += [Q(0)] * max(0, self.degree - len(out))
        for k in range(len(out) - 1, self.degree - 1, -1):
            q = out[k]
            for j in range(self.degree):
                out[k - self.degree + j] -= q * self.modulus[j]
        return tuple(out[:self.degree])

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def mul(self, a, b):
        out = [Q(0)] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x * y
        return self.value(out)

    def power(self, a, n):
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out


embeddings = 0
for rec in records:
    if rec["type"] != "complexification":
        continue
    field = RationalField(rec["polynomial"])
    a, z = field.value(rec["alpha"]), field.value(rec["zeta"])
    assert field.power(a, 3 ** rec["d"]) == field.value([17])
    assert field.add(field.add(field.mul(z, z), z), field.one) == field.zero
    assert rec["prime3_degrees"] == [[2 * 3 ** (rec["d"] - 1), 1]] * 3
    embeddings += 2

primes = [r for r in records if r["type"] == "prime"]
finite_norms = 0
for rec in primes:
    p, f = rec["p"], rec["f"]
    field = FiniteField(p, rec["residue_modulus"])
    assert field.degree == f
    a = field.value(rec["residue_polynomial"])
    assert field.power(a, 3) == field.value([17])
    N = p ** f
    if N % 3 == 1:
        z = field.value(rec["zeta_polynomial"])
        assert field.power(z, 3) == field.one and z != field.one
        assert field.power(a, (N - 1) // 3) == field.power(z, rec["symbol"])
        expected = [[1, 1]] * 3 if rec["symbol"] == 0 else [[1, 3]]
    else:
        assert rec["symbol"] == -1
        cube_root = field.power(a, pow(3, -1, N - 1))
        assert field.power(cube_root, 3) == a
        expected = [[1, 1], [1, 2]]
    assert rec["relative_degrees"] == expected
    h = rec["hnf"]
    assert all(h[i][j] == 0 for i in range(3) for j in range(i))
    assert h[0][0] * h[1][1] * h[2][2] == N

    def det3(cols):
        out = field.zero
        for perm, sign in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                           ((2, 1, 0), -1), ((1, 0, 2), -1), ((0, 2, 1), -1)]:
            t = field.one
            for j, i in enumerate(perm):
                t = field.mul(t, cols[j][i])
            out = field.add(out, field.scale(t, sign))
        return out

    for u, v, w in product((-1, 0, 1), repeat=3):
        if (u, v, w) == (0, 0, 0):
            continue
        cols = [
            [field.value([u]), field.value([v]), field.value([w])],
            [field.scale(a, w), field.value([u]), field.value([v])],
            [field.scale(a, v), field.scale(a, w), field.value([u])],
        ]
        expected_norm = field.add(
            field.add(field.value([u ** 3]), field.scale(a, v ** 3 - 3 * u * v * w)),
            field.scale(field.mul(a, a), w ** 3))
        assert det3(cols) == expected_norm
        finite_norms += 1

a = symbols("a")
unit_norms = []
for rec in records:
    if rec["type"] != "unit_norm":
        continue
    coeffs = list(map(Q, rec["element"]))
    u = [sum(coeffs[j] * a ** (j // 3) for j in range(i, len(coeffs), 3))
         for i in range(3)]
    matrix = Matrix([[u[0], a * u[2], a * u[1]],
                     [u[1], u[0], a * u[2]],
                     [u[2], u[1], u[0]]])
    actual = Poly(matrix.det(), a).rem(Poly(a ** 3 - 17, a))
    expected = Poly(sum(Q(c) * a ** i for i, c in enumerate(rec["norm"])), a)
    assert (actual - expected).is_zero
    sign, exponent = rec["coordinates"][1], rec["coordinates"][0]
    stated = Poly((-1) ** sign * (7 * a - 18) ** exponent, a).rem(Poly(a ** 3 - 17, a))
    assert (actual - stated).is_zero
    unit_norms.append({"index": rec["index"], "epsilon_exponent": exponent, "sign": sign})
assert [r["epsilon_exponent"] for r in unit_norms] == [0, 3, 0, 0]

eisenstein = []
for d in range(1, 7):
    m, rho = 3 ** (d - 1), 23
    pure = [comb(m, j) * (-1) ** (m - j) - (rho if j == 0 else 0)
            for j in range(m + 1)]
    wild = [comb(2 * m, j) * (-1) ** (2 * m - j)
            + (rho * comb(m, j) * (-1) ** (m - j) if j <= m else 0)
            + (rho * rho if j == 0 else 0) for j in range(2 * m + 1)]
    for poly in (pure, wild):
        assert poly[-1] == 1 and all(x % 3 == 0 for x in poly[:-1])
        assert poly[0] % 9 == 3
    eisenstein.append({"d": d, "degrees": [m, 2 * m],
                       "constant_terms_mod9": [pure[0] % 9, wild[0] % 9]})
assert (23 ** 3 - 17) % (3 ** 5) == 0
assert (23 ** 3 - 17) % (3 ** 6) != 0

r = DVR(1)
w = local["records"][0]["norm_character_weights"]
epsilon = r.add(r.scale(r.x, 7), r.scale(r.one, -25))
coords = r.coords(epsilon)
assert coords == [2, 0, 2, 2]
symbol = sum(c * t for c, t in zip(coords, w)) % 3
assert symbol == 2
for k in range(9):
    assert sum(c * t for c, t in zip(r.coords(r.power(epsilon, k)), w)) % 3 == 2 * k % 3

out = {
    "status": "PASS",
    "certified_pure_fields": 2,
    "exact_complexification_embedding_identities": embeddings,
    "actual_prime_contractions": len(primes),
    "split_records": sum(r["symbol"] == 0 for r in primes),
    "inert_records": sum(r["symbol"] > 0 for r in primes),
    "linear_quadratic_records": sum(r["symbol"] == -1 for r in primes),
    "finite_norm_determinants": finite_norms,
    "exact_unit_norm_determinants": unit_norms,
    "unit_norm_index": 3,
    "eisenstein_layers": eisenstein,
    "wild_local_layers": [r["d"] for r in local["records"]],
    "wild_local_norm_dimensions": [r["norm_cokernel_dimension"] for r in local["records"]],
    "wild_additivity_checks": sum(r["additivity_checks"] for r in local["records"]),
    "fundamental_unit_coordinates": coords,
    "fundamental_unit_wild_symbol": symbol,
    "fundamental_unit_power_checks": 9,
}
(HERE / "e_pure_norm_verify.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
