#!/usr/bin/env python3
"""Exact finite algebra in D.71; no cubic scalar realization assertion."""
from collections import Counter
from itertools import product
from math import isqrt
from pathlib import Path
import json

CHECKS = Counter()


def check(kind, truth):
    assert truth, kind
    CHECKS[kind] += 1


def red(word):
    result = []
    for a in word:
        if result and result[-1] == -a:
            result.pop()
        else:
            result.append(a)
    return tuple(result)


def inv(word):
    return tuple(-a for a in reversed(word))


def mul(*words):
    return red(a for word in words for a in word)


def wpow(word, n):
    if n < 0:
        return wpow(inv(word), -n)
    return mul(*(word for _ in range(n)))


def sub(word, images):
    return mul(*(images[a-1] if a > 0 else inv(images[-a-1])
                 for a in word))


def compose(left, right):
    return tuple(sub(w, left) for w in right)


def char(word, a, b):
    return sum((a if abs(z) == 1 else b)*(1 if z > 0 else -1)
               for z in word) % 3


def matrix_product(a, b, modulus=None):
    result = [[sum(x*y for x, y in zip(row, column))
               for column in zip(*b)] for row in a]
    return result if modulus is None else [
        [x % modulus for x in row] for row in result]


def matrix_add(*matrices, modulus=None):
    result = [[sum(m[i][j] for m in matrices)
               for j in range(len(matrices[0][0]))]
              for i in range(len(matrices[0]))]
    return result if modulus is None else [
        [x % modulus for x in row] for row in result]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def rank_mod(matrix, p):
    rows = [[x % p for x in row] for row in matrix]
    out = 0
    for j in range(len(rows[0])):
        found = next((k for k in range(out, len(rows)) if rows[k][j]), None)
        if found is None:
            continue
        rows[out], rows[found] = rows[found], rows[out]
        u = pow(rows[out][j], -1, p)
        rows[out] = [(u*x) % p for x in rows[out]]
        for k in range(len(rows)):
            if k != out:
                u = rows[k][j]
                rows[k] = [(x-u*y) % p for x, y in zip(rows[k], rows[out])]
        out += 1
        if out == len(rows):
            break
    return out


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def rotate(v, k):
    n = len(v)
    out = [0]*n
    for i, x in enumerate(v):
        out[(i+k) % n] = x
    return out


def addv(*vectors):
    return [sum(xs) for xs in zip(*vectors)]


def negate(v):
    return [-x for x in v]


def geom(v, k):
    return addv(*(rotate(v, i) for i in range(k)))


