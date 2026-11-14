"""Exact certificates for the zero-rank-one nonfixed-t row cover.

These are actual previously word-derived source rows and operators.
The field arguments and every nonzero factor are written separately;
this program checks the displayed rational and Laurent identities.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    chart_path = folder/'affine_nonproduct_moving_kernel_chart_stage_output.json'
    orbit_path = folder/'affine_nonproduct_general_observability_stage_output.json'
    cover_path = folder/'affine_nonproduct_same_rh_row_cover_stage_output.json'
    special_path = folder/'affine_nonproduct_q_special_rows_stage_output.json'
    moving_path = folder/'affine_nonproduct_general_moving_rows_stage_output.json'
    chart, orbit, cover, special, moving = [json.loads(p.read_text()) for p in
                                           [chart_path, orbit_path, cover_path, special_path, moving_path]]
    r, h, t, u, v, w, z, H = sp.symbols('r h t u v w z H')
    local = {str(x): x for x in [r, h, t, u, v, w, z, H]}
    local['s'] = h/(r*t*u*v*w*z)
    basis = sp.Matrix([[sp.sympify(x, locals=local) for x in row] for row in chart['basis']])
    remaining = {int(index): sp.Matrix([[sp.sympify(x, locals=local) for x in row]])
                 for index, row in chart['remaining_rows_on_chart'].items()}
    orbits = {record['index']: sp.Matrix([[sp.sympify(x, locals=local)
                                         for x in record['qT_basis_first_five_divided_by_r_minus_one']]])
              for record in orbit['records']}
    checks = []

    def check(name, value, expected=0):
        assert sp.cancel(value-expected) == 0, name
        checks.append(name)

    # Both full quartics are displayed in the written collision proof.
    full_polynomials = []
    for index in [6, 8, 9, 10]:
        record = next(rec for rec in special['records'] if rec['index'] == index)
        old = next(rec for rec in moving['records'] if rec['index'] == index)
        all_roots = record['roots_removed']+[record['special_root']]
        assert sorted(all_roots) == sorted(old['base_roots']+[old['moving_root']])
        checks.append('same_actual_degree4_roots_'+str(index))
        full_polynomials.append({'index_zero_based': index, 'roots': all_roots,
                                 'direct_special_left_row': record['primitive_row'],
                                 'q_polynomial_orbit_factor': record['q_polynomial_orbit_factor']})

    retained_pairings = []
    for index, substitution, expected in [
        (2, {}, -h*(r*t+1)/(t*u*w*z)),
        (9, {t: -1/r}, h*r*(u-1)/(u**2*w*z)),
        (6, {t: -1/r, u: 1}, -h*r**2*(z-1)/(w*z**2)),
        (10, {t: -1/r, u: 1, z: 1}, -h*r**2*(v-1)/(v*w)),
        (3, {t: -1/r, u: 1, z: 1, v: 1}, -h*r**2*(w-1)/w**2)]:
        value = sp.factor(orbits[index][0].subs(substitution, simultaneous=True))
        check('retained_line_source_'+str(index), value, expected)
        retained_pairings.append({'source_zero_based': index,
                                  'substitution': {str(k): str(val) for k, val in substitution.items()},
                                  'q_T_b_divided_by_r_minus_one': str(value)})

    check('q5_second_pivot', remaining[5][1], -h*u*z*(t-1)*(h+v-1))
    f3 = sp.sympify(cover['reduced_determinant3'], locals=local)
    f5 = sp.sympify(cover['reduced_determinant5'], locals=local)
    # H != 1, z != 1: D4 gives u=1 and D6 determines this t.
    ts = -(r-1)*(v-1)/(r*v*(H-1))
    substitution = {h: H/r, u: 1, t: ts}
    A = -H**2*w*(v-1)-H*(H-1)*z*(w-1)
    B = w*(H*(v-1)+(H-1)*z)
    check('Hneq_zneq_f3', f3.subs(substitution, simultaneous=True),
          -(r-1)*(A+r*B)/(r*(H-1)))
    check('Hneq_zneq_f3_nonzero_combination', A+H*B, H*(H-1)*z)
    A5 = H*(H*(v-1)+(H-1)*z)
    B5 = (v-1)*((H-1)*z-H)
    check('Hneq_zneq_w1_f5', f5.subs({**substitution, w: 1}, simultaneous=True),
          -(r-1)*(A5+r*B5)/(r*(H-1)))
    check('Hneq_zneq_w1_f5_nonzero_combination', A5-H*B5/(v-1), H**2*v)

    # Exact degree-one resultants; no generic-rank step occurs here.
    cases = [
        ('Hneq_uz1', {h: H/r, u: 1, z: 1},
         -r*v*w*(r-H)*(r-1)*(r*w-H*(w-1))*(H+r*(v+w-1))),
        ('H1_z1', {h: 1/r, z: 1},
         -r*v*w*(r-1)**2*(r*w-w+1)*(r*u*v-r*u+r*w+u))]
    resultants = []
    for name, substitution, expected in cases:
        a = sp.cancel(r*f3.subs(substitution, simultaneous=True))
        b = sp.cancel(r**2*f5.subs(substitution, simultaneous=True))
        assert sp.Poly(a, t).degree() == sp.Poly(b, t).degree() == 1
        checks.append(name+'_both_degree_one')
        resultant = sp.factor(sp.resultant(a, b, t))
        check(name+'_resultant', resultant, expected)
        resultants.append({'name': name, 'first_polynomial': str(sp.factor(a)),
                           'second_polynomial': str(sp.factor(b)),
                           'resultant_in_t': str(resultant)})

    def orbit_on_chart(index, substitution, coefficients):
        specialized = basis.subs(substitution, simultaneous=True)*coefficients.subs(substitution, simultaneous=True)
        row = orbits[index].subs(substitution, simultaneous=True)
        return sp.factor((row*specialized[1:, :])[0])

    final_cover = []
    def final(name, index, substitution, coefficients, expected):
        value = orbit_on_chart(index, substitution, coefficients)
        check(name, value, expected)
        final_cover.append({'name': name, 'source_zero_based': index,
                            'substitution': {str(k): str(val) for k, val in substitution.items()},
                            'chart_column': [str(x) for x in coefficients],
                            'q_T_b_divided_by_r_minus_one': str(value)})

    final('v1_qT9', 9, {v: 1}, sp.Matrix([1, 0]), h**3*(h+w)*(w-1)/w**4)
    final('wz1_qT8', 8, {w: 1, z: 1}, sp.Matrix([1, (v-1)/(u*(h+v-1))]),
          h**2*(h+v)*(v-1)/(v**2*(h+v-1)))
    final('reciprocal_qT2', 2, {h: 1/r, v: 1, w: 1}, sp.Matrix([1, 0]),
          -(t-1)*(r*t+1)/(r*t))
    final('reciprocal_rtminus1_qT1', 1, {h: 1/r, v: 1, w: 1, t: -1/r}, sp.Matrix([1, 0]),
          -(u-1)*(r*u+1)/(r*u**2))
    final('reciprocal_rtminus1_qT10', 10, {h: 1/r, v: 1, w: 1, t: -1/r}, sp.Matrix([1, 0]),
          (z-1)*(r*z+1)/(r**2*z**2))
    result = {
        'status': 'PASS_EXACT_ZERO_RANK_ONE_NONFIXED_T_COVER',
        'producer_sha256': sha256(script.read_bytes()).hexdigest(),
        'inputs': {str(p): sha256(p.read_bytes()).hexdigest()
                   for p in [chart_path, orbit_path, cover_path, special_path, moving_path]},
        'coefficient_map': 's=h/(r*t*u*v*w*z)',
        'full_degree4_annihilator_roots': full_polynomials,
        'retained_line_pairing_cover': retained_pairings,
        'Hneq_zneq_t': str(ts),
        'Hneq_zneq_f3_coefficients': [str(A), str(B)],
        'Hneq_zneq_w1_f5_coefficients': [str(A5), str(B5)],
        'linear_resultants': resultants, 'last_source_pairing_cover': final_cover,
        'checks': checks, 'direct_check_count': len(checks),
        'scope': 'Exact source-row identities for the written zero-R0 Frobenius case analysis, including full quartic root lists and every displayed residual pairing. These calculations alone make no claim about the remaining fixed-t quadratic sign case.'}
    output = script.with_name('affine_nonproduct_zero_rank_one_moving_cover_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': len(checks),
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2), flush=True)


if __name__ == '__main__':
    main()
