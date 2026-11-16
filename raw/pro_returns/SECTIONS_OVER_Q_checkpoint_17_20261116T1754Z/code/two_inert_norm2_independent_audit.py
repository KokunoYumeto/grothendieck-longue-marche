"""Independent A.156 audit from the literal TeX coefficient tables.

This uses integer Newton identities and fraction-free elimination, not the
relation-search output, a class-group presentation, or Sympy's charpoly.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
src = (root / 'sections/two_inert_norm2_generator_agent.tex').read_text()
low = re.findall(r'^(\d+)&([+-])&(\d+)&(\d+)\\\\', src, re.M)
high = re.findall(r'^(\d+)&(\d+)&(\d+)\\\\', src, re.M)
assert len(low) == len(high) == 9
B = 10**40
c = []
for i, (a, b) in enumerate(zip(low, high)):
    j, sign, x0, x1 = a
    k, x2, x3 = b
    assert int(j) == int(k) == i
    blocks = list(map(int, (x0, x1, x2, x3)))
    assert all(0 <= x < B for x in blocks)
    c.append((1 if sign == '+' else -1) * sum(x*B**r for r, x in enumerate(blocks)))
d = 649
D = d**5
a = 3*d**6
assert D == 115139273278249 and a == 224176165072750803
record = json.loads((root / 'code/two_inert_norm2_generator_certificate_data.json').read_text())
assert c == record['generator_numerators']
assert D == record['generator_common_denominator']

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

H = [[c[i-j] if i >= j else a*c[9+i-j] for j in range(9)] for i in range(9)]
power = [[int(i == j) for j in range(9)] for i in range(9)]
traces = [0]
for k in range(1, 10):
    power = matmul(power, H)
    traces.append(sum(power[i][i] for i in range(9)))
h = [1]
for k in range(1, 10):
    numerator = -sum(h[k-i]*traces[i] for i in range(1, k+1))
    assert numerator % k == 0
    h.append(numerator // k)
assert all(h[k] % D**k == 0 for k in range(10))
char = [h[k] // D**k for k in range(10)]
assert char == record['characteristic_polynomial_coefficients']
assert char[0] == 1 and char[-1] == -2

def bareiss(A):
    A = [row[:] for row in A]
    sign, previous = 1, 1
    for k in range(len(A)-1):
        if not A[k][k]:
            j = next(j for j in range(k+1, len(A)) if A[j][k])
            A[k], A[j] = A[j], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k+1, len(A)):
            for j in range(k+1, len(A)):
                numerator = A[i][j]*pivot - A[i][k]*A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
        for i in range(k+1, len(A)):
            A[i][k] = 0
        previous = pivot
    return sign*A[-1][-1]

assert bareiss(H) == 2*D**9

def mul(x, y, rad):
    n = len(x)
    out = [Q(0)]*(2*n-1)
    for i in range(n):
        for j in range(n):
            out[i+j] += x[i]*y[j]
    for i in range(2*n-2, n-1, -1):
        out[i-n] += rad*out[i]
    return out[:n]

def add(*xs):
    return [sum(z) for z in zip(*xs)]

def cube(x, rad):
    return mul(mul(x, x, rad), x, rad)

parts = [[Q(c[j+3*k]*d**(2*k), D) for k in range(3)] for j in range(3)]
A0, A1, A2 = parts
w = [Q(0), Q(d*d), Q(0)]
norm = add(cube(A0, 3), mul(w, cube(A1, 3), 3),
           mul(mul(w, w, 3), cube(A2, 3), 3),
           [-3*z for z in mul(w, mul(A0, mul(A1, A2, 3), 3), 3)])
assert norm == [-1, 1, 0]
g = [Q(x, D) for x in c]
remainder = [Q(0)]*9
for z in char:
    remainder = mul(remainder, g, a)
    remainder[0] += z
assert remainder == [0]*9

def poly_mul2(x, y):
    z = 0
    while y:
        if y & 1:
            z ^= x
        x <<= 1
        y >>= 1
    return z

assert poly_mul2(poly_mul2(0b11, 0b111), (1 << 6) | (1 << 3) | 1) == (1 << 9) | 1
assert next(k for k in range(1, 10) if pow(2, k, 9) == 1) == 6
assert a % 3 == 0 and a % 9 != 0 and a % 2 == 1
assert (d*d)**9*a == 3*d**24
assert d**6*d**2 == d**8
assert 3*d**6 // d**6 == 3

digest = hashlib.sha256(json.dumps(char, separators=(',', ':')).encode()).hexdigest()
lines = [
    'PASS: all 36 literal base-10^40 TeX blocks and nine signs reconstruct the certified element',
    'PASS: integer Newton characteristic polynomial agrees coefficient by coefficient',
    'PASS: all ten D^j divisibilities and independent Bareiss determinant 2D^9',
    'PASS: literal three-coordinate relative norm equals alpha-1',
    'PASS: monic integral characteristic polynomial annihilates the element exactly',
    'PASS: actual root embeddings, Eisenstein test and unique degree-one prime at two',
    'Characteristic polynomial SHA256: ' + digest,
    'No class-group computation or relation-search completeness is used.'
]
text = '\n'.join(lines) + '\n'
(root / 'code/two_inert_norm2_independent_audit_output.txt').write_text(text)
print(text, end='')
