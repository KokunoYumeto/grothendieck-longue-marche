"""Independent small-factor certificate for the Burau F11 pentagon source.

Uses exact 3x3 projective matrices only. No group-theory package is imported.
The huge common derived source is certified as a product of four perfect
central extensions of simple groups by small enumerations and separating
word-order witnesses. The input matrices are mathematical definitions;
all relations and factor properties are recomputed.
"""
from collections import deque
import argparse
import json
from pathlib import Path
import time

parser = argparse.ArgumentParser()
parser.add_argument("--full-orbits", action="store_true")
args = parser.parse_args()
started = time.time()
outdir = Path(__file__).resolve().parent
suffix = "_orbits" if args.full_orbits else ""
data = json.loads((outdir / ("c_burau_11_2"+suffix+".json")).read_text())
p = 11
I = (1, 0, 0, 0, 1, 0, 0, 0, 1)


def canon(M):
    z = next(x for x in M if x)
    inverse = pow(z, -1, p)
    return tuple(x*inverse % p for x in M)


def mul(A, B):
    return canon(tuple(sum(A[3*i+k]*B[3*k+j] for k in range(3)) % p
                       for i in range(3) for j in range(3)))


def inv(A):
    a, b, c, d, e, f, g, h, i = A
    return canon(tuple(x % p for x in (e*i-f*h, c*h-b*i, b*f-c*e,
                                      f*g-d*i, a*i-c*g, c*d-a*f,
                                      d*h-e*g, b*g-a*h, a*e-b*d)))


S = [canon(tuple(M)) for M in data["braid_matrices"]]
assert mul(mul(S[0], S[1]), S[0]) == mul(mul(S[1], S[0]), S[1])
assert mul(mul(S[1], S[2]), S[1]) == mul(mul(S[2], S[1]), S[2])
assert mul(S[0], S[2]) == mul(S[2], S[0])
assert S[0] != S[2]
a, b, e = [mul(s, s) for s in S]
c, d = mul(mul(S[1], a), inv(S[1])), mul(mul(S[2], b), inv(S[2]))
initial = [(b, e), (mul(a, c), mul(d, e)), (a, b),
           (a, mul(b, d)), (mul(c, b), e)]
pairs = [(canon(tuple(x)), canon(tuple(y))) for x, y in data["evaluation_pairs"]]
assert pairs[:5] == initial
relations = data["relations"]
assert len(relations) == (30 if args.full_orbits else 5)
for relation in relations:
    x, y = pairs[relation["xy"]]
    z = inv(mul(x, y))
    assert pairs[relation["yx"]] == (y, x)
    assert pairs[relation["zx"]] == (z, x)
    assert pairs[relation["yz"]] == (y, z)


def tuplemul(A, B):
    return tuple(mul(a, b) for a, b in zip(A, B))


def tupleinv(A):
    return tuple(inv(a) for a in A)


def normal_closure(unit, seeds, conjugators, multiply, inverse):
    elements = {unit}
    queue = deque([unit])
    conjugators = [(g, inverse(g)) for g in conjugators]
    while queue:
        h = queue.popleft()
        images = [multiply(h, c) for c in seeds]
        images += [multiply(multiply(g, h), gi) for g, gi in conjugators]
        for value in images:
            if value not in elements:
                elements.add(value)
                queue.append(value)
    return elements


def closure(generators):
    elements, queue = {I}, deque([I])
    while queue:
        h = queue.popleft()
        for g in generators:
            value = mul(h, g)
            if value not in elements:
                elements.add(value)
                queue.append(value)
    return elements


blocks = [[0, 2, 5, 6, 7, 11, 12, 13], [1, 8, 16, 18],
          [3, 9, 17, 19], [4, 10, 14, 15]]
