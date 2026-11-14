#!/usr/bin/env python3
"""Independent full replay of E57's four frozen finite certificates."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time
import numpy as np
from audit_a6_joint_quotients_generator_failure_root import mathematical, verify_hashes

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    started = time.time()
    manifest_path = HERE / 'de_a6_uniform_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    protected = {name: row['sha256'] for name, row in manifest['records'].items()}
    protected.update({name: row['sha256'] for name, row in manifest['documents'].items()})
    protected['code/de_a6_uniform_manifest.json'] = digest(manifest_path)
    assert all(digest(ROOT / name) == value for name, value in protected.items())
    replay = HERE / 'root_a6_uniform_replay'
    replay.mkdir(exist_ok=False)
    for name in manifest['records']:
        path = Path(name)
        assert path.parts[0] == 'code' and len(path.parts) == 2
        shutil.copy2(ROOT / name, replay / path.name)
    with (replay / 'compile_schreier_root.out').open('x') as log:
        run = subprocess.run(['g++', '-std=c++17', '-O3', 'de_a6_schreier.cpp',
                              '-o', 'de_a6_schreier_root'], cwd=replay,
                             stdout=log, stderr=subprocess.STDOUT)
    assert run.returncode == 0
    rows = []

    def program(stem, extra=()):
        tick = time.time()
        outputs = [stem + '.json', stem + '.npz', *extra]
        for name in outputs:
            (replay / name).unlink(missing_ok=True)
        with (replay / (stem + '_root_check.out')).open('x') as log:
            run = subprocess.run([sys.executable, '-u', stem + '.py'], cwd=replay,
                                 stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, stem
        a = json.loads((HERE / (stem + '.json')).read_text())
        b = json.loads((replay / (stem + '.json')).read_text())
        declared = set()
        verify_hashes(a, HERE, declared)
        verify_hashes(b, replay, declared)
        assert mathematical(a) == mathematical(b), stem
        with np.load(HERE / (stem + '.npz')) as a, np.load(replay / (stem + '.npz')) as b:
            assert set(a.files) == set(b.files)
            assert all(np.array_equal(a[key], b[key]) for key in a.files)
            literal = sorted(a.files)
        for name in extra:
            assert (HERE / name).read_bytes() == (replay / name).read_bytes()
        row = {'program': stem, 'exit_code': 0, 'all_mathematical_JSON_equal': True,
               'literal_arrays': literal, 'own_location_hashes_verified': sorted(declared),
               'seconds': round(time.time() - tick, 3)}
        rows.append(row)
        print(json.dumps(row), flush=True)

    program('de_a6_uniform_comparison')
    program('de_a6_uniform_target_prepare', ['de_a6_uniform_target.input'])
    tick = time.time()
    output = replay / 'de_a6_uniform_target_root_check.out'
    with output.open('x') as log:
        run = subprocess.run([str(replay / 'de_a6_schreier_root'), '--replay',
                              'de_a6_uniform_target.bin'], cwd=replay,
                             stdout=log, stderr=subprocess.STDOUT)
    assert run.returncode == 0
    a = json.loads((HERE / 'de_a6_uniform_target.out').read_text().splitlines()[-1])
    b = json.loads(output.read_text().splitlines()[-1])
    keys = ('status', 'degree', 'order', 'strong_generators', 'word_DAG_nodes',
            'derived_mode', 'complete_final_Schreier_relations', 'base', 'orbit_lengths')
    assert all(a[key] == b[key] for key in keys)
    assert b['status'] == 'PASS' and b['degree'] == 536
    assert b['complete_final_Schreier_relations'] == 219684
    assert b['total_discovery_relation_scans'] == 219684
    assert not b['derived_mode'] and b['normal_conjugation_checks'] == 0
    rows.append({'program': 'complete_uniform_target_chain', 'exit_code': 0,
                 'all_exact_chain_fields_equal': True,
                 'complete_final_Schreier_relations': 219684,
                 'seconds': round(time.time() - tick, 3)})
    print(json.dumps(rows[-1]), flush=True)
    program('de_a6_uniform_target_certificate')
    assert all(digest(ROOT / name) == value for name, value in protected.items())
    result = {'all_passed': True, 'steps': rows, 'original_artifacts_unchanged': True,
              'proof_sha256': protected['sections/E_a6_uniform_agent.tex'],
              'protected_sha256': protected, 'seconds': round(time.time() - started, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print('ROOT_A6_UNIFORM_COMPLETE_REPLAY_PASS', flush=True)


if __name__ == '__main__':
    main()
