#!/usr/bin/env python3
"""Exact relative Lie, Fox and weighted Magnus certificates for E.77.

No arithmetic source relation is guessed here.  The theorem constructs
its actual source change of basis.  This program checks the integral
graded maps, all small correction systems, and actual group variations.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from math import comb
import json
import numpy as np
import sympy as sp

OUT = Path(__file__).resolve().parent
MAX_DEGREE = 6


def is_lyndon(w):
    return bool(w) and all(w < w[i:] + w[:i] for i in range(1, len(w)))


LY = {
    n: [w for w in product(range(4), repeat=n) if is_lyndon(w)]
    for n in range(1, MAX_DEGREE + 1)
}


def add(a, b, scalar=1):
    out = dict(a)
    for w, x in b.items():
        out[w] = out.get(w, 0) + scalar * x
        if not out[w]:
            del out[w]
    return out


def mul(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            w = u + v
            out[w] = out.get(w, 0) + x * y
    return {w: x for w, x in out.items() if x}


def bracket(a, b):
    return add(mul(a, b), mul(b, a), -1)


@lru_cache(None)
def split(w):
    assert len(w) > 1 and is_lyndon(w)
    i = next(i for i in range(1, len(w)) if is_lyndon(w[i:]))
    assert is_lyndon(w[:i])
    return w[:i], w[i:]


@lru_cache(None)
def hall(w):
    if len(w) == 1:
        return {w: 1}
    u, v = split(w)
    return bracket(hall(u), hall(v))


def lie_coords(poly):
    if not poly:
        return {}
    n = len(next(iter(poly)))
    assert all(len(w) == n for w in poly)
    rem = dict(poly)
    ans = {}
    for w in LY[n]:
        x = rem.get(w, 0)
        if x:
            ans[w] = x
            rem = add(rem, hall(w), -x)
    assert not rem, rem
    return ans


def vertical_count(w):
    return sum(x >= 2 for x in w)


def weighted_basis(n, minimum_vertical):
    return [
        (n - d, w)
        for d in range(1, n + 1)
        for w in LY[d]
        if vertical_count(w) >= minimum_vertical
    ]


def swap_poly(poly):
    return {tuple(x ^ 1 for x in w): a for w, a in poly.items()}


def weighted_coords(terms, basis):
    index = {x: i for i, x in enumerate(basis)}
    out = np.zeros(len(basis), dtype=np.int64)
    for power, poly in terms:
        for w, a in lie_coords(poly).items():
            out[index[power, w]] += a
    return out


def inverse_mod3(a):
    n = len(a)
    m = np.concatenate((np.asarray(a, dtype=np.int64) % 3,
                        np.eye(n, dtype=np.int64)), axis=1)
    for j in range(n):
        k = next(k for k in range(j, n) if m[k, j])
        m[[j, k]] = m[[k, j]]
        m[j] = m[j] * int(m[j, j]) % 3
        factors = m[:, j].copy()
        factors[j] = 0
        m = (m - factors[:, None] * m[j][None, :]) % 3
    assert np.array_equal(m[:, :n], np.eye(n, dtype=np.int64))
    return m[:, n:]


def pivots(a):
    m = np.asarray(a, dtype=np.int64).copy() % 3
    rows, cols = m.shape
    selected = []
    k = 0
    for j in range(cols):
        hits = np.flatnonzero(m[k:, j])
        if not len(hits):
            continue
        i = k + int(hits[0])
        m[[k, i]] = m[[i, k]]
        m[k] = m[k] * int(m[k, j]) % 3
        if k + 1 < rows:
            f = m[k+1:, j].copy()
            m[k+1:] = (m[k+1:] - f[:, None] * m[k][None, :]) % 3
        selected.append(j)
        k += 1
        if k == rows:
            break
    return selected


def sparse(a):
    a = np.asarray(a)
    return {
        "shape": list(a.shape),
        "entries": [
            [int(i), int(j), int(a[i, j])]
            for i, j in zip(*np.nonzero(a))
        ],
    }


# Integral one-vertical Fox maps.  A horizontal associative word acts
# by left concatenation, so the maps are computed in the actual
# semidirect Lie algebra of the proof.
@lru_cache(None)
def fox_hall(w):
    if len(w) == 1:
        return {((), w[0] - 2): 1} if w[0] >= 2 else {}
    u, v = split(w)
    fu, fv = fox_hall(u), fox_hall(v)
    pu = hall(u) if not vertical_count(u) else {}
    pv = hall(v) if not vertical_count(v) else {}
    out = {}
    for a, x in pu.items():
        for (b, i), y in fv.items():
            key = (a + b, i)
            out[key] = out.get(key, 0) + x*y
    for a, x in pv.items():
        for (b, i), y in fu.items():
            key = (a + b, i)
            out[key] = out.get(key, 0) - x*y
    return {x: y for x, y in out.items() if y}


fox_records = []
fox_zero_checks = 0
for n in range(1, MAX_DEGREE + 1):
    words = [w for w in LY[n] if vertical_count(w) == 1]
    target = [(w, i) for w in product(range(2), repeat=n-1) for i in range(2)]
    ix = {w: i for i, w in enumerate(target)}
    m = sp.zeros(len(target), len(words))
    for j, w in enumerate(words):
        for key, value in fox_hall(w).items():
            m[ix[key], j] = value
    assert m.rows == m.cols == 2**n
    inv = m.inv()
    assert all(x.q == 1 for x in inv)
    assert m*inv == sp.eye(m.rows)
    for w in LY[n]:
        if vertical_count(w) >= 2:
            assert not fox_hall(w)
            fox_zero_checks += 1
    fox_records.append({
        "ordinary_degree": n,
        "rank": m.rows,
        "matrix": sparse(np.asarray(m.tolist(), dtype=np.int64)),
        "integral_inverse": sparse(np.asarray(inv.tolist(), dtype=np.int64)),
    })


graded = []
for n in range(2, MAX_DEGREE + 1):
    target = weighted_basis(n, 2)
    dom_h = weighted_basis(n-1, 1)
    dom_v = weighted_basis(n-1, 2)
    C = np.zeros((len(target), len(target)), dtype=np.int64)
    for j, (p, w) in enumerate(target):
        C[:, j] = weighted_coords([(p, swap_poly(hall(w)))], target)
    assert np.array_equal(C @ C, np.eye(len(target), dtype=np.int64))

    columns = []
    labels = []
    for p, w in dom_h:
        x = hall(w)
        val = bracket(x, {(2,): 1})
        cval = swap_poly(val)
        columns.append(weighted_coords([(p, add(val, cval, -1))], target))
        labels.append(["horizontal", p, list(w)])
    for p, w in dom_v:
        y = hall(w)
        val = bracket({(0,): 1}, y)
        terms = [(p, add(val, swap_poly(val), -1)),
                 (p+1, add(y, swap_poly(y), -1))]
        terms[1] = (terms[1][0], {k: -2*v for k, v in terms[1][1].items()})
        columns.append(weighted_coords(terms, target))
        labels.append(["vertical", p, list(w)])
    M = np.stack(columns, axis=1) % 3
    assert not np.any((C @ M + M) % 3)
    anti = (np.eye(len(target), dtype=np.int64) - C) % 3
    cols = pivots(M)
    anti_cols = pivots(anti)
    assert len(cols) == len(anti_cols)
    selected = M[:, cols]
    rows = pivots(selected.T)
    assert len(rows) == len(cols)
    inv = inverse_mod3(selected[rows, :])
    coordinates = inv @ anti[rows, :] % 3
    assert not np.any((selected @ coordinates - anti) % 3)
    assert not np.any((inv @ selected[rows, :] -
                       np.eye(len(rows), dtype=np.int64)) % 3)
    graded.append({
        "weight": n,
        "relative_derived_rank": len(target),
        "anti_invariant_rank": len(cols),
        "paired_correction_domain_rank": len(labels),
        "target_basis": [[p, list(w)] for p, w in target],
        "correction_labels": labels,
        "involution": sparse(C),
        "correction_matrix_mod3": sparse(M),
        "selected_columns": cols,
        "selected_rows": rows,
        "unit_minor_inverse_mod3": sparse(inv),
        "all_anti_generator_coordinates_mod3": sparse(coordinates),
    })
    print("graded", n, "target", len(target), "anti", len(cols),
          "paired domain", len(labels), "PASS", flush=True)


class WeightedMagnus:
    """Associative group calculation modulo weighted degree > n."""
    def __init__(self, n):
        self.n = n
        self.mod = [3**(n+1-d) for d in range(n+1)]
        self.one = {(): 1}
        self.gens = [{(): 1, (i,): 1} for i in range(4)]
        self.cache = {}

    def clean(self, a):
        return {w: x % self.mod[len(w)] for w, x in a.items()
                if len(w) <= self.n and x % self.mod[len(w)]}

    def add(self, a, b, scalar=1):
        return self.clean(add(a, b, scalar))

    def mul(self, a, b):
        out = {}
        for u, x in a.items():
            for v, y in b.items():
                if len(u)+len(v) <= self.n:
                    w = u+v
                    out[w] = out.get(w, 0) + x*y
        return self.clean(out)

    def inv(self, a):
        assert a.get((), 0) == 1
        x = self.add(a, self.one, -1)
        out = self.one
        term = self.one
        for k in range(1, self.n+1):
            term = self.mul(term, x)
            out = self.add(out, term, (-1)**k)
        assert self.mul(a, out) == self.one
        return out

    def power(self, a, k):
        if k < 0:
            return self.power(self.inv(a), -k)
        out = self.one
        while k:
            if k & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            k //= 2
        return out

    def comm(self, a, b):
        return self.mul(self.mul(self.mul(a, b), self.inv(a)), self.inv(b))

    def hall(self, w):
        if w not in self.cache:
            if len(w) == 1:
                self.cache[w] = self.gens[w[0]]
            else:
                u, v = split(w)
                self.cache[w] = self.comm(self.hall(u), self.hall(v))
        return self.cache[w]

    def c(self, a):
        return {tuple(i ^ 1 for i in w): x for w, x in a.items()}

    def f(self, t, r):
        return self.mul(self.mul(self.mul(t, r), self.inv(t)),
                        self.power(r, -7))

    def rho(self, generators):
        t, tp, r, rp = generators
        return self.mul(self.f(t, r), self.inv(self.f(tp, rp)))

    def leading(self, a):
        rem = self.add(a, self.one, -1)
        out = {}
        for w, x in rem.items():
            k = self.n-len(w)
            assert x % 3**k == 0, (self.n, w, x)
            z = x//3**k % 3
            if z:
                out[k, w] = z
        return out


def leading_expected(terms):
    out = {}
    for p, poly in terms:
        for w, x in poly.items():
            key = p, w
            out[key] = (out.get(key, 0) + x) % 3
    return {k: x for k, x in out.items() if x}


magnus_records = []
for n in range(2, MAX_DEGREE + 1):
    alg = WeightedMagnus(n)
    original = alg.rho(alg.gens)
    # Both source relators are actually c-inverted, before truncation
    # as words and here in every retained quotient.
    assert alg.c(original) == alg.inv(original)
    count_h = count_v = 0
    for kind, basis in [("horizontal", weighted_basis(n-1, 1)),
                        ("vertical", weighted_basis(n-1, 2))]:
        for p, w in basis:
            delta = alg.power(alg.hall(w), 3**p)
            new = list(alg.gens)
            i = 0 if kind == "horizontal" else 2
            new[i] = alg.mul(new[i], delta)
            new[i+1] = alg.mul(new[i+1], alg.c(delta))
            rho = alg.rho(new)
            assert alg.c(rho) == alg.inv(rho)
            change = alg.mul(rho, alg.inv(original))
            if kind == "horizontal":
                h = bracket(hall(w), {(2,): 1})
                expected = leading_expected([(p, add(h, swap_poly(h), -1))])
                count_h += 1
            else:
                h = bracket({(0,): 1}, hall(w))
                yp = add(hall(w), swap_poly(hall(w)), -1)
                expected = leading_expected([
                    (p, add(h, swap_poly(h), -1)),
                    (p+1, {k: -2*v for k, v in yp.items()})
                ])
                count_v += 1
            assert alg.leading(change) == expected, (n, kind, p, w)
    magnus_records.append({
        "weight": n,
        "horizontal_actual_word_variations": count_h,
        "vertical_actual_word_variations": count_v,
        "all_paired_relators_exactly_c_inverted": True,
        "all_variations_match_full_weighted_Magnus": True,
    })
    print("Magnus", n, count_h, count_v, "PASS", flush=True)

# The initial shear is checked for every residue.
alg = WeightedMagnus(2)
base = alg.rho(alg.gens)
for a in range(3):
    new = list(alg.gens)
    new[0] = alg.mul(new[0], alg.power(new[3], a))
    new[1] = alg.mul(new[1], alg.power(new[2], a))
    actual = alg.leading(alg.mul(alg.rho(new), alg.inv(base)))
    expected = leading_expected([(0, {
        w: -2*a*x for w, x in bracket({(2,): 1}, {(3,): 1}).items()
    })])
    assert actual == expected

# Exact nonlinear relation in finite class-two targets.  Each target is
# a BCH Heisenberg group; the actual semidirect word is evaluated with
# the two specified, c-conjugate automorphisms.
def heis_mul(a, b, modulus):
    inv2 = pow(2, -1, modulus)
    return ((a[0]+b[0]) % modulus,
            (a[1]+b[1]) % modulus,
            (a[2]+b[2]+inv2*(a[0]*b[1]-a[1]*b[0])) % modulus)


def heis_inv(a, modulus):
    return tuple(-x % modulus for x in a)


def heis_power(a, k, modulus):
    return tuple(k*x % modulus for x in a)


def heis_J(a, modulus):
    return a[1], a[0], -a[2] % modulus


def heis_T(a, modulus):
    return 7*a[0] % modulus, 49*a[1] % modulus, 343*a[2] % modulus


def heis_f(u, a, modulus):
    return heis_mul(
        heis_mul(heis_mul(u, heis_T(a, modulus), modulus),
                 heis_inv(u, modulus), modulus),
        heis_power(a, -7, modulus), modulus)


nonlinear_checks = 0
central_checks = 0
for modulus in (9, 27, 81):
    for i in range(120):
        u = ((11*i+1) % modulus, (7*i*i+3) % modulus, (5*i+2) % modulus)
        a = ((2*i+4) % modulus, (i*i+5) % modulus, (13*i+1) % modulus)
        v = heis_f(u, a, modulus)
        # c-conjugate t' action is J T J, including the central sign.
        up, ap = heis_J(u, modulus), heis_J(a, modulus)
        Tap = heis_J(heis_T(heis_J(ap, modulus), modulus), modulus)
        vp = heis_mul(heis_mul(heis_mul(up, Tap, modulus),
                               heis_inv(up, modulus), modulus),
                      heis_power(ap, -7, modulus), modulus)
        assert vp == heis_J(v, modulus)
        defect = heis_mul(v, heis_inv(vp, modulus), modulus)
        assert heis_J(defect, modulus) == heis_inv(defect, modulus)
        nonlinear_checks += 1
        b = (0, 0, (17*i+2) % modulus)
        d = (0, 0, (19*i+1) % modulus)
        changed = heis_f(heis_mul(u, b, modulus),
                         heis_mul(a, d, modulus), modulus)
        delta = (0, 0, (343-7)*d[2] % modulus)
        assert changed == heis_mul(v, delta, modulus)
        changed_defect = heis_mul(changed,
                                 heis_inv(heis_J(changed, modulus), modulus),
                                 modulus)
        expected_delta = (0, 0, 2*(343-7)*d[2] % modulus)
        assert changed_defect == heis_mul(defect, expected_delta, modulus)
        central_checks += 1

answer = {
    "status": "PASS",
    "maximum_weight": MAX_DEGREE,
    "commutator": "a b a^-1 b^-1",
    "pi": "leading term of cubing, weight one",
    "relative_fox_integral_certificates": fox_records,
    "fox_zero_checks_on_two_or_more_vertical_letters": fox_zero_checks,
    "paired_relative_correction_certificates": graded,
    "actual_weighted_Magnus_variations": magnus_records,
    "initial_shear_residues_checked": 3,
    "nonlinear_semidirect_relation_checks": nonlinear_checks,
    "central_defect_change_checks": central_checks,
    "scope": "The actual local source and convergent over-P change of basis are proved in E77. These certificates verify the exact integral Fox maps, all paired graded systems through weight six, and every displayed finite group-word variation.",
}
(OUT / "a_wild_nonlinear.json").write_text(
    json.dumps(answer, indent=2) + "\n")
print("ALL PASS", flush=True)
