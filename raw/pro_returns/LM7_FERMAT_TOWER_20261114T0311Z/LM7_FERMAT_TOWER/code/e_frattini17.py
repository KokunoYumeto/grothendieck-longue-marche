#!/usr/bin/env python3
"""Independent finite fields, Fox module and uniform inert-prime certificate for E.59."""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = json.loads((BASE / "e_frattini17_certificate.json").read_text())


class Field:
    def __init__(self, p, polynomial):
        self.p = p
        self.mod = tuple(c % p for c in polynomial)
        self.n = len(polynomial) - 1
        assert self.mod[-1] == 1
        self.zero = (0,) * self.n
        self.one = (1,) + (0,) * (self.n - 1)
        self.x = (0, 1) + (0,) * (self.n - 2)

    def scalar(self, a):
        a = Fraction(a)
        v = a.numerator * pow(a.denominator % self.p, -1, self.p) % self.p
        return (v,) + (0,) * (self.n - 1)

    def add(self, a, b):
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x % self.p for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        c = [0] * (2 * self.n - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i+j] = (c[i+j] + x*y) % self.p
        for d in range(len(c)-1, self.n-1, -1):
            for j in range(self.n):
                c[d-self.n+j] = (c[d-self.n+j] - c[d]*self.mod[j]) % self.p
        return tuple(c[:self.n])

    def power(self, a, n):
        if n < 0:
            return self.power(a, n % (self.p**self.n - 1))
        b = self.one
        while n:
            if n & 1:
                b = self.mul(b, a)
            a = self.mul(a, a)
            n //= 2
        return b

    def evaluate(self, coefficients, a):
        b = self.zero
        for c in reversed(coefficients):
            b = self.add(self.mul(b, a), self.scalar(c))
        return b


def rref(A):
    A = [[x % 3 for x in row] for row in A]
    pivots = []
    row = 0
    for col in range(len(A[0])):
        pivot = next((i for i in range(row, len(A)) if A[i][col]), None)
        if pivot is None:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        inv = pow(A[row][col], -1, 3)
        A[row] = [(inv*x) % 3 for x in A[row]]
        for i in range(len(A)):
            if i != row and A[i][col]:
                f = A[i][col]
                A[i] = [(x-f*y) % 3 for x, y in zip(A[i], A[row])]
        pivots.append(col)
        row += 1
        if row == len(A):
            break
    return A, pivots


def rank(A):
    return len(rref(A)[1])


def kernel(A):
    R, piv = rref(A)
    out = []
    for j in range(len(A[0])):
        if j in piv:
            continue
        v = [0] * len(A[0])
        v[j] = 1
        for i, k in enumerate(piv):
            v[k] = -R[i][j] % 3
        out.append(v)
    return transpose(out)


def transpose(A):
    return [list(x) for x in zip(*A)]


def mm(A, B):
    return [[sum(a*b for a, b in zip(row, col)) % 3
             for col in zip(*B)] for row in A]


def sub(A, B):
    return [[(x-y) % 3 for x, y in zip(a, b)] for a, b in zip(A, B)]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def prime_match(F, values, ideals):
    matches = []
    for k, H in enumerate(ideals):
        tests = []
        for col in zip(*H):
            v = F.zero
            for c, w in zip(col, values):
                v = F.add(v, F.mul(F.scalar(c), w))
            tests.append(v == F.zero)
        if all(tests):
            matches.append(k)
    assert len(matches) == 1, matches
    return matches[0]


def check_residues(p):
    if p == 17:
        F = Field(17, [1, 1, 1])
        omega = F.x
        roots = [a for a in product(range(17), repeat=2)
                 if F.power(a, 3) == omega]
        assert len(roots) == 3
        pairs = [(z, F.mul(F.scalar(7), F.power(omega, j)))
                 for z in roots for j in range(3)]
        expected, ideals, exponent = DATA["frobenius17"], DATA["primes17"], 96
    else:
        F = Field(2, [1, 0, 0, 1, 0, 0, 1])
        z = F.x
        omega = F.power(z, 3)
        pairs = [(z, F.power(omega, j)) for j in range(3)]
        expected, ideals, exponent = DATA["frobenius2_cubes"], DATA["primes2"], 21
    seen = set()
    checks = 0
    for z, root3 in pairs:
        theta = F.sub(root3, z)
        assert F.evaluate(DATA["polynomial"], theta) == F.zero
        assert F.evaluate(DATA["zeta9"], theta) == z
        assert F.evaluate(DATA["root3"], theta) == root3
        assert F.power(z, 9) == F.one and F.power(z, 3) != F.one
        vals = [F.evaluate(v, theta) for v in DATA["integral_basis"]]
        k = prime_match(F, vals, ideals)
        assert k not in seen
        seen.add(k)
        for i, unit in enumerate(DATA["units"]):
            q = F.power(F.evaluate(unit, theta), exponent)
            assert q == F.power(F.power(z, 3), expected[i][k]), (p, i, k)
            checks += 1
    assert len(seen) == len(ideals)
    return checks


