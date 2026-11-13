#!/usr/bin/env python3
"""Exact finite identities used in D.59.

This program checks incidence ranks, boundary modules, cyclic cohomology
dimensions, and the characteristic class-two group of order 32.  It does
not replace the full-profinite conjugacy or Brown restriction arguments.
"""
from itertools import product
from math import gcd
from pathlib import Path
import json

BASE = Path(__file__).resolve().with_suffix("")


def binary_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def boundary_vectors(m):
    return [1 << i for i in range(m - 1)] + [(1 << (m - 1)) - 1]


def apply_columns(columns, vector):
    result = 0
    for j, column in enumerate(columns):
        if (vector >> j) & 1:
            result ^= column
    return result


def incidence_checks():
    summaries = []
    total = 0
    compatible = 0
    for m in range(3, 32, 2):
        d = boundary_vectors(m)
        assert binary_rank(d) == m - 1
        assert _xor(d) == 0
        rotation = d[1:m]
        for v in d:
            norm = 0
            current = v
            for _ in range(m):
                norm ^= current
                current = apply_columns(rotation, current)
            assert current == v and norm == 0
        cases = []
        for h in divisors(m):
            vertices = m // h
            for delta in range(m):
                incidence = [
                    (1 << (i % vertices))
                    ^ (1 << ((i + delta) % vertices))
                    for i in range(m)
                ]
                rank = binary_rank(incidence)
                augmented_rank = binary_rank([
                    incidence[i] | (d[i] << vertices)
                    for i in range(m)
                ])
                # All m-1 boundary coordinates must admit vertex values.
                actual = rank == augmented_rank
                predicted = h == 1 and gcd(delta, m) == 1
                assert actual == predicted
                assert rank == vertices - gcd(delta, vertices)
                cases.append({
                    "centralizer_image_order": h,
                    "transporter_character": delta,
                    "vertex_count": vertices,
                    "incidence_rank": rank,
                    "augmented_rank": augmented_rank,
                    "boundary_assignment_exists": actual,
                })
                total += 1
                compatible += int(actual)
        summaries.append({
            "degree": m,
            "boundary_rank": m - 1,
            "deck_average_on_boundary": "zero",
            "cases": cases,
        })
    return {
        "degrees": list(range(3, 32, 2)),
        "case_count": total,
        "compatible_cases": compatible,
        "exact_criterion": "h=1 and gcd(delta,m)=1",
        "details": summaries,
    }


def _xor(values):
    result = 0
    for value in values:
        result ^= value
    return result


def multiply_matrix(a, b):
    return tuple(
        sum(a[2*i+k] * b[2*k+j] for k in range(2)) % 2
        for i in range(2) for j in range(2)
    )


