"""Exact original-row test of the specific quadratic sign candidate in F49."""
from pathlib import Path
from hashlib import sha256
import json


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    rows_path = folder/'affine_rank_one_certificate_stage_output.json'
    actions_path = folder/'affine_obstruction_stage_output.json'
    traces_path = folder/'affine_nonproduct_general_rank_one_pairings_stage_output.json'
    rows, actions, traces = [json.loads(p.read_text()) for p in [rows_path, actions_path, traces_path]]
    p, square = 7, 5
    one, zero, r = (1, 0), (0, 0), (0, 1)

    def add(a, b):
        return ((a[0]+b[0]) % p, (a[1]+b[1]) % p)

    def mul(a, b):
        return ((a[0]*b[0]+square*a[1]*b[1]) % p, (a[0]*b[1]+a[1]*b[0]) % p)

    def power(a, exponent):
        if exponent < 0:
            denominator = pow((a[0]*a[0]-square*a[1]*a[1]) % p, -1, p)
            a = (a[0]*denominator % p, -a[1]*denominator % p)
            exponent = -exponent
        answer = one
        while exponent:
            if exponent & 1:
                answer = mul(answer, a)
            a = mul(a, a)
            exponent >>= 1
        return answer

    character = [r, (4, 0), (2, 0), one, one, one, (4, 0)]
    h = one
    for value in character:
        h = mul(h, value)
    assert h == (0, 4) and h == mul((-1 % p, 0), power(r, -1))
    assert mul(r, power(h, -1)) == (2, 0)

    def evaluate(poly, scalars=character):
        answer = zero
        for coefficient, exponent in poly:
            value = (coefficient % p, 0)
            for scalar, degree in zip(scalars, exponent):
                value = mul(value, power(scalar, degree))
            answer = add(answer, value)
        return answer

    def echelon(matrix):
        result = [[a % p for a in row] for row in matrix]
        pivots = []
        for col in range(14):
            selected = next((i for i in range(len(pivots), len(result)) if result[i][col]), None)
            if selected is None:
                continue
            dest = len(pivots)
            result[dest], result[selected] = result[selected], result[dest]
            scale = pow(result[dest][col], -1, p)
            result[dest] = [scale*a % p for a in result[dest]]
            for i in range(len(result)):
                if i != dest and result[i][col]:
                    coefficient = result[i][col]
                    result[i] = [(a-coefficient*b) % p for a, b in zip(result[i], result[dest])]
            pivots.append(col)
        return result[:len(pivots)], pivots

    evaluated = [[evaluate(poly) for poly in row] for row in rows['source_rows']]
    linear = [[value[1] for value in row]+[value[0] for value in row] for row in evaluated]
    principal = [(value[0]-1) % p for value in character]+[value[1] for value in character]
    assert all(sum(a*b for a, b in zip(row, principal)) % p == 0 for row in linear)
    basis, pivots = echelon(linear)
    initial_rank = len(basis)
    source_actions = []
    for record in actions['records']:
        if record['index'] >= 11:
            continue
        matrix = [[evaluate(poly) for poly in row] for row in record['action_matrix']]
        integer_matrix = [[value[0] for value in row]+[square*value[1] % p for value in row]
                          for row in matrix]+[[value[1] for value in row]+[value[0] for value in row]
                                              for row in matrix]
        assert [sum(a*b for a, b in zip(row, principal)) % p for row in integer_matrix] == principal
        source_actions.append(integer_matrix)
    rounds = []
    while True:
        combined = list(basis)
        for matrix in source_actions:
            combined += [[sum(row[k]*matrix[k][j] for k in range(14)) % p for j in range(14)]
                         for row in basis]
        next_basis, next_pivots = echelon(combined)
        rounds.append(len(next_basis))
        stable = len(next_basis) == len(basis)
        basis, pivots = next_basis, next_pivots
        if stable:
            break
        assert len(rounds) <= 14
    kernel = []
    for free in [j for j in range(14) if j not in pivots]:
        vector = [0]*14
        vector[free] = 1
        for row, pivot in zip(basis, pivots):
            vector[pivot] = -row[free] % p
        assert all(sum(a*b for a, b in zip(row, vector)) % p == 0 for row in basis)
        kernel.append(vector)
    chart = [r, h]+character[2:]
    trace_values = {str(record['index']): evaluate(record['exact_laurent_coefficients'], chart)
                    for record in traces['records']}
    result = {
        'status': 'EXACT_SPECIFIC_F49_SIGN_CANDIDATE_TEST',
        'producer_sha256': sha256(script.read_bytes()).hexdigest(),
        'inputs': {str(path): sha256(path.read_bytes()).hexdigest() for path in [rows_path, actions_path, traces_path]},
        'field': 'F7[r]/(r^2-5)', 'coordinate_pair': '[constant, coefficient_of_r]',
        'original_character': character, 'h': h, 'ratio_r_over_h': [2, 0],
        'initial_actual_64_row_rank': initial_rank, 'source_closure_ranks': rounds,
        'final_rank': len(basis), 'principal_vector': principal, 'kernel_basis': kernel,
        'all_eleven_actual_rank_one_traces': trace_values,
        'scope': 'Exact test of this one original character and its sign conjugate. Row operations and actual source closure preserve the necessary imaginary restriction equations. No other field or parameter point is covered.'}
    output = script.with_name('affine_nonproduct_f49_specific_sign_candidate_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)
    print(json.dumps({'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
