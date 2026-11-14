"""Exact exploratory moving-root rows of the full nonproduct H1 module.

The original seven-coordinate character is retained through
(r,s,t,u,v,w,z)=(r,h/(r*t*u*v*w*z),t,u,v,w,z).
The matrices are the previously word-checked boundary quotient.
No separation or all-field rank conclusion is asserted here.
"""
from hashlib import sha256
from pathlib import Path
import json
import runpy
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    products = folder/'affine_full_product_one_independent_audit.py'
    data = json.loads(source.read_text())
    arithmetic, sparse = runpy.run_path(str(helper)), runpy.run_path(str(products))
    names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
    characters = [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(7)] for j in range(2, 7)]
    arithmetic['configure'](names, characters)
    parse, pm = arithmetic['parse'], arithmetic['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    add, neg, mul, mm, shifted = [sparse[k] for k in ['plus', 'neg', 'times', 'mm', 'shifted']]
    variables = sp.symbols(' '.join(names))

    def change(poly):
        answer = {}
        for coefficient, (a, b, c, d, e, f, g) in poly:
            answer = add(answer, {(a-b, b, c-b, d-b, e-b, f-b, g-b): coefficient})
        return answer

    def expression(poly):
        return sp.Add(*(coefficient*sp.prod(x**n for x, n in zip(variables, exponent))
                        for exponent, coefficient in poly.items()))

    targets = [
        (1, ['1', '1/(r*u)**2', '1/(v*w)'], '1/(t*z)'),
        (3, ['1', '1/(r*v)**2', '1/(u*z)'], '1/(t*w)'),
        (4, ['1', '1/(r*w)**2', '1/(v*z)'], '1/(t*u)'),
        (5, ['1', '1/(r*z)**2', '1/(u*w)'], '1/(t*v)'),
        (6, ['1', '(h/u)**2', '1/(v*w)'], '1/(t*z)'),
        (8, ['1', '(h/v)**2', '1/(u*z)'], '1/(t*w)'),
        (9, ['1', '(h/w)**2', '1/(v*z)'], '1/(t*u)'),
        (10, ['1', '(h/z)**2', '1/(u*w)'], '1/(t*v)')]
    records = []
    for index, bases, moving in targets:
        old = next(record for record in data['records'] if record['index'] == index)
        matrix = [[change(p) for p in row] for row in old['boundary_quotient_matrix_6']]
        operator = sparse['eye'](6, parse('1'))
        tau = parse('1')
        for base in bases:
            operator = mm(operator, shifted(matrix, parse(base)))
            tau = mul(tau, add(parse(moving), neg(parse(base))))
        check = mm(operator, shifted(matrix, parse(moving)))
        assert all(not entry for row in check for entry in row), ('annihilator', index)
        trace = {}
        for j in range(6):
            trace = add(trace, operator[j][j])
        assert trace == tau, ('trace', index)
        selected = min((i for i, row in enumerate(operator) if any(row)),
                       key=lambda i: sum(len(p) for p in operator[i]))
        chosen = operator[selected]
        minima = tuple(min(e[j] for p in chosen for e in p) for j in range(7))
        polys = [sp.Poly(expression({tuple(e[j]-minima[j] for j in range(7)): a
                                    for e, a in p.items()}), *variables, domain=sp.ZZ)
                 for p in chosen]
        nonzero = [p for p in polys if not p.is_zero]
        common = nonzero[0]
        for poly in nonzero[1:]:
            common = sp.gcd(common, poly)
        q = [sp.factor(poly.exquo(common).as_expr()) for poly in polys]
        row = pm([[str(entry) for entry in q]])
        assert mm(row, matrix) == sparse['scale'](parse(moving), row), ('direct_left_eigenrow', index)
        assert mm(row, operator) == sparse['scale'](tau, row), ('polynomial_row_evaluation', index)
        item = {'index': index, 'label': old['label'], 'base_roots': bases,
                'moving_root': moving, 'annihilator_verified': True,
                'selected_operator_row_zero_based': selected,
                'row_q': [str(entry) for entry in q],
                'trace_product': str(sp.factor(expression(tau))),
                'direct_left_eigenrow_verified': True,
                'row_monomial_count': sum(map(len, row[0]))}
        records.append(item)
        print(json.dumps(item), flush=True)
    result = {'status': 'EXACT_FULL_NONPRODUCT_MOVING_EIGENROWS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest()
                         for path in [source, helper, products]},
              'variables': names, 'characters': characters, 'records': records,
              'scope': 'Eight exact full six-dimensional original-source moving-root annihilators, traces, left eigenrows and polynomial row evaluations. No all-field row rank, invariant-submodule classification or new affine-image conclusion is asserted.'}
    output = script.with_name('affine_nonproduct_general_moving_rows_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
