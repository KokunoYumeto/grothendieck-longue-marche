"""Exact exploratory traces of the actual source-zero rank-one operator."""
from hashlib import sha256
from pathlib import Path
import json
import runpy
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    matrix_path = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    factor_path = folder/'affine_nonproduct_source_zero_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    products = folder/'affine_full_product_one_independent_audit.py'
    matrices, factors = json.loads(matrix_path.read_text()), json.loads(factor_path.read_text())
    arithmetic, sparse = runpy.run_path(str(helper)), runpy.run_path(str(products))
    names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
    arithmetic['configure'](names, [[int(i == j) for i in range(7)] for j in range(7)])
    parse, pm = arithmetic['parse'], arithmetic['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    q, column = pm([factors['row_q']]), pm([[a] for a in factors['column_a']])
    mm, add = sparse['mm'], sparse['plus']
    rank_one = mm(column, q)

    def change(poly):
        out = {}
        for coefficient, (a, b, c, d, e, f, g) in poly:
            out = add(out, {(a-b, b, c-b, d-b, e-b, f-b, g-b): coefficient})
        return out

    variables = sp.symbols(' '.join(names))

    def expression(poly):
        return sp.Add(*(a*sp.prod(x**n for x, n in zip(variables, e)) for e, a in poly.items()))

    records = []
    for record in matrices['records']:
        matrix = [[change(p) for p in row] for row in record['boundary_quotient_matrix_6']]
        scalar = mm(mm(q, matrix), column)[0][0]
        product = mm(rank_one, matrix)
        trace = {}
        for i in range(6):
            trace = add(trace, product[i][i])
        assert scalar == trace
        factored = str(sp.factor(expression(scalar))) if len(scalar) <= 120 else None
        if factored is not None:
            assert parse(factored) == scalar
        item = {'index': record['index'], 'label': record['label'],
                'trace_of_source_zero_rank_one_times_source': factored,
                'exact_laurent_coefficients': arithmetic['serialize'](scalar),
                'monomial_count': len(scalar)}
        records.append(item)
        print(json.dumps({key: value for key, value in item.items()
                          if key != 'exact_laurent_coefficients'}), flush=True)
    result = {'status': 'EXACT_GENERAL_SOURCE_ZERO_RANK_ONE_TRACE_PAIRINGS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest()
                         for path in [matrix_path, factor_path, helper, products]},
              'rank_one_definition': 'T0-(r/h)*I6=a*q', 'scalar_definition': 'q*T_l*a=trace((T0-(r/h)I6)*T_l)',
              'variables': names, 'coefficient_map': 's=h/(r*t*u*v*w*z)',
              'records': records,
              'scope': 'Exact original-source rank-one trace pairings in the actual boundary quotient. No completeness, irreducibility, character separation or new affine-image statement is asserted.'}
    output = script.with_name('affine_nonproduct_general_rank_one_pairings_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
