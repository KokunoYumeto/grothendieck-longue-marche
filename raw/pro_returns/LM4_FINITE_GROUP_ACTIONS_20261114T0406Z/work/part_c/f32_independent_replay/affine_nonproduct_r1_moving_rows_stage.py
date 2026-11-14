"""Exact exploratory moving-root rows for r=1 and boundary product h!=1."""
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json
import runpy
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_r1_source_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    products = folder/'affine_full_product_one_independent_audit.py'
    data = json.loads(source.read_text())
    arithmetic, sparse = runpy.run_path(str(helper)), runpy.run_path(str(products))
    arithmetic['configure'](data['variables'], data['characters'])
    parse = arithmetic['parse']
    parse.__globals__['UNITS']['h'] = parse('s*t*u*v*w*z')
    add, mul, mm, shifted, unpack = [sparse[key] for key in
                                    ['plus', 'times', 'mm', 'shifted', 'unpack_matrix']]
    variables = sp.symbols(' '.join(data['variables']))

    def expression(poly):
        return sp.Add(*(coefficient*sp.prod(x**n for x, n in zip(variables, exponent))
                        for exponent, coefficient in poly.items()))

    targets = [
        (1, ['1', '1/(v*w)'], '1/(t*z)'),
        (3, ['1', '1/(u*z)'], '1/(t*w)'),
        (4, ['1', '1/(v*z)'], '1/(t*u)'),
        (5, ['1', '1/(u*w)'], '1/(t*v)'),
        (6, ['1', '1/(v*w)', '(h/u)**2'], '1/(t*z)'),
        (8, ['1', '1/(u*z)', '(h/v)**2'], '1/(t*w)'),
        (9, ['1', '1/(v*z)', '(h/w)**2'], '1/(t*u)'),
        (10, ['1', '1/(u*w)', '(h/z)**2'], '1/(t*v)')]
    records, primitive_rows = [], []
    for index, bases, moving in targets:
        old = next(record for record in data['records'] if record['index'] == index)
        matrix = unpack(old['core_matrix_5'])
        operator = shifted(matrix, parse(bases[0]))
        tau = parse('1')
        for base in bases[1:]:
            operator = mm(operator, shifted(matrix, parse(base)))
        for base in bases:
            tau = mul(tau, add(parse(moving), {e: -a for e, a in parse(base).items()}))
        annihilator = mm(operator, shifted(matrix, parse(moving)))
        assert all(not entry for row in annihilator for entry in row), ('annihilator', index)
        trace = {}
        for j in range(5):
            trace = add(trace, operator[j][j])
        assert trace == tau, ('trace', index)
        selected = min((i for i, row in enumerate(operator) if any(row)),
                       key=lambda i: sum(len(poly) for poly in operator[i]))
        chosen = operator[selected]
        minima = tuple(min(e[j] for p in chosen for e in p) for j in range(6))
        polynomials = [sp.Poly(expression({tuple(e[j]-minima[j] for j in range(6)): a
                                          for e, a in p.items()}), *variables, domain=sp.ZZ)
                       for p in chosen]
        nonzero = [p for p in polynomials if not p.is_zero]
        common = nonzero[0]
        for p in nonzero[1:]:
            common = sp.gcd(common, p)
        q = [sp.factor(p.exquo(common).as_expr()) for p in polynomials]
        first = next(j for j, x in enumerate(q) if x != 0)
        column = [sp.factor(sp.cancel(expression(row[first])/q[first])) for row in operator]
        row_parsed = [[parse(str(entry)) for entry in q]]
        column_parsed = [[parse(str(entry))] for entry in column]
        assert mm(column_parsed, row_parsed) == operator, ('integral_outer_factor', index)
        assert mm(row_parsed, matrix) == sparse['scale'](parse(moving), row_parsed), ('eigenrow', index)
        record = {'index': index, 'label': old['label'], 'base_roots': bases, 'moving_root': moving,
                  'annihilator_zero': True, 'trace_product': str(sp.factor(expression(tau))),
                  'selected_operator_row_zero_based': selected,
                  'row_q': [str(entry) for entry in q], 'column_a': [str(entry) for entry in column],
                  'left_eigenrow_verified': True}
        records.append(record); primitive_rows.append(q)
        print(json.dumps(record), flush=True)
    determinants = {}
    for position in range(4, 8):
        selected = primitive_rows[:4]+[primitive_rows[position]]
        determinant = 0
        for permutation in permutations(range(5)):
            factors = [selected[i][permutation[i]] for i in range(5)]
            if any(value == 0 for value in factors):
                continue
            inversions = sum(permutation[i] > permutation[j] for i in range(5) for j in range(i+1, 5))
            determinant += (-1)**inversions*sp.prod(factors)
        determinants[str(targets[position][0])] = str(sp.factor(sp.expand(determinant)))
    result = {'status': 'EXACT_R1_NONPRODUCT_MOVING_ROOT_ROWS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest() for path in [source, helper, products]},
              'variables': data['variables'], 'records': records,
              'row_determinants_first_four_sources': [1, 3, 4, 5],
              'row_determinants_by_last_source': determinants,
              'scope': 'Exact integral source-core annihilators and left eigenrows with four square row determinants for r=1,h!=1. Every all-finite-field nonzero-factor argument and source-module consequence remains to be proved separately.'}
    output = script.with_name('affine_nonproduct_r1_moving_rows_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'determinants': determinants,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
