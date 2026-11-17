"""Exact modulo-12 checks for the locally anti-invariant parity-one frame.

The infinite existence assertion is proved in A.16--A.17.  This file
checks only its explicitly specified matrix word and quotient labels.
All matrix entries are reduced modulo 12.  No numerical approximation
or claim of an equivariant full lift is involved.
"""

MODULUS = 12


def multiply(a, b):
    return tuple(
        sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) % MODULUS
        for i in range(2)
        for j in range(2)
    )


def inverse(a):
    det = (a[0] * a[3] - a[1] * a[2]) % MODULUS
    det_inverse = pow(det, -1, MODULUS)
    return tuple(det_inverse * v % MODULUS for v in (a[3], -a[1], -a[2], a[0]))


def conjugate(a, b):
    return multiply(multiply(a, b), inverse(a))


def commutator(a, b):
    return multiply(conjugate(a, b), inverse(b))


def projectively_equal(a, b):
    return a == b or a == tuple(-v % MODULUS for v in b)


I = (1, 0, 0, 1)
X = (1, 2, 0, 1)
Y = (1, 0, 10, 1)
S = (0, 1, 11, 0)
R = (0, 11, 1, 11)
D = (0, 1, 1, 0)
Z0 = (5, 0, 0, 5)

assert projectively_equal(conjugate(D, S), S)
assert conjugate(D, R) == inverse(R)
assert conjugate(D, X) == inverse(Y)
assert conjugate(D, Y) == inverse(X)

C = commutator(X, Y)
H = multiply(C, conjugate(X, C))
assert C == (1, 8, 8, 5)
assert H == (9, 4, 8, 9)
assert tuple(v % 4 for v in H) == I
assert tuple(v % 3 for v in H) == tuple(v % 3 for v in S)
assert multiply(H, inverse(conjugate(D, H))) == Z0
assert multiply(Z0, Z0) == I
assert conjugate(D, Z0) == Z0
assert multiply(Z0, R) == multiply(R, Z0)

# The finite reflected generator Z0*D has order two and reverses R.
T = multiply(Z0, D)
assert multiply(T, T) == I
assert conjugate(T, R) == inverse(R)
assert multiply(multiply(R, R), R) == I

print("Modulus:", MODULUS)
print("q([x,y]):", C)
print("h = [x,y] * x[x,y]x^-1")
print("q(h):", H)
print("q(h) modulo 4:", tuple(v % 4 for v in H))
print("q(h) modulo 3:", tuple(v % 3 for v in H))
print("q(h*d(h)^-1):", multiply(H, inverse(conjugate(D, H))))
print("z0*d has order two and inverts the named order-three R: True")
print("All assertions passed.")
