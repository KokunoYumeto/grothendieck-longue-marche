#!/usr/bin/env python3
"""Independent finite audit of the A137 geometric quotient's class.

This does not import the cover-graph certificate.  It computes powers of
the augmentation ideal of F2[P] and traces a literal free-group word on
the Cayley cover.  The mathematical identification of the path-chain
kernel with H^2[H,H] is supplied in the proof, not assumed from these tests.
"""
from pathlib import Path
import json


def enc(a, b, k):
    return a % 4 + 4 * (b % 4) + 16 * (k % 8)


def dec(g):
    return g % 4, (g // 4) % 4, g // 16


def mul(g, h):
    a, b, k = dec(g)
    c, d, l = dec(h)
    if k & 1:
        c, d = d, c
    return enc(a + c, b + d, k + l)


P = range(128)
X, Y = enc(1, 0, 0), enc(0, 0, 1)
INV = [next(h for h in P if mul(g, h) == mul(h, g) == 0) for g in P]


def permute(v, g):
    ans = 0
    while v:
        bit = v & -v
        ans ^= 1 << mul(g, bit.bit_length() - 1)
        v ^= bit
    return ans


def row_basis(rows):
    pivots = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p] = row
                break
    return list(pivots.values())


def subgroup(generators):
    gens = list(generators)
    seen, queue = {0}, [0]
    while queue:
        g = queue.pop()
        for h in gens:
            k = mul(g, h)
            if k not in seen:
                seen.add(k)
                queue.append(k)
    return seen


def powg(g, n):
    ans = 0
    for _ in range(n):
        ans = mul(ans, g)
    return ans


def cg(g, h):
    return mul(mul(mul(g, h), INV[g]), INV[h])


def inv_word(w):
    return [-l for l in reversed(w)]


def comm_word(w, v):
    return w + v + inv_word(w) + inv_word(v)


def trace_word(word):
    g, vx, vy = 0, 0, 0
    for letter in word:
        target = X if abs(letter) == 1 else Y
        if letter > 0:
            source = g
            g = mul(g, target)
        else:
            g = mul(g, INV[target])
            source = g
        if abs(letter) == 1:
            vx ^= 1 << source
        else:
            vy ^= 1 << source
    return g, vx, vy


def main():
    assert len(subgroup([X, Y])) == 128
    c = cg(X, Y)
    gamma2 = subgroup([c])
    gamma3 = subgroup([cg(g, h) for g in gamma2 for h in (X, Y)])
    gamma4 = subgroup([cg(g, h) for g in gamma3 for h in (X, Y)])
    assert (len(gamma2), len(gamma3), len(gamma4)) == (4, 2, 1)
    d2 = subgroup([powg(g, 2) for g in P] + [c])
    d3 = subgroup([powg(g, 4) for g in P] +
                  [powg(g, 2) for g in gamma2] + list(gamma3))
    d4 = subgroup([powg(g, 4) for g in P] +
                  [powg(g, 2) for g in gamma2])
    d5 = subgroup([powg(g, 8) for g in P] +
                  [powg(g, 4) for g in gamma2] +
                  [powg(g, 2) for g in gamma3])
    assert (len(d2), len(d3), len(d4), len(d5)) == (32, 4, 4, 1)
    print("PASS: P has order128 and class3; its dimension-subgroup orders are 128,32,4,4,1.")

    basis = [1 << g for g in P]
    dimensions = [len(basis)]
    degree = 0
    while basis:
        basis = row_basis([v ^ permute(v, g) for v in basis for g in (X, Y)])
        degree += 1
        dimensions.append(len(basis))
        assert degree <= 18
    assert dimensions[-2:] == [1, 0] and degree == 17
    print("Augmentation-ideal dimensions I^0,...,I^17:", dimensions)
    hilbert = [1]
    for weight in (1, 1, 2, 2, 2, 4, 4):
        nxt = [0] * (len(hilbert) + weight)
        for i, coefficient in enumerate(hilbert):
            nxt[i] += coefficient
            nxt[i + weight] += coefficient
        hilbert = nxt
    assert [dimensions[k] - dimensions[k + 1] for k in range(17)] == hilbert
    print("Associated-graded dimensions:", hilbert)
    print("PASS: exact coefficient agreement with (1+t)^2(1+t^2)^3(1+t^4)^2.")
    print("PASS: I^17=0; I^16 has dimension1.  The Fox-chain weight bound gives Gamma18(Q)=1.")

    w = comm_word([1], [2])
    w = comm_word(w, [1])
    w = comm_word(w, [1])
    tail = "XXYXYXYYYYYYY"
    for letter in tail:
        w = comm_word(w, [1] if letter == "X" else [2])
    endpoint, vx, vy = trace_word(w)
    assert len(tail) == 13
    assert endpoint == 0 and vx == (1 << 128) - 1 and vy == 0
    print("PASS: the literal weight17 commutator has all128 X-edges and no Y-edges.")
    print("Unreduced free-word length:", len(w))
    print("EXACT CLASS17: upper bound from the group-ring calculation and lower bound from the literal word.")
    Path(__file__).with_name("harmonic_quotient_augmentation_audit_data.json").write_text(
        json.dumps({"augmentation_dimensions": dimensions,
                    "associated_graded_dimensions": hilbert,
                    "witness_weight": 17, "witness_seed": "[[[X,Y],X],X]",
                    "witness_tail": tail, "word_length": len(w),
                    "x_chain_hex": hex(vx), "y_chain_hex": hex(vy)}, indent=2) + "\n")


if __name__ == "__main__":
    main()
