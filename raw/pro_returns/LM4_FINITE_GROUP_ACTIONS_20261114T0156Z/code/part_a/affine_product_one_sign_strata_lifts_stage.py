"""Exact forced lifts on the fifteen nontrivial product-one sign strata.

Original r=1; deleted characters u,v,w,c are signs and not all one.
The original t remains an indeterminate. Core moving rows give a
canonical necessary lift, which is tested against all actual sources.
"""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    full_path = folder/'affine_product_one_retained_pivots_stage_output.json'
    moving_path = folder/'affine_product_one_r1_moving_rows_stage_output.json'
    full = json.loads(full_path.read_text())['charts'][1]
    moving = json.loads(moving_path.read_text())
    s, t, u, v, w = sp.symbols('s t u v w')
    local = dict(zip(['s', 't', 'u', 'v', 'w'], [s, t, u, v, w]))
    results = []

    def clean(matrix):
        return matrix.applyfunc(lambda x: sp.factor(sp.cancel(x)))

    def strings(matrix):
        return [[str(x) for x in row] for row in matrix.tolist()]

    def universal_nonzero(expression):
        numerator, denominator = sp.fraction(sp.cancel(expression))
        evidence = []
        for polynomial in (numerator, denominator):
            constant, factors = sp.factor_list(polynomial, t)
            constant = sp.Rational(constant)
            if constant == 0:
                return None
            for integer in (abs(int(constant.p)), abs(int(constant.q))):
                while integer and integer % 2 == 0:
                    integer //= 2
                if integer != 1:
                    return None
            if any(sp.degree(factor, t) > 1 for factor, power in factors):
                return None
            evidence.append({'constant': str(constant),
                             'linear_factors': [[str(factor), power] for factor, power in factors]})
        return evidence

    for uu, vv, ww, cc in product([1, -1], repeat=4):
        if (uu, vv, ww, cc) == (1, 1, 1, 1):
            continue
        epsilon = cc*uu*vv*ww
        substitution = {s: epsilon/t, u: uu, v: vv, w: ww}

        def specialize(poly):
            terms = {}
            for coefficient, exponent in poly:
                a, b, d, e, f = exponent
                sign = ((-1 if a % 2 else 1) if epsilon == -1 else 1)
                for value, degree in [(uu, d), (vv, e), (ww, f)]:
                    if value == -1 and degree % 2:
                        sign = -sign
                power = b-a
                terms[power] = terms.get(power, 0)+coefficient*sign
            return sp.Add(*(coefficient*t**power for power, coefficient in terms.items() if coefficient))

        matrices = {record['index']: sp.Matrix([[specialize(poly) for poly in row]
                                               for row in record['block_matrix_6']])
                    for record in full['source_records']}
        core_rows = sp.Matrix([[sp.sympify(text, locals=local).subs(substitution)
                               for text in record['primitive_row']]
                              for record in moving['records']])
        core_rows = clean(core_rows)
        assert all(t not in x.free_symbols for x in core_rows)
        assert core_rows.det() == 1
        extended_rows = []
        for position, record in enumerate(moving['records']):
            index = record['index']
            base = sp.sympify(record['base_root'], locals=local).subs(substitution)
            moving_root = sp.sympify(record['moving_root'], locals=local).subs(substitution)
            operator = clean((matrices[index]-sp.eye(6))*(matrices[index]-base*sp.eye(6)))
            trace = sp.factor((moving_root-1)*(moving_root-base))
            row = clean(core_rows[position, :]*operator[:4, :]/trace)
            assert row[:, :4] == core_rows[position, :]
            extended_rows.append(list(row))
        extended = sp.Matrix(extended_rows)
        lifts = clean((-core_rows.inv()*extended[:, 4:]).col_join(sp.eye(2)))
        candidates = []
        for column, name in [(0, 'boundary'), (1, 'X1')]:
            candidate = lifts[:, column]
            residuals = []
            for index, matrix in matrices.items():
                scalar = (t if index == 2 else 1/t if index == 7 else 1)
                if name == 'X1':
                    scalar = (1/t if index == 2 else t if index == 7 else 1)
                residual = clean(matrix*candidate-scalar*candidate)
                residuals.append({'index': index, 'residual': strings(residual)})
            selected = None
            for entry in residuals:
                for coordinate, item in enumerate(entry['residual']):
                    expression = sp.sympify(item[0], locals=local)
                    if expression == 0:
                        continue
                    evidence = universal_nonzero(expression)
                    if evidence is not None:
                        selected = {'source_index': entry['index'], 'coordinate_zero_based': coordinate,
                                    'residual': str(expression),
                                    'numerator_and_denominator_factorization': evidence}
                        break
                if selected is not None:
                    break
            candidates.append({'type': name, 'candidate': strings(candidate),
                               'all_source_residuals': residuals,
                               'selected_all_odd_characteristic_nonzero_residual': selected})
        record = {'signs': {'u': uu, 'v': vv, 'w': ww, 'c': cc}, 's_coefficient_epsilon': epsilon,
                  'core_row_matrix': strings(core_rows), 'core_row_inverse': strings(core_rows.inv()),
                  'extended_moving_rows': strings(extended), 'candidates': candidates}
        results.append(record)
        print(json.dumps({'signs': record['signs'],
                          'boundary': candidates[0]['selected_all_odd_characteristic_nonzero_residual'],
                          'X1': candidates[1]['selected_all_odd_characteristic_nonzero_residual']}), flush=True)
    result = {'status': 'EXACT_PRODUCT_ONE_SIGN_STRATUM_FORCED_LIFTS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [full_path, moving_path]},
              'strata': results,
              'all_boundary_candidates_excluded_by_recorded_factors':
                  all(x['candidates'][0]['selected_all_odd_characteristic_nonzero_residual'] is not None for x in results),
              'scope': 'Exact coefficient specializations, unimodular core row inverses, necessary lifts and actual source residuals. All-field conclusions require the nonzero-factor reasoning and separate literal-word review of these computations.'}
    output = script.with_name('affine_product_one_sign_strata_lifts_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'strata': len(results),
                      'all_boundary_candidates_excluded': result['all_boundary_candidates_excluded_by_recorded_factors'],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
