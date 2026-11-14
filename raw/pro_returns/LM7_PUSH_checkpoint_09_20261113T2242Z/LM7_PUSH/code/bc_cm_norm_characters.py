#!/usr/bin/env python3
"""Exact order-four CM inclusion and integral rigidity comparison.

The braid equalities use the independently audited faithful Artin evaluator
in bc_hyperelliptic_sewing.py.  The free-by-cyclic calculation is a second,
literal model of <d,y | y^2=d^4>.  Nothing here assigns an unevaluated GT
character a Galois value.
"""
from pathlib import Path
import hashlib
import itertools
import json

from bc_hyperelliptic_sewing import Artin, red, inv, subst, compose, eye, mm, mp


HERE = Path(__file__).resolve().parent
IDENTITY = ((1,), (2,))
ALPHA = ((2,), (-1,))


def alpha_power(n):
    out = IDENTITY
    for _ in range(n % 4):
        out = compose(ALPHA, out)
    return out


def smul(a, b):
    return red(a[0] + subst(b[0], alpha_power(a[1]))), a[1] + b[1]


def sinv(a):
    return subst(inv(a[0]), alpha_power(-a[1])), -a[1]


def sword(word):
    images = {1: ((), 1), 2: ((1,), 2)}
    images.update({-i: sinv(images[i]) for i in (1, 2)})
    out = ((), 0)
    for letter in word:
        out = smul(out, images[letter])
    return out


def modmat(a, m):
    return tuple(tuple(x % m for x in row) for row in a)


