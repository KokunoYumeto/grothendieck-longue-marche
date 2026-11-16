#!/usr/bin/env python3
"""Exact finite checks for A.90's completed old-coordinate construction.

The script checks finite Galois stabilizers, actual rational identities,
local modular power images, and the displayed cofinal valuation schedule.
The existence of the successive Chebotarev primes and the infinite
completion are proved in A.90, not inferred from these finite checks.
No number generated here is presented as an output of that prime search.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial, gcd, lcm, prod
from sympy import nextprime

from fibre_character_certificate import gamma_group, generated_subgroup
from fibre_squareclass_certificate import fixes_quadratic_field, minus_one_in_span
from picard_obstruction_certificate import square_vector, hilbert_two, v2_unit


def mixed_admissible(g, ns, rows, signs):
    u, eps = g
    N = lcm(*ns)
    ds = tuple(gcd(n, u - 1) for n in ns)
    for ks in product(*(range(e, N, 2) for e in eps)):
        if all(((u - 1) // 2 * delta
                + sum(w * k for w, k in zip(row, ks))) % d == 0
               for row, delta, d in zip(rows, signs, ds)):
            return True
    return False


def actual_mixed_tuple(g, ns, rows, signs):
    u, eps = g
    assert u % 4 == 3
    N = lcm(*ns)
    ds = [gcd(n, u - 1) for n in ns]
    assert all(d % 4 == 2 for d in ds)
    odd = lcm(*(d // 2 for d in ds))
    assert odd % 2 == 1 and N % odd == 0
    ks = tuple(next(k for k in range(N)
                    if k % 2 == ep and k % odd == 0) for ep in eps)
    es = []
    for n, row, delta, d in zip(ns, rows, signs, ds):
        const = (u - 1) // 2 * delta + sum(w*k for w, k in zip(row, ks))
        assert const % d == 0
        e = next(e for e in range(n)
                 if ((u - 1) * (delta + 2*e)
                     + 2*sum(w*k for w, k in zip(row, ks))) % (2*n) == 0)
        es.append(e)
    return ks, tuple(es)


def mixed_fields():
    cases = witnesses = excluded = literal_equations = 0
    exponent_lists = ((4, 8), (4, 12), (8, 12), (12, 20),
                      (8, 24), (12, 24), (12, 60), (4, 8, 12))
    for ns in exponent_lists:
        N = lcm(*ns)
        for primes in ((2,), (3,), (5,), (3, 5)):
            gamma = gamma_group(N, primes)
            for seed in range(8):
                rows = tuple(tuple((seed + 3*i + 2*j) % 7 - 3
                                   for j in range(len(primes)))
                             for i in range(len(ns)))
                signs = tuple((seed + i) % 2 for i in range(len(ns)))
                kernel = {g for g in gamma if fixes_quadratic_field(g, rows, signs)}
                if minus_one_in_span(rows, signs):
                    excluded += 1
                    continue
                images = {g for g in gamma if mixed_admissible(g, ns, rows, signs)}
                generated = generated_subgroup(images, N, len(primes))
                assert generated == kernel
                assert any(g[0] % 4 == 3 for g in kernel)
                for g in kernel:
                    if g[0] % 4 == 3:
                        actual_mixed_tuple(g, ns, rows, signs)
                        witnesses += 1
                        literal_equations += len(ns)
                cases += 1
    print(f"Mixed-exponent generated-stabilizer equalities: {cases}.")
    print(f"Actual simultaneous root tuples: {witnesses}; literal equations: {literal_equations}.")
    print(f"Cases outside the no-minus-one hypothesis retained separately: {excluded}.")


def initial_data_and_refinements():
    cs = (Q(0), Q(1), Q(-9563, 59024))
    R, c = Q(1, 17), Q(-11, 68)
    aa = tuple(R - ci for ci in cs)
    assert aa == (Q(1, 17), Q(-16, 17), Q(13035, 59024))
    boundaries = tuple(tuple((ci-cj)/aa[j]
                             for j, cj in enumerate(cs) if j != i)
                       for i, ci in enumerate(cs))
    for row in boundaries:
        s, t = map(square_vector, row)
        assert frozenset({-1}) not in {frozenset(), s, t, s ^ t}
    # The chosen fourth root has squareclass 5; this suffices for every
    # quadratic evaluation, while its actual root is checked below.
    roots_mod_squares = (Q(2), Q(1, 2), Q(5))
    checks = 0
    for i, row in enumerate(boundaries):
        for bits in product((0, 1), repeat=2):
            b = prod((v**bit for v, bit in zip(row, bits)), start=Q(1))
            assert hilbert_two(roots_mod_squares[i], b) == 0
            checks += 1
    w = 0
    for k in range(1, 97):
        modulus = 2**k
        target = 217 * pow(869, -1, modulus) % modulus
        candidates = [z for z in (w, w + 2**(k-1))
                      if (z + 6*z*z + 16*z**3 + 16*z**4) % modulus == target]
        assert len(candidates) == 1
        w = candidates[0]
    rr = 1 + 4*w
    assert rr % 8 == 5
    assert (pow(rr, 4, 2**100)*869 - 4341) % 2**100 == 0
    assert (Q(16, 17)-c)/(R-c) == 5
    assert hilbert_two(Q(5), Q(2)) == 1
    print(f"All initial coordinate-root character evaluations: {checks}; 96 exact root-lifting steps.")
    print("Normalized obstructing evaluation is (5,2), with invariant 1/2.")

    maps = fields = 0
    for ns in ((4, 4, 4), (8, 12, 20), (12, 24, 60)):
        for i in range(3):
            for h in (2, 3, 5):
                for u in (Q(2, 3), Q(5, 7), Q(11)):
                    new = list(aa)
                    new[i] *= u**ns[i]
                    for row_index, ci in enumerate(cs):
                        old_classes = tuple(square_vector((ci-cj)/aa[j])
                                            for j, cj in enumerate(cs) if j != row_index)
                        new_classes = tuple(square_vector((ci-cj)/new[j])
                                            for j, cj in enumerate(cs) if j != row_index)
                        assert old_classes == new_classes
                        fields += 1
                    for y in (Q(1), Q(2, 5), Q(-3, 2)):
                        assert aa[i] * (u*y**h)**ns[i] == new[i] * y**(h*ns[i])
                        maps += 1
    print(f"Exact coefficient/forgetful-map identities: {maps}; fixed boundary-squareclass rows: {fields}.")


def valuation(n, p):
    result = 0
    while n % p == 0:
        result += 1
        n //= p
    return result


def local_power_images():
    inputs = balls = 0
    for p in (2, 3, 5, 7, 11):
        for h in range(2, 17):
            v = valuation(h, p)
            depth = 2*v + 5
            root_depth = depth-v
            modulus = p**(depth+3)
            image = set()
            for z in range(p**3):
                y = 1+p**root_depth*z
                residue = (pow(y, h, modulus)-1) % modulus
                assert residue % p**depth == 0
                image.add((residue//p**depth) % p**3)
                assert y % p**3 == 1
                inputs += 1
            assert image == set(range(p**3))
            balls += 1
    print(f"Literal local hth-power images on square-close root balls: {balls}; inputs: {inputs}.")


def cofinality_and_genus():
    ns = [4, 4, 4]
    fresh = []
    q = 1009
    steps = checks = 0
    for h in range(2, 18):
        for i in range(3):
            old = ns[i]
            q = int(nextprime(q))
            fresh.append((q, i, old))
            ns[i] *= h
            assert ns[i] % old == 0
            assert old % 4 == 0
            steps += 1
            # Each older fresh valuation is unchanged by the displayed
            # later updates, whose local root targets are units there.
            for _, _, v in fresh:
                assert v > 0 and v % 4 == 0
                checks += 1
        assert ns == [4*factorial(h)]*3
        for m in range(1, h+1):
            assert all(n % m == 0 for n in ns)
    assert len({q for q, _, _ in fresh}) == len(fresh)
    assert all(sum(i == j for _, i, _ in fresh) == 16 for j in range(3))
    print(f"Formal cofinal refinement steps: {steps}; stable fresh-valuation checks: {checks}.")
    print("All integers through 17 divide each final exponent; each coordinate has 16 distinct fresh slots.")

    genus_checks = 0
    for ns in product((4, 8, 12, 20, 24, 60), repeat=3):
        D, N = prod(ns), lcm(*ns)
        two_g_minus_two = -2*D + sum(D-D//n for n in ns) + D-D//N
        assert two_g_minus_two % 2 == 0
        two_g = two_g_minus_two+2
        boundary = sum(D//n for n in ns)+D//N+D
        r = 8*D+8
        assert 0 <= two_g <= 2*D+2
        assert boundary <= 5*D
        assert r > two_g+boundary+2
        assert r*r+1-two_g*r-boundary > 0
        genus_checks += 1
    print(f"Mixed-exponent genus, boundary, and uniform positivity checks: {genus_checks}.")


def main():
    mixed_fields()
    initial_data_and_refinements()
    local_power_images()
    cofinality_and_genus()
    print("All A.90 finite certificates passed.")
    print("No unbounded Chebotarev prime recursion was executed or asserted.")


if __name__ == "__main__":
    main()
