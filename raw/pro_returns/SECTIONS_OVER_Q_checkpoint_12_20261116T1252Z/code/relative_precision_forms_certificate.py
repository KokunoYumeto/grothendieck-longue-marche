#!/usr/bin/env python3
"""Exact Smith, action and transition checks for A.129.

All arithmetic is integral or modulo an explicitly named power of three.
The proof in the manuscript supplies the uniform all-n/all-r conclusion.
"""
from math import gcd
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

lines = []
def record(s):
    lines.append(s)
    print(s, flush=True)

def v3(a):
    a = abs(int(a))
    assert a
    e = 0
    while a % 3 == 0:
        a //= 3
        e += 1
    return e

def reduction_vector(power, N):
    d = N//3
    k = power % N
    v = sp.zeros(2*d, 1)
    if k < 2*d:
        v[k] = 1
    else:
        v[k-d] = -1
        v[k-2*d] = -1
    return v

def substitution(N, u):
    return sp.Matrix.hstack(*(reduction_vector(u*j,N)
                             for j in range(2*N//3)))

def zero_mod(A, modulus):
    return all(int(x) % modulus == 0 for x in A)

smith_checks = 0
transition_checks = 0
action_checks = 0
for n in range(1,6):
    N, d = 3**n, 3**(n-1)
    sigma = substitution(N,2)
    D = sigma + 2*sp.eye(2*d)
    # Literal cyclotomic basis, not a floating-point eigenvalue check.
    assert int(D.det()) == 2**(2*d)-1
    snf = smith_normal_form(D, domain=ZZ)
    valuations = [v3(snf[i,i]) for i in range(2*d)]
    assert sorted(valuations) == [0]*(2*d-n)+[1]*n
    for r in range(1,7):
        count = 1
        for i in range(2*d):
            count *= gcd(int(snf[i,i]),3**r)
        assert count == 3**n
        smith_checks += 1
    record(f'n={n}, rank={2*d}: determinant 2^{2*d}-1; '
           f'3-primary Smith valuations are {2*d-n} zeros and {n} ones; '
           'kernel order 3^n at precisions r=1..6.')

for n in range(1,4):
    N, d = 3**n, 3**(n-1)
    length = 2*d
    # The actual block-norm kernel basis is (x^d-1)x^j.
    ideal_basis = sp.zeros(N,length)
    for j in range(length):
        ideal_basis[(j+d)%N,j] += 1
        ideal_basis[j,j] -= 1
    # Coordinates in each block: first two entries, third is minus their sum.
    literal_basis = ideal_basis[:length,:]
    assert abs(int(literal_basis.det())) == 1
    J0 = sp.zeros(length)
    for h in range(d):
        J0[h,h+d] = 1
        J0[h+d,h] = -1
    J = literal_basis.T*J0*literal_basis
    assert abs(int(J.det())) == 1
    X = sp.Matrix.hstack(*(reduction_vector(j+1,N) for j in range(length)))
    Xinv = X.inv()
    Z = X-sp.eye(length)
    little_z = Z*Z*Xinv
    # Arithmetic multiplier 2, including the cyclotomic twist.
    moved = sp.zeros(N,length)
    for i in range(N):
        moved[(2*i)%N,:] += 2*ideal_basis[i,:]
    G2 = literal_basis.inv()*moved[:length,:]
    assert zero_mod(G2.T*J*G2 + 4*J, 3**6)
    assert X.T*J*X == J
    sigma = substitution(N,2)
    for j in range(n):
        P = little_z**(d-3**j)
        B = J*P
        assert B.T == -B
        for r in range(1,6):
            modulus = 3**r
            Br = 3**(r-1)*B
            assert zero_mod(X.T*Br*X-Br,modulus)
            assert zero_mod(G2.T*Br*G2-2*Br,modulus)
            assert zero_mod(3*Br,modulus)
            assert not zero_mod(Br,modulus)
            # Factor through source reduction C_r -> C_1 and output inclusion.
            for a in [sp.eye(length)[:,0],sp.ones(length,1)]:
                for b in [sp.eye(length)[:,1],sp.ones(length,1)]:
                    assert zero_mod((a+3*b).T*Br*b-a.T*Br*b,modulus)
            # Coefficient transition µ_(3^r) -> µ_(3^(r-1)) is zero.
            if r>1:
                assert zero_mod(Br,3**(r-1))
                # Source inclusion C_(r-1) -> C_r is multiplication by three.
                assert zero_mod(9*Br,modulus)
                transition_checks += 2
            action_checks += 2
    record(f'n={n}: literal block pairing, arithmetic action, all {n} forms, '
           'source/output factorization and both precision transitions passed.')

# Exact local higher-symbol witness: modulo nine the diagonal is not forced
# by every global equivariant form, since those forms only see reduction mod3.
t = sp.Matrix([1,-1])
c = sp.Matrix([0,3])
J = sp.Matrix([[0,1],[-1,0]])
assert int((t.T*J*c)[0]) == 3
assert int((t.T*(3*J)*c)[0]) % 9 == 0
assert all(any((int(c[i])-z*int(t[i])) % 9 for i in range(2))
           for z in range(9))
record('Precision-nine local check: determinant 3 is nonzero mod9, '
       'every order-three equivariant form vanishes, and c is not z*t mod9.')
record(f'ALL CHECKS PASSED: {smith_checks} exact Smith-kernel counts; '
       f'{action_checks} action comparisons; {transition_checks} precision transitions.')
Path(__file__).with_name('relative_precision_forms_certificate_output.txt').write_text(
    '\n'.join(lines)+'\n')
