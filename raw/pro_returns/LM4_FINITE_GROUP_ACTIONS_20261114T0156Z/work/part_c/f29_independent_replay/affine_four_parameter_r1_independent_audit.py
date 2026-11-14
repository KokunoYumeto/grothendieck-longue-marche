"""Literal-word audit of the r=1 four-parameter cohomology chart.

The generic affine word evaluator and integral Laurent arithmetic are loaded
from the separate three-chart verifier. No producer or algebra package is
imported. Candidate quotient matrices are transported by the displayed
Laurent basis and are then checked against every original source word.
"""
from hashlib import sha256
from pathlib import Path
import json
import runpy


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    arithmetic = folder / 'affine_four_parameter_extension_independent_audit.py'
    ns = runpy.run_path(str(arithmetic))
    names = ['s', 't', 'u']
    characters = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
                  (0, 0, 0), (0, 0, 0), (-1, -1, -1)]
    ns['configure'](names, characters)
    namespace = ns['parse'].__globals__
    namespace['UNITS']['r'] = namespace['ONE']
    namespace['UNITS']['c'] = ns['parse']('s*t*u')
    check = ns['check']
    parse = ns['parse']
    pm = ns['parse_matrix']
    mm = ns['matrix_mul']
    ms = ns['matrix_sub']
    sm = ns['scalar_mul']
    identity = ns['identity']
    serial = ns['serial_matrix']

    candidate = folder / 'affine_product_one_four_parameter_stage_output.json'
    candidate_code = folder / 'affine_product_one_four_parameter_stage.py'
    words_path = folder / 'full_cross_source_stage/marginal_braids.json'
    universal_path = folder / 'affine_obstruction_stage_output.json'
    source = json.loads(candidate.read_text())
    words = json.loads(words_path.read_text())
    check(source['producer_sha256'] == sha256(candidate_code.read_bytes()).hexdigest(),
          'candidate_producer_binding')
    check(source['source_sha256'] == sha256(universal_path.read_bytes()).hexdigest(),
          'candidate_universal_binding')

    basis_strings = [
        ['0', '0', '0', '1', '0', '0'],
        ['-s', '-s*t', '1', '-1', '-c', '-c'],
        ['1', '0', '0', '0', '0', '0'],
        ['0', '1', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '1'],
    ]
    inverse_strings = [
        ['0', '0', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '0', '0'],
        ['1', '1', 's', 's*t', 'c', 'c'],
        ['1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '1'],
    ]
    basis, inverse = pm(basis_strings), pm(inverse_strings)
    check(mm(basis, inverse) == identity(6), 'explicit_basis_inverse')
    check(mm(inverse, basis) == identity(6), 'explicit_inverse_basis')
    section = identity(6) + [[{} for _ in range(6)]]
    lift = mm(section, basis)
    delta = [[ns['add']({e: 1}, ns['negative'](namespace['ONE']))]
             for e in characters]
    quotient_table = [
        ['1', '1', '1', '1'],
        ['1', '1/u**2', '1', '1'],
        ['t', '1/t', 't/u', 'c*t'],
        ['1', '1', '1', '1/t'],
        ['1', '1', 'c', '1'],
        ['1', 'c**2', '1/t', '1/u'],
        ['1/u**2', '1', '1', '1'],
        ['1/t', 't', 't/u', 'c*t'],
        ['1', '1', '1', '1/t'],
        ['1', '1', 'c', '1'],
        ['c**2', '1', '1/t', '1/u'],
    ]
    old = [x for x in words['records'] if x['index'] < 11]
    check(len(old) == len(source['source_records']) == 11, 'eleven_actual_sources')
    records, blocks, cores = [], [], []
    for index, (word, shown) in enumerate(zip(old, source['source_records'])):
        check(word['index'] == shown['index'] == index and word['label'] == shown['label'],
              'actual_source_index_and_label')
        decoration, action = ns['literal_braid'](word['negative_braid'])
        check(action == pm(shown['action_7']), 'literal_seven_dimensional_action')
        check(mm(action, delta) == delta, 'literal_principal_vector_fixed')
        quotient = pm(shown['action_H1_6'])
        block = mm(mm(inverse, quotient), basis)
        lhs, rhs = mm(action, lift), mm(lift, block)
        check(sm(delta[6][0], ms(lhs, rhs)) == mm(delta, [lhs[6]]),
              'literal_denominator_cleared_quotient')
        check(all(not block[i][j] for i in range(2, 6) for j in range(6) if i != j),
              'invariant_core_and_four_character_quotient')
        check([block[i][i] for i in range(2, 6)] == [parse(x) for x in quotient_table[index]],
              'all_four_quotient_characters')
        core = [row[:2] for row in block[:2]]
        blocks.append(block)
        cores.append(core)
        records.append({'source_index_zero_based': index, 'source_label': word['label'],
                        'decoration_scalar': ns['serialize']({decoration[0]: 1}),
                        'block_matrix': serial(block), 'core_matrix': serial(core),
                        'quotient_characters': quotient_table[index]})
    for index in (2, 7):
        check(cores[index] == sm(parse('t'), identity(2)), 'two_scalar_core_operators')
    for index in (0, 5, 10):
        check(cores[index] == identity(2), 'identity_core_operators')
    for index, scalar in [(8, 'c/u'), (9, '1/(t*u)')]:
        polynomial = mm(ms(cores[index], identity(2)),
                        ms(cores[index], sm(parse(scalar), identity(2))))
        check(all(not x for row in polynomial for x in row),
              'literal_integral_quadratic_core_annihilator')

    inputs = [arithmetic, candidate, candidate_code, words_path, universal_path]
    result = {
        'status': 'PASS_R1_FOUR_PARAMETER_LITERAL_WORD_CHART',
        'producer_sha256': sha256(script.read_bytes()).hexdigest(),
        'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in inputs},
        'variables': names, 'coefficient_abbreviation': 'c=s*t*u',
        'character_exponents': characters, 'principal_pivot_original_index': 7,
        'basis': basis_strings, 'inverse_basis': inverse_strings,
        'coordinate_order': ['core_x', 'core_y', 'boundary', 'X1', 'X5', 'X6'],
        'source_records': records,
        'core_annihilators': {'8': '(z-1)*(z-c/u)', '9': '(z-1)*(z-1/(t*u))'},
        'checks': dict(namespace['CHECKS']), 'check_total': sum(namespace['CHECKS'].values()),
        'independence': 'Every source is reconstructed from the original decorated Artin word with integer Laurent arithmetic. The candidate cohomology matrix is checked through the exact original seven-dimensional action with only the displayed principal-pivot denominator cleared.',
        'scope': 'The r=1,c!=1 chart maps, all eleven source matrices, four quotient characters and two core annihilators. The field separation and the separately audited exceptional forced lifts are written in the F29 proof.'
    }
    output = script.with_name('affine_four_parameter_r1_independent_audit_output.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'check_total': result['check_total'],
                      'literal_word_evaluations': 11,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