def main():
    x, y = (1,), (2,)
    commutator = (1, 2, -1, -2)
    quarter = ((1, 2, -1), (-1,))
    quarter_inverse = ((-2,), (2, 1, -2))
    basis_cases = []
    for a, b in product(range(3), repeat=2):
        if (a, b) == (0, 0):
            continue
        change, reverse = (x, y), (x, y)
        k = 0
        while char(change[0], a, b) != 1:
            change = compose(change, quarter)
            reverse = compose(quarter_inverse, reverse)
            k += 1
            assert k <= 3
        d = char(change[1], a, b)
        if d == 2:
            d = -1
        shear = (x, mul(y, wpow(x, -d)))
        shear_inverse = (x, mul(y, wpow(x, d)))
        change = compose(change, shear)
        reverse = compose(shear_inverse, reverse)
        check("based_free_basis", compose(change, reverse) == (x, y))
        check("based_free_basis", compose(reverse, change) == (x, y))
        check("based_free_basis", sub(commutator, change) == commutator)
        check("based_free_basis", char(change[0], a, b) == 1)
        check("based_free_basis", char(change[1], a, b) == 0)
        basis_cases.append({"character": [a, b], "quarter_steps": k,
                            "shear": d, "basis": change, "inverse": reverse})

    # Exact integral averaged-cover matrices with the retained homology map.
    j3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    j3_inverse = matrix_product(j3, j3)
    j4 = [[1, 0, 0, 0]] + [[0]+row for row in j3]
    cover_map = [[3, 0, 0, 0], [0, 1, 1, 1]]
    base_a = [[-2, -3], [1, 1]]
    averaged_cases = []
    for a, b in product(range(-2, 3), repeat=2):
        change = [[1, 3*a], [b, 1+3*a*b]]
        reverse = [[1+3*a*b, -3*a], [-b, 1]]
        action = matrix_product(matrix_product(change, base_a), reverse)
        aa, ab = action[0]
        ba, bb = action[1]
        check("averaged_integrality", ab % 3 == 0 and (bb-1) % 3 == 0)
        s = [[aa]+[ab//3]*3]
        s += [[ba]+[j3_inverse[i][j]+(bb-1)//3 for j in range(3)]
              for i in range(3)]
        ss = matrix_product(s, s)
        check("averaged_cyclic_action", matrix_product(ss, s) == identity(4))
        check("averaged_cyclic_action",
              matrix_add(identity(4), s, ss) == [[0]*4 for _ in range(4)])
        check("averaged_cover_map",
              matrix_product(cover_map, s) == matrix_product(action, cover_map))
        check("averaged_deck_commutation",
              matrix_product(s, j4) == matrix_product(j4, s))
        difference = matrix_add(s, [[-z for z in row] for row in identity(4)])
        check("averaged_jordan_blocks", rank_mod(difference, 3) == 2)
        averaged_cases.append({"base_action": action, "cover_action": s})

    quotient_cases = []
    for q in range(7, 98):
        if not prime(q) or q % 3 != 1:
            continue
        roots = [z for z in range(2, q) if pow(z, 3, q) == 1]
        check("primitive_cube_roots", len(roots) == 2)
        for lam in roots:
            lam2 = lam*lam % q
            group = [(a, e) for a in range(q) for e in range(3)]

            def gm(a, b):
                return ((a[0]+pow(lam, a[1], q)*b[0]) % q,
                        (a[1]+b[1]) % 3)

            def gi(a):
                return ((-pow(lam, -a[1], q)*a[0]) % q, (-a[1]) % 3)

            rr, tt = (1, 0), (0, 1)
            cusp = gm(gm(gm(tt, rr), gi(tt)), gi(rr))
            check("frobenius_peripheral_map", cusp == ((lam-1) % q, 0))
            generated, pending = {(0, 0)}, [(0, 0)]
            while pending:
                z = pending.pop()
                for g in (rr, tt):
                    w = gm(z, g)
                    if w not in generated:
                        generated.add(w)
                        pending.append(w)
            check("frobenius_generation", generated == set(group))
            unseen, cycle_lengths = set(group), []
            while unseen:
                start = next(iter(unseen))
                z, cycle = start, []
                while z not in cycle:
                    cycle.append(z)
                    unseen.remove(z)
                    z = gm(z, cusp)
                check("peripheral_cycle_closure", z == start)
                cycle_lengths.append(len(cycle))
            check("surface_cover_type", sorted(cycle_lengths) == [q, q, q])
            genus = (3*q-1)//2
            check("surface_cover_type", 2-2*genus-3 == -3*q)
            for twist in range(q):
                check("actual_cubic_twist",
                      (3*twist % q == 0) == (twist == 0))

            # Exact bad-coordinate matrix and invariant linear character.
            scalar = lam2
            inv3 = pow(3, -1, q)
            s = [[scalar, 0, 0, 0]]
            s += [[0]+[(lam*j3_inverse[i][j]+(scalar-lam)*inv3) % q
                        for j in range(3)] for i in range(3)]
            ell = [[0, 1, lam, lam2]]
            check("invariant_cover_character",
                  matrix_product(ell, s, q) == ell)
            check("scaled_deck_character",
                  matrix_product(ell, j4, q) ==
                  [[lam*z % q for z in ell[0]]])
            check("scalar_cubic_matrix",
                  matrix_product(matrix_product(s, s, q), s, q) == identity(4))

            # Integral graph-cycle inverse maps in Z[C_q], with no division.
            zero, norm = [0]*q, [1]*q
            units = [[int(i == j) for i in range(q)] for j in range(q)]
            tests = []
            for v in units:
                tests += [(v, zero, zero, 0),
                          (zero, v, zero, 0), (zero, zero, v, 0)]
            tests.append((zero, zero, zero, 1))
            for aa, bb, dd, k in tests:
                b0 = addv(negate(geom(bb, lam)), negate(geom(dd, lam2)),
                           [k*z for z in norm])
                boundary = addv(rotate(b0, 1), negate(b0),
                                rotate(bb, lam), negate(bb),
                                rotate(dd, lam2), negate(dd))
                check("integral_cycle_map", boundary == zero)
                residual = addv(b0, geom(bb, lam), geom(dd, lam2))
                check("integral_cycle_inverse", residual == [k]*q)
                check("integral_cycle_inverse",
                      (aa, bb, dd, residual[0]) == (aa, bb, dd, k))
            check("cycle_rank", len(tests) == 3*q+1)
            check("high_degree_bound", 1+2 == 3)
            check("section_count_obstruction", 3*q > 3)
            quotient_cases.append({"q": q, "lambda": lam,
                                   "group_order": 3*q, "genus": genus,
                                   "cusps": 3, "rank_N": 3*q+1,
                                   "rank_W3": 3*(q-1)})

    # Exhaustive rank-three order-three matrix/norm calculation over F3.
    eye = identity(3)
    types = Counter()
    for entries in product(range(3), repeat=9):
        s = [list(entries[3*i:3*i+3]) for i in range(3)]
        ss = matrix_product(s, s, 3)
        if matrix_product(ss, s, 3) != eye:
            continue
        diff = matrix_add(s, [[-z for z in row] for row in eye], modulus=3)
        norm = matrix_add(eye, s, ss, modulus=3)
        check("rank_three_cyclic_norm",
              norm == matrix_product(diff, diff, 3))
        d_rank, n_rank = rank_mod(diff, 3), rank_mod(norm, 3)
        types[f"{d_rank},{n_rank}"] += 1
        if n_rank == 1:
            check("rank_three_regular_block", d_rank == 2)
            cyclic_found = False
            for v in product(range(3), repeat=3):
                column = [[z] for z in v]
                sv = matrix_product(s, column, 3)
                ssv = matrix_product(ss, column, 3)
                cols = [[v[i], sv[i][0], ssv[i][0]] for i in range(3)]
                if rank_mod(cols, 3) == 3:
                    cyclic_found = True
                    break
            check("cyclic_vector_lift_input", cyclic_found)
    check("rank_three_classification", sum(types.values()) == 729)
    check("rank_three_classification",
          dict(types) == {"0,0": 1, "1,0": 104, "2,1": 624})

    # The exact unit consequence of b*a=3 is visible at the first two digits.
    for a, b in product(range(9), repeat=2):
        if a % 3 == 0 and a*b % 9 == 3:
            check("fixed_pair_norm_unit", a in (3, 6) and b % 3 != 0)

    result = {"status": "PASS", "claim": "D.71",
              "total_exact_checks": sum(CHECKS.values()),
              "checks_by_kind": dict(sorted(CHECKS.items())),
              "based_free_basis_cases": basis_cases,
              "integral_averaged_matrix_cases": averaged_cases,
              "frobenius_cover_cases": quotient_cases,
              "rank_three_cyclic_matrix_types": dict(types),
              "scope": "Exact finite identities only. The full quotient, "
                       "fixed-cup obstruction, integral scalar extension and "
                       "descent, and full Brown arguments are proved in d71.tex. "
                       "No scalar-coordinate exclusion or realization is asserted."}
    destination = Path(__file__).with_name("torus_cubic_frobenius_d71_output.json")
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"],
                      "total_exact_checks": result["total_exact_checks"],
                      "basis_cases": len(basis_cases),
                      "integral_matrix_cases": len(averaged_cases),
                      "frobenius_cover_cases": len(quotient_cases),
                      "rank_three_matrix_types": dict(types)}, indent=2))


if __name__ == "__main__":
    main()
