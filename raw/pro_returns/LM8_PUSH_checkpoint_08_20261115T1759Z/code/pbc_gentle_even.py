"""Exact low-weight diagnostic for special S3-invariant outer derivations.

This computes only a graded Lie algebra and its graded abelianization.
It makes no inference of a full profinite character from a graded class.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import gcd, lcm
from pathlib import Path
import argparse
import json
import time

import numpy as np
import sympy as sp

parser = argparse.ArgumentParser()
parser.add_argument("--max-weight", type=int, default=10)
args = parser.parse_args()
started = time.monotonic()
PRIME = 65521

def add(*polynomials):
    out = defaultdict(int)
    for p in polynomials:
        for w, c in p.items():
            out[w] += c
    return {w: c for w, c in out.items() if c}

def scale(p, c):
    return {w: v*c for w, v in p.items() if v*c}

def mul(p, q):
    out = defaultdict(int)
    for w, a in p.items():
        for v, b in q.items():
            out[w+v] += a*b
    return {w: c for w, c in out.items() if c}

def bracket(p, q):
    return add(mul(p, q), scale(mul(q, p), -1))

def lyndon(w):
    return all(w < w[i:] for i in range(1, len(w)))

@lru_cache(None)
def standard(w):
    if len(w) == 1:
        return {w: 1}
    assert lyndon(w)
    for i in range(1, len(w)):
        if lyndon(w[i:]):
            return bracket(standard(w[:i]), standard(w[i:]))
    raise AssertionError(w)

def subst(p, xx, yy):
    out = {}
    for w, c in p.items():
        term = {"": c}
        for letter in w:
            term = mul(term, xx if letter == "x" else yy)
        out = add(out, term)
    return out

x, y = {"x": 1}, {"y": 1}
z = {"x": -1, "y": -1}
xy = {"x": 1, "y": 1}

def constraints(f):
    return [
        add(f, subst(f, y, x)),
        add(bracket(x, f), scale(bracket(xy, subst(f, z, y)), -1)),
        add(f, subst(f, y, z), subst(f, z, x)),
    ]

def derivation(f, g):
    yy = bracket(y, f)
    out = defaultdict(int)
    for w, c in g.items():
        for i, letter in enumerate(w):
            if letter == "y":
                for v, d in yy.items():
                    out[w[:i]+v+w[i+1:]] += c*d
    return {w: c for w, c in out.items() if c}

def ihara(f, g):
    return add(bracket(f, g), derivation(f, g), scale(derivation(g, f), -1))

def coordinates(p, words):
    rest = dict(p)
    answer = []
    for w in words:
        c = rest.get(w, 0)
        answer.append(c)
        if c:
            rest = add(rest, scale(standard(w), -c))
    assert not rest
    return answer

def independent_rows_mod_p(array):
    matrix = np.remainder(array, PRIME).copy()
    row_names = list(range(matrix.shape[0]))
    rank = 0
    for col in range(matrix.shape[1]):
        candidates = np.flatnonzero(matrix[rank:, col])
        if not len(candidates):
            continue
        pivot = rank + int(candidates[0])
        if pivot != rank:
            matrix[[rank, pivot]] = matrix[[pivot, rank]]
            row_names[rank], row_names[pivot] = row_names[pivot], row_names[rank]
        matrix[rank] = matrix[rank] * pow(int(matrix[rank, col]), -1, PRIME) % PRIME
        factors = matrix[rank+1:, col].copy()
        active = np.flatnonzero(factors)
        if len(active):
            rows = active + rank + 1
            matrix[rows] = (matrix[rows] - factors[active, None] * matrix[rank]) % PRIME
        rank += 1
        if rank == matrix.shape[0]:
            break
    return row_names[:rank]

spaces = {}
results = []
for weight in range(2, args.max_weight + 1):
    words = ["".join(w) for w in product("xy", repeat=weight)
             if lyndon("".join(w))]
    polynomials = [standard(w) for w in words]
    columns = [constraints(f) for f in polynomials]
    row_keys = sorted({(family, w)
                       for col in columns
                       for family, p in enumerate(col)
                       for w in p})
    row_index = {key: i for i, key in enumerate(row_keys)}
    array = np.zeros((len(row_keys), len(words)), dtype=np.int64)
    for j, column in enumerate(columns):
        for family, p in enumerate(column):
            for w, c in p.items():
                array[row_index[family, w], j] = c
    selected = independent_rows_mod_p(array)
    square = sp.Matrix(array[selected].tolist())
    rational_kernel = square.nullspace()
    integer_kernel = []
    basis = []
    for vector in rational_kernel:
        denominator = lcm(*(int(c.q) for c in vector))
        v = [int(c*denominator) for c in vector]
        common = gcd(*v)
        v = [c//common for c in v]
        f = add(*(scale(p, c) for p, c in zip(polynomials, v) if c))
        assert all(not p for p in constraints(f))
        integer_kernel.append(v)
        basis.append(f)
    # Mod-p rank is a lower bound for rational rank.  Every vector in the
    # selected-row rational kernel satisfies ALL original rows, proving
    # equality and the exact dimension, without modular reconstruction.
    assert len(selected) + len(basis) == len(words)
    bracket_vectors = []
    bracket_pairs = []
    for a in range(2, weight//2 + 1):
        b = weight-a
        if a not in spaces or b not in spaces:
            continue
        for i, f in enumerate(spaces[a]["basis"]):
            for j, g in enumerate(spaces[b]["basis"]):
                if a == b and i >= j:
                    continue
                h = ihara(f, g)
                assert all(not q for q in constraints(h))
                if h:
                    bracket_vectors.append(coordinates(h, words))
                    bracket_pairs.append([a, i, b, j])
    bracket_matrix = sp.Matrix.hstack(
        *(sp.Matrix(v) for v in bracket_vectors)
    ) if bracket_vectors else sp.zeros(len(words), 0)
    bracket_rank = bracket_matrix.rank()
    indecomposable = len(basis)-bracket_rank
    example = None
    if weight % 2 == 0 and indecomposable:
        for v in integer_kernel:
            if bracket_matrix.row_join(sp.Matrix(v)).rank() > bracket_rank:
                example = [[w, c] for w, c in zip(words, v) if c]
                break
        assert example is not None
    row = {
        "weight": weight,
        "free_lie_dimension": len(words),
        "constraint_rank": len(selected),
        "gentle_dimension": len(basis),
        "bracket_rank": bracket_rank,
        "indecomposable_dimension": indecomposable,
        "standard_lyndon_words": words,
        "integral_basis_coordinates": integer_kernel,
        "bracket_pairs": bracket_pairs,
        "bracket_coordinates": bracket_vectors,
        "even_indecomposable_example": example,
        "exact_all_row_check": True,
    }
    results.append(row)
    spaces[weight] = {"basis": basis}
    print(json.dumps({k: row[k] for k in [
        "weight", "free_lie_dimension", "gentle_dimension",
        "bracket_rank", "indecomposable_dimension",
    ]}), "seconds", round(time.monotonic()-started, 3), flush=True)
    Path(__file__).with_suffix(".json").write_text(json.dumps({
        "scope": "graded special S3-invariant derivations only; no full character assertion",
        "rank_verification_prime": PRIME,
        "weights": results,
    }, indent=2) + "\n")
