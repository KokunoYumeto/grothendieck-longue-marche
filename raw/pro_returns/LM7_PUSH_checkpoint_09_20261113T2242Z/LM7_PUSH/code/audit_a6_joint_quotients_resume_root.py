#!/usr/bin/env python3
"""Finish the E54 isolated audit after proving the exact generator maps.

The initial failed run and its entire directory remain unchanged. Its
eleven completed steps are re-compared; the twelfth uses the explicit
mutual signed-word maps under the identity ambient permutation action.
The remaining eight programs run in a fresh isolated directory.
"""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time
import numpy as np
from audit_a6_joint_quotients_generator_failure_root import digest, mathematical, verify_hashes

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def compare(name, directory, identity_certificate=None):
    old, new = HERE / name, directory / name
    assert new.is_file(), name
    if old.suffix == '.json':
        a, b = json.loads(old.read_text()), json.loads(new.read_text())
        declared = set()
        verify_hashes(a, HERE, declared)
        verify_hashes(b, directory, declared)
        assert mathematical(a) == mathematical(b), ('JSON', name)
        if name == 'de_a6_gl_prepare.json':
            for place, record in ((HERE, a), (directory, b)):
                assert digest(place / 'de_a6_gl_model.bin') == record['export_sha256']
        return {'file': name, 'all_mathematical_records_equal': True,
                'own_location_hashes_verified': sorted(declared)}
    if old.suffix == '.npz':
        literal, maps = [], []
        with np.load(old) as a, np.load(new) as b:
            assert set(a.files) == set(b.files), name
            for key in a.files:
                if identity_certificate is not None and key in (
                        'm15_Fprime_generators', 'm30_Fprime_generators'):
                    assert name == 'de_a6_gl_common_quotient.npz'
                    record = next(r for r in identity_certificate['exact_identity_morphisms']
                                  if r['array'] == key)
                    assert np.array_equal(a[key], record['old_generators'])
                    assert np.array_equal(b[key], record['replayed_generators'])
                    for targets, gens, words in (
                        (a[key], b[key], record['old_generators_as_signed_words_in_replayed']),
                        (b[key], a[key], record['replayed_generators_as_signed_words_in_old'])):
                        inverse = np.argsort(gens, axis=1)
                        assert len(targets) == len(words)
                        for target, word in zip(targets, words):
                            value = np.arange(len(target))
                            for letter in word:
                                row = gens[letter - 1] if letter > 0 else inverse[-letter - 1]
                                value = row[value]
                            assert np.array_equal(value, target)
                    maps.append(key)
                else:
                    assert np.array_equal(a[key], b[key]), (name, key)
                    literal.append(key)
        return {'file': name, 'all_arrays_literal': sorted(literal),
                'exact_mutual_identity_word_maps': sorted(maps)}
    assert old.read_bytes() == new.read_bytes(), name
    return {'file': name, 'literally_equal': True}


