"""Exact two-coordinate chart for the actual moving-row common kernel.

The chart applies to t != 1 and uses only displayed Laurent-unit
denominators.  The additional rows are retained, with no full-rank
assertion inferred from a generic symbolic rank.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    moving = folder/'affine_nonproduct_general_moving_rows_stage_output.json'
    outer = folder/'affine_nonproduct_source_zero_stage_output.json'
    rows, factors = json.loads(moving.read_text()), json.loads(outer.read_text())
    r, h, t, u, v, w, z = variables = sp.symbols('r h t u v w z')
    local = dict(zip(map(str, variables), variables))
    local['s'] = h/(r*t*u*v*w*z)
    q = {record['index']: sp.Matrix([[sp.sympify(x, locals=local)
                                    for x in record['row_q']]])
         for record in rows['records']}
    q0 = sp.Matrix([[sp.sympify(x, locals=local) for x in factors['row_q']]])
    eta = sp.Matrix([[0, 1/(t-1), 1, u, u*v, u*v*w]])
    inverse = eta.col_join(sp.Matrix([[0, 0, 0, 1, 0, 0]]))
    scale = h/(u*v*w*z)
    basis = sp.zeros(6, 2)
    basis[2, 0] = scale*(u-1)
    basis[4, 0] = scale*(w-1)
    basis[5, 0] = scale*(z-1)
    basis[3, 1] = 1
    basis[1, 0] = (t-1)*(1-scale*((u-1)+u*v*(w-1)+u*v*w*(z-1)))
    basis[1, 1] = -(t-1)*u
    for col in range(2):
        basis[0, col] = sp.factor(-sum(q0[j]*basis[j, col] for j in range(1, 6))/q0[0])
    checks = 0
    for row in [q0, q[1], q[8], q[9]]:
        assert all(sp.cancel(x) == 0 for x in row*basis)
        checks += 1
    assert all(sp.cancel(x) == 0 for x in inverse*basis-sp.eye(2)); checks += 1
    # Recover every original coordinate from these four row equations.
    row_equations = q0.col_join(q[1]).col_join(q[8]).col_join(q[9])
    reconstruction = sp.zeros(6, 4)
    reconstruction[2, 3] = -1/((t-1)*u*v*w*z)
    reconstruction[5, 1] = 1/((t-1)*u*v*w*z)
    reconstruction[4, 1] = -(w-1)/((t-1)*u*v*w*z)
    reconstruction[4, 2] = -1/((t-1)*u*v*w)
    for col in range(4):
        reconstruction[1, col] = -(t-1)*(reconstruction[2, col]+u*v*reconstruction[4, col]
                                             +u*v*w*reconstruction[5, col])
        reconstruction[0, col] = sp.factor((int(col == 0)-sum(q0[j]*reconstruction[j, col]
                                                               for j in range(1, 6)))/q0[0])
    full_basis = reconstruction.row_join(basis)
    full_inverse = row_equations.col_join(inverse)
    assert all(sp.cancel(x) == 0 for x in full_basis*full_inverse-sp.eye(6)); checks += 1
    assert all(sp.cancel(x) == 0 for x in full_inverse*full_basis-sp.eye(6)); checks += 1
    determinant = sp.factor(full_inverse.det())
    assert sp.cancel(determinant-r*t*u**3*v**4*w**3*z**2*(t-1)**2) == 0
    checks += 1
    reduced = {str(index): [str(sp.factor(x)) for x in q[index]*basis]
               for index in [3, 4, 5, 6, 10]}
    result = {
        'status': 'PASS_ACTUAL_MOVING_KERNEL_CHART',
        'producer_sha256': sha256(script.read_bytes()).hexdigest(),
        'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [moving, outer]},
        'coordinate_map': 's=h/(r*t*u*v*w*z)',
        'kernel_rows': ['q0', 'q1', 'q8', 'q9'],
        'coordinates': ['eta*x', 'x4'],
        'basis': [[str(sp.factor(x)) for x in row] for row in basis.tolist()],
        'inverse': [[str(x) for x in row] for row in inverse.tolist()],
        'augmented_row_order': ['q0', 'q1', 'q8', 'q9', 'eta', 'e4'],
        'augmented_row_determinant': str(determinant),
        'reconstruction': [[str(sp.factor(x)) for x in row] for row in reconstruction.tolist()],
        'remaining_rows_on_chart': reduced,
        'direct_check_count': checks,
        'scope': 'Exact actual chart and inverse on the four-row kernel for t != 1. Every additional row is retained; no generic rank is asserted at a specialized field point.'}
    output = script.with_name('affine_nonproduct_moving_kernel_chart_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': checks, 'remaining_rows': reduced,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2), flush=True)


if __name__ == '__main__':
    main()
