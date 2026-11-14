"""Actual special-root polynomial images of the source-zero column.

The negative-source special roots are (h/c)^2. Their other three
roots are 1 and the displayed peripheral/moving roots. Only exact
polynomial identities are recorded here.
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
    variables = sp.symbols(' '.join(names))

    def change(poly):
        answer = {}
        for coefficient, (a, b, c, d, e, f, g) in poly:
            answer = sparse['plus'](answer, {(a-b, b, c-b, d-b, e-b, f-b, g-b): coefficient})
        return answer

    def expression(poly):
        return sp.Add(*(a*sp.prod(x**n for x, n in zip(variables, e)) for e, a in poly.items()))

    def packed(poly):
        return [[a, list(e)] for e, a in sorted(poly.items())]

    a = pm([[x] for x in factor['column_a']])
    targets = [(10, ['1', '1/(u*w)', '1/(t*v)'], '(h/z)**2'),
               (9, ['1', '1/(v*z)', '1/(t*u)'], '(h/w)**2'),
               (8, ['1', '1/(u*z)', '1/(t*w)'], '(h/v)**2'),
               (6, ['1', '1/(v*w)', '1/(t*z)'], '(h/u)**2')]
    records = []
    for index, roots, special in targets:
        record = next(d for d in data['records'] if d['index'] == index)
        matrix = [[change(p) for p in row] for row in record['boundary_quotient_matrix_6']]
        image = a
        counts = []
        for root in roots:
            image = sparse['mm'](sparse['shifted'](matrix, parse(root)), image)
            counts.append(sum(len(p[0]) for p in image))
            print(json.dumps({'index': index, 'root_removed': root, 'monomials': counts[-1]}), flush=True)
        assert sparse['mm'](matrix, image) == sparse['scale'](parse(special), image), ('special_root', index)
        factored = [str(sp.factor(expression(p[0]))) for p in image]
        records.append({'index': index, 'label': record['label'], 'base_roots': roots,
                        'special_root': special, 'ordered_image_monomial_counts': counts,
                        'image': [packed(p[0]) for p in image], 'image_factored': factored,
                        'special_eigenvector_identity': True})
        print(json.dumps({'index': index, 'factored_lengths': [len(p) for p in factored]}), flush=True)
    result = {'status': 'PASS_EXACT_RANK_ONE_SPECIAL_ROOT_IMAGES',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, outer, helper, product]},
              'variables': names, 'characters': characters, 'records': records,
              'scope': 'Exact polynomial images of the actual source-zero column, with all actual source matrices retained; no nonvanishing or affine-image conclusion is assumed.'}
    output = script.with_name('affine_nonproduct_rank_one_special_roots_stage_output.json')
    output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
