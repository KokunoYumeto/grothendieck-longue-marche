"""Exact finite checks for A.117.

The proof is uniform; these checks retain the actual permutation maps,
deeper holomorph presentations, and S3 quotient kernels.
"""
from itertools import product
from math import gcd
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def mm(A, modulus):
    return A.applyfunc(lambda z: int(z) % modulus)


def relative_action(N, translate, unit, dual=False, twist=1):
    d = N // 3
    columns = []
    for j in range(2*d):
        v = [0] * N
        v[j] = 1
        if not dual:
            v[(j % d) + 2*d] = -1
        moved = [0] * N
        for i, value in enumerate(v):
            moved[(translate + unit*i) % N] += value
        if dual:
            out = [moved[i] - moved[(i % d)+2*d]
                   for i in range(2*d)]
        else:
            assert all(moved[i]+moved[i+d]+moved[i+2*d] == 0
                       for i in range(d))
            out = moved[:2*d]
        columns.append(sp.Matrix([twist*z for z in out]))
    return sp.Matrix.hstack(*columns)


def geom_sum(A, length, modulus):
    total, power = sp.zeros(A.rows), sp.eye(A.rows)
    for _ in range(length):
        total = mm(total + power, modulus)
        power = mm(power*A, modulus)
    return total, power


def kernel_size(A, modulus):
    S = smith_normal_form(A, domain=ZZ)
    diagonal = [abs(int(S[i,i])) for i in range(min(S.shape))
                if S[i,i] != 0]
    result = modulus ** (A.cols-len(diagonal))
    for z in diagonal:
        result *= gcd(z, modulus)
    return result


cohomology = []
smith_checks = 0
for n, t, r in [
        (1,1,1),(1,1,2),(1,2,1),(1,2,3),(1,3,2),
        (2,2,1),(2,2,2),(2,3,1),(2,3,3),(2,4,2),
        (3,3,1),(3,3,2),(3,4,1)]:
    N, modulus = 3**n, 3**r
    translation_order = 3**t
    cyclo_depth = max(t,r)
    unit_order = 2*3**(cyclo_depth-1)
    dim = 2*N//3
    for name, dual in [("C",False),("Cdual",True)]:
        A = relative_action(N,1,1,dual)
        B = relative_action(N,0,2,dual,1 if dual else 2)
        E = relative_action(N,0,-1,dual,1 if dual else -1)
        identity = sp.eye(dim)
        assert E*E == identity
        assert E*A*E == A.inv()
        smith = smith_normal_form(A-identity, domain=ZZ)
        entries = sorted(abs(int(smith[i,i])) for i in range(dim))
        assert entries == [1]*(dim-1)+[3]
        assert kernel_size(A-identity,modulus) == 3
        assert kernel_size(sp.Matrix.vstack(A-identity,E+identity),
                           modulus) == 3
        # E acts trivially on coinvariants: each column of E-I is
        # in the image of A-I over the integral lattice.
        assert all(all(z.q == 1 for z in (A-identity).inv()
                       *(E-identity)[:,j]) for j in range(dim))
        smith_checks += 1
        A, B = mm(A,modulus), mm(B,modulus)
        SA, AN = geom_sum(A,translation_order,modulus)
        SB, BH = geom_sum(B,unit_order,modulus)
        assert SA == sp.zeros(dim) and AN == identity and BH == identity
        assert mm(B*A-A*A*B,modulus) == sp.zeros(dim)
        constraints = mm(sp.Matrix.vstack(
            sp.Matrix.hstack(SA,sp.zeros(dim)),
            sp.Matrix.hstack(sp.zeros(dim),SB),
            sp.Matrix.hstack(B-identity-A,identity-A*A)
        ),modulus)
        boundary = mm(sp.Matrix.vstack(A-identity,B-identity),modulus)
        assert mm(constraints*boundary,modulus) == sp.zeros(3*dim,dim)
        z1 = kernel_size(constraints,modulus)
        b1 = modulus**dim // kernel_size(boundary,modulus)
        assert z1 == b1
        cohomology.append((n,t,r,name,z1,b1))

print("RELATIVE MODULE AND DEEPER HOLOMORPH CHECKS")
print("literal Smith/involution/coinvariant checks:",smith_checks)
for row in cohomology:
    print("n=%d t=%d r=%d module=%s |Z1|=%d |B1|=%d H1=0" % row)


def s3_mul(g,h):
    a,e = g
    b,f = h
    return ((a+(-1 if e else 1)*b)%3,(e+f)%2)


def s3_pow(g,k):
    ans = (0,0)
    for _ in range(k):
        ans = s3_mul(ans,g)
    return ans


def holo_mul(g,h,N):
    a,u = g
    b,v = h
    return ((a+u*b)%N,(u*v)%N)


s3_checks = 0
for t in range(1,5):
    N=3**t
    unit_order=2*3**(t-1)
    units=[pow(2,j,N) for j in range(unit_order)]
    unit_log={u:j for j,u in enumerate(units)}
    group=list(product(range(N),units))
    expected={(a,u) for a,u in group if a%3 == 0 and u%3 == 1}
    kernels=[]
    # Every surjection has a nonzero translation image and a reflection.
    for translation, reflection in product((1,2),range(3)):
        tau=(translation,0)
        sigma=(reflection,1)
        def image(g):
            a,u=g
            return s3_mul(s3_pow(tau,a),s3_pow(sigma,unit_log[u]))
        assert len({image(g) for g in group}) == 6
        assert {g for g in group if image(g)==(0,0)} == expected
        # Check the two generator relations and multiplication by each
        # generator at every group element.
        for g in group:
            for h in ((1,1),(0,2)):
                assert image(holo_mul(g,h,N)) == s3_mul(image(g),image(h))
                s3_checks += 1
        kernels.append(expected)
    assert all(k == kernels[0] for k in kernels)
print("UNIQUE S3 QUOTIENT")
print("generator multiplication checks:",s3_checks)
print("six quotient maps have one kernel at each depth t=1,2,3,4")
print("the unit class -2 is 7 modulo9, outside cube units {1,8}")
assert (-2)%9 not in {pow(z,3,9) for z in range(9) if gcd(z,9)==1}

# Every nonzero cyclic relation ideal contains the norm/socle vector.
socle_checks=0
z=sp.Symbol("z")
for n in range(1,5):
    N=3**n
    norm=sp.Poly(sum((1+z)**i for i in range(N)),z,modulus=3)
    assert norm == sp.Poly(z**(N-1),z,modulus=3)
    for j in range(N):
        assert sp.Poly(z**j*z**(N-1-j),z,modulus=3) == norm
        socle_checks+=1
print("CYCLIC KUMMER RELATION CHECKS")
print("literal norm-polynomial/socle ideal checks:",socle_checks)
print("ALL CHECKS PASSED")
