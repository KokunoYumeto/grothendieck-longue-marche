#!/usr/bin/env python3
"""Exact C2*C3 words and finite images of the original standard input.

The input is alpha=delta and the actual full h=1, g=x^-1, w=x.
Only nu=-1,+1 are used as full profinite units. Finite witnesses
are images of the proved M=C2*C3 under explicit PSL2(F_p) maps.
"""
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json

orders = (2, 3)
one = ()
A, B = ((0, 1),), ((1, 1),)


def normal(syllables):
    out = []
    for factor, exponent in syllables:
        exponent %= orders[factor]
        if not exponent:
            continue
        if out and out[-1][0] == factor:
            exponent = (out.pop()[1] + exponent) % orders[factor]
        if exponent:
            out.append((factor, exponent))
    return tuple(out)


def mul(*values):
    return normal(tuple(s for value in values for s in value))


def inv(value):
    return normal((factor, -exponent) for factor, exponent in reversed(value))


def power(value, exponent):
    if exponent < 0:
        return power(inv(value), -exponent)
    result = one
    while exponent:
        if exponent & 1:
            result = mul(result, value)
        value = mul(value, value)
        exponent >>= 1
    return result


def conj(left, value):
    return mul(left, value, inv(left))


def substitute(value, image_a, image_b):
    return mul(*(power((image_a, image_b)[factor], exponent)
                 for factor, exponent in value))


x = power(mul(A, B), -2)
y = conj(B, x)
z = inv(mul(x, y))
p = mul(x, A)
g, w = inv(x), x


def theta(value):
    return conj(A, value)


def omega(value, epsilon=1):
    return conj(power(B, epsilon), value)


def delta(value):
    return substitute(value, A, mul(A, inv(B), A))


checks = []


def check(name, result):
    assert result, name
    checks.append({'name': name, 'passed': True})


check('factor_relations', power(A, 2) == power(B, 3) == one)
check('kernel_X_Y_Z_words',
      x == mul(power(B, 2), A, power(B, 2), A)
      and y == mul(A, power(B, 2), A, power(B, 2))
      and z == mul(B, A, power(B, 2), A, B))
check('source_theta_and_omega_actions',
      theta(x) == y and theta(y) == x
      and omega(x) == y and omega(y) == z and omega(z) == x)
check('source_x_y_p_and_cusp_words',
      power(mul(A, B), 2) == inv(x)
      and power(mul(A, inv(B)), 2) == y
      and p == mul(inv(B), A, inv(B)) and power(p, 2) == inv(z))
check('theta_omega_square_is_original_inner_x_inverse', all(
      theta(omega(theta(omega(value)))) == conj(inv(x), value)
      for value in (x, y)))
check('full_delta_extension_is_an_involution', all(
      delta(delta(value)) == value for value in (A, B)))
check('full_delta_extension_has_original_restriction',
      delta(x) == inv(x) and delta(y) == inv(y)
      and delta(p) == mul(A, inv(p), A))
check('original_standard_beta_is_theta',
      conj(inv(w), mul(inv(z), g)) == y
      and conj(inv(w), inv(g)) == x)
check('original_standard_eta_is_inner_p',
      mul(inv(z), g) == conj(p, x) and inv(g) == conj(p, y))
check('canonical_original_W_is_one',
      mul(inv(w), g, w, x) == one)

# All reduced words in the original free basis of length at most four.
free_words = [()]
frontier = [()]
for length in range(1, 5):
    frontier = [word + (letter,) for word in frontier
                for letter in (1, -1, 2, -2)
                if not word or letter != -word[-1]]
    free_words.extend(frontier)


def evaluate_free(word):
    return mul(*(power(x if abs(letter) == 1 else y,
                       1 if letter > 0 else -1) for letter in word))


def print_free(word):
    return ' '.join({1: 'x', -1: 'x^-1', 2: 'y', -2: 'y^-1'}[v]
                    for v in word) or '1'


check('complete_reduced_free_word_corpus_through_length_four',
      len(free_words) == len(set(free_words)) == 161
      and Counter(map(len, free_words)) == {0: 1, 1: 4, 2: 12, 3: 36, 4: 108})

# q_l:M -> PSL2(F_l), q_l(A)=[[0,-1],[1,0]],
# q_l(B)=[[0,-1],[1,1]]. Multiplication is modulo the scalar +/-I.
primes = (3, 5, 7, 11)


def canonical(matrix, prime):
    matrix = tuple(value % prime for value in matrix)
    return min(matrix, tuple(-value % prime for value in matrix))


def matmul(left, right, prime):
    a, b, c, d = left
    e, f, gg, hh = right
    return canonical((a*e+b*gg, a*f+b*hh, c*e+d*gg, c*f+d*hh), prime)


@lru_cache(maxsize=None)
def finite_image(value, prime):
    result = (1, 0, 0, 1)
    images = (canonical((0, -1, 1, 0), prime),
              canonical((0, -1, 1, 1), prime))
    for factor, exponent in value:
        for _ in range(exponent):
            result = matmul(result, images[factor], prime)
    return result


