#!/usr/bin/env python3
"""Verify the C13 cover by fixed-point addition, independently of Cantor code.

Use CRT interpolation, local Taylor jets and conjugate cancellation, followed
by explicit degree-three divisor reduction. No producer arithmetic is imported.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import json

def product(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1
        a <<= 1
        if a & 64: a ^= 67
    return r
M = [[product(a, b) for b in range(64)] for a in range(64)]
I = [None] + [next(b for b in range(1, 64) if M[a][b] == 1)
              for a in range(1, 64)]
def powf(a, n):
    v = 1
    while n:
        if n & 1: v = M[v][a]
        a = M[a][a]
        n >>= 1
    return v
assert all(powf(a, 64) == a for a in range(64))
def trim(a):
    a = list(a)
    while a and not a[-1]: a.pop()
    return tuple(a)
def add(a, b):
    c = list(a) + [0] * max(0, len(b) - len(a))
    for i, x in enumerate(b): c[i] ^= x
    return trim(c)
def scale(a, c): return trim(M[x][c] for x in a)
def mul(a, b):
    c = [0] * max(0, len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] ^= M[x][y]
    return trim(c)
def division(a, b):
    assert b
    r = list(a); q = [0] * max(0, len(a) - len(b) + 1)
    while len(r) >= len(b):
        d = len(r) - len(b); c = M[r[-1]][I[b[-1]]]; q[d] = c
        for i, x in enumerate(b): r[i+d] ^= M[c][x]
        while r and r[-1] == 0: r.pop()
    return trim(q), tuple(r)
def rem(a, b): return division(a, b)[1]
def exact(a, b):
    q, r = division(a, b)
    assert not r
    return q
def ev(a, x):
    s = 0
    for c in reversed(a): s = M[s][x] ^ c
    return s
h = (0, 0, 1); f = (0, 1, 0, 0, 0, 1); O = ((1,), ())
checks = Counter()
def validate(D):
    u, v = D
    assert 1 <= len(u) <= 3 and u[-1] == 1 and len(v) < len(u)
    assert not rem(add(add(mul(v, v), mul(h, v)), f), u)
    return D
def add_point(D, P):
    if P is None: return D
    u, v = D; a, b = P; l = (a, 1)
    ua, va = ev(u, a), ev(v, a)
    if ua:
        checks['distinct_interpolation'] += 1
        c = M[b ^ va][I[ua]]
        U, V = mul(u, l), add(v, scale(u, c))
    elif va == b ^ M[a][a]:
        checks['conjugate_cancellation'] += 1
        U = exact(u, l); V = rem(v, U)
    else:
        assert a and va == b
        c1 = M[powf(a, 4) ^ 1][I[M[a][a]]]
        jet1 = add((b,), scale(l, c1))
        if u == l:
            checks['double_point_taylor'] += 1
            U, V = mul(l, l), jet1
        elif u == mul(l, l):
            checks['triple_point_taylor'] += 1
            c2 = M[M[c1][c1] ^ b][I[M[a][a]]]
            U, V = mul(u, l), add(jet1, scale(u, c2))
        else:
            checks['double_point_and_distinct_CRT'] += 1
            other = exact(u, l)
            assert len(other) == 2 and other[1] == 1
            c = other[0]
            assert c != a
            l2 = mul(l, l)
            coef = M[ev(v, c) ^ ev(jet1, c)][I[ev(l2, c)]]
            U, V = mul(l2, other), add(jet1, scale(l2, coef))
    if len(U) > 3:
        checks['degree_three_reduction'] += 1
        W = exact(add(add(f, mul(V, V)), mul(h, V)), U)
        U = scale(W, I[W[-1]]); V = rem(add(h, V), U)
    return validate((U, V))

points = [None] + [(a, b) for a in range(64) for b in range(64)
                  if M[b][b] ^ M[M[a][a]][b] == powf(a, 5) ^ a]
assert len(points) == 64
counts_small = {}
for degree in (1, 2, 6):
    subfield = {a for a in range(64) if powf(a, 2**degree) == a}
    counts_small[str(degree)] = sum(P is None or (P[0] in subfield and P[1] in subfield)
                                   for P in points)
assert counts_small == {'1': 4, '2': 4, '6': 64}
# Newton recurrence, independent of the producer's companion matrix.
a = [1, 0, 2, 4]; s = [4]
for n in range(1, 25):
    if n <= 4:
        s.append(-sum(a[j-1]*s[n-j] for j in range(1, n)) - n*a[n-1])
    else:
        s.append(-sum(a[j-1]*s[n-j] for j in range(1, 5)))
c = [Fraction(1)]
for n in range(1, 5):
    c.append(-sum(c[n-j]*s[6*j] for j in range(1, n+1))/n)
assert c == [1, -1, -80, -64, 4096]
order = int(sum(c)); assert order == 3952
cycles, projections = [], []
for P in points:
    if P is None:
        cycle = [O]
    else:
        cycle = [O]; D = add_point(O, P)
        while D != O:
            cycle.append(D)
            assert len(cycle) <= order
            D = add_point(D, P)
        assert order % len(cycle) == 0
    cycles.append(cycle); projections.append(cycle[304 % len(cycle)])
idx = next(i for i, D in enumerate(projections) if D != O)
cycle = cycles[idx]
subgroup = [cycle[(304*j) % len(cycle)] for j in range(13)]
assert len(set(subgroup)) == 13
log = {D:j for j, D in enumerate(subgroup)}
chi = [log[D] for D in projections]
occupancies = [chi.count(j) for j in range(13)]
assert occupancies == [16] + [4]*12
# Compare every coordinate, not merely aggregate occupancy, with the producer.
producer = json.loads(Path(__file__).with_name('b5_char2_13_certificate.json').read_text())
def canonical(u, v): return trim(u), trim(v)
producer_log = {canonical(r['u'], r['v']):r['j'] for r in producer['subgroup_table']}
assert set(producer_log) == set(log)
point_to_projection = {None if P is None else tuple(P):D
                       for P, D in zip(points, projections)}
for row in producer['point_table']:
    P = None if row['point'] is None else tuple(row['point'])
    D = canonical(row['u'], row['v'])
    assert point_to_projection[P] == D
    assert producer_log[D] == row['chi']
certificate = {
 'method':'independent fixed-point addition by CRT and Taylor jets, no Cantor import',
 'field_modulus_bits':67, 'curve':'Y^2+X^2Y=X^5+X',
 'point_counts_by_field_degree':counts_small,
 'H64_coefficients_descending':[int(x) for x in c], 'jacobian_order':order,
 'point_class_orders':[len(cycle) for cycle in cycles],
 'point_table':[{'point':P, 'projection':D, 'chi':j}
                for P, D, j in zip(points, projections, chi)],
 'subgroup_generator':subgroup[1], 'subgroup_table':subgroup,
 'occupancies':occupancies, 'twisted_polynomial_ascending':[1,12,64],
 'primitive_slopes':{'1/3':12, '2/3':12}, 'relative_class_number':77**12,
 'checked_cases':dict(checks),
 'producer_comparison':'all64pointprojectionsandall13subgroupelementsagree'}
Path(__file__).with_suffix('.json').write_text(json.dumps(certificate, indent=2)+'\n')
print('PASS independent fixed-point-addition verification')
print('point counts', counts_small, 'Jacobian order', order)
print('occupancies', occupancies)
print('point-class orders', dict(sorted(Counter(len(cycle) for cycle in cycles).items())))
print('checked addition cases', dict(checks))
print('all point projections and subgroup elements agree with producer')
