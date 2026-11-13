#!/usr/bin/env python3
"""D.44 finite first-symmetry construction on every A5 factor orbit."""
from itertools import permutations
from collections import Counter
from pathlib import Path
import json


def multiply(g, h):
    return tuple(g[h[i]] for i in range(5))


def inverse(g):
    return tuple(g.index(i) for i in range(5))


def parity(g):
    return sum(g[i] > g[j] for i in range(5) for j in range(i+1, 5)) % 2


def main():
    symmetric = list(permutations(range(5)))
    one = tuple(range(5))
    alternating = [g for g in symmetric if parity(g) == 0]
    assert len(symmetric) == 120 and len(alternating) == 60
    ix = {g: i for i, g in enumerate(alternating)}
    identity = ix[one]
    mul = [[ix[multiply(g, h)] for h in alternating] for g in alternating]
    inv = [ix[inverse(g)] for g in alternating]
    conj = {g: [ix[multiply(multiply(g, t), inverse(g))]
                for t in alternating] for g in symmetric}
    involutions = [i for i in range(60) if i != identity and mul[i][i] == identity]
    involutory_symmetric = [g for g in symmetric if multiply(g, g) == one]
    assert len(involutions) == 15 and len(involutory_symmetric) == 26
    conjugators = {
        (t, v): [h for h in range(60) if mul[mul[inv[h]][t]][h] == v]
        for t in involutions for v in involutions
    }
    assert all(len(hs) == 4 for hs in conjugators.values())

    fixed_count, fixed_solution_histogram = 0, Counter()
    for g in involutory_symmetric:
        for t in involutions:
            if parity(g) == 0:
                v = one
            else:
                v = next(v for v in symmetric
                         if parity(v) and multiply(v, v) == one
                         and multiply(v, alternating[t]) == multiply(alternating[t], v))
            h = ix[multiply(v, inverse(g))]
            assert mul[mul[inv[h]][t]][h] == conj[g][t]
            assert mul[h][conj[g][h]] == identity
            solutions = [w for w in range(60)
                         if mul[mul[inv[w]][t]][w] == conj[g][t]
                         and mul[w][conj[g][w]] == identity]
            fixed_solution_histogram[len(solutions)] += 1
            fixed_count += 1

    pair_count, pair_solution_histogram = 0, Counter()
    for g in symmetric:
        gi = inverse(g)
        for ti in involutions:
            for tj in involutions:
                hs = conjugators[ti, conj[g][tj]]
                for hi in hs:
                    hj = conj[gi][inv[hi]]
                    assert mul[mul[inv[hi]][ti]][hi] == conj[g][tj]
                    assert mul[mul[inv[hj]][tj]][hj] == conj[gi][ti]
                    assert mul[hi][conj[g][hj]] == identity
                    assert mul[hj][conj[gi][hi]] == identity
                pair_solution_histogram[len(hs)] += 1
                pair_count += 1
    assert fixed_count == 390 and pair_count == 27000
    assert dict(fixed_solution_histogram) == {4: 240, 2: 150}
    assert dict(pair_solution_histogram) == {4: 27000}
    result = {
        "claim": "D.44",
        "fixed_factor_cases": fixed_count,
        "fixed_factor_solution_histogram": dict(sorted(fixed_solution_histogram.items())),
        "two_factor_cases": pair_count,
        "two_factor_solution_histogram": dict(sorted(pair_solution_histogram.items())),
        "equations": ["h^-1*t*h=theta(t)", "h*theta(h)=1"],
        "unsolved_cases": 0,
        "consequence_for_D38": "Every theta factor orbit of every triangle-surviving A5^19 tuple admits the finite first-symmetry solution. Hence all5062500 triangle survivors, including the2531250 failing the finite peripheral-conjugacy test, pass this additional finite equation.",
        "scope": "The global profinite existence is proved using the exact V4 normalizer in the text. This finite certificate establishes no lifting of arbitrary finite candidates."
    }
    Path(__file__).with_name("pure_involution_first_symmetry_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
