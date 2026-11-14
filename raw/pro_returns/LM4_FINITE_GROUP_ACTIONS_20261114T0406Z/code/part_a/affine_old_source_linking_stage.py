"""Exact old-strand linking map for the retained eleven F23 source loops."""
from pathlib import Path
from itertools import combinations
from hashlib import sha256
import json
import sympy as sp


def main():
    producer = Path(__file__).resolve()
    source = producer.with_name('full_cross_source_stage')/'marginal_braids.json'
    data = json.loads(source.read_text())
    pairs = list(combinations(range(1, 8), 2))
    rows = []
    records = []
    for record in data['records'][:11]:
        order = list(range(1, 8))
        crossings = {pair: 0 for pair in pairs}
        for letter in record['old_braid']:
            i = abs(letter)-1
            pair = tuple(sorted(order[i:i+2]))
            crossings[pair] += 1 if letter > 0 else -1
            order[i], order[i+1] = order[i+1], order[i]
        assert order == list(range(1, 8))
        assert all(value % 2 == 0 for value in crossings.values())
        linking = [crossings[pair]//2 for pair in pairs]
        assert linking[0] == 0
        rows.append(linking)
        records.append({'source_index': record['index'], 'label': record['label'],
                        'linking': linking})
    matrix = sp.Matrix(rows)
    reduced, pivots = matrix.rref()
    output = {'status': 'EXACT_OLD_SOURCE_LINKING_RESEARCH_STAGE',
              'producer_sha256': sha256(producer.read_bytes()).hexdigest(),
              'input_sha256': sha256(source.read_bytes()).hexdigest(),
              'label_pairs': [list(pair) for pair in pairs], 'records': records,
              'rational_rank': matrix.rank(), 'pivot_columns': list(pivots),
              'rref': [[str(value) for value in reduced.row(i)] for i in range(11)],
              'scope': 'The literal old seven-strand F23 words and their signed pairwise linking coordinates. All have zero linking between the two fixed labels 0 and1. This does not determine their finite Gassner image.'}
    target = producer.with_name('affine_old_source_linking_stage_output.json')
    target.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'rank': output['rational_rank'], 'source_loops': 11,
                      'old_linking_coordinates': 21,
                      'fixed_first_pair_zero': True,
                      'output_sha256': sha256(target.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
