"""Exact source-zero eigenspace identities in the general boundary model."""
from hashlib import sha256
from pathlib import Path
import json
import runpy
import sympy as sp


def main():
    program = Path(__file__).resolve()
    folder = program.parent
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    products = folder/'affine_full_product_one_independent_audit.py'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    data = json.loads(source.read_text())
    sparse, arithmetic = runpy.run_path(str(products)), runpy.run_path(str(helper))
    arithmetic['configure'](data['variables'], data['characters'])
    parse = arithmetic['parse']
    add, mul, mm, shifted, unpack = [sparse[name] for name in ['plus', 'times', 'mm', 'shifted', 'unpack_matrix']]
    record = data['records'][0]
    assert record['index'] == 0
    matrix = unpack(record['boundary_quotient_matrix_6'])
    alpha = parse('1/(s*t*u*v*w*z)')
    operator = shifted(matrix, alpha)
    quadratic = mm(operator, shifted(matrix, parse('1')))
    assert all(not entry for row in quadratic for entry in row)
    trace = {}
    for j in range(6):
        trace = add(trace, matrix[j][j])
    assert trace == parse('5/(s*t*u*v*w*z)+1')
    print('Exact quadratic (T0-r/h I)(T0-I)=0 and trace 5r/h+1 PASS.', flush=True)
    variables = sp.symbols(' '.join(data['variables']))

    def expression(poly):
        return sp.Add(*(coefficient*sp.prod(x**power for x, power in zip(variables, exponent))
                        for exponent, coefficient in poly.items()))

    selected = min((i for i, row in enumerate(operator) if any(row)),
                   key=lambda i: sum(len(entry) for entry in operator[i]))
    chosen = operator[selected]
    minima = tuple(min(e[j] for entry in chosen for e in entry) for j in range(7))
    polynomials = [sp.Poly(expression({tuple(e[j]-minima[j] for j in range(7)): a
                                      for e, a in entry.items()}), *variables, domain=sp.ZZ)
                   for entry in chosen]
    nonzero = [p for p in polynomials if not p.is_zero]
    common = nonzero[0]
    for polynomial in nonzero[1:]:
        common = sp.gcd(common, polynomial)
    row = [sp.factor(polynomial.exquo(common).as_expr()) for polynomial in polynomials]
    first = next(i for i, entry in enumerate(row) if entry != 0)
    column = [sp.factor(sp.cancel(expression(line[first])/row[first])) for line in operator]
    q = [[parse(str(entry)) for entry in row]]
    a = [[parse(str(entry))] for entry in column]
    assert mm(a, q) == operator
    assert mm(q, matrix) == q
    assert mm(matrix, a) == a
    assert mm(q, a) == [[parse('1-1/(s*t*u*v*w*z)')]]
    result = {'status': 'EXACT_GENERAL_SOURCE_ZERO_QUADRATIC_AND_OUTER_FACTOR',
              'producer_sha256': sha256(program.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest()
                         for path in [source, products, helper]},
              'source_index': 0, 'source_label': record['label'],
              'scalar_alpha': 'r/h=1/(s*t*u*v*w*z)',
              'quadratic_zero': True, 'trace': '5*r/h+1',
              'outer_factor_identity': 'T0-(r/h)I=a*q; q*T0=q; T0*a=a; q*a=1-r/h',
              'selected_operator_row_zero_based': selected,
              'row_q': [str(entry) for entry in row],
              'column_a': [str(entry) for entry in column],
              'scope': 'Exact integer Laurent source-zero identities in the actual boundary quotient model. Rank and invariant-subspace consequences at each finite-field parameter stratum require their nonzero factors and maps to be proved separately; no general-character affine equality is asserted.'}
    output = program.with_name('affine_nonproduct_source_zero_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'row_q': result['row_q'],
                      'column_a': result['column_a'],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