def det(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def minv(a):
    assert det(a) == 1
    return ((a[1][1], -a[0][1]), (-a[1][0], a[0][0]))


def evaluate_matrix_polynomial(a, b, r):
    return tuple(tuple(a*int(i == j) + b*r[i][j]
                       for j in range(2)) for i in range(2))


def main():
    art4, art3 = Artin(4), Artin(3)
    a, b, c = (1,), (2,), (3,)
    d = a+b+c
    y = inv(b)+d*2+b
    x = inv(y+d)
    z4 = d*4
    xi1 = c+inv(a)
    xi2 = a+b+a+inv(c)+inv(b)+inv(a)
    k0 = y+inv(d)*2
    k1 = d+y+inv(d)*3
    fold = ((1,), (2,), (1,))
    s = (1, 2, 1)
    comparisons = [
        art4.compare('Quartic: y squared equals total centre', y*2, z4),
        art4.compare('Quartic: first free kernel word', k0, inv(xi2)),
        art4.compare('Quartic: second free kernel word', k1, inv(xi1)),
        art4.compare('Quartic: d on xi1', d+xi1+inv(d), inv(xi2)),
        art4.compare('Quartic: d on xi2', d+xi2+inv(d), xi1),
        art4.compare('Quartic: d on k0', d+k0+inv(d), k1),
        art4.compare('Quartic: d on k1', d+k1+inv(d), inv(k0)),
        art4.compare('Quartic: xyz equals one', x+y+d, ()),
        art4.compare('Quartic: cusp exact factor', x, xi1+inv(d)*3),
        art4.compare('Quartic: cusp fourth power and centre',
                     x*4+z4*3, xi1+inv(xi2)+inv(xi1)+xi2),
        art4.compare('Quartic: oriented boundary conjugacy',
                     xi1+inv(xi2)+inv(xi1)+xi2,
                     inv(xi2)+inv(xi1+xi2+inv(xi1)+inv(xi2))+xi2),
        art3.compare('Quartic fold of d', subst(d, fold), s),
        art3.compare('Quartic fold of y', subst(y, fold), s*2),
        art3.compare('Quartic fold of x', subst(x, fold), inv(s)*3),
    ]

    # This is the exact semidirect presentation, not an exponent-only check.
    assert alpha_power(4) == IDENTITY
    srecords = []
    for label, word, expected in (
        ('relation y2=d4', (2, 2, -1, -1, -1, -1), ((), 0)),
        ('k0=y d^-2', (2, -1, -1), ((1,), 0)),
        ('k1=d y d^-3', (1, 2, -1, -1, -1), ((2,), 0)),
        ('conjugation d k0 d^-1', (1, 2, -1, -1, -1), ((2,), 0)),
        ('conjugation d k1 d^-1', (1, 1, 2, -1, -1, -1, -1), ((-1,), 0)),
        ('cusp x=(yd)^-1', (-1, -2), ((-2,), -3)),
    ):
        got = sword(word)
        assert got == expected, (label, got, expected)
        srecords.append(dict(label=label, word=word, value=got))

    I = eye(2)
    U = ((1, 1), (0, 1))
    L = ((1, 0), (-1, 1))
    R = mm(U, L)
    S = mm(R, U)
    assert R == ((0, 1), (-1, 1))
    assert S == ((0, 1), (-1, 0))
    assert mp(R, 3) == ((-1, 0), (0, -1))
    assert mp(S, 2) == ((-1, 0), (0, -1))

    # Exhaustive finite checks complement the coefficient-ring proof:
    # commuting with U,L gives A=a I, for every commutative ring.
    finite = []
    for modulus in range(2, 13):
        both = []
        rcentral, scentral = set(), set()
        for entries in itertools.product(range(modulus), repeat=4):
            A = (entries[:2], entries[2:])
            commu = modmat(mm(A, U), modulus) == modmat(mm(U, A), modulus)
            comml = modmat(mm(A, L), modulus) == modmat(mm(L, A), modulus)
            if commu and comml:
                both.append(A)
                assert A == ((entries[0], 0), (0, entries[0]))
            if modmat(mm(A, R), modulus) == modmat(mm(R, A), modulus):
                rcentral.add(A)
            if modmat(mm(A, S), modulus) == modmat(mm(S, A), modulus):
                scentral.add(A)
        rexpect = {modmat(evaluate_matrix_polynomial(a0, b0, R), modulus)
                   for a0, b0 in itertools.product(range(modulus), repeat=2)}
        sexpect = {modmat(evaluate_matrix_polynomial(a0, b0, S), modulus)
                   for a0, b0 in itertools.product(range(modulus), repeat=2)}
        assert rcentral == rexpect and scentral == sexpect
        finite.append(dict(modulus=modulus, joint_centralizer=len(both),
                           R_centralizer=len(rcentral), S_centralizer=len(scentral)))

    cm = []
    for name, matrix in (('Eisenstein', R), ('Gaussian', S)):
        table = []
        for a0, b0 in itertools.product(range(3), repeat=2):
            A = modmat(evaluate_matrix_polynomial(a0, b0, matrix), 3)
            if det(A) % 3 != 1:
                continue
            if name == 'Eisenstein':
                w = ((1,), (2,))
                image = modmat(mm(A, w), 3)
                assert image in (w, ((2,), (1,)))
                bit = int(image != w)
            else:
                bit = int(b0 != 0)
            table.append(dict(a=a0, b=b0, matrix=A, positive_E1_bit=bit))
        assert len(table) == (6 if name == 'Eisenstein' else 4)
        cm.append(dict(name=name, values=table))

    # The exact integral covariance fixes the signed shear uniquely.
    # F_rho is E61's matrix; the following holds as integer matrices for
    # every integer rho, and the saved polynomial coefficients are universal.
    rigidity = []
    for rho in range(-4, 5):
        t = 8*rho
        F = ((1, -t), (-t, 1+t*t))
        V = ((1, t), (0, 1))
        assert mm(mm(V, L), minv(V)) == mm(mm(minv(F), L), F)
        assert mm(mm(V, S), minv(V)) == mm(S, F)
        Rminus = tuple(tuple(-v for v in row) for row in R)
        assert mm(mm(V, Rminus), minv(V)) == mm(minv(F), Rminus)
        rigidity.append(dict(rho=rho, F=F, V=V))

    output = dict(
        status='PASS_EXACT_ORDER_FOUR_INCLUSION_AND_CM_RIGIDITY',
        scope='Literal braid/free-by-cyclic maps and signed matrix comparisons; '
              'no unevaluated full-GT character is assigned a Galois value.',
        comparison_count=len(comparisons), comparisons=comparisons,
        inclusion=dict(d=d, y=y, x=x, centre=z4, k0=k0, k1=k1,
                       free_kernel_images=[inv(xi2), inv(xi1)],
                       quotient_to_Z={'d': 1, 'y': 2, 'x': -3},
                       triangle_quotient='C4 * C2',
                       semidirect_action=ALPHA),
        exact_semidirect_records=srecords,
        matrices=dict(U=U, L=L, Rplus=R, S=S),
        integral_centralizer_coefficient_equations={
            'A_U_minus_U_A': [['-c', 'a-d'], ['0', 'c']],
            'A_L_minus_L_A': [['-b', '0'], ['a-d', 'b']],
            'consequence': 'b=c=0 and d=a over every commutative ring',
            'first_column_e1_consequence': 'a=1'},
        finite_coefficient_ring_checks=finite,
        positive_E1_CM_tables=cm,
        signed_covariance_checks=rigidity,
        analytic_cover={'curve': 'Y^2=X^3-X', 'map': 't=1/X^2',
                        'ramification_at_0_1_infinity': [4, 2, 4],
                        'deleted_point': 'O over t=0',
                        'deck_automorphism': '(X,Y)->(-X,iY)'},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        evaluator_sha256=hashlib.sha256((HERE/'bc_hyperelliptic_sewing.py').read_bytes()).hexdigest(),
    )
    (HERE/'bc_cm_norm_characters.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: output[k] for k in
                     ('status', 'scope', 'comparison_count', 'source_sha256',
                      'evaluator_sha256')}, indent=2))


if __name__ == '__main__':
    main()
