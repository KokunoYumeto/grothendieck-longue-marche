"""Literal deleted-first two-parameter specialization of the actual source.

The ring map is (t1,...,t7) -> (1,s,t,(s*t)^-1,1,1,1); principal pivot X4.
All operations below are exact over Z[s^+-1,t^+-1,(1-s*t)^-1].
This file records symbolic identities; it does not infer fieldwise ranks
from a numerical sample or replace the eleven actual source operators.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sympy as sp


s, t = sp.symbols('s t')
CHECKS = {}


def check(test, category):
    assert test, category
    CHECKS[category] = CHECKS.get(category, 0) + 1


def simplify(value):
    return sp.factor(sp.cancel(value))


def specialized(poly):
    terms = {}
    for coefficient, exponent in poly:
        key = exponent[1] - exponent[3], exponent[2] - exponent[3]
        terms[key] = terms.get(key, 0) + coefficient
    return sp.Add(*(coefficient * s**a * t**b
                    for (a, b), coefficient in terms.items() if coefficient))


def clean(matrix):
    return matrix.applyfunc(simplify)


def zero_matrix(matrix, category):
    for value in matrix:
        check(sp.cancel(value) == 0, category)


def serialized(matrix):
    return [[str(simplify(matrix[i, j])) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


def main():
    producer = Path(__file__).resolve()
    source = producer.with_name('affine_obstruction_stage_output.json')
    universal = json.loads(source.read_text())
    old = [r for r in universal['records'] if r['index'] < 11]
    seeds = [r for r in universal['records'] if r['index'] >= 11]
    check(len(old) == 11 and len(seeds) == 8, 'actual_source_count')
    character = sp.Matrix([1, s, t, 1/(s*t), 1, 1, 1])
    delta = character - sp.ones(7, 1)
    keep = [0, 1, 2, 4, 5, 6]
    projection, section = sp.zeros(6, 7), sp.zeros(7, 6)
    for j, i in enumerate(keep):
        projection[j, i] = 1
        projection[j, 3] = -delta[i]/delta[3]
        section[i, j] = 1
    zero_matrix(projection * section - sp.eye(6), 'principal_projection_section')
    boundary = sp.Matrix([[1, 1, s, 1, 1, 1]])
    line = sp.Matrix([0, 1, -1/s, 0, 0, 0])
    cocycle_line = section*line
    e = sp.eye(6)
    columns = [line, e[:, 1], e[:, 4] - e[:, 1],
               e[:, 3] - e[:, 1], e[:, 0] - e[:, 1],
               e[:, 5] - e[:, 1]]
    change = sp.Matrix.hstack(*columns)
    inverse_change = sp.Matrix.vstack(-s*e[2, :], boundary, e[4, :],
                                       e[3, :], e[0, :], e[5, :])
    zero_matrix(inverse_change * change - sp.eye(6), 'flag_inverse_change')
    zero_matrix(change * inverse_change - sp.eye(6), 'flag_change_inverse')
    records, actions, star = [], [], []
    for record in old:
        action = sp.Matrix([[specialized(p) for p in row]
                            for row in record['action_matrix']])
        zero_matrix(action * delta - delta, 'principal_line_fixed')
        quotient = clean(projection * action * section)
        flag = clean(inverse_change * quotient * change)
        for i in range(1, 6):
            for j in range(6):
                if i != j:
                    check(flag[i, j] == 0, 'only_first_row_extensions')
        u_scalar = s**(record['u_character'][1]-record['u_character'][3]) * \
            t**(record['u_character'][2]-record['u_character'][3])
        zero_matrix(boundary * quotient - u_scalar * boundary, 'actual_boundary_character')
        correction = simplify((action * cocycle_line)[3] / delta[3])
        zero_matrix(action * cocycle_line - flag[0, 0] * cocycle_line - correction * delta,
                    'actual_socle_cocycle_correction')
        actions.append(action)
        star.append(flag)
        records.append({'index': record['index'], 'label': record['label'],
                        'u_scalar': str(simplify(u_scalar)),
                        'socle_character': str(flag[0, 0]),
                        'diagonal': [str(flag[j, j]) for j in range(6)],
                        'extension_row': [str(flag[0, j]) for j in range(1, 6)],
                        'principal_correction': str(correction),
                        'action_7': serialized(action),
                        'action_H1_6': serialized(quotient),
                        'action_flag_6': serialized(flag)})
    seed_records = []
    seed_rows = {}
    for record in seeds:
        row = sp.Matrix([[specialized(p) for p in record['u_derivation_row']]])
        seed_rows[record['index']] = row
        scalar = s**(record['u_character'][1]-record['u_character'][3]) * \
            t**(record['u_character'][2]-record['u_character'][3])
        check(simplify((row * delta)[0] - (scalar-1)) == 0, 'seed_fundamental_identity')
        seed_records.append({'index': record['index'], 'label': record['label'],
                             'scalar': str(simplify(scalar)),
                             'socle_value': str(simplify((row*cocycle_line)[0]))})
    chosen = seed_rows[13]
    kappa = clean(chosen * (actions[2] - sp.eye(7)))
    kappa_next = clean(kappa * actions[2])
    zero_matrix(kappa * delta, 'kappa_kills_principals')
    zero_matrix(kappa_next * delta, 'source_kappa_kills_principals')
    kappa_value = simplify((kappa * cocycle_line)[0])
    kappa_next_value = simplify((kappa_next * cocycle_line)[0])
    check(simplify(kappa_next_value - star[2][0, 0] * kappa_value) == 0,
          'actual_socle_source_evaluation')
    commutator_rows = []
    for j in range(11):
        commutator = clean(star[4] * star[j] - star[j] * star[4])
        for r in range(1, 6):
            for c in range(6):
                check(commutator[r, c] == 0, 'commutator_image_in_socle')
        check(commutator[0, 0] == 0, 'commutator_kills_socle')
        row = list(commutator[0, 1:])
        if any(row):
            commutator_rows.append({'source_pair': [4, j], 'row': row})
    unique_rows = []
    seen = set()
    for record in commutator_rows:
        key = tuple(record['row'])
        if key not in seen:
            seen.add(key)
            unique_rows.append(record)
    minors = []
    for subset in combinations(range(len(unique_rows)), 5):
        matrix = sp.Matrix([unique_rows[j]['row'] for j in subset])
        determinant = simplify(matrix.det(method='domain-ge'))
        if determinant:
            minors.append({'source_pairs': [unique_rows[j]['source_pair'] for j in subset],
                           'determinant': str(determinant)})
    result = {
        'status': 'EXACT_DELETED_FIRST_TWO_PARAMETER_SOURCE_IDENTITIES',
        'producer_sha256': sha256(producer.read_bytes()).hexdigest(),
        'source_sha256': sha256(source.read_bytes()).hexdigest(),
        'coefficient_ring': 'Z[s^+-1,t^+-1,(1-s*t)^-1]',
        'character': [str(x) for x in character],
        'principal_pivot': 4, 'quotient_original_indices': [1,2,3,5,6,7],
        'principal_projection': serialized(projection),
        'principal_section': serialized(section),
        'boundary_covector': serialized(boundary),
        'socle_line_vector': serialized(line),
        'flag_change': serialized(change), 'flag_inverse': serialized(inverse_change),
        'source_records': records, 'seed_records': seed_records,
        'kappa_word': 'B_2(u_(cross_0_-1_1))*u_(cross_0_-1_1)^-1',
        'kappa_row': serialized(kappa), 'source_kappa_row': serialized(kappa_next),
        'kappa_socle_value': str(kappa_value), 'source_kappa_socle_value': str(kappa_next_value),
        'commutator_rows': [{'source_pair': r['source_pair'],
                             'row': [str(x) for x in r['row']]} for r in unique_rows],
        'nonzero_five_by_five_commutator_minors': minors,
        'checks': CHECKS, 'check_total': sum(CHECKS.values()),
        'scope': 'Exact identities on the specified two-parameter character locus. Fieldwise essentiality, character separation and marginal image consequences require analysis of the displayed polynomial factors; they are not inferred from numerical samples.'}
    output = producer.with_name('affine_deleted_first_two_parameter_stage_output.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'checks': result['check_total'],
                      'source_table': [{k: r[k] for k in ['index', 'diagonal', 'extension_row', 'principal_correction']}
                                       for r in records],
                      'seed_records': seed_records,
                      'kappa_socle_value': str(kappa_value),
                      'source_kappa_socle_value': str(kappa_next_value),
                      'commutator_rows': result['commutator_rows'],
                      'nonzero_minors': minors,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
