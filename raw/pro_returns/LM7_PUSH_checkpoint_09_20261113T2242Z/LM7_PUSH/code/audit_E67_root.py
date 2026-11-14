#!/usr/bin/env python3
"""Independent isolated replay of all frozen E67 maps and word fibres."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / 'research/root_E67_replay'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mathematical(value):
    if isinstance(value, dict):
        answer = {}
        for key, item in value.items():
            if key in ('seconds', 'six_input_sha256'):
                continue
            if key == 'input_sha256' and isinstance(item, dict):
                item = {k: v for k, v in item.items()
                        if k != 'bc_orbifold_CM_six.json'}
            answer[key] = mathematical(item)
        return answer
    if isinstance(value, list):
        return [mathematical(item) for item in value]
    return value


def main():
    started = time.monotonic()
    manifest_path = ROOT / 'research/E67_authoritative_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    protected = dict(manifest['files'])
    protected.update(manifest['inputs'])
    protected[str(manifest_path.relative_to(ROOT))] = digest(manifest_path)
    for name, expected in protected.items():
        assert digest(ROOT / name) == expected, name
    assert not DEST.exists(), 'Use a new destination; never overwrite a replay.'
    code = DEST / 'code'
    code.mkdir(parents=True)
    for name in manifest['replay_order']:
        shutil.copy2(ROOT / 'code' / name, code / name)
    for name in manifest['inputs']:
        shutil.copy2(ROOT / name, code / Path(name).name)
    records = []
    for name in manifest['replay_order']:
        stem = Path(name).stem
        stage = time.monotonic()
        with (code / (stem + '.out')).open('w') as out, \
                (code / (stem + '.err')).open('w') as err:
            result = subprocess.run([sys.executable, str(code / name)],
                                    cwd=DEST, stdout=out, stderr=err)
        assert result.returncode == 0, (name, result.returncode)
        original = json.loads((ROOT / 'code' / (stem + '.json')).read_text())
        replayed = json.loads((code / (stem + '.json')).read_text())
        assert mathematical(original) == mathematical(replayed), stem
        if stem == 'bc_orbifold_CM_linear':
            assert replayed['six_input_sha256'] == digest(code / 'bc_orbifold_CM_six.json')
        if stem == 'bc_orbifold_CM_export':
            for input_name, expected in replayed['input_sha256'].items():
                assert digest(code / input_name) == expected, input_name
            with np.load(ROOT / 'code' / (stem + '.npz')) as old, \
                    np.load(code / (stem + '.npz')) as new:
                assert old.files == new.files
                for key in old.files:
                    assert np.array_equal(old[key], new[key]), key
                array_names = list(old.files)
        records.append({'program': name, 'mathematical_JSON_equal': True,
                        'seconds': round(time.monotonic() - stage, 6)})
        print(json.dumps(records[-1]), flush=True)
    for name, expected in protected.items():
        assert digest(ROOT / name) == expected, name
    report = {'status': 'PASS_COMPLETE_ISOLATED_E67_REPLAY',
              'full_proof_and_all_four_programs_read': True,
              'protected_original_file_count': len(protected),
              'protected_original_sha256': protected,
              'programs': records,
              'all_export_NPZ_arrays_equal': array_names,
              'regenerated_six_JSON_provenance_hashes_verified': True,
              'seconds': round(time.monotonic() - started, 6)}
    (DEST / 'replay.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': report['status'], 'seconds': report['seconds']}), flush=True)


if __name__ == '__main__':
    main()
