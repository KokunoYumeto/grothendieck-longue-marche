"""Exact positive special-root rank-one traces and their sign-odd parts."""
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
    old['configure'](names, [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(7)] for j in range(2, 7)])
    parse, pm = old['parse'], old['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    r, h, t, u, v, w, z = variables = sp.symbols(' '.join(names))

    def change(poly):
        answer = {}
        for coefficient, (aa, bb, cc, dd, ee, ff, gg) in poly:
            answer = sparse['plus'](answer, {(aa-bb, bb, cc-bb, dd-bb, ee-bb, ff-bb, gg-bb): coefficient})
        return answer

    def expression(poly):
        return sp.Add(*(aa*sp.prod(x**nn for x, nn in zip(variables, ee)) for ee, aa in poly.items()))

    def packed(poly):
        return [[aa, list(ee)] for ee, aa in sorted(poly.items())]

    a = pm([[x] for x in factor['column_a']])
    q = pm([factor['row_q']])
    ae = [sp.factor(expression(p[0])) for p in a]
    assert sp.cancel(ae[5]-(z-1)*(h+w-1)/(h*u*z)) == 0
    assert sp.cancel(ae[4]+(w-1)*(h*(h+w-1)*(z-1)-w*z)/(h**2*u*z)) == 0
    assert sp.cancel(ae[4].subs(z, 1)-w*(w-1)/(h**2*u)) == 0
    assert sp.cancel(ae[3].subs({z: 1, w: 1})-(v-1)/(h**2*u)) == 0
    assert sp.cancel(ae[2].subs({z: 1, w: 1, v: 1})-(u-1)/u) == 0
    targets = [(1, ['1', '1/(v*w)', '1/(t*z)'], '1/(r*u)**2'),
               (4, ['1', '1/(v*z)', '1/(t*u)'], '1/(r*w)**2'),
               (3, ['1', '1/(u*z)', '1/(t*w)'], '1/(r*v)**2'),
               (5, ['1', '1/(u*w)', '1/(t*v)'], '1/(r*z)**2')]
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
        assert sparse['mm'](matrix, image) == sparse['scale'](parse(special), image)
        trace = sparse['mm'](q, image)[0][0]
        odd = {ee: aa for ee, aa in trace.items() if (ee[0]+ee[1]) % 2}
        conjugate = {ee: (-aa if (ee[0]+ee[1]) % 2 else aa) for ee, aa in trace.items()}
        assert sparse['plus'](trace, sparse['neg'](conjugate)) == sparse['times'](parse('2'), odd)
        item = {'index': index, 'label': record['label'], 'roots_of_P': roots,
                'special_root': special, 'image_monomial_counts': counts,
                'trace': packed(trace), 'odd_part': packed(odd),
                'trace_factored': str(sp.factor(expression(trace))),
                'odd_part_factored': str(sp.factor(expression(odd)))}
        records.append(item)
        print(json.dumps({'index': index, 'trace_monomials': len(trace), 'odd_monomials': len(odd),
                          'odd_part_factored': item['odd_part_factored']}), flush=True)
    output = script.with_name('affine_nonproduct_positive_special_trace_stage_output.json')
    result = {'status': 'PASS_EXACT_POSITIVE_SPECIAL_TRACE_SIGN_PARTS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, outer, helper, product]},
              'variables': names, 'outer_column_nonzero_cover_identities_checked': 5,
              'outer_column_deleted_entries': [str(x) for x in ae[2:]], 'records': records,
              'scope': 'Exact positive special-root projector trace and sign-parity identities, plus five direct identities for the nonzero-column cover. The all-field sign comparison remains a separate proof task.'}
    output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
