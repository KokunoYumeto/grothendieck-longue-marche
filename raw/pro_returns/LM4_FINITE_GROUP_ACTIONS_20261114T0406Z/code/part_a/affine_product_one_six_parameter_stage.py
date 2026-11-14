"""Exploratory actual-source matrices on the full product-one torus.

The coefficient tuple is (r,s,t,u,v,w,(rstuvw)^-1). The actual
principal pivot is X7. Both the five-dimensional boundary kernel
and its r=1 four-dimensional refinement are retained with explicit
bases and inverse maps. No marginal-image conclusion is registered.
"""
from hashlib import sha256
from pathlib import Path
import json
import sympy as sp


PARAMETERS = sp.symbols('r s t u v w')
r, s, t, u, v, w = PARAMETERS
CHECKS = {}


def check(value, name):
    assert value, name
    CHECKS[name] = CHECKS.get(name, 0) + 1


def simp(value):
    return sp.factor(sp.cancel(value))


def clean(matrix):
    return matrix.applyfunc(simp)


def verify(matrix, name):
    for value in matrix:
        check(sp.cancel(value) == 0, name)


def specialize(poly):
    terms = {}
    for coefficient, exponent in poly:
        key = tuple(exponent[i] - exponent[6] for i in range(6))
        terms[key] = terms.get(key, 0) + coefficient
    return sp.Add(*(coefficient * sp.prod(x**n for x, n in zip(PARAMETERS, exponent))
                    for exponent, coefficient in terms.items() if coefficient))


def serialize(matrix):
    return [[str(simp(matrix[i, j])) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


def main():
    program = Path(__file__).resolve()
    source = program.with_name('affine_obstruction_stage_output.json')
    data = json.loads(source.read_text())
    c = sp.prod(PARAMETERS)
    character = sp.Matrix(list(PARAMETERS) + [1/c])
    delta = character - sp.ones(7, 1)
    section = sp.eye(6).col_join(sp.zeros(1, 6))
    projection = sp.eye(6).row_join(-delta[:6, 0]/delta[6])
    e = sp.eye(6)
    boundary = sp.Matrix([[sp.prod(PARAMETERS[:i]) for i in range(6)]])
    basis = sp.Matrix.hstack(*[e[:, i] - boundary[i]*e[:, 0] for i in range(1, 6)],
                             e[:, 0])
    inverse = sp.Matrix.vstack(*[e[i, :] for i in range(1, 6)], boundary)
    verify(basis*inverse-e, 'basis_inverse')
    verify(inverse*basis-e, 'inverse_basis')
    boundary1 = boundary.subs(r, 1)
    basis1 = sp.Matrix.hstack(*[e[:, i]-boundary1[i]*e[:, 1] for i in range(2, 6)],
                              e[:, 1], e[:, 0]-e[:, 1])
    inverse1 = sp.Matrix.vstack(*[e[i, :] for i in range(2, 6)], boundary1, e[0, :])
    verify(basis1*inverse1-e, 'r1_basis_inverse')
    verify(inverse1*basis1-e, 'r1_inverse_basis')
    records = []
    for item in [a for a in data['records'] if a['index'] < 11]:
        action = sp.Matrix([[specialize(poly) for poly in row] for row in item['action_matrix']])
        verify(action*delta-delta, 'principal_vector_fixed')
        quotient = clean(projection*action*section)
        block = clean(inverse*quotient*basis)
        verify(block[5, :5], 'boundary_quotient')
        verify(delta[6]*(action*section*basis-section*basis*block)
               -delta*(action*section*basis)[6, :], 'cleared_principal_quotient')
        block1 = clean(inverse1*quotient.subs(r, 1)*basis1)
        for i in range(4, 6):
            for j in range(6):
                if i != j:
                    check(block1[i, j] == 0, 'r1_boundary_and_X1_quotients')
        core = block[:5, :5]
        core1 = block1[:4, :4]
        records.append({
            'index': item['index'], 'label': item['label'],
            'action_7': serialize(action), 'action_H1_6': serialize(quotient),
            'block_action_6': serialize(block), 'core_matrix_5': serialize(core),
            'boundary_character': str(block[5, 5]),
            'core_equals_r_identity': clean(core-r*sp.eye(5)) == sp.zeros(5),
            'core_equals_t_identity': clean(core-t*sp.eye(5)) == sp.zeros(5),
            'r1_block_action_6': serialize(block1), 'r1_core_matrix_4': serialize(core1),
            'r1_quotient_characters': [str(block1[i, i]) for i in range(4, 6)],
            'r1_core_equals_t_identity': clean(core1-t*sp.eye(4)) == sp.zeros(4),
            'r1_boundary_X1_ratio': str(simp(block1[4, 4]/block1[5, 5])),
        })
    result = {
        'status': 'EXPLORATORY_FULL_PRODUCT_ONE_EXACT_SOURCE_IDENTITIES',
        'producer_sha256': sha256(program.read_bytes()).hexdigest(),
        'source_sha256': sha256(source.read_bytes()).hexdigest(),
        'coefficient_ring': 'Z[r^+-1,s^+-1,t^+-1,u^+-1,v^+-1,w^+-1,(1-rstuvw)^-1]',
        'character': [str(x) for x in character],
        'principal_pivot_original_index': 7, 'principal_projection': serialize(projection),
        'principal_section': serialize(section), 'boundary_covector': serialize(boundary),
        'basis': serialize(basis), 'inverse_basis': serialize(inverse),
        'r1_basis': serialize(basis1), 'r1_inverse_basis': serialize(inverse1),
        'source_records': records, 'checks': CHECKS, 'check_total': sum(CHECKS.values()),
        'scope': 'Actual source matrices on the specified full product-one torus and its explicit r=1 refinement. This exploratory symbolic calculation has no independent original-word audit yet. No new affine-image or unrestricted marginal equality is asserted.',
    }
    output = program.with_name('affine_product_one_six_parameter_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'status': result['status'], 'checks': result['check_total'],
        'comparison_table': [{key: record[key] for key in [
            'index', 'label', 'boundary_character', 'core_equals_r_identity',
            'core_equals_t_identity', 'r1_quotient_characters',
            'r1_core_equals_t_identity', 'r1_boundary_X1_ratio']}
            for record in records],
        'output_sha256': sha256(output.read_bytes()).hexdigest(),
    }, indent=2))


if __name__ == '__main__':
    main()
