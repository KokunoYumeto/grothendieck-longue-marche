#!/usr/bin/env python3
"""Exact finite certificates for D.50's maps and local square obstruction."""
import json
from pathlib import Path


def reduce_word(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inverse(word):
    return tuple(-a for a in word[::-1])


def substitute(word, images):
    out = ()
    for a in word:
        b = images[abs(a) - 1]
        out = reduce_word(out + (b if a > 0 else inverse(b)))
    return out


def compose(a, b):
    return tuple(substitute(w, a) for w in b)


def power(a, n):
    z = ((1,), (2,))
    for _ in range(n):
        z = compose(z, a)
    return z


def matrix(a):
    return tuple(tuple(w.count(i) - w.count(-i) for w in a)
                 for i in (1, 2))


def main():
    identity = ((1,), (2,))
    r = ((2,), (-1,))
    s = ((2,), (1,))
    c = (1, 2, -1, -2)
    assert power(r, 4) == identity
    assert power(s, 2) == identity
    assert compose(s, compose(r, s)) == power(r, 3)
    assert substitute(c, r) == reduce_word((-1,) + c + (1,))
    assert substitute(c, s) == inverse(c)
    elements = [compose(power(r, i), power(s, j))
                for i in range(4) for j in range(2)]
    matrices = [matrix(a) for a in elements]
    assert len(set(elements)) == len(set(matrices)) == 8
    v4 = [identity, power(r, 2), s, compose(power(r, 2), s)]
    assert len(set(v4)) == 4
    assert all(power(a, 2) == identity for a in v4)
    square_checks = []
    for u in range(8):
        for v in range(8):
            if not (u % 2 or v % 2):
                continue
            value = (u*u + v*v) % 8
            if u % 2 and v % 2:
                assert value == 2
            else:
                assert value % 4 == 1
            assert value != 7
            square_checks.append((u, v, value))
    assert len(square_checks) == 48
    result = {
        "claim": "D.50",
        "abstract_types": ["1", "C2", "C4", "C2 x C2", "D8 (order 8)"],
        "actual_free_word_relations": {
            "r^4": True, "s^2": True, "s r s = r^-1": True,
            "r(c) = x^-1 c x": True, "s(c) = c^-1": True,
        },
        "eight_distinct_homology_matrices": matrices,
        "explicit_V4_size": len(set(v4)),
        "unit_residue_square_checks": len(square_checks),
        "no_unit_residue_pair_sums_to_minus_one_modulo_eight": True,
        "scope": (
            "Finite checks of the displayed free words and residue identities. "
            "The full Q2 obstruction uses the proved minimum-valuation argument; "
            "D33 supplies primary homology faithfulness. No conjugacy or arbitrary "
            "cyclic C4 global multiplier conclusion is inferred."
        ),
    }
    Path(__file__).with_name("torus_two_subgroups_d50_output.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
