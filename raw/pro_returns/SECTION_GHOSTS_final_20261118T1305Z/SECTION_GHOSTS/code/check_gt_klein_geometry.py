#!/usr/bin/env python3
"""Exact finite and polynomial certificates for E.177--E.179.

This does not test a GT source census or certify the Tate-cover argument.
It verifies the labelled 32-element centralizer, the two fixed components,
the common four-point coordinate, and the actual Schreier substitutions.
Only the Python standard library is used.
"""
from itertools import product
from pathlib import Path
import hashlib
import json


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def permutation(bits):
    ea, eb, ec, ta, tb = bits
    out = list(range(10))
    for start, bit in ((0, ea), (2, eb), (4, ec)):
        if bit:
            out[start], out[start + 1] = out[start + 1], out[start]
    for h in range(4):
        out[6 + h] = 6 + (h ^ ta ^ (2 * tb))
    return tuple(out)


IDENTITY = tuple(range(10))
A = permutation((0, 1, 1, 1, 0))
B = permutation((1, 0, 1, 0, 1))
H = {IDENTITY, A, B, compose(A, B)}
centralizer = {permutation(bits): bits for bits in product(range(2), repeat=5)}
assert len(centralizer) == 32
assert all(compose(p, A) == compose(A, p) and compose(p, B) == compose(B, p)
           for p in centralizer)

# Independent exhaustive enumeration from equivariance of each orbit.
# Each of the three two-point orbits has its own stabilizer.  The
# regular orbit has four choices for the image of its chosen point.
independent = set()
orbits = ((0, 1), (2, 3), (4, 5), (6, 7, 8, 9))
for images in product(*orbits):
    q = [None] * 10
    for orbit, image in zip(orbits, images):
        seed = orbit[0]
        for h in H:
            q[h[seed]] = h[image]
    assert all(v is not None for v in q)
    independent.add(tuple(q))
assert independent == set(centralizer)

actions = {}
for p, (ea, eb, ec, ta, tb) in centralizer.items():
    # z -> (-1)^sign * z^(+/-1), delta -> (-1)^component * delta.
    actions[p] = ((eb + ta) % 2, (ea + tb) % 2, (ea + eb + ec) % 2)
assert {p for p, action in actions.items() if action == (0, 0, 0)} == H
positive = {p for p in centralizer if actions[p][2] == 0}
assert len(positive) == 16
assert len({actions[p][:2] for p in positive}) == 4

theta = permutation((0, 0, 1, 0, 0))
assert actions[theta] == (0, 0, 1)
block_b, block_a = {6, 8}, {6, 7}
nb = {p for p in positive if {p[i] for i in block_b} == block_b}
na = {p for p in positive if {p[i] for i in block_a} == block_a}
assert len(nb) == len(na) == 8
assert H & nb == {IDENTITY, B}
assert H & na == {IDENTITY, A}
assert {compose(h, n) for h in H for n in nb} == positive
assert {compose(h, n) for h in H for n in na} == positive
assert all(theta[i] == i for i in {0, 1, 2, 3, 6, 7, 8, 9})


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    out = [0] * max(len(p), len(q))
    for i, v in enumerate(p):
        out[i] += v
    for i, v in enumerate(q):
        out[i] += v
    return trim(out)


def scale(p, a):
    return trim([a * v for v in p])


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, v in enumerate(p):
        for j, w in enumerate(q):
            out[i + j] += v * w
    return trim(out)


def power(p, n):
    out = (1,)
    for _ in range(n):
        out = mul(out, p)
    return out


zm, zp = (-1, 1), (1, 1)
num_r = add(power(zm, 4), power(zp, 4))
den_r = mul(power(zm, 2), power(zp, 2))
num_u, den_u = (1, 0, 0, 0, 1), (0, 0, 1)
num_t = scale(add(num_u, scale(den_u, 6)), 2)
den_t = add(num_u, scale(den_u, -2))
assert mul(num_r, den_t) == mul(num_t, den_r)
assert mul((-1, -2, 1), (-1, 2, 1)) == (1, 0, -6, 0, 1)


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


T = ((2, 12), (1, -2))
W = ((1, -6), (1, 2))
reflection = ((-1, 0), (0, 1))
assert matmul(T, T) == ((16, 0), (0, 16))
assert matmul(W, T) == tuple(tuple(4 * x for x in row)
                            for row in matmul(reflection, W))

# Reduced words in C2(a) * Z(d): a is encoded by 0, d by 1, d^-1 by -1.
def reduce_word(word):
    stack = []
    for letter in word:
        if stack and ((letter == 0 and stack[-1] == 0)
                      or (letter != 0 and stack[-1] == -letter)):
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse(word):
    return tuple(0 if x == 0 else -x for x in reversed(word))


def multiply(*words):
    return reduce_word(sum((tuple(w) for w in words), ()))


d, v = (1,), (0, -1)
X, Y = v, (1, 1)
assert multiply(v, d, v, d) == ()
assert multiply(d, v, inverse(d)) == multiply(inverse(v), inverse(Y))
schreier = [
    multiply(d, d),
    multiply(v, v),
    multiply(d, v, v, inverse(d)),
]
expected = [
    Y,
    multiply(X, X),
    multiply(inverse(X), inverse(Y), inverse(X), inverse(Y)),
]
assert schreier == expected

certificate = {
    "status": "PASS",
    "centralizer_order": len(centralizer),
    "component_count": 2,
    "component_stabilizer_order": len(positive),
    "parameter_action_order": len({actions[p][:2] for p in positive}),
    "fixed_locus_action_kernel": sorted(map(list, H)),
    "stabilizer_orders": {"N_b_labels": len(nb), "N_a_labels": len(na)},
    "all_label_records": [
        {"permutation": p, "bits": centralizer[p], "action": actions[p]}
        for p in sorted(centralizer)
    ],
    "coordinate_cross_products": list(mul(num_r, den_t)),
    "mobius_T": T,
    "mobius_W": W,
    "schreier_images": schreier,
    "scope": "Exact labelled geometry and word checks; no GT source census or topological proof certification.",
}
payload = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["data_sha256"] = hashlib.sha256(payload).hexdigest()
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
print(f"PASS: 32 label cases, two components, exact coordinate and Schreier identities; "
      f"SHA256 {certificate['data_sha256']}")
