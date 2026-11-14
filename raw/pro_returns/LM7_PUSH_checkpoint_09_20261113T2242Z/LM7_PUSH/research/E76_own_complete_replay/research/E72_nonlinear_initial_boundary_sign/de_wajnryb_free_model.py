#!/usr/bin/env python3
"""Literal free-group Wajnryb generators, inverses, and boundary map.

The source is the displayed A/B/C/Cprime presentation. All equalities
below are equalities of reduced words, before any finite evaluation.
The characteristic finite targets use the quotient by the exact saved
boundary word, and do not assume a shadow preserves their kernels.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import sympy as sp

HERE = Path(__file__).resolve().parent
STEM = 'de_wajnryb_free_model'


def reduce_word(w):
    out = []
    for a in w:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inverse_word(w):
    return tuple(-a for a in reversed(w))


def multiply_words(*words):
    return reduce_word(a for word in words for a in word)


def apply(automorphism, word):
    return multiply_words(*(automorphism[a-1] if a > 0
                            else inverse_word(automorphism[-a-1]) for a in word))


def compose(a, b):
    """Function composition a after b; abelianization multiplies M_a M_b."""
    return tuple(apply(a, w) for w in b)


def identity(n):
    return tuple((i,) for i in range(1, n+1))


def power(a, n):
    assert n >= 0
    out = identity(len(a))
    while n:
        if n & 1:
            out = compose(out, a)
        a = compose(a, a)
        n //= 2
    return out


def abelianization(a):
    n = len(a)
    M = sp.zeros(n)
    for j, w in enumerate(a):
        for t in w:
            M[abs(t)-1, j] += 1 if t > 0 else -1
    return M


def build(g):
    assert g >= 2
    n = 2*g
    one = identity(n)
    generators, inverses = [], []
    for i in range(1, n):
        a, b = list(one), list(one)
        a[i-1], a[i] = (i, -i-1, i), (i,)
        b[i-1], b[i] = (i+1,), (i+1, -i, i+1)
        generators.append(tuple(a))
        inverses.append(tuple(b))
    generators.append(tuple((i, -n) if i < n else (n,) for i in range(1, n+1)))
    inverses.append(tuple((i, n) if i < n else (n,) for i in range(1, n+1)))
    w = (1, -2, 3, -4)
    generators.append(tuple(multiply_words(w, (i,)) if i <= 4 else (i,)
                            for i in range(1, n+1)))
    inverses.append(tuple(multiply_words(inverse_word(w), (i,)) if i <= 4 else (i,)
                          for i in range(1, n+1)))
    assert all(compose(a, b) == compose(b, a) == one
               for a, b in zip(generators, inverses))
    def evaluate(word):
        out = one
        for t in word:
            out = compose(out, generators[t-1] if t > 0 else inverses[-t-1])
        return out
    D = n+1
    relations = []
    for i in range(1, n):
        relations.append((f'chain_braid_{i}', (i, i+1, i), (i+1, i, i+1)))
    for i in range(1, n+1):
        for j in range(i+2, n+1):
            relations.append((f'chain_commutation_{i}_{j}', (i, j), (j, i)))
    for i in range(1, n+1):
        if i == 4:
            relations.append(('d_braid_4', (D, i, D), (i, D, i)))
        else:
            relations.append((f'd_commutation_{i}', (D, i), (i, D)))
    Y5 = (4, 3, 2, 1, 1, 2, 3, 4)
    relations.append(('B', (D,)+Y5+(D,)+inverse_word(Y5), (1, 2, 3)*4))
    d3_word = None
    if g >= 3:
        t1, t2 = (2, 1, 3, 2), (4, 3, 5, 4)
        d3_word = (inverse_word(t1)+inverse_word(t2)+(D,)+t2+t1+
                   inverse_word(t2)+(D,)+t2+(D, -1, -3, -5))
        relations.append(('C', d3_word+(6,)+d3_word, (6,)+d3_word+(6,)))
        w6 = (1, -2, 3, -4, 5, -6)
        expected = tuple(multiply_words(w6, (i,)) if i <= 6 else (i,)
                         for i in range(1, n+1))
        assert evaluate(d3_word) == expected
        if g >= 4:
            t3 = (6, 5, 7, 6)
            dp = Y5+(D,)+inverse_word(Y5)
            h = t2+t1+t3+t2
            hd = h+(D,)+inverse_word(h)
            relations.append(('Cprime', dp+hd, hd+dp))
    certificates = []
    for name, left, right in relations:
        L, R = evaluate(left), evaluate(right)
        assert L == R, (g, name, L, R)
        certificates.append({'name': name, 'left_word': list(left),
                             'right_word': list(right),
                             'common_generator_images': [list(w) for w in L]})
    v = tuple(i if i % 2 else -i for i in range(1, n+1))
    boundary = v+tuple(-t for t in v)
    assert reduce_word(boundary) == boundary
    assert all(apply(a, boundary) == boundary for a in generators+inverses)
    central_word = tuple(range(1, n+1))*(n+1)*2
    central = evaluate(central_word)
    inner = tuple(multiply_words(inverse_word(boundary), (i,), boundary)
                  for i in range(1, n+1))
    assert central == inner, (g, 'boundary_twist')
    # Every edge of the boundary polygon is paired oppositely.  The
    # vertex quotient has one vertex, giving the oriented genus g cell.
    parent = list(range(2*n))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def join(i, j):
        parent[find(i)] = find(j)
    for t in range(1, n+1):
        p, q = boundary.index(t), boundary.index(-t)
        join(p, (q+1) % (2*n))
        join((p+1) % (2*n), q)
    vertices = len({find(i) for i in range(2*n)})
    assert vertices == 1 and vertices-n+1 == 2-2*g
    # The exact basis e_i=u_i-u_(i+1), e_n=u_n has determinant one.
    C = sp.eye(n)
    for i in range(n-1):
        C[i+1, i] = -1
    assert C.det() == 1
    J = sp.zeros(n)
    for i in range(n-1):
        J[i, i+1], J[i+1, i] = 1, -1
    E = sp.eye(n)
    expected = [E+E[:, i]*E[:, i].T*J for i in range(n)]
    vd = E[:, 0]+E[:, 2]
    expected.append(E+vd*vd.T*J)
    assert all(C.inv()*abelianization(a)*C == M for a, M in zip(generators, expected))
    pairs = []
    for k in range(2, n+1):
        yw = tuple(range(k-1, 0, -1))+tuple(range(1, k))
        pairs.append((evaluate(yw), evaluate((k, k))))
    return {'genus': g, 'rank': n, 'generators': generators, 'inverses': inverses,
            'relations': certificates, 'boundary_word': boundary,
            'boundary_polygon_vertices': vertices,
            'boundary_twist_word': central_word,
            'boundary_twist_generator_images': central,
            'boundary_twist_action': 'Inn(boundary_word^-1)',
            'homology_basis_columns': [list(map(int, C[:, i])) for i in range(n)],
            'd3_word': d3_word, 'pairs': pairs}


def main():
    start = time.time()
    models = [build(g) for g in (2, 3, 4)]
    out = {'status': 'PASS_LITERAL_WAJNRYB_FREE_AUTOMORPHISMS_AND_CAPPING',
           'function_composition': 'a*b means a after b',
           'finite_tuple_action': 'precomposition is the corresponding right action',
           'models': models,
           'capping_map': 'F_(2g) -> F_(2g)/closed_normal(boundary_word); the displayed boundary twist acts trivially on this quotient',
           'all_relations_checked_by_free_reduction': True,
           'all_generator_inverses_and_boundary_images_checked': True,
           'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
           'seconds': round(time.time()-start, 6)}
    (HERE/(STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'models'}, indent=2), flush=True)
    for m in models:
        print('genus', m['genus'], 'relations', len(m['relations']),
              'boundary_length', len(m['boundary_word']), 'PASS', flush=True)


if __name__ == '__main__':
    main()
