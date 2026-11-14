"""Exact exploratory moving-root rows in the full five-dimensional core."""
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json
import runpy
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_product_one_retained_pivots_stage_output.json'
    arithmetic = folder/'affine_four_parameter_extension_independent_audit.py'
    products = folder/'affine_product_one_r1_moving_rows_stage.py'
    data = json.loads(source.read_text())['charts'][0]
    sparse = runpy.run_path(str(products))
    add, mul, mm, shifted = [sparse[k] for k in ['add', 'mul', 'mm', 'shifted']]
    ns = runpy.run_path(str(arithmetic))
    ns['configure'](['r', 's', 't', 'u', 'v', 'w'], data['character_exponents'])
    parse = ns['parse']
    variables = sp.symbols('r s t u v w')

    def expr(poly):
        return sp.Add(*(a*sp.prod(x**e for x, e in zip(variables, exponent))
                        for exponent, a in poly.items()))

    targets = [
        (6, ['1', '1/(v*w)'], 'r*s*u*v*w'),
        (8, ['1', 'r*s*t*v*w'], '1/(t*w)'),
        (9, ['1', 'r*s*t*u*w'], '1/(t*u)'),
        (10, ['1', '1/(u*w)'], '1/(t*v)'),
        (1, ['1', '1/(v*w)', '1/(r**2*u**2)'], 'r*s*u*v*w'),
        (3, ['1', 'r*s*t*v*w', '1/(r**2*v**2)'], '1/(t*w)'),
        (4, ['1', 'r*s*t*u*w', '1/(r**2*w**2)'], '1/(t*u)'),
        (5, ['1', '1/(u*w)', 's**2*t**2*u**2*v**2*w**2'], '1/(t*v)'),
    ]
    results, primitive_rows = [], []
    for index, base_texts, moving_text in targets:
        record = next(x for x in data['source_records'] if x['index'] == index)
        matrix = [[{tuple(e): a for a, e in p} for p in row] for row in record['core_matrix']]
        factors = [shifted(matrix, parse(text)) for text in base_texts]
        operator = factors[0]
        for factor in factors[1:]:
            operator = mm(operator, factor)
        moving = parse(moving_text)
        annihilator = mm(operator, shifted(matrix, moving))
        assert all(not p for row in annihilator for p in row), index
        trace = {}
        for i in range(5):
            trace = add(trace, operator[i][i])
        expected = parse('1')
        for text in base_texts:
            expected = mul(expected, add(moving, {e: -a for e, a in parse(text).items()}))
        assert trace == expected, ('trace', index)
        smallest = min((i for i, row in enumerate(operator) if any(row)),
                       key=lambda i: sum(len(p) for p in operator[i]))
        chosen = operator[smallest]
        minima = tuple(min(e[j] for p in chosen for e in p) for j in range(6))
        shifted_rows = [{tuple(e[j]-minima[j] for j in range(6)): a
                         for e, a in p.items()} for p in chosen]
        polynomials = [sp.Poly(expr(p), *variables, domain=sp.ZZ) for p in shifted_rows]
        nonzero = [p for p in polynomials if not p.is_zero]
        common_poly = nonzero[0]
        for polynomial in nonzero[1:]:
            common_poly = sp.gcd(common_poly, polynomial)
        common = sp.factor(sp.prod(x**e for x, e in zip(variables, minima))*common_poly.as_expr())
        primitive = [sp.factor(p.exquo(common_poly).as_expr()) for p in polynomials]
        first = next(i for i, x in enumerate(primitive) if x != 0)
        column = [sp.factor(sp.cancel(expr(row[first])/primitive[first])) for row in operator]
        assert all(sp.cancel(expr(operator[i][j])-column[i]*primitive[j]) == 0
                   for i in range(5) for j in range(5)), ('outer_factorization', index)
        primitive_rows.append(primitive)
        result = {'index': index, 'label': record['label'],
                  'base_roots': base_texts, 'moving_root': moving_text,
                  'annihilator_zero': True, 'trace': str(sp.factor(expr(trace))),
                  'selected_row_index': smallest, 'selected_row_factor': str(common),
                  'column_factor': [str(x) for x in column],
                  'primitive_row': [str(x) for x in primitive]}
        results.append(result)
        print(json.dumps(result), flush=True)
    determinants = {}
    for row_index in range(4, 8):
        selected = primitive_rows[:4]+[primitive_rows[row_index]]
        determinant = 0
        for permutation in permutations(range(5)):
            factors = [selected[i][permutation[i]] for i in range(5)]
            if any(x == 0 for x in factors):
                continue
            inversions = sum(permutation[i] > permutation[j] for i in range(5) for j in range(i+1, 5))
            determinant += (-1)**inversions*sp.prod(factors)
        determinants[str(targets[row_index][0])] = str(sp.factor(sp.expand(determinant)))
    result = {'status': 'EXACT_GENERIC_MOVING_ROOT_OPERATORS_AND_ROW_FACTORIZATION',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, arithmetic, products]},
              'variables': [str(x) for x in variables], 'records': results,
              'row_determinants_by_positive_source': determinants,
              'scope': 'Exact integer Laurent annihilators/traces and exact symbolic rank-one factorizations for eight selected original source operators, with four explicit square row determinants. All finite-field consequences and exceptional factors require separate proof and independent audit.'}
    output = script.with_name('affine_product_one_generic_moving_rows_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'determinants': determinants,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
