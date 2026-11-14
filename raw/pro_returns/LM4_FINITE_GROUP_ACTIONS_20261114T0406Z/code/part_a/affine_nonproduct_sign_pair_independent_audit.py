"""Independent literal-word and localized-row audit of the sign-pair rank.

No producer arithmetic is imported. Artin words are reconstructed using
generic crossed-homomorphism multiplication; all later arithmetic is
independent sparse integer Laurent arithmetic. Recorded divisions are
replayed by descending polynomial division and checked by multiplication.
"""
from pathlib import Path
from hashlib import sha256
import json


DIM = 7
ZERO = (0,)*DIM
UNIT = [tuple(int(i == j) for i in range(DIM)) for j in range(DIM)]
ONE = {ZERO: 1}
CHECKS = 0


def check(value, label):
    global CHECKS
    if not value:
        raise AssertionError(label)
    CHECKS += 1


def plus(*polys):
    result = {}
    for polynomial in polys:
        for exponent, coefficient in polynomial.items():
            value = result.get(exponent, 0)+coefficient
            if value:
                result[exponent] = value
            elif exponent in result:
                del result[exponent]
    return result


def negative(poly):
    return {exponent: -coefficient for exponent, coefficient in poly.items()}


def shifted(poly, exponent, coefficient=1):
    return {tuple(x+y for x, y in zip(power, exponent)): coefficient*value
            for power, value in poly.items()}


def times(left, right):
    result = {}
    for exponent, coefficient in left.items():
        result = plus(result, shifted(right, exponent, coefficient))
    return result


def read_poly(serial):
    result = {}
    for coefficient, exponent in serial:
        key = tuple(exponent)
        check(len(key) == DIM and isinstance(coefficient, int) and coefficient != 0,
              'serialized_integer_Laurent_monomial')
        check(key not in result, 'unique_serialized_monomial')
        result[key] = coefficient
    return result


def read_row(serial):
    return [read_poly(poly) for poly in serial]


def fundamental(row):
    return plus(*(plus(shifted(poly, UNIT[i]), negative(poly)) for i, poly in enumerate(row)))


def group_product(left, right):
    a, da = left
    b, db = right
    return tuple(x+y for x, y in zip(a, b)), [plus(x, shifted(y, a)) for x, y in zip(da, db)]


def group_inverse(value):
    exponent, derivative = value
    inverse_exponent = tuple(-x for x in exponent)
    return inverse_exponent, [shifted(poly, inverse_exponent, -1) for poly in derivative]


def literal_braid(word):
    identity = (ZERO, [{} for _ in range(DIM)])
    values = [(UNIT[i], [ONE if j == i else {} for j in range(DIM)]) for i in range(DIM)]+[identity]
    conjugators = [identity for _ in range(DIM+1)]
    labels = list(range(DIM+1))
    for letter in word:
        j = abs(letter)-1
        check(0 <= j < DIM, 'actual_eight_strand_braid_letter')
        x, y = values[j], values[j+1]
        cx, cy = conjugators[j], conjugators[j+1]
        if letter > 0:
            values[j] = group_product(group_product(x, y), group_inverse(x))
            values[j+1] = x
            conjugators[j] = group_product(x, cy)
            conjugators[j+1] = cx
        else:
            values[j] = y
            values[j+1] = group_product(group_product(group_inverse(y), x), y)
            conjugators[j] = cy
            conjugators[j+1] = group_product(group_inverse(y), cx)
        labels[j], labels[j+1] = labels[j+1], labels[j]
    check(labels == list(range(DIM+1)), 'actual_braid_is_pure')
    check([value[0] for value in values] == UNIT+[ZERO], 'all_character_values_return_to_original_labels')
    check(values[-1] == identity, 'erased_eighth_generator_is_identity')
    decoration = group_inverse(conjugators[-1])
    check(fundamental(decoration[1]) == plus({decoration[0]: 1}, negative(ONE)),
          'literal_decoration_Fox_identity')
    action = [group_product(group_product(decoration, value), group_inverse(decoration))[1]
              for value in values[:DIM]]
    for i, row in enumerate(action):
        check(fundamental(row) == {UNIT[i]: 1, ZERO: -1}, 'literal_source_action_Fox_identity')
    return decoration[0], decoration[1], action


