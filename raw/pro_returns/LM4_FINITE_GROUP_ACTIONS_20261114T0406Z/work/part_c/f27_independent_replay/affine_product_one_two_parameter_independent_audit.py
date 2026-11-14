"""Independent integral Laurent audit for the two-parameter source locus.

This program imports neither the producer nor a symbolic algebra system.
It evaluates the nineteen literal F23 braid words by generic multiplication
in an affine group over Z[s^+-1,t^+-1], verifies every displayed source
matrix by a denominator-cleared principal-quotient identity, and computes
the selected determinant by its 120 signed permutation terms.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import ast
import json


CHECKS = Counter()
ZERO = (0, 0)
ONE = {ZERO: 1}
S = {(1, 0): 1}
T = {(0, 1): 1}
CHARACTERS = [ZERO, (1, 0), (0, 1), ZERO, ZERO, ZERO, (-1, -1)]


def check(test, category):
    assert test, category
    CHECKS[category] += 1


def add(p, q):
    result = dict(p)
    for exponent, c in q.items():
        value = result.get(exponent, 0) + c
        if value:
            result[exponent] = value
        else:
            result.pop(exponent, None)
    return result


def negative(p):
    return {e: -c for e, c in p.items()}


def shift(p, exponent):
    return {(a+exponent[0], b+exponent[1]): c for (a, b), c in p.items()}


def mul(p, q):
    result = {}
    for (a, b), c in p.items():
        for (x, y), d in q.items():
            result = add(result, {(a+x, b+y): c*d})
    return result


def power(p, n):
    if n < 0:
        check(len(p) == 1, 'only_monomial_denominators')
        (a, b), c = next(iter(p.items()))
        check(c in [-1, 1], 'only_signed_unit_denominators')
        return {(a*n, b*n): -1 if c == -1 and n % 2 else 1}
    result = ONE
    for _ in range(n):
        result = mul(result, p)
    return result


def integer_literal(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -integer_literal(node.operand)
    raise ValueError('Noninteger exponent')


def parse_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return {ZERO: node.value} if node.value else {}
    if isinstance(node, ast.Name) and node.id in ['s', 't']:
        return S if node.id == 's' else T
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return negative(parse_node(node.operand))
    if isinstance(node, ast.BinOp):
        left = parse_node(node.left)
        if isinstance(node.op, ast.Pow):
            return power(left, integer_literal(node.right))
        right = parse_node(node.right)
        if isinstance(node.op, ast.Add):
            return add(left, right)
        if isinstance(node.op, ast.Sub):
            return add(left, negative(right))
        if isinstance(node.op, ast.Mult):
            return mul(left, right)
        if isinstance(node.op, ast.Div):
            return mul(left, power(right, -1))
    raise ValueError('Unsupported Laurent syntax')


def parse(text):
    return parse_node(ast.parse(text, mode='eval').body)


def parse_matrix(rows):
    return [[parse(x) for x in row] for row in rows]


def identity(n):
    return [[ONE if i == j else {} for j in range(n)] for i in range(n)]


def matrix_mul(a, b):
    answer = [[{} for _ in b[0]] for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        answer[i][j] = add(answer[i][j], mul(x, y))
    return answer


def matrix_sub(a, b):
    return [[add(x, negative(y)) for x, y in zip(row, old)]
            for row, old in zip(a, b)]


def scalar_mul(p, a):
    return [[mul(p, x) for x in row] for row in a]


def group_mul(g, h):
    a, x = g
    b, y = h
    return (a[0]+b[0], a[1]+b[1]), [add(xx, shift(yy, a)) for xx, yy in zip(x, y)]


def group_inv(g):
    a, x = g
    ai = (-a[0], -a[1])
    return ai, [negative(shift(xx, ai)) for xx in x]


def group_conj(g, h):
    return group_mul(group_mul(g, h), group_inv(g))


def group_product(elements):
    answer = (ZERO, [{} for _ in range(7)])
    for element in elements:
        answer = group_mul(answer, element)
    return answer


def literal_braid(word):
    unit = (ZERO, [{} for _ in range(7)])
    x = [(e, row) for e, row in zip(CHARACTERS, identity(7))] + [unit]
    c = [unit] * 8
    labels = list(range(8))
    initial_boundary = group_product(x)
    for crossing in word:
        j = abs(crossing)-1
        a, b = x[j:j+2]
        ca, cb = c[j:j+2]
        if crossing > 0:
            x[j:j+2] = [group_conj(a, b), a]
            c[j:j+2] = [group_mul(a, cb), ca]
        else:
            bi = group_inv(b)
            x[j:j+2] = [b, group_conj(bi, a)]
            c[j:j+2] = [cb, group_mul(bi, ca)]
        labels[j], labels[j+1] = labels[j+1], labels[j]
    check(labels == list(range(8)), 'literal_pure_braid')
    check(x[-1] == unit, 'erased_meridian')
    check([g[0] for g in x[:-1]] == CHARACTERS, 'literal_character_preserved')
    check(group_product(x) == initial_boundary, 'literal_boundary_product_fixed')
    u = group_inv(c[-1])
    action = [group_conj(u, g)[1] for g in x[:-1]]
    return u, action


def determinant(a):
    n = len(a)
    result = {}
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = ONE if inversions % 2 == 0 else negative(ONE)
        for i, j in enumerate(perm):
            term = mul(term, a[i][j])
        result = add(result, term)
    return result


def serialize(p):
    return [[c, list(e)] for e, c in sorted(p.items())]


def main():
    CHECKS.clear()
    producer = Path(__file__).resolve()
    folder = producer.parent
    paths = {'braids': folder/'full_cross_source_stage/marginal_braids.json',
             'symbolic': folder/'affine_product_one_two_parameter_stage_output.json',
             'universal': folder/'affine_obstruction_stage_output.json'}
    hashes = {name: sha256(path.read_bytes()).hexdigest() for name, path in paths.items()}
    braids = json.loads(paths['braids'].read_text())
    symbolic = json.loads(paths['symbolic'].read_text())
    check(symbolic['source_sha256'] == hashes['universal'], 'universal_input_binding')
    old = [r for r in braids['records'] if r['index'] < 11]
    seeds = [r for r in braids['records'] if r['index'] >= 11
             and int(r['label'].split('_')[2]) == -1]
    check(len(old) == 11 and len(seeds) == 8, 'nineteen_literal_words')
    delta = [[add({e: 1}, negative(ONE))] for e in CHARACTERS]
    line = [[{}], [ONE], [negative(power(S, -1))], [{}], [{}], [{}]]
    cocycle_line = line + [[{}]]
    # Construct these matrices independently from their explicit columns/rows.
    change = parse_matrix([
        ['0','0','0','0','1','0'],
        ['1','1','-s*t','-s*t','-1','-s*t'],
        ['-1/s','0','0','0','0','0'],
        ['0','0','0','1','0','0'],
        ['0','0','1','0','0','0'],
        ['0','0','0','0','0','1']])
    inverse_change = parse_matrix([
        ['0','0','-s','0','0','0'],
        ['1','1','s','s*t','s*t','s*t'],
        ['0','0','0','0','1','0'],
        ['0','0','0','1','0','0'],
        ['1','0','0','0','0','0'],
        ['0','0','0','0','0','1']])
    check(matrix_mul(change, inverse_change) == identity(6), 'flag_change_inverse')
    check(matrix_mul(inverse_change, change) == identity(6), 'flag_inverse_change')
    check(change == parse_matrix(symbolic['flag_change']), 'producer_flag_change')
    check(inverse_change == parse_matrix(symbolic['flag_inverse']), 'producer_flag_inverse')
    section = identity(6) + [[{} for _ in range(6)]]
    section_change = matrix_mul(section, change)
    boundary = parse_matrix([['1','1','s','s*t','s*t','s*t','s*t']])
    check(matrix_mul(boundary, delta) == [[{}]], 'boundary_kills_principals')
    actual, flags, scalar_rows = [], [], []
    for braid, displayed in zip(old, symbolic['source_records']):
        check(braid['index'] == displayed['index'], 'literal_source_index')
        u, action = literal_braid(braid['negative_braid'])
        check(action == parse_matrix(displayed['action_7']), 'literal_seven_dimensional_action')
        check({u[0]: 1} == parse(displayed['u_scalar']), 'literal_boundary_scalar')
        check(matrix_mul(action, delta) == delta, 'principal_vector_fixed')
        check(matrix_mul(boundary, action) == scalar_mul({u[0]: 1}, boundary),
              'actual_boundary_quotient')
        flag = parse_matrix(displayed['action_flag_6'])
        lhs = matrix_mul(action, section_change)
        rhs = matrix_mul(section_change, flag)
        # Multiplication by delta7 clears the only nonmonomial denominator.
        correction = matrix_mul(delta, [lhs[6]])
        check(scalar_mul(delta[6][0], matrix_sub(lhs, rhs)) == correction,
              'actual_principal_quotient_flag_identity')
        principal_correction = parse(displayed['principal_correction'])
        line_difference = matrix_sub(matrix_mul(action, cocycle_line),
                                     scalar_mul(flag[0][0], cocycle_line))
        check(line_difference == scalar_mul(principal_correction, delta),
              'actual_socle_character_identity')
        expected_nu = ['1','s','t','1','1','1','s','t','1','1','1'][braid['index']]
        check(flag[0][0] == parse(expected_nu), 'explicit_socle_character')
        for r in range(1, 6):
            for c in range(6):
                if r != c:
                    check(flag[r][c] == {}, 'flag_star_support')
        actual.append(action)
        flags.append(flag)
        scalar_rows.append([serialize(flag[j][j]) for j in range(6)])
    seed_data = []
    chosen_row = None
    displayed_seeds = {r['index']: r for r in symbolic['seed_records']}
    for braid in seeds:
        u, _ = literal_braid(braid['negative_braid'])
        shown = displayed_seeds[braid['index']]
        check({u[0]: 1} == parse(shown['scalar']), 'literal_seed_scalar')
        value = matrix_mul([u[1]], cocycle_line)[0][0]
        check(value == parse(shown['socle_value']), 'literal_seed_socle_value')
        seed_data.append({'index': braid['index'], 'label': braid['label'],
                          'scalar': serialize({u[0]: 1}), 'socle_value': serialize(value)})
        if braid['index'] == 25:
            check(braid['label'] == 'cross_4_-1_1', 'chosen_literal_seed')
            chosen_row = u[1]
    check(chosen_row is not None, 'chosen_seed_exists')
    kappa = matrix_mul([chosen_row], matrix_sub(actual[1], identity(7)))
    kappa_next = matrix_mul(kappa, actual[1])
    check(kappa == parse_matrix(symbolic['kappa_row']), 'literal_kappa_row')
    check(kappa_next == parse_matrix(symbolic['source_kappa_row']), 'literal_source_kappa_row')
    check(matrix_mul(kappa, delta) == [[{}]], 'kappa_evaluation_on_cohomology')
    value = matrix_mul(kappa, cocycle_line)[0][0]
    next_value = matrix_mul(kappa_next, cocycle_line)[0][0]
    check(value == parse('s*(s*t-1)'), 'explicit_nonzero_socle_evaluation')
    check(next_value == parse('s**2*(s*t-1)'), 'explicit_source_socle_evaluation')
    check(value == parse(symbolic['kappa_socle_value']), 'producer_socle_evaluation')
    selected = [2, 4, 5, 6, 7]
    rows = []
    for j in selected:
        commutator = matrix_sub(matrix_mul(flags[1], flags[j]), matrix_mul(flags[j], flags[1]))
        check(all(not p for row in commutator[1:] for p in row), 'commutator_image_in_line')
        check(not commutator[0][0], 'commutator_kills_line')
        rows.append(commutator[0][1:])
    det = determinant(rows)
    check(all(isinstance(c, int) for c in det.values()), 'integer_determinant_coefficients')
    expected = parse('(s-1)**6*(t-1)**6*(t+1)/t**4')
    check(det == expected, 'integral_five_by_five_determinant')
    matching = [r for r in symbolic['nonzero_five_by_five_commutator_minors']
                if r['source_pairs'] == [[1, j] for j in selected]]
    check(len(matching) == 1 and parse(matching[0]['determinant']) == expected,
          'producer_selected_determinant')
    # The exact identity has integer coefficients and only Laurent-unit
    # denominators. No prime or characteristic is excluded by the audit.
    output = producer.with_name('affine_product_one_two_parameter_independent_audit_output.json')
    result = {'status': 'PASS_INTEGRAL_TWO_PARAMETER_LITERAL_SOURCE_AUDIT',
              'producer_sha256': sha256(producer.read_bytes()).hexdigest(),
              'inputs': {str(paths[name]): hashes[name] for name in paths},
              'ring': 'Z[s^+-1,t^+-1]; delta7^-1 used only through a cleared identity',
              'source_words': 11, 'seed_words': 8,
              'source_diagonals': scalar_rows, 'seed_data': seed_data,
              'selected_commutator_indices': selected,
              'selected_commutator_rows': [[serialize(p) for p in row] for row in rows],
              'determinant': serialize(det),
              'determinant_formula': '(s-1)^6*(t-1)^6*(t+1)/t^4',
              'kappa_socle_value': serialize(value),
              'source_kappa_socle_value': serialize(next_value),
              'checks': dict(CHECKS), 'check_total': sum(CHECKS.values()),
              'independence': 'No producer imports and no computer algebra package. Generic integral affine multiplication evaluates the original braid words; strict Laurent parsing checks the displayed identities; a 120-term permutation determinant verifies the exact nonzero-factor certificate.'}
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': result['check_total'],
                      'source_words': 11, 'seed_words': 8,
                      'determinant_formula': result['determinant_formula'],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
