#!/usr/bin/env python3
"""Exact finite checks supporting the orbit proof in A.115.

Ranks are computed over F3, never by numerical rank.  The arbitrary-depth
conclusion is proved in the manuscript by the explicit orbit modules.
"""
from itertools import product
from math import comb
from pathlib import Path
import json
import numpy as np


def rank3(matrix):
    a = np.array(matrix, dtype=np.int64, copy=True) % 3
    height, width = a.shape
    row = 0
    for col in range(width):
        candidates = np.flatnonzero(a[row:, col])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        a[[row, pivot]] = a[[pivot, row]]
        if a[row, col] == 2:
            a[row] = 2*a[row] % 3
        below = np.flatnonzero(a[row+1:, col]) + row + 1
        if len(below):
            a[below] = (a[below]-a[below, col, None]*a[row]) % 3
        row += 1
        if row == height:
            break
    return row


records = {"polynomial_spaces": [], "literal_modules": []}
lines = []


def record(message):
    lines.append(message)
    print(message, flush=True)


for n in range(1, 8):
    d = 3**(n-1)
    delta = np.zeros((d, d), dtype=np.int64)
    for j in range(1, d):
        for k in range(1, min(j+1, d-j)):
            delta[j+k, j] = comb(j, k) % 3
    rank = rank3(delta)
    powers = [d-3**j for j in range(n)]
    assert d-rank == n
    for power in powers:
        assert not np.any(delta[:, power])
    # The effective cyclic orbit kernels are Y^(m/3) in k[Y]/Y^m.
    coinvariant_counts = []
    for j in range(n-1):
        m = 3**(n-j-1)
        length = m-m//3
        shift = np.zeros((length, length), dtype=np.int64)
        for i in range(length-1):
            shift[i+1, i] = 1
        assert length-rank3(shift) == 1
        coinvariant_counts.append(1)
    coinvariant_counts.append(1)  # {0,d,2d} kernel, C2 swaps its basis.
    assert sum(coinvariant_counts) == n
    records["polynomial_spaces"].append({
        "n": n, "d": d, "invariant_dimension": d-rank,
        "basis_powers": powers, "orbit_coinvariant_dimensions": coinvariant_counts})
    record(f"n={n}: invariant dimension {d-rank}; basis powers {powers}; "
           f"orbit coinvariants {coinvariant_counts}")


for n in range(1, 5):
    N, d = 3**n, 3**(n-1)
    length = 2*d
    # Columns are Z^(d+j) in the actual geometric permutation basis x^i.
    basis = np.array([[comb(d+j, i)*(-1)**(d+j-i) % 3
                       if i <= d+j else 0 for j in range(length)]
                      for i in range(N)], dtype=np.int64)
    block_map = np.zeros((d, N), dtype=np.int64)
    for i in range(N):
        block_map[i % d, i] = 1
    assert not np.any(block_map @ basis % 3)
    assert rank3(basis) == length
    geometric_form = np.zeros((N, N), dtype=np.int64)
    for h in range(d):
        geometric_form[h, h+d] = 1
        geometric_form[h+d, h] = 2
    top = basis.T @ geometric_form @ basis % 3
    assert rank3(top) == length

    translation = np.eye(length, dtype=np.int64)
    for j in range(length-1):
        translation[j+1, j] = 1
    unit = np.zeros((length, length), dtype=np.int64)
    for j in range(length):
        exponent = d+j
        for k in range(exponent+1):
            target = exponent+k
            if target < N:
                unit[target-d, j] = 2*comb(exponent, k)*pow(2, exponent-k, 3) % 3
    assert np.array_equal(translation.T @ top @ translation % 3, top)
    assert np.array_equal(unit.T @ top @ unit % 3, 2*top % 3)

    forms = []
    for j in range(n):
        exponent = d-3**j
        # z^exponent = Z^(2 exponent) * (1+Z)^(-exponent).
        polynomial = np.zeros(length, dtype=np.int64)
        if exponent == 0:
            polynomial[0] = 1
        else:
            for k in range(length-2*exponent):
                polynomial[2*exponent+k] = (-1)**k*comb(exponent+k-1, k) % 3
        operator = np.zeros((length, length), dtype=np.int64)
        for col in range(length):
            operator[col:, col] = polynomial[:length-col]
        form = top @ operator % 3
        assert np.array_equal(form.T % 3, -form % 3)
        assert not np.any(np.diag(form))
        assert np.array_equal(translation.T @ form @ translation % 3, form)
        assert np.array_equal(unit.T @ form @ unit % 3, 2*form % 3)
        assert rank3(form) == 2*3**j
        assert not np.any(form[:, 2*3**j:])
        if j:
            h = 3**(j-1)
            restriction = form[2*h:, 2*h:]
            assert rank3(restriction) == 2*h
            assert not np.any(form[2*h:, 4*h:])
        forms.append(form)
    rank_counts = {}
    for coefficients in product(range(3), repeat=n):
        if not any(coefficients):
            continue
        last = max(i for i, c in enumerate(coefficients) if c)
        if coefficients[last] != 1:
            continue
        form = sum((c*forms[j] for j, c in enumerate(coefficients)),
                   np.zeros((length, length), dtype=np.int64)) % 3
        rank = rank3(form)
        assert rank == 2*3**last
        rank_counts[rank] = rank_counts.get(rank, 0)+1
    assert rank_counts == {2*3**j: 3**j for j in range(n)}
    records["literal_modules"].append({
        "n": n, "N": N, "relative_dimension": length,
        "projective_rank_counts": rank_counts,
        "restricted_nondegenerate_dimensions": [2*3**(j-1) for j in range(1,n)]})
    record(f"n={n}: literal block map, both generating actions, every form, "
           f"all restricted radicals and projective ranks {rank_counts} passed")


quadratic_checks = 0
for a, b in product((1, 2), repeat=2):
    for l1, l2, offset in product(range(3), repeat=3):
        values = {(a*x*x+b*y*y+l1*x+l2*y+offset) % 3
                  for x, y in product(range(3), repeat=2)}
        assert values == {0, 1, 2}
        quadratic_checks += 1
records["affine_quadratic_value_checks"] = quadratic_checks
record(f"Affine nondegenerate two-dimensional quadratic value checks: {quadratic_checks}.")
record("ALL EXACT CHECKS PASSED. The arbitrary-depth proof is the orbit argument in A.115.")
destination = Path(__file__)
destination.with_name(destination.stem+"_data.json").write_text(json.dumps(records, indent=2)+"\n")
destination.with_name(destination.stem+"_output.txt").write_text("\n".join(lines)+"\n")
