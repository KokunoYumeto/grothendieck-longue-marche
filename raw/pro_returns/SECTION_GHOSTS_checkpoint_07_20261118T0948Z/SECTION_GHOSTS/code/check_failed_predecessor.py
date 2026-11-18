"""Exact finite certificate for E.149, independent of its Chebotarev step.

Coordinates are the odd-prime Lie coordinates on H_3.  The actual
residual scalar -1 fixes the center.  Old place 5 pins the global
cyclocubic twist; at a new prime 2 mod 9 the displaced cusp condition
requires a different twist.  Every geometric conjugator is enumerated.
"""

from itertools import product

H = list(product(range(3), repeat=3))
one = (0, 0, 0)
x = (1, 0, 0)


def mul(u, v):
    a, b, c = u
    aa, bb, cc = v
    return ((a + aa) % 3, (b + bb) % 3,
            (c + cc + 2 * (a * bb - b * aa)) % 3)


def inv(u):
    return tuple(-v % 3 for v in u)


def sigma(u):
    a, b, c = u
    return (-a % 3, -b % 3, c)


def conjugate(h, u):
    return mul(mul(h, u), inv(h))


def conjugate_frobenius(h, u):
    return mul(mul(h, u), sigma(inv(h)))


def matching_conjugators(inertia, frobenius, target_inertia=x):
    return [h for h in H
            if conjugate(h, inertia) == target_inertia
            and conjugate_frobenius(h, frobenius) == one]


for u in H:
    assert mul(u, inv(u)) == one
    for v in H:
        assert sigma(mul(u, v)) == mul(sigma(u), sigma(v))

k5 = ((5**4 - 1) // 3) % 3
k2 = ((2**4 - 1) // 3) % 3
k8 = ((8**4 - 1) // 3) % 3
assert (k5, k2, k8) == (1, 2, 0)
assert [u for u in product(range(3), repeat=2)
        if tuple(-a % 3 for a in u) == u] == [(0, 0)]

print("H3 order:", len(H))
print("Cyclocubic localization factors at 5, 2 mod9, -1 mod9:",
      k5, k2, k8)
print("Fixed vectors of the local lower scalar -1: only zero.")
print("twist | old5 conjugators | new minimal-q conjugators | both")
both_counts = []
for c in range(3):
    old = matching_conjugators(x, (0, 0, k5 * c % 3))
    new = matching_conjugators(one, (0, 0, (1 + k2 * c) % 3),
                               target_inertia=one)
    both = bool(old) and bool(new)
    both_counts.append(both)
    print(c, len(old), len(new), both)
assert not any(both_counts)

print("One-place nonminimal-q conjugator counts:",
      [len(matching_conjugators(one, (0, 0, (1 + k8 * c) % 3),
                                target_inertia=one))
       for c in range(3)])
assert all(not matching_conjugators(one, (0, 0, (1 + k8 * c) % 3),
                                     target_inertia=one)
           for c in range(3))

central_classes = []
for c in range(3):
    central_classes.append(
        {conjugate_frobenius(h, (0, 0, c)) for h in H}
        & {(0, 0, j) for j in range(3)})
assert central_classes == [{(0, 0, c)} for c in range(3)]
print("Each central Frobenius class meets the center only in itself.")
print("PASS: no global twist satisfies both frozen local conditions.")
print("Scope: this certificate checks the finite normal form and all")
print("geometric conjugators; prime existence and arithmetic realization")
print("are the separate proofs in E.149.")
