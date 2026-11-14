"""Exact exploratory original-word identities with retained principal pivots.

On the full product-one tuple, the r!=1 chart uses X1 and the r=1
proper-field chart uses X3. Integer Laurent calculations clear only
these exact pivots. No full marginal or affine-image claim is made.
"""
from hashlib import sha256
from pathlib import Path
import json
import runpy


def divide_axis_minus_one(poly, axis, ns):
    """Exact Laurent division by x_axis-1, proved by multiplication back."""
    fibres = {}
    for exponent, coefficient in poly.items():
        key = exponent[:axis]+exponent[axis+1:]
        fibre = fibres.setdefault(key, {})
        fibre[exponent[axis]] = coefficient
    result = {}
    for key, fibre in fibres.items():
        ns['check'](sum(fibre.values()) == 0, 'pivot_divisibility_fibre')
        running = 0
        for power in range(min(fibre), max(fibre)):
            running -= fibre.get(power, 0)
            if running:
                exponent = key[:axis]+(power,)+key[axis:]
                result[exponent] = running
    dimension = len(ns['parse'].__globals__['ZERO'])
    exponent = tuple(int(i == axis) for i in range(dimension))
    divisor = ns['add']({exponent: 1}, ns['negative'](ns['parse'].__globals__['ONE']))
    ns['check'](ns['mul'](result, divisor) == poly, 'exact_pivot_division_inverse')
    return result


