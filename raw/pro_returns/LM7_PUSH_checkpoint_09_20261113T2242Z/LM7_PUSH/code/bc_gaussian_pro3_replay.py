#!/usr/bin/env python3
"""Isolated exact replay of E70, including all six Schreier certificates."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
import numpy as np


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mathematical(value):
    if isinstance(value, dict):
        return {k: mathematical(v) for k, v in value.items()
                if k not in ('seconds', 'input_sha256')}
    if isinstance(value, list):
        return [mathematical(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    out = (Path(args.directory).resolve() if args.directory
           else root / 'research/E70_isolated_replay')
    if out.exists():
        raise RuntimeError('Use a fresh isolated replay directory: ' + str(out))
    out.mkdir(parents=True)
    code = out / 'code'
    code.mkdir()
    manifest = json.loads((root / 'research/E70_authoritative_manifest.json').read_text())
    protected = {**manifest['files'], **manifest['inputs']}
    assert all(digest(root / p) == h for p, h in protected.items())
    for name in manifest['inputs']:
        if name.startswith('code/'):
            shutil.copy2(root / name, code / Path(name).name)
    for name in manifest['replay_order']:
        shutil.copy2(root / 'code' / (name + '.py'), code / (name + '.py'))
    start = time.monotonic()
    with (out / 'compile.out').open('w') as stdout, (out / 'compile.err').open('w') as stderr:
        subprocess.run(['g++', '-O3', '-std=c++17', str(code / 'de_a6_schreier.cpp'),
                        '-o', str(code / 'de_a6_schreier_fast')],
                       cwd=code, stdout=stdout, stderr=stderr, check=True)
    records = []
    for name in manifest['replay_order']:
        then = time.monotonic()
        with (code / (name + '.out')).open('w') as stdout, (code / (name + '.err')).open('w') as stderr:
            subprocess.run([sys.executable, str(code / (name + '.py'))],
                           cwd=code, stdout=stdout, stderr=stderr, check=True)
        old = json.loads((root / 'code' / (name + '.json')).read_text())
        got = json.loads((code / (name + '.json')).read_text())
        provenance = []
        for side, base, data in [('original', root / 'code', old), ('replay', code, got)]:
            assert data['source_sha256'] == digest(base / (name + '.py'))
            for filename, h in data.get('input_sha256', {}).items():
                assert digest(base / filename) == h, (side, name, filename)
                provenance.append([side, filename, h])
        # Every input hash is validated against its own actual bytes before
        # removing it from comparison. Only elapsed-time fields are omitted
        # recursively; all source hashes and mathematical fields are retained.
        assert mathematical(old) == mathematical(got), name
        arrays = []
        npz = code / (name + '.npz')
        if npz.exists():
            a = np.load(root / 'code' / (name + '.npz'))
            b = np.load(npz)
            assert a.files == b.files
            for key in a.files:
                assert np.array_equal(a[key], b[key]), (name, key)
            arrays = a.files
        certificates = []
        if name == 'bc_gaussian_pro3_frattini_common':
            for prefix in manifest['Schreier_certificate_prefixes']:
                for suffix in ('.input', '.bin'):
                    filename = prefix + suffix
                    assert digest(root / 'code' / filename) == digest(code / filename), filename
                    certificates.append(filename)
                # The program's certify() already ran the independent full
                # word/Schreier relation replay on each regenerated binary.
                replay = (code / (prefix + '_replay.out')).read_text()
                assert 'PASS' in replay, prefix
        record = {'program': name, 'status': 'PASS',
                  'seconds': round(time.monotonic() - then, 6),
                  'all_mathematical_JSON_fields_identical': True,
                  'identical_NPZ_arrays': arrays,
                  'byte_identical_Schreier_inputs_and_binaries': certificates,
                  'verified_input_provenance': provenance}
        records.append(record)
        print(name, 'PASS', record['seconds'], flush=True)
    assert all(digest(root / p) == h for p, h in protected.items())
    result = {'status': 'PASS_COMPLETE_ISOLATED_E70_REPLAY',
              'seconds': round(time.monotonic() - start, 6),
              'protected_originals_unchanged': len(protected), 'results': records}
    (out / 'replay.json').write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'], result['seconds'], flush=True)


if __name__ == '__main__':
    main()
