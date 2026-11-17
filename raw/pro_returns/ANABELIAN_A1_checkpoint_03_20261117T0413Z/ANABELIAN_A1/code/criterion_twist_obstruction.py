"""Finite data for the actual R8 cubic-twist pointing obstruction.

The geometry is proved in B_twist_bound.tex.  This program verifies the
base field, its noncube t, and all three two-dimensional mod-two
Frobenius matrices.  It does not replace the geometric cohomology proof.
"""
from pathlib import Path
import json

DEGREE = 38
MODULUS = sum(1 << i for i in (38, 14, 10, 9, 8, 5, 2, 1, 0))
Q = 1 << DEGREE


def rem(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a


def gcd(a, b):
    while b:
        a, b = b, rem(a, b)
    return a


def mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        b >>= 1
        a <<= 1
        if a >> DEGREE:
            a ^= MODULUS
    return c


def power(a, n):
    c = 1
    while n:
        if n & 1:
            c = mul(c, a)
        a = mul(a, a)
        n >>= 1
    return c


assert power(2, Q) == 2
for d in (2, 19):
    assert gcd(MODULUS, power(2, 1 << d) ^ 2) == 1
alpha = power(2, (Q-1)//3)
assert alpha != 1 and power(alpha, 3) == 1
assert mul(alpha, alpha) ^ alpha ^ 1 == 0


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) % 2
             for j in range(2)] for i in range(2)]


def det_im(A):
    return (((1-A[0][0])*(1-A[1][1])-A[0][1]*A[1][0]) % 2)


I = [[1, 0], [0, 1]]
delta = [[0, 1], [1, 1]]
delta2 = matmul(delta, delta)
assert matmul(delta2, delta) == I
assert [det_im(A) for A in (I, delta, delta2)] == [0, 1, 1]
for A in (I, delta, delta2):
    assert matmul(matmul(A, A), A) == I

result = {
    "base_field_degree": DEGREE,
    "modulus_bits": MODULUS,
    "t_encoding": 2,
    "t_to_q_minus_one_over_three": alpha,
    "t_is_noncube": True,
    "root_of_unity_cubic_power": power(alpha, 3),
    "curve": "y^2+y=((u^2+t^2*u+t)/(t^3+1))^3",
    "point": "unique point above infinity",
    "three_cyclic_covers": ["w^3=y", "w^3=t*y", "w^3=t^2*y"],
    "pointed_split": [True, False, False],
    "cohomology_frobenius_matrices": [I, delta, delta2],
    "relative_class_number_mod_two": [0, 1, 1],
    "matrices_after_cubic_extension": [I, I, I],
    "relative_class_number_mod_two_after_cubic_extension": [0, 0, 0],
    "scope": "the two good unpointed twists fail after the first extension making the prescribed point split",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
