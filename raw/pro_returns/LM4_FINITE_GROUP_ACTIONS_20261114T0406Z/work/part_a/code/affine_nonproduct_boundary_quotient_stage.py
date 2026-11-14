"""Exact exploratory boundary-coordinate module for arbitrary characters.

The seven scalars are independent Laurent variables. The actual H1
identification uses h-1, where h is their product. The integral source
matrices themselves are computed without this division. Every original
old source is reconstructed from its literal decorated Artin word.
This program establishes only the recorded coordinate/source identities.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import runpy


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    products = folder/'affine_full_product_one_independent_audit.py'
    words_path = folder/'full_cross_source_stage/marginal_braids.json'
    universal_path = folder/'affine_obstruction_stage_output.json'
    arithmetic = runpy.run_path(str(helper))
    sparse = runpy.run_path(str(products))
    add, neg, mul, mm, sub, scale, eye = [sparse[name] for name in
                                         ['plus', 'neg', 'times', 'mm', 'minus', 'scale', 'eye']]
    shifted, unpack, unpack_matrix = [sparse[name] for name in ['shifted', 'unpack', 'unpack_matrix']]
    serial = arithmetic['serial_matrix']
    names = ['r', 's', 't', 'u', 'v', 'w', 'z']
    characters = [[int(i == j) for i in range(7)] for j in range(7)]
    arithmetic['configure'](names, characters)
    parse, pm = arithmetic['parse'], arithmetic['parse_matrix']
    one = parse('1')
    h = parse('r*s*t*u*v*w*z')
    arithmetic['parse'].__globals__['UNITS']['h'] = h
    delta = [[parse(name+'-1')] for name in names]
    boundary = pm([['1', 'r', 'r*s', 'r*s*t', 'r*s*t*u', 'r*s*t*u*v', 'r*s*t*u*v*w']])
    h_minus_one = add(h, neg(one))
    cleared = sub(scale(h_minus_one, eye(7, one)), mm(delta, boundary))
    inclusion = [[{} for _ in range(6)] for _ in range(7)]
    for j in range(6):
        inclusion[0][j] = neg(boundary[0][j+1])
        inclusion[j+1][j] = one
    projection = [[{} for _ in range(7)] for _ in range(6)]
    for j in range(6):
        projection[j][j+1] = one
    checks = Counter()

    def check(test, name):
        assert test, name
        checks[name] += 1

    check(mm(boundary, delta) == [[h_minus_one]], 'actual_boundary_principal_pairing')
    check(mm(cleared, delta) == [[{}]]*7, 'cleared_projection_principal_kernel')
    check(mm(boundary, cleared) == [[{}]*7], 'cleared_projection_boundary_kernel')
    check(mm(cleared, cleared) == scale(h_minus_one, cleared), 'cleared_projection_idempotence')
    check(mm(boundary, inclusion) == [[{}]*6], 'six_coordinate_boundary_kernel')
    check(mm(projection, inclusion) == eye(6, one), 'six_coordinate_left_inverse')
    first_coordinate = [[one]]+[[{}]]*6
    check(mm(inclusion, projection) == sub(eye(7, one), mm(first_coordinate, boundary)),
          'six_coordinate_right_inverse_on_boundary_kernel')
    check(mm(cleared, inclusion) == scale(h_minus_one, inclusion), 'cleared_principal_section')
    check(mm(mm(inclusion, projection), cleared) == cleared, 'cleared_principal_quotient_inverse')
    words = {record['index']: record for record in json.loads(words_path.read_text())['records']
             if record['index'] < 11}
    universal = {record['index']: record for record in json.loads(universal_path.read_text())['records']
                 if record['index'] < 11}
    character_table = ['1', '1', 'r*t', '1', '1', '1', '1/u**2',
                       '1/(h*t)', '1/v**2', '1/w**2', '1/z**2']
    records = []
    for index in range(11):
        word, old = words[index], universal[index]
        check(word['label'] == old['label'], 'actual_source_label')
        decoration, action = arithmetic['literal_braid'](word['negative_braid'])
        scalar, row = {decoration[0]: 1}, [decoration[1]]
        check(action == unpack_matrix(old['action_matrix']), 'literal_action_matches_frozen_universal')
        check(scalar == {tuple(old['u_character']): 1}, 'literal_decoration_character_matches_universal')
        check(row == [[unpack(entry) for entry in old['u_derivation_row']]],
              'literal_decoration_derivation_matches_universal')
        check(scalar == parse(character_table[index]), 'actual_general_decoration_character')
        check(mm(row, delta) == [[add(scalar, neg(one))]], 'decoration_principal_pairing')
        check(mm(action, delta) == delta, 'actual_principal_line_fixed')
        corrected = [[add(a, b) for a, b in zip(line, correction)]
                     for line, correction in zip(action, mm(delta, row))]
        check(mm(boundary, corrected) == scale(scalar, boundary), 'corrected_boundary_action')
        check(mm(corrected, delta) == scale(scalar, delta), 'corrected_principal_action')
        check(mm(cleared, action) == mm(corrected, cleared), 'actual_cleared_boundary_quotient_intertwiner')
        matrix = mm(mm(projection, corrected), inclusion)
        check(mm(corrected, inclusion) == mm(inclusion, matrix), 'actual_six_coordinate_source_action')
        trace = {}
        for j in range(6):
            trace = add(trace, matrix[j][j])
        item = {'index': index, 'label': word['label'],
                'decoration_character': arithmetic['serialize'](scalar),
                'boundary_quotient_matrix_6': serial(matrix),
                'trace': arithmetic['serialize'](trace),
                'matrix_monomial_count': sum(len(entry) for line in matrix for entry in line)}
        if index == 0:
            product_matrix = mm(shifted(matrix, parse('r')), shifted(matrix, h))
            item['source_zero_r_h_quadratic_zero'] = all(not entry for line in product_matrix for entry in line)
            item['source_zero_r_h_quadratic_defect'] = serial(product_matrix)
            item['source_zero_trace_equals_5r_plus_h'] = trace == parse('5*r+h')
        records.append(item)
        print(json.dumps({key: value for key, value in item.items()
                          if key not in ['boundary_quotient_matrix_6', 'source_zero_r_h_quadratic_defect']}), flush=True)
    word_checks = dict(parse.__globals__['CHECKS'])
    output = script.with_name('affine_nonproduct_boundary_quotient_stage_output.json')
    result = {'status': 'EXACT_EXPLORATORY_GENERAL_BOUNDARY_QUOTIENT_SOURCE_DATA',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest()
                         for path in [helper, products, words_path, universal_path]},
              'variables': names, 'characters': characters, 'boundary_product': 'r*s*t*u*v*w*z',
              'boundary_row': serial(boundary), 'principal_vector': serial(delta),
              'cleared_projection': serial(cleared), 'basis_inclusion': serial(inclusion),
              'basis_projection': serial(projection), 'records': records,
              'checks': dict(checks), 'check_total': sum(checks.values()),
              'reviewed_word_parser_checks': word_checks,
              'scope': 'Exact original-word source action on the six-dimensional boundary kernel, together with its denominator-cleared principal-quotient maps on h!=1. The source-zero quadratic is recorded as an explicit tested integral identity. No general-character summed-restriction or affine-image equality is asserted.'}
    output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({'status': result['status'], 'checks': result['check_total'],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
