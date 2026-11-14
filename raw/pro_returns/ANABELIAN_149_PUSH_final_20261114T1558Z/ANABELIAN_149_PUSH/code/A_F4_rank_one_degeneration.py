#!/usr/bin/env python3
"""Independent fixed rank-one norm certificate audit.

No imported search, C, Jacobian, jet, or earlier finite-field arithmetic.
Each norm equality is checked coefficient by coefficient over a freshly
constructed binary field. Only positive annihilator claims are certified.
"""
from pathlib import Path
from math import gcd, comb
import hashlib
import json

ROOT = Path(__file__).resolve().parent


class Binary:
    def __init__(self, e, modulus, generator):
        self.e = e
        self.q = 1 << e
        self.modulus = modulus
        a, seen = 1, set()
        for _ in range(self.q - 1):
            assert a and a not in seen
            seen.add(a)
            a = self.mul(a, generator)
        assert a == 1 and seen == set(range(1, self.q))

    def mul(self, a, b):
        c = 0
        while b:
            if b & 1:
                c ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.modulus
        return c

    def power(self, a, n):
        c = 1
        while n:
            if n & 1:
                c = self.mul(c, a)
            a = self.mul(a, a)
            n >>= 1
        return c

    def inv(self, a):
        assert a
        return self.power(a, self.q - 2)

    @staticmethod
    def trim(a):
        a = list(a)
        while a and a[-1] == 0:
            a.pop()
        return a

    def add(self, *polys):
        out = [0] * max(map(len, polys), default=0)
        for a in polys:
            for j, x in enumerate(a):
                out[j] ^= x
        return self.trim(out)

    def product(self, a, b):
        if not a or not b:
            return []
        out = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] ^= self.mul(x, y)
        return self.trim(out)

    def eval(self, a, x):
        c = 0
        for v in reversed(a):
            c = self.mul(c, x) ^ v
        return c


def main():
    path = ROOT / "A_F4_rank_one_witnesses.json"
    raw = path.read_bytes()
    data = json.loads(raw)
    rows, covered = [], set()
    for r in data["witnesses"]:
        F = Binary(r["field_degree_over_F2"], r["field_modulus"],
                   r["field_generator"])
        alpha = r["alpha"]
        assert F.mul(alpha, alpha) ^ alpha == 1
        embed = [0, 1, alpha, alpha ^ 1]
        A, B = r["A"], r["B"]
        a0, b0 = r["F4_coefficients"]
        assert A == embed[a0] and B == embed[b0] and A
        t, y = r["point"]
        assert t
        rhs = F.mul(A, F.power(t, 3)) ^ F.mul(B, t) ^ F.inv(t)
        assert F.mul(y, y) ^ y == rhs

        n = r["exact_order"]  # Used only as the supplied annihilator.
        assert n > 1 and n % 2
        d = (n - 1) // 2
        a, b = r["numerator_A"], r["numerator_B"]
        c = r["norm_scalar"]
        assert r["denominator_power"] == d
        assert len(a) - 1 == d and len(b) - 1 <= d - 2
        assert b[0] and F.eval(b, t)
        assert F.eval(a, t) ^ F.mul(F.eval(b, t), y) == 0
        assert c == F.mul(a[-1], a[-1]) and c

        # N(a+b*y) = a^2+a*b+b^2*(A*x^3+B*x+1/x).
        left = F.add(
            F.product([0, 1], F.add(F.product(a, a), F.product(a, b))),
            F.product(F.product(b, b), [1, 0, B, 0, A]))
        right = [F.mul(c, F.power(t, n - j)) if comb(n, j) % 2 else 0
                 for j in range(n + 1)]
        assert left == right

        units = {i for i in range(n) if gcd(i, n) == 1}
        powers = []
        j = 1
        while j not in powers:
            powers.append(j)
            j = 2 * j % n
        assert j == 1
        signs = set(powers) | {-i % n for i in powers}
        assert signs == units
        # No exact-order assertion is needed: every divisor d0>1
        # of n inherits the generated-unit property.
        divisors = [d0 for d0 in range(2, n + 1) if n % d0 == 0]
        for d0 in divisors:
            assert {i % d0 for i in signs} == {
                i for i in range(d0) if gcd(i, d0) == 1}

        # The two coefficientwise-square conjugates exhaust each orbit.
        sq = [0, 1, 3, 2]
        orbit = {(a0, b0), (sq[a0], sq[b0])}
        assert not covered.intersection(orbit)
        covered.update(orbit)
        rows.append({
            "F4_coefficients": [a0, b0],
            "field_size": F.q,
            "annihilator": n,
            "norm_degree": len(left) - 1,
            "coefficient_identity": True,
            "correct_chosen_point_and_nonzero_conjugate": True,
            "pole_order_at_W0": 2 * d + 1,
            "no_pole_at_infinity": True,
            "doubling_period": len(powers),
            "doubling_with_sign_is_full_unit_group": True,
            "all_possible_nontrivial_exact_orders": divisors,
            "Frobenius_two_orbit_size": len(orbit)
        })

    assert covered == {(a, b) for a in [1, 2, 3] for b in range(4)}
    out = {
        "status": "PASS",
        "fixed_witness_sha256": hashlib.sha256(raw).hexdigest(),
        "independence": "Fresh binary polynomial field and coefficient convolution; no imports from discovery, Jacobian, jets, or previous checkers.",
        "verified_norms": len(rows),
        "covered_F4_parameter_pairs": sorted(map(list, covered)),
        "covered_geometric_rank_one_classes": len(covered),
        "rows": rows,
        "scope": "Positive annihilator/divisor certificates and complete parameter coverage. No exact39 claim or negative search is used."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

