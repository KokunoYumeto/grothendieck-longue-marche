"""Reproduce the page-005 finite checks recorded in math_checks.json.

This script uses only Python's standard library. It enumerates labelled partial
orders on three elements and checks the stated closed-downset lemma, computes
the two-point topology counterexample, and checks the three-set fork example.
Run from any directory with: python /absolute/path/to/math_checks.py
The JSON record is written beside this script. The script was preserved after
the original successful calculation; it was not rerun during preservation.
"""
from itertools import product
import json
from pathlib import Path


def main():
    I = frozenset(range(3))
    allsets = [frozenset(i for i in I if m >> i & 1) for m in range(8)]
    edges = [(i, j) for i in I for j in I if i != j]
    count = 0
    examples = []
    posetcount = 0
    for bits in product((0, 1), repeat=len(edges)):
        relation = {(i, i) for i in I} | {e for e, b in zip(edges, bits) if b}
        if any(i != j and (j, i) in relation for i, j in relation):
            continue
        if any((i, k) not in relation for i, j in relation
               for jj, k in relation if j == jj):
            continue
        posetcount += 1
        down = {j: frozenset(i for i in I if (i, j) in relation) for j in I}
        closed = [K for K in allsets if all(down[j] <= K for j in K)]
        for J in allsets:
            if J in closed:
                continue
            if any((K & J) not in closed and not J <= K for K in closed):
                continue
            count += 1
            maxima = [j for j in J if J <= down[j]]
            assert len(maxima) == 1
            j = maxima[0]
            J0 = J - {j}
            union = frozenset().union(*(down[k] for k in J0))
            assert J0 in closed and J0 == union and not down[j] <= J
            assert any((i, j) in relation and i != j and i not in J0 for i in I)
            if len(examples) < 3:
                examples.append({"order": sorted(relation), "J": sorted(J),
                                 "j": j, "J0": sorted(J0)})

    X = frozenset({0, 1})
    B = frozenset({0})
    open_X = {frozenset(), X}
    open_Y = {frozenset(), frozenset({0}), frozenset({1}), X}
    closed_X = {X - U for U in open_X}
    closed_Y = {X - U for U in open_Y}

    def closure(A, closed):
        return frozenset.intersection(*(C for C in closed if A <= C))

    assert all(U in open_Y for U in open_X)
    assert closure(B, closed_Y) != closure(B, closed_X)
    family = {"a": frozenset({"a"}), "b": frozenset({"b"}),
              "c": frozenset({"a", "b"})}
    order = {(u, v) for u in family for v in family if family[u] <= family[v]}
    assert order == {("a", "a"), ("b", "b"), ("c", "c"),
                     ("a", "c"), ("b", "c")}
    assert not (family["c"] - (family["a"] | family["b"]))
    record = {
        "finite_poset_check": {
            "posets": posetcount,
            "qualifying_nonclosed_J": count,
            "failures": 0,
            "sample_cases": examples,
        },
        "open_map_counterexample": {
            "X_topology": [sorted(U) for U in open_X],
            "Y_topology": [sorted(U) for U in open_Y],
            "B": sorted(B),
            "inverse_image_closure_B": sorted(closure(B, closed_Y)),
            "closure_inverse_image_B": sorted(closure(B, closed_X)),
        },
        "fork_example": {"inclusion_pairs": sorted(order), "c_star": []},
    }
    output = Path(__file__).resolve().with_name("math_checks.json")
    output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record))


if __name__ == "__main__":
    main()
