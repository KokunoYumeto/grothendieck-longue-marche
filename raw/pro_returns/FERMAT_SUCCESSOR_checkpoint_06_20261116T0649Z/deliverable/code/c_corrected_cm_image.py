"""Exact finite certificates for the corrected integral CM image.

No symbolic group package is required.  All operations are on tuples
of integer residues.  The program checks the actual signed pure image,
the image of F' F^3, the E.58 central element, the two finite centralizers,
and the positive-modulo-four signs of norm-one units at two.
It does not claim to test the infinite lifting or CM reciprocity proofs.
"""
from itertools import product


def multiply(a, b, modulus):
    return tuple(
        sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) % modulus
        for i in range(2) for j in range(2)
    )


def inverse(a, modulus):
    assert (a[0] * a[3] - a[1] * a[2]) % modulus == 1
    return (a[3], -a[1] % modulus, -a[2] % modulus, a[0])


def power(a, n, modulus):
    answer = (1, 0, 0, 1)
    while n:
        if n & 1:
            answer = multiply(answer, a, modulus)
        a = multiply(a, a, modulus)
        n >>= 1
    return answer


def generated(generators, modulus):
    generators = set(generators)
    identity = (1, 0, 0, 1)
    seen = {identity}
    pending = [identity]
    while pending:
        a = pending.pop()
        for b in generators:
            c = multiply(a, b, modulus)
            if c not in seen:
                seen.add(c)
                pending.append(c)
    return seen


def commutator(a, b, modulus):
    return multiply(
        multiply(multiply(a, b, modulus), inverse(a, modulus), modulus),
        inverse(b, modulus), modulus
    )


identity = (1, 0, 0, 1)
x = (1, 2, 0, 1)
y = (1, 0, 10, 1)
pure = generated([x, y], 12)
derived = generated({commutator(a, b, 12) for a in pure for b in pure}, 12)
h0 = generated(derived | {power(a, 3, 12) for a in pure}, 12)
central = power(commutator(x, y, 12), 2, 12)
assert len(pure) == 96
assert len(derived) == 8
assert len(h0) == 32
assert central == (5, 0, 0, 5)
assert central in h0 and central != identity and power(central, 2, 12) == identity
assert all(multiply(central, a, 12) == multiply(a, central, 12) for a in pure)
print("Signed pure image modulo 12:", len(pure))
print("Derived subgroup:", len(derived))
print("Image of F' F^3:", len(h0))
print("Commutator square:", central, "central of order 2")
print("Its reductions modulo 4 and 3:", tuple(z % 4 for z in central), tuple(z % 3 for z in central))

pure4 = {tuple(z % 4 for z in a) for a in pure}
pure3 = {tuple(z % 3 for z in a) for a in pure}
h04 = {tuple(z % 4 for z in a) for a in h0}
h03 = {tuple(z % 3 for z in a) for a in h0}
assert len(pure4) == len(h04) == 4 and len(pure3) == 24 and len(h03) == 8
assert {(tuple(a % 4 for a in g), tuple(a % 3 for a in g)) for g in pure} == set(product(pure4, pure3))
assert {(tuple(a % 4 for a in g), tuple(a % 3 for a in g)) for g in h0} == set(product(h04, h03))
assert sum(power(g, 2, 3) == identity for g in h03) == 2
assert all(power(g, 4, 3) == identity for g in h03)
print("CRT factors: pure = V4 x SL2(F3); F' F^3 = V4 x Q8")

u = (1, 1, 0, 1)
ell = (1, 0, 2, 1)
s = multiply(multiply(u, ell, 3), u, 3)
rplus = multiply(u, ell, 3)
rzero = tuple(-z % 3 for z in rplus)
sl2 = {a for a in product(range(3), repeat=4) if (a[0] * a[3] - a[1] * a[2]) % 3 == 1}
cubic = {a for a in sl2 if multiply(a, rzero, 3) == multiply(rzero, a, 3)}
gaussian = {a for a in sl2 if multiply(a, s, 3) == multiply(s, a, 3)}
assert len(cubic) == 6 and len(gaussian) == 4
assert cubic == generated([rzero, (2, 0, 0, 2)], 3)
assert gaussian == generated([s], 3)
line = (1, 2)


def act(a, v):
    return ((a[0] * v[0] + a[1] * v[1]) % 3, (a[2] * v[0] + a[3] * v[1]) % 3)


epsilon3 = {a: int(act(a, line) == (2, 1)) for a in cubic}
assert all(act(a, line) in (line, (2, 1)) for a in cubic)
epsilon4 = {power(s, j, 3): j % 2 for j in range(4)}
for group, epsilon in ((cubic, epsilon3), (gaussian, epsilon4)):
    assert set(epsilon.values()) == {0, 1}
    assert all(epsilon[multiply(a, b, 3)] == (epsilon[a] + epsilon[b]) % 2 for a in group for b in group)
assert (epsilon3[tuple(z % 3 for z in central)], epsilon4[identity]) == (1, 0)
print("Cubic centralizer order 6, Gaussian centralizer order 4; both parity maps are surjective homomorphisms")
print("E.58 parity (epsilon3, epsilon4) = (1, 0)")

# At sufficient 2-power modulus a norm-one unit congruent to 1 mod 2
# reduces to one of the two scalar units modulo 4.  Modulo 8 is needed
# on the ramified Gaussian side: norm-one modulo 4 alone is insufficient.
for modulus in (8, 16, 32):
    for name, cross in (("Eisenstein", -1), ("Gaussian", 0)):
        units = [(a, b) for a, b in product(range(modulus), repeat=2)
                 if a % 2 == 1 and b % 2 == 0
                 and (a*a + cross*a*b + b*b) % modulus == 1]
        reductions = {(a % 4, b % 4) for a, b in units}
        assert reductions == {(1, 0), (3, 0)}
        print(name, "norm-one level-two units modulo", modulus, "count", len(units), "reductions modulo 4", sorted(reductions))
print("All finite assertions passed; no infinite image statement is inferred solely from this program.")
