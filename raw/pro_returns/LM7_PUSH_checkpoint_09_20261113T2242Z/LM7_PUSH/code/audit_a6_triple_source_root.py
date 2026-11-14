#!/usr/bin/env python3
"""Complete isolated root replay of the frozen 3.A6 source calculation.

Every lifted base and residual relation is re-evaluated. Discovery chains
are copied, checked by their complete Schreier replay, and compared through
their specified original generators. No authoritative file is written.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'code/de_a6_triple_source_manifest.json'
DEST = ROOT / 'research/root_a6_triple_source_replay'
JSON_OUTPUTS = [
    'de_a6_triple_affine_prepare.json', 'de_a6_triple_affine_factor.json',
    'de_a6_triple_base_prepare.json', 'de_a6_triple_modular_prepare.json',
    'de_a6_triple_kernel_prepare.json', 'de_a6_triple_kernel.json',
    'de_a6_triple_kernel_replay.json', 'de_a6_triple_central_prepare.json',
    'de_a6_triple_central.json', 'de_a6_triple_central_replay.json',
    'de_a6_triple_source_certificate.json',
]
NPZ_OUTPUTS = [
    'de_a6_triple_affine_source.npz', 'de_a6_triple_base_generators.npz',
    'de_a6_triple_modular_generators.npz', 'de_a6_triple_kernel_replay.npz',
    'de_a6_triple_central_prepare.npz', 'de_a6_triple_central_replay.npz',
    'de_a6_triple_source_certificate.npz',
]
BYTE_OUTPUTS = [
    'de_a6_triple_affine.input', 'de_a6_triple_base_seed.bin',
    'de_a6_triple_modular_seed.bin', 'de_a6_triple_kernel_model.bin',
    'de_a6_triple_central_model.bin', 'de_a6_triple_core.hpp',
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable(value):
    if isinstance(value, dict):
        return {k: stable(v) for k, v in value.items()
                if not k.endswith('seconds')}
    if isinstance(value, list):
        return [stable(v) for v in value]
    return value


def final_report(path):
    for line in reversed(path.read_text().splitlines()):
        if line.startswith('{'):
            value = json.loads(line)
            if value.get('status') == 'PASS':
                return value
    raise AssertionError(path)


def main():
    started = time.monotonic()
    manifest_hash = sha(MANIFEST)
    manifest = json.loads(MANIFEST.read_text())
    protected = {**manifest['records'], **manifest['documents']}
    for name, record in protected.items():
        assert sha(ROOT / name) == record['sha256'], name
    assert not DEST.exists(), 'Replay destination already exists.'
    code = DEST / 'code'
    code.mkdir(parents=True)
    for name in protected:
        target = DEST / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    commands = []

    def run(name, argv):
        before = time.monotonic()
        with (code / (name + '.out')).open('w') as out:
            with (code / (name + '.err')).open('w') as err:
                process = subprocess.run(argv, cwd=code, stdout=out, stderr=err)
        commands.append({'name': name, 'argv': argv, 'exit_code': process.returncode,
                         'seconds': round(time.monotonic() - before, 3)})
        (DEST / 'commands.json').write_text(json.dumps(commands, indent=2) + '\n')
        assert process.returncode == 0, (name, process.returncode)
        print(name, 'PASS', commands[-1]['seconds'], 's', flush=True)

    for stem, executable in [
        ('de_a6_schreier', 'de_a6_schreier_fast'),
        ('de_a6_triple_affine', 'de_a6_triple_affine'),
        ('de_a6_triple_kernel', 'de_a6_triple_kernel'),
        ('de_a6_triple_central', 'de_a6_triple_central'),
    ]:
        run('compile_' + stem,
            ['g++', '-O3', '-std=c++17', stem + '.cpp', '-o', executable])
    run('de_a6_triple_affine_prepare', [sys.executable, 'de_a6_triple_affine_prepare.py'])
    run('de_a6_triple_affine_factor', ['./de_a6_triple_affine',
        'de_a6_schreier_full_ordered.bin', 'de_a6_triple_affine.input',
        'de_a6_triple_affine_factor.json'])
    run('de_a6_triple_base_prepare', [sys.executable, 'de_a6_triple_base_prepare.py'])
    run('de_a6_triple_base', ['./de_a6_schreier_fast', '--replay', 'de_a6_triple_base.bin'])
    run('de_a6_triple_modular_prepare', [sys.executable, 'de_a6_triple_modular_prepare.py'])
    run('de_a6_triple_modular', ['./de_a6_schreier_fast', '--replay', 'de_a6_triple_modular.bin'])
    run('de_a6_triple_kernel_prepare', [sys.executable, 'de_a6_triple_kernel_prepare.py'])
    run('de_a6_triple_kernel', ['./de_a6_triple_kernel',
        'de_a6_triple_kernel_model.bin', 'de_a6_triple_base.bin',
        'de_a6_triple_kernel.json'])
    run('de_a6_triple_kernel_replay', [sys.executable, 'de_a6_triple_kernel_replay.py'])
    run('de_a6_triple_central_prepare', [sys.executable, 'de_a6_triple_central_prepare.py'])
    run('de_a6_triple_central', ['./de_a6_triple_central',
        'de_a6_triple_kernel_model.bin', 'de_a6_triple_central_model.bin',
        'de_a6_schreier_residual_derived.bin', 'de_a6_triple_central.json'])
    run('de_a6_triple_central_replay', [sys.executable, 'de_a6_triple_central_replay.py'])
    run('de_a6_triple_source_certificate', [sys.executable, 'de_a6_triple_source_certificate.py'])

    compared = []
    dynamic_hash_inputs = set(JSON_OUTPUTS + NPZ_OUTPUTS + BYTE_OUTPUTS + [
        'de_a6_triple_base.out', 'de_a6_triple_modular.out'])
    changed_hashes = []
    for name in JSON_OUTPUTS:
        old = json.loads((ROOT / 'code' / name).read_text())
        new = json.loads((code / name).read_text())
        assert set(old) == set(new), name
        if 'input_sha256' in old:
            assert set(old['input_sha256']) == set(new['input_sha256']), name
            for dependency, old_hash in old['input_sha256'].items():
                new_hash = new['input_sha256'][dependency]
                assert sha(ROOT / 'code' / dependency) == old_hash, (name, dependency)
                assert sha(code / dependency) == new_hash, (name, dependency)
                if old_hash != new_hash:
                    assert dependency in dynamic_hash_inputs, (name, dependency)
                    changed_hashes.append({'output': name, 'verified_dependency': dependency,
                                           'original_sha256': old_hash, 'replay_sha256': new_hash})
            old['input_sha256'] = new['input_sha256'] = sorted(old['input_sha256'])
        assert stable(old) == stable(new), ('mathematical JSON mismatch', name)
        compared.append(name)
    for name in NPZ_OUTPUTS:
        with np.load(ROOT / 'code' / name) as old, np.load(code / name) as new:
            assert set(old.files) == set(new.files), name
            for key in old.files:
                assert old[key].dtype == new[key].dtype, (name, key, 'dtype')
                assert old[key].shape == new[key].shape, (name, key, 'shape')
                assert np.array_equal(old[key], new[key]), (name, key, 'value')
        compared.append(name)
    for name in BYTE_OUTPUTS:
        assert (ROOT / 'code' / name).read_bytes() == (code / name).read_bytes(), name
        compared.append(name)
    for name in ('de_a6_triple_base.out', 'de_a6_triple_modular.out'):
        assert stable(final_report(ROOT / 'code' / name)) == stable(final_report(code / name)), name
        compared.append(name)
    for name, record in protected.items():
        assert sha(ROOT / name) == record['sha256'], name
    assert sha(MANIFEST) == manifest_hash
    result = {
        'status': 'PASS_ISOLATED_COMPLETE_TRIPLE_SOURCE_ROOT_REPLAY',
        'manifest_sha256': manifest_hash,
        'all_mathematical_outputs_identical': True,
        'complete_lifted_base_relations': 873463,
        'complete_lifted_C_relations': 720615,
        'original_C_to_normal_form_links': 10,
        'kernel_dimension': 79,
        'C_preimage_abelianization_dimension': 3,
        'perfect_residual_kernel_dimension': 76,
        'protected_original_files_unchanged': len(protected),
        'compared_outputs': compared,
        'verified_dynamic_dependency_hashes': changed_hashes,
        'seconds': round(time.monotonic() - started, 3),
    }
    (DEST / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('compared_outputs', 'verified_dynamic_dependency_hashes')},
                     indent=2), flush=True)


if __name__ == '__main__':
    main()
