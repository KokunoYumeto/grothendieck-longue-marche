#!/usr/bin/env python3
"""Bounded, exact sanity checks for family 008, Proposition 4.1.

This is NOT a verification of the all-weight estimate or a Lean proof.
We retain the nine rational B3 hyperplanes separately before reduction mod 2.
Run from the deliverable directory: python code/e_deletion_checks.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import gcd
from pathlib import Path
import json

H = {
    "z1": (1, 0, 0), "z2": (0, 1, 0), "z3": (0, 0, 1),
    "z1-z2": (1, -1, 0), "z1+z2": (1, 1, 0),
    "z1-z3": (1, 0, -1), "z1+z3": (1, 0, 1),
    "z2-z3": (0, 1, -1), "z2+z3": (0, 1, 1),
}
# Letters: 0, e=1, p=(z2-z3)/(z2+z3); right endpoint w=(z2-z1)/(z2+z1).
edge = {
    frozenset(("0", "e")): {},
    frozenset(("0", "p")): {"z2-z3": 1, "z2+z3": -1},
    frozenset(("0", "w")): {"z1-z2": 1, "z1+z2": -1},
    frozenset(("e", "p")): {"z3": 1, "z2+z3": -1},
    frozenset(("e", "w")): {"z1": 1, "z1+z2": -1},
    frozenset(("p", "w")): {
        "z2": 1, "z1-z3": 1, "z2+z3": -1, "z1+z2": -1,
    },
}

def valuation(a, b, hyperplane):
    # The prescription for equal adjacent letters in the source is zero.
    return 0 if a == b else edge[frozenset((a, b))].get(hyperplane, 0)

def delete(hyperplane, word):
    out = defaultdict(int)
    ext = ("0",) + word + ("w",)
    for j in range(len(word)):
        coefficient = (valuation(ext[j+1], ext[j+2], hyperplane)
                       - valuation(ext[j], ext[j+1], hyperplane))
        out[word[:j] + word[j+1:]] += coefficient
    return {k: v for k, v in out.items() if v}

def apply(hyperplanes, vector):
    out = defaultdict(int)
    for word, coefficient in vector.items():
        for hyperplane in hyperplanes:
            for shorter, weight in delete(hyperplane, word).items():
                out[shorter] += coefficient * weight
    return {k: v for k, v in out.items() if v}

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def normalize(v):
    common = 0
    for x in v:
        common = gcd(common, abs(x))
    w = tuple(x // common for x in v)
    return tuple(-x for x in w) if next(x for x in w if x) < 0 else w

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def deletion_check(max_length=5):
    flats = sorted({normalize(cross(a, b)) for a, b in combinations(H.values(), 2)})
    relation_count = 0
    word_count = sum(3**n for n in range(max_length + 1))
    for flat in flats:
        contained = tuple(name for name, normal in H.items() if dot(flat, normal) == 0)
        for distinguished in contained:
            for n in range(max_length + 1):
                for word in product(("0", "e", "p"), repeat=n):
                    # [T_H, sum_{H' containing flat} T_H'] on the word.
                    left = apply((distinguished,), apply(contained, {word: 1}))
                    right = apply(contained, apply((distinguished,), {word: 1}))
                    if left != right:
                        raise AssertionError((flat, distinguished, word, left, right))
                    relation_count += 1
    return {
        "hyperplanes_over_Q": len(H), "rank_two_flats": len(flats),
        "max_word_length": max_length, "number_of_words": word_count,
        "integer_commutator_instances": relation_count, "failures": 0,
        "interpretation": "Exact bounded deletion-representation check only; no all-weight proof.",
    }

def multiply(a, b, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b[:degree+1-i]):
                if bj:
                    out[i+j] += ai*bj
    return out

def mobius(n):
    factors = 0
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            factors += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors += 1
    return -1 if factors % 2 else 1

def free_lie_dimensions(degree=30):
    # PBW: -log(1-v(t))=sum_n (sum_{d|n} d*l_d) t^n/n.
    v = [Fraction(int(n >= 3 and n % 2 == 1)) for n in range(degree + 1)]
    log = [Fraction(0) for _ in range(degree + 1)]
    power = [Fraction(0) for _ in range(degree + 1)]
    power[0] = Fraction(1)
    for k in range(1, degree // 3 + 1):
        power = multiply(power, v, degree)
        for n in range(degree + 1):
            log[n] += power[n] / k
    weighted = [n * log[n] for n in range(degree + 1)]
    dims = {}
    for n in range(1, degree + 1):
        dimension = sum(mobius(d) * weighted[n//d] for d in range(1, n+1) if n % d == 0) / n
        assert dimension.denominator == 1 and dimension >= 0
        dims[str(n)] = int(dimension)
    return dims

def finite_counterexample():
    # C2 has a nontrivial finite quotient, unlike 1. Every homomorphism
    # from C2 to a characteristic-zero unipotent group is trivial because
    # the target is torsion-free (the mathematical argument is in E.23).
    table = [[(a+b) % 2 for b in range(2)] for a in range(2)]
    for a, b, c in product(range(2), repeat=3):
        assert table[table[a][b]][c] == table[a][table[b][c]]
    return {"C2_table": table, "identity": 0, "nonidentity": 1,
            "nonidentity_square": table[1][1],
            "finite_groups_distinct": True,
            "unipotent_completion_triviality": "Proved in E.23, not inferred by this finite check."}

if __name__ == "__main__":
    result = {"deletion": deletion_check(), "free_lie_dimensions": free_lie_dimensions(),
              "completion_counterexample": finite_counterexample()}
    target = Path(__file__).resolve().parents[1] / "audit" / "E_computation.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
