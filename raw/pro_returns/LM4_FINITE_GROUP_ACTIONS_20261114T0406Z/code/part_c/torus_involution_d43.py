#!/usr/bin/env python3
"""Exact Heisenberg-cover and representation certificates for D.43."""
from itertools import product
from pathlib import Path
import json


def rank_mod(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix]
    if not a:
        return 0
    m, n, pivot = len(a), len(a[0]), 0
    for col in range(n):
        row = next((i for i in range(pivot, m) if a[i][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        scale = pow(a[pivot][col], -1, p)
        a[pivot] = [v * scale % p for v in a[pivot]]
        # Eliminate below only; rank is all that is needed.
        for i in range(pivot + 1, m):
            factor = a[i][col]
            if factor:
                a[i] = [(u - factor * v) % p for u, v in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == m:
            break
    return pivot


def matmul(a, b, p):
    n, middle, m = len(a), len(b), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(middle)) % p
             for j in range(m)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def heisenberg(q):
    half = pow(2, -1, q)
    elements = list(product(range(q), repeat=3))
    def multiply(v, w):
        a, b, z = v
        c, d, t = w
        return ((a+c) % q, (b+d) % q,
                (z+t+half*(a*d-b*c)) % q)
    def inverse(v):
        return tuple(-a % q for a in v)
    return elements, multiply, inverse


def cover(q, field):
    group, mul, inv = heisenberg(q)
    index = {g: i for i, g in enumerate(group)}
    n = len(group)
    x, y, z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    one = (0, 0, 0)
    assert mul(mul(mul(x, y), inv(x)), inv(y)) == z
    for g in group:
        h = one
        for _ in range(q):
            h = mul(h, g)
        assert h == one
    # Each edge (g,k) joins g to g*generator[k].
    d1 = [[0] * (2*n) for _ in range(n)]
    for g in group:
        for k, generator in enumerate((x, y)):
            edge = 2*index[g] + k
            d1[index[g]][edge] -= 1
            d1[index[mul(g, generator)]][edge] += 1
    reps = [(a, b, 0) for a, b in product(range(q), repeat=2)]
    d2 = [[0] * len(reps) for _ in range(2*n)]
    relator = [(0, 1), (1, 1), (0, -1), (1, -1)] * q
    for cap, start in enumerate(reps):
        current = start
        for k, sign in relator:
            generator = (x, y)[k]
            if sign > 0:
                d2[2*index[current]+k][cap] += 1
                current = mul(current, generator)
            else:
                current = mul(current, inv(generator))
                d2[2*index[current]+k][cap] -= 1
        assert current == start
    assert all(sum(row) == 0 for row in d2)
    # Check the chain identity using the two endpoints of each edge.
    for cap in range(len(reps)):
        boundary = [0] * n
        for g in group:
            for k, generator in enumerate((x, y)):
                coefficient = d2[2*index[g]+k][cap]
                boundary[index[g]] -= coefficient
                boundary[index[mul(g, generator)]] += coefficient
        assert not any(boundary)
    r1, r2 = rank_mod(d1, field), rank_mod(d2, field)
    assert r1 == n-1 and r2 == q*q-1
    h1 = 2*n-r1-r2
    assert h1 == 2+q**3-q*q
    central = [[0] * (2*n) for _ in range(2*n)]
    for g in group:
        for k in range(2):
            central[2*index[mul(z, g)]+k][2*index[g]+k] = 1
    for cap in range(len(reps)):
        for g in group:
            for k in range(2):
                assert d2[2*index[mul(z, g)]+k][cap] == d2[2*index[g]+k][cap]
    root = next(a for a in range(2, field)
                if pow(a, q, field) == 1 and a != 1)
    dimensions = []
    for j in range(q):
        eigenvalue = pow(root, j, field)
        eigen_equations = [[(central[i][k] - (eigenvalue if i == k else 0)) % field
                            for k in range(2*n)] for i in range(2*n)]
        kernel_dimension = 2*n-rank_mod(d1+eigen_equations, field)
        dim = kernel_dimension-(r2 if j == 0 else 0)
        assert dim == (2 if j == 0 else q*q)
        dimensions.append(dim)
    # Explicit Schrödinger blocks and their rational inversion operator.
    X = [[int(i == (j+1) % q) for j in range(q)] for i in range(q)]
    J = [[int(i == (-j) % q) for j in range(q)] for i in range(q)]
    assert matmul(J, J, field) == ident(q)
    assert matmul(transpose(J), J, field) == ident(q)
    assert matmul(matmul(J, X, field), J, field) == transpose(X)
    for j in range(1, q):
        Y = [[pow(root, -j*i % q, field) if i == k else 0
              for k in range(q)] for i in range(q)]
        Yinv = [[pow(root, j*i % q, field) if i == k else 0
                 for k in range(q)] for i in range(q)]
        commutator = matmul(matmul(matmul(X, Y, field), transpose(X), field), Yinv, field)
        scalar = [[pow(root, j, field) if i == k else 0
                   for k in range(q)] for i in range(q)]
        assert commutator == scalar
        assert matmul(matmul(J, Y, field), J, field) == Yinv
        assert matmul(transpose(Y), Yinv, field) == ident(q)
    return {
        'q': q, 'group_order': n, 'coefficient_field': field,
        'vertices': n, 'edges': 2*n, 'caps': q*q,
        'boundary_one_rank': r1, 'boundary_two_rank': r2,
        'closed_genus': h1//2, 'closed_H1_dimension': h1,
        'central_eigenspace_dimensions': dimensions,
        'nontrivial_multiplicity': q,
        'Schrodinger_and_rational_implementer_checks': True,
        'all_checks_passed': True,
    }


def finite_automorphisms():
    q = 3
    group, mul, inv = heisenberg(q)
    vectors = list(product(range(q), repeat=2))
    identity, minus_identity = (1, 0, 0, 1), (2, 0, 0, 2)
    def vector(M, v):
        return ((M[0]*v[0]+M[1]*v[1]) % q,
                (M[2]*v[0]+M[3]*v[1]) % q)
    def automorphism(M, ell, g):
        det = (M[0]*M[3]-M[1]*M[2]) % q
        v = vector(M, g[:2])
        return v + ((det*g[2]+ell[0]*g[0]+ell[1]*g[1]) % q,)
    total, involutions, positive, conjugators = 0, 0, 0, []
    for M in product(range(q), repeat=4):
        determinant = (M[0]*M[3]-M[1]*M[2]) % q
        if determinant == 0:
            continue
        for ell in vectors:
            total += 1
            theta = {g: automorphism(M, ell, g) for g in group}
            if not all(theta[theta[g]] == g for g in group):
                continue
            involutions += 1
            for a in group:
                for b in group:
                    assert theta[mul(a, b)] == mul(theta[a], theta[b])
            if determinant != 1:
                continue
            positive += 1
            assert M in (identity, minus_identity)
            if M == identity:
                assert ell == (0, 0)
                continue
            # omega(u,v)=ell(v)/2.
            u = (ell[1]*2 % q, -ell[0]*2 % q, 0)
            def inner(h, g):
                return mul(mul(h, g), inv(h))
            for g in group:
                conjugated = inner(u, theta[inner(inv(u), g)])
                assert conjugated == ((-g[0]) % q, (-g[1]) % q, g[2])
            conjugators.append({'ell': ell, 'inner_conjugator': u})
    assert total == 432 and involutions == 46 and positive == 10
    return {'automorphisms': total, 'elements_with_square_one': involutions,
            'determinant_one_square_one': positive,
            'minus_identity_exact_conjugators': conjugators,
            'all_checks_passed': True}


def main():
    covers = [cover(3, 7), cover(5, 11)]
    automorphisms = finite_automorphisms()
    out = {'purpose': 'Exact Heisenberg cover and local representation validation for D43',
           'covers': covers, 'G3_automorphisms': automorphisms,
           'all_checks_passed': True}
    destination = Path(__file__).with_name('torus_involution_d43_output.json')
    destination.write_text(json.dumps(out, indent=2) + '\n')
    for case in covers:
        print('q=', case['q'], 'closed genus=', case['closed_genus'],
              'chain ranks=', case['boundary_one_rank'], case['boundary_two_rank'],
              'central-character dimensions=', case['central_eigenspace_dimensions'])
    print('All432 automorphisms of H3 enumerated; all46 with square1 checked.')
    print('All10 determinant-one cases have the proved exact normalization.')
    print('All Schrödinger and rational-implementer identities passed.')
    print('Wrote', destination)


if __name__ == '__main__':
    main()
