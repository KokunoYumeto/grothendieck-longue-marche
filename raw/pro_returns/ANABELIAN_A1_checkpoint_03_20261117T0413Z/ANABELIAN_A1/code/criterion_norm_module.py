#!/usr/bin/env python3
"""Exact small checks for B.NM5--B.NM6; no external packages required."""
from itertools import product
import json
from pathlib import Path


class BinaryField:
    def __init__(self, degree, modulus):
        self.degree, self.modulus = degree, modulus
        self.q = 1 << degree

    def mul(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.modulus
        return result

    def power(self, a, n):
        result = 1
        while n:
            if n & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            n >>= 1
        return result

    def inv(self, a):
        assert a
        return self.power(a, self.q - 2)


curve_results = []
for degree, modulus in [(1, 0b11), (2, 0b111)]:
    field = BinaryField(degree, modulus)
    assert all(field.power(a, field.q - 1) == 1
               for a in range(1, field.q))
    points = []
    right_sides = []
    for x in range(field.q):
        if x in (0, 1):
            continue
        rhs = x ^ field.inv(x) ^ field.inv(x ^ 1)
        trace = 0
        t = rhs
        for _ in range(degree):
            trace ^= t
            t = field.mul(t, t)
        right_sides.append(dict(x=x, rhs=rhs, absolute_trace=trace))
        for y in range(field.q):
            if (field.mul(y, y) ^ y) == rhs:
                points.append([x, y])
    curve_results.append(dict(q=field.q, modulus_binary=bin(modulus),
                              affine_nonpole_points=points,
                              pole_points=3,
                              count=len(points) + 3,
                              right_sides=right_sides))

assert [r['count'] for r in curve_results] == [3, 3]
q, n1, n2 = 2, 3, 3
s1, s2 = q + 1 - n1, q*q + 1 - n2
a1, a2 = -s1, (s1*s1 - s2)//2
weil_polynomial = [1, a1, a2, q*a1, q*q]
assert weil_polynomial == [1, 0, -1, 0, 4]
assert sum(weil_polynomial) == 4

field = BinaryField(2, 0b111)
omega = 2
group = list(product(range(3), repeat=2))
vector = (1, 1)


def act(element, v):
    a, b = element
    return (field.mul(field.power(omega, a), v[0]),
            field.mul(field.power(omega, b), v[1]))


orbit = sorted(set(act(g, vector) for g in group))
stabilizer = [g for g in group if act(g, vector) == vector]
diagonal = [(i, i) for i in range(3)]
norm = (0, 0)
for g in diagonal:
    a, b = act(g, vector)
    norm = (norm[0] ^ a, norm[1] ^ b)
assert len(orbit) == 9
assert stabilizer == [(0, 0)]
assert norm == (0, 0)

certificate = dict(
    curve='y^2+y=x+1/x+1/(x+1) over F2',
    curve_counts=curve_results,
    weil_polynomial_coefficients=weil_polynomial,
    jacobian_order=sum(weil_polynomial),
    rational_jacobian_group='C2 x C2, using the two divisor identities in B.NM5',
    abstract_norm_counterexample=dict(
        group='C3 x C3', field='F2[w]/(w^2+w+1)',
        representation='(a,b)(u,v)=(w^a*u,w^b*v)', vector=vector,
        orbit=orbit, stabilizer=stabilizer, subgroup=diagonal,
        norm=norm, quotient_order=3))

stem = Path(__file__).with_suffix('')
stem.with_suffix('.json').write_text(json.dumps(certificate, indent=2)+'\n')
print(json.dumps(certificate, indent=2))
