"""Separate exploratory source-zero covector orbits for r!=1,h!=1.

All inputs are read unchanged. The original boundary quotient is
transported by s=h/(r*t*u*v*w*z), with explicit monomial exponent map.
The source-zero covector basis has a Laurent-unit pivot r*t*v.
Only the exact recorded identities are asserted.
"""
from hashlib import sha256
from pathlib import Path
import json
import runpy
import sympy as sp


def divide_r_minus_one(poly):
    groups = {}
    for exponent, coefficient in poly.items():
        groups.setdefault(exponent[1:], {})[exponent[0]] = coefficient
    answer = {}
    for other, coefficients in groups.items():
        assert sum(coefficients.values()) == 0, ('not_divisible_by_r_minus_one', other)
        lower, upper = min(coefficients), max(coefficients)
        cumulative = 0
        for degree in range(lower, upper):
            cumulative += coefficients.get(degree, 0)
            if cumulative:
                answer[(degree,)+other] = -cumulative
    return answer


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    matrix_path = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    factor_path = folder/'affine_nonproduct_source_zero_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    products = folder/'affine_full_product_one_independent_audit.py'
    matrices = json.loads(matrix_path.read_text())
    factors = json.loads(factor_path.read_text())
    arithmetic, sparse = runpy.run_path(str(helper)), runpy.run_path(str(products))
    arithmetic['configure'](['r', 'h', 't', 'u', 'v', 'w', 'z'],
                            [[int(i == j) for i in range(7)] for j in range(7)])
    parse, pm = arithmetic['parse'], arithmetic['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    add, neg, mul, mm, eye, sub = [sparse[x] for x in ['plus', 'neg', 'times', 'mm', 'eye', 'minus']]
    one = parse('1')
    q = pm([factors['row_q']])
    column = pm([[x] for x in factors['column_a']])
    check_count = 0
    assert q[0][0] == parse('r*t*v'); check_count += 1
    basis = [[{} for _ in range(6)] for _ in range(6)]
    inverse = [[{} for _ in range(6)] for _ in range(6)]
    for j in range(5):
        basis[0][j] = mul(parse('-1/(r*t*v)'), q[0][j+1])
        basis[j+1][j] = one
        inverse[j][j+1] = one
    basis[0][5] = parse('1/(r*t*v)')
    inverse[5] = q[0]
    assert mm(basis, inverse) == eye(6, one); check_count += 1
    assert mm(inverse, basis) == eye(6, one); check_count += 1

    def change(poly):
        out = {}
        for coefficient, (a, b, c, d, e, f, g) in poly:
            out = add(out, {(a-b, b, c-b, d-b, e-b, f-b, g-b): coefficient})
        return out

    symbols = sp.symbols('r h t u v w z')

    def expression(poly):
        return sp.Add(*(coefficient*sp.prod(x**n for x, n in zip(symbols, exponent))
                        for exponent, coefficient in poly.items()))

    records = []
    for record in matrices['records']:
        matrix = [[change(p) for p in row] for row in record['boundary_quotient_matrix_6']]
        index = record['index']
        row = mm(mm(q, matrix), basis)[0]
        divided = [divide_r_minus_one(p) for p in row[:5]]
        assert [mul(parse('r-1'), p) for p in divided] == row[:5]; check_count += 1
        if index == 0:
            assert row == [{}]*5+[one]; check_count += 1
            assert sub(matrix, sparse['scale'](parse('r/h'), eye(6, one))) == mm(column, q); check_count += 1
        factored = [str(sp.factor(expression(p))) for p in divided]
        scalar = str(sp.factor(expression(row[5])))
        assert pm([factored]) == [divided]; check_count += 1
        item = {'index': index, 'label': record['label'],
                'qT_basis_first_five_divided_by_r_minus_one': factored,
                'last_coordinate_scalar': scalar,
                'first_five_raw_monomial_count': sum(map(len, row[:5])),
                'divided_monomial_count': sum(map(len, divided))}
        records.append(item)
        print(json.dumps(item), flush=True)
    result = {'status': 'EXACT_GENERAL_SOURCE_ZERO_COVECTOR_ORBITS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest()
                         for path in [matrix_path, factor_path, helper, products]},
              'variables': ['r', 'h', 't', 'u', 'v', 'w', 'z'],
              'coefficient_map': 's=h/(r*t*u*v*w*z)',
              'covector_q': factors['row_q'],
              'basis': arithmetic['serial_matrix'](basis),
              'inverse_basis': arithmetic['serial_matrix'](inverse),
              'records': records, 'direct_check_count': check_count,
              'scope': 'Exact Laurent source-zero covector orbit rows and their r-1 factors with both basis inverses. No full-rank, invariant-submodule, Frobenius-separation or new affine-image conclusion is asserted.'}
    output = script.with_name('affine_nonproduct_general_observability_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': check_count,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