def main():
    program = Path(__file__).resolve()
    folder = program.parent
    arithmetic = folder/'affine_four_parameter_extension_independent_audit.py'
    words_path = folder/'full_cross_source_stage/marginal_braids.json'
    ns = runpy.run_path(str(arithmetic))
    words = [x for x in json.loads(words_path.read_text())['records'] if x['index'] < 11]
    mm, ms, sm = [ns[x] for x in ['matrix_mul', 'matrix_sub', 'scalar_mul']]
    identity, pm, parse = [ns[x] for x in ['identity', 'parse_matrix', 'parse']]
    serial, check = ns['serial_matrix'], ns['check']
    namespace = parse.__globals__
    cases = [
        {'name': 'r_nontrivial_X1_pivot', 'names': ['r', 's', 't', 'u', 'v', 'w'],
         'characters': [[int(i == j) for i in range(6)] for j in range(6)] + [[-1]*6],
         'pivot': 0, 'pivot_axis': 0, 'keep': list(range(1, 7)), 'dimension': 5, 'indices': list(range(11)),
         'boundary': ['1', 'r', 'r*s', 'r*s*t', 'r*s*t*u', 'r*s*t*u*v', 'r*s*t*u*v*w'],
         'basis': [
             ['-s', '-s*t', '-s*t*u', '-s*t*u*v', '-s*t*u*v*w', '1/r'],
             ['1', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'],
             ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0'],
             ['0', '0', '0', '0', '1', '0']],
         'inverse': [
             ['0', '1', '0', '0', '0', '0'], ['0', '0', '1', '0', '0', '0'],
             ['0', '0', '0', '1', '0', '0'], ['0', '0', '0', '0', '1', '0'],
             ['0', '0', '0', '0', '0', '1'],
             ['r', 'r*s', 'r*s*t', 'r*s*t*u', 'r*s*t*u*v', 'r*s*t*u*v*w']],
         'scalar_indices': {0: 'r', 7: 't'}},
        {'name': 'r_equals_one_X3_pivot', 'names': ['s', 't', 'u', 'v', 'w'],
         'characters': [[0]*5] + [[int(i == j) for i in range(5)] for j in range(5)] + [[-1]*5],
         'pivot': 2, 'pivot_axis': 1, 'keep': [0, 1, 3, 4, 5, 6], 'dimension': 4, 'indices': list(range(11)),
         'boundary': ['1', '1', 's', 's*t', 's*t*u', 's*t*u*v', 's*t*u*v*w'],
         'basis': [
             ['0', '0', '0', '0', '0', '1'],
             ['-s*t', '-s*t*u', '-s*t*u*v', '-s*t*u*v*w', '1', '-1'],
             ['1', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'],
             ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0']],
         'inverse': [
             ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0'],
             ['0', '0', '0', '0', '1', '0'], ['0', '0', '0', '0', '0', '1'],
             ['1', '1', 's*t', 's*t*u', 's*t*u*v', 's*t*u*v*w'],
             ['1', '0', '0', '0', '0', '0']],
         'scalar_indices': {2: 't', 7: 't'}},
    ]
    outputs = []
    for case in cases:
        ns['configure'](case['names'], case['characters'])
        basis, inverse = pm(case['basis']), pm(case['inverse'])
        check(mm(basis, inverse) == identity(6), 'explicit_retained_basis_inverse')
        check(mm(inverse, basis) == identity(6), 'explicit_retained_inverse_basis')
        section = [[{} for _ in range(6)] for _ in range(7)]
        for j, i in enumerate(case['keep']):
            section[i][j] = namespace['ONE']
        lift = mm(section, basis)
        core_lift = [row[:case['dimension']] for row in lift]
        delta = [[ns['add']({tuple(e): 1}, ns['negative'](namespace['ONE']))]
                 for e in case['characters']]
        boundary = pm([case['boundary']])
        check(mm(boundary, delta) == [[{}]], 'boundary_annihilates_principals')
        records = []
        for index in case['indices']:
            word = words[index]
            check(word['index'] == index, 'actual_source_index')
            decoration, action = ns['literal_braid'](word['negative_braid'])
            check(mm(action, delta) == delta, 'actual_principal_fixed')
            boundary_scalar = {decoration[0]: 1}
            check(mm(boundary, action) == sm(boundary_scalar, boundary),
                  'actual_boundary_quotient')
            image_all = mm(action, lift)
            numerator = [[ns['add'](ns['mul'](delta[case['pivot']][0], image_all[i][j]),
                         ns['negative'](ns['mul'](delta[i][0], image_all[case['pivot']][j])))
                         for j in range(6)] for i in case['keep']]
            quotient_image = [[divide_axis_minus_one(p, case['pivot_axis'], ns) for p in row]
                              for row in numerator]
            block = mm(inverse, quotient_image)
            check(all(not block[i][j] for i in range(case['dimension'], 6)
                      for j in range(6) if i != j), 'exact_diagonal_quotient_block')
            item = {'index': index, 'label': word['label'],
                    'boundary_scalar': ns['serialize'](boundary_scalar),
                    'action_7': serial(action), 'block_matrix_6': serial(block),
                    'core_matrix': serial([row[:case['dimension']] for row in block[:case['dimension']]])}
            if index in case['scalar_indices']:
                scalar = parse(case['scalar_indices'][index])
                image = mm(action, core_lift)
                defect = ms(image, sm(scalar, core_lift))
                exact = sm(delta[case['pivot']][0], defect) == mm(delta, [image[case['pivot']]])
                item['tested_core_scalar'] = case['scalar_indices'][index]
                item['scalar_core_identity_holds'] = exact
                if not exact:
                    item['cleared_scalar_core_defect'] = serial(ms(
                        sm(delta[case['pivot']][0], defect),
                        mm(delta, [image[case['pivot']]])))
            if case['name'] == 'r_equals_one_X3_pivot':
                check(all(not x for x in action[0][1:]), 'actual_X1_scalar_quotient')
                item['X1_scalar'] = ns['serialize'](action[0][0])
            records.append(item)
        outputs.append({'name': case['name'], 'variables': case['names'],
                        'character_exponents': case['characters'],
                        'principal_pivot_original_index': case['pivot']+1,
                        'quotient_original_indices': [i+1 for i in case['keep']],
                        'basis': case['basis'], 'inverse_basis': case['inverse'],
                        'core_dimension': case['dimension'], 'source_records': records})
    result = {
        'status': 'EXACT_EXPLORATORY_FULL_PRODUCT_ONE_RETAINED_PIVOT_SOURCE_DATA',
        'producer_sha256': sha256(program.read_bytes()).hexdigest(),
        'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [arithmetic, words_path]},
        'charts': outputs, 'checks': dict(namespace['CHECKS']),
        'check_total': sum(namespace['CHECKS'].values()),
        'scope': 'Original-word boundary/X1 quotient identities and explicit tests of scalar-core identities on two retained-generator principal charts. Every failed scalar test retains its exact nonzero integral defect; no scalar-core conclusion is asserted for those cases. General field separation and affine-image consequences remain to be proved separately.'
    }
    output = program.with_name('affine_product_one_retained_pivots_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': result['check_total'],
                      'tables': [{'name': c['name'], 'records': [
                          {k: v for k, v in item.items() if k not in
                           ['action_7', 'block_matrix_6', 'core_matrix', 'cleared_scalar_core_defect']}
                          for item in c['source_records']]} for c in outputs],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