if args.full_orbits:
    blocks = [[0, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
              [1, 16, 22, 26, 40, 41, 45, 46, 50, 53, 54, 58],
              [3, 17, 19, 23, 24, 42, 43, 47, 49, 51, 55, 59],
              [4, 18, 20, 21, 25, 38, 39, 44, 48, 52, 56, 57]]
assert sorted(j for block in blocks for j in block) == list(range(len(pairs)))
records, centres, factor_sets = [], [], []
for number, block in enumerate(blocks):
    X, Y = [tuple(pairs[j][k] for j in block) for k in (0, 1)]
    unit = (I,)*len(block)
    C = tuplemul(tuplemul(tuplemul(X, Y), tupleinv(X)), tupleinv(Y))
    actual = normal_closure(unit, [C], [X, Y], tuplemul, tupleinv)
    group = {h[0] for h in actual}
    assert len(group) == len(actual), "Other block coordinates must be determined by the first."
    factor_sets.append(group)
    generators, generated = [], {I}
    for g in sorted(group):
        if g not in generated:
            generators.append(g)
            generated = closure(generators)
    assert generated == group
    commutators = [mul(mul(mul(g, h), inv(g)), inv(h)) for g in generators for h in generators]
    derived = normal_closure(I, commutators, generators, mul, inv)
    assert derived == group
    centre = [z for z in group if all(mul(z, g) == mul(g, z) for g in generators)]
    assert len(centre) == 2
    nonidentity = next(z for z in centre if z != I)
    centres.append(nonidentity)

    def qcan(g):
        return min(g, mul(nonidentity, g))

    def qmul(g, h):
        return qcan(mul(g, h))

    def qinv(g):
        return qcan(inv(g))

    qunit = qcan(I)
    quotient = {qcan(g) for g in group}
    qgenerators = [qcan(g) for g in generators]
    remaining = set(quotient)
    classes = []
    while remaining:
        representative = min(remaining)
        orbit, queue = {representative}, deque([representative])
        while queue:
            h = queue.popleft()
            for g in qgenerators:
                value = qmul(qmul(g, h), qinv(g))
                if value not in orbit:
                    orbit.add(value)
                    queue.append(value)
        assert orbit <= remaining
        remaining -= orbit
        normal_order = len(normal_closure(qunit, [representative], qgenerators, qmul, qinv))
        assert normal_order == (1 if representative == qunit else len(quotient))
        classes.append({"representative": representative, "size": len(orbit),
                        "normal_closure_order": normal_order})
    row = {"factor": number, "coordinate_indices": block, "order": len(group),
           "number_of_generators": len(generators), "derived_order": len(derived),
           "centre_order": len(centre), "quotient_order": len(quotient),
           "quotient_simple": True, "classes": classes,
           "generators": generators, "central_involution": nonidentity}
    records.append(row)
    print("factor", number, "order", len(group), "perfect", True,
          "central quotient order", len(quotient), "simple", True, flush=True)

# Distinguish the three order-660 simple factors by orders of common words.
coordinates = [block[0] for block in blocks]
X, Y = [tuple(pairs[j][k] for j in coordinates) for k in (0, 1)]
XI, YI = tupleinv(X), tupleinv(Y)
C = tuplemul(tuplemul(tuplemul(X, Y), XI), YI)
unit = (I,)*4
words = {unit: ()}
queue = deque([unit])
unresolved = {(1, 2), (1, 3), (2, 3)}
witnesses = []
order_cache = [{} for _ in range(4)]


def quotient_order(value, j):
    cache = order_cache[j]
    if value not in cache:
        running = I
        for n in range(1, 133):
            running = mul(running, value)
            if running in (I, centres[j]):
                cache[value] = n
                break
        else:
            raise AssertionError("Order bound too small")
    return cache[value]


while unresolved:
    h = queue.popleft()
    word = words[h]
    orders = [quotient_order(value, j) for j, value in enumerate(h)]
    for i, j in sorted(unresolved.copy()):
        if orders[i] != orders[j]:
            witnesses.append({"factor_pair": [i, j], "word": word,
                              "quotient_orders": [orders[i], orders[j]], "values": h})
            unresolved.remove((i, j))
    successors = [(tuplemul(h, C), word+(1, 2, -1, -2)),
                  (tuplemul(tuplemul(X, h), XI), (1,)+word+(-1,)),
                  (tuplemul(tuplemul(Y, h), YI), (2,)+word+(-2,))]
    for value, witness in successors:
        if value not in words:
            words[value] = witness
            queue.append(value)
    assert len(words) < 100000

for witness in witnesses:
    value = unit
    for letter in witness["word"]:
        value = tuplemul(value, {1: X, 2: Y, -1: XI, -2: YI}[letter])
    assert value == witness["values"]
    assert sum(z for z in witness["word"] if abs(z) == 1) == 0
    assert sum(z//2 for z in witness["word"] if abs(z) == 2) == 0
    print("separating factors", witness["factor_pair"], "by quotient orders",
          witness["quotient_orders"], "word length", len(witness["word"]), flush=True)

order = 1
for record in records:
    order *= record["order"]
assert order == data["summary"]["common_derived_order"]
assert data["summary"]["common_second_derived_order"] == order
summary = {"common_derived_order": order, "common_derived_perfect": True,
           "all_six_substitution_orbits": args.full_orbits,
           "factor_orders": [r["order"] for r in records],
           "simple_central_quotient_orders": [r["quotient_order"] for r in records],
           "all_simple_pairs_independent": True,
           "certificate_scope": "Exact product and perfectness proof via four small enumerations, simple quotient normal closures, and separating common-word orders; no enumeration of the huge product.",
           "seconds": round(time.time()-started, 3)}
(outdir / (Path(__file__).stem+suffix+".json")).write_text(json.dumps(
    {"summary": summary, "factors": records, "separating_words": witnesses}, indent=2)+"\n")
print(json.dumps(summary, indent=2), flush=True)
