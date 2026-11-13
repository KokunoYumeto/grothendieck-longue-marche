#!/usr/bin/env python3
"""Isolated literal replay of the independent D50 finite scalar covers."""
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
    started = time.monotonic()
    stem = 'bc_scalar_cover_count'
    protected = {stem + ext: digest(HERE / (stem + ext))
                 for ext in ('.py', '.json', '.out')}
    replay = HERE / 'root_scalar_cover_count_replay'
    replay.mkdir(exist_ok=False)
    shutil.copy2(HERE / (stem + '.py'), replay / (stem + '.py'))
    with (replay / (stem + '_root_check.out')).open('x') as out:
        run = subprocess.run([sys.executable, stem + '.py'], cwd=replay,
                             stdout=out, stderr=subprocess.STDOUT)
    assert run.returncode == 0
    a = json.loads((HERE / (stem + '.json')).read_text())
    b = json.loads((replay / (stem + '.json')).read_text())
    assert a == b and a['status'] == 'PASS'
    assert a['source_sha256'] == protected[stem + '.py']
    assert digest(replay / (stem + '.py')) == a['source_sha256']
    assert all(digest(HERE / name) == value for name, value in protected.items())
    result = {'all_passed': True, 'all_mathematical_JSON_literal': True,
              'Q8_scalar_phase_cases': sum(a['q8_projective_phase']['surface_cases'].values()),
              'noncentral_kernel_surface_cases': sum(a['binary_tetrahedral']['surface_cases'].values()),
              'pair_group_product_checks': a['binary_tetrahedral']['pair_group_quotient_product_checks'],
              'proper_subgroup_counts': a['proper_subgroups_and_mobius']['proper_subgroup_formula_cases'],
              'ordinary_Mobius_counts': a['proper_subgroups_and_mobius']['ordinary_mobius_epi_cases'],
              'literal_boundary_transports': a['proper_subgroups_and_mobius']['all_literal_boundary_transports'],
              'nonfaithful_representation_pullback_elements': a['nonfaithful_d8']['pullback_elements'],
              'complete_source_read': True, 'original_artifacts_unchanged': True,
              'protected_sha256': protected,
              'seconds': round(time.monotonic() - started, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
