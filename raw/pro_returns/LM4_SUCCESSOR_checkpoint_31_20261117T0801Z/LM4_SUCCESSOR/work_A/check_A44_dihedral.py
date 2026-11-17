"""Exact finite coset/incidence checks for the hypothetical collapse in A.44.

The general theorem is proved in A_involutions.tex. These checks verify the
coset formulas, cusp Euler characteristic, disconnected graph, and relative
Frattini matrix. No existence of a forbidden full involution is asserted.
"""

from collections import defaultdict


def orbits(permutation):
    unseen = set(range(len(permutation)))
    answer = []
    while unseen:
        first = min(unseen)
        cycle = []
        j = first
        while j not in cycle:
            cycle.append(j)
            unseen.remove(j)
            j = permutation[j]
        assert j == first
        answer.append(tuple(cycle))
    return answer


def components(vertices, edges):
    adjacent = defaultdict(set)
    for i, j in edges:
        adjacent[i].add(j)
        adjacent[j].add(i)
    unseen = set(vertices)
    result = []
    while unseen:
        first = min(unseen)
        todo = [first]
        found = set()
        while todo:
            v = todo.pop()
            if v in found:
                continue
            found.add(v)
            todo.extend(adjacent[v] - found)
        unseen -= found
        result.append(sorted(found))
    return result


def check(p):
    k = (p - 1) // 2
    x = [(-j) % p for j in range(p)]
    y = [(1 - j) % p for j in range(p)]
    z = [(j - 1) % p for j in range(p)]
    ox, oy, oz = map(orbits, (x, y, z))
    assert sorted(map(len, ox)) == [1] + [2] * ((p - 1) // 2)
    assert sorted(map(len, oy)) == [1] + [2] * ((p - 1) // 2)
    assert list(map(len, oz)) == [p]
    cusp_count = len(ox) + len(oy) + len(oz)
    assert cusp_count == p + 2
    genus_twice = 2 + p - cusp_count
    assert genus_twice == 0

    edges = []
    for cycle in ox:
        if len(cycle) == 1:
            assert cycle == (0,)
            edges.append((0, p))
        else:
            edges.append(cycle)
    for cycle in oy:
        shifted = tuple((j + k) % p for j in cycle)
        if len(cycle) == 1:
            assert shifted == (0,)
            edges.append((0, p + 1))
        else:
            assert sum(shifted) % p == 0
            edges.append(shifted)
    edges.append((p, p + 1))
    comps = components(range(p + 2), edges)
    assert sorted(map(len, comps)) == [2] * ((p - 1) // 2) + [3]
    assert len(edges) == p + 2
    assert len(comps) == (p + 1) // 2
    print(f'p={p}: x widths={list(map(len, ox))}; '
          f'y widths={list(map(len, oy))}; z widths={[p]}')
    print(f'  genus=0; section vertices={p+2}; cusp edges={len(edges)}; '
          f'components={comps}')


for prime in (3, 5, 7, 11, 13):
    check(prime)

# Conjugation by x on the Schreier basis A=x^2, B=y*x^-1, C=x*y.
T = ((1, -1, 1), (0, 0, 1), (0, 1, 0))
A = (1, 0, 0)
Y2 = (0, 1, 1)
S = (1, 1, -1)


def act(v):
    return tuple(sum(T[i][j] * v[j] for j in range(3)) for i in range(3))


assert act(A) == A and act(Y2) == Y2
assert act(S) == tuple(-v for v in S)
determinant = A[0] * (Y2[1] * S[2] - Y2[2] * S[1])
assert determinant == -2
print('Relative Frattini basis: invariant A,Y^2; sign A+B-C; determinant=-2')
print('All finite incidence and matrix checks passed.')
