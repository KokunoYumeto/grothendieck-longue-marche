#!/usr/bin/env python3
"""Exact finite source certificate for E.201; standard library only.

All groups are generated from the literal modular generators.  This
certificate verifies finite images and markings, not the infinite
coprime-centralizer or full peripheral lifting arguments.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json


def mm(a, b, n):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % n
                 for i in range(2) for j in range(2))


def mi(a, n):
    assert (a[0]*a[3]-a[1]*a[2]) % n == 1
    return (a[3] % n, -a[1] % n, -a[2] % n, a[0] % n)


def canonical(a):
    a = tuple(t % 12 for t in a)
    return min(a, tuple(-t % 12 for t in a))


def qm(a, b):
    return canonical(mm(a, b, 12))


def qi(a):
    return canonical(mi(a, 12))


def generated(generators, mul, one):
    seen = {one}
    frontier = deque([one])
    while frontier:
        a = frontier.popleft()
        for b in generators:
            c = mul(a, b)
            if c not in seen:
                seen.add(c)
                frontier.append(c)
    return seen


def power(a, n, mul, one):
    out = one
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


I = (1, 0, 0, 1)
S = canonical((0, 1, -1, 0))
R = canonical((0, -1, 1, -1))
Q = generated([S, R], qm, I)
all_projective = {
    canonical(a) for a in product(range(12), repeat=4)
    if (a[0]*a[3]-a[1]*a[2]) % 12 == 1
}
assert Q == all_projective and len(Q) == 576
assert qm(S, S) == I and power(R, 3, qm, I) == I
tau = qm(S, R)
x = qi(qm(tau, tau))
y = qm(qm(S, x), qi(S))
assert x == canonical((1, 2, 0, 1))
assert y == canonical((1, 0, -2, 1))
F = generated([x, y], qm, I)
assert len(F) == 96
assert F == {a for a in Q if tuple(t % 2 for t in a) == I}

V4 = {(1, 2*a, 2*b, 1) for a, b in product(range(2), repeat=2)}
SL3 = {a for a in product(range(3), repeat=4)
       if (a[0]*a[3]-a[1]*a[2]) % 3 == 1}
assert len(V4) == 4 and len(SL3) == 24
assert tuple(-t % 4 for t in I) not in V4


def signed(a):
    candidates = [a, tuple(-t % 12 for t in a)]
    selected = [b for b in candidates if tuple(t % 4 for t in b) in V4]
    assert len(selected) == 1
    return selected[0]


def coordinates(a):
    b = signed(a)
    return tuple(t % 4 for t in b), tuple(t % 3 for t in b)


assert {coordinates(a) for a in F} == set(product(V4, SL3))
checked_products = 0
for a, b in product(F, repeat=2):
    ac, bc = coordinates(a), coordinates(b)
    assert coordinates(qm(a, b)) == (mm(ac[0], bc[0], 4), mm(ac[1], bc[1], 3))
    checked_products += 1

commutators = {
    qm(qm(qm(a, b), qi(a)), qi(b)) for a, b in product(F, repeat=2)
}
derived = generated(commutators, qm, I)
cubes = {power(a, 3, qm, I) for a in F}
H = generated(derived | cubes, qm, I)
i = (0, 1, 2, 0)
j = (1, 1, 1, 2)
Q8 = generated([i, j], lambda a, b: mm(a, b, 3), I)
minus_I3 = (2, 0, 0, 2)
assert len(Q8) == 8
assert mm(i, i, 3) == mm(j, j, 3) == minus_I3
assert mm(i, j, 3) == tuple(-v % 3 for v in mm(j, i, 3))
assert {coordinates(a) for a in derived} == {(I, b) for b in Q8}
assert len(H) == 32 and {coordinates(a) for a in H} == set(product(V4, Q8))

# The affine source D = B/(F' F^3), generated independently.
def mv(a, v):
    return ((a[0]*v[0]+a[1]*v[1]) % 3,
            (a[2]*v[0]+a[3]*v[1]) % 3)


def dm(a, b):
    av = mv(a[0], b[1])
    return mm(a[0], b[0], 3), tuple((a[1][i]+av[i]) % 3 for i in range(2))


def di(a):
    # Affine linear parts may have determinant -1.
    l = a[0]
    det = (l[0]*l[3]-l[1]*l[2]) % 3
    invdet = pow(det, -1, 3)
    inv = tuple(invdet*t % 3 for t in (l[3], -l[1], -l[2], l[0]))
    v = mv(inv, a[1])
    return inv, tuple(-t % 3 for t in v)


D1 = (I, (0, 0))
DS = ((0, 1, 1, 0), (0, 0))
DR = ((0, 2, 1, 2), (0, 1))
assert dm(DS, DS) == D1 and power(DR, 3, dm, D1) == D1
D = generated([DS, DR], dm, D1)
dtau = dm(DS, DR)
dx = di(dm(dtau, dtau))
dy = dm(dm(DS, dx), di(DS))
assert dx == (I, (1, 0)) and dy == (I, (0, 1))
assert len(D) == 54
assert generated([dx, dy], dm, D1) == {(I, v) for v in product(range(3), repeat=2)}


def jm(a, b):
    return qm(a[0], b[0]), dm(a[1], b[1])


J1 = (I, D1)
JS, JR = (S, DS), (R, DR)
J = generated([JS, JR], jm, J1)
assert len(J) == 1728
assert {a[0] for a in J} == Q and {a[1] for a in J} == D
assert {a[0] for a in J if a[1] == D1} == H
fibre_sizes = {d: sum(a[1] == d for a in J) for d in D}
assert set(fibre_sizes.values()) == {32}

comm = qm(qm(qm(x, y), qi(x)), qi(y))
assert comm == canonical((1, 8, 8, 5))
z0 = qm(comm, comm)
assert z0 == canonical((5, 0, 0, 5)) and z0 != I
assert qm(z0, z0) == I and all(qm(z0, a) == qm(a, z0) for a in Q)
assert (z0, D1) in J
assert jm((z0, D1), JR) == jm(JR, (z0, D1))
assert coordinates(z0) == (I, minus_I3)
assert signed(z0) == (5, 0, 0, 5)
positive_line = (1, 2)
positive_R3 = (0, 2, 1, 2)
assert mv(positive_R3, positive_line) == positive_line
assert mv(minus_I3, positive_line) == (2, 1)
assert mv(I, positive_line) == positive_line

result = {
    'statement_id': 'E.201',
    'status': 'PASS',
    'orders': {'Q': len(Q), 'qF': len(F), 'qH': len(H), 'D': len(D), 'J': len(J)},
    'literal_qx': x,
    'literal_qy': y,
    'literal_commutator': comm,
    'literal_commutator_square_signed': signed(z0),
    'signed_product_checks': checked_products,
    'affine_x_translation': dx[1],
    'affine_y_translation': dy[1],
    'joint_fibre_size': 32,
    'joint_r_centralizer_order': sum(jm(a, JR) == jm(JR, a) for a in J),
    'cm_line': positive_line,
    'cm_line_image': (2, 1),
    'cm_bits': (1, 0),
    'scope': 'Finite source groups and exact signed frames only; full centralizer and peripheral lifts are proved in the manuscript.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
