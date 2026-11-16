"""Finite certificate for the generic normalizer countermodel B.51.5.

The infinite profinite embedding uses the projectivity proof in TeX.
This checks the two-generator Heisenberg quotient at p=2 and q=3.
"""
from itertools import product

def hmul(a, b, p):
    return ((a[0]+b[0]) % p,
            (a[1]+b[1]) % p,
            (a[2]+b[2]+a[0]*b[1]) % p)

def hinv(a, p):
    return (-a[0] % p, -a[1] % p, (-a[2]+a[0]*a[1]) % p)

zero = (0, 0, 0)
unit = (zero, zero)
def mul(a, b):
    return hmul(a[0], b[0], 2), hmul(a[1], b[1], 3)

def inv(a):
    return hinv(a[0], 2), hinv(a[1], 3)

def power(a, n):
    result = unit
    for _ in range(n):
        result = mul(result, a)
    return result

def commutator(a, b):
    return mul(mul(mul(inv(a), inv(b)), a), b)

H2 = list(product(range(2), repeat=3))
H3 = list(product(range(3), repeat=3))
G = set(product(H2, H3))
S2 = {(a, zero) for a in H2}
S3 = {(zero, b) for b in H3}
x, y = (1, 0, 0), (0, 1, 0)
a, b = (x, x), (y, y)
seen, todo = {unit}, [unit]
generators = (a, b, inv(a), inv(b))
while todo:
    g = todo.pop()
    for s in generators:
        t = mul(g, s)
        if t not in seen:
            seen.add(t)
            todo.append(t)
assert seen == G
assert len(G) == 216 and len(S2) == 8 and len(S3) == 27
assert power(a, 3) == (x, zero)
assert power(a, 4) == (zero, x)
assert power(b, 3) == (y, zero)
assert power(b, 4) == (zero, y)
assert commutator((x, zero), (y, zero)) != unit
assert commutator((zero, x), (zero, y)) != unit
for g in G:
    for s in S2:
        assert mul(mul(g, s), inv(g)) in S2
    for t in S3:
        assert mul(mul(g, t), inv(g)) in S3
for s in S2:
    for t in S3:
        assert mul(s, t) == mul(t, s)
print('Heisenberg direct-product quotient order: 216')
print('Sylow orders: 8 and27; both nonabelian: PASS')
print('Two diagonal generators generate the full product: PASS')
print('Primary powers3 and4 separate both generator components: PASS')
print('Both Sylows normalized by every group element: PASS')
print('The two Sylows centralize each other: PASS')
print('Infinite-model embedding is supplied by the projectivity proof, '
      'not inferred from this finite check.')
