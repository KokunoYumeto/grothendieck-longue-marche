#!/usr/bin/env python3
"""Exact conjugators for all D37 weight-five maps on P_1.

The all-elements assertion is proved by the commutator identities in the
accompanying research note. This program checks every parameter and every
abelian residue, with actual Magnus multiplication and nontrivial higher
abelian/derived coordinates. No full profinite lift is inferred.
"""
from itertools import product
from pathlib import Path
import json
from a_weight5_characteristic import Magnus

HERE = Path(__file__).resolve().parent


def evaluate(poly, x, y):
    return sum(a * pow(x, i, 5) * pow(y, j, 5)
               for (i, j), a in poly.items()) % 5


def exact_linear_division(A, numerator, r, s):
    assert s % 5
    linear = {(1, 0): r, (0, 1): s}
    linear = {m: a % 5 for m, a in linear.items() if a % 5}
    remainder, quotient = dict(numerator), {}
    for j in range(4, 0, -1):
        coefficient = remainder.get((4-j, j), 0) * pow(s, -1, 5) % 5
        if coefficient:
            monomial = {(4-j, j-1): coefficient}
            quotient = A.add(quotient, monomial)
            remainder = A.add(remainder, A.mul(linear, monomial), -1)
    assert not remainder
    assert A.mul(linear, quotient) == numerator
    return quotient


def conjugator(A, Q, r, s):
    if not s:
        return A.id, 0, {}, {}
    d = A.mul(A.mul(A.Y, A.add(A.X, A.Y)), Q)
    d = A.add({}, d, -s)
    t = evaluate(d, s, -r) * pow(s, -1, 5) % 5
    numerator = A.add({(4, 0): t*s % 5} if t*s % 5 else {}, d, -1)
    p = exact_linear_division(A, numerator, r, s)
    u = A.gm(A.gp(A.x, 5*t), A.module(p))
    return u, t, p, d


def main():
    A = Magnus(1)
    basis = [(i, total-i) for total in range(5) for i in range(total+1)]
    cases = []
    nonidentity_conjugators = 0
    restricted_power_cases = 0
    for aa, bb, cc in product(range(5), repeat=3):
        Q = {mon: value for mon, value in
             zip(((2, 0), (1, 1), (0, 2)), (aa, bb, cc)) if value}
        beta = A.beta(Q)[0]
        for r, s in product(range(5), repeat=2):
            u, t, p, d = conjugator(A, Q, r, s)
            # Higher abelian coordinates and all derived degrees are retained.
            rr = r + 5*((aa+bb+r) % 5)
            ss = s + 5*((bb+cc+s) % 5)
            k = {(i, j): ((aa+1)*(i+1)+(bb+1)*(j+1)+cc+r+s) % 5
                 for i, j in basis}
            k = {mon: value for mon, value in k.items() if value}
            g = A.gm(A.gm(A.gp(A.x, rr), A.gp(A.y, ss)), A.module(k))
            assert beta(g) == A.conj(u, g)
            assert A.comm(A.gp(A.x, 5), g) == A.module(
                {(4, 0): s} if s else {})
            assert A.comm(A.module(p), g) == A.module(
                A.add({}, A.mul({mon: value for mon, value in
                                (((1, 0), r), ((0, 1), s)) if value}, p), -1))
            assert A.comm(u, g) == A.module(d)
            nonidentity_conjugators += int(u != A.id)
            restricted_power_cases += int(t != 0)
            cases.append({'Q': [aa, bb, cc], 'abelian_residue': [r, s],
                          'checked_abelian_coordinates': [rr, ss],
                          'x_fifth_power_coefficient': t,
                          'module_conjugator': A.serialize(p),
                          'central_change': A.serialize(d)})
    assert len(cases) == 125*25
    # The extra restricted inner power cannot simply be omitted: the
    # central change below has nonzero evaluation on the commuting line.
    example_Q = {(2, 0): 1}
    _, t, p, d = conjugator(A, example_Q, 1, 2)
    assert evaluate(d, 2, -1) != 0 and t != 0
    payload = {
        'status': 'PASS_EXACT_CLASS_PRESERVING_WEIGHT_FIVE_P1',
        'source': 'The actual Magnus P_1 of D37, order 5^19',
        'formula': 'd=-s Y(X+Y)Q; t=d(s,-r)/s; p=(t s X^4-d)/(r X+s Y); u=x^(5t)c^p',
        'zero_case': 'If s=0 then beta_Q(g)=g and u=1',
        'exact_commutators': ['[x^5,g]=c^(s X^4)',
                             '[c^p,g]=c^(-(r X+s Y)p)',
                             '[u,g]=c^d'],
        'parameter_count': 125,
        'abelian_residue_count': 25,
        'checked_cases': len(cases),
        'nonidentity_conjugators': nonidentity_conjugators,
        'restricted_fifth_power_cases': restricted_power_cases,
        'required_fifth_power_example': {'Q': [1, 0, 0], 'r_s': [1, 2],
                                        't': t, 'p': A.serialize(p),
                                        'nonzero_line_evaluation': evaluate(d, 2, -1)},
        'cases': cases,
        'scope': 'Elementwise conjugators on P_1. The D37 nonzero ordinary outer classes remain nonzero. No full profinite peripheral lift is asserted.'
    }
    HERE.joinpath('a_weight5_class_preserving.json').write_text(
        json.dumps(payload, indent=2)+'\n')
    print('Exact Magnus checks:', len(cases), 'cases,', nonidentity_conjugators,
          'nonidentity conjugators,', restricted_power_cases,
          'requiring the displayed nonzero x^5 coefficient')
    print(payload['status'])


if __name__ == '__main__':
    main()