def high_cohomology_checks():
    identity = (1, 0, 0, 1)
    base_matrices = [
        a for a in product(range(2), repeat=4)
        if multiply_matrix(a, a) == identity
    ]
    result = []
    for m in range(3, 32, 2):
        rows = []
        for a in base_matrices:
            columns = [
                a[0] | (a[2] << 1),
                a[1] | (a[3] << 1),
            ] + [1 << i for i in range(2, m + 1)]
            norm_columns = [
                column ^ (1 << j) for j, column in enumerate(columns)
            ]
            rank_norm = binary_rank(norm_columns)
            for column in norm_columns:
                assert apply_columns(norm_columns, column) == 0
            positive_cyclic_dimension = (m + 1) - 2 * rank_norm
            high_extension_dimension = 1 + positive_cyclic_dimension
            expected = m + 2 if a == identity else m
            assert high_extension_dimension == expected
            rows.append({
                "base_matrix": a,
                "norm_rank": rank_norm,
                "positive_cyclic_dimension": positive_cyclic_dimension,
                "high_extension_dimension": high_extension_dimension,
            })
        # The degree-three cover prohibits a cusp H1 dimension of one.
        if m == 3:
            allowed_r = [r for r in (0, 1) if m * (1 + r) <= m + 2]
            assert allowed_r == [0]
        # Other-section Brown contribution in the identity-mod-two case.
        solutions = []
        for h in divisors(m):
            for d in range(m + 3):
                if (m // h) * (1 + d) == 2:
                    solutions.append((h, d))
        assert solutions == [(m, 1)]
        result.append({
            "degree": m,
            "module_cases": rows,
            "other_section_Brown_solutions_h_d": solutions,
        })
    return result


def q32_product(g, h):
    a, b, k = g
    c, d, l = h
    return ((a + c) % 4, (b + d) % 4, (k + l + b*c) % 2)


def q32_power(g, n):
    result = (0, 0, 0)
    for _ in range(n):
        result = q32_product(result, g)
    return result


def q32_inverse(g):
    a, b, k = g
    return ((-a) % 4, (-b) % 4, (k + a*b) % 2)


def q32_commutator(g, h):
    result = (0, 0, 0)
    for value in (g, h, q32_inverse(g), q32_inverse(h)):
        result = q32_product(result, value)
    return result


def degree_two_checks():
    elements = list(product(range(4), range(4), range(2)))
    identity = (0, 0, 0)
    x, y, z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    assert q32_commutator(x, y) == z
    # Direct finite checks of inverses, powers and the centre.
    for g in elements:
        assert q32_product(g, q32_inverse(g)) == identity
        assert q32_power(g, 4) == identity
    centre = [
        g for g in elements
        if q32_product(g, x) == q32_product(x, g)
        and q32_product(g, y) == q32_product(y, g)
    ]
    assert centre == [
        g for g in elements if g[0] % 2 == 0 and g[1] % 2 == 0
    ]
    assert len(centre) == 8

    def central_vector(g):
        assert g in centre
        return (g[0] // 2) | ((g[1] // 2) << 1) | (g[2] << 2)

    def word_image(g, xx, yy, zz):
        a, b, k = g
        result = q32_product(q32_power(xx, a), q32_power(yy, b))
        return q32_product(result, q32_power(zz, k))

    output = []
    matrix_identity = (1, 0, 0, 1)
    for matrix in product(range(2), repeat=4):
        if multiply_matrix(matrix, matrix) != matrix_identity:
            continue
        a, b, c, d = matrix
        xx = (a, c, 0)
        yy = (b, d, 0)
        zz = q32_commutator(xx, yy)
        assert zz == z
        images = [word_image(g, xx, yy, zz) for g in elements]
        assert len(set(images)) == 32
        for i, g in enumerate(elements):
            for j, h in enumerate(elements):
                assert word_image(q32_product(g, h), xx, yy, zz) == (
                    q32_product(images[i], images[j])
                )
        columns = [
            a | (c << 1) | ((a*c) << 2),
            b | (d << 1) | ((b*d) << 2),
            4,
        ]
        for g in centre:
            assert central_vector(word_image(g, xx, yy, zz)) == (
                apply_columns(columns, central_vector(g))
            )
        difference_image = {
            v ^ apply_columns(columns, v) for v in range(8)
        }
        assert 4 not in difference_image
        output.append({
            "matrix": matrix,
            "degree_two_columns": columns,
            "I_plus_action_image": sorted(difference_image),
            "commutator_vector": 4,
            "commutator_in_image": False,
            "full_group_homomorphism_comparisons": 32 * 32,
            "degree_two_element_comparisons": 8,
        })
    assert len(output) == 4
    return {
        "characteristic_group_order": 32,
        "central_degree_two_order": 8,
        "involutive_base_matrix_count": 4,
        "cases": output,
    }


def main():
    output = {
        "claim": "D.59",
        "status": "all exact finite checks passed",
        "scope": (
            "These calculations certify the displayed finite algebra. "
            "Full conjugacy classes, deck topology, Brown restriction and "
            "ambient homology conclusions are proved in d59.tex."
        ),
        "incidence": incidence_checks(),
        "cyclic_cohomology": high_cohomology_checks(),
        "degree_two": degree_two_checks(),
    }
    BASE.with_name(BASE.name + "_output.json").write_text(
        json.dumps(output, indent=2) + "\n"
    )
    lines = [
        "D.59 exact finite certificate: PASS",
        f"Odd cover degrees: {len(output['incidence']['degrees'])}",
        f"Incidence systems: {output['incidence']['case_count']}",
        f"Compatible systems: {output['incidence']['compatible_cases']}",
        "Compatibility exactly h=1 and gcd(delta,m)=1.",
        "Boundary deck averages, high cohomology and Brown dimensions: PASS",
        "Four involutive GL2(F2) degree-two actions: PASS",
        "Characteristic group order 32; 4096 exact homomorphism comparisons.",
        "The commutator vector is outside every I+action image.",
        output["scope"],
    ]
    report = "\n".join(lines) + "\n"
    BASE.with_name(BASE.name + "_stdout.txt").write_text(report)
    print(report, end="")


if __name__ == "__main__":
    main()
