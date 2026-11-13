#!/usr/bin/env python3
"""Isolated eight-program replay of the complete E47 integral tower."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time
import traceback
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
INPUTS = [
    'bc_fermat_class_two_integral_kernel.npz',
    'bc_fermat_class_two_3adic_norms.npz',
    'bc_fermat_class_two_3adic_tower.json',
    'bc_fermat_class_three_norms.npz',
    'bc_fermat_class_three_tower_comparison.json',
]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def mathematical(value):
    if isinstance(value, dict):
        return {k: mathematical(v) for k, v in value.items() if k != 'elapsed_seconds'}
    if isinstance(value, list):
        return [mathematical(v) for v in value]
    return value


def main():
    start = time.time()
    manifest = json.loads((ROOT / 'research/E47_authoritative_manifest.json').read_text())
    for name, info in manifest['files'].items():
        assert digest(ROOT / name) == info['sha256']
        assert (ROOT / name).stat().st_size == info['bytes']
    protected = {Path(n).name: digest(ROOT / n) for n in manifest['files']}
    protected.update({n: digest(HERE / n) for n in INPUTS})
    replay = HERE / 'root_integral_class_three_replay'
    replay.mkdir(exist_ok=False)
    copied_python = {}
    for path in HERE.glob('*.py'):
        shutil.copy2(path, replay / path.name)
        copied_python[path.name] = digest(path)
    for name in INPUTS:
        shutil.copy2(HERE / name, replay / name)
    result = {'all_passed': False, 'programs': [],
              'protected_sha256': protected, 'copied_python_sha256': copied_python,
              'ignored_JSON_field': 'elapsed_seconds'}
    try:
        for relative in manifest['replay_order']:
            name = Path(relative).name
            stem = Path(name).stem
            row = {'program': name}
            with (replay / (stem + '_root_check.out')).open('x') as log:
                proc = subprocess.run([sys.executable, '-u', str(replay / name)],
                                      cwd=replay, stdout=log, stderr=subprocess.STDOUT)
            row['exit_code'] = proc.returncode
            result['programs'].append(row)
            assert proc.returncode == 0, name
            original = json.loads((HERE / (stem + '.json')).read_text())
            repeated = json.loads((replay / (stem + '.json')).read_text())
            assert mathematical(original) == mathematical(repeated), stem + ': JSON'
            row['all_mathematical_JSON_entries_equal'] = True
            arrayfile = HERE / (stem + '.npz')
            if arrayfile.exists():
                with np.load(arrayfile) as a, np.load(replay / arrayfile.name) as b:
                    assert set(a.files) == set(b.files), stem + ': NPZ names'
                    row['array_shapes'] = {}
                    for key in a.files:
                        assert np.array_equal(a[key], b[key]), (stem, key)
                        row['array_shapes'][key] = list(a[key].shape)
                row['all_NPZ_arrays_equal'] = True
            print('PASS', name, flush=True)
        result['all_passed'] = True
    except Exception as exc:
        result['exception'] = repr(exc)
        result['traceback'] = traceback.format_exc()
        raise
    finally:
        result['original_artifacts_unchanged'] = all(
            digest(HERE / n) == h for n, h in protected.items())
        result['seconds'] = round(time.time() - start, 3)
        Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps({k: v for k, v in result.items() if k not in
                         ('programs', 'protected_sha256', 'copied_python_sha256')}, indent=2), flush=True)
        assert result['original_artifacts_unchanged']


if __name__ == '__main__':
    main()
