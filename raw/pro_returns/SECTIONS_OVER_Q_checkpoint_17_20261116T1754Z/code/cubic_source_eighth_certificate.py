#!/usr/bin/env python3
"""Exact finite audit of A125's arbitrary odd-place theorem and cubic source.

The odd-place tests use actual rational d_i=(w_i^8-x)/(1-x), retain
their complete generated eighth-power class subgroup, and test every
positive/negative fourth-power product with all local root classes.
The hypotheses about the local squareclass field and two norm symbols
are imposed explicitly.  Separate tests use complete global common
characters computed from literal root stabilizers on the actual source.
"""

from collections import defaultdict, deque, Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd

import sympy as sp

from odd_quartic_subset_certificate import valuation_unit, legendre, hilbert
from cubic_source_quartic_certificate import PUNCTURES, profile, vu
from eighth_common_characters import common_characters, valuation_row, CHI16
from harmonic_eighth_remaining_search import eighth, evaluation


def symbolic():
    Z, X, D, R, T, c, b = sp.symbols("Z X D R T c b")
    assert sp.resultant(Z**8-D, X-Z, Z) == X**8-D
    f = (T-c)/(R-c)
    assert sp.factor(f.subs(T, R*X**8)-(X**8-c/R)/(1-c/R)) == 0
    assert sp.factor((1/T-1/b)/(1/R-1/b)-(R/T)*(T-b)/(R-b)) == 0
    assert sp.factor((1/T-1/c)/(1/R-1/c)-f*R/T) == 0
    d = (X**8-T)/(1-T)
    assert sp.factor(1/T+(1-1/T)*d/X**8-1/X**8) == 0
    roots = sp.symbols("Z0:4")
    transform = lambda z: (1/z[0], *(z[i]/z[0] for i in range(1, 4)))
    assert all(sp.factor(a-b) == 0 for a, b in zip(transform(transform(roots)), roots))
    print("PASS: literal octic norm resultant, normalized norm quotient, all root inverses and local inversion identities.", flush=True)


