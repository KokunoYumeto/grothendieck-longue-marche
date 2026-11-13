#!/usr/bin/env python3
"""Exact checks of formulas in Parts 1(e), 2 and 3.

Only the Python standard library is used. These finite computations detect
matrix, sign and substitution mistakes; they are not proofs of arbitrary
asphericity, the surface classification, or any factorization conjecture.
Run directly; JSON is written beside this script and printed to stdout.
"""
from fractions import Fraction
from math import gcd
from pathlib import Path
import json


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mv(a, v):
    return tuple(sum(row[j] * v[j] for j in range(len(v))) for row in a)


def determinant(a):
    a = [list(map(Fraction, row)) for row in a]
    ans = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            ans = -ans
        value = a[j][j]
        ans *= value
        for k in range(j, len(a)):
            a[j][k] /= value
        for i in range(j + 1, len(a)):
            value = a[i][j]
            for k in range(j, len(a)):
                a[i][k] -= value * a[j][k]
    return ans


def inv2(a):
    d = determinant(a)
    assert d in (1, -1)
    return [[int(a[1][1] / d), int(-a[0][1] / d)],
            [int(-a[1][0] / d), int(a[0][0] / d)]]


def mpow(a, n):
    if n < 0:
        return mpow(inv2(a), -n)
    out = ident(len(a))
    while n:
        if n & 1:
            out = mm(out, a)
        a = mm(a, a)
        n //= 2
    return out


def padd(a, b):
    out = a.copy()
    for exps, c in b.items():
        out[exps] = out.get(exps, 0) + c
    return {e: c for e, c in out.items() if c}


def pmul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            key = tuple(x + y for x, y in zip(e, f))
            out[key] = out.get(key, 0) + c * d
    return {e: c for e, c in out.items() if c}


def ppow(a, n):
    out = {(0, 0): 1}
    for _ in range(n):
        out = pmul(out, a)
    return out


def cusp_pullback(x, y):
    return padd(ppow(y, 2), {e: -c for e, c in ppow(x, 3).items()})


def terms(p):
    return [{"exponents": e, "coefficient": p[e]} for e in sorted(p)]


def cross(v, w):
    return v[0] * w[1] - v[1] * w[0]


def self_intersections(rays):
    assert all(cross(rays[i], rays[(i + 1) % len(rays)]) == 1
               for i in range(len(rays)))
    return [-cross(rays[i - 1], rays[(i + 1) % len(rays)])
            for i in range(len(rays))]


