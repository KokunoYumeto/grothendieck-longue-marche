"""Finite group checks for E.133 and E.134.

The Galois comparison, reciprocity, and infinite-prime construction are
proved in the paper. This independently enumerates the finite triangle
group and the common-displacement cardinality used in those arguments.
"""
from collections import Counter
from itertools import product


def act(u, k, modulus=9):
    a, b = u
    for _ in range(k % 3):
        a, b = -b, a-b
    return a % modulus, b % modulus


def mul(g, h, modulus=9):
    a, b, k = g
    c, d = act(h[:2], k, modulus)
    return (a+c) % modulus, (b+d) % modulus, (k+h[2]) % 3


def inverse(g, modulus=9):
    a, b = act((-g[0], -g[1]), -g[2], modulus)
    return a, b, (-g[2]) % 3


def comm(g, h):
    return mul(mul(mul(g, h), inverse(g)), inverse(h))


def closure(generators):
    generators = set(generators)
    known = {(0, 0, 0)}
    frontier = list(known)
    while frontier:
        g = frontier.pop()
        for h in generators:
            gh = mul(g, h)
            if gh not in known:
                known.add(gh)
                frontier.append(gh)
    return known


G = set(product(range(9), range(9), range(3)))
identity = (0, 0, 0)
x, y = (0, 0, 1), (1, 0, 1)
assert closure([x, y]) == G
for z in (x, y, mul(x, y)):
    assert mul(mul(z, z), z) == identity
    assert z != identity
layers = [G]
while len(layers[-1]) > 1:
    layers.append(closure(comm(g, h) for g in layers[-1] for h in G))
assert list(map(len, layers)) == [243, 27, 9, 3, 1]
assert layers[2] == {(a, b, 0) for a in (0, 3, 6) for b in (0, 3, 6)}
H3 = set(product(range(3), range(3), range(3)))
assert all(mul(mul(g, g, 3), g, 3) == identity for g in H3)
assert mul(x, y, 3) != mul(y, x, 3)
print('E134 triangle group order:', len(G))
print('E134 lower central subgroup orders:', list(map(len, layers)))
print('E134 H3 quotient order/exponent:', len(H3), 3)
print('E134 compact kernel over H3:', len(layers[2]), '= (Z/3)^2')

# E133: all 729 possible linear parts of nine simultaneous residuals.
# Adding a fixed constant merely translates the set of forbidden shifts.
image_sizes = Counter()
for columns in product(list(product(range(3), repeat=3)), repeat=2):
    image = {tuple((a*columns[0][i]+b*columns[1][i]) % 3
                   for i in range(3))
             for a, b in product(range(3), repeat=2)}
    image_sizes[len(image)] += 1
    assert len(image) <= 9 and 27-len(image) >= 18
assert dict(image_sizes) == {1: 1, 3: 104, 9: 624}
print('E133 image-size counts for all 3x2 matrices:', dict(image_sizes))
print('E133 common central displacements avoiding every candidate: at least18')
print('PASS: finite group and vector-space certificates only')
