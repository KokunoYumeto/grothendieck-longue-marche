"""Exact A5 certificate for D.24; standard library only.

The profinite lifting in D.24 is proved using the opened Gaschuetz
lemma. This finite computation certifies the quotient and the failure
of peripheral preservation, not a profinite peripheral lifting claim.
"""
from itertools import permutations
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
one = tuple(range(5))

def mul(a, b):
    return tuple(a[b[i]] for i in range(5))

def inv(a):
    out = [0] * 5
    for i, v in enumerate(a):
        out[v] = i
    return tuple(out)

def conj(a, b):
    return mul(mul(a, b), inv(a))

def closure(gens):
    gens = tuple(gens)
    seen = {one}
    queue = [one]
    for a in queue:
        for b in gens:
            c = mul(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen

def even(a):
    return sum(a[i] > a[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0

def order(a):
    b, n = a, 1
    while b != one:
        b = mul(b, a)
        n += 1
    return n

x = (1, 2, 3, 4, 0)  # (1 2 3 4 5)
y = (1, 2, 0, 3, 4)  # (1 2 3)
t = (1, 0, 2, 3, 4)  # (1 2)
A5 = {a for a in permutations(range(5)) if even(a)}
assert closure([x, y]) == A5 and len(A5) == 60
remaining, classes = set(A5), []
while remaining:
    a = min(remaining)
    cc = {conj(g, a) for g in A5}
    remaining -= cc
    classes.append(cc)
classes.sort(key=lambda c: (len(c), min(c)))
normal_closures = [len(closure(c)) for c in classes]
assert normal_closures == [1, 60, 60, 60, 60]
commutators = {mul(mul(mul(a, b), inv(a)), inv(b)) for a in A5 for b in A5}
assert closure(commutators) == A5
xc = {conj(g, x) for g in A5}
tx = conj(t, x)
txc = {conj(g, tx) for g in A5}
assert len(xc) == len(txc) == 12 and xc.isdisjoint(txc)
assert {conj(t, g) for g in A5} == A5
assert all(conj(t, mul(a, b)) == mul(conj(t, a), conj(t, b))
           for a in A5 for b in A5)
data = {
    'group_order': len(A5),
    'generator_orders': [order(x), order(y)],
    'generators_one_based': [[j+1 for j in a] for a in (x, y)],
    'odd_conjugator_one_based': [j+1 for j in t],
    'x_image_one_based': [j+1 for j in tx],
    'conjugacy_class_sizes': [len(c) for c in classes],
    'normal_closure_orders': normal_closures,
    'derived_subgroup_order': len(closure(commutators)),
    'x_and_image_class_intersection': len(xc & txc),
    'automorphism_multiplication_checks': 60**2,
    'PASS': True,
}
(BASE/'d_lifting.json').write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps(data, indent=2))
