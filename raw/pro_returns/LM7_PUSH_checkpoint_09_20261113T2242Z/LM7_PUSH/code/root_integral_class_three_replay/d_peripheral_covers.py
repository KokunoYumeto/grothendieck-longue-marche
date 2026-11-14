#!/usr/bin/env python3
"""Literal finite-cover checks of the D.24 central peripheral obstruction.

Every retained cover is specified by permutations of its cosets.  Schreier
words, all induced boundary words, and all central corrections are computed
from those permutations.  Matrix evaluations are in SL(2,F_11), using the
displayed D.24 triple.  No cohomological criterion is used to find solutions.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
I = (1, 0, 0, 1)
MINUS_I = (10, 0, 0, 10)
U = (0, 10, 1, 10)
V = (1, 0, 1, 1)
Z = (1, 10, 0, 1)


def mul(a, b):
    return tuple(t % 11 for t in (
        a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
        a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))


def inv(a):
    return (a[3], -a[1] % 11, -a[2] % 11, a[0])


def inverse_word(word):
    return [-a for a in reversed(word)]


def matrix_word(word, generators):
    ans = I
    for a in word:
        g = generators[abs(a)-1]
        ans = mul(ans, g if a > 0 else inv(g))
    return ans


def order(g):
    h = I
    for n in range(1, 1321):
        h = mul(h, g)
        if h == I:
            return n
    raise AssertionError("SL2(F11) order bound exhausted")


def inverse_permutation(p):
    out = [None] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return out


def cycles(p):
    seen = set()
    out = []
    for j in range(len(p)):
        if j in seen:
            continue
        cycle = []
        k = j
        while k not in seen:
            seen.add(k)
            cycle.append(k)
            k = p[k]
        out.append(cycle)
    return out


def rank2(matrix):
    rows = [sum((a % 2) << j for j, a in enumerate(row)) for row in matrix]
    pivots = {}
    for value in rows:
        while value:
            p = value.bit_length()-1
            if p not in pivots:
                pivots[p] = value
                break
            value ^= pivots[p]
    return len(pivots)


def check_cover(px, py, label):
    d = len(px)
    action = {1: px, 2: py, -1: inverse_permutation(px), -2: inverse_permutation(py)}
    paths = {0: []}
    tree = set()
    todo = deque([0])
    while todo:
        u = todo.popleft()
        for a in (1, 2, -1, -2):
            v = action[a][u]
            if v not in paths:
                paths[v] = paths[u]+[a]
                tree.add((u, a) if a > 0 else (v, -a))
                todo.append(v)
    assert len(paths) == d
    edges = [(u, a) for u in range(d) for a in (1, 2) if (u, a) not in tree]
    edge_index = {e: j+1 for j, e in enumerate(edges)}
    basis = [paths[u]+[a]+inverse_word(paths[action[a][u]]) for u, a in edges]
    assert len(basis) == d+1

    def rewrite(word):
        u = 0
        ans = []
        for a in word:
            v = action[a][u]
            edge = (u, a) if a > 0 else (v, -a)
            if edge in edge_index:
                ans.append(edge_index[edge] * (1 if a > 0 else -1))
            u = v
        assert u == 0
        return ans

    for j, word in enumerate(basis):
        assert rewrite(word) == [j+1]
    pz = [action[-1][action[-2][u]] for u in range(d)]
    boundaries = []
    rows = []
    errors = []
    original_images = [matrix_word(w, (U, V)) for w in basis]
    for i, (word, permutation) in enumerate(zip(([1], [2], [-2, -1]), (px, py, pz))):
        c = cycles(permutation)
        assert sum(map(len, c)) == d
        for cycle in c:
            t = paths[cycle[0]]
            boundary = t+word*len(cycle)+inverse_word(t)
            hword = rewrite(boundary)
            image = matrix_word(boundary, (U, V))
            assert matrix_word(hword, original_images) == image
            parity = int(order(image) % 2 == 0)
            odd_lift = mul(MINUS_I, image) if parity else image
            assert order(odd_lift) % 2 == 1
            assert parity == (len(cycle) % 2 if i == 2 else 0)
            abelian = [hword.count(j)-hword.count(-j) for j in range(1, d+2)]
            rows.append(abelian)
            errors.append(parity)
            boundaries.append({"peripheral_index": i+1, "cycle": cycle,
                               "literal_F_word": boundary, "literal_H_word": hword,
                               "H_abelianization": abelian,
                               "uncorrected_matrix": image, "prescribed_odd_lift": odd_lift})
    b = len(boundaries)
    assert all(sum(row[j] for row in rows) == 0 for j in range(d+1))
    assert rank2(rows) == b-1
    genus_twice = d+2-b
    assert genus_twice >= 0 and genus_twice % 2 == 0
    solutions = []
    for correction in product((0, 1), repeat=d+1):
        if any(sum(a*c for a, c in zip(row, correction)) % 2 != error
               for row, error in zip(rows, errors)):
            continue
        images = [mul(MINUS_I, g) if bit else g for bit, g in zip(correction, original_images)]
        for boundary in boundaries:
            assert matrix_word(boundary["literal_H_word"], images) == tuple(boundary["prescribed_odd_lift"])
        solutions.append(list(correction))
    expected = 0 if d % 2 else 2**genus_twice
    assert len(solutions) == expected
    result = {"label": label, "index": d, "x_permutation": px, "y_permutation": py,
              "Schreier_basis": basis, "boundaries": boundaries,
              "boundary_count": b, "genus": genus_twice//2,
              "boundary_matrix_rank_mod2": rank2(rows),
              "relative_obstruction_mod2": sum(errors) % 2,
              "all_central_corrections_tested": 2**(d+1),
              "literal_lift_count": len(solutions), "central_corrections": solutions}
    print(json.dumps({k: result[k] for k in (
        "label", "index", "boundary_count", "genus", "relative_obstruction_mod2", "literal_lift_count")}), flush=True)
    return result


def main():
    assert mul(mul(U, V), Z) == MINUS_I
    assert [order(a) for a in (U, V, Z)] == [3, 11, 11]
    records = []
    for d in range(1, 10):
        px = [(j+1) % d for j in range(d)]
        seen = set()
        for name, py in (("cyclic_x", list(range(d))), ("equal_cycles", px),
                         ("reflection_y", [(-j) % d for j in range(d)])):
            if tuple(py) in seen:
                continue
            seen.add(tuple(py))
            records.append(check_cover(px, py, name))
    output = {"records": records, "covers_checked": len(records),
              "all_boundary_words_and_all_central_corrections_verified": True,
              "scope": "Explicit connected covers of indices 1 through 9. The all-index theorem is proved by the relative restriction map in D.26."}
    HERE.joinpath("d_peripheral_covers.json").write_text(json.dumps(output, indent=2)+"\n")
    print("PERIPHERAL_COVERS_PASS", flush=True)


if __name__ == "__main__":
    main()