assert check_residues(17) == 90
assert check_residues(2) == 30
M, N = DATA["frobenius17"], DATA["frobenius2_cubes"]
assert rank(M) == 5
assert all(sum(row) % 3 == 0 for row in M)
assert all(any(col) for col in zip(*M))
relations = kernel(M)
assert len(relations[0]) == 4
assert mm(M, relations) == [[0]*4 for _ in range(10)]
X, Y, C = DATA["actions"]
I = eye(10)
assert mm(mm(X, X), X) == I and mm(mm(Y, Y), Y) == I
assert mm(X, Y) == mm(Y, X)
assert mm(C, C) == I
assert mm(mm(C, X), C) == X
assert mm(mm(C, Y), C) == mm(Y, Y)
dx, dy = sub(X, I), sub(Y, I)
stack = mm(dx, dx) + mm(dx, dy) + mm(dy, dy)
W, Wminus = DATA["low_units"], DATA["low_minus_units"]
assert rank(W) == 5 and rank(stack) == 5
assert mm(stack, W) == [[0]*5 for _ in range(30)]
assert rank(Wminus) == 2
assert mm(sub(C, [[-x % 3 for x in row] for row in I]), Wminus) == [[0]*2 for _ in range(10)]
low17, low2 = mm(transpose(Wminus), M), mm(transpose(Wminus), N)
assert low17 == [[1]*9, [2]*9]
assert low2 == [[1]*3, [1]*3]
h = [[(a-b) % 3] for a, b in Wminus]
gamma = [[x] for x in DATA["heisenberg_vector"]]
assert mm(sub(mm(Y, Y), I), h) == gamma
assert mm(transpose(gamma), N) == [[0]*3]
assert DATA["triple_pairing"] == 1
assert mm(transpose(h), M) == [[2]*9]
assert mm(transpose(h), N) == [[0]*3]

# An independent Fox model of Phi(P)/Phi(Phi(P)).
monomials = [(i, j) for i in range(3) for j in range(3)]
pos = {a: i for i, a in enumerate(monomials)}
def monomial_matrix(di, dj):
    A = [[0]*9 for _ in range(9)]
    for k, (i, j) in enumerate(monomials):
        if i+di < 3 and j+dj < 3:
            A[pos[i+di, j+dj]][k] = 1
    return A
FX, FY = monomial_matrix(1, 0), monomial_matrix(0, 1)
boundary = [a+b for a, b in zip(FX, FY)]
cycles = kernel(boundary)
assert rank(cycles) == 10
blockX = [row+[0]*9 for row in FX] + [[0]*9+row for row in FX]
blockY = [row+[0]*9 for row in FY] + [[0]*9+row for row in FY]
J2 = [a+b+c for a, b, c in zip(
    mm(mm(blockX, blockX), cycles),
    mm(mm(blockX, blockY), cycles),
    mm(mm(blockY, blockY), cycles))]
assert rank(J2) == 5
fullnorm = monomial_matrix(2, 2)
blocknorm = [row+[0]*9 for row in fullnorm] + [[0]*9+row for row in fullnorm]
assert mm(blocknorm, cycles) == [[0]*10 for _ in range(18)]

# The short cross ratio gives the actual low character without a chosen
# fundamental-unit expression.
assert DATA["cross_ratio_vector"] == [row[0] for row in h]
for p in [2, 17]:
    if p == 2:
        F = Field(2, [1, 0, 0, 1, 0, 0, 1])
        z = F.x
        rr = F.one
        expected_h = 0
    else:
        F = Field(17, [1, 1, 1])
        z = next(a for a in product(range(17), repeat=2)
                 if F.power(a, 3) == F.x)
        rr = F.scalar(7)
        expected_h = 2
    omega = F.power(z, 3)
    def cross_ratio(F, z, rr):
        omega = F.power(z, 3)
        def u_at(w):
            return F.neg(F.mul(F.power(w, 2),
                               F.power(F.sub(F.one, w), 2)))
        u, u1 = u_at(z), u_at(F.power(z, 4))
        rm = F.mul(F.power(omega, 2), rr)
        numer = F.mul(F.sub(rr, u), F.sub(rm, u1))
        denom = F.mul(F.sub(rm, u), F.sub(rr, u1))
        assert numer != F.zero and denom != F.zero
        return F.mul(numer, F.power(denom, -1))
    hh = cross_ratio(F, z, rr)
    theta = F.sub(rr, z)
    assert hh == F.evaluate(DATA["cross_ratio"], theta)
    assert F.power(hh, (F.p**F.n-1)//3) == F.power(omega, expected_h)

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))

