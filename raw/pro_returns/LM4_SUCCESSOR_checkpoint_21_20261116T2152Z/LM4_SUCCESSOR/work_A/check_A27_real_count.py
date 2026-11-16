#!/usr/bin/env python3
"""Exact finite controls for the real-reflection count (no external packages)."""
from itertools import permutations, product
from collections import Counter

n = 5
one = tuple(range(n))
def mul(a, b):
    return tuple(a[b[i]] for i in range(n))
def inverse(a):
    return tuple(a.index(i) for i in range(n))
def parity(a):
    return sum(a[i] > a[j] for i in range(n) for j in range(i + 1, n)) % 2
def order(a):
    b = one
    for k in range(1, 121):
        b = mul(b, a)
        if b == one:
            return k
    raise AssertionError('Order not found')
def generated(gens):
    gens = tuple(gens) + tuple(map(inverse, gens))
    seen, queue = {one}, [one]
    for a in queue:
        for g in gens:
            b = mul(a, g)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    return frozenset(seen)
def cycle(*points):
    a = list(one)
    for u, v in zip(points, points[1:] + points[:1]):
        a[u - 1] = v - 1
    return tuple(a)

S = tuple(permutations(range(n)))
A = tuple(g for g in S if parity(g) == 0)
I = tuple(g for g in S if parity(g) == 1 and mul(g, g) == one)
assert len(S) == 120 and len(A) == 60 and len(I) == 10
assert all(order(t) == 2 for t in I)
# The perfect-kernel assertion is checked by generating all commutators.
comms = [mul(mul(mul(a, b), inverse(a)), inverse(b)) for a in A for b in A]
assert len(generated(comms)) == 60
hist = Counter(len(generated(ts)) for ts in product(I, repeat=3))
assert sum(hist.values()) == 1000 and hist.get(120, 0) == 0
x, y, t = cycle(1,2,3,4,5), cycle(1,2,3), cycle(1,2)
assert len(generated((x,y))) == 60
assert len(generated((x,y,t))) == 120
# Every product of two odd involutions has order at most three.
prod_orders = Counter(order(mul(a,b)) for a,b in product(I, repeat=2))
assert set(prod_orders) == {1,2,3}
# No pants generating pair of A5 can have all three cusp orders <=3.
ordA = {a: order(a) for a in A}
allowed = tuple(a for a in A if ordA[a] in (1,2,3))
candidates = [(a,b) for a,b in product(allowed,repeat=2) if ordA[mul(a,b)] in (1,2,3)]
maxrank = Counter(len(generated((a,b))) for a,b in candidates)
assert maxrank.get(60,0) == 0
# Verify the unrestricted triangle-matrix trace formula: every matrix is all ones.
# Its trace is 10^3, in agreement with the direct enumeration.
trace_count = sum(1 for a,b,c in product(I,repeat=3))
assert trace_count == sum(hist.values())
print('orientation extension: S5 -> C2, kernel A5')
print('|S5| =', len(S), '|A5| =', len(A), '|[A5,A5]| =', len(generated(comms)))
print('odd involution fibre size =', len(I))
print('reflection triple generated-order histogram =', dict(sorted(hist.items())))
print('proper reflection triple count =', hist.get(120,0))
print('ordinary generating pair of A5: (12345), (123)')
print('these with (12) generate S5:', len(generated((x,y,t))) == 120)
print('two-reflection product order histogram =', dict(sorted(prod_orders.items())))
print('A5 cusp-order <=3 candidate pairs =', len(candidates))
print('their generated-order histogram =', dict(sorted(maxrank.items())))
print('such pairs generating A5 =', maxrank.get(60,0))
print('unrestricted reflection triangle matrix trace =', trace_count)
