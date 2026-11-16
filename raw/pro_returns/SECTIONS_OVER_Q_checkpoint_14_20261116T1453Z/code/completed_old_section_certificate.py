#!/usr/bin/env python3
"""Exact finite checks for A.93's geometric quotient and cross cocycle.

The script uses finite semidirect products to check the literal cochain
formulas and the actual 64-sheet Schreier graph. It does not replace the
cohomology comparison or global Brauer reciprocity proof by enumeration.
"""
from collections import deque
from itertools import product


def matrix_product(a, b):
    return ((a[0]*b[0] + a[1]*b[2]) % 2,
            (a[0]*b[1] + a[1]*b[3]) % 2,
            (a[2]*b[0] + a[3]*b[2]) % 2,
            (a[2]*b[1] + a[3]*b[3]) % 2)


def matrix_vector(a, v):
    x, y = v & 1, v >> 1
    return ((a[0]*x + a[1]*y) % 2
            + 2*((a[2]*x + a[3]*y) % 2))


def dot(a, b):
    return (a & b).bit_count() % 2


def dual_action(g, phi, inverses):
    return sum(dot(phi, matrix_vector(inverses[g], 1 << i)) << i
               for i in range(2))


def covering_graph():
    vertices = tuple(product(range(4), repeat=3))
    indices = {v: i for i, v in enumerate(vertices)}
    edges = []
    adjacency = [[] for _ in vertices]
    for v in vertices:
        for j in range(3):
            w = list(v)
            w[j] = (w[j] + 1) % 4
            w = tuple(w)
            index = len(edges)
            edges.append((indices[v], indices[w]))
            adjacency[indices[v]].append((indices[w], index))
            adjacency[indices[w]].append((indices[v], index))
    visited = {0}
    tree = set()
    todo = deque([0])
    while todo:
        v = todo.popleft()
        for w, e in adjacency[v]:
            if w not in visited:
                visited.add(w)
                tree.add(e)
                todo.append(w)
    assert len(visited) == 64
    assert len(edges) == 192
    assert len(tree) == 63
    assert len(edges) - len(tree) == 129
    # Independent row reduction of the F2 incidence columns.
    pivots = {}
    for v, w in edges:
        column = (1 << v) ^ (1 << w)
        while column:
            p = column.bit_length()-1
            if p not in pivots:
                pivots[p] = column
                break
            column ^= pivots[p]
    assert len(pivots) == 63
    assert 192-len(pivots) == 129
    order = 4**3 * 2**129
    assert order == 2**135
    print("Actual (Z/4)^3 Schreier graph: 64 vertices, 192 edges, 63 tree edges, rank 129.")
    print(f"Independent incidence rank: {len(pivots)}; geometric quotient order: 2^135 = {order}.")
    basis = tuple(product(range(4), repeat=3))
    assert len(basis) == 64 and max(map(sum, basis)) == 9
    degree_ten = [(a, b, 10-a-b) for a in range(11)
                  for b in range(11-a)]
    assert all(max(monomial) >= 4 for monomial in degree_ten)
    assert len(degree_ten) == 66
    print("Augmentation ring: 64 basis monomials; all 66 degree-ten monomials vanish, so Gamma_12=1.")


def matrix_cases():
    identity = (1, 0, 0, 1)
    gl = tuple(a for a in product((0, 1), repeat=4)
               if (a[0]*a[3]-a[1]*a[2]) % 2 == 1)
    order_three = (0, 1, 1, 1)
    cyclic_three = (identity, order_three, matrix_product(order_three, order_three))
    cocycles = triples = changes = edges = 0
    for group in (cyclic_three, gl):
        inverses = {g: next(h for h in group if matrix_product(g, h) == identity)
                    for g in group}
        elements = tuple(product(range(4), group))

        def multiply(a, b):
            h, g = a
            k, r = b
            return h ^ matrix_vector(g, k), matrix_product(g, r)

        for phi in range(4):
            eta = {g: phi ^ dual_action(g, phi, inverses) for g in group}
            assert eta[identity] == 0
            for g, r in product(group, repeat=2):
                assert eta[matrix_product(g, r)] == (
                    eta[g] ^ dual_action(g, eta[r], inverses))

            def cross(a, b):
                return dot(eta[a[1]], matrix_vector(a[1], b[0]))

            for a, b, c in product(elements, repeat=3):
                assert (cross(b, c) ^ cross(multiply(a, b), c)
                        ^ cross(a, multiply(b, c)) ^ cross(a, b)) == 0
                triples += 1
            for g in group:
                for h in range(4):
                    assert cross((0, g), (h, identity)) == dot(
                        eta[g], matrix_vector(g, h))
                    edges += 1
            for correction in range(4):
                eta_new = {g: eta[g] ^ correction
                           ^ dual_action(g, correction, inverses) for g in group}
                for a, b in product(elements, repeat=2):
                    cross_new = dot(eta_new[a[1]], matrix_vector(a[1], b[0]))
                    delta = (dot(correction, a[0]) ^ dot(correction, b[0])
                             ^ dot(correction, multiply(a, b)[0]))
                    assert cross_new ^ cross(a, b) == delta
                    changes += 1
            for h, k in product(range(4), repeat=2):
                assert cross((h, identity), (k, identity)) == 0
            for g, r in product(group, repeat=2):
                assert cross((0, g), (0, r)) == 0
            cocycles += 1

    # A nonzero H1 class: trivial action of G=C2 on H=F2.
    elements = tuple(product((0, 1), repeat=2))
    def multiply(a, b):
        return a[0] ^ b[0], a[1] ^ b[1]
    for eta_generator in (0, 1):
        def cross(a, b):
            return eta_generator * a[1] * b[0]
        for a, b, c in product(elements, repeat=3):
            assert (cross(b, c) ^ cross(multiply(a, b), c)
                    ^ cross(a, multiply(b, c)) ^ cross(a, b)) == 0
            triples += 1
        if eta_generator:
            # Coboundaries on an abelian group are symmetric, whereas this
            # cross cocycle has nonsymmetric values on these two elements.
            assert cross((0, 1), (1, 0)) == 1
            assert cross((1, 0), (0, 1)) == 0
        cocycles += 1
    print(f"Normalized literal cross cocycles: {cocycles}; full cocycle identities: {triples}.")
    print(f"Recovered edge evaluations: {edges}; splitting-change coboundary identities: {changes}.")
    print("The trivial-action C2 example retains a nonzero H1 edge and a non-coboundary cross class.")


def main():
    covering_graph()
    matrix_cases()
    print("All A.93 finite certificates passed.")


if __name__ == "__main__":
    main()
