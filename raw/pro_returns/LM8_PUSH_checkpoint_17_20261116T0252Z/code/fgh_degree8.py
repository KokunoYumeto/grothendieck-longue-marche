#!/usr/bin/env python3
"""Independent exact tensor/Lyndon audit of the degree-eight ambient plane.

No attached Python module is imported.  This computes universal Lie
derivations only; it does not manufacture Galois elements or a scalar lambda.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


def add(*terms):
    out = {}
    for p in terms:
        for w, a in p.items():
            out[w] = out.get(w, Q(0)) + a
            if not out[w]:
                del out[w]
    return out


def scale(p, a):
    return {w: a*b for w, b in p.items() if a*b}


def mul(p, q):
    out = {}
    for u, a in p.items():
        for v, b in q.items():
            w = u+v
            out[w] = out.get(w, Q(0))+a*b
            if not out[w]:
                del out[w]
    return out


def br(p, q):
    return add(mul(p, q), scale(mul(q, p), -1))


x, y = {(0,): Q(1)}, {(1,): Q(1)}


def adx(n, p):
    for _ in range(n):
        p = br(x, p)
    return p


def deriv(D, p):
    out = {}
    for w, a in p.items():
        for i, letter in enumerate(w):
            for v, b in D[letter].items():
                z = w[:i]+v+w[i+1:]
                out[z] = out.get(z, Q(0))+a*b
                if not out[z]:
                    del out[z]
    return out


def dbr(D, E):
    return tuple(add(deriv(D, E[i]), scale(deriv(E, D[i]), -1)) for i in range(2))


def ds(D, a):
    return tuple(scale(p, a) for p in D)


def da(D, E):
    return tuple(add(p, q) for p, q in zip(D, E))


def eps(m):
    assert m % 2 == 0 and m >= 2
    return adx(m, y), add(*(scale(br(adx(j, y), adx(m-1-j, y)), (-1)**j)
                            for j in range(m//2)))


F = (y, {})


def lower(D, n):
    for _ in range(n):
        D = dbr(F, D)
    return D


def is_lyndon(w):
    return all(w < w[i:] for i in range(1, len(w)))


@lru_cache(None)
def lb(w):
    if len(w) == 1:
        return {w: Q(1)}
    i = next(i for i in range(1, len(w)) if is_lyndon(w[i:]))
    return br(lb(w[:i]), lb(w[i:]))


def coords(p):
    rest, out = dict(p), {}
    while rest:
        w = min(rest)
        assert is_lyndon(w), ('not a Lie element', w)
        a = rest[w]
        out[w] = a
        rest = add(rest, scale(lb(w), -a))
    return out


def word(w):
    return ''.join('xy'[a] for a in w)


def desc(D):
    return {z: {word(w): str(a) for w, a in coords(D[i]).items()}
            for i, z in enumerate('xy')}


def weight(D):
    weights = {(w.count(0)-(i == 0), w.count(1)-(i == 1))
               for i, p in enumerate(D) for w in p}
    assert len(weights) == 1
    return next(iter(weights))


# Metabelian Lie algebra Q*x + Q*y + Q[u,v]*[x,y].
def padd(p, q):
    out = dict(p)
    for w, a in q.items():
        out[w] = out.get(w, Q(0))+a
        if not out[w]: del out[w]
    return out


def pmove(p, shift, a):
    return {(i+shift[0], j+shift[1]): a*b for (i, j), b in p.items() if a*b}


def mbr(A, B):
    a, b, p = A
    c, d, q = B
    z = {(0, 0): a*d-b*c} if a*d-b*c else {}
    for t in (pmove(q, (1, 0), a), pmove(q, (0, 1), b),
              pmove(p, (1, 0), -c), pmove(p, (0, 1), -d)):
        z = padd(z, t)
    return Q(0), Q(0), z


@lru_cache(None)
def lm(w):
    if len(w) == 1:
        return (Q(1), Q(0), {}) if w == (0,) else (Q(0), Q(1), {})
    i = next(i for i in range(1, len(w)) if is_lyndon(w[i:]))
    return mbr(lm(w[:i]), lm(w[i:]))


def meta(p):
    out = {}
    for w, a in coords(p).items():
        _, _, q = lm(w)
        out = padd(out, {v: a*b for v, b in q.items()})
    return {str(w): str(a) for w, a in out.items()}


def main():
    A = ds(lower(eps(8), 3), Q(1, 120))
    B = ds(dbr(eps(4), lower(eps(4), 2)), Q(1, 2))
    C = da(A, ds(B, Q(31, 20)))
    comm = br(x, y)
    for D in (A, B, C):
        assert not deriv(D, comm)
        assert weight(D) == (4, 4)
        swap = tuple({tuple(1-j for j in w): a for w, a in D[1-i].items()}
                     for i in range(2))
        assert swap == ds(D, -1)
    w0 = (0,)*5+(1,)*4
    w1 = (0,)*4+(1, 0)+(1,)*3
    alpha = lambda D: -D[0].get(w0, 0)
    nu = lambda D: D[0].get(w1, 0)+4*D[0].get(w0, 0)
    assert [(alpha(D), nu(D)) for D in (A, B, C)] == [
        (1, Q(-31, 20)), (0, 1), (1, 0)]
    denominators = {name: sorted({a.denominator for p in D for a in coords(p).values()})
                    for name, D in [('A8', A), ('B8', B), ('C8', C)]}
    assert all(d % 5 for name in ('B8', 'C8') for d in denominators[name])
    assert meta(B[0]) == meta(B[1]) == {}
    assert meta(A[0]) and meta(A[1])
    # A nonzero 2x2 coordinate minor independently certifies rank two.
    assert alpha(C)*nu(B)-alpha(B)*nu(C) == 1
    result = {
        'scope': 'Universal ambient derivations; no actual arithmetic element is supplied.',
        'definitions': {'A8': 'ad_F^3(epsilon8)/120',
                        'B8': '[epsilon4,ad_F^2(epsilon4)]/2',
                        'C8': 'A8+31*B8/20', 'F': 'F(x)=y,F(y)=0'},
        'coordinates': {name: {'alpha': str(alpha(D)), 'nu': str(nu(D))}
                        for name, D in [('A8', A), ('B8', B), ('C8', C)]},
        'lyndon_denominators': denominators,
        'metabelian': {name: {'x': meta(D[0]), 'y': meta(D[1])}
                       for name, D in [('A8', A), ('B8', B)]},
        'lyndon': {name: desc(D) for name, D in [('A8', A), ('B8', B), ('C8', C)]},
        'checked': ['special equation D([x,y])=0', 'weight (4,4)',
                    'swap sign minus', 'Lyndon decomposition',
                    'Z5 integrality and saturation certificate', 'metabelian kernel for B8'],
        'lambda': 'Open', 'arithmetic_lattice': 'Open'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'lyndon'}, indent=2))


if __name__ == '__main__':
    main()
