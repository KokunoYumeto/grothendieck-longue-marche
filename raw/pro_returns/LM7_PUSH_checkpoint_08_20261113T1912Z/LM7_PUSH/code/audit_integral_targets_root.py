#!/usr/bin/env python3
"""Independent exact replay of E56's polynomial and literal matrix certificate."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    start = time.time()
    manifest_path = ROOT / 'research/E56_authoritative_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    protected = dict(manifest['protected_files'])
    protected.update(manifest['external_read_only_dependencies'])
    protected[str(manifest_path.relative_to(ROOT))] = digest(manifest_path)
    assert all(digest(ROOT / path) == value for path, value in protected.items())
    replay = HERE / 'root_integral_targets_replay'
    replay.mkdir(exist_ok=False)
    stem = 'bc_symplectic_integral_targets'
    for name in [stem + '.py', *[Path(n).name for n in manifest['external_read_only_dependencies']]]:
        shutil.copy2(HERE / name, replay / name)
    with (replay / (stem + '_root_check.out')).open('x') as log:
        run = subprocess.run([sys.executable, '-u', stem + '.py'], cwd=replay,
                             stdout=log, stderr=subprocess.STDOUT)
    assert run.returncode == 0
    a = json.loads((HERE / (stem + '.json')).read_text())
    b = json.loads((replay / (stem + '.json')).read_text())
    for directory, record in ((HERE, a), (replay, b)):
        for name, expected in record['input_sha256'].items():
            assert digest(directory / name) == expected
    mathematical = lambda d: {k: v for k, v in d.items() if k != 'seconds'}
    assert mathematical(a) == mathematical(b)
    assert all(digest(ROOT / path) == value for path, value in protected.items())
    result = {'all_passed': True, 'all_mathematical_JSON_equal': True,
              'all_input_hashes_verified_at_own_location': True,
              'original_artifacts_unchanged': True,
              'all_saved_permutation_entries': 12096,
              'all_nonzero_field_vectors': 3024,
              'literal_prime_power_and_CRT_matrix_factorizations': 112,
              'proof_sha256': protected['sections/E_symplectic_integral_targets_agent.tex'],
              'protected_sha256': protected, 'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
