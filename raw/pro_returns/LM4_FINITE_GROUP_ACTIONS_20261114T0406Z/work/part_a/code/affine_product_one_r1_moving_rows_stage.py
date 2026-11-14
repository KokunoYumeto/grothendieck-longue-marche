"""Exact exploratory moving-root operators on the full r=1 product-one core.

All matrix products are expanded over integer Laurent coefficients before
the optional symbolic row factorization. No finite affine claim is made.
"""
from hashlib import sha256
from pathlib import Path
import json
import runpy
import sympy as sp


def add(left, right):
    out = dict(left)
    for exponent, coefficient in right.items():
        value = out.get(exponent, 0)+coefficient
        if value:
            out[exponent] = value
        else:
            out.pop(exponent, None)
    return out


def mul(left, right):
    out = {}
    for e, a in left.items():
        for f, b in right.items():
            exponent = tuple(x+y for x, y in zip(e, f))
            out[exponent] = out.get(exponent, 0)+a*b
    return {e: a for e, a in out.items() if a}


def mm(left, right):
    out = [[{} for _ in right[0]] for _ in left]
    for i, row in enumerate(left):
        for k, poly in enumerate(row):
            if poly:
                for j, other in enumerate(right[k]):
                    if other:
                        out[i][j] = add(out[i][j], mul(poly, other))
    return out


def shifted(matrix, scalar):
    out = [[dict(p) for p in row] for row in matrix]
    for i in range(len(out)):
        out[i][i] = add(out[i][i], {e: -a for e, a in scalar.items()})
    return out


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_product_one_retained_pivots_stage_output.json'
    arithmetic = folder/'affine_four_parameter_extension_independent_audit.py'
    data = json.loads(source.read_text())['charts'][1]
    ns = runpy.run_path(str(arithmetic))
    ns['configure'](['s', 't', 'u', 'v', 'w'], data['character_exponents'])
    parse = ns['parse']
    variables = sp.symbols('s t u v w')
    s, t, u, v, w = variables

    def expr(poly):
        return sp.Add(*(a*sp.prod(x**e for x, e in zip(variables, exponent))
                        for exponent, a in poly.items()))

    def factor(poly):
        return sp.factor(expr(poly))

    targets = {6: ('1/(v*w)', 's*u*v*w'),
               8: ('s*t*v*w', '1/(t*w)'),
               9: ('s*t*u*w', '1/(t*u)'),
               10: ('1/(u*w)', '1/(t*v)')}
    results, primitive_rows = [], []
    for index, (base_text, moving_text) in targets.items():
        record = next(r for r in data['source_records'] if r['index'] == index)
        matrix = [[{tuple(e): a for a, e in p} for p in row] for row in record['core_matrix']]
        base, moving = parse(base_text), parse(moving_text)
        operator = mm(shifted(matrix, parse('1')), shifted(matrix, base))
        annihilator = mm(operator, shifted(matrix, moving))
        assert all(not p for row in annihilator for p in row), index
        trace = {}
        for j in range(4):
            trace = add(trace, operator[j][j])
        expected = mul(add(moving, {e: -a for e, a in parse('1').items()}),
                       add(moving, {e: -a for e, a in base.items()}))
        assert trace == expected, ('trace', index)
        smallest = min((i for i, row in enumerate(operator) if any(row)),
                       key=lambda i: sum(len(p) for p in operator[i]))
        chosen = operator[smallest]
        minima = tuple(min(e[j] for p in chosen for e in p) for j in range(5))
        shifted_rows = [{tuple(e[j]-minima[j] for j in range(5)): a
                         for e, a in p.items()} for p in chosen]
        polynomials = [sp.Poly(expr(p), *variables, domain=sp.ZZ) for p in shifted_rows]
        nonzero = [p for p in polynomials if not p.is_zero]
        common_poly = nonzero[0]
        for p in nonzero[1:]:
            common_poly = sp.gcd(common_poly, p)
        monomial = sp.prod(x**e for x, e in zip(variables, minima))
        common = sp.factor(monomial*common_poly.as_expr())
        primitive = [sp.factor(p.exquo(common_poly).as_expr()) for p in polynomials]
        first = next(j for j, x in enumerate(primitive) if x != 0)
        column = [sp.factor(sp.cancel(expr(row[first])/primitive[first])) for row in operator]
        assert all(sp.cancel(expr(operator[i][j])-column[i]*primitive[j]) == 0
                   for i in range(4) for j in range(4)), ('outer_factorization', index)
        primitive_rows.append(primitive)
        results.append({'index': index, 'label': record['label'],
                        'base_root': base_text, 'moving_root': moving_text,
                        'annihilator_zero': True, 'trace': str(factor(trace)),
                        'selected_row_index': smallest, 'selected_row_factor': str(common),
                        'column_factor': [str(x) for x in column],
                        'primitive_row': [str(x) for x in primitive]})
        print(json.dumps(results[-1]), flush=True)
    determinant = sp.factor(sp.det(sp.Matrix(primitive_rows)))
    output = script.with_name('affine_product_one_r1_moving_rows_stage_output.json')
    result = {'status': 'EXACT_R1_MOVING_ROOT_OPERATORS_AND_ROW_FACTORIZATION',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, arithmetic]},
              'variables': [str(x) for x in variables], 'records': results,
              'row_determinant': str(determinant),
              'scope': 'Exact integer Laurent annihilators and traces, plus exact symbolic rank-one factorizations for the displayed original r=1 source core. Consequences at all finite-field parameter strata require the displayed factors and maps to be audited separately.'}
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'determinant': str(determinant),
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