def local_fourth_roots(x, p):
    v, u = valuation_unit(x, p)
    if v % 4:
        return ()
    return tuple(Q(p)**(v//4)*r for r in range(1, p) if pow(r, 4, p) == u)


def odd_prime(p):
    eighths = {pow(u, 8, p) for u in range(1, p)}
    coset = {u: min(u*z % p for z in eighths) for u in range(1, p)}

    def cl(x):
        v, u = valuation_unit(x, p)
        return v % 8, coset[u]

    def sq(x):
        v, u = valuation_unit(x, p)
        return (v % 2) | ((legendre(u, p) < 0) << 1)

    ws = {Q(p)**e*u for e, u in product(range(-2, 4), range(1, p))}
    xs = sorted({Q(p)**h*u for h, u in product(range(-3, 10), range(1, p))} - {Q(1)})
    active = states_count = positive = negative = root_checks = excluded = 0
    for x in xs:
        if hilbert(x, -1, p) != 1 or hilbert(x, 2, p) != 1:
            excluded += 1
            continue
        generators = {}
        for w in ws:
            d = (w**8-x)/(1-x)
            if d:
                generators.setdefault(cl(d), d)
        square_span = {0}
        for d in generators.values():
            square_span |= {z ^ sq(d) for z in tuple(square_span)}
        if sq(Q(-1)) not in square_span:
            excluded += 1
            continue
        active += 1
        states = {cl(Q(1)): Q(1)}
        todo = deque(states)
        while todo:
            old = todo.popleft()
            value = states[old]
            for d in generators.values():
                new = value*d
                key = cl(new)
                if key not in states:
                    states[key] = new
                    todo.append(key)
        assert len(states) <= 8*gcd(8, p-1)
        states_count += len(states)
        for value in states.values():
            for sign in (1, -1):
                roots = local_fourth_roots(sign*value, p)
                if roots:
                    if sign == 1:
                        positive += 1
                    else:
                        negative += 1
                for r in roots:
                    root_checks += 1
                    inv4 = 2*(hilbert(x, r, p) < 0)
                    if sign == -1:
                        inv4 += valuation_unit(x, p)[0]*CHI16[p % 16]
                    assert inv4 % 4 == 0, (p, x, value, sign, r, inv4)
    print(f"p={p}: sampled_x={len(xs)}, active_norm/field_cases={active}, "
          f"excluded_hypotheses={excluded}, generated_states={states_count}, "
          f"positive_products={positive}, negative_products={negative}, "
          f"literal_root/character_checks={root_checks}; PASS.", flush=True)
    return len(xs), active, states_count, root_checks


def dyadic_geometry():
    offsets = {sign*Q(2)**e*u for sign, e, u in
               product((-1, 1), range(-16, 21), (1, 3, 5, 7, 9, 11, 13, 15))}
    centres = sorted({a+t for a, t in product(PUNCTURES, offsets)} - set(PUNCTURES))
    fibres = defaultdict(list)
    for z in centres:
        signature = []
        for a in PUNCTURES:
            v, u = vu(z-a, 32)
            signature.append((v % 8, u))
        fibres[tuple(signature)].append(z)
    cases = Counter()
    for values in fibres.values():
        for R, T in combinations(values, 2):
            row_R, vals_R = profile(R)
            row_T, vals_T = profile(T)
            assert row_R == row_T
            s = vu(T-R)[0]
            if vals_R == vals_T:
                assert s >= max(vals_R)+5
                cases['equal'] += 1
            elif row_R == 'infinity':
                assert min(-vals_R[0], -vals_T[0]) >= 5
                cases['infinity'] += 1
            else:
                index, delta = {'zero': (0, 1), 'two_thirds': (2, 1),
                                'one': (1, 2), 'minus_third': (3, 2)}[row_R]
                assert min(vals_R[index], vals_T[index]) == s >= delta+5
                cases[row_R] += 1
    mixed = 0
    for e, eT in product(range(5, 81), repeat=2):
        if e == eT or (e-eT) % 8:
            continue
        s = min(e, eT)
        for k in range(1, 5):
            if s-k == 3:
                assert k >= 2 and (k-e) % 8 == 5
                for t in product(range(4), repeat=4):
                    if t[0]*(k-e) % 4 == 0:
                        assert t[0] == 0
                    mixed += 1
    print(f"Dyadic source: {len(centres)} centres in {len(fibres)} exact octic fibres; "
          f"{sum(cases.values())} actual point pairs, cases={dict(sorted(cases.items()))}; PASS.", flush=True)
    print(f"All {mixed} sampled four-coordinate mixed-relation depth implications passed.", flush=True)


def actual_global_characters():
    pairs = []
    for R in (Q(2), Q(3), Q(1, 7), Q(3, 2), Q(-1, 2), Q(64), Q(129)):
        M = max(vu(R-a)[0] for a in PUNCTURES)
        pairs.append((R, R+Q(2)**(M+5), 2))
    pairs.extend((R, T, 2) for R, T in
                 [(Q(64), Q(16384)), (Q(129), Q(32769)),
                  (Q(194, 3), Q(49154, 3)), (Q(383, 3), Q(98303, 3)),
                  (Q(1, 32), Q(1, 8192))])
    # A genuine change between two boundary discs at the bad odd prime3.
    pairs.append((Q(2+2*3**9, 3), Q(-1+3**9, 3), 3))
    totals = Counter()
    for R, T, p in pairs:
        assert all(eighth((T-a)/(R-a), p) for a in PUNCTURES)
        cs = {Q(-2), Q(-1), Q(1, 2), Q(3, 2), Q(2), Q(4), Q(5), Q(16), -R, -16*R, -81*R}
        for c in sorted(cs - set(PUNCTURES) - {R, T}):
            D = tuple((c-a)/(R-a) for a in PUNCTURES)
            primes = set().union(*(set(valuation_row(d)) for d in D)) - {2}
            if len(primes) > 7:
                totals['omitted_large_prime_basis'] += 1
                continue
            common = common_characters(D)
            totals['actual_global_fibres'] += 1
            f = (T-c)/(R-c)
            for ch in common['characters']:
                assert evaluation(f, ch, common['primes'], p) == 0, (R, T, c, p, ch)
                totals[f'place_{p}_character_evaluations'] += 1
                if ch[0] % 2:
                    totals['actual_order_four_evaluations'] += 1
    print("Literal global root-stabilizer/common-character tests:", dict(sorted(totals.items())), flush=True)
    print("Bad-three old-point pair:", pairs[-1], flush=True)


def main():
    symbolic()
    totals = [0, 0, 0, 0]
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
        totals = [a+b for a, b in zip(totals, odd_prime(p))]
    print("Odd totals (x values, active cases, product states, character checks):", totals, flush=True)
    dyadic_geometry()
    actual_global_characters()
    print("PASS: all exact finite checks. The arbitrary-coordinate and finite-initialization assertions are proved in A125.", flush=True)


if __name__ == '__main__':
    main()
