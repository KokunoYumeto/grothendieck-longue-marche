#!/usr/bin/env python3
"""Complete isolated E76 replay with exact arrays and routed input hashes."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import re
import shutil
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def mathematical(value):
    if isinstance(value, dict):
        return {k: mathematical(v) for k, v in value.items()
                if k not in {'seconds', 'input_sha256'}}
    if isinstance(value, list):
        return [mathematical(v) for v in value]
    return value


def verify_provenance(value, tree, context):
    records = []
    def walk(obj, pointer):
        if isinstance(obj, dict):
            for key, entry in obj.items():
                if key == 'input_sha256':
                    assert isinstance(entry, dict), (context, pointer, 'untyped provenance')
                    for name, expected in entry.items():
                        assert isinstance(expected, str) and re.fullmatch('[0-9a-f]{64}', expected)
                        given = Path(name)
                        if given.is_absolute():
                            relative = given.relative_to(ROOT)
                        elif len(given.parts) == 1:
                            relative = Path('code')/given
                        else:
                            assert given.parts[0] in {'code', 'research'}, (context, name)
                            relative = given
                        assert '..' not in relative.parts
                        actual = tree/relative
                        assert actual.is_file(), ('missing exact input route', context, name)
                        observed = sha256(actual.read_bytes()).hexdigest()
                        assert observed == expected, ('input provenance mismatch', context, name)
                        records.append({'record': context, 'json_pointer': pointer+'/input_sha256',
                                        'input': name, 'actual_relative_path': str(relative),
                                        'sha256': observed})
                else:
                    walk(entry, pointer+'/'+str(key))
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                walk(item, pointer+'/'+str(i))
    walk(value, '')
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--destination', required=True)
    args = parser.parse_args()
    started = time.monotonic()
    dest = Path(args.destination)
    if not dest.is_absolute():
        dest = ROOT/dest
    assert not dest.exists(), ('fresh isolated destination required', str(dest))
    manifest_path = HERE/'de_wajnryb_surface_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    for name, entry in manifest['files'].items():
        actual = ROOT/name
        assert sha256(actual.read_bytes()).hexdigest() == entry['sha256'], ('frozen input', name)
        target = dest/name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(actual, target)
    code = dest/'code'
    rows = []
    report = {'status': 'RUNNING', 'steps': rows,
              'manifest_sha256': sha256(manifest_path.read_bytes()).hexdigest(),
              'protected_original_count': len(manifest['files']),
              'verified_input_provenance': [], 'historical_engine_routes': []}
    def save():
        (dest/'replay.json').write_text(json.dumps(report, indent=2)+'\n')
    def compare(name):
        actual, original = code/name, HERE/name
        assert actual.is_file() and original.is_file(), ('missing output', name)
        if actual.suffix == '.json':
            new, old = json.loads(actual.read_text()), json.loads(original.read_text())
            report['verified_input_provenance'].extend(verify_provenance(old, ROOT, 'original:'+name))
            report['verified_input_provenance'].extend(verify_provenance(new, dest, 'regenerated:'+name))
            assert mathematical(new) == mathematical(old), ('JSON mathematics', name)
        elif actual.suffix == '.npz':
            with np.load(actual) as a, np.load(original) as b:
                assert set(a.files) == set(b.files), ('array keys', name)
                for key in a.files:
                    assert a[key].dtype == b[key].dtype and a[key].shape == b[key].shape, ('array type', name, key)
                    assert np.array_equal(a[key], b[key]), ('array value', name, key)
        else:
            assert actual.read_bytes() == original.read_bytes(), ('literal byte output', name)
    def run(row):
        begin = time.monotonic()
        record = {'label': row['label'], 'command': [sys.executable]+row['arguments'], 'status': 'RUNNING'}
        rows.append(record)
        save()
        print(json.dumps(record), flush=True)
        with (dest/(row['label']+'.out')).open('w') as out, (dest/(row['label']+'.err')).open('w') as err:
            completed = subprocess.run(record['command'], cwd=code, stdout=out, stderr=err)
        record['exit_code'] = completed.returncode
        assert completed.returncode == 0, ('program failed', row['label'])
        for name in row['outputs']:
            compare(name)
        record.update(status='PASS', exact_outputs=row['outputs'], seconds=round(time.monotonic()-begin, 3))
        save()
        print(json.dumps(record), flush=True)
    try:
        # The S4 engine-construction record names its first, retained versions.
        # It is not reinterpreted as a hash claim about the final repaired files.
        for tree, tag in ((ROOT, 'original'), (dest, 'copy')):
            records = json.loads((tree/'code/de_wajnryb_s4_engines_prepare.json').read_text())
            for row in records:
                historical = Path('research/E74_S4_initial_engine_metadata')/Path(row['output']).name
                assert sha256((tree/row['source']).read_bytes()).hexdigest() == row['source_sha256']
                assert sha256((tree/historical).read_bytes()).hexdigest() == row['output_sha256']
                report['historical_engine_routes'].append({'tree': tag, 'declared_output': row['output'],
                    'retained_actual_path': str(historical), 'sha256': row['output_sha256']})
        for row in manifest['steps']:
            run(row)
        assert all(sha256((ROOT/name).read_bytes()).hexdigest() == entry['sha256']
                   for name, entry in manifest['files'].items())
        report.update(status='PASS_COMPLETE_ISOLATED_E76_REPLAY', all_originals_unchanged=True,
                      verified_input_hash_count=len(report['verified_input_provenance']),
                      every_omitted_input_hash_independently_verified=True,
                      every_finite_tuple_and_every_source_relation_repeated=True,
                      stdout_scope='New per-step logs retained; elapsed-time stdout is not byte compared.',
                      seconds=round(time.monotonic()-started, 3))
        save()
        print(json.dumps({k: v for k, v in report.items() if k not in
                          {'steps', 'verified_input_provenance', 'historical_engine_routes'}}, indent=2), flush=True)
    except BaseException as error:
        report.update(status='FAILED_PRESERVED_ISOLATED_E76_REPLAY', failure=repr(error),
                      seconds=round(time.monotonic()-started, 3))
        save()
        raise


if __name__ == '__main__':
    main()
