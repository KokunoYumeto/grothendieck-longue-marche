"""Exact rational-function specializations of the broader source cores.

These coefficient maps evaluate all deleted scalars and c at the displayed
rational units, retain t as an indeterminate, and set s=c/(r*t*u*v*w).
They are exploratory exact identities over Q(t), not all-field statements.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import sympy as sp


def evaluate(poly, scalars, s_axis, t_axis, variable):
    answer = {}
    for coefficient, exponent in poly:
        power = exponent[t_axis]-exponent[s_axis]
        value = Fraction(coefficient)
        for scalar, degree in zip(scalars, exponent):
            value *= scalar**degree
        answer[power] = answer.get(power, Fraction(0))+value
    return sp.Add(*(sp.Rational(a.numerator, a.denominator)*variable**power
                    for power, a in answer.items() if a))


def main():
    script = Path(__file__).resolve()
    source = script.with_name('affine_product_one_retained_pivots_stage_output.json')
    data = json.loads(source.read_text())
    t, z = sp.symbols('t z')
    cases = [
        {'r': 1, 'u': 2, 'v': 3, 'w': 5, 'c': 7},
        {'r': 1, 'u': 3, 'v': 5, 'w': 7, 'c': 11},
        {'r': 2, 'u': 2, 'v': 3, 'w': 5, 'c': 7},
    ]
    outputs = []
    for parameters in cases:
        r0, u0, v0, w0, c0 = [Fraction(parameters[x]) for x in ['r', 'u', 'v', 'w', 'c']]
        if r0 == 1:
            chart = data['charts'][1]
            scalars = [c0/(u0*v0*w0), Fraction(1), u0, v0, w0]
            s_axis, t_axis = 0, 1
        else:
            chart = data['charts'][0]
            scalars = [r0, c0/(r0*u0*v0*w0), Fraction(1), u0, v0, w0]
            s_axis, t_axis = 1, 2
        records = []
        for record in chart['source_records']:
            matrix = sp.Matrix([[evaluate(poly, scalars, s_axis, t_axis, t)
                                 for poly in row] for row in record['core_matrix']])
            characteristic = sp.factor(matrix.charpoly(z).as_expr())
            records.append({'index': record['index'], 'label': record['label'],
                            'characteristic_polynomial': str(characteristic),
                            'trace': str(sp.factor(sp.trace(matrix))),
                            'determinant': str(sp.factor(matrix.det()))})
            print(json.dumps({'parameters': parameters, 'source': record['index'],
                              'characteristic_polynomial': str(characteristic)}), flush=True)
        outputs.append({'parameters': parameters, 'chart': chart['name'], 'records': records})
    result = {'status': 'EXACT_RATIONAL_FUNCTION_SPECTRAL_SPECIALIZATIONS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'input': str(source), 'input_sha256': sha256(source.read_bytes()).hexdigest(),
              'cases': outputs,
              'scope': 'Only the displayed exact coefficient maps to Q(t). These spectra do not prove arbitrary-parameter or arbitrary-finite-field source separation.'}
    output = script.with_name('affine_product_one_core_spectral_specializations_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
