#!/usr/bin/env python3
"""Exact supplementary Sidon certificate for the e=19 A6 family.

Input conductors are the already independently verified AG.34 list.  For
each conductor, construct H=<-2^19,-1> in (Z/n)^* and test every ordered
nonzero difference in {0} union H.  A theta curve on a principally
polarized genus-two Jacobian permits at most two representations.
No finite-field arithmetic, floating point, or external package is used.
"""
from collections import defaultdict
import json
from pathlib import Path


def subgroup(n):
    generators = [(-pow(2, 19, n)) % n, n - 1]
    seen = {1}
    queue = [1]
    for a in queue:
        for g in generators:
            b = a * g % n
            if b not in seen:
                seen.add(b)
                queue.append(b)
    return sorted(seen)


def main():
    candidates = [191, 229, 361, 419, 457, 571, 573, 647, 687,
                  955, 1083, 1257, 1371]
    rows = []
    for n in candidates:
        H = subgroup(n)
        S = [0] + H
        differences = defaultdict(list)
        for a in S:
            for b in S:
                if a != b:
                    differences[(a - b) % n].append([a, b])
        failures = {str(d): pairs for d, pairs in sorted(differences.items())
                    if len(pairs) > 2}
        rows.append({
            "n": n,
            "H": H,
            "H_size": len(H),
            "maximum_nonzero_difference_multiplicity":
                max(map(len, differences.values())),
            "all_failing_differences_with_all_ordered_pairs": failures,
            "passes_necessary_Sidon_test": not failures,
        })
    surviving = [r["n"] for r in rows if r["passes_necessary_Sidon_test"]]
    assert surviving == [191, 229, 457, 1257]
    result = {
        "status": "exact necessary-condition certificate, not a chosen curve parameter",
        "e": 19,
        "input_conductors": candidates,
        "surviving_conductors": surviving,
        "rows": rows,
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    for r in rows:
        print(f'n={r["n"]}: |H|={r["H_size"]}, '
              f'max={r["maximum_nonzero_difference_multiplicity"]}, '
              f'passes={r["passes_necessary_Sidon_test"]}')
    print("surviving conductors:", surviving)
    print("certificate:", target)


if __name__ == "__main__":
    main()
