#!/usr/bin/env python3
"""Exact cyclic-cover chain, averaging and norm certificates for D.54-D.55."""
import json
from pathlib import Path


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zero(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


def add(a, b, p):
    return [[(x+y) % p for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, k, p):
    return [[k*x % p for x in row] for row in a]


def multiply(a, b, p):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def power(a, k, p):
    result = eye(len(a))
    for _ in range(k):
        result = multiply(result, a, p)
    return result


def rank(a, p):
    b = [[x % p for x in row] for row in a]
    r = 0
    for j in range(len(b[0])):
        pivot = next((i for i in range(r, len(b)) if b[i][j]), None)
        if pivot is None:
            continue
        b[r], b[pivot] = b[pivot], b[r]
        b[r] = [x*pow(b[r][j], -1, p) % p for x in b[r]]
        for i in range(len(b)):
            if i != r and b[i][j]:
                factor = b[i][j]
                b[i] = [(x-factor*y) % p for x, y in zip(b[i], b[r])]
        r += 1
        if r == len(b):
            break
    return r


def inverse(a, p):
    n = len(a)
    b = [[x % p for x in row] + identity
         for row, identity in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if b[i][j])
        b[j], b[pivot] = b[pivot], b[j]
        b[j] = [x*pow(b[j][j], -1, p) % p for x in b[j]]
        for i in range(n):
            if i != j and b[i][j]:
                factor = b[i][j]
                b[i] = [(x-factor*y) % p for x, y in zip(b[i], b[j])]
    assert [row[:n] for row in b] == eye(n)
    return [row[n:] for row in b]


def check_cover(p, q):
    assert p != q
    # The q-sheeted x-cycle/y-loop graph has C1 of rank 2q, C0 of rank q.
    # Its kernel basis is X=sum x_i, y_0,...,y_(q-1).
    d1 = zero(q, 2*q)
    for i in range(q):
        d1[i][i] = -1 % p
        d1[(i+1) % q][i] = 1
    assert rank(d1, p) == q-1
    n = q+1
    cycles = zero(2*q, n)
    for i in range(q):
        cycles[i][0] = 1
        cycles[q+i][1+i] = 1
    assert multiply(d1, cycles, p) == zero(q, n)
    assert rank(cycles, p) == n

    deck = zero(n, n)
    deck[0][0] = 1
    for i in range(q):
        deck[1+(i+1) % q][1+i] = 1
    assert power(deck, q, p) == eye(n)
    boundaries = zero(n, q)
    for i in range(q):
        boundaries[1+(i+1) % q][i] = 1
        boundaries[1+i][i] = -1 % p
    assert rank(boundaries, p) == q-1
    assert all(sum(row) % p == 0 for row in boundaries)
    assert all(any(row[i] for row in boundaries) for i in range(q))

    # Columns: X, Y=sum y_i, then q-1 individual boundary vectors.
    change = zero(n, n)
    change[0][0] = 1
    for i in range(q):
        change[1+i][1] = 1
    for i in range(q-1):
        for j in range(n):
            change[j][2+i] = boundaries[j][i]
    assert rank(change, p) == n
    change_inverse = inverse(change, p)
    average = zero(n, n)
    for j in range(q):
        average = add(average, power(deck, j, p), p)
    average = scale(average, pow(q, -1, p), p)
    assert multiply(average, average, p) == average
    assert rank(average, p) == 2
    assert multiply(average, boundaries, p) == zero(n, q)
    diagonal_average = zero(n, n)
    diagonal_average[0][0] = diagonal_average[1][1] = 1
    assert multiply(change, multiply(diagonal_average, change_inverse, p), p) == average

    # The forced action is cyclotomic on eM and identity on boundary augmentation.
    block = eye(n)
    base = [[0, -1], [1, -1]] if p == 3 else [[-1, 0], [0, -1]]
    for i in range(2):
        for j in range(2):
            block[i][j] = base[i][j] % p
    action = multiply(change, multiply(block, change_inverse, p), p)
    assert power(action, p, p) == eye(n)
    assert multiply(action, boundaries, p) == boundaries
    assert multiply(action, deck, p) == multiply(deck, action, p)
    norm = zero(n, n)
    for j in range(p):
        norm = add(norm, power(action, j, p), p)
    assert norm == zero(n, n)
    selected_boundary = [row[0] for row in boundaries]
    assert any(selected_boundary)

    return {
        "coefficient_prime": p,
        "cover_degree": q,
        "surface_type": [1, q],
        "cover_graph_boundary_rank": q-1,
        "H1_rank": n,
        "boundary_span_rank": q-1,
        "deck_average_rank": 2,
        "selected_primitive_boundary": selected_boundary,
        "all_individual_boundary_vectors_nonzero": True,
        "action_fixes_boundary_and_commutes_with_deck": True,
        "order_p_norm_is_zero_mod_p": True,
        "nonzero_unit_boundary_power_cannot_be_a_norm": True
    }


def main():
    cases = [check_cover(3, q) for q in (2, 5, 7, 11, 13, 17, 19)]
    cases += [check_cover(2, q) for q in (3, 5, 7, 11, 13, 17, 19)]
    result = {
        "claims": ["D.54", "D.55"],
        "cases": cases,
        "case_count": len(cases),
        "all_assertions_passed": True,
        "scope": (
            "Exact covering-chain and homology calculations over F2/F3. "
            "The maps in the proofs identify the forced module for an invariant "
            "character with this averaging and boundary structure. The certificate "
            "constructs no full hypothetical automorphism and makes no finite-to-full "
            "recognition inference."
        )
    }
    Path(__file__).with_name("torus_cover_norm_d54_d55_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
