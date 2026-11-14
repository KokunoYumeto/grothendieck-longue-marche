"""Exact exploratory images of the actual source-zero rank-one column.

The basis and the original decorated source words are retained through the
frozen nonproduct boundary quotient. No invariant-line conclusion is presumed.
"""
from pathlib import Path
from hashlib import sha256
import json
import runpy
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    outer = folder/'affine_nonproduct_source_zero_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    product = folder/'affine_full_product_one_independent_audit.py'
    data, factor = json.loads(source.read_text()), json.loads(outer.read_text())
    old, sparse = runpy.run_path(str(helper)), runpy.run_path(str(product))
    names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
    characters = [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(7)] for j in range(2, 7)]
    old['configure'](names, characters)
    parse, pm = old['parse'], old['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    plus, neg, times, mm, scale = [sparse[k] for k in ['plus', 'neg', 'times', 'mm', 'scale']]
    variables = sp.symbols(' '.join(names))

    def change(poly):
        answer = {}
        for coefficient, (a, b, c, d, e, f, g) in poly:
            answer = plus(answer, {(a-b, b, c-b, d-b, e-b, f-b, g-b): coefficient})
        return answer

    def expression(poly):
        return sp.Add(*(a*sp.prod(x**n for x, n in zip(variables, e)) for e, a in poly.items()))

    def packed(poly):
        return [[a, list(e)] for e, a in sorted(poly.items())]

    q = pm([factor['row_q']])
    a = pm([[x] for x in factor['column_a']])
    assert mm(q, a) == pm([['1-r/h']])
    records = []
    for index, displayed_scalar in [(2, 'r*t'), (7, 't/h')]:
        record = next(d for d in data['records'] if d['index'] == index)
        matrix = [[change(p) for p in row] for row in record['boundary_quotient_matrix_6']]
        image = mm(matrix, a)
        residual = sparse['minus'](image, scale(parse(displayed_scalar), a))
        wedges = {}
        for i in range(6):
            for j in range(i+1, 6):
                wedges[f'{i},{j}'] = plus(times(image[i][0], a[j][0]), neg(times(image[j][0], a[i][0])))
        out = {'index': index, 'label': record['label'], 'displayed_scalar': displayed_scalar,
               'image': [packed(p[0]) for p in image],
               'residual': [packed(p[0]) for p in residual],
               'residual_factored': [str(sp.factor(expression(p[0]))) for p in residual],
               'wedge_counts': {key: len(poly) for key, poly in wedges.items()},
               'wedges': {key: packed(poly) for key, poly in wedges.items()}}
        records.append(out)
        print(json.dumps({'index': index, 'residual_counts': [len(p[0]) for p in residual],
                          'residual_factored': out['residual_factored'],
                          'wedge_counts': out['wedge_counts']}), flush=True)
    result = {'status': 'EXACT_SOURCE_ZERO_LINE_IMAGES_EXPLORATORY',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, outer, helper, product]},
              'variables': names, 'characters': characters,
              'rank_one_column': [packed(p[0]) for p in a],
              'records': records,
              'scope': 'Exact actual T2 and T7 images and all proportionality minors of the source-zero eigenvalue-one column. No all-field invariant-line classification or new affine-image conclusion is asserted.'}
    output = script.with_name('affine_nonproduct_source_zero_line_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
