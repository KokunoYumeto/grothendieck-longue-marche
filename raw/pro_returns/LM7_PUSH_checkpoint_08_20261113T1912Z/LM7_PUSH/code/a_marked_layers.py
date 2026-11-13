#!/usr/bin/env python3
"""Exact rank certificates for the marked depth-two lower-central layers.

The theorem is the integral semidirect/augmentation proof in A.44.
This script independently enumerates Lyndon words through degree five,
counts the permitted marked-letter depths, and compares the resulting
ordinary free-Lie ranks with the tensor/wedge formula.  No field or
floating-point arithmetic enters.
"""

from collections import Counter
from itertools import product
import json
from pathlib import Path


def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign


def witt_rank(alphabet_size, degree):
    numerator = sum(
        mobius(d) * alphabet_size ** (degree // d)
        for d in range(1, degree + 1)
        if degree % d == 0
    )
    assert numerator % degree == 0
    return numerator // degree


def marked_parts(degree):
    depth0 = witt_rank(9, degree)
    depth1 = 9 ** (degree - 1)
    if degree == 1:
        depth2 = 0
    else:
        ordered = (degree - 1) * 9 ** (degree - 2)
        diagonal = 9 ** (degree // 2 - 1) if degree % 2 == 0 else 0
        assert (ordered - diagonal) % 2 == 0
        depth2 = (ordered - diagonal) // 2
    return [depth0, depth1, depth2]


def is_lyndon(word):
    return all(word < word[k:] + word[:k] for k in range(1, len(word)))


def enumerate_lyndon(degree):
    counts = Counter()
    for word in product(range(10), repeat=degree):
        if is_lyndon(word):
            counts[word.count(9)] += 1
    assert sum(counts.values()) == witt_rank(10, degree)
    return counts


def independent_wedge_count(degree):
    # The two tensor words have lengths a,b and total ordinary degree a+b+2.
    count = 0
    for a in range(max(0, degree - 1)):
        b = degree - 2 - a
        if a > b:
            continue
        if a < b:
            count += sum(1 for _ in product(range(9), repeat=a + b))
        else:
            words = list(product(range(9), repeat=a))
            count += sum(1 for i, _ in enumerate(words) for _ in words[i + 1 :])
    return count


def main():
    records = []
    print("Integral marked depth-two layer rank certificate")
    print("r | depth0 | depth1 | depth2 | marked rank | full rank | removed")
    for degree in range(1, 11):
        parts = marked_parts(degree)
        total = sum(parts)
        full = witt_rank(10, degree)
        row = {
            "degree": degree,
            "depth_parts": parts,
            "marked_rank": total,
            "full_rank": full,
            "removed_rank": full - total,
        }
        print(degree, *parts, total, full, full - total, sep=" | ")
        if degree <= 5:
            counts = enumerate_lyndon(degree)
            assert [counts[i] for i in range(3)] == parts
            assert independent_wedge_count(degree) == parts[2]
            row["enumerated_lyndon_counts_by_marked_depth"] = dict(sorted(counts.items()))
            row["enumeration_checked"] = True
        records.append(row)
    assert [row["marked_rank"] for row in records[1:4]] == [45, 330, 2466]
    assert records[3]["removed_rank"] == 9
    payload = {
        "status": "PASS",
        "coefficient_ring": "Z_3; all ranks checked with exact integer arithmetic",
        "group": "F_3(10)/gamma_3(normal_closure(marked generator))",
        "proof": "A.44, integral class-two normal-closure model and augmentation filtration",
        "independent_enumeration_max_degree": 5,
        "records": records,
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(payload, indent=2) + "\n")
    print("PASS: all ordinary Lyndon and tensor/wedge counts agree through degree five.")


if __name__ == "__main__":
    main()
