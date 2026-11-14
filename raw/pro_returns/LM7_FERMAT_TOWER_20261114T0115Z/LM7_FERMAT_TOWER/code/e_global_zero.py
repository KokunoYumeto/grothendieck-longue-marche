#!/usr/bin/env python3
"""Exact finite checks for E.47; no numerical class-number inference.

The all-level class-number and unit-index arguments are proved in the text.
This program checks the actual cyclotomic elements, norms, positional maps,
and finite free-group cohomology presentations used by those arguments.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def v3(n: int) -> int:
    n = abs(n)
    assert n
    r = 0
    while n % 3 == 0:
        n //= 3
        r += 1
    return r


class Cyclotomic3:
    """Z[z]/(z^(2d)+z^d+1), d=3^(n-1), represented integrally."""

    def __init__(self, n: int):
        self.n = n
        self.m = 3**n
        self.d = 3 ** (n - 1)
        self.degree = 2 * self.d
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def reduce(self, coeffs):
        a = list(coeffs) + [0] * max(0, self.degree - len(coeffs))
        for k in range(len(a) - 1, self.degree - 1, -1):
            c = a[k]
            if c:
                a[k - self.d] -= c
                a[k - 2 * self.d] -= c
        return tuple(a[: self.degree])

    def mul(self, a, b):
        ans = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        ans[i + j] += x * y
        return self.reduce(ans)

    def z(self, exponent: int):
        exponent %= self.m
        a = [0] * (exponent + 1)
        a[exponent] = 1
        return self.reduce(a)

    def product(self, values):
        out = self.one
        for value in values:
            out = self.mul(out, value)
        return out

    def epsilon(self, a: int = 1):
        return self.mul(self.sub(self.one, self.z(a)),
                        self.sub(self.one, self.z(-a)))

    def conjugate(self, value):
        out = self.zero
        for i, c in enumerate(value):
            if c:
                out = self.add(out, tuple(c * x for x in self.z(-i)))
        return out

    def eval_poly(self, poly, value):
        out = self.zero
        for coeff in poly.all_coeffs():
            out = self.mul(out, value)
            out = self.add(out, (int(coeff),) + (0,) * (self.degree - 1))
        return out


def check_cyclotomic_elements():
    x = sp.symbols("x")
    p = sp.Poly(x - 3, x, domain=sp.ZZ)
    data = []
    total_ratio_checks = 0
    for n in range(1, 5):
        ring = Cyclotomic3(n)
        reps = [a for a in range(1, (ring.m + 1) // 2) if a % 3]
        assert len(reps) == 3 ** (n - 1)
        assert ring.eval_poly(p, ring.epsilon()) == ring.zero
        assert int(p.TC()) == -3
        assert p.degree() == len(reps)
        assert ring.product(ring.epsilon(a) for a in reps) == (
            3,
        ) + (0,) * (ring.degree - 1)
        for a in reps:
            # eta_a = z^((1-a)/2) * (1-z^a)/(1-z), with 1/2 mod 3^n.
            half_exp = ((1 - a) * pow(2, -1, ring.m)) % ring.m
            quotient = ring.zero
            for j in range(a):
                quotient = ring.add(quotient, ring.z(j))
            eta = ring.mul(ring.z(half_exp), quotient)
            assert ring.conjugate(eta) == eta
            # Clear the unit denominator: epsilon_a = epsilon_1 * eta_a^2.
            assert ring.mul(ring.epsilon(), ring.mul(eta, eta)) == ring.epsilon(a)
            total_ratio_checks += 1
        data.append({
            "n": n,
            "conductor": ring.m,
            "real_degree": len(reps),
            "epsilon_minimal_polynomial": str(p.as_expr()),
            "epsilon_absolute_norm": 3,
            "ratio_checks": len(reps),
        })
        p = sp.Poly(p.as_expr().subs(x, x * (3 - x) ** 2), x, domain=sp.ZZ)
    print(f"Cyclotomic elements: {total_ratio_checks} exact real-unit identities; n=1,...,4 PASS")
    return data


def check_norms():
    data = []
    for n in range(1, 4):
        top = Cyclotomic3(n + 1)
        kernel = [1 + j * (3**n) for j in range(3)]
        reps = [a for a in range(1, 3**n) if a % 3]
        for a in reps:
            assert top.product(top.z(a * k) for k in kernel) == top.z(3 * a)
            assert top.product(top.sub(top.one, top.z(a * k)) for k in kernel) == top.sub(top.one, top.z(3 * a))
            assert top.product(top.epsilon(a * k) for k in kernel) == top.epsilon(3 * a)
        # Label real conjugates by powers of 7.  The norm sends each top basis
        # element to its image under reduction of the label, with coefficient 1.
        size_low = 3 ** (n - 1)
        size_top = 3**n
        low_labels = [pow(7, i, 3**n) for i in range(size_low)]
        top_labels = [pow(7, i, 3 ** (n + 1)) for i in range(size_top)]
        assert len(set(low_labels)) == size_low
        assert len(set(top_labels)) == size_top
        transition = [i % size_low for i in range(size_top)]
        for i, a in enumerate(top_labels):
            assert a % (3**n) == low_labels[transition[i]]
        data.append({
            "n": n,
            "element_checks": len(reps),
            "root_norm_exponent_reduction_mod": 3**n,
            "real_group_ring_transition_columns": transition,
        })
    print("Root, cyclotomic-uniformizer, and real-unit norms: all conjugates through conductor 81 PASS")
    return data


def check_centered_annuli():
    data = []
    for k in range(1, 6):
        m = 3**k
        columns = []
        for j in range(k):
            u_mod = 3 ** (k - j)
            columns.extend((j, u, (3**j) * u) for u in range(u_mod) if u % 3)
        positions = [c[2] for c in columns]
        assert sorted(positions) == list(range(1, m))
        # Every column is delta_x-delta_0, a permuted standard augmentation basis.
        for multiplier in [2, 4, 7, 19]:
            assert sorted((multiplier * p) % m for p in positions) == list(range(1, m))
            for j, u, pos in columns:
                assert (multiplier * pos) % m == 3**j * ((multiplier * u) % (3 ** (k - j)))
        # All later centered terms vanish in this positional quotient.
        for j in range(k, k + 4):
            assert pow(3, j, m) == 0
        data.append({"positional_exponent": k, "augmentation_rank": m - 1,
                     "annular_column_positions": positions, "tail_vanishes_from_j": k})
    print("Centered annular decomposition: five exact finite positional isomorphisms and action checks PASS")
    return data


def check_free_group_presentation():
    data = []
    previous = None
    for n in range(1, 6):
        size = 3 ** (n - 1)
        modulus = 3**n
        cyclic_relation = 7**size - 1
        assert v3(cyclic_relation) == n
        weights = [pow(7, -i, modulus) for i in range(size)]
        # Column i of 7*S-1 is 7*delta_(i+1)-delta_i.  Evaluation at 1/7
        # kills it, including the wraparound column.
        assert all((7 * weights[(i + 1) % size] - weights[i]) % modulus == 0
                   for i in range(size))
        # Unit pivots successively eliminate delta_1,...,delta_(size-1),
        # leaving exactly (7^size-1)*delta_0.  The resulting cyclic factor
        # has order 3^n, exactly the root-of-unity factor at K_n.
        if previous is not None:
            low_size, low_modulus, low_weights = previous
            for i in range(size):
                assert weights[i] % low_modulus == low_weights[i % low_size]
        data.append({
            "n": n, "group_ring_rank": size,
            "diagonal_coboundary_cokernel_free_rank": size,
            "torsion_order": modulus,
            "evaluation_weights_mod_3n": weights,
            "integral_cyclic_relation": str(cyclic_relation),
        })
        previous = (size, modulus, weights)
    print("Free-P diagonal coboundaries: five exact finite cyclic factors and all norm transitions PASS")
    return data


def main():
    result = {
        "statement": "E.47",
        "status": "PASS",
        "scope": "Exact cyclotomic identities and transition maps; all-level class and unit indices are proved in the manuscript.",
        "cyclotomic_elements": check_cyclotomic_elements(),
        "norms": check_norms(),
        "centered_annuli": check_centered_annuli(),
        "free_group_presentation": check_free_group_presentation(),
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print("E.47 exact finite checks PASS")
    print(f"Wrote {out.name}")


if __name__ == "__main__":
    main()
