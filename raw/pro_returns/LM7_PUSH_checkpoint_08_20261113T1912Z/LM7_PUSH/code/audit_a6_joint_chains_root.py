#!/usr/bin/env python3
"""Complete independent replay of every newly frozen E54 stabilizer chain."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import struct
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def last_record(path):
    rows = [json.loads(line) for line in path.read_text().splitlines()
            if line.startswith('{') and line.endswith('}')]
    assert rows and rows[-1]['status'] == 'PASS', path
    return rows[-1]


def main():
    start = time.time()
    manifest_path = HERE / 'de_a6_gl_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    protected = {name: row['sha256'] for name, row in manifest['records'].items()}
    protected.update({name: row['sha256'] for name, row in manifest['documents'].items()})
    protected['code/de_a6_gl_manifest.json'] = digest(manifest_path)
    for name, expected in protected.items():
        assert digest(ROOT / name) == expected, ('protected input', name)
    replay = HERE / 'root_a6_joint_chain_replay'
    replay.mkdir(exist_ok=False)
    for name in manifest['records']:
        path = Path(name)
        assert path.parts[0] == 'code' and len(path.parts) == 2, name
        shutil.copy2(ROOT / name, replay / path.name)
    with (replay / 'compile_schreier_root.out').open('x') as log:
        run = subprocess.run(['g++', '-std=c++17', '-O3',
                              'de_a6_schreier.cpp', '-o', 'de_a6_schreier_root'],
                             cwd=replay, stdout=log, stderr=subprocess.STDOUT)
    assert run.returncode == 0, 'C++ compilation'
    rows = []
    exact_keys = ('status', 'degree', 'order', 'strong_generators',
                  'word_DAG_nodes', 'derived_mode',
                  'complete_final_Schreier_relations', 'base', 'orbit_lengths')
    for name in manifest['new_complete_chain_replay_order']:
        tick = time.time()
        stem = Path(name).stem
        candidates = [HERE / (stem + suffix)
                      for suffix in ('_replay.out', '_fresh_replay.out', '.out', '_order.out')]
        # Preparation logs share some stems with chain logs.  Select only a
        # completed exact chain record, preserving the initial failure separately.
        matches = []
        for path in candidates:
            if not path.is_file():
                continue
            records = [json.loads(line) for line in path.read_text().splitlines()
                       if line.startswith('{') and line.endswith('}')]
            if records and records[-1].get('status') == 'PASS' and all(
                    key in records[-1] for key in exact_keys):
                matches.append((path, records[-1]))
        assert matches, ('no complete chain log', name)
        expected_path, expected = matches[0]
        assert all(all(record[key] == expected[key] for key in exact_keys)
                   for _, record in matches), ('inconsistent saved chain logs', name)
        output = replay / (stem + '_root_check.out')
        with output.open('x') as log:
            run = subprocess.run([str(replay / 'de_a6_schreier_root'), '--replay', name],
                                 cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, (name, run.returncode)
        actual = last_record(output)
        assert all(actual[key] == expected[key] for key in exact_keys), name
        assert actual['total_discovery_relation_scans'] == actual['complete_final_Schreier_relations']
        assert actual['selected_original_indices'] == []
        with (replay / name).open('rb') as stream:
            magic, degree = struct.unpack('<II', stream.read(8))
            if magic == 0x41365354:
                derived, original_count = struct.unpack('<II', stream.read(8))
            else:
                assert magic == 0x41365353
                derived, original_count = 0, struct.unpack('<I', stream.read(4))[0]
        assert degree == actual['degree'] and bool(derived) == actual['derived_mode']
        expected_checks = original_count * actual['strong_generators'] if derived else 0
        assert actual['normal_conjugation_checks'] == expected_checks, name
        row = {'certificate': name, 'source_sha256': digest(HERE / name),
               'exit_code': 0, 'all_exact_chain_fields_equal': True,
               'all_original_word_DAG_values_verified': True,
               'complete_final_Schreier_relations': actual['complete_final_Schreier_relations'],
               'derived_normality_checks': expected_checks,
               'comparison_record': expected_path.name,
               'replay_output_sha256': digest(output),
               'seconds': round(time.time() - tick, 3)}
        rows.append(row)
        Path(__file__).with_suffix('.partial.json').write_text(
            json.dumps({'completed_steps': rows}, indent=2) + '\n')
        print(json.dumps(row), flush=True)
    assert all(digest(ROOT / name) == h for name, h in protected.items())
    out = {'all_passed': True, 'steps': rows, 'original_artifacts_unchanged': True,
           'protected_sha256': protected, 'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print('ROOT_A6_JOINT_COMPLETE_CHAINS_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
