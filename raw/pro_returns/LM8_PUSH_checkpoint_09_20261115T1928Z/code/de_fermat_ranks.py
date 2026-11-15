#!/usr/bin/env python3
"""Exact signed-permutation check of D.20's real homology dimensions.

The compact summand is a symplectic homology representation of complex
conjugation: g plus and g minus dimensions.  In the boundary summand we
omit one of the three real cusps.  The two remaining real loops have
sign -1; each nonreal conjugate pair is exchanged with sign -1.
Exterior squares are computed as actual signed permutations, not by
substituting into the claimed formula.
"""
import json
from pathlib import Path


def involution_eigenspaces(perm, signs):
    assert len(perm) == len(signs)
    seen = set()
    plus = minus = 0
    for i in range(len(perm)):
        assert perm[perm[i]] == i and signs[i] * signs[perm[i]] == 1
        if i in seen:
            continue
        j = perm[i]
        seen.update((i, j))
        if i == j:
            plus += signs[i] == 1
            minus += signs[i] == -1
        else:
            plus += 1
            minus += 1
    return plus, minus


def certificate(n):
    assert n >= 3 and n % 2
    genus = (n - 1) * (n - 2) // 2
    perm = list(range(2 * genus + 2))
    signs = [1] * genus + [-1] * (genus + 2)
    for _ in range((3 * n - 3) // 2):
        i = len(perm)
        perm.extend((i + 1, i))
        signs.extend((-1, -1))
    rank = len(perm)
    pairs = [(i, j) for i in range(rank) for j in range(i + 1, rank)]
    pair_index = {ij: k for k, ij in enumerate(pairs)}
    wedge_perm = []
    wedge_signs = []
    for i, j in pairs:
        a, b = perm[i], perm[j]
        sign = signs[i] * signs[j]
        if a > b:
            a, b = b, a
            sign = -sign
        wedge_perm.append(pair_index[(a, b)])
        wedge_signs.append(sign)
    vp, vm = involution_eigenspaces(perm, signs)
    wp, wm = involution_eigenspaces(wedge_perm, wedge_signs)
    expected = (n * n - 1) * (n * n + 3) // 4
    assert rank == n * n + 1
    assert vp == (n * n - 1) // 2
    assert vm == (n * n + 3) // 2
    assert wm == vp * vm == expected
    return {
        "n": n, "genus": genus, "cusps": 3 * n,
        "real_cusps": 3, "geometric_rank": rank,
        "V_plus": vp, "V_minus": vm,
        "wedge_rank": len(pairs), "wedge_plus": wp,
        "wedge_minus": wm, "d_n": expected,
        "actual_signed_permutation_verified": True,
    }


result = {
    "statement": "D.20",
    "arithmetic_scope": "Only verifies the exact real-action ranks; the arithmetic cocycle and Haar arguments are proved in D.tex.",
    "certificates": [certificate(n) for n in (3, 5, 9, 25)],
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
