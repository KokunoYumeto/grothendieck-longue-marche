"""Exact compact row coordinates and determinant cover for the r=1 chart.

This producer applies the specified Laurent-ring isomorphism
s=h/(t*u*v*w*z).  It preserves all eight original moving eigenrows,
with q=hat(q)*diag(1,t-1,t-1,t-1,t-1), and computes the four
determinants used by the field proof.  No finite-field sampling occurs.
"""
from hashlib import sha256
from pathlib import Path
import json
import runpy


def compact_rows():
    return {
        1: ['-h*(z-1)/(u*v*w*z)', '-h*(z-1)/(u*v*w*z)',
            '-h*(z-1)/(v*w*z)', '-h*(z-1)/(w*z)', '-(h*z-h-z)/z'],
        3: ['-h*(w-1)/(u*w*z)', '-(h+u*w*z)*(w-1)/(u*w*z)', '0',
            'h*(u*w-w+1)/(w*z)', 'h*(u-1)*(w-1)/z'],
        4: ['h**2*(u-1)/(u**2*w*z)',
            'h**2*(u-1)/(u**2*w*z)+h*v*(u-1)/u-v',
            '-h*(u-1)*(h*(u-1)-u)/(u*w*z)',
            '-h*(u-1)*(h*((u-1)*v+u*(z-1))-u*(v+z-1))/(u*w*z)',
            '-(u-1)*(h**2*(u*(v*w+w*z-w-z)-v*w)+h*u*(-v*w-2*w*z+w+z)+u*w*z)/(u*w*z)'],
        5: ['h*(v-1)/(u*w*z)', 'h*(v-1)/(u*w*z)',
            '-h*(h*z+(v-1)*(z-1))/(w*z)',
            '-(v-1)*(h**2*z+h*v*(z-1)+h*(w-1)*z-w*z)/(w*z)',
            '-(v-1)*(h**2*z+h*v*(z-1)+h*(w-2)*z-(v+w-1)*z)/z'],
        6: ['h**2*(z-1)/(u**2*w*z**2)',
            'h*(h+u*v*w*z)*(z-1)/(u**2*w*z**2)',
            '-h**2*(u-1)*(z-1)/(u*w*z**2)',
            '-h*(z-1)*(h*(u*(v+z-1)-v)-u*z)/(u*w*z**2)',
            '-((z-1)*(h**2*(v*w*(u-1)+u*w*(z-1)-u*z)+h*u*z*(1-2*w))+u*w*z**2)/(u*w*z**2)'],
        8: ['-h*(w-1)/(u*v*w)', '-h*(w-1)/(u*v*w)',
            '-h*(w-1)/(v*w)', '-(h*w-h-w)/w', '-(h-1)*(w-1)'],
        9: ['h*(u-1)/(u*v*w*z)', 'h*(u-1)/(u*v*w*z)-1',
            'h*(u-1)/(v*w*z)', 'h*(u-1)/(w*z)', 'h*(u-1)/z'],
        10: ['1-v', '1-v', 'u', '0', '0']}


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_r1_moving_rows_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    products = folder/'affine_full_product_one_independent_audit.py'
    data = json.loads(source.read_text())
    arithmetic, sparse = runpy.run_path(str(helper)), runpy.run_path(str(products))
    characters = [[0]*6, [1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(6)] for j in range(1, 6)]
    arithmetic['configure'](['h', 't', 'u', 'v', 'w', 'z'], characters)
    parse, pm = arithmetic['parse'], arithmetic['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(t*u*v*w*z)')
    one, zero = parse('1'), {}
    diagonal = [[(one if i == 0 else parse('t-1')) if i == j else zero
                 for j in range(5)] for i in range(5)]
    row_texts = compact_rows()
    rows = {}
    for record in data['records']:
        index = record['index']
        row = pm([row_texts[index]])
        actual = sparse['mm'](row, diagonal)
        assert actual == pm([record['row_q']]), ('exact_column_scaling', index)
        rows[index] = row[0]
    expected = {
        3: 'h*u*(h-1)*(w-1)/(w*z)',
        4: '-h*(h-1)*(u-1)*(h*w-h-w)/w**2',
        5: '-h*(h-1)*(v-1)',
        6: '-h*(h-1)*(z-1)*(h*w-h-w)/(w**2*z)'}
    determinants = []
    for index, formula in expected.items():
        selected = [rows[i] for i in [1, 8, 9, 10, index]]
        value = sparse['determinant'](selected, one)
        assert value == parse(formula), ('compact_row_determinant', index)
        actual = sparse['mm'](selected, diagonal)
        assert sparse['determinant'](actual, one) == sparse['times'](parse('(t-1)**4'), value)
        determinants.append({'source_indices_zero_based': [1, 8, 9, 10, index],
                             'compact_determinant': formula,
                             'actual_determinant': '(t-1)**4*('+formula+')'})
    result = {'status': 'EXACT_R1_NONPRODUCT_DETERMINANT_COVER',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest()
                         for path in [source, helper, products]},
              'variables': ['h', 't', 'u', 'v', 'w', 'z'], 'characters': characters,
              'coefficient_map': {'s': 'h/(t*u*v*w*z)', 't': 't', 'u': 'u',
                                  'v': 'v', 'w': 'w', 'z': 'z'},
              'inverse_coefficient_map': {'h': 's*t*u*v*w*z', 't': 't', 'u': 'u',
                                          'v': 'v', 'w': 'w', 'z': 'z'},
              'column_scaling': ['1', 't-1', 't-1', 't-1', 't-1'],
              'compact_rows': {str(i): row for i, row in row_texts.items()},
              'determinants': determinants,
              'scope': 'Exact compact eigenrow coordinates and four determinant identities. The proof supplies the nonzero-factor argument over every finite field and the actual source-module/affine consequence.'}
    output = script.with_name('affine_nonproduct_r1_determinants_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'determinants': determinants,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