def main():
    started = time.time()
    manifest_path = HERE / 'de_a6_gl_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    protected = {name: row['sha256'] for name, row in manifest['records'].items()}
    protected.update({name: row['sha256'] for name, row in manifest['documents'].items()})
    protected['code/de_a6_gl_manifest.json'] = digest(manifest_path)
    assert all(digest(ROOT / name) == value for name, value in protected.items())
    failed = HERE / 'root_a6_joint_quotient_replay'
    failed_hashes = {p.name: digest(p) for p in failed.iterdir() if p.is_file()}
    rows = json.loads((HERE / 'audit_a6_joint_quotients_generator_failure_root.partial.json').read_text())['completed_steps']
    assert len(rows) == 11
    for row in rows:
        for output in row['outputs']:
            compare(output['file'], failed)
    morphism_path = HERE / 'audit_a6_common_generator_morphisms_root.json'
    morphisms = json.loads(morphism_path.read_text())
    assert morphisms['all_passed'] and morphisms['original_and_replayed_inputs_unchanged']
    assert all(digest(Path(name)) == value for name, value in morphisms['protected_sha256'].items())
    outputs = [compare('de_a6_gl_common_quotient.json', failed),
               compare('de_a6_gl_common_quotient.npz', failed, morphisms)]
    common = json.loads((failed / 'de_a6_gl_common_quotient.json').read_text())
    rows.append({'program': 'de_a6_gl_common_quotient', 'exit_code': 0,
                 'all_comparisons_passed': True, 'outputs': outputs,
                 'identity_morphism_certificate_sha256': digest(morphism_path),
                 'seconds': common['seconds']})
    print('PASS first eleven exact re-comparisons and the two literal identity word maps', flush=True)
    replay = HERE / 'root_a6_joint_quotient_continuation'
    replay.mkdir(exist_ok=False)
    for name in manifest['records']:
        path = Path(name)
        assert path.parts[0] == 'code' and len(path.parts) == 2
        shutil.copy2(ROOT / name, replay / path.name)
    for stem in ('de_a6_gl_central', 'de_a6_subgroup_checks'):
        with (replay / (stem + '_compile_root.out')).open('x') as log:
            run = subprocess.run(['g++', '-std=c++17', '-O3', stem + '.cpp', '-o', stem],
                                 cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, stem

    def execute(label, command, outputs):
        tick = time.time()
        for name in outputs:
            path = replay / name
            if path.exists():
                path.unlink()
        with (replay / (label + '_root_check.out')).open('x') as log:
            run = subprocess.run(command, cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, (label, run.returncode)
        comparisons = [compare(name, replay) for name in outputs]
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

    py('de_a6_gl_central_prepare', ['de_a6_gl_central_prepare.json',
       'de_a6_gl_central_prepare.npz', 'de_a6_gl_central_model.bin'])
    execute('complete_central_pullback',
            [str(replay / 'de_a6_gl_central'), 'de_a6_gl_central_model.bin',
             'de_a6_schreier_residual_derived.bin', 'de_a6_gl_central.json'],
            ['de_a6_gl_central.json'])
    py('de_a6_gl_central_replay')
    py('de_a6_gl_central_signs')
    py('de_a6_gl_boundary')
    py('de_a6_gl_target_prepare', ['de_a6_gl_target_prepare.json',
       'de_a6_gl_target_prepare.npz', 'de_a6_gl_target.input'])
    execute('complete_target_normality',
            [str(replay / 'de_a6_subgroup_checks'), 'de_a6_gl_target_derived3.bin',
             'de_a6_gl_target.input', 'de_a6_gl_target_normal.json', 'normal'],
            ['de_a6_gl_target_normal.json'])
    py('de_a6_gl_target_certificate')
    assert len(rows) == 20
    chains = json.loads((HERE / 'audit_a6_joint_chains_root.json').read_text())
    assert chains['all_passed'] and chains['original_artifacts_unchanged']
    assert all(digest(ROOT / name) == value for name, value in protected.items())
    assert all(digest(failed / name) == value for name, value in failed_hashes.items())
    result = {'all_passed': True, 'steps': rows,
              'independent_complete_chain_audit': 'audit_a6_joint_chains_root.json',
              'exact_derived_generator_identity_maps': str(morphism_path.relative_to(ROOT)),
              'initial_failed_run_preserved': 'research/E54_root_derived_generator_replay_failure.json',
              'initial_isolated_directory_unchanged': True,
              'original_artifacts_unchanged': True, 'protected_sha256': protected,
              'seconds': round(sum(row['seconds'] for row in rows), 3),
              'seconds_scope': 'Sum of the twenty completed program/comparison steps; preserved failure overhead excluded.',
              'continuation_wall_seconds': round(time.time() - started, 3)}
    (HERE / 'audit_a6_joint_quotients_root.json').write_text(json.dumps(result, indent=2) + '\n')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print('ROOT_A6_JOINT_COMPLETE_QUOTIENTS_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
