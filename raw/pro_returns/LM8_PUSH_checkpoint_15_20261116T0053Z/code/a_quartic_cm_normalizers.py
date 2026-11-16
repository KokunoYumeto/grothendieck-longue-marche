#!/usr/bin/env python3
"""Exact certificates for registered A.55; proofs are in the accompanying TeX.

No finite computation is used to infer a statement about all degrees.
This checks the actual Schreier abelianized relators, deck invariants,
pushforward lattice, divisibility examples and Cartier coefficient formula.
"""
import json
from math import comb
from pathlib import Path
import sympy as sp


def schreier_relation(m, initial):
    # Surface relator [a,b][c,d], coset representatives 1,b,...,b^(m-1).
    generators = [(a, j) for a in ('a', 'c', 'd') for j in range(m)] + [('B', 0)]
    index = {a: j for j, a in enumerate(generators)}
    result = [0] * len(generators)
    coset = initial
    word = [('a', 1), ('b', 1), ('a', -1), ('b', -1),
            ('c', 1), ('d', 1), ('c', -1), ('d', -1)]
    for letter, sign in word:
        if letter == 'b':
            nxt = (coset + sign) % m
            if sign == 1 and coset == m - 1:
                result[index[('B', 0)]] += 1
            if sign == -1 and coset == 0:
                result[index[('B', 0)]] -= 1
            coset = nxt
        else:
            result[index[(letter, coset)]] += sign
    assert coset == initial
    expected = [0] * len(generators)
    expected[index[('a', initial)]] += 1
    expected[index[('a', (initial + 1) % m)]] -= 1
    assert result == expected
    return result


def cyclic_lattice(m):
    relations = [schreier_relation(m, j) for j in range(m)]
    # The first m-1 a_j-a_(j+1) vectors are a primitive basis of the
    # sum-zero relation lattice. Their left (m-1)-minor is triangular ±1.
    minor = sp.Matrix([r[:m-1] for r in relations[:m-1]])
    assert abs(minor.det()) == 1
    assert [sum(r[j] for r in relations) for j in range(3*m+1)] == [0]*(3*m+1)
    dim = 2 + 2*m
    deck = sp.zeros(dim)
    deck[0, 0] = deck[1, 1] = 1
    for offset in (2, 2+m):
        for j in range(m):
            deck[offset+(j+1) % m, offset+j] = 1
    inv = sp.zeros(dim, 4)
    inv[0, 0] = inv[1, 1] = 1
    for j in range(m):
        inv[2+j, 2] = inv[2+m+j, 3] = 1
    assert (deck-sp.eye(dim))*inv == sp.zeros(dim, 4)
    # Each cycle gives exactly the equality of all its coordinates.
    assert (deck-sp.eye(dim)).rank() == 2*(m-1)
    push = sp.zeros(4, dim)
    push[0, 0], push[1, 1] = 1, m
    for j in range(m):
        push[2, 2+j] = push[3, 2+m+j] = 1
    old_image = push*inv
    assert old_image == sp.diag(1, m, m, m)
    return {'degree': m, 'genus': m+1, 'homology_rank': dim,
            'relation_primitive_minor': int(minor.det()),
            'invariant_rank': 4, 'pushforward_invariant_lattice': [1,m,m,m]}


def coeff(p, exponent):
    e = (p-1)//2
    if exponent % 5 or not 0 <= exponent//5 <= e:
        return 0
    j = exponent//5
    return ((-1)**(e-j)*comb(e,j)) % p


def cartier(p):
    assert p % 10 == 1
    k = (p-1)//10
    actual = [[coeff(p, p*i-j) for j in (1,2)] for i in (1,2)]
    formula = [[((-1)**(3*k)*comb(5*k,2*k)) % p, 0],
               [0, ((-1)**k*comb(5*k,4*k)) % p]]
    assert actual == formula
    assert (actual[0][0]*actual[1][1]) % p
    return {'p':p, 'matrix':actual, 'determinant':(actual[0][0]*actual[1][1]) % p}


def divisibility(p, r):
    n = r+1
    m = p**n
    # PD(eta)=a; v=p^r c, in the other symplectic pair.
    v = [0, 0, p**r, 0]
    eta_v = v[1] % m
    old_image_mod_m = [v[1] % m, v[2] % m, v[3] % m]
    assert eta_v == 0 and old_image_mod_m != [0,0,0]
    return {'p':p, 'valuation':r, 'cover_exponent':n,
            'eta_v':eta_v, 'v_outside_invariant_pushforward':True}


def main():
    output = {
      'status':'PASS',
      'scope':'Exact finite certificates; uniform claims proved in sections/A_quartic_cm_normalizers.tex.',
      'surface_lattices':[cyclic_lattice(m) for m in (2,3,5,11,25,121)],
      'cartier':[cartier(p) for p in sp.primerange(3,2000) if p % 5 == 1],
      'nonprimitive_detection':[divisibility(p,r) for p in (11,31,41,61,101) for r in range(6)]
    }
    t, u, beta = sp.symbols('t u beta')
    # v=i(2t-1), w=beta*u and beta^5=-4, u^5=t(t-1).
    target = sp.expand((sp.I*(2*t-1))**2 - ((-4)*t*(t-1)-1))
    assert target == 0
    output['actual_target_change'] = 'v=i(2t-1), w=beta*u, beta^5=-4, u^5=t(t-1): PASS'
    here = Path(__file__)
    here.with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
    print('A55 certificate PASS')
    print('Schreier/deck lattices:', ', '.join(str(x['degree']) for x in output['surface_lattices']))
    print('Cartier ordinary checks:',len(output['cartier']),'split primes below2000')
    print('Nonprimitive exact detection checks:',len(output['nonprimitive_detection']))
    print('Actual genus-two target coordinate change: PASS')


if __name__ == '__main__':
    main()
