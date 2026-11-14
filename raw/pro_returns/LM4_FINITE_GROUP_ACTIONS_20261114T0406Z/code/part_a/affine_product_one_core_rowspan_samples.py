"""Exact rational samples of moving-eigenvalue row spaces.

Every scalar specialization is recorded. These finite samples establish
only their displayed ranks and matrix identities, not universal ranks.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import sympy as sp


def evaluate(poly, values):
    result = Fraction(0)
    for coefficient, exponent in poly:
        term = Fraction(coefficient)
        for value, power in zip(values, exponent):
            term *= value**power
        result += term
    return sp.Rational(result.numerator, result.denominator)


def main():
    script = Path(__file__).resolve()
    source = script.with_name('affine_product_one_retained_pivots_stage_output.json')
    data = json.loads(source.read_text())
    parameter_rows = [
        (2, 11, 2, 3, 5, 7), (3, 13, 3, 5, 7, 11),
        (1, 11, 2, 3, 5, 7), (1, 13, 3, 5, 7, 11),
        (2, 11, 2, 1, 1, 7), (1, 11, -1, 1, 1, -1),
        (1, 11, 2, 3, 5, 1),
        (2, 11, 2, 3, 5, 1), (2, 11, 1, 3, 1, 1),
    ]
    outputs = []
    for row in parameter_rows:
        rr, tt, uu, vv, ww, cc = map(Fraction, row)
        ss = cc/(rr*tt*uu*vv*ww)
        chart = data['charts'][int(rr == 1)]
        values = ([ss, tt, uu, vv, ww] if rr == 1 else [rr, ss, tt, uu, vv, ww])
        matrices = {record['index']: sp.Matrix([[evaluate(poly, values) for poly in line]
                                               for line in record['core_matrix']])
                    for record in chart['source_records']}
        dimension = chart['core_dimension']
        eye = sp.eye(dimension)
        aa = {6: 1/(vv*ww), 8: cc/uu, 9: cc/vv, 10: 1/(uu*ww)}
        bb = {6: cc/tt, 8: 1/(tt*ww), 9: 1/(tt*uu), 10: 1/(tt*vv)}
        rows = {}
        annihilators = {}
        for index in (6, 8, 9, 10):
            rows[index] = (matrices[index]-eye)*(matrices[index]-sp.Rational(aa[index])*eye)
            annihilators[index] = rows[index]*(matrices[index]-sp.Rational(bb[index])*eye) == sp.zeros(dimension)
        for positive, negative, extra in [(1, 6, 1/(rr*rr*uu*uu)),
                                          (3, 8, 1/(rr*rr*vv*vv)),
                                          (4, 9, 1/(rr*rr*ww*ww)),
                                          (5, 10, (cc/rr)**2)]:
            rows[positive] = (matrices[positive]-eye)*(matrices[positive]-sp.Rational(aa[negative])*eye)
            if rr != 1:
                rows[positive] = rows[positive]*(matrices[positive]-sp.Rational(extra)*eye)
            annihilators[positive] = rows[positive]*(matrices[positive]-sp.Rational(bb[negative])*eye) == sp.zeros(dimension)
        defect = matrices[7]-sp.Rational(tt)*eye
        comparisons = []
        for indices in ([8, 10], [8, 9, 10], [6, 8, 9, 10], [1, 3, 4, 5, 6, 8, 9, 10]):
            stacked = sp.Matrix.vstack(*(rows[i] for i in indices))
            comparisons.append({'source_indices': indices, 'row_rank': stacked.rank(),
                                'rank_with_source7_minus_t': sp.Matrix.vstack(stacked, defect).rank()})
        outputs.append({'parameters': dict(zip(['r', 't', 'u', 'v', 'w', 'c'], row)),
                        's': str(ss), 'core_dimension': dimension,
                        'moving_row_ranks': {str(i): m.rank() for i, m in rows.items()},
                        'tested_annihilators_zero': annihilators,
                        'source7_minus_t_rank': defect.rank(), 'rowspace_comparisons': comparisons})
    result = {'status': 'EXACT_RATIONAL_CORE_ROWSPACE_SAMPLES',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'input': str(source), 'input_sha256': sha256(source.read_bytes()).hexdigest(),
              'samples': outputs,
              'scope': 'Only the displayed rational coefficient evaluations. These ranks and zero products do not establish arbitrary-parameter or all-finite-field source-module identities.'}
    output = script.with_name('affine_product_one_core_rowspan_samples_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
