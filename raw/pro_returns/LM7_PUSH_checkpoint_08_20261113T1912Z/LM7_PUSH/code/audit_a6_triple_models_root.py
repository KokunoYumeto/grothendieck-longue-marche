#!/usr/bin/env python3
"""Isolated complete replay of the frozen central-three A6 cover/model."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    started = time.monotonic()
    manifest_path = HERE / 'de_a6_triple_models_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    assert manifest['files'] == len(manifest['records']) == 16
    protected = {name: record['sha256'] for name, record in manifest['records'].items()}
    protected[manifest_path.name] = digest(manifest_path)
    assert all(digest(HERE / name) == value for name, value in protected.items())
    replay = HERE / 'root_a6_triple_models_replay'
    replay.mkdir(exist_ok=False)
    for name in protected:
        shutil.copy2(HERE / name, replay / name)
    steps = []
    for stem in ('de_a6_triple_cover', 'de_a6_triple_model'):
        before = time.monotonic()
        with (replay / (stem + '_root_check.out')).open('x') as out, \
                (replay / (stem + '_root_check.err')).open('x') as err:
            run = subprocess.run([sys.executable, stem + '.py'], cwd=replay,
                                 stdout=out, stderr=err)
        assert run.returncode == 0, (stem, run.returncode)
        a = json.loads((HERE / (stem + '.json')).read_text())
        b = json.loads((replay / (stem + '.json')).read_text())
        for directory, record in ((HERE, a), (replay, b)):
            for name, expected in record['source_sha256'].items():
                assert digest(directory / name) == expected
        assert {k: v for k, v in a.items() if k != 'seconds'} == {
            k: v for k, v in b.items() if k != 'seconds'}
        arrays = []
        with np.load(HERE / (stem + '.npz'), allow_pickle=False) as original, \
                np.load(replay / (stem + '.npz'), allow_pickle=False) as current:
            assert set(original.files) == set(current.files)
            for key in sorted(original.files):
                x, y = original[key], current[key]
                assert x.shape == y.shape and x.dtype == y.dtype
                assert np.array_equal(x, y), (stem, key)
                arrays.append(key)
        steps.append({'program': stem, 'exit_code': run.returncode,
                      'all_mathematical_JSON_equal': True,
                      'literal_arrays': arrays,
                      'all_own_location_hashes_verified': True,
                      'seconds': round(time.monotonic() - before, 3)})
    assert all(digest(HERE / name) == value for name, value in protected.items())
    result = {'all_passed': True, 'complete_root_read_of_both_new_programs': True,
              'steps': steps, 'original_artifacts_unchanged': True,
              'protected_sha256': protected,
              'scope': 'Exact cover, automorphism, universal free image and Ferrari model; source fibre still under calculation',
              'seconds': round(time.monotonic() - started, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