def row_action(row, matrix):
    return [plus(*(times(row[k], matrix[k][j]) for k in range(DIM))) for j in range(DIM)]


def quadratic_parts(poly):
    even, odd = {}, {}
    for exponent, coefficient in poly.items():
        er = exponent[0]
        residue = er % 2
        key = ((er-residue)//2,)+exponent[1:]
        target = odd if residue else even
        target[key] = target.get(key, 0)+coefficient
    return ({e: c for e, c in even.items() if c}, {e: c for e, c in odd.items() if c})


def specialize(poly, indices):
    out = {}
    for exponent, coefficient in poly.items():
        key = tuple(0 if j in indices else e for j, e in enumerate(exponent))
        out[key] = out.get(key, 0)+coefficient
    return {e: c for e, c in out.items() if c}


def divide_difference(poly, index):
    groups = {}
    for exponent, coefficient in poly.items():
        key = exponent[:index]+exponent[index+1:]
        groups.setdefault(key, {})[exponent[index]] = coefficient
    quotient = {}
    for other, coefficients in groups.items():
        remainder = dict(coefficients)
        lower = min(remainder)
        for degree in range(max(remainder), lower, -1):
            leading = remainder.pop(degree, 0)
            if leading:
                qexp = other[:index]+(degree-1,)+other[index:]
                quotient[qexp] = quotient.get(qexp, 0)+leading
                remainder[degree-1] = remainder.get(degree-1, 0)+leading
        check(not any(remainder.values()), 'descending_difference_division_remainder')
    quotient = {e: c for e, c in quotient.items() if c}
    check(times(quotient, {UNIT[index]: 1, ZERO: -1}) == poly, 'difference_division_multiplication_inverse')
    return quotient


def normalization(row, operation, active):
    shift = tuple(operation['shift'])
    check(len(shift) == DIM, 'normalization_monomial_dimension')
    answer = [shifted(poly, shift) for poly in row]
    for index, field in [(0, 'R_minus_one_divisions'), (active, 'active_difference_divisions')]:
        count = operation[field]
        check(isinstance(count, int) and count >= 0, 'nonnegative_difference_division_count')
        for _ in range(count):
            answer = [divide_difference(poly, index) for poly in answer]
    twos = operation['two_divisions']
    check(isinstance(twos, int) and twos >= 0, 'nonnegative_power_of_two_division_count')
    for _ in range(twos):
        check(all(coefficient % 2 == 0 for poly in answer for coefficient in poly.values()),
              'exact_integer_division_by_two')
        old = answer
        answer = [{exponent: coefficient//2 for exponent, coefficient in poly.items()} for poly in old]
        check([{exponent: 2*coefficient for exponent, coefficient in poly.items()} for poly in answer] == old,
              'division_by_two_multiplication_inverse')
    return answer


def certify_unit(poly, witness, active):
    reduced = normalization([poly], witness['normalization'], active)[0]
    check(witness['sign'] in (-1, 1), 'unit_final_sign')
    check(reduced == {tuple(witness['final_monomial']): witness['sign']}, 'exact_localized_unit_identity')


def audit_chart(initial, chart):
    active = chart['active_deleted_index_zero_based']
    prescribed = {3: [], 4: [3], 5: [3, 4], 6: [3, 4, 5]}
    check(chart['specialized_to_one'] == prescribed[active], 'exact_ordered_character_chart')
    rows = [[specialize(poly, prescribed[active]) for poly in row] for row in initial]
    for operation in chart['operations']:
        index = operation['row']
        if operation['operation'] == 'normalize':
            rows[index] = normalization(rows[index], operation, active)
        else:
            check(operation['operation'] == 'eliminate_then_normalize', 'known_row_operation')
            pivot_index = operation['pivot_row']
            column = operation['column_zero_based']
            pivot = read_poly(operation['pivot_coefficient'])
            coefficient = read_poly(operation['old_coefficient'])
            check(rows[pivot_index][column] == pivot, 'current_pivot_coefficient_matches')
            check(rows[index][column] == coefficient, 'current_target_coefficient_matches')
            changed = [plus(times(pivot, a), negative(times(coefficient, b)))
                       for a, b in zip(rows[index], rows[pivot_index])]
            check(not changed[column], 'eliminated_entry_exactly_zero')
            rows[index] = normalization(changed, operation, active)
    columns, used_rows = [], []
    for pivot in chart['pivots']:
        index, column = pivot['row'], pivot['column_zero_based']
        check(index not in used_rows and column not in columns, 'distinct_pivot_row_and_column')
        check(all(not rows[index][prior] for prior in columns), 'triangular_pivot_row')
        coefficient = read_poly(pivot['coefficient'])
        check(rows[index][column] == coefficient, 'final_triangular_pivot_coefficient')
        certify_unit(coefficient, pivot['unit'], active)
        columns.append(column); used_rows.append(index)
    check(chart['single_pivot_count'] == len(columns), 'single_pivot_count_exact')
    for record in chart['remaining_rows']:
        check(record['row'] not in used_rows, 'remaining_row_is_not_a_pivot')
        check(rows[record['row']] == read_row(record['coefficients']), 'whole_remaining_row_matches')
    block = chart['terminal_two_by_two_block']
    if block is not None:
        indices, residual_columns = block['rows'], block['columns_zero_based']
        check(len(indices) == 2 and len(set(indices)) == 2 and not set(indices).intersection(used_rows),
              'terminal_block_uses_two_new_rows')
        check(residual_columns == [j for j in range(13) if j not in columns], 'terminal_block_exact_remaining_columns')
        check(all(not rows[index][column] for index in indices for column in columns), 'terminal_block_zero_in_prior_columns')
        entries = [read_row(row) for row in block['entries']]
        check(entries == [[rows[index][column] for column in residual_columns] for index in indices],
              'terminal_block_entries_from_actual_replayed_rows')
        aa, bb = entries[0]; cc, dd = entries[1]
        determinant = plus(times(aa, dd), negative(times(bb, cc)))
        check(determinant == read_poly(block['determinant']), 'terminal_block_signed_determinant')
        adjugate = [read_row(row) for row in block['adjugate']]
        check(adjugate == [[dd, negative(bb)], [negative(cc), aa]], 'terminal_block_actual_adjugate')
        for left, right in [(entries, adjugate), (adjugate, entries)]:
            for i in range(2):
                for j in range(2):
                    check(plus(*(times(left[i][k], right[k][j]) for k in range(2)))
                          == (determinant if i == j else {}), 'both_adjugate_inverse_identities')
        for i, result in enumerate(block['resulting_coordinate_rows']):
            actual = [plus(*(times(adjugate[i][k], rows[indices[k]][j]) for k in range(2))) for j in range(13)]
            check(actual == read_row(result), 'whole_adjugate_coordinate_row_matches')
            check(actual == [determinant if j == residual_columns[i] else {} for j in range(13)],
                  'adjugate_gives_unit_coordinate_row')
        certify_unit(determinant, block['unit'], active)
        columns += residual_columns
    check(len(columns) == chart['pivot_count'] == 13 and set(columns) == set(range(13)), 'all_thirteen_columns_certified')
    check(chart['status'] == 'FULL_RANK13', 'completed_chart_status')
    return {'active_deleted_index_zero_based': active, 'single_pivots': chart['single_pivot_count'],
            'terminal_block_rows': None if block is None else block['rows'], 'certified_rank': 13}


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    names = ['full_cross_source_stage/marginal_braids.json', 'affine_obstruction_stage_output.json',
             'affine_rank_one_certificate_stage_output.json', 'affine_nonproduct_sign_pair_rank_certificate_stage_output.json',
             'affine_nonproduct_sign_pair_rank_certificate_stage.py', 'affine_obstruction_stage.py',
             'affine_localized_rows_stage.py', 'affine_rank_one_certificate_stage.py']
    paths = [folder/name for name in names]
    braid_data, universal, source_rows, certificate = [json.loads(path.read_text()) for path in paths[:4]]
    hashes = {name: sha256(path.read_bytes()).hexdigest() for name, path in zip(names, paths)}
    check(universal['source_sha256'] == hashes[names[0]], 'universal_braid_input_binding')
    check(universal['producer_sha256'] == hashes['affine_obstruction_stage.py'], 'universal_producer_binding')
    check(source_rows['universal_derivation_input_sha256'] == hashes[names[1]], 'original_row_universal_input_binding')
    check(source_rows['producer_sha256'] == hashes['affine_rank_one_certificate_stage.py'], 'original_row_producer_binding')
    check(source_rows['row_arithmetic_helper_sha256'] == hashes['affine_localized_rows_stage.py'], 'original_row_helper_binding')
    check(certificate['input_sha256'] == hashes[names[2]], 'sign_certificate_original_row_binding')
    check(certificate['producer_sha256'] == hashes[names[4]], 'sign_certificate_producer_binding')
    helper_hashes = {Path(path).name: value for path, value in certificate['helper_bindings'].items()}
    check(helper_hashes == {name: hashes[name] for name in ['affine_obstruction_stage.py', 'affine_localized_rows_stage.py']},
          'both_recorded_arithmetic_helper_bindings')
    selected = [record for record in braid_data['records']
                if record['index'] < 11 or int(record['label'].split('_')[2]) == -1]
    check([record['index'] for record in selected] == [record['index'] for record in universal['records']],
          'exact_nineteen_actual_negative_sources_selected')
    old_actions, seeds, labels = {}, [], []
    for record, expected in zip(selected, universal['records']):
        exponent, seed, action = literal_braid(record['negative_braid'])
        check(list(exponent) == expected['u_character'], 'literal_decoration_character_matches')
        check(seed == read_row(expected['u_derivation_row']), 'literal_decoration_derivative_matches')
        if record['index'] < 11:
            check(action == [read_row(row) for row in expected['action_matrix']], 'literal_seven_coordinate_action_matches')
            old_actions[record['index']] = action
        else:
            check(exponent == UNIT[{0: 3, 2: 4, 3: 5, 4: 6}[int(record['label'].split('_')[1])]],
                  'actual_seed_deleted_character')
            seeds.append(seed); labels.append(record['label'])
    rows, row_labels = list(seeds), list(labels)
    source_indices = [2, 9, 8, 10, 1, 0, 7]
    check(source_rows['source_automorphism_indices'] == source_indices, 'exact_selected_old_source_order')
    old_labels = {record['index']: record['label'] for record in selected if record['index'] < 11}
    for index in source_indices:
        for seed, label in zip(seeds, labels):
            rows.append(row_action(seed, old_actions[index]))
            row_labels.append(label+' after '+old_labels[index])
    check(len(rows) == 64 and row_labels == source_rows['source_row_labels'], 'all_sixtyfour_actual_source_row_labels')
    check(rows == [read_row(row) for row in source_rows['source_rows']], 'all_sixtyfour_literal_source_rows_match')
    sign_rows = []
    for row in rows:
        parts = [quadratic_parts(poly) for poly in row]
        aa, bb = [p[0] for p in parts], [p[1] for p in parts]
        principal = plus(negative(bb[0]), aa[0],
                         *(times(bb[j], {UNIT[j]: 1, ZERO: -1}) for j in range(1, DIM)))
        check(not principal, 'exact_real_imaginary_principal_line_identity')
        sign_rows.append(bb+aa[1:])
    check([chart['active_deleted_index_zero_based'] for chart in certificate['charts']] == [3, 4, 5, 6],
          'all_four_ordered_charts_present')
    summaries = [audit_chart(sign_rows, chart) for chart in certificate['charts']]
    result = {'status': 'PASS_INDEPENDENT_LITERAL_WORD_SIGN_PAIR_RANK13_AUDIT',
              'checker': {'path': script.name, 'sha256': sha256(script.read_bytes()).hexdigest()},
              'input_bindings': [{'path': name, 'bytes': path.stat().st_size, 'sha256': hashes[name]}
                                  for name, path in zip(names, paths)],
              'literal_sources': len(selected), 'original_source_rows': len(rows),
              'charts': summaries, 'check_count': CHECKS,
              'arithmetic': 'Independent integer Laurent arithmetic; generic group multiplication for original Artin words; descending division with exact multiplication inverses; no producer arithmetic imports.',
              'scope': 'All four exact13-column original sign-pair row charts, including every original word, source conjugation, principal identity, localized row operation, pivot and terminal adjugate. The written proof supplies the field maps and all nonzero-divisor arguments.'}
    output = script.with_name('affine_nonproduct_sign_pair_independent_audit_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': CHECKS, 'charts': summaries,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2), flush=True)


if __name__ == '__main__':
    main()
