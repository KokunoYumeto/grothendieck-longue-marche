"""Exact row-cover identities for the actual nonproduct source matrices.

This exploratory certificate retains the original boundary coordinates.
It records the moving-row pairings, determinant cover and reciprocal
residual kernel with its actual source2 image. No general affine-image
conclusion is asserted.
"""
from pathlib import Path
from hashlib import sha256
import json
import runpy
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    moving = folder/'affine_nonproduct_general_moving_rows_stage_output.json'
    outer = folder/'affine_nonproduct_source_zero_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    product = folder/'affine_full_product_one_independent_audit.py'
    data, rows, factor = [json.loads(p.read_text()) for p in [source, moving, outer]]
    old, sparse = runpy.run_path(str(helper)), runpy.run_path(str(product))
    names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
    old['configure'](names, [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(7)] for j in range(2, 7)])
    parse, pm = old['parse'], old['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    r, h, t, u, v, w, z = variables = sp.symbols(' '.join(names))
    local = dict(zip(names, variables))
    local['s'] = h/(r*t*u*v*w*z)

    def expression(poly):
        return sp.Add(*(a*sp.prod(x**n for x, n in zip(variables, e)) for e, a in poly.items()))

    q = {rec['index']: pm([rec['row_q']])[0] for rec in rows['records']}
    q0 = pm([factor['row_q']])[0]
    a = pm([[x] for x in factor['column_a']])
    pairings = {}
    for index, row in q.items():
        value = sparse['mm']([row], a)[0][0]
        pairings[index] = sp.factor(expression(value))
    cover = [
        (4, {}, u*w*z*(h-1)*(t-1)*(u-1)),
        (6, {u: 1}, w*z*(h-1)*(t-1)*(z-1)),
        (3, {u: 1, z: 1}, w*(h-1)*(t-1)*(w-1)/h),
        (10, {u: 1, z: 1, w: 1}, (h-1)*(t-1)*(v-1)/h)]
    cover_records = []
    for index, subs, expected in cover:
        value = sp.factor(pairings[index].subs(subs, simultaneous=True))
        assert sp.cancel(value-expected) == 0, ('pairing_cover', index)
        cover_records.append({'index': index, 'substitution': {str(k): str(vv) for k, vv in subs.items()},
                              'value': str(value)})
    determinants = {}
    for index in [3, 4, 5, 6]:
        matrix = [q0]+[q[j] for j in [1, 8, 9, 10, index]]
        result = sparse['determinant'](matrix, parse('1'))
        determinants[index] = sp.factor(expression(result))
        print(json.dumps({'determinant_append_source': index, 'monomials': len(result),
                          'factored': str(determinants[index])}), flush=True)
    reduced3 = sp.cancel(determinants[3]/(h**2*r**2*t**2*u**5*v**3*w**2*z**2*(t-1)**4*(w-1)))
    reduced5 = sp.cancel(determinants[5]/(h**2*r*t*u**4*v**3*w**2*z**3*(t-1)**4*(v-1)))
    poly3, poly5 = sp.Poly(reduced3, t), sp.Poly(reduced5.subs(w, 1), t)
    assert poly3.degree() == 1 and sp.cancel(poly3.nth(1)-r*v*w*(1-h)) == 0
    assert poly5.degree() == 1 and sp.cancel(poly5.nth(1)-r*v*(h-1)) == 0
    expected4 = h**2*r**2*t**2*u**5*v**4*w**2*z**3*(t-1)**4*(u-1)*(h*r-1)*(h*w-h-w)
    expected6 = h**2*r*t*u**5*v**3*w**2*z**3*(t-1)**4*(z-1)*(h*w-h-w)*(r*t*v*(h*r-1)+(r-1)*u*(v-1))
    assert sp.cancel(determinants[4]-expected4) == 0
    assert sp.cancel(determinants[6]-expected6) == 0

    subs = {h: 1/r, v: 1, w: 1}
    qsp = {index: sp.Matrix([[sp.factor(expression(p).subs(subs, simultaneous=True)) for p in row]])
           for index, row in q.items()}
    q0sp = sp.Matrix([[sp.factor(expression(p).subs(subs, simultaneous=True)) for p in q0]])
    b = sp.Matrix([(-r**2*t*u*z+r**2*u**2*z**2-r*u**2*z**2+r*u*z-u*z+1)/(r**2*t*u*z),
                   (t-1)*(r*u*z-u*z+1), u-1, 0, 0, z-1])
    assert all(sp.cancel(x) == 0 for x in q0sp*b)
    for index in qsp:
        assert all(sp.cancel(x) == 0 for x in qsp[index]*b), ('residual_kernel', index)
    assert qsp[5] == sp.Matrix([[0, 0, 0, -u*z*(t-1)/r**2, 0, 0]])
    assert qsp[8] == sp.Matrix([[0, 0, 0, 0, -u*(t-1), 0]])
    cross = sp.Matrix([qsp[1][j] for j in [1, 2, 5]]).cross(
        sp.Matrix([qsp[9][j] for j in [1, 2, 5]]))
    cross_expected = u*z*(t-1)/r*sp.Matrix([(t-1)*(r*u*z-u*z+1), u-1, z-1])
    assert all(sp.cancel(x) == 0 for x in cross-cross_expected)
    assert q0sp[0] == r*t
    raw2 = next(d for d in data['records'] if d['index'] == 2)['boundary_quotient_matrix_6']

    def reciprocal_expression(poly):
        return sp.Add(*(coefficient*r**(aa-2*bb)*t**(cc-bb)*u**(dd-bb)*z**(gg-bb)
                        for coefficient, (aa, bb, cc, dd, ee, ff, gg) in poly))

    matrix2 = sp.Matrix([[reciprocal_expression(p) for p in row] for row in raw2])
    residue = (matrix2-r*t*sp.eye(6))*b
    expected_residue = sp.Matrix([0, -u**2*z**2*(r-1)*(t-1)*(r*t+1)/t, 0, 0, 0, 0])
    assert all(sp.cancel(x) == 0 for x in residue-expected_residue)
    next_pairing = sp.factor((q0sp*matrix2*b)[0])
    assert sp.cancel(next_pairing+u*z*(r-1)*(t-1)*(r*t+1)/t) == 0
    result = {'status': 'PASS_EXACT_SAME_RH_ROW_COVER_IDENTITIES',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, moving, outer, helper, product]},
              'variables': names,
              'pairings_q_l_a': {str(i): str(p) for i, p in pairings.items()},
              'nonzero_pairing_cover': cover_records,
              'determinant_row_order': ['q0', 'q1', 'q8', 'q9', 'q10', 'q_append'],
              'determinants': {str(i): str(p) for i, p in determinants.items()},
              'reduced_determinant3': str(sp.factor(reduced3)),
              'reduced_determinant5': str(sp.factor(reduced5)),
              'leading_coefficient3_in_t': str(sp.factor(poly3.nth(1))),
              'leading_coefficient5_in_t_at_w1': str(sp.factor(poly5.nth(1))),
              'reciprocal_stratum': {
                  'h': '1/r', 'v': '1', 'w': '1',
                  'kernel_column_b': [str(x) for x in b],
                  'q0_first_pivot': 'r*t', 'q5_pivot': '-u*z*(t-1)/r**2', 'q8_pivot': '-u*(t-1)',
                  'q1_q9_cross_product_in_coordinates_2_3_6': [str(sp.factor(x)) for x in cross],
                  'source2_minus_rt_image': [str(x) for x in expected_residue],
                  'q0_T2_b': str(next_pairing)},
              'scope': 'Exact integer Laurent/rational identities in the original six boundary coordinates. The written field argument must supply each nonzero factor and actual Frobenius fixed-field inclusion; no broader affine-image conclusion is asserted by this computation.'}
    output = script.with_name('affine_nonproduct_same_rh_row_cover_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
