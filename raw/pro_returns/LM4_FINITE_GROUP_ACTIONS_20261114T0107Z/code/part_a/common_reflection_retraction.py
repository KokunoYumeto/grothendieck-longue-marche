#!/usr/bin/env python3
"""Exact integral homology obstruction for the specified F.12 map (claim F.13)."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json


def rref_rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    pivot_row = 0
    pivot_columns = []
    for column in range(len(a[0])):
        pivot = next((r for r in range(pivot_row, len(a))
                      if a[r][column]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][column]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(len(a)):
            if r != pivot_row and a[r][column]:
                scale = a[r][column]
                a[r] = [x - scale * y
                        for x, y in zip(a[r], a[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row, pivot_columns, a


def main():
    # Source order: zero, infinity, five plus cusps, five minus cusps.
    matrix, labels = [], []
    for j in range(5):
        row = [0] * 12
        row[2 + j], row[7 + j] = 2, -2
        matrix.append(row)
        labels.append(["L", j + 1])
    for j in range(5):
        row = [0] * 12
        row[0], row[1], row[7 + j] = 1, 1, -2
        matrix.append(row)
        labels.append(["M", j + 1])
    for i, j in combinations(range(5), 2):
        k = (3 * (i + j)) % 5
        assert (2 * k - i - j) % 5 == 0
        row = [0] * 12
        row[0] = row[1] = 1
        row[2 + k] += 1
        row[7 + k] += 1
        row[7 + i] -= 2
        row[7 + j] -= 2
        matrix.append(row)
        labels.append(["N", i + 1, j + 1])
    assert len(matrix) == 20
    assert all(sum(row) == 0 for row in matrix)
    full_kernel_vector = [1, -1] + [0] * 10
    assert all(sum(a * b for a, b in zip(row, full_kernel_vector)) == 0
               for row in matrix)

    # Quotient by the puncture sum, with infinity omitted as a basis vector.
    reduced = [[row[0]] + row[2:] for row in matrix]
    kernel = [2] + [1] * 10
    assert all(sum(a * b for a, b in zip(row, kernel)) == 0
               for row in reduced)
    assert [full_kernel_vector[i] - full_kernel_vector[1]
            for i in [0] + list(range(2, 12))] == kernel
    rank, pivots, rr = rref_rank(reduced)
    assert rank == 10
    assert len(reduced[0]) - rank == 1

    primary = []
    for prime in (2, 3, 5, 7, 11, 13, 17, 19):
        for exponent in (1, 2, 3):
            modulus = prime ** exponent
            vec = [x % modulus for x in kernel]
            assert any(vec)
            assert all(x == 1 for x in vec[1:])
            assert all(sum(a * b for a, b in zip(row, vec)) % modulus == 0
                       for row in reduced)
            primary.append({"prime": prime, "exponent": exponent,
                            "modulus": modulus, "kernel_vector": vec})

    result = {
        "claim": "F.13",
        "status": "PASS",
        "source_cusp_order": ["0", "infinity"]
            + [f"+zeta^{j}" for j in range(5)]
            + [f"-zeta^{j}" for j in range(5)],
        "target_characters": labels,
        "full_divisor_matrix": matrix,
        "puncture_sum_killed": True,
        "full_cusp_kernel_vector": full_kernel_vector,
        "omitted_basis_cusp": "infinity",
        "primitive_kernel_vector": kernel,
        "rational_rank": rank,
        "pivot_columns": pivots,
        "primary_checks": primary,
        "counts": {"divisor_rows": len(matrix),
                   "primary_reductions": len(primary),
                   "primary_row_equalities": len(matrix) * len(primary)},
        "scope": "Exact homology of the specified F.12 injection and its left-inverse obstruction. No assertion about its full equalizer, arbitrary finite-index domains, or faithfulness of a forgotten map."
    }
    target = Path(__file__).with_name("common_reflection_retraction_output.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in
                     ("claim", "status", "primitive_kernel_vector", "rational_rank",
                      "counts", "scope")}, indent=2))


if __name__ == "__main__":
    main()
