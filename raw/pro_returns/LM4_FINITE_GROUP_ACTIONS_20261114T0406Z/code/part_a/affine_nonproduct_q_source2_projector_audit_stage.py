"""Actual source2 eigenvalue rows in the orbit of the source-zero row q."""
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
    variables = sp.symbols(' '.join(names))

    def change(poly):
        answer = {}
        for coefficient, (a, b, c, d, e, f, g) in poly:
            answer = sparse['plus'](answer, {(a-b, b, c-b, d-b, e-b, f-b, g-b): coefficient})
        return answer

    def expression(poly):
        return sp.Add(*(a*sp.prod(x**n for x, n in zip(variables, e)) for e, a in poly.items()))

    q = pm([factor['row_q']])
    roots2 = ['r*t', 'r*t/(u*v)', 'r*t/(w*z)', '1/(r*t)']
    targets = [(2, [root for root in roots2 if root != special], special) for special in roots2]
    records = []
    projector_checks = 0
    for index, roots, special in targets:
        record = next(d for d in data['records'] if d['index'] == index)
        matrix = [[change(p) for p in row] for row in record['boundary_quotient_matrix_6']]
        row = q
        projector = sparse['eye'](6, parse('1'))
        for root in roots:
            shifted = sparse['shifted'](matrix, parse(root))
            row = sparse['mm'](row, shifted)
            projector = sparse['mm'](projector, shifted)
        assert sparse['mm'](row, matrix) == sparse['scale'](parse(special), row)
        minima = tuple(min(e[j] for p in row[0] for e in p) for j in range(7))
        polys = [sp.Poly(expression({tuple(e[j]-minima[j] for j in range(7)): a for e, a in p.items()}),
                         *variables, domain=sp.ZZ) for p in row[0]]
        nonzero = [p for p in polys if not p.is_zero]
        common = nonzero[0]
        for polynomial in nonzero[1:]:
            common = sp.gcd(common, polynomial)
        primitive = [str(sp.factor(p.exquo(common).as_expr())) for p in polys]
        common_expression = sp.prod(x**n for x, n in zip(variables, minima))*common.as_expr()
        common_poly = parse(str(sp.factor(common_expression)))
        primitive_row = pm([primitive])
        assert sparse['scale'](common_poly, primitive_row) == row
        assert sparse['mm'](primitive_row, matrix) == sparse['scale'](parse(special), primitive_row)
        if special != 'r*t':
            for operator_row in projector:
                for j in range(6):
                    for k in range(j+1, 6):
                        assert sparse['times'](operator_row[j], primitive_row[0][k]) == sparse['times'](operator_row[k], primitive_row[0][j])
                        projector_checks += 1
        item = {'index': index, 'label': record['label'], 'roots_removed': roots,
                'special_root': special, 'q_polynomial_orbit_factor': str(sp.factor(common_expression)),
                'primitive_row': primitive, 'raw_row_monomials': sum(len(p) for p in row[0]),
                'primitive_monomials': sum(len(p) for p in primitive_row[0])}
        records.append(item)
        print(json.dumps(item), flush=True)
    output = script.with_name('affine_nonproduct_q_source2_projector_audit_stage_output.json')
    result = {'status': 'PASS_EXACT_Q_SOURCE2_PROJECTOR_ROWS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, outer, helper, product]},
              'variables': names, 'records': records, 'projector_cross_product_checks': projector_checks,
              'scope': 'Exact actual polynomial-orbit rows, their integral factors and primitive direct eigenrows. Inverting a displayed factor in a field requires a separate nonzero-stratum proof.'}
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