check('every_finite_map_respects_the_actual_full_coproduct_relations', all(
      matmul(finite_image(A, ell), finite_image(A, ell), ell) == (1, 0, 0, 1)
      and matmul(matmul(finite_image(B, ell), finite_image(B, ell), ell),
                 finite_image(B, ell), ell) == (1, 0, 0, 1)
      for ell in primes))

solutions = []
rows = []
finite_separations = Counter()
case_count = 0
for nu in (-1, 1):
    k = (nu-1)//2
    image_x = conj(inv(w), mul(power(z, -(k+1)), g))
    image_y = conj(inv(w), mul(inv(g), power(z, -k)))
    image_z = conj(inv(w), power(z, nu))
    check('nu_%d_original_gamma_values_and_cusp' % nu,
          image_x == (inv(x) if nu == -1 else y)
          and image_y == (inv(y) if nu == -1 else x)
          and mul(image_x, image_y, image_z) == one)
    epsilon_selected = 1 if nu == -1 else -1
    c_selected = power(y, -k) if epsilon_selected == 1 else power(x, -(k+1))
    kappa_selected = mul(c_selected, power(B, epsilon_selected))
    check('nu_%d_exact_standard_order_three_extension' % nu,
          kappa_selected == mul(A, power(B, -1 if nu == -1 else 1), A)
          and power(kappa_selected, 3) == one
          and power(mul(A, kappa_selected), -2) == image_x
          and conj(kappa_selected, image_x) == image_y)
    for epsilon in (1, -1):
        zeros = []
        witness_sample = None
        for free_word in free_words:
            c = evaluate_free(free_word)
            kappa = mul(c, power(B, epsilon))
            d = theta(c)  # h=1 is the actual original standard value.
            e_epsilon = inv(x) if epsilon == 1 else y
            formulas = (
                mul(c, omega(c, epsilon), omega(c, 2*epsilon)),
                mul(image_x, d, theta(omega(d, epsilon)), e_epsilon),
                mul(inv(image_y), c, omega(image_x, epsilon), inv(c)))
            ambient = (power(kappa, 3), mul(image_x, power(mul(A, kappa), 2)),
                       mul(inv(image_y), conj(kappa, image_x)))
            assert formulas == ambient, (nu, epsilon, free_word)
            case_count += 1
            if all(value == one for value in formulas):
                solutions.append((nu, epsilon, free_word))
                zeros.append(print_free(free_word))
                continue
            witness = next((ell, index, finite_image(value, ell))
                           for ell in primes for index, value in enumerate(formulas)
                           if finite_image(value, ell) != (1, 0, 0, 1))
            finite_separations[witness[0]] += 1
            if witness_sample is None:
                witness_sample = {'c': print_free(free_word), 'prime': witness[0],
                                  'defect': ('N', 'R_x', 'R_y')[witness[1]],
                                  'projective_matrix': list(witness[2])}
        check('nu_%d_epsilon_%d_all_161_literal_defect_equalities' % (nu, epsilon), True)
        rows.append({'nu': nu, 'epsilon': epsilon, 'c_count': len(free_words),
                     'simultaneous_zero_c_words': zeros,
                     'finite_nonzero_separations': len(free_words)-len(zeros),
                     'first_nonzero_finite_witness': witness_sample})

check('exactly_644_original_standard_defect_cases', case_count == 644)
check('only_the_two_stated_full_word_extensions_in_the_corpus',
      set(solutions) == {(-1, 1, (2,)), (1, -1, (-1,))})
check('all_642_nonzero_cases_have_explicit_actual_finite_M_images',
      sum(finite_separations.values()) == 642)
check('opposite_epsilon_abelian_obstruction',
      [(-k, -2*k) if nu == -1 else (-2*(k+1), -(k+1))
       for nu, k in ((-1, -1), (1, 0))] == [(1, 2), (-2, -1)])

output = {
    'status': 'PASS',
    'scope': 'Exact actual standard input h=1, g=x^-1, w=x, m=-1; full units nu=-1,+1 only.',
    'group': 'The proved actual M=C2(A)*C3(B), A=tau, B=xi.',
    'finite_maps': 'M -> PSL2(F_l), A -> [[0,-1],[1,0]], B -> [[0,-1],[1,1]].',
    'finite_map_primes': list(primes),
    'c_word_bound': 4,
    'c_word_count': len(free_words),
    'defect_case_count': case_count,
    'simultaneous_solutions_in_corpus': [
        {'nu': nu, 'epsilon': eps, 'c': print_free(word)} for nu, eps, word in solutions],
    'finite_nonzero_separations_by_prime': dict(sorted(finite_separations.items())),
    'checks': checks,
    'assertion_count': len(checks),
    'rows': rows,
    'remaining_actual_target': 'No remaining original h is assigned, and neither full-unit m nor W=1 is proved here.'
}
text = json.dumps(output, indent=2) + '\n'
Path(__file__).with_name('actual_order_three_defects_output.json').write_text(text)
print(text, end='')
