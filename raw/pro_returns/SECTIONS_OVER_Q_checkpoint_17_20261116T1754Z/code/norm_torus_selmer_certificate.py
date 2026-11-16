"""Exact finite checks for A.109--A.110; no analytic inference from sampling."""
from itertools import product
from math import gcd
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def mod_matrix(mat, modulus):
    return mat.applyfunc(lambda value: int(value) % modulus)


def permutation_action(N, translate, unit, quotient, twist, modulus):
    d = N - 1
    columns = []
    for j in range(d):
        vector = [0] * N
        vector[j] = 1
        if not quotient:
            vector[-1] = -1
        moved = [0] * N
        for i, value in enumerate(vector):
            moved[(translate + unit * i) % N] += value
        if quotient:
            column = [moved[i] - moved[-1] for i in range(d)]
        else:
            assert sum(moved) == 0
            column = moved[:-1]
        columns.append(sp.Matrix([(twist * value) % modulus for value in column]))
    return sp.Matrix.hstack(*columns)


def geom_sum(A, length, modulus):
    result = sp.zeros(A.rows)
    power = sp.eye(A.rows)
    for _ in range(length):
        result = mod_matrix(result + power, modulus)
        power = mod_matrix(power * A, modulus)
    return result, power


def kernel_size(matrix, modulus):
    diagonal = smith_normal_form(matrix, domain=ZZ)
    values = [abs(int(diagonal[i, i])) for i in range(min(diagonal.shape))
              if diagonal[i, i] != 0]
    answer = modulus ** (matrix.cols - len(values))
    for value in values:
        answer *= gcd(value, modulus)
    return answer


checks = []
for n, r in [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1)]:
    N, modulus = 3**n, 3**r
    cyclotomic = 3 ** max(n, r)
    h = 2 * cyclotomic // 3
    d = N - 1
    for name, quotient, twisted in [("M", False, True), ("J", True, False)]:
        A = permutation_action(N, 1, 1, quotient, 1, modulus)
        B = permutation_action(N, 0, 2, quotient, 2 if twisted else 1, modulus)
        SA, AN = geom_sum(A, N, modulus)
        SB, BH = geom_sum(B, h, modulus)
        identity = sp.eye(d)
        assert AN == identity and BH == identity
        assert mod_matrix(B * A - A * A * B, modulus) == sp.zeros(d)
        constraints = sp.Matrix.vstack(
            sp.Matrix.hstack(SA, sp.zeros(d)),
            sp.Matrix.hstack(sp.zeros(d), SB),
            sp.Matrix.hstack(B - identity - A, identity - A * A),
        )
        constraints = mod_matrix(constraints, modulus)
        coboundary = sp.Matrix.vstack(A - identity, B - identity)
        coboundary = mod_matrix(coboundary, modulus)
        assert mod_matrix(constraints * coboundary, modulus) == sp.zeros(3*d, d)
        cocycles = kernel_size(constraints, modulus)
        boundaries = modulus**d // kernel_size(coboundary, modulus)
        assert cocycles == boundaries
        checks.append((n, r, name, cocycles, boundaries))

print("PRESENTATION-COHOMOLOGY CHECKS")
for check in checks:
    print("n=%d r=%d module=%s |Z1|=%d |B1|=%d H1=0" % check)


N = 9
def f(value):
    value %= N
    return value // 3 if value % 3 == 0 else 0

W = sp.Matrix(N, N, lambda i, j: f(j-i))
W = mod_matrix(W, 3)
assert mod_matrix(W + W.T, 3) == sp.zeros(N)
one = sp.ones(N, 1)
assert mod_matrix(W * one, 3) == sp.zeros(N, 1)
equivariance_checks = 0
for translate in range(N):
    for unit in range(N):
        if gcd(unit, N) != 1:
            continue
        C = sp.zeros(N)
        for i in range(N):
            C[(translate + unit*i) % N, i] = unit % 3
        assert mod_matrix(C.T * W * C - (unit % 3) * W, 3) == sp.zeros(N)
        equivariance_checks += 1

t = sp.zeros(N, 1)
c = sp.zeros(N, 1)
t[0], t[1] = 1, -1
c[3], c[2] = 1, -1
assert int((t.T * W * c)[0]) % 3 == 1

graph_checks = 0
for coordinates in product(range(3), repeat=N-1):
    v = sp.Matrix([*coordinates, -sum(coordinates) % 3])
    Wv = W * v
    vv = int((v.T * Wv)[0]) % 3
    vo = int((v.T * W * one)[0]) % 3
    assert vv == 0 and vo == 0
    for z, w in product(range(3), repeat=2):
        assert (z * vv + w * vo) % 3 == 0
        graph_checks += 1

group = list(product(range(3), repeat=2))
def add(x, y):
    return ((x[0]+y[0]) % 3, (x[1]+y[1]) % 3)

def qform(g, h):
    return 2 * (g[0]*h[1] - g[1]*h[0]) % 3

cochain_checks = 0
for g, h, k in product(group, repeat=3):
    assert (qform(h, k) - qform(add(g, h), k)
            + qform(g, add(h, k)) - qform(g, h)) % 3 == 0
    cochain_checks += 1
assert (qform((1, 0), (0, 1)) - qform((0, 1), (1, 0))) % 3 == 1

for prime in sp.primerange(5, 100000):
    if prime % 9 == 1 and pow(3, (prime-1)//9, prime) == 1:
        q = int(prime)
        break
else:
    raise AssertionError("explicit splitting-prime search failed")
root = next(x for x in range(1, q) if pow(x, 9, q) == 3)
unit = int(sp.primitive_root(q))
assert sp.isprime(q) and pow(root, 9, q) == 3
assert pow(unit, (q-1)//3, q) != 1
roots = sorted(x for x in range(1, q) if pow(x, 9, q) == 3)
assert len(roots) == 9
print("ALTERNATING BRAUER FORM")
print("arithmetic equivariance identities:", equivariance_checks)
print("diagonal-shift graph isotropy identities:", graph_checks)
print("literal normalized 2-cocycle identities:", cochain_checks)
print("B(e0-e1,e3-e2)=1; commutator of half-cup=1")
T_basis = sp.Matrix.hstack(*[
    sp.Matrix([sp.binomial(k, i)*(-1)**(k-i) % 3 if i <= k else 0
               for i in range(N)]) for k in range(1, N)])
gram = mod_matrix(T_basis.T * W * T_basis, 3)
assert gram[4:, :] == sp.zeros(4, 8)
assert gram[:, 4:] == sp.zeros(8, 4)
assert int(gram[:4, :4].det()) % 3 != 0
print("three-adic quotient Gram matrix:", gram[:4, :4].tolist())
print("coefficient radical is exactly T^5 through T^8")
c_bad = sp.zeros(N, 1)
c_bad[3], c_bad[4] = 1, -1
assert int((t.T * W * c_bad)[0]) % 3 == 2
print("A106 comparison B(e0-e1,e3-e4)=2")
quadratic_checks = 0
for coefficients in product((1, 2), repeat=4):
    values = {sum(a*x*x for a, x in zip(coefficients, coordinates)) % 3
              for coordinates in product(range(3), repeat=4)}
    assert values == {0, 1, 2}
    quadratic_checks += 1
print("nondegenerate diagonal four-variable quadratic value tests:", quadratic_checks)
print("explicit q =", q, "; primitive unit =", unit,
      "; ninth root of 3 =", root)
print("all nine roots:", roots)
print("unit cubic character:", pow(unit, (q-1)//3, q))
print("ALL CHECKS PASSED")
