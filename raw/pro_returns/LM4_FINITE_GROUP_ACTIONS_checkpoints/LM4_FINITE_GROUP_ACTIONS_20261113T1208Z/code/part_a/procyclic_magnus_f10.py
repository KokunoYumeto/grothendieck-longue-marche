#!/usr/bin/env python3
"""Exact small checks of the formulae in F.10.

This checks integral Magnus substitutions, the finite-group block action,
and the finite logarithm identities.  It does not purport to compute the
unknown separating truncation for the F.9 word or the full A5 centralizer.
All calculations use integers or fractions; no numerical approximation.
"""
from fractions import Fraction
from itertools import product, permutations
from pathlib import Path
import json


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


def word_product(*words):
    return reduce_word(a for w in words for a in w)


def word_sub(w, images):
    return word_product(*(images[a-1] if a > 0 else
                          inverse_word(images[-a-1]) for a in w))


def automorphism_product(left, right):
    return tuple(word_sub(w, left) for w in right)


def clean(a):
    return {k: v for k, v in a.items() if v}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return clean(out)


def scale(a, c):
    return clean({k: c*v for k, v in a.items()})


def polynomial_product(a, b, degree):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            if len(u) + len(v) <= degree:
                key = u+v
                out[key] = out.get(key, 0) + x*y
    return clean(out)


def magnus(w, degree):
    out = {(): 1}
    for a in w:
        letter = abs(a)-1
        factor = {(): 1, (letter,): 1} if a > 0 else {
            (letter,)*j: (-1)**j for j in range(degree+1)}
        out = polynomial_product(out, factor, degree)
    return out


def monomial_basis(rank, degree):
    return [m for j in range(degree, -1, -1)
            for m in product(range(rank), repeat=j)]


def substitution_matrix(images, degree):
    rank = len(images)
    basis = monomial_basis(rank, degree)
    positions = {w: i for i, w in enumerate(basis)}
    values = [add(magnus(w, degree), {(): -1}) for w in images]
    matrix = {}
    for column, monomial in enumerate(basis):
        value = {(): 1}
        for variable in monomial:
            value = polynomial_product(value, values[variable], degree)
        for w, coefficient in value.items():
            matrix[positions[w], column] = coefficient
    return clean(matrix)


def identity(n):
    return {(i, i): 1 for i in range(n)}


def matrix_product(a, b):
    brows = {}
    for (i, j), x in b.items():
        brows.setdefault(i, []).append((j, x))
    out = {}
    for (i, k), x in a.items():
        for j, y in brows.get(k, ()):
            out[i, j] = out.get((i, j), 0) + x*y
    return clean(out)


def matrix_power(a, e, n):
    assert e >= 0
    out = identity(n)
    while e:
        if e & 1:
            out = matrix_product(out, a)
        a = matrix_product(a, a)
        e //= 2
    return out


def log_matrix(a, n):
    nil = add(a, scale(identity(n), -1))
    power = dict(nil)
    out = {}
    for j in range(1, n+1):
        if not power:
            return out
        out = add(out, scale(power, Fraction((-1)**(j+1), j)))
        power = matrix_product(power, nil)
    raise AssertionError('matrix was not unipotent')


def exp_matrix(a, n):
    power = identity(n)
    out = dict(power)
    for j in range(1, n+1):
        power = scale(matrix_product(power, a), Fraction(1, j))
        if not power:
            return out
        out = add(out, power)
    raise AssertionError('matrix was not nilpotent')


def inner_images(w, rank):
    return tuple(word_product(w, (i+1,), inverse_word(w))
                 for i in range(rank))


