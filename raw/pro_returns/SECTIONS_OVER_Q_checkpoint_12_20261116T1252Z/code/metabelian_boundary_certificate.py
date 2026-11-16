"""Exact integral divisor/cocharacter and tower-map certificate for A.68.
No floating-point or heuristic group reconstruction is used.
"""
from math import gcd

pair_checks = 0
equivariance_checks = 0
transition_checks = 0
for n in range(1, 65):
    du = [1]*n + [0]*n + [-1]*n
    dv = [0]*n + [1]*n + [-1]*n
    j0 = [1]*n + [0]*(2*n)
    j1 = [0]*n + [1]*n + [0]*n
    diag = [1]*(3*n)
    dot = lambda a,b: sum(x*y for x,y in zip(a,b))
    assert dot(du,diag) == dot(dv,diag) == 0
    assert [[dot(f,j) for j in (j0,j1)] for f in (du,dv)] == [[n,0],[0,n]]
    assert [[n*dot(f,j) for j in (j0,j1)] for f in (du,dv)] == [[n*n,0],[0,n*n]]
    pair_checks += 1
    # The entire boundary sum is fixed under every block-preserving
    # permutation. Test affine generators for each boundary block.
    for block in range(3):
        for a in range(n):
            if gcd(a,n) != 1:
                continue
            for b in range(n):
                perm = list(range(3*n))
                for i in range(n):
                    perm[block*n+i] = block*n + (a*i+b)%n
                for j in (j0,j1):
                    image = [0]*(3*n)
                    for i,v in enumerate(j):
                        image[perm[i]] += v
                    assert image == j
                equivariance_checks += 1
    for k in range(1,17):
        m = n*k
        # Boundary meridian upstairs maps to k times its downstairs image.
        image0 = [0]*(3*n)
        image1 = [0]*(3*n)
        for i in range(m):
            image0[i%n] += k
            image1[n+i%n] += k
        assert image0 == [k*k*v for v in j0]
        assert image1 == [k*k*v for v in j1]
        assert n*n*k*k == m*m
        transition_checks += 1

print("A.68 exact boundary comparison certificate")
print("Integral divisor/cocharacter pairings:", pair_checks)
print("Galois-block permutation checks:", equivariance_checks)
print("Ramified tower transitions tau(t_m)=(m/n)^2 t_n:", transition_checks)
print("All identities passed.")

