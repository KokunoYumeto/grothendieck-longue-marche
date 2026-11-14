#!/usr/bin/env python3
"""Isolated exact replay of the characteristic weight-five Magnus targets."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    start = time.time()
    stem = 'a_weight5_characteristic'
    names = [stem + suffix for suffix in ('.py', '.json', '.out')]
    protected = {name: digest(HERE / name) for name in names}
    replay = HERE / 'root_weight5_characteristic_replay'
    replay.mkdir(exist_ok=False)
    shutil.copy2(HERE / (stem + '.py'), replay / (stem + '.py'))
    with (replay / (stem + '_root_check.out')).open('x') as log:
        proc = subprocess.run([sys.executable, str(replay / (stem + '.py'))],
                              cwd=replay, stdout=log, stderr=subprocess.STDOUT)
    assert proc.returncode == 0
    original = json.loads((HERE / (stem + '.json')).read_text())
    repeated = json.loads((replay / (stem + '.json')).read_text())
    assert original == repeated
    assert digest(HERE / (stem + '.json')) == digest(replay / (stem + '.json'))
    assert [row['n'] for row in original['executed_precisions']] == [1, 2]
    for row in original['executed_precisions']:
        n = row['n']
        assert row['actual_group_order'] == 5 ** (17 * n + 2)
        assert row['diagonal_order'] == 5 ** (2 * n + 2)
        assert row['derived_rank'] == 15
        assert row['centralizer_diagonal_exponents']['y_exponent'] == [0]
        assert len(row['module_monomial_words']) == 15
        assert len(row['special_basis_maps']) == 3
        assert len(row['geometric_symmetry_with_inner_corrections']) == 6
    assert all(digest(HERE / name) == value for name, value in protected.items())
    result = {
        'status': 'ROOT_CHARACTERISTIC_WEIGHT_FIVE_REPLAY_PASS',
        'all_passed': True,
        'entire_JSON_byte_identical': True,
        'all_original_artifacts_unchanged': True,
        'executed_precisions': [1, 2],
        'group_orders': [row['actual_group_order']
                         for row in original['executed_precisions']],
        'protected_sha256': protected,
        'seconds': round(time.time() - start, 3),
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
