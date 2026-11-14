"""Exact F30 coefficient transport from the frozen universal source data."""
from hashlib import sha256
from pathlib import Path
import json


def transport_exponent(exponent):
    return tuple(exponent[i]-exponent[6] for i in range(6))


def transport_poly(poly):
    answer = {}
    for coefficient, exponent in poly:
        key = transport_exponent(exponent)
        answer[key] = answer.get(key, 0)+coefficient
    return [[coefficient, list(exponent)] for exponent, coefficient in sorted(answer.items())
            if coefficient]


def main():
    script = Path(__file__).resolve()
    source = script.with_name('affine_obstruction_stage_output.json')
    source_data = json.loads(source.read_text())
    selected = [0, 2, 7]
    records = []
    for index in selected:
        record = next(x for x in source_data['records'] if x['index'] == index)
        records.append({
            'index': index, 'label': record['label'], 'braid_length': record['braid_length'],
            'u_character': list(transport_exponent(record['u_character'])),
            'action_matrix': [[transport_poly(poly) for poly in row]
                              for row in record['action_matrix']],
        })
    basis = [
        ['-s', '-s*t', '-s*t*u', '-s*t*u*v', '-s*t*u*v*w', '1/r'],
        ['1', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'],
        ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0'],
    ]
    inverse = [
        ['0', '1', '0', '0', '0', '0'], ['0', '0', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '0', '0'], ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '1'],
        ['r', 'r*s', 'r*s*t', 'r*s*t*u', 'r*s*t*u*v', 'r*s*t*u*v*w'],
    ]
    result = {
        'status': 'EXACT_FULL_PRODUCT_ONE_FIRST_SCALAR_COEFFICIENT_TRANSPORT',
        'producer_sha256': sha256(script.read_bytes()).hexdigest(),
        'source': str(source), 'source_sha256': sha256(source.read_bytes()).hexdigest(),
        'coefficient_map': '(t1,...,t7)->(r,s,t,u,v,w,(r*s*t*u*v*w)^-1)',
        'coefficient_exponent_map': '(a1-a7,a2-a7,a3-a7,a4-a7,a5-a7,a6-a7)',
        'coefficient_ring': 'Z[r^+-1,s^+-1,t^+-1,u^+-1,v^+-1,w^+-1]',
        'principal_pivot_original_index': 1, 'quotient_original_indices': [2, 3, 4, 5, 6, 7],
        'basis': basis, 'inverse_basis': inverse, 'source_records': records,
        'scope': 'Exact candidate coefficient transport for the three original sources used in F30. The separate literal-word verifier establishes the identities needed by the proof.'
    }
    output = script.with_name('affine_product_one_first_scalar_field_stage_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'source_indices': selected,
                      'source_words': len(records),
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
