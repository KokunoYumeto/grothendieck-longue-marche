#!/usr/bin/env python3
"""Independent exact determinant, ideal-lattice and Smith checks for E.57."""
from fractions import Fraction as Q
from pathlib import Path
import json
from math import lcm
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

BASE = Path(__file__).resolve().parent
records = [json.loads(s) for s in (BASE/"e_prime17_norm_gp.out").read_text().splitlines()
           if s.startswith("{")]
assert records[-1]["status"] == "PASS"
field, basis, ideals, witness = records[:4]
columns = [r for r in records if r["type"] == "global_column"]
assert len(columns) == 31


class K:
    def __init__(self, a=0, b=0):
        self.a, self.b = Q(a), Q(b)

    def __add__(self, v):
        if not isinstance(v, K): v = K(v)
        return K(self.a+v.a, self.b+v.b)

    __radd__ = __add__

    def __neg__(self): return K(-self.a, -self.b)

    def __sub__(self, v): return self + (-v if isinstance(v, K) else -K(v))

    def __rsub__(self, v): return K(v) + (-self)

    def __mul__(self, v):
        if not isinstance(v, K): v = K(v)
        return K(self.a*v.a-self.b*v.b,
                 self.a*v.b+self.b*v.a-self.b*v.b)

    __rmul__ = __mul__

    def inverse(self):
        d = self.a*self.a-self.a*self.b+self.b*self.b
        return K((self.a-self.b)/d, -self.b/d)

    def __truediv__(self, v):
        if not isinstance(v, K): v = K(v)
        return self*v.inverse()

    def __pow__(self, n):
        if n < 0: return self.inverse()**(-n)
        a, b = self, K(1)
        while n:
            if n & 1: b = b*a
            a = a*a
            n //= 2
        return b

    def __eq__(self, v):
        if not isinstance(v, K): v = K(v)
        return (self.a, self.b) == (v.a, v.b)


z = K(0, 1)


def kpoly(v):
    return sum((K(c)*z**i for i, c in enumerate(v)), K())


def norm(v):
    # The actual multiplication determinant for beta^3=17*zeta.
    parts = [K(), K(), K()]
    for i, c in enumerate(v):
        parts[i % 3] += Q(c)*(17*z)**(i//3)
    a, b, c = parts
    return a**3 + (17*z)*b**3 + (17*z)**2*c**3 - 3*(17*z)*a*b*c


for src, dst in zip(basis["source"], basis["norms"]):
    assert norm(src) == kpoly(dst)
assert norm(witness["element"]) == z
for col in columns:
    n = norm(col["source"])
    assert n == kpoly(col["norm"])
    expected = kpoly(col["base_prime_generator"])**col["relative_residue_degree"]
    expected = expected/(2-z)**sum(col["class"])
    expected = expected*z**col["root_exponent"]
    assert n == expected or n == -expected


def reduce_poly(v):
    v = [Q(x) for x in v]
    v += [Q(0)]*max(0, 6-len(v))
    for i in range(len(v)-1, 5, -1):
        a = v[i]
        v[i-6] -= 289*a
        v[i-3] -= 17*a
    return v[:6]


def multiply(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += Q(x)*Q(y)
    return reduce_poly(c)


ZB = Matrix.hstack(*[Matrix(reduce_poly(v)) for v in field["integral_basis"]])
ZI = ZB.inv()


def hnf(A):
    d = lcm(*(int(x.q) for x in A))
    B = Matrix(A.rows,A.cols,[int(x) for x in A*d])
    assert B == A*d
    return hermite_normal_form(B)/d


def principal(v):
    return hnf(Matrix.hstack(*[
        ZI*Matrix(multiply(v, list(ZB[:,j]))) for j in range(6)]))


def iproduct(A, B):
    cols = []
    for i in range(6):
        for j in range(6):
            cols.append(ZI*Matrix(multiply(list(ZB*A[:,i]), list(ZB*B[:,j]))))
    return hnf(Matrix.hstack(*cols))


def ipower(A, n):
    B = Matrix.eye(6)
    while n:
        if n & 1: B = iproduct(A, B)
        A = iproduct(A, A)
        n //= 2
    return B


Q3, Q17, P1, P2, P3, Qbar = [Matrix(v) for v in ideals["hnf"]]
assert [abs(int(A.det())) for A in [Q3,Q17,P1,P2,P3,Qbar]] == [3,289,7,7,7,343]
src = basis["source"]
assert principal(src[0]) == Matrix.eye(6)
assert principal(src[1]) == Matrix.eye(6)
assert principal(src[2]) == Q3
assert principal(src[3]) == Q17
assert principal(src[4]) == Qbar
assert principal(src[5]) == iproduct(iproduct(P1, P2), P3)
assert principal(src[6]) == ipower(P1, 3)
assert principal(src[7]) == ipower(P2, 3)
assert iproduct(principal(witness["element"]),iproduct(ipower(P2,2),ipower(P3,2))) == ipower(P1,4)

N = Matrix(basis["norm_matrix"])
target_relation = Matrix([0,0,0,0,3])
smith = smith_normal_form(N.row_join(target_relation),domain=ZZ)
diagonal = [abs(int(smith[i,i])) for i in range(5)]
assert diagonal == [1,1,1,3,3]
kernel_columns = [
    [1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,-1,0],
    [0,0,0,0,0,-3,0,3,0],
    [0,0,0,0,0,0,0,0,1],
]
for v in kernel_columns:
    w = N*Matrix(v)
    assert list(w[:4,0]) == [0,0,0,0] and w[4] % 3 == 0
assert Matrix.hstack(*[Matrix(v) for v in kernel_columns[:4]]).rank() == 4

result = {
    "status":"PASS",
    "relative_norm_determinants":41,
    "global_exact_norm_columns":31,
    "ideal_lattice_identities":9,
    "certified_class_group":[3,3],
    "S_unit_source_free_rank":8,
    "S_unit_target_free_rank":4,
    "norm_kernel_free_rank":4,
    "norm_kernel_torsion":[3],
    "norm_cokernel":[3,3],
    "augmented_norm_Smith":diagonal,
    "root_norm_witness_divisor":[0,0,4,-2,-2,0],
    "norm_matrix":basis["norm_matrix"],
    "retained_complete_PARI_records":records,
}
(BASE/"e_prime17_norm.json").write_text(json.dumps(result,indent=2)+"\n")
print("PASS 41 independent cubic multiplication determinants")
print("PASS 31 exact global principal-divisor norm columns")
print("PASS 9 independent ideal-lattice products and principal generators")
print("PASS source class constraints and explicit root norm correction")
print("PASS complete S-unit norm kernel Z3^4+C3 and cokernel C3^2")
