"""Independent literal-word audit of F.32's nonproduct r=1 chart.

This checker imports neither a new producer nor a symbolic algebra package.
It reconstructs every original decorated Artin word directly on the
(h,t,u,v,w,z) chart.  The boundary quotient is checked by cleared
seven-coordinate intertwiners.  Its independently prescribed eigenrows,
annihilators and determinant cover are checked over integer Laurent rings.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json
import runpy


CHECKS = Counter()


def check(test, category):
    assert test, category
    CHECKS[category] += 1


def add(left, right):
    answer = dict(left)
    for exponent, coefficient in right.items():
        value = answer.get(exponent, 0)+coefficient
        if value:
            answer[exponent] = value
        else:
            answer.pop(exponent, None)
    return answer


def negative(poly):
    return {e: -a for e, a in poly.items()}


def multiply(left, right):
    answer = {}
    for e, a in left.items():
        for f, b in right.items():
            exponent = tuple(x+y for x, y in zip(e, f))
            answer[exponent] = answer.get(exponent, 0)+a*b
    return {e: a for e, a in answer.items() if a}


def matmul(left, right):
    answer = [[{} for _ in right[0]] for _ in left]
    for i, row in enumerate(left):
        for k, first in enumerate(row):
            for j, second in enumerate(right[k]):
                if first and second:
                    answer[i][j] = add(answer[i][j], multiply(first, second))
    return answer


def difference(left, right):
    return [[add(a, negative(b)) for a, b in zip(row, old)]
            for row, old in zip(left, right)]


def scale(poly, matrix):
    return [[multiply(poly, entry) for entry in row] for row in matrix]


def identity(size, one):
    return [[one if i == j else {} for j in range(size)] for i in range(size)]


def shift(matrix, scalar):
    answer = [[dict(entry) for entry in row] for row in matrix]
    for i in range(len(matrix)):
        answer[i][i] = add(answer[i][i], negative(scalar))
    return answer


def determinant(matrix, one):
    answer = {}
    for order in permutations(range(len(matrix))):
        parity = sum(order[i] > order[j] for i in range(len(order))
                     for j in range(i+1, len(order))) % 2
        term = negative(one) if parity else one
        for i, j in enumerate(order):
            term = multiply(term, matrix[i][j])
        answer = add(answer, term)
    return answer


def unpack(poly):
    return {tuple(e): a for a, e in poly}


def change(poly, inverse=False, original=False):
    answer = {}
    for exponent, coefficient in poly.items():
        if original:
            exponent = exponent[1:]  # exact original X1 character equals one
        a, b, c, d, e, f = exponent
        target = ((a, b+a, c+a, d+a, e+a, f+a) if inverse
                  else (a, b-a, c-a, d-a, e-a, f-a))
        answer = add(answer, {target: coefficient})
    return answer


def change_matrix(serialized, original=False):
    return [[change(unpack(entry), original=original) for entry in row]
            for row in serialized]


def prescribed_rows():
    # These h-chart formulas are independently prescribed, not imported.
    return {
        1: ['-h*(z-1)/(u*v*w*z)', '-h*(z-1)/(u*v*w*z)',
            '-h*(z-1)/(v*w*z)', '-h*(z-1)/(w*z)', '1-h*(z-1)/z'],
        8: ['-h*(w-1)/(u*v*w)', '-h*(w-1)/(u*v*w)',
            '-h*(w-1)/(v*w)', '1-h*(w-1)/w', '-(h-1)*(w-1)'],
        9: ['h*(u-1)/(u*v*w*z)', 'h*(u-1)/(u*v*w*z)-1',
            'h*(u-1)/(v*w*z)', 'h*(u-1)/(w*z)', 'h*(u-1)/z'],
        10: ['1-v', '1-v', 'u', '0', '0'],
        3: ['-h*(w-1)/(u*w*z)', '-h*(w-1)/(u*w*z)-(w-1)', '0',
            'h*(u*w-w+1)/(w*z)', 'h*(u-1)*(w-1)/z'],
        4: ['h**2*(u-1)/(u**2*w*z)',
            '(h**2*(u-1)+h*u*v*w*z*(u-1)-u**2*v*w*z)/(u**2*w*z)',
            '-h*(u-1)*(h*u-h-u)/(u*w*z)',
            '-h*(u-1)*(h*u*v+h*u*z-h*u-h*v-u*v-u*z+u)/(u*w*z)',
            '-(u-1)*(h**2*u*v*w+h**2*u*w*z-h**2*u*w-h**2*u*z-h**2*v*w-h*u*v*w-2*h*u*w*z+h*u*w+h*u*z+u*w*z)/(u*w*z)'],
        5: ['h*(v-1)/(u*w*z)', 'h*(v-1)/(u*w*z)',
            '-h*(h*z+v*z-v-z+1)/(w*z)',
            '-(v-1)*(h**2*z+h*v*z-h*v+h*w*z-h*z-w*z)/(w*z)',
            '-(v-1)*(h**2*z+h*v*z-h*v+h*w*z-2*h*z-v*z-w*z+z)/z'],
        6: ['h**2*(z-1)/(u**2*w*z**2)',
            'h*(h+u*v*w*z)*(z-1)/(u**2*w*z**2)',
            '-h**2*(u-1)*(z-1)/(u*w*z**2)',
            '-h*(z-1)*(h*u*v+h*u*z-h*u-h*v-u*z)/(u*w*z**2)',
            '-(h**2*u*v*w*z-h**2*u*v*w+h**2*u*w*z**2-2*h**2*u*w*z+h**2*u*w-h**2*u*z**2+h**2*u*z-h**2*v*w*z+h**2*v*w-2*h*u*w*z**2+2*h*u*w*z+h*u*z**2-h*u*z+u*w*z**2)/(u*w*z**2)']}


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    inputs = {
        'word_arithmetic': folder/'affine_four_parameter_extension_independent_audit.py',
        'original_words': folder/'full_cross_source_stage/marginal_braids.json',
        'universal': folder/'affine_obstruction_stage_output.json',
        'producer_sparse_arithmetic': folder/'affine_full_product_one_independent_audit.py',
        'general_data': folder/'affine_nonproduct_boundary_quotient_stage_output.json',
        'source_data': folder/'affine_nonproduct_r1_source_stage_output.json',
        'moving_data': folder/'affine_nonproduct_r1_moving_rows_stage_output.json',
        'determinant_data': folder/'affine_nonproduct_r1_determinants_stage_output.json'}
    data = {key: json.loads(inputs[key].read_text())
            for key in ['universal', 'general_data', 'source_data', 'moving_data', 'determinant_data']}
    for key in ['general_data', 'source_data', 'moving_data', 'determinant_data']:
        producer = inputs[key].with_name(inputs[key].name.replace('_output.json', '.py'))
        check(data[key]['producer_sha256'] == sha256(producer.read_bytes()).hexdigest(), 'producer_binding')
        inputs['producer_'+producer.stem] = producer
        for old_path, expected in data[key]['inputs'].items():
            basename = Path(old_path).name
            resolved = (folder/'full_cross_source_stage'/basename if basename == 'marginal_braids.json'
                        else folder/basename)
            check(sha256(resolved.read_bytes()).hexdigest() == expected, 'producer_input_binding')
    arithmetic = runpy.run_path(str(inputs['word_arithmetic']))
    characters = [[0]*6, [1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(6)] for j in range(1, 6)]
    arithmetic['configure'](['h', 't', 'u', 'v', 'w', 'z'], characters)
    parse, pm = arithmetic['parse'], arithmetic['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(t*u*v*w*z)')
    one, hminusone = parse('1'), parse('h-1')
    check(data['determinant_data']['characters'] == characters, 'actual_character_chart')
    for i in range(6):
        generator = {tuple(int(i == j) for j in range(6)): 1}
        check(change(change(generator), inverse=True) == generator, 'coefficient_map_inverse')
        check(change(change(generator, inverse=True)) == generator, 'inverse_coefficient_map')
    boundary = pm([['1', '1', 's', 's*t', 's*t*u', 's*t*u*v', 's*t*u*v*w']])
    delta = pm([['0'], ['s-1'], ['t-1'], ['u-1'], ['v-1'], ['w-1'], ['z-1']])
    cleared = difference(scale(hminusone, identity(7, one)), matmul(delta, boundary))
    inclusion = [[{} for _ in range(6)] for _ in range(7)]
    projection = [[{} for _ in range(7)] for _ in range(6)]
    for j in range(6):
        inclusion[0][j] = negative(boundary[0][j+1])
        inclusion[j+1][j] = projection[j][j+1] = one
    check(matmul(boundary, delta) == [[hminusone]], 'boundary_principal_pairing')
    check(matmul(cleared, delta) == [[{}]]*7, 'cleared_principal_kernel')
    check(matmul(boundary, cleared) == [[{}]*7], 'cleared_boundary_kernel')
    check(matmul(cleared, cleared) == scale(hminusone, cleared), 'cleared_idempotence')
    check(matmul(boundary, inclusion) == [[{}]*6], 'boundary_kernel_section')
    check(matmul(projection, inclusion) == identity(6, one), 'boundary_section_left_inverse')
    check(matmul(inclusion, projection) == difference(identity(7, one), matmul([[one]]+[[{}]]*6, boundary)),
          'boundary_section_right_inverse')
    check(matmul(cleared, inclusion) == scale(hminusone, inclusion), 'cleared_principal_section')
    check(matmul(matmul(inclusion, projection), cleared) == cleared, 'cleared_principal_quotient_inverse')
    basis = pm([['-s', '-s*t', '-s*t*u', '-s*t*u*v', '-s*t*u*v*w', '1'],
                ['1', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'],
                ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0'],
                ['0', '0', '0', '0', '1', '0']])
    inverse = pm([['0', '1', '0', '0', '0', '0'], ['0', '0', '1', '0', '0', '0'],
                  ['0', '0', '0', '1', '0', '0'], ['0', '0', '0', '0', '1', '0'],
                  ['0', '0', '0', '0', '0', '1'],
                  ['1', 's', 's*t', 's*t*u', 's*t*u*v', 's*t*u*v*w']])
    check(matmul(basis, inverse) == identity(6, one), 'core_basis_right_inverse')
    check(matmul(inverse, basis) == identity(6, one), 'core_basis_left_inverse')
    check(basis == pm(data['source_data']['basis']), 'producer_basis_matches')
    check(inverse == pm(data['source_data']['inverse_basis']), 'producer_inverse_matches')
    lift = matmul(inclusion, basis)
    check(lift[0] == pm([['0', '0', '0', '0', '0', '-1']])[0], 'actual_minus_X1_quotient_coordinate')
    check(matmul(boundary, lift) == [[{}]*6], 'actual_full_lift_boundary_zero')
    words = {r['index']: r for r in json.loads(inputs['original_words'].read_text())['records'] if r['index'] < 11}
    universal = {r['index']: r for r in data['universal']['records'] if r['index'] < 11}
    general = {r['index']: r for r in data['general_data']['records']}
    sources = {r['index']: r for r in data['source_data']['records']}
    moving = {r['index']: r for r in data['moving_data']['records']}
    decoration_table = ['1', '1', 't', '1', '1', '1', '1/u**2', '1/(h*t)', '1/v**2', '1/w**2', '1/z**2']
    quotient_table = ['1', '1/u**2', '1/t', '1/v**2', '1/w**2', '1/z**2', '1', 't/h', '1', '1', '1']
    cores = {}
    for index in range(11):
        word, old = words[index], sources[index]
        check(word['index'] == index and word['label'] == old['label'] == universal[index]['label'], 'actual_source_index_label')
        decoration, action = arithmetic['literal_braid'](word['negative_braid'])
        scalar, row = {decoration[0]: 1}, [decoration[1]]
        check(action == change_matrix(universal[index]['action_matrix'], original=True), 'literal_full_action_matches_universal')
        check(scalar == change({tuple(universal[index]['u_character']): 1}, original=True), 'literal_decoration_scalar')
        check(row == [[change(unpack(p), original=True) for p in universal[index]['u_derivation_row']]], 'literal_decoration_derivative')
        check(scalar == parse(decoration_table[index]), 'original_decoration_character_table')
        check(matmul(action, delta) == delta, 'literal_principal_line_fixed')
        check(matmul(row, delta) == [[add(scalar, negative(one))]], 'literal_decoration_principal_pairing')
        corrected = difference(action, scale(parse('-1'), matmul(delta, row)))
        check(matmul(boundary, corrected) == scale(scalar, boundary), 'corrected_boundary_action')
        check(matmul(corrected, delta) == scale(scalar, delta), 'corrected_principal_action')
        check(matmul(cleared, action) == matmul(corrected, cleared), 'full_cleared_quotient_intertwiner')
        matrix = change_matrix(general[index]['boundary_quotient_matrix_6'], original=True)
        check(matmul(corrected, inclusion) == matmul(inclusion, matrix), 'literal_six_coordinate_quotient')
        block = change_matrix(old['block_matrix_6'])
        check(matmul(matrix, basis) == matmul(basis, block), 'actual_core_basis_intertwiner')
        check(matmul(cleared, matmul(action, lift)) == scale(hminusone, matmul(lift, block)), 'cleared_full_core_quotient_intertwiner')
        check(action[0] == [parse(quotient_table[index])]+[{}]*6, 'literal_X1_evaluation_character')
        check(block[5] == [{}]*5+[parse(quotient_table[index])], 'invariant_core_and_actual_quotient')
        check(old['X1_quotient_character'] == quotient_table[index], 'stored_quotient_character_table')
        core = [row[:5] for row in block[:5]]
        check(core == change_matrix(old['core_matrix_5']), 'core_data_matches')
        for row in block:
            for entry in row:
                check(change(change(entry, inverse=True)) == entry, 'matrix_coefficient_inverse')
        if index == 0:
            check(core == scale(parse('1/h'), identity(5, one)), 'source_zero_scalar_core')
        cores[index] = core
        print(json.dumps({'literal_source_completed': index, 'label': word['label']}), flush=True)
    targets = [(1, ['1', '1/(v*w)'], '1/(t*z)'),
               (3, ['1', '1/(u*z)'], '1/(t*w)'),
               (4, ['1', '1/(v*z)'], '1/(t*u)'),
               (5, ['1', '1/(u*w)'], '1/(t*v)'),
               (6, ['1', '1/(v*w)', '(h/u)**2'], '1/(t*z)'),
               (8, ['1', '1/(u*z)', '(h/v)**2'], '1/(t*w)'),
               (9, ['1', '1/(v*z)', '(h/w)**2'], '1/(t*u)'),
               (10, ['1', '1/(u*w)', '(h/z)**2'], '1/(t*v)')]
    compact = prescribed_rows()
    diagonal = [[(one if i == 0 else parse('t-1')) if i == j else {}
                 for j in range(5)] for i in range(5)]
    rows, hatrows = {}, {}
    for index, bases, moving_text in targets:
        hatrow = pm([compact[index]])
        row = matmul(hatrow, diagonal)
        record = moving[index]
        check(hatrow == pm([data['determinant_data']['compact_rows'][str(index)]]), 'independently_prescribed_compact_row')
        check(row == pm([record['row_q']]), 'exact_eigenrow_column_scaling')
        check([parse(a) for a in bases] == [parse(a) for a in record['base_roots']], 'moving_base_root_table')
        moving_root = parse(moving_text)
        check(moving_root == parse(record['moving_root']), 'moving_root_table')
        core = cores[index]
        check(matmul(row, core) == scale(moving_root, row), 'direct_literal_left_eigenrow')
        operator, tau = identity(5, one), one
        for base in bases:
            operator = matmul(operator, shift(core, parse(base)))
            tau = multiply(tau, add(moving_root, negative(parse(base))))
        check(matmul(operator, shift(core, moving_root)) == [[{}]*5 for _ in range(5)], 'literal_moving_annihilator')
        check(matmul(row, operator) == scale(tau, row), 'direct_eigenrow_polynomial_evaluation')
        trace = {}
        for j in range(5):
            trace = add(trace, operator[j][j])
        check(trace == tau == parse(record['trace_product']), 'moving_trace_product')
        rows[index], hatrows[index] = row[0], hatrow[0]
        print(json.dumps({'moving_source_completed': index}), flush=True)
    determinant_table = {3: 'h*u*(h-1)*(w-1)/(w*z)',
                         4: '-h*(h-1)*(u-1)*(h*w-h-w)/w**2',
                         5: '-h*(h-1)*(v-1)',
                         6: '-h*(h-1)*(z-1)*(h*w-h-w)/(w**2*z)'}
    determinant_summary = []
    for index, formula in determinant_table.items():
        indices = [1, 8, 9, 10, index]
        compact_det = determinant([hatrows[i] for i in indices], one)
        actual_det = determinant([rows[i] for i in indices], one)
        check(compact_det == parse(formula), 'compact_row_determinant')
        check(actual_det == multiply(parse('(t-1)**4'), compact_det), 'actual_column_scaling_determinant')
        stored = next(r for r in data['determinant_data']['determinants'] if r['source_indices_zero_based'] == indices)
        check(compact_det == parse(stored['compact_determinant']), 'compact_determinant_record')
        check(actual_det == parse(stored['actual_determinant']), 'actual_determinant_record')
        determinant_summary.append({'sources_zero_based': indices, 'compact_determinant': formula})
    check(parse('h*1-h-1') == parse('-1'), 'w_equals_one_exceptional_factor')
    word_checks = dict(parse.__globals__['CHECKS'])
    result = {'status': 'PASS_NONPRODUCT_R1_LITERAL_WORD_MODULE_AUDIT',
              'verifier_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest() for path in inputs.values()},
              'literal_word_count': 11, 'moving_source_count': 8,
              'character_chart': {'variables': ['h', 't', 'u', 'v', 'w', 'z'], 'original_characters': characters},
              'quotient_characters': quotient_table, 'determinants': determinant_summary,
              'checks': dict(CHECKS), 'check_total': sum(CHECKS.values()),
              'reviewed_word_and_parser_checks': word_checks,
              'reviewed_word_and_parser_check_total': sum(word_checks.values()),
              'total_exact_checks': sum(CHECKS.values())+sum(word_checks.values()),
              'scope': 'All eleven original decorated words, actual boundary principal quotient and five-dimensional X1 kernel, eight moving-source annihilators/direct eigenrows, explicit ring/basis inverses and four determinant identities over integer Laurent coefficients. The proof supplies the all-finite-field separation and affine-image consequences.'}
    output = script.with_name('affine_nonproduct_r1_independent_audit_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': result['total_exact_checks'],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
