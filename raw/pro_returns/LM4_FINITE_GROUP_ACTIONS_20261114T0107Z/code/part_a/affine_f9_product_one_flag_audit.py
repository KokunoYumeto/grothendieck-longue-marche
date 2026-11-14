"""Exact source-word audit of one product-one F9 cohomology representation.

No producer is imported. The eleven literal F23 braid words are evaluated
in the affine group with seven independent translation coordinates. This
reconstructs the actual source actions, the principal-line quotient, its
boundary quotient and five-dimensional kernel. Independent Gauss--Jordan
elimination then verifies the prime-field source algebra, common eigenlines,
full invariant flags when available, and Frobenius intertwiners.

This is a finite, explicitly specified research calculation. It does not
assert a theorem for other characters, fields, or the full pure braid group.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import json


CHARACTER = [1, 3, 3, 1, 1, 1, 2]
CHECKS = Counter()


def check(condition, category):
    assert condition, category
    CHECKS[category] += 1


def add(a, b):
    return (a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3)


def neg(a):
    return (-a % 3) % 3 + 3 * ((-(a // 3)) % 3)


def mul(a, b):
    ar, ai, br, bi = a % 3, a // 3, b % 3, b // 3
    return (ar * br - ai * bi) % 3 + 3 * ((ar * bi + ai * br) % 3)


def power(a, n):
    n %= 8
    result = 1
    for _ in range(n):
        result = mul(result, a)
    return result


def inverse(a):
    check(a != 0, 'inverse_nonzero')
    return power(a, 7)


def total(values):
    answer = 0
    for value in values:
        answer = add(answer, value)
    return answer


def zero(rows, cols):
    return [[0] * cols for _ in range(rows)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(col) for col in zip(*a)]


def mm(a, b):
    if not a:
        return []
    return [[total(mul(x, y) for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def rref(rows, width, prime=False):
    """Full scalar Gauss--Jordan elimination; returns canonical nonzero rows."""
    a = [list(row) for row in rows]
    check(all(len(row) == width for row in a), 'row_width')
    plus = (lambda x, y: (x + y) % 3) if prime else add
    times = (lambda x, y: (x * y) % 3) if prime else mul
    minus = (lambda x: -x % 3) if prime else neg
    inv = (lambda x: x) if prime else inverse
    pivots = []
    rank = 0
    for col in range(width):
        candidates = [i for i in range(rank, len(a)) if a[i][col]]
        if not candidates:
            continue
        pick = candidates[0]
        a[rank], a[pick] = a[pick], a[rank]
        scale = inv(a[rank][col])
        a[rank] = [times(scale, x) for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                c = minus(a[i][col])
                a[i] = [plus(x, times(c, y)) for x, y in zip(a[i], a[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(a):
            break
    check(all(not any(row) for row in a[rank:]), 'zero_remainder_rows')
    return a[:rank], pivots


def nullspace(rows, width):
    basis, pivots = rref(rows, width)
    free = [i for i in range(width) if i not in pivots]
    answer = []
    for col in free:
        vector = [int(i == col) for i in range(width)]
        for row, pivot in zip(basis, pivots):
            vector[pivot] = neg(row[col])
        check(all(total(mul(a, b) for a, b in zip(row, vector)) == 0
                  for row in rows), 'null_vector')
        answer.append(vector)
    return answer


def matrix_inverse(a):
    n = len(a)
    rows = [row + unit for row, unit in zip(a, identity(n))]
    reduced, pivots = rref(rows, 2 * n)
    check(pivots[:n] == list(range(n)), 'matrix_invertible')
    answer = [row[n:] for row in reduced]
    check(mm(a, answer) == identity(n) and mm(answer, a) == identity(n),
          'matrix_inverse_identities')
    return answer


def rank(a, width=None):
    return len(rref(a, width if width is not None else len(a[0]))[0])


def affine_mul(g, h):
    a, x = g
    b, y = h
    return mul(a, b), [add(xx, mul(a, yy)) for xx, yy in zip(x, y)]


def affine_inverse(g):
    a, x = g
    ai = inverse(a)
    return ai, [neg(mul(ai, xx)) for xx in x]


def affine_conjugate(g, h):
    return affine_mul(affine_mul(g, h), affine_inverse(g))


def affine_product(elements):
    answer = (1, [0] * 7)
    for element in elements:
        answer = affine_mul(answer, element)
    return answer


def actual_braid(word):
    unit = (1, [0] * 7)
    meridians = [(t, row) for t, row in zip(CHARACTER, identity(7))] + [unit]
    initial_product = affine_product(meridians)
    conjugators = [unit] * 8
    labels = list(range(8))
    for crossing in word:
        j = abs(crossing) - 1
        a, b = meridians[j:j + 2]
        ca, cb = conjugators[j:j + 2]
        if crossing > 0:
            meridians[j:j + 2] = [affine_conjugate(a, b), a]
            conjugators[j:j + 2] = [affine_mul(a, cb), ca]
        else:
            bi = affine_inverse(b)
            meridians[j:j + 2] = [b, affine_conjugate(bi, a)]
            conjugators[j:j + 2] = [cb, affine_mul(bi, ca)]
        labels[j], labels[j + 1] = labels[j + 1], labels[j]
    check(labels == list(range(8)), 'literal_pure_braid')
    check(meridians[-1] == unit, 'erased_eighth_meridian')
    check([x[0] for x in meridians[:-1]] == CHARACTER, 'fixed_character')
    check(affine_product(meridians) == initial_product, 'boundary_product_fixed')
    u = affine_inverse(conjugators[-1])
    a = [affine_conjugate(u, x)[1] for x in meridians[:-1]]
    return u, a, conjugators


def eval_monomial(exponent):
    answer = 1
    for t, n in zip(CHARACTER, exponent):
        answer = mul(answer, power(t, n))
    return answer


def eval_polynomial(poly):
    return total(mul(coefficient % 3, eval_monomial(exponent))
                 for coefficient, exponent in poly)


def prime_vector(a):
    return [d for row in a for x in row for d in (x % 3, x // 3)]


def from_prime_vector(v, n):
    elements = [v[i] + 3 * v[i + 1] for i in range(0, len(v), 2)]
    return [elements[i:i + n] for i in range(0, len(elements), n)]


def prime_remainder(v, basis, pivots):
    result = list(v)
    for row, pivot in zip(basis, pivots):
        c = result[pivot]
        result = [(x - c * y) % 3 for x, y in zip(result, row)]
    return result


def source_algebra(source):
    n = len(source[0])
    basis, pivots = rref([prime_vector(identity(n))], 2 * n * n, prime=True)
    history = [len(basis)]
    while True:
        candidates = list(basis)
        for vector in basis:
            matrix = from_prime_vector(vector, n)
            candidates.extend(prime_vector(mm(matrix, a)) for a in source)
        enlarged, new_pivots = rref(candidates, 2 * n * n, prime=True)
        history.append(len(enlarged))
        if len(enlarged) == len(basis):
            check(enlarged == basis and new_pivots == pivots, 'stable_algebra_basis')
            break
        basis, pivots = enlarged, new_pivots
    for a in [identity(n)] + source:
        check(not any(prime_remainder(prime_vector(a), basis, pivots)),
              'algebra_contains_identity_and_sources')
    for vector in basis:
        matrix = from_prime_vector(vector, n)
        for a in source:
            check(not any(prime_remainder(prime_vector(mm(matrix, a)), basis, pivots)),
                  'algebra_right_closure')
    imaginary_scalar = [[3 * int(i == j) for j in range(n)] for i in range(n)]
    residue = prime_remainder(prime_vector(imaginary_scalar), basis, pivots)
    return {'dimension_over_F3': len(basis), 'round_dimensions': history,
            'basis_pivots': pivots, 'basis_vectors': basis,
            'imaginary_scalar_contained': not any(residue),
            'imaginary_scalar_remainder': residue}


def common_eigenspaces(source, dual=False):
    n = len(source[0])
    branches = [(identity(n), [])]
    for a in source:
        action = a if dual else transpose(a)
        next_branches = []
        for b, character in branches:
            ba = mm(b, action)
            for scalar in range(1, 9):
                equations = [[add(x, neg(mul(scalar, y))) for x, y in zip(row, old)]
                             for row, old in zip(ba, b)]
                coefficients = nullspace(transpose(equations), len(b))
                if coefficients:
                    new_basis, _ = rref(mm(coefficients, b), n)
                    next_branches.append((new_basis, character + [scalar]))
        branches = next_branches
        if not branches:
            break
    answer = []
    for basis, character in branches:
        for v in basis:
            for a, scalar in zip(source, character):
                image = mm([v], a if dual else transpose(a))[0]
                check(image == [mul(scalar, x) for x in v], 'common_eigenvector')
        answer.append({'character': character, 'basis': basis, 'dimension': len(basis)})
    return answer


def invariant_flag(source):
    n = len(source[0])
    change = identity(n)
    quotient = source
    characters = []
    for j in range(n):
        spaces = common_eigenspaces(quotient)
        if not spaces:
            return {'complete': False, 'steps': j, 'change_columns': change,
                    'characters': characters}
        chosen = spaces[0]
        v = chosen['basis'][0]
        pivot = next(i for i, x in enumerate(v) if x)
        v = [mul(inverse(v[pivot]), x) for x in v]
        keep = [i for i in range(len(v)) if i != pivot]
        small = [[v[r]] + [int(r == c) for c in keep] for r in range(len(v))]
        small_inverse = matrix_inverse(small)
        transformed = [mm(mm(small_inverse, a), small) for a in quotient]
        for a, scalar in zip(transformed, chosen['character']):
            check(a[0][0] == scalar and all(row[0] == 0 for row in a[1:]),
                  'invariant_flag_line')
        extension = identity(n)
        for r in range(n - j):
            extension[j + r][j:] = small[r]
        change = mm(change, extension)
        characters.append(chosen['character'])
        quotient = [[row[1:] for row in a[1:]] for a in transformed]
    change_inverse = matrix_inverse(change)
    triangular = [mm(mm(change_inverse, a), change) for a in source]
    for a in triangular:
        check(all(a[r][c] == 0 for r in range(n) for c in range(r)),
              'full_upper_triangular_flag')
    for j, character in enumerate(characters):
        check([a[j][j] for a in triangular] == character, 'flag_diagonal_character')
    return {'complete': True, 'change_columns': change,
            'inverse_change': change_inverse, 'characters': characters,
            'upper_triangular_actions': triangular}


def intertwiners(target, source):
    r, s = len(target[0]), len(source[0])
    equations = []
    for a, b in zip(target, source):
        for i in range(r):
            for j in range(s):
                equation = [0] * (r * s)
                for k in range(r):
                    equation[k * s + j] = add(equation[k * s + j], a[i][k])
                for k in range(s):
                    equation[i * s + k] = add(equation[i * s + k], neg(b[k][j]))
                equations.append(equation)
    solutions = nullspace(equations, r * s)
    matrices = [[v[i:i + s] for i in range(0, len(v), s)] for v in solutions]
    for matrix in matrices:
        for a, b in zip(target, source):
            check(mm(a, matrix) == mm(matrix, b), 'intertwiner_equation')
    return {'dimension_over_F9': len(matrices), 'basis_matrices': matrices,
            'basis_matrix_ranks': [rank(a) for a in matrices]}


def frobenius(source):
    return [[[power(x, 3) if x else 0 for x in row] for row in a] for a in source]


def main():
    for a, b, c in product(range(9), repeat=3):
        check(add(add(a, b), c) == add(a, add(b, c)), 'field_add_associative')
        check(mul(mul(a, b), c) == mul(a, mul(b, c)), 'field_mul_associative')
        check(mul(a, add(b, c)) == add(mul(a, b), mul(a, c)), 'field_distributive')
    for a in range(9):
        check(add(a, neg(a)) == 0 and mul(a, 1) == a, 'field_units')
        if a:
            check(mul(a, inverse(a)) == 1, 'field_inverse')
    folder = Path(__file__).resolve().parent
    paths = {'braids': folder / 'full_cross_source_stage/marginal_braids.json',
             'universal': folder / 'affine_obstruction_stage_output.json',
             'prior_algebra': folder / 'affine_source_algebra_stage_output.json'}
    data = {name: json.loads(path.read_text()) for name, path in paths.items()}
    hashes = {name: sha256(path.read_bytes()).hexdigest() for name, path in paths.items()}
    check(data['universal']['source_sha256'] == hashes['braids'], 'universal_source_hash')
    old_words = [r for r in data['braids']['records'] if r['index'] < 11]
    old_universal = [r for r in data['universal']['records'] if r['index'] < 11]
    check(len(old_words) == len(old_universal) == 11, 'eleven_actual_sources')
    delta = [add(t, neg(1)) for t in CHARACTER]
    pivot = 6
    check(delta[pivot] == 1, 'chosen_principal_pivot')
    prefix, running = [], 1
    for t in CHARACTER:
        prefix.append(running)
        running = mul(running, t)
    check(running == 1, 'product_one_character')
    check(total(mul(a, b) for a, b in zip(prefix, delta)) == 0,
          'boundary_kills_principals')
    boundary = prefix[:6]
    check(boundary[0] == 1, 'chosen_boundary_section')
    # In H1 coordinates the seventh cocycle value is zero. The kernel of
    # the boundary covector has coordinates (v2,...,v6), with v1 recovered.
    kernel_section = [[neg(x) for x in boundary[1:]]] + identity(5)
    kernel_projection = [[int(j == i + 1) for j in range(6)] for i in range(5)]
    boundary_change = kernel_projection + [boundary]
    boundary_inverse = [[*row, int(i == 0)] for i, row in enumerate(kernel_section)]
    check(mm(boundary_change, boundary_inverse) == identity(6), 'boundary_change_inverse')
    check(mm(boundary_inverse, boundary_change) == identity(6), 'boundary_inverse_change')
    records, source, kernels = [], [], []
    for word, universal in zip(old_words, old_universal):
        check(word['index'] == universal['index'], 'source_order')
        u, action, conjugators = actual_braid(word['negative_braid'])
        check(u[0] == eval_monomial(universal['u_character']), 'literal_u_scalar')
        check(u[1] == [eval_polynomial(p) for p in universal['u_derivation_row']],
              'literal_u_derivative')
        expected = [[eval_polynomial(p) for p in row] for row in universal['action_matrix']]
        check(action == expected, 'literal_source_action')
        check(mm(action, [[x] for x in delta]) == [[x] for x in delta],
              'principal_line_fixed')
        quotient = [[add(action[r][c], neg(mul(delta[r], action[pivot][c])))
                     for c in range(6)] for r in range(6)]
        check(mm([boundary], quotient)[0] == [mul(u[0], x) for x in boundary],
              'actual_boundary_character')
        kernel = mm(mm(kernel_projection, quotient), kernel_section)
        block = mm(mm(boundary_change, quotient), boundary_inverse)
        check([row[:5] for row in block[:5]] == kernel,
              'actual_five_dimensional_kernel')
        check(block[-1] == [0] * 5 + [u[0]], 'boundary_block_last_row')
        check(mm(quotient, kernel_section) == mm(kernel_section, kernel),
              'kernel_inclusion_intertwines')
        source.append(quotient)
        kernels.append(kernel)
        records.append({'index': word['index'], 'label': word['label'],
                        'source_braid_length': len(word['negative_braid']),
                        'u_scalar': u[0], 'u_row': u[1], 'action_7': action,
                        'action_H1_6': quotient, 'boundary_kernel_5': kernel,
                        'boundary_extension_column': [row[-1] for row in block[:5]],
                        'pure_braid_conjugator_scalars': [c[0] for c in conjugators]})
    algebra = source_algebra(source)
    check(algebra['dimension_over_F3'] == 20, 'twenty_dimensional_source_algebra')
    check(not algebra['imaginary_scalar_contained'], 'imaginary_scalar_absent')
    prior = next(r for field in data['prior_algebra']['results'] if field['field_order'] == 9
                 for r in field['results'] if r['characters'] == CHARACTER)
    prior_canonical, prior_pivots = rref(prior['basis_vectors'], 72, prime=True)
    check(prior_canonical == algebra['basis_vectors'] and prior_pivots == algebra['basis_pivots'],
          'prior_algebra_exact_span_comparison')
    source_dual = common_eigenspaces(source, dual=True)
    source_lines = common_eigenspaces(source)
    kernel_dual = common_eigenspaces(kernels, dual=True)
    kernel_lines = common_eigenspaces(kernels)
    source_flag = invariant_flag(source)
    kernel_flag = invariant_flag(kernels)
    # Five explicit common quotient covectors, together with their common
    # one-dimensional kernel, give a particularly short invariant flag.
    quotient_covectors = [boundary, identity(6)[4], identity(6)[3],
                          identity(6)[0], identity(6)[5]]
    line = [0, 1, 3, 0, 0, 0]
    sections = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 0], [1, 2, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1]]
    star_change = transpose([line] + sections)
    star_inverse = [[0, 0, 6, 0, 0, 0]] + quotient_covectors
    check(mm(star_change, star_inverse) == identity(6), 'star_change_inverse')
    check(mm(star_inverse, star_change) == identity(6), 'star_inverse_change')
    star_actions = [mm(mm(star_inverse, a), star_change) for a in source]
    for a in star_actions:
        check(all(a[r][c] == 0 for r in range(1, 6) for c in range(6) if c != r),
              'star_only_first_row_extensions')
    star_characters = [[a[j][j] for a in star_actions] for j in range(6)]
    check(len({tuple(c) for c in star_characters}) == 6, 'distinct_star_characters')
    check(star_characters[4] == [power(x, 3) for x in star_characters[1]],
          'boundary_coordinate_frobenius_pair')
    extension_obstructions = []
    for j in range(1, 6):
        # At source 1 the line character is i and each quotient is 1.
        denominator = add(star_characters[j][1], neg(star_characters[0][1]))
        candidate = mul(star_actions[1][0][j], inverse(denominator))
        failures = [i for i, a in enumerate(star_actions)
                    if a[0][j] != mul(add(a[j][j], neg(a[0][0])), candidate)]
        check(bool(failures), 'each_quotient_extension_nonsplit')
        extension_obstructions.append({'quotient_column': j,
                                       'candidate_splitting_parameter': candidate,
                                       'failed_source_indices': failures})
    diagonal_vectors = []
    for v in algebra['basis_vectors']:
        a = mm(mm(star_inverse, from_prime_vector(v, 6)), star_change)
        check(all(a[r][c] == 0 for r in range(1, 6) for c in range(6) if c != r),
              'algebra_star_support')
        check(a[4][4] == (power(a[1][1], 3) if a[1][1] else 0),
              'algebra_frobenius_diagonal_relation')
        diagonal_vectors.append([d for j in range(6) for d in (a[j][j] % 3, a[j][j] // 3)])
    diagonal_basis, _ = rref(diagonal_vectors, 12, prime=True)
    check(len(diagonal_basis) == 10, 'full_constrained_diagonal_image')
    for j in range(1, 6):
        for scalar in [1, 3]:
            elementary = zero(6, 6)
            elementary[0][j] = scalar
            original = mm(mm(star_change, elementary), star_inverse)
            check(not any(prime_remainder(prime_vector(original),
                                           algebra['basis_vectors'], algebra['basis_pivots'])),
                  'all_first_row_radical_elements')
    check(star_characters[0] != [power(x, 3) for x in star_characters[0]],
          'distinct_frobenius_socle_characters')
    kernel_algebra = source_algebra(kernels)
    star_description = {
        'change_columns': star_change, 'inverse_change': star_inverse,
        'quotient_covectors': quotient_covectors, 'kernel_line': line,
        'characters': star_characters, 'source_actions': star_actions,
        'extension_obstructions': extension_obstructions,
        'diagonal_image_dimension_over_F3': 10,
        'first_row_radical_dimension_over_F3': 10,
        'exact_algebra': 'In this basis all matrices have only diagonal and first-row entries; the six diagonal entries satisfy d4=d1^3 (zero-based positions), the other five diagonal coordinates are arbitrary in F9, and the five off-diagonal first-row entries are arbitrary in F9. The algebra has F3-dimension 20 and its scalar matrices are precisely F3*I.',
        'socle': 'Every nonzero invariant subspace contains the line (0,1,i,0,0,0): the explicit complete invariant flag gives a common eigenline and the five nonsplit extensions exclude all other common eigencharacters.'}
    # Actual K-elements detecting the essential line. Let a be the literal
    # negative seed cross_4_-1_1 and kappa=B_1(a)*a^{-1}. Its character is 1,
    # so evaluation at kappa descends to H1 of K without a representative
    # ambiguity. Both words below remain actual elements of K.
    seed_words = [r for r in data['braids']['records'] if r['index'] >= 11
                  and int(r['label'].split('_')[2]) == -1]
    seed_universal = {r['index']: r for r in data['universal']['records'] if r['index'] >= 11}
    check(len(seed_words) == len(seed_universal) == 8, 'eight_actual_negative_seeds')
    cocycle_line = line + [0]
    seed_records = []
    for word in seed_words:
        u, _, _ = actual_braid(word['negative_braid'])
        universal = seed_universal[word['index']]
        check(u[0] == eval_monomial(universal['u_character']), 'literal_seed_scalar')
        check(u[1] == [eval_polynomial(p) for p in universal['u_derivation_row']],
              'literal_seed_derivative')
        seed_records.append({'index': word['index'], 'label': word['label'],
                             'scalar': u[0], 'row': u[1],
                             'line_value': mm([u[1]], [[x] for x in cocycle_line])[0][0]})
    seed = next(r for r in seed_records if r['label'] == 'cross_4_-1_1')
    check(seed['index'] == 25 and seed['scalar'] == 2 and seed['line_value'] == 1,
          'chosen_actual_seed')
    source_one = records[1]['action_7']
    source_seed_row = mm([seed['row']], source_one)[0]
    kappa_row = [add(x, neg(y)) for x, y in zip(source_seed_row, seed['row'])]
    second_row = mm([kappa_row], source_one)[0]
    line_values = [mm([row], [[x] for x in cocycle_line])[0][0]
                   for row in [kappa_row, second_row]]
    check(line_values == [3, 2], 'actual_socle_evaluation_values')
    for row in [kappa_row, second_row]:
        check(mm([row], [[x] for x in delta]) == [[0]],
              'actual_socle_evaluation_kills_principals')
    evaluation_matrix = [[x, power(x, 3)] for x in line_values]
    evaluation_inverse = matrix_inverse(evaluation_matrix)
    check(evaluation_inverse == [[3, 1], [6, 1]], 'socle_evaluation_explicit_inverse')
    principal_corrections = []
    for r, scalar in zip(records, star_characters[0]):
        image = [x[0] for x in mm(r['action_7'], [[x] for x in cocycle_line])]
        correction = image[6]
        check(image == [add(mul(scalar, x), mul(correction, d))
                        for x, d in zip(cocycle_line, delta)],
              'socle_actual_cocycle_principal_correction')
        principal_corrections.append(correction)
    source_evaluations = {
        'cocycle_line_values_on_X1_through_X7': cocycle_line,
        'actual_seed_records': seed_records,
        'principal_correction_by_source': principal_corrections,
        'chosen_seed_index': 25, 'chosen_seed_label': 'cross_4_-1_1',
        'chosen_source_index': 1, 'chosen_source_label': 'old_1_0',
        'first_word': 'kappa=B_1(a)*a^{-1}, a=u_(cross_4_-1_1)',
        'second_word': 'B_1(kappa)', 'both_word_characters': [1, 1],
        'first_word_row': kappa_row, 'second_word_row': second_row,
        'line_values': line_values,
        'Frobenius_line_values': [power(x, 3) for x in line_values],
        'evaluation_matrix_on_two_socles': evaluation_matrix,
        'inverse_evaluation_matrix': evaluation_inverse,
        'meaning': 'The two actual K-element evaluations define a map on H1(K) because their scalar characters are 1. On the two Frobenius-conjugate essential lines, the map is [[i,-i],[-1,-1]], with inverse [[i,1],[-i,1]].'}
    inter = {'H1_from_Frobenius_H1': intertwiners(source, frobenius(source)),
             'kernel_from_Frobenius_kernel': intertwiners(kernels, frobenius(kernels)),
             'H1_endomorphisms': intertwiners(source, source),
             'kernel_endomorphisms': intertwiners(kernels, kernels)}
    result = {
        'status': 'PASS_EXACT_PRODUCT_ONE_SOURCE_FLAG_RESEARCH',
        'producer_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'inputs': {str(paths[name]): hashes[name] for name in paths},
        'field': 'F3[i]/(i^2+1), code a+3b=a+b*i',
        'character': CHARACTER, 'principal_vector': delta, 'principal_pivot': 7,
        'H1_coordinates': 'Gauge v7=0; quotient v_r -> v_r-delta_r*v7 for 1<=r<=6',
        'boundary_word': 'X1 X2 X3 X4 X5 X6 X7',
        'boundary_row_7': prefix, 'boundary_row_H1_6': boundary,
        'boundary_character': [r['u_scalar'] for r in records],
        'boundary_change_matrix': boundary_change,
        'boundary_inverse_change_matrix': boundary_inverse,
        'kernel_section': kernel_section, 'kernel_projection': kernel_projection,
        'source_records': records, 'prime_field_source_algebra': algebra,
        'prime_field_boundary_kernel_algebra': kernel_algebra,
        'H1_common_submodule_eigenspaces': source_lines,
        'H1_common_quotient_eigenspaces': source_dual,
        'kernel_common_submodule_eigenspaces': kernel_lines,
        'kernel_common_quotient_eigenspaces': kernel_dual,
        'H1_invariant_flag': source_flag, 'kernel_invariant_flag': kernel_flag,
        'explicit_star_representation': star_description,
        'socle_source_evaluations': source_evaluations,
        'intertwiners': inter, 'checks': dict(CHECKS), 'check_total': sum(CHECKS.values()),
        'scope': 'Only the stated concrete character is treated. Every action is reconstructed from the eleven actual F23 source words. The algebra comparison and invariant flags give exact finite evidence; no general unequal-field rank theorem or full-pure-braid image theorem is asserted.'}
    output = Path(__file__).with_name('affine_f9_product_one_flag_audit_output.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'checks': result['check_total'],
                      'boundary_character': result['boundary_character'],
                      'algebra_dimension': algebra['dimension_over_F3'],
                      'algebra_rounds': algebra['round_dimensions'],
                      'imaginary_scalar_contained': algebra['imaginary_scalar_contained'],
                      'kernel_algebra_dimension': kernel_algebra['dimension_over_F3'],
                      'kernel_imaginary_scalar_contained': kernel_algebra['imaginary_scalar_contained'],
                      'H1_submodule_eigenspaces': source_lines,
                      'H1_quotient_eigenspaces': source_dual,
                      'kernel_submodule_eigenspaces': kernel_lines,
                      'kernel_quotient_eigenspaces': kernel_dual,
                      'H1_complete_flag': source_flag['complete'],
                      'H1_flag_characters': source_flag['characters'],
                      'kernel_complete_flag': kernel_flag['complete'],
                      'kernel_flag_characters': kernel_flag['characters'],
                      'star_diagonal_dimension': len(diagonal_basis),
                      'star_extension_obstructions': extension_obstructions,
                      'socle_evaluation_matrix': evaluation_matrix,
                      'intertwiner_dimensions': {k: v['dimension_over_F9'] for k, v in inter.items()},
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
