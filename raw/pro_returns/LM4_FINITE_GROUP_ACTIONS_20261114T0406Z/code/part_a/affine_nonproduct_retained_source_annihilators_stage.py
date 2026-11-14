"""Exact original-source polynomial identities for sources 2 and 7.

Indices are zero based; the matrices come from the frozen literal-word
boundary quotient. This verifies identities over the integer Laurent ring.
"""
from hashlib import sha256
from pathlib import Path
import json
import runpy


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    product = folder/'affine_full_product_one_independent_audit.py'
    old, sparse = runpy.run_path(str(helper)), runpy.run_path(str(product))
    data = json.loads(source.read_text())
    names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
    characters = [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(7)] for j in range(2, 7)]
    old['configure'](names, characters)
    parse = old['parse']

    def change(poly):
        answer = {}
        for coefficient, (a, b, c, d, e, f, g) in poly:
            answer = sparse['plus'](answer, {(a-b, b, c-b, d-b, e-b, f-b, g-b): coefficient})
        return answer

    records = []
    for index, roots in [(2, ['r*t', 'r*t/(u*v)', 'r*t/(w*z)', '1/(r*t)']),
                         (7, ['t/h', 't/(h*u*v)', 't/(h*w*z)', 'h/t'])]:
        record = next(d for d in data['records'] if d['index'] == index)
        matrix = [[change(p) for p in row] for row in record['boundary_quotient_matrix_6']]
        operator = sparse['eye'](6, parse('1'))
        counts = []
        for root in roots:
            operator = sparse['mm'](operator, sparse['shifted'](matrix, parse(root)))
            counts.append(sum(len(p) for row in operator for p in row))
            print(json.dumps({'source': index, 'factor_root': root, 'operator_monomial_count': counts[-1]}), flush=True)
        assert all(not p for row in operator for p in row), ('annihilator', index)
        trace = {}
        for j in range(6):
            trace = sparse['plus'](trace, matrix[j][j])
        expected = sparse['plus'](sparse['times'](parse('3'), parse(roots[0])),
                                  sparse['plus'](parse(roots[1]), sparse['plus'](parse(roots[2]), parse(roots[3]))))
        assert trace == expected, ('trace', index)
        records.append({'index': index, 'label': record['label'], 'roots': roots,
                        'ordered_product_monomial_counts': counts,
                        'annihilator_zero': True, 'trace_multiplicities': [3, 1, 1, 1],
                        'trace_verified': True})
    result = {'status': 'PASS_EXACT_RETAINED_SOURCE_ANNIHILATORS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, helper, product]},
              'variables': names, 'characters': characters, 'records': records,
              'scope': 'Integral Laurent annihilator identities and traces of the actual six-dimensional source2/source7 actions; source indices are zero based. No invariant-line classification is assumed.'}
    output = script.with_name('affine_nonproduct_retained_source_annihilators_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