def primitive_ninth_root(F):
    for a in product(range(F.p), repeat=2):
        if a == F.zero:
            continue
        z = F.power(a, (F.p**2-1)//9)
        if F.power(z, 3) != F.one:
            return z
    raise AssertionError("ninth root not found")

uniform = []
uniform_checks = 0
deeper_matrices = []
for p in range(17, 2001, 9):
    if not is_prime(p):
        continue
    F = Field(p, [1, 1, 1])
    z = primitive_ninth_root(F)
    omega = F.power(z, 3)
    rr = F.scalar(pow(3, pow(3, -1, p-1), p))
    assert F.power(rr, 3) == F.scalar(3)
    a = ((p*p-1)//9) % 3
    bvalues = set()
    for i, j in product(range(3), repeat=2):
        zi = F.power(z, 1+3*i)
        rj = F.mul(rr, F.power(omega, j))
        hh = cross_ratio(F, zi, rj)
        symbol = F.power(hh, (p*p-1)//3)
        b = next(k for k in range(3) if symbol == F.power(omega, k))
        bvalues.add(b)
        assert F.power(zi, (p*p-1)//3) == F.power(omega, a)
        # This direct finite identity also checks the exact Heisenberg
        # normalization in every residue field used here.
        def unit(w):
            return F.neg(F.mul(F.power(w, 2),
                               F.power(F.sub(F.one, w), 2)))
        uu = [unit(F.power(zi, 4**k)) for k in range(3)]
        assert F.mul(F.mul(uu[0], uu[1]), uu[2]) == F.scalar(3)
        uniform_checks += 1
    assert len(bvalues) == 1
    b = bvalues.pop()
    row = {"prime": p, "x_cube_coefficient": a,
           "triple_bracket_coefficient": b}
    if b:
        row["Frattini_orbit_rank"] = 5
    elif a:
        row["Frattini_orbit_rank"] = 3
    else:
        cols = []
        for i, j in product(range(3), repeat=2):
            zi = F.power(z, 1+3*i)
            rj = F.mul(rr, F.power(omega, j))
            theta = F.sub(rj, zi)
            col = []
            for coeffs in DATA["units"]:
                value = F.evaluate(coeffs, theta)
                assert value != F.zero
                symbol = F.power(value, (p*p-1)//3)
                col.append(next(k for k in range(3)
                                if symbol == F.power(omega, k)))
            cols.append(col)
        matrix = transpose(cols)
        row["Frattini_orbit_rank"] = rank(matrix)
        deeper_matrices.append({"prime":p, "matrix":matrix,
                                "rank":rank(matrix)})
    uniform.append(row)
assert next(t for t in uniform if t["prime"] == 17) == {
    "prime":17, "x_cube_coefficient":2, "triple_bracket_coefficient":2,
    "Frattini_orbit_rank":5}

result = {
    "status": "PASS",
    "independent_cubic_residue_checks": 120,
    "frobenius17_rank": 5,
    "four_relations": relations,
    "every_frobenius_nonzero": True,
    "sum_of_nine_frobenii": [0]*10,
    "fox_module_dimension": 10,
    "fox_augmentation_squared_dimension": 5,
    "low_conjugation_fixed_dimension": 2,
    "degree_three_word": "x^6 [y,[x,y]]^2 modulo D_4(P)",
    "exact_Frattini_depth": 1,
    "exact_Zassenhaus_depth": 3,
    "uniform_inert_prime_count": len(uniform),
    "uniform_prolongation_checks": uniform_checks,
    "uniform_inert_prime_table": uniform,
    "deeper_Frobenius_matrices": deeper_matrices,
    "additional_deeper_cubic_residue_checks": 90*len(deeper_matrices),
}
(BASE / "e_frattini17.json").write_text(json.dumps(result, indent=2)+"\n")
print("PASS 120 independent cubic-residue calculations with exact prime-ideal matching")
print("PASS rank5, four independent relations, nonzero columns, universal norm relation")
print("PASS exact C3^2 and conjugation matrices, five-dimensional low quotient")
print("PASS explicit Heisenberg comparison and Frobenius word x^6 [y,[x,y]]^2 mod D4")
print("PASS independent ten-dimensional Fox module and rank5 augmentation-square layer")
print(f"PASS uniform cross-ratio formula at {len(uniform)} inert primes through2000")
print(f"PASS {uniform_checks} prolongation-invariance and Heisenberg-norm checks")
print("PASS actual deeper orbit ranks",
      [(r["prime"],r["rank"]) for r in deeper_matrices])
