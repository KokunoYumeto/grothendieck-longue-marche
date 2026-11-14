"""Independent integral audit of the full product-one source-module proof.

No new producer or symbolic algebra package is imported. The previously
reviewed Laurent word evaluator reconstructs all eleven original words on
each retained principal chart. This checker verifies the quotient matrices
by cleared intertwining identities, rather than the producer's Laurent
division. It then checks annihilators, explicitly prescribed left eigenrows,
determinants, and all fifteen sign-stratum necessary lifts using sparse
integer Laurent arithmetic. No finite-field sampling is used.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json
import runpy


CHECKS = Counter()


def check(test, category):
    assert test, category
    CHECKS[category] += 1


def plus(left, right):
    answer = dict(left)
    for exponent, coefficient in right.items():
        value = answer.get(exponent, 0) + coefficient
        if value:
            answer[exponent] = value
        else:
            answer.pop(exponent, None)
    return answer


def neg(poly):
    return {exponent: -coefficient for exponent, coefficient in poly.items()}


def times(left, right):
    answer = {}
    for e, a in left.items():
        for f, b in right.items():
            exponent = tuple(x+y for x, y in zip(e, f))
            answer[exponent] = answer.get(exponent, 0) + a*b
    return {e: a for e, a in answer.items() if a}


def mm(left, right):
    answer = [[{} for _ in right[0]] for _ in left]
    for i, row in enumerate(left):
        for k, entry in enumerate(row):
            for j, other in enumerate(right[k]):
                if entry and other:
                    answer[i][j] = plus(answer[i][j], times(entry, other))
    return answer


def minus(left, right):
    return [[plus(a, neg(b)) for a, b in zip(row, old)]
            for row, old in zip(left, right)]


def scale(poly, matrix):
    return [[times(poly, entry) for entry in row] for row in matrix]


def eye(n, one):
    return [[one if i == j else {} for j in range(n)] for i in range(n)]


def shifted(matrix, scalar):
    answer = [[dict(entry) for entry in row] for row in matrix]
    for i in range(len(answer)):
        answer[i][i] = plus(answer[i][i], neg(scalar))
    return answer


def determinant(matrix, one):
    answer = {}
    for order in permutations(range(len(matrix))):
        sign = sum(order[i] > order[j] for i in range(len(order))
                   for j in range(i+1, len(order))) % 2
        term = neg(one) if sign else one
        for i, j in enumerate(order):
            term = times(term, matrix[i][j])
        answer = plus(answer, term)
    return answer


def unpack(poly):
    return {tuple(exponent): coefficient for coefficient, exponent in poly}


def unpack_matrix(matrix):
    return [[unpack(entry) for entry in row] for row in matrix]


def generic_rows():
    # B=t-1, H=rt-t+1, A=rst and c=rstuvw are exact Laurent abbreviations.
    return {
        6: ['-A*(c-1)*H', '-B*(c-1)*(A*H+1)',
            '-A*u*B*(c-1)*(H-u)',
            '-A*u*B*(c-1)*(v*(H-u)+u)',
            '-c*B*((c-1)*(H-u)+c*u/v)'],
        8: ['w-1', 'B*(w-1)', 'u*B*(w-1)', '-u*v*B', '0'],
        9: ['A*(u-1)', 'B*(A*(u-1)-1)', 'A*u*B*(u-1)',
            'A*u*v*B*(u-1)', 'c*B*(u-1)'],
        10: ['v-1', 'B*(v-1)', '-u*B*((r-1)*v+1)',
             '-u*v*(r-1)*B*(v-1)', '-u*v*w*(r-1)*B*(v-1)'],
        1: ['c-1', 'B*(c-1)', 'u*B*(c-1)', 'u*v*B*(c-1)', 'c*u*v*w*B'],
        3: ['s*t*v*(w-1)', 'B*(w-1)*(s*t*v+1)',
            '-s*t*u*v*(r-1)*B*(w-1)',
            '-s*t*u*v*B*((w-1)*L+r*u)', '-s*t*u*v*w*B*(w-1)*L'],
        4: ['-A*(u-1)*H', '-B*(A*H*(u-1)-1)',
            '-A*u*B*(u-1)*H', '-A*u*v*B*(u-1)*H', '-c*B*(u-1)*H'],
        5: ['-A*w*(v-1)', '-A*w*B*(v-1)', '-B*(A*u*w*(v-1)-1)',
            '-B*(v-1)*(c-1)', '-c*w*B*(v-1)']}


def r1_rows():
    return {
        6: ['-(s*t+1)*(c-1)', 's*t*u*(u-1)*(c-1)',
            's*t*u*(c-1)*(u*v-u-v)', 'c*(c*u-c*u/v-c-u+1)'],
        8: ['1-w', '-u*(w-1)', 'u*v', '0'],
        9: ['-s*t*u+s*t+1', '-s*t*u*(u-1)',
            '-s*t*u*v*(u-1)', '-c*(u-1)'],
        10: ['1-v', 'u', '0', '0']}


def chart_specs():
    return [
        {'name': 'r_nontrivial_X1_pivot', 'names': ['r', 's', 't', 'u', 'v', 'w'],
         'characters': [[int(i == j) for i in range(6)] for j in range(6)] + [[-1]*6],
         'pivot': 0, 'keep': [1, 2, 3, 4, 5, 6], 'dimension': 5,
         'boundary': ['1', 'r', 'r*s', 'r*s*t', 'r*s*t*u', 'r*s*t*u*v', 'r*s*t*u*v*w'],
         'basis': [['-s', '-s*t', '-s*t*u', '-s*t*u*v', '-s*t*u*v*w', '1/r'],
                   ['1', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'],
                   ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0'],
                   ['0', '0', '0', '0', '1', '0']],
         'inverse': [['0', '1', '0', '0', '0', '0'], ['0', '0', '1', '0', '0', '0'],
                     ['0', '0', '0', '1', '0', '0'], ['0', '0', '0', '0', '1', '0'],
                     ['0', '0', '0', '0', '0', '1'],
                     ['r', 'r*s', 'r*s*t', 'r*s*t*u', 'r*s*t*u*v', 'r*s*t*u*v*w']]},
        {'name': 'r_equals_one_X3_pivot', 'names': ['s', 't', 'u', 'v', 'w'],
         'characters': [[0]*5] + [[int(i == j) for i in range(5)] for j in range(5)] + [[-1]*5],
         'pivot': 2, 'keep': [0, 1, 3, 4, 5, 6], 'dimension': 4,
         'boundary': ['1', '1', 's', 's*t', 's*t*u', 's*t*u*v', 's*t*u*v*w'],
         'basis': [['0', '0', '0', '0', '0', '1'],
                   ['-s*t', '-s*t*u', '-s*t*u*v', '-s*t*u*v*w', '1', '-1'],
                   ['1', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'],
                   ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0']],
         'inverse': [['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0'],
                     ['0', '0', '0', '0', '1', '0'], ['0', '0', '0', '0', '0', '1'],
                     ['1', '1', 's*t', 's*t*u', 's*t*u*v', 's*t*u*v*w'],
                     ['1', '0', '0', '0', '0', '0']]}
    ]


def check_chart(specification, data, words, evaluator):
    configure, parse, pm = [evaluator[key] for key in ['configure', 'parse', 'parse_matrix']]
    configure(specification['names'], specification['characters'])
    one = parse('1')
    namespace = parse.__globals__
    namespace['UNITS']['r'] = parse('1') if specification['dimension'] == 4 else parse('r')
    namespace['UNITS']['c'] = parse('r*s*t*u*v*w')
    for name, text in [('A', 'r*s*t'), ('B', 't-1'), ('H', 'r*t-t+1'),
                       ('L', 'r*u+(r-1)*v-r')]:
        namespace['UNITS'][name] = parse(text)
    check(data['name'] == specification['name'], 'chart_name')
    check(data['character_exponents'] == specification['characters'], 'exact_character_map')
    check(data['principal_pivot_original_index'] == specification['pivot']+1, 'original_principal_pivot')
    check(data['quotient_original_indices'] == [i+1 for i in specification['keep']], 'original_quotient_order')
    basis, inverse = pm(specification['basis']), pm(specification['inverse'])
    check(basis == pm(data['basis']) and inverse == pm(data['inverse_basis']), 'displayed_basis_data')
    check(mm(basis, inverse) == eye(6, one), 'basis_inverse')
    check(mm(inverse, basis) == eye(6, one), 'inverse_basis')
    section = [[{} for _ in range(6)] for _ in range(7)]
    for j, i in enumerate(specification['keep']):
        section[i][j] = one
    lift = mm(section, basis)
    delta = [[plus({tuple(e): 1}, neg(one))] for e in specification['characters']]
    boundary = pm([specification['boundary']])
    check(mm(boundary, delta) == [[{}]], 'boundary_descends_exactly')
    check(mm(boundary, lift) == pm([['0']*specification['dimension']+
          ['1']+(['0'] if specification['dimension'] == 4 else [])]), 'displayed_boundary_coordinate')
    boundary_table = ['1', '1', 'r*t', '1', '1', '1', '1/u**2', '1/t', '1/v**2', '1/w**2', 'c**2']
    x1_table = ['1', '1/u**2', '1/t', '1/v**2', '1/w**2', 'c**2', '1', 't', '1', '1', '1']
    output = {}
    for index, record in enumerate(data['source_records']):
        word = words[index]
        check(word['index'] == record['index'] == index, 'actual_original_source_index')
        check(word['label'] == record['label'], 'actual_original_source_label')
        decoration, action = evaluator['literal_braid'](word['negative_braid'])
        check(action == unpack_matrix(record['action_7']), 'full_literal_action_matches_data')
        check(mm(action, delta) == delta, 'principal_line_fixed')
        scalar = {decoration[0]: 1}
        check(scalar == parse(boundary_table[index]), 'boundary_character_table')
        check(scalar == unpack(record['boundary_scalar']), 'boundary_character_record')
        check(mm(boundary, action) == scale(scalar, boundary), 'literal_boundary_quotient')
        block = unpack_matrix(record['block_matrix_6'])
        image = mm(action, lift)
        check(scale(delta[specification['pivot']][0], minus(image, mm(lift, block))) ==
              mm(delta, [image[specification['pivot']]]), 'cleared_actual_quotient_intertwiner')
        dimension = specification['dimension']
        check(all(not block[i][j] for i in range(dimension, 6)
                  for j in range(6) if i != j), 'invariant_core_and_diagonal_quotient')
        check(block[dimension][dimension] == scalar, 'block_boundary_scalar')
        core = [row[:dimension] for row in block[:dimension]]
        check(core == unpack_matrix(record['core_matrix']), 'core_record_exact')
        if dimension == 5 and index == 0:
            check(core == scale(parse('r'), eye(5, one)), 'source_zero_scalar_on_W5')
        if dimension == 4:
            x1 = parse(x1_table[index])
            check(action[0] == [x1]+[{}]*6, 'literal_X1_quotient')
            check(block[5][5] == x1 == unpack(record['X1_scalar']), 'block_X1_scalar')
        output[index] = {'matrix': block, 'core': core}
    print(json.dumps({'completed_word_chart': specification['name'], 'words': 11}), flush=True)
    return output


def check_moving(dimension, matrices, certificate, evaluator):
    parse, pm = evaluator['parse'], evaluator['parse_matrix']
    one = parse('1')
    targets = [
        (6, ['1', '1/(v*w)'], 'c/t'), (8, ['1', 'c/u'], '1/(t*w)'),
        (9, ['1', 'c/v'], '1/(t*u)'), (10, ['1', '1/(u*w)'], '1/(t*v)')]
    if dimension == 5:
        targets += [(1, ['1', '1/(v*w)', '1/(r**2*u**2)'], 'c/t'),
                    (3, ['1', 'c/u', '1/(r**2*v**2)'], '1/(t*w)'),
                    (4, ['1', 'c/v', '1/(r**2*w**2)'], '1/(t*u)'),
                    (5, ['1', '1/(u*w)', '(c/r)**2'], '1/(t*v)')]
    prescribed = generic_rows() if dimension == 5 else r1_rows()
    rows, roots = {}, {}
    for index, base_texts, moving_text in targets:
        record = next(x for x in certificate['records'] if x['index'] == index)
        bases, moving = [parse(text) for text in base_texts], parse(moving_text)
        stored_base = record['base_roots'] if dimension == 5 else ['1', record['base_root']]
        check(bases == [parse(text) for text in stored_base], 'moving_base_root_table')
        check(moving == parse(record['moving_root']), 'moving_root_table')
        q = pm([prescribed[index]])
        check(q == pm([record['primitive_row']]), 'displayed_primitive_eigenrow')
        matrix = matrices[index]['core']
        check(mm(q, matrix) == scale(moving, q), 'direct_left_moving_eigenrow')
        operator = eye(dimension, one)
        tau = one
        for base in bases:
            operator = mm(operator, shifted(matrix, base))
            tau = times(tau, plus(moving, neg(base)))
        check(mm(operator, shifted(matrix, moving)) ==
              [[{} for _ in range(dimension)] for _ in range(dimension)], 'full_moving_annihilator')
        trace = {}
        for j in range(dimension):
            trace = plus(trace, operator[j][j])
        check(trace == tau == parse(record['trace']), 'moving_operator_trace_product')
        check(mm(q, operator) == scale(tau, q), 'eigenrow_polynomial_evaluation')
        rows[index], roots[index] = q[0], (bases, moving, tau)
        print(json.dumps({'completed_moving_operator': index, 'dimension': dimension}), flush=True)
    if dimension == 4:
        expected = parse('u**2*c**2')
        check(determinant([rows[i] for i in [6, 8, 9, 10]], one) == expected,
              'r1_unit_row_determinant')
        check(parse(certificate['row_determinant']) == expected, 'r1_determinant_record')
    else:
        determinants = {
            1: 'c*u**2*v*w*(r-1)*B**4*(c-1)*(r*t*v+u*v-u)',
            3: 'c**2*u**2*(r-1)*B**4*(w-1)',
            4: 'r*t*c**2*u**2*(r-1)*B**4*(u-1)',
            5: '-c*u*v*w*(r-1)*B**4*(v-1)*((c-1)*(r*t+u)-c*u/v)'}
        for index, text in determinants.items():
            value = determinant([rows[i] for i in [6, 8, 9, 10, index]], one)
            check(value == parse(text), 'generic_row_determinant')
            check(value == parse(certificate['row_determinants_by_positive_source'][str(index)]),
                  'generic_determinant_record')
    return rows, roots


SIGN_TABLE = [
    ((1, 1, 1, -1), [0, 0, 0, 0], 1, 3, '-2*(t+1)/t'),
    ((1, 1, -1, 1), [0, 0, -2, 0], 3, 2, '2*(t+1)/t'),
    ((1, 1, -1, -1), [0, 0, 2, 0], 1, 2, '-4'),
    ((1, -1, 1, 1), [0, 0, 0, 0], 5, 1, '-2*(t+1)/t'),
    ((1, -1, 1, -1), [0, 0, 0, 0], 1, 1, '4'),
    ((1, -1, -1, 1), [0, 0, -2, 0], 3, 1, '4/t'),
    ((1, -1, -1, -1), [0, 0, 2, 0], 1, 1, '4'),
    ((-1, 1, 1, 1), [-2, 0, 0, 0], 4, 0, '2*(t+1)/t'),
    ((-1, 1, 1, -1), [-2, 0, 0, -4], 1, 0, '4'),
    ((-1, 1, -1, 1), [2, 0, 2, 0], 3, 0, '4*(2*t-1)/t'),
    ((-1, 1, -1, -1), [2, 0, 6, 4], 1, 0, '4'),
    ((-1, -1, 1, 1), [-2, -4, 0, 0], 4, 0, '2*(3*t-1)/t'),
    ((-1, -1, 1, -1), [-2, -4, 0, -4], 1, 0, '-4'),
    ((-1, -1, -1, 1), [2, 4, 2, 0], 3, 0, '4*(2*t-1)/t'),
    ((-1, -1, -1, -1), [2, 4, 6, 4], 1, 0, '-4')]


def check_signs(matrices, rows, roots, certificate, evaluator):
    evaluator['configure'](['t'], [[0]]*7)
    parse, pm = evaluator['parse'], evaluator['parse_matrix']
    one = parse('1')
    check([x[0] for x in SIGN_TABLE] == [x for x in product([1, -1], repeat=4)
                                       if x != (1, 1, 1, 1)], 'all_fifteen_sign_strata')
    summaries = []
    for table, record in zip(SIGN_TABLE, certificate['strata']):
        signs, forced, source, coordinate, residual_text = table
        u, v, w, c = signs
        epsilon = c*u*v*w
        check(tuple(record['signs'][name] for name in ['u', 'v', 'w', 'c']) == signs,
              'exact_sign_stratum_record')
        check(record['s_coefficient_epsilon'] == epsilon, 'exact_sign_coefficient_map')

        def coefficient_map(poly):
            answer = {}
            for (a, b, d, e, f), value in poly.items():
                sign = (-1 if epsilon == -1 and a % 2 else 1)
                for scalar, exponent in [(u, d), (v, e), (w, f)]:
                    if scalar == -1 and exponent % 2:
                        sign = -sign
                answer = plus(answer, {(b-a,): value*sign})
            return answer

        def matrix_map(matrix):
            return [[coefficient_map(entry) for entry in row] for row in matrix]

        actual = {i: matrix_map(item['matrix']) for i, item in matrices.items()}
        q = matrix_map([rows[i] for i in [6, 8, 9, 10]])
        check(q == pm(record['core_row_matrix']), 'specialized_core_rows')
        check(determinant(q, one) == one, 'sign_unit_determinant')
        inverse = pm(record['core_row_inverse'])
        check(mm(q, inverse) == eye(4, one), 'sign_row_right_inverse')
        check(mm(inverse, q) == eye(4, one), 'sign_row_left_inverse')
        extended = pm(record['extended_moving_rows'])
        check([row[:4] for row in extended] == q, 'extended_row_first_four_coordinates')
        for position, index in enumerate([6, 8, 9, 10]):
            bases, moving, tau = roots[index]
            operator = eye(6, one)
            for base in bases:
                operator = mm(operator, shifted(actual[index], coefficient_map(base)))
            check(mm([q[position]], operator[:4]) ==
                  scale(coefficient_map(tau), [extended[position]]), 'cleared_extended_row_identity')
        boundary = pm([[str(a)] for a in forced+[1, 0]])
        check(boundary == pm(record['candidates'][0]['candidate']), 'displayed_boundary_necessary_lift')
        check(mm(extended, boundary) == [[{}]]*4, 'necessary_boundary_lift_constraints')
        for candidate in record['candidates']:
            vector = pm(candidate['candidate'])
            check(mm(extended, vector) == [[{}]]*4, 'stored_lift_constraints')
            for item in candidate['all_source_residuals']:
                index = item['index']
                scalar = ('t' if index == 2 else '1/t' if index == 7 else '1')
                if candidate['type'] == 'X1':
                    scalar = ('1/t' if index == 2 else 't' if index == 7 else '1')
                residual = minus(mm(actual[index], vector), scale(parse(scalar), vector))
                check(residual == pm(item['residual']), 'all_stored_sign_source_residuals')
        selected = record['candidates'][0]['selected_all_odd_characteristic_nonzero_residual']
        check((selected['source_index'], selected['coordinate_zero_based']) == (source, coordinate),
              'selected_boundary_source_coordinate')
        residual = minus(mm(actual[source], boundary), boundary)[coordinate][0]
        check(residual == parse(residual_text) == parse(selected['residual']),
              'displayed_nonzero_boundary_residual')
        summaries.append({'signs': list(signs), 'boundary_core_lift': forced,
                          'source_zero_based': source, 'coordinate_zero_based': coordinate,
                          'residual': residual_text})
    check(len(certificate['strata']) == 15, 'exact_stratum_count')
    return summaries


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    inputs = {
        'word_arithmetic': folder/'affine_four_parameter_extension_independent_audit.py',
        'original_words': folder/'full_cross_source_stage/marginal_braids.json',
        'retained_data': folder/'affine_product_one_retained_pivots_stage_output.json',
        'generic_rows': folder/'affine_product_one_generic_moving_rows_stage_output.json',
        'r1_rows': folder/'affine_product_one_r1_moving_rows_stage_output.json',
        'sign_strata': folder/'affine_product_one_sign_strata_lifts_stage_output.json'}
    evaluator = runpy.run_path(str(inputs['word_arithmetic']))
    retained = json.loads(inputs['retained_data'].read_text())
    generic = json.loads(inputs['generic_rows'].read_text())
    r1 = json.loads(inputs['r1_rows'].read_text())
    signs = json.loads(inputs['sign_strata'].read_text())
    for path, data in [(inputs['retained_data'], retained), (inputs['generic_rows'], generic),
                       (inputs['r1_rows'], r1), (inputs['sign_strata'], signs)]:
        producer = path.with_name(path.name.replace('_output.json', '.py'))
        check(data['producer_sha256'] == sha256(producer.read_bytes()).hexdigest(), 'producer_binding')
        inputs['producer_'+producer.stem] = producer
        for input_path, expected_hash in data['inputs'].items():
            basename = Path(input_path).name
            resolved = (folder/'full_cross_source_stage'/basename if basename == 'marginal_braids.json'
                        else folder/basename)
            check(sha256(resolved.read_bytes()).hexdigest() == expected_hash, 'producer_input_binding')
    words = [record for record in json.loads(inputs['original_words'].read_text())['records']
             if record['index'] < 11]
    outputs = []
    for position, specification in enumerate(chart_specs()):
        matrices = check_chart(specification, retained['charts'][position], words, evaluator)
        rows, roots = check_moving(specification['dimension'], matrices,
                                  generic if position == 0 else r1, evaluator)
        outputs.append({'chart': specification['name'], 'core_dimension': specification['dimension'],
                        'literal_words': 11, 'moving_operators': 8 if position == 0 else 4})
        if position == 1:
            sign_summaries = check_signs(matrices, rows, roots, signs, evaluator)
    word_checks = dict(evaluator['parse'].__globals__['CHECKS'])
    result = {'status': 'PASS_FULL_PRODUCT_ONE_LITERAL_WORD_MODULE_AUDIT',
              'verifier_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest() for path in inputs.values()},
              'charts': outputs, 'sign_strata': sign_summaries,
              'checks': dict(CHECKS), 'check_total': sum(CHECKS.values()),
              'reviewed_word_and_parser_checks': word_checks,
              'reviewed_word_and_parser_check_total': sum(word_checks.values()),
              'total_exact_checks': sum(CHECKS.values())+sum(word_checks.values()),
              'scope': 'Exact integer Laurent identities from all eleven literal original source words on both retained principal charts, independently checked quotient intertwiners, twelve moving-root annihilators/eigenrows, five determinants and all fifteen sign coefficient maps/necessary lifts/residual obstructions. The field arguments and affine consequence are supplied in the proof.'}
    output = script.with_name('affine_full_product_one_independent_audit_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': result['total_exact_checks'],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
