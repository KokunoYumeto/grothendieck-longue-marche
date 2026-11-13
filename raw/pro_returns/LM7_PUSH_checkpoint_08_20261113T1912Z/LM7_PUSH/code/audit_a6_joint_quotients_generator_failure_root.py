#!/usr/bin/env python3
"""Full isolated E54 presentation, module, common-map and target replay.

The independent new-chain replay runs separately. Every new presentation
evaluator also replays its supplied complete chain before evaluating it.
Only timing metadata and verified named input digests are separated from
mathematical comparison. All NPZ arrays must agree literally.
"""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
HASH_KEYS = {'input_sha256', 'source_input_sha256', 'exact_input_hashes'}
TIME_KEYS = {'seconds', 'total_seconds', 'elapsed_seconds'}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def mathematical(value):
    if isinstance(value, dict):
        return {key: (sorted(item) if key in HASH_KEYS else mathematical(item))
                for key, item in value.items() if key not in TIME_KEYS}
    if isinstance(value, list):
        return [mathematical(item) for item in value]
    return value


def verify_hashes(value, directory, records):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in HASH_KEYS:
                for name, expected in item.items():
                    assert digest(directory / name) == expected, (str(directory), name)
                    records.add(name)
            else:
                verify_hashes(item, directory, records)
    elif isinstance(value, list):
        for item in value:
            verify_hashes(item, directory, records)


