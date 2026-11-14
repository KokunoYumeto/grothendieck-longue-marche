"""Independent literal-word audit for the F30 first-scalar field locus.

No producer or symbolic algebra package is imported. The frozen F29
integer Laurent arithmetic evaluates the three exact original braid
words; independently displayed coefficient maps are checked directly.
"""
from hashlib import sha256
from pathlib import Path
import json
import runpy


def decode(poly):
    return {tuple(exponent): coefficient for coefficient, exponent in poly}


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    arithmetic = folder/'affine_four_parameter_extension_independent_audit.py'
    candidate_path = folder/'affine_product_one_first_scalar_field_stage_output.json'
    producer = folder/'affine_product_one_first_scalar_field_stage.py'
    universal = folder/'affine_obstruction_stage_output.json'
    word_path = folder/'full_cross_source_stage/marginal_braids.json'
    ns = runpy.run_path(str(arithmetic))
    names = ['r', 's', 't', 'u', 'v', 'w']
    characters = [[int(i == j) for i in range(6)] for j in range(6)] + [[-1]*6]
    ns['configure'](names, characters)
    globals_ = ns['parse'].__globals__
    check, parse, pm = [ns[key] for key in ['check', 'parse', 'parse_matrix']]
    mm, ms, sm = [ns[key] for key in ['matrix_mul', 'matrix_sub', 'scalar_mul']]
    identity, serial = ns['identity'], ns['serial_matrix']
    candidate = json.loads(candidate_path.read_text())
    words = {x['index']: x for x in json.loads(word_path.read_text())['records']}
    check(candidate['producer_sha256'] == sha256(producer.read_bytes()).hexdigest(),
          'producer_binding')
    check(candidate['source_sha256'] == sha256(universal.read_bytes()).hexdigest(),
          'universal_binding')
    basis = pm([
        ['-s', '-s*t', '-s*t*u', '-s*t*u*v', '-s*t*u*v*w', '1/r'],
        ['1', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'],
        ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0'],
    ])
    inverse = pm([
        ['0', '1', '0', '0', '0', '0'], ['0', '0', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '0', '0'], ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '1'],
        ['r', 'r*s', 'r*s*t', 'r*s*t*u', 'r*s*t*u*v', 'r*s*t*u*v*w'],
    ])
    check(basis == pm(candidate['basis']), 'displayed_candidate_basis')
    check(inverse == pm(candidate['inverse_basis']), 'displayed_candidate_inverse')
    check(mm(basis, inverse) == identity(6), 'both_basis_maps_first_composite')
    check(mm(inverse, basis) == identity(6), 'both_basis_maps_second_composite')
    section = [[{} for _ in range(6)]]+identity(6)
    lift = mm(section, basis)
    core_lift = [row[:5] for row in lift]
    delta = [[ns['add']({tuple(e): 1}, ns['negative'](globals_['ONE']))]
             for e in characters]
    boundary = pm([['1', 'r', 'r*s', 'r*s*t', 'r*s*t*u',
                    'r*s*t*u*v', 'r*s*t*u*v*w']])
    check(mm(boundary, delta) == [[{}]], 'boundary_principal_vanishing')
    check(mm(boundary, lift) == pm([['0', '0', '0', '0', '0', '1']]),
          'actual_boundary_kernel_and_section')
    expected = {0: ('old0', '1'), 2: ('old_1_1', 'r*t'), 7: ('old_-1_1', '1/t')}
    records = []
    for index, (label, scalar_text) in expected.items():
        word = words[index]
        shown = next(x for x in candidate['source_records'] if x['index'] == index)
        check(word['index'] == shown['index'] == index and word['label'] == shown['label'] == label,
              'original_source_index_and_label')
        decoration, action = ns['literal_braid'](word['negative_braid'])
        check(action == [[decode(poly) for poly in row] for row in shown['action_matrix']],
              'complete_literal_action_comparison')
        check(list(decoration[0]) == shown['u_character'], 'literal_decoration_character')
        scalar = parse(scalar_text)
        check({decoration[0]: 1} == scalar, 'displayed_boundary_character')
        check(mm(action, delta) == delta, 'literal_principal_fixed')
        check(mm(boundary, action) == sm(scalar, boundary), 'actual_boundary_covector_operator')
        record = {'index': index, 'label': label, 'boundary_character': scalar_text}
        if index == 0:
            image = mm(action, core_lift)
            defect = ms(image, sm(parse('r'), core_lift))
            check(sm(parse('r-1'), defect) == mm(delta, [image[0]]),
                  'actual_five_dimensional_scalar_core')
            record['core_scalar'] = 'r'
            record['principal_correction_numerator'] = serial([image[0]])
        records.append(record)
    result = {
        'status': 'PASS_FULL_PRODUCT_ONE_FIRST_SCALAR_LITERAL_WORD_AUDIT',
        'producer_sha256': sha256(script.read_bytes()).hexdigest(),
        'inputs': {str(p): sha256(p.read_bytes()).hexdigest()
                   for p in [arithmetic, candidate_path, producer, universal, word_path]},
        'coefficient_variables': names, 'character_exponents': characters,
        'principal_pivot_original_index': 1, 'quotient_original_indices': [2, 3, 4, 5, 6, 7],
        'source_records': records, 'checks': dict(globals_['CHECKS']),
        'check_total': sum(globals_['CHECKS'].values()),
        'independence': 'No producer or symbolic algebra package import. Exact original decorated Artin words are reconstructed by integer Laurent affine arithmetic. Both inverse bases and the original seven-coordinate scalar-core identity are checked with only r-1 cleared.',
        'scope': 'The exact product-one coefficient torus and retained X1 principal chart used in F30. Finite-field specialization requires r!=1 for this chart; the proof derives it from the proper scalar-field extension generated by r. No universal t-scalar identity is used.'
    }
    output = script.with_name('affine_product_one_first_scalar_field_independent_audit_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'check_total': result['check_total'],
                      'literal_source_words': 3, 'source_indices': list(expected),
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