def permutation_product(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def permutation_inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def act_word(a, w):
    return tuple((1 if x > 0 else -1)*(a[abs(x)-1]+1) for x in w)


def parity(a):
    return sum(a[i] > a[j] for i in range(len(a))
               for j in range(i+1, len(a))) % 2


def main():
    # The coefficient used in the self-contained Magnus injectivity proof.
    words = [()]
    frontier = [()]
    for length in range(1, 6):
        frontier = [w+(a,) for w in frontier for a in (-2, -1, 1, 2)
                    if not w or w[-1] != -a]
        words += frontier
    for w in words[1:]:
        syllables = []
        for a in w:
            if syllables and abs(syllables[-1][0]) == abs(a):
                syllables[-1][1] += 1 if a > 0 else -1
            else:
                syllables.append([a, 1 if a > 0 else -1])
        monomial = tuple(abs(a)-1 for a, exponent in syllables)
        expected = 1
        for a, exponent in syllables:
            expected *= exponent
        assert magnus(w, len(syllables)).get(monomial) == expected != 0

    # Genuine pure Artin automorphisms of F3, not arbitrary unipotent data.
    s1 = ((1, 2, -1), (1,), (3,))
    s2 = ((1,), (2, 3, -2), (2,))
    p = automorphism_product(s1, s1)
    q = automorphism_product(s2, s2)
    rank, degree = 3, 3
    n = len(monomial_basis(rank, degree))
    pm, qm = substitution_matrix(p, degree), substitution_matrix(q, degree)
    assert substitution_matrix(automorphism_product(p, q), degree) == \
        matrix_product(pm, qm)
    assert substitution_matrix(automorphism_product(q, p), degree) == \
        matrix_product(qm, pm)
    for matrix in (pm, qm):
        assert all(i <= j for i, j in matrix)
        assert all(matrix.get((i, i)) == 1 for i in range(n))
        assert all(isinstance(x, int) for x in matrix.values())
    logarithm = log_matrix(pm, n)
    assert logarithm and exp_matrix(logarithm, n) == pm
    inverse = exp_matrix(scale(logarithm, -1), n)
    assert matrix_product(pm, inverse) == identity(n)
    for exponent in range(-5, 6):
        actual = matrix_power(pm if exponent >= 0 else inverse, abs(exponent), n)
        assert exp_matrix(scale(logarithm, exponent), n) == actual
        assert log_matrix(actual, n) == scale(logarithm, exponent)

    # Actual A5 semidirect action: A5 permutes a basis of F5, then acts on
    # Inn(F5).  The block formula is the same as (F.10.6)--(F.10.8).
    group = [a for a in permutations(range(5)) if parity(a) == 0]
    assert len(group) == 60
    generators = [(1, 2, 0, 3, 4), (1, 0, 3, 2, 4), (1, 0, 2, 4, 3)]
    cache = {}

    def rho(w):
        if w not in cache:
            cache[w] = substitution_matrix(inner_images(w, 5), 2)
        return cache[w]

    h, k = (1, -2, 3), (4, 5, -1)
    block_checks = 0
    product_checks = 0
    for g in group:
        gi = permutation_inverse(g)
        assert rho(act_word(gi, word_product(h, k))) == matrix_product(
            rho(act_word(gi, h)), rho(act_word(gi, k)))
        product_checks += 1
        for a in generators:
            left_index = permutation_product(permutation_inverse(a), g)
            left = rho(act_word(permutation_inverse(left_index), h))
            right = rho(act_word(gi, act_word(a, h)))
            assert left == right
            block_checks += 1
    # At the identity block, an actual A5 conjugation changes a logarithm.
    base = rho((1,))
    changed = rho(act_word(generators[0], (1,)))
    n5 = len(monomial_basis(5, 2))
    delta = add(log_matrix(changed, n5), scale(log_matrix(base, n5), -1))
    assert delta
    nonzero_entry = next(iter(delta.items()))

    # Explicit finite p-power reductions: a nilpotent unitriangular matrix
    # has p-power order, and the polynomial power formula agrees modulo p^2.
    finite_checks = []
    for prime in (2, 3, 5, 7, 11):
        modulus = prime**2
        exponent = prime
        while True:
            power = matrix_power(pm, exponent, n)
            reduced = clean({ij: int(c) % modulus for ij, c in power.items()})
            if reduced == identity(n):
                break
            exponent *= prime
            assert exponent <= prime**6
        for e in (0, 1, prime, prime+1, exponent+1):
            lhs = exp_matrix(scale(logarithm, e), n)
            rhs = matrix_power(pm, e, n)
            assert lhs == rhs
            assert all(Fraction(c).denominator == 1 for c in lhs.values())
        finite_checks.append({'prime': prime, 'modulus': modulus,
                              'verified_p_power_annihilator': exponent})

    result = {
        'scope': 'Exact small formula checks for F10; no computed separating truncation for the F9 word and no full residual centralizer claim.',
        'maximal_syllable_coefficient_cases': len(words)-1,
        'pure_Artin_rank': 3,
        'Magnus_degree': degree,
        'integral_upper_unitriangular_dimension': n,
        'substitution_composition_checks': 2,
        'log_exp_power_checks': 11,
        'actual_finite_block_action': 'A5 on Inn(F5) by permutation of the five free generators',
        'A5_order': len(group),
        'block_conjugation_checks': block_checks,
        'block_product_checks': product_checks,
        'nonzero_logarithm_commutator_entry': {
            'row_column': list(nonzero_entry[0]), 'value': str(nonzero_entry[1])},
        'finite_p_power_reductions': finite_checks,
        'all_assertions_passed': True,
    }
    destination = Path(__file__).with_name('procyclic_magnus_f10_output.json')
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