def main():
    start = time.time()
    manifest_path = HERE / 'de_a6_gl_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    protected = {name: row['sha256'] for name, row in manifest['records'].items()}
    protected.update({name: row['sha256'] for name, row in manifest['documents'].items()})
    protected['code/de_a6_gl_manifest.json'] = digest(manifest_path)
    for name, expected in protected.items():
        assert digest(ROOT / name) == expected, ('frozen input', name)
    replay = HERE / 'root_a6_joint_quotient_replay'
    replay.mkdir(exist_ok=False)
    for name in manifest['records']:
        path = Path(name)
        assert path.parts[0] == 'code' and len(path.parts) == 2
        shutil.copy2(ROOT / name, replay / path.name)
    for stem in ('de_a6_gl_kernel', 'de_a6_gl_epikernels',
                 'de_a6_gl_central', 'de_a6_subgroup_checks'):
        with (replay / (stem + '_compile_root.out')).open('x') as log:
            run = subprocess.run(['g++', '-std=c++17', '-O3', stem + '.cpp', '-o', stem],
                                 cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, stem
    rows = []

    def execute(label, command, outputs):
        tick = time.time()
        for name in outputs:
            path = replay / name
            if path.exists():
                path.unlink()
        with (replay / (label + '_root_check.out')).open('x') as log:
            run = subprocess.run(command, cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, (label, run.returncode)
        comparisons = []
        for name in outputs:
            old, new = HERE / name, replay / name
            assert new.is_file(), ('missing regenerated output', name)
            if old.suffix == '.json':
                a, b = json.loads(old.read_text()), json.loads(new.read_text())
                declared = set()
                verify_hashes(a, HERE, declared)
                verify_hashes(b, replay, declared)
                assert mathematical(a) == mathematical(b), ('JSON', name)
                if name == 'de_a6_gl_prepare.json':
                    for directory, record in ((HERE, a), (replay, b)):
                        assert digest(directory / 'de_a6_gl_model.bin') == record['export_sha256']
                comparisons.append({'file': name, 'all_mathematical_records_equal': True,
                                    'own_location_hashes_verified': sorted(declared)})
            elif old.suffix == '.npz':
                with np.load(old) as a, np.load(new) as b:
                    assert set(a.files) == set(b.files), name
                    for key in a.files:
                        assert np.array_equal(a[key], b[key]), (name, key)
                    keys = sorted(a.files)
                comparisons.append({'file': name, 'all_arrays_literal': keys})
            else:
                assert old.read_bytes() == new.read_bytes(), ('literal output', name)
                comparisons.append({'file': name, 'literally_equal': True})
        row = {'program': label, 'exit_code': 0, 'all_comparisons_passed': True,
               'outputs': comparisons, 'seconds': round(time.time() - tick, 3)}
        rows.append(row)
        Path(__file__).with_suffix('.partial.json').write_text(
            json.dumps({'completed_steps': rows}, indent=2) + '\n')
        print(json.dumps({k: v for k, v in row.items() if k != 'outputs'}), flush=True)

    def py(stem, outputs=None):
        if outputs is None:
            outputs = [stem + '.json']
            if (HERE / (stem + '.npz')).is_file():
                outputs.append(stem + '.npz')
        execute(stem, [sys.executable, '-u', stem + '.py'], outputs)

    def cpp(label, stem, args, output):
        execute(label, [str(replay / stem), *args], [output])

    py('de_a6_a5_common_source', ['de_a6_a5_common_source.json',
       'de_a6_a5_common_source.npz', 'de_a6_a5_common_source.input'])
    py('de_a6_gl_prepare', ['de_a6_gl_prepare.json', 'de_a6_gl_model.bin'])
    cpp('complete_signed_kernel', 'de_a6_gl_kernel',
        ['de_a6_gl_model.bin', 'de_a6_a5_common_source.bin', 'de_a6_gl_kernel.json'],
        'de_a6_gl_kernel.json')
    py('de_a6_gl_kernel_replay')
    py('de_a6_gl_lower_chain_prepare', ['de_a6_gl_lower_chain_prepare.json',
       'de_a6_gl_lower_chain.npz', 'de_a6_gl_lower_chain.input', 'de_a6_gl_lower_chain_model.bin'])
    cpp('complete_lower_signed_kernel', 'de_a6_gl_kernel',
        ['de_a6_gl_lower_chain_model.bin', 'de_a6_gl_lower_chain.bin', 'de_a6_gl_lower_kernel.json'],
        'de_a6_gl_lower_kernel.json')
    py('de_a6_gl_lower_compare')
    py('de_a6_gl_epikernels_prepare', ['de_a6_gl_epikernels_prepare.json',
       'de_a6_gl_epikernels.npz', 'de_a6_gl_epikernels.input', 'de_a6_gl_A5_source.input'])
    cpp('complete_A6_epikernels', 'de_a6_gl_epikernels',
        ['de_a6_schreier_full_ordered.bin', 'de_a6_gl_epikernels.input', 'de_a6_gl_A6_factors.json'],
        'de_a6_gl_A6_factors.json')
    cpp('complete_A5_epikernels', 'de_a6_gl_epikernels',
        ['de_a6_gl_A5_source.bin', 'de_a6_gl_epikernels.input', 'de_a6_gl_A5_factors.json'],
        'de_a6_gl_A5_factors.json')
    py('de_a6_gl_presentation_gate')
    py('de_a6_gl_common_quotient')
    py('de_a6_gl_central_prepare', ['de_a6_gl_central_prepare.json',
       'de_a6_gl_central_prepare.npz', 'de_a6_gl_central_model.bin'])
    cpp('complete_central_pullback', 'de_a6_gl_central',
        ['de_a6_gl_central_model.bin', 'de_a6_schreier_residual_derived.bin', 'de_a6_gl_central.json'],
        'de_a6_gl_central.json')
    py('de_a6_gl_central_replay')
    py('de_a6_gl_central_signs')
    py('de_a6_gl_boundary')
    py('de_a6_gl_target_prepare', ['de_a6_gl_target_prepare.json',
       'de_a6_gl_target_prepare.npz', 'de_a6_gl_target.input'])
    cpp('complete_target_normality', 'de_a6_subgroup_checks',
        ['de_a6_gl_target_derived3.bin', 'de_a6_gl_target.input',
         'de_a6_gl_target_normal.json', 'normal'], 'de_a6_gl_target_normal.json')
    py('de_a6_gl_target_certificate')

    assert all(digest(ROOT / name) == expected for name, expected in protected.items())
    result = {'all_passed': True, 'steps': rows,
              'independent_complete_chain_audit': 'audit_a6_joint_chains_root.json',
              'original_artifacts_unchanged': True,
              'protected_sha256': protected, 'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print('ROOT_A6_JOINT_COMPLETE_QUOTIENTS_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
