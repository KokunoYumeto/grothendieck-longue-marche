#!/usr/bin/env python3
"""Independent nonincremental check of the criteria agent's packet search."""
from collections import Counter
from math import gcd
import json
from pathlib import Path


def generate(n, generators):
    out = {1}
    while True:
        new = out | {a*b % n for a in out for b in generators}
        if new == out:
            return out
        out = new


def partition(n, ambient, subgroup):
    unseen = set(ambient)
    parts = []
    while unseen:
        representative = min(unseen)
        part = {representative*h % n for h in subgroup}
        assert part <= unseen
        parts.append(part)
        unseen -= part
    return parts


def review(n):
    units = {a for a in range(n) if gcd(a, n) == 1}
    H = generate(n, [pow(2, 19, n), n-1])
    D = generate(n, [2, n-1])
    packets = [partition(n, orbit, H) for orbit in partition(n, units, D)]
    counts = [0]*len(packets)
    tested = [0]*len(packets)

    def search(chosen, indices):
        depth = len(indices)
        counts[depth-1] += 1
        if depth == len(packets):
            return indices, sorted(chosen)
        for i, part in enumerate(packets[depth]):
            tested[depth] += 1
            enlarged = chosen | part
            ds = Counter((a-b) % n for a in enlarged for b in enlarged if a != b)
            if max(ds.values()) <= 2:
                result = search(enlarged, indices+[i])
                if result is not None:
                    return result
        return None

    answer = search({0} | H, [0])
    expected = n in (457, 1257)
    assert (answer is None) == expected
    if n == 457:
        assert counts == [1, 17, 226, 879, 262, 0]
    return {"n": n, "excluded": answer is None,
            "nodes_by_depth": counts, "tested_by_depth": tested,
            "compatible_configuration_if_any": answer}


if __name__ == "__main__":
    rows = [review(n) for n in (191, 229, 457, 1257)]
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(rows, indent=2)+"\n")
    print(json.dumps(rows, indent=2))
