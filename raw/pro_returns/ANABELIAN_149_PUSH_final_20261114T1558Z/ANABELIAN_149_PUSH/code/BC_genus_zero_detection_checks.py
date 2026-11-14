#!/usr/bin/env python3
"""Exact icosahedral certificate for C.7d; standard-library arithmetic only.

All field operations take place in Q[z]/(z^4+z^3+z^2+z+1).  The
enumeration certifies the matrix group, its five Klein-four subgroups,
the resulting faithful A5 action, and the three ramification orbits.
It is independent of floating-point calculations and group libraries.
"""
from collections import Counter, deque
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path


def elt(*a):
    return tuple(F(x) for x in a) + (F(0),) * (4 - len(a))


ZERO, ONE, Z = elt(0), elt(1), elt(0, 1)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = [F(0)] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    for k in range(6, 3, -1):
        for j in range(1, 5):
            c[k - j] -= c[k]
        c[k] = 0
    return tuple(c[:4])


def inv(a):
    if a == ZERO:
        raise ZeroDivisionError
    basis = [elt(*(int(i == j) for i in range(4))) for j in range(4)]
    columns = [mul(a, e) for e in basis]
    rows = [[columns[j][i] for j in range(4)] + [F(i == 0)]
            for i in range(4)]
    for j in range(4):
        pivot = next(i for i in range(j, 4) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        d = rows[j][j]
        rows[j] = [x / d for x in rows[j]]
        for i in range(4):
            if i != j:
                d = rows[i][j]
                rows[i] = [x - d * y for x, y in zip(rows[i], rows[j])]
    answer = tuple(rows[i][4] for i in range(4))
    assert mul(a, answer) == ONE
    return answer


def power(a, n):
    answer = ONE
    while n:
        if n & 1:
            answer = mul(answer, a)
        a = mul(a, a)
        n //= 2
    return answer


def mm(a, b):
    return (
        add(mul(a[0], b[0]), mul(a[1], b[2])),
        add(mul(a[0], b[1]), mul(a[1], b[3])),
        add(mul(a[2], b[0]), mul(a[3], b[2])),
        add(mul(a[2], b[1]), mul(a[3], b[3])),
    )


def project(a):
    scale = inv(next(x for x in a if x != ZERO))
    return tuple(mul(x, scale) for x in a)


IDENTITY = (ONE, ZERO, ZERO, ONE)
a, b = sub(Z, power(Z, 4)), sub(power(Z, 2), power(Z, 3))
S = (a, b, b, neg(a))
T = (power(Z, 2), ZERO, ZERO, power(Z, 3))

assert add(power(a, 2), power(b, 2)) == elt(-5)
assert power(mul(a, b), 2) == elt(5)
assert mm(S, S) == tuple(mul(elt(-5), x) for x in IDENTITY)
assert project(mm(mm(S, T), mm(mm(S, T), mm(S, T)))) == IDENTITY

generators = [project(S), project(T)]
group, indices, words = [IDENTITY], {IDENTITY: 0}, [""]
queue = deque([0])
while queue:
    i = queue.popleft()
    for letter, gen in zip("st", generators):
        product = project(mm(group[i], gen))
        if product not in indices:
            assert len(group) < 1000, "unexpectedly large matrix group"
            indices[product] = len(group)
            words.append(words[i] + letter)
            queue.append(len(group))
            group.append(product)
assert len(group) == 60

table = [[indices[project(mm(x, y))] for y in group] for x in group]
inverses = [next(j for j in range(60) if table[i][j] == 0)
            for i in range(60)]


def order(i):
    n, current = 1, i
    while current:
        current = table[current][i]
        n += 1
        assert n <= 60
    return n


orders = [order(i) for i in range(60)]
assert Counter(orders) == {1: 1, 2: 15, 3: 20, 5: 24}
kleins = sorted({tuple(j for j in range(60) if table[i][j] == table[j][i])
                 for i in range(60) if orders[i] == 2})
assert len(kleins) == 5
assert all(len(k) == 4 and all(orders[i] in (1, 2) for i in k)
           for k in kleins)
for k in kleins:
    assert all(table[i][j] in k for i in k for j in k)


def conjugate(i, j):
    return table[table[i][j]][inverses[i]]


perms = [tuple(kleins.index(tuple(sorted(conjugate(i, j) for j in k)))
               for k in kleins) for i in range(60)]


def parity(sigma):
    return sum(sigma[i] > sigma[j] for i in range(5)
               for j in range(i + 1, 5)) % 2


alternating = {sigma for sigma in permutations(range(5)) if parity(sigma) == 0}
assert set(perms) == alternating
for i in range(60):
    for j in range(60):
        assert perms[table[i][j]] == tuple(perms[i][perms[j][k]] for k in range(5))

# Finite point stabilizers in PGL2 over characteristic zero are cyclic.
# The element-order list therefore implies that each nontrivial cyclic
# subgroup is a full stabilizer at each of its two fixed points.
ramification = []
for e in (2, 3, 5):
    subgroup_count = orders.count(e) // (e - 1)
    fixed_points = 2 * subgroup_count
    orbit_size = 60 // e
    assert fixed_points == orbit_size
    ramification.append({"index": e, "cyclic_subgroups": subgroup_count,
                          "ramified_points": fixed_points,
                          "orbits": fixed_points // orbit_size})
rh_sum = sum(row["ramified_points"] * (row["index"] - 1)
             for row in ramification)
assert rh_sum == 118 and -120 + rh_sum == -2

# An explicit missing composition-factor quotient, using the Known
# Burness/FGM classification cited in the manuscript.  This computation
# verifies generation only; it does not claim to prove that classification.
prime = 47


def modular_project(m):
    m = tuple(x % prime for x in m)
    return min(m, tuple(-x % prime for x in m))


def modular_product(m, n):
    return modular_project((m[0] * n[0] + m[1] * n[2],
                            m[0] * n[1] + m[1] * n[3],
                            m[2] * n[0] + m[3] * n[2],
                            m[2] * n[1] + m[3] * n[3]))


modular_generators = ((1, 1, 0, 1), (1, 0, 1, 1))
modular_group = {modular_project((1, 0, 0, 1))}
modular_queue = deque(modular_group)
while modular_queue:
    m = modular_queue.popleft()
    assert (m[0] * m[3] - m[1] * m[2]) % prime == 1
    for n in modular_generators:
        product = modular_product(m, n)
        if product not in modular_group:
            modular_group.add(product)
            modular_queue.append(product)
assert len(modular_group) == prime * (prime * prime - 1) // 2 == 51888


def encode(x):
    return [str(c) for c in x]


out = {
    "claim": "C.7d explicit nonsolvable genus-zero monodromy quotient",
    "arithmetic": "exact Q[z]/Phi_5(z), standard-library Fraction",
    "group_order": len(group),
    "element_order_distribution": dict(sorted(Counter(orders).items())),
    "klein_four_subgroups": len(kleins),
    "faithful_permutation_image": "all 60 even permutations of five objects",
    "matrix_S": [encode(x) for x in S],
    "matrix_T": [encode(x) for x in T],
    "permutation_S_zero_based": perms[indices[project(S)]],
    "permutation_T_zero_based": perms[indices[project(T)]],
    "ramification": ramification,
    "Riemann_Hurwitz_total_different": rh_sum,
    "source_genus": 0,
    "quotient_genus": 0,
    "branch_values_after_normalization": [0, 1, "infinity"],
    "explicit_missing_simple_quotient": {
        "group": "PSL2(F47)",
        "projective_classes_enumerated": len(modular_group),
        "SL2_generators": modular_generators,
        "genus_zero_exclusion": "Known input: Burness 2018 author p36, Section4.3; original FGM proof not opened",
        "computation_scope": "Exact generation and order only, not classification",
    },
    "scope": "Certificate supplies the finite matrix quotients; arithmetic fixed-group proof is in the manuscript and the missing-factor classification is a Known source input.",
    "all_checks_passed": True,
}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