def main():
    out = {"scope": "Exact finite formula checks, not global theorem verification"}
    blowups = []
    for s in range(1, 8):
        matrix = [row + [1] for row in ident(s)]
        kernel = (-1,) * s + (1,)
        assert mv(matrix, kernel) == (0,) * s
        determinants = []
        for j in range(s):
            chart = ident(s)
            for i in range(s):
                chart[i][j] = 1
            d = determinant(chart)
            assert d == 1
            determinants.append(int(d))
        blowups.append({"s": s, "kernel": kernel,
                        "stratal_chart_determinants": determinants})
    out["blowup_lattices_s_1_through_7"] = blowups

    substitutions = [
        ({(1, 0): 1}, {(1, 1): 1}, {(2, 2): 1, (3, 0): -1}),
        ({(1, 1): 1}, {(1, 2): 1}, {(2, 4): 1, (3, 3): -1}),
        ({(2, 1): 1}, {(3, 2): 1}, {(6, 4): 1, (6, 3): -1}),
    ]
    out["cusp_resolution_substitutions"] = []
    for x, y, expected in substitutions:
        actual = cusp_pullback(x, y)
        assert actual == expected
        out["cusp_resolution_substitutions"].append(
            {"x": terms(x), "y": terms(y), "y2_minus_x3": terms(actual)})

    a = [[0, -1], [1, 0]]
    b = [[0, -1], [1, 1]]
    minus_i = [[-1, 0], [0, -1]]
    assert mpow(a, 2) == mpow(b, 3) == minus_i
    m = mm(a, inv2(b))
    assert m == [[1, 0], [1, 1]]
    assert mm(mm(b, a), m) == minus_i
    for n in range(1, 25):
        assert mpow(m, n) == [[1, 0], [n, 1]]
    out["affine_cusp_SL2Z_certificate"] = {
        "a": a, "b": b, "h": minus_i, "m": m,
        "checked_m_powers": [1, 24],
        "interpretation": "Checks relations and a nontrivial unipotent meridian image."}

    A = [[0, -1], [1, 1]]
    assert mpow(A, 6) == ident(2)
    assert all(mpow(A, i) != ident(2) for i in range(1, 6))

    def product(g, h):
        v, n = g
        w, k = h
        aw = mv(mpow(A, n), w)
        return (tuple(v[i] + aw[i] for i in range(2)), n + k)

    def power(g, n):
        result = ((0, 0), 0)
        for _ in range(n):
            result = product(result, g)
        return result

    def inverse(g):
        v, n = g
        av = mv(mpow(A, -n), v)
        return (tuple(-x for x in av), -n)

    ap = ((0, 1), 3)
    bp = ((1, 0), 2)
    mp = ((0, 0), 1)
    hp = ((0, 0), 6)
    assert power(ap, 2) == power(bp, 3) == power(mp, 6) == hp
    assert product(ap, inverse(bp)) == mp
    assert product(product(bp, ap), mp) == hp
    intersection = [[-6, 0, 0, 1], [0, -3, 0, 1],
                    [0, 0, -2, 1], [1, 1, 1, -1]]
    multiplicities = (1, 2, 3, 6)
    assert mv(intersection, multiplicities) == (0, 0, 0, 0)
    out["proper_cusp_certificate"] = {
        "monodromy": A, "order": 6, "a": ap, "b": bp, "m": mp,
        "h": hp, "intersection_matrix": intersection,
        "multiplicity_null_vector": multiplicities,
        "node_kernels": [[-3, 1], [-2, 1], [-6, 1]]}

    roots = []
    for k in (2, 3, 6):
        for nleaf, ncentral in ((1, 1), (2, 3), (5, 7), (6, 4)):
            d = gcd(k * ncentral, nleaf)
            vector = (-k * ncentral // d, nleaf // d)
            assert nleaf * vector[0] + k * ncentral * vector[1] == 0
            assert gcd(abs(vector[0]), abs(vector[1])) == 1
            roots.append({"power": k, "root_indices": [nleaf, ncentral],
                          "primitive_new_kernel": vector})
    out["root_index_examples"] = roots

    p2 = [(1, 0), (0, 1), (-1, -1)]
    assert self_intersections(p2) == [1, 1, 1]
    p2_blowup = [(1, 0), (1, 1), (0, 1), (-1, -1)]
    assert self_intersections(p2_blowup) == [0, -1, 0, 1]
    fans = []
    for n in range(8):
        rays = [(1, 0), (0, 1), (-1, n), (0, -1)]
        squares = self_intersections(rays)
        assert squares == [0, -n, 0, n]
        fans.append({"n": n, "rays": rays, "squares": squares,
                     "boundary_minimal": -1 not in squares})
    assert [f["n"] for f in fans if not f["boundary_minimal"]] == [1]
    out["toric_surface_fans"] = {
        "P2": p2, "P2_squares": self_intersections(p2),
        "corner_blowup_squares": self_intersections(p2_blowup),
        "Hirzebruch_n_0_through_7": fans}

    graph = {"A": {"B", "C", "E"}, "B": {"A", "C"},
             "C": {"A", "B"}, "E": {"A", "F"}, "F": {"E"}}
    weights = {"A": -1, "B": 0, "C": 0, "E": -2, "F": -1}
    history = []
    for name in ("F", "E"):
        assert weights[name] == -1
        neighbours = sorted(graph[name])
        assert len(neighbours) <= 2
        for v in neighbours:
            graph[v].remove(name)
            weights[v] += 1
        if len(neighbours) == 2:
            v, w = neighbours
            graph[v].add(w)
            graph[w].add(v)
        del graph[name], weights[name]
        history.append({"contracted": name, "weights": weights.copy()})
    assert set(graph) == {"A", "B", "C"}
    assert all(value == 0 for value in weights.values())
    out["smooth_fringe_contraction"] = history
    out["self_node_square_drop"] = {
        "multiplicity": 2, "drop": 2 ** 2,
        "uniqueness_threshold": 2,
        "resolved_threshold": 2 - 2 ** 2}
    out["all_assertions_passed"] = True
    text = json.dumps(out, indent=2, ensure_ascii=False) + "\n"
    Path(__file__).with_name("compactifications_checks_output.json").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
