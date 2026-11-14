#!/usr/bin/env python3
"""Isolated root audit of the frozen E60 source and target continuation.

The old complete source upper bound was already replayed independently.
This audit uses the signed79-word lower bound, all60 normal-form queries,
and fresh complete replays of the six new target chains.
"""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / 'research/root_a6_triple_fibres_replay'


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def math_json(value):
    if isinstance(value, dict):
        return {k: math_json(v) for k, v in value.items()
                if k not in {'seconds', 'wall_seconds', 'input_sha256'}}
    if isinstance(value, list):
        return [math_json(v) for v in value]
    return value


def main():
    started = time.monotonic()
    manifest_path = ROOT / 'code/de_a6_triple_fibres_manifest.json'
    manifest_sha = sha(manifest_path)
    assert manifest_sha == '6fb3b1ace496838ae1825f2fc09f59bdc1f9f8370d89f2c6c7a61b8663d576cb'
    manifest = json.loads(manifest_path.read_text())
    records = {**manifest['records'], **manifest['documents']}
    assert not DEST.exists(), 'Preserve all preceding runs; choose a fresh directory.'
    DEST.mkdir(parents=True)
    protected = {}
    for name, record in records.items():
        source = ROOT / name
        assert sha(source) == record['sha256'] and source.stat().st_size == record['bytes'], name
        protected[name] = record['sha256']
        target = DEST / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    shutil.copy2(manifest_path, DEST / 'code/de_a6_triple_fibres_manifest.json')
    code = DEST / 'code'
    logs = DEST / 'logs'
    logs.mkdir()
    commands = [
        ['g++', '-O3', '-std=c++17', 'de_a6_schreier.cpp', '-o', 'e60_schreier'],
        ['g++', '-O3', '-std=c++17', 'de_a6_triple_query.cpp', '-o', 'e60_queries'],
        [sys.executable, 'de_a6_triple_signed_base_prepare.py'],
        ['./e60_schreier', '--replay', 'de_a6_triple_signed_base.bin'],
        [sys.executable, 'de_a6_triple_signed_replay.py'],
        [sys.executable, 'de_a6_triple_commutator_prepare.py'],
        ['./e60_queries', 'de_a6_triple_kernel_model.bin', 'de_a6_triple_central_model.bin',
         'de_a6_schreier_residual_derived.bin', 'de_a6_triple_commutator_queries.bin',
         'de_a6_triple_commutator_queries.json'],
        [sys.executable, 'de_a6_triple_commutator_replay.py'],
        [sys.executable, 'de_a6_triple_deep_certificate.py'],
        [sys.executable, 'de_a6_triple_target_prepare.py'],
        [sys.executable, 'de_a6_triple_target_quotient.py'],
        [sys.executable, 'de_a6_triple_target_old_maps.py'],
        [sys.executable, 'de_a6_triple_target_complete_replay.py'],
        [sys.executable, 'de_a6_triple_target_certificate.py'],
    ]
    rows = []
    for i, command in enumerate(commands):
        begin = time.monotonic()
        with (logs / f'{i:02d}.out').open('w') as stdout, (logs / f'{i:02d}.err').open('w') as stderr:
            subprocess.run(command, cwd=code, stdout=stdout, stderr=stderr, check=True)
        row = {'stage': i, 'command': command, 'status': 'PASS',
               'seconds': round(time.monotonic()-begin, 3)}
        rows.append(row)
        print(json.dumps(row), flush=True)
    json_stems = ['de_a6_triple_signed_base_prepare', 'de_a6_triple_signed_replay',
                  'de_a6_triple_commutator_prepare', 'de_a6_triple_commutator_queries',
                  'de_a6_triple_commutator_replay', 'de_a6_triple_deep_certificate',
                  'de_a6_triple_target_prepare', 'de_a6_triple_target_quotient',
                  'de_a6_triple_target_old_maps', 'de_a6_triple_target_complete_replay',
                  'de_a6_triple_target_certificate']
    comparisons = []
    for stem in json_stems:
        name = stem+'.json'
        original = json.loads((ROOT / 'code' / name).read_text())
        replay = json.loads((code / name).read_text())
        assert math_json(original) == math_json(replay), name
        for source, expected in replay.get('input_sha256', {}).items():
            assert sha(code / source) == expected, (name, source)
        comparisons.append(name)
    npz_stems = ['de_a6_triple_signed_base_generators', 'de_a6_triple_signed_replay',
                 'de_a6_triple_commutator_prepare', 'de_a6_triple_commutator_replay',
                 'de_a6_triple_target_prepare', 'de_a6_triple_target_quotient',
                 'de_a6_triple_target_certificate']
    npz_compared = []
    for stem in npz_stems:
        name = stem+'.npz'
        with np.load(ROOT / 'code' / name) as a, np.load(code / name) as b:
            assert set(a.files) == set(b.files), name
            for key in a.files:
                assert a[key].shape == b[key].shape and a[key].dtype == b[key].dtype, (name, key)
                assert np.array_equal(a[key], b[key]), (name, key)
        npz_compared.append(name)
    byte_names = ['de_a6_triple_signed_base_seed.bin', 'de_a6_triple_signed_kernel_model.bin',
                  'de_a6_triple_commutator_queries.bin', 'de_a6_triple_target.input']
    for name in byte_names:
        assert (ROOT / 'code' / name).read_bytes() == (code / name).read_bytes(), name
    # The isolated signed-base replay is an actual complete chain check;
    # compare every structural field with the saved mathematical report.
    sys.path.insert(0, str(code))
    from de_a6_triple_source_certificate import report
    original = report('de_a6_triple_signed_base.out')
    replay_text = (logs / '03.out').read_text()
    replay = json.loads(replay_text[replay_text.index('{'):])
    excluded = {'seconds', 'total_discovery_relation_scans', 'selected_original_indices'}
    assert {k:v for k,v in original.items() if k not in excluded} == \
           {k:v for k,v in replay.items() if k not in excluded}
    assert replay['complete_final_Schreier_relations'] == 1159255
    assert not replay['derived_mode'] and replay['normal_conjugation_checks'] == 0
    for name, expected in protected.items():
        assert sha(ROOT / name) == expected, name
    assert sha(manifest_path) == manifest_sha
    result = {'status': 'PASS_ROOT_COMPLETE_E60_CONTINUATION_REPLAY',
              'manifest_sha256': manifest_sha, 'protected_original_count': len(protected),
              'all_original_files_unchanged': True,
              'all_mathematical_JSON_outputs_identical': comparisons,
              'all_NPZ_arrays_shapes_and_dtypes_identical': npz_compared,
              'all_byte_outputs_identical': byte_names,
              'signed_complete_base_relations': 1159255,
              'signed_kernel_lower_bound79_matches_previously_root_replayed_upper_bound79': True,
              'complete_normal_form_query_count': 60,
              'fresh_complete_target_chain_count': 6,
              'complete_target_relation_count': 3144734,
              'signed_report_provenance': {k: [original.get(k), replay.get(k)] for k in sorted(excluded)},
              'stages': rows, 'seconds': round(time.monotonic()-started, 3)}
    (DEST / 'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
