#!/usr/bin/env python3
"""Peer replay of the frozen F29 literal-word audits with exact file bindings."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / 'work/part_c/f29_independent_replay'
AUTHOR = ROOT / 'work/part_a/code'
MANIFEST = ROOT / 'work/part_a/f_four_parameter_product_one_images_evidence_manifest.json'


def binding(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': sha256(data).hexdigest()}


def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def manifest_check():
    manifest = json.loads(MANIFEST.read_text())
    assert manifest['claim'] == 'F.29'
    assert len(manifest['entries']) == 63
    paths = set()
    records = []
    for expected in manifest['entries']:
        path = ROOT / expected['path']
        assert expected['path'] not in paths
        paths.add(expected['path'])
        actual = binding(path)
        assert actual == expected, (expected, actual)
        records.append(actual)
    return {'status': 'PASS', 'manifest': binding(MANIFEST),
            'entry_count': len(records), 'entries': records}


def copy_file(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    assert source.read_bytes() == target.read_bytes()
    return {'original': binding(source), 'copy': binding(target)}


def run(script, stdout, stderr):
    with stdout.open('wb') as out, stderr.open('wb') as err:
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                                stdout=out, stderr=err, check=False)
    assert result.returncode == 0, (script, result.returncode)
    assert stderr.read_bytes() == b'', stderr
    return {'exit_code': result.returncode, 'stdout': binding(stdout),
            'stderr': binding(stderr)}


def main():
    before = manifest_check()
    DEST.mkdir(parents=True, exist_ok=False)
    dump(DEST / 'manifest_validation_before.json', before)
    names = [
        'affine_four_parameter_extension_independent_audit.py',
        'affine_four_parameter_r1_independent_audit.py',
        'affine_product_one_four_parameter_stage.py',
        'affine_product_one_four_parameter_stage_output.json',
        'affine_product_one_deleted_first_stage.py',
        'affine_product_one_deleted_first_stage_output.json',
        'affine_deleted_first_two_parameter_stage.py',
        'affine_deleted_first_two_parameter_stage_output.json',
        'full_cross_source_stage/marginal_braids.json',
        'affine_obstruction_stage_output.json',
    ]
    copies = [copy_file(AUTHOR / name, DEST / name) for name in names]
    results = []
    for stem, expected_checks, expected_path_count in [
        ('affine_four_parameter_extension_independent_audit', 3246, 8),
        ('affine_four_parameter_r1_independent_audit', 996, 5),
    ]:
        execution = run(DEST / (stem + '.py'),
                        DEST / (stem + '_stdout.txt'),
                        DEST / (stem + '_stderr.txt'))
        output = DEST / (stem + '_output.json')
        original = AUTHOR / (stem + '_output.json')
        raw = json.loads(output.read_text())
        assert raw['check_total'] == expected_checks
        assert sum(raw['checks'].values()) == expected_checks
        transported = deepcopy(raw)
        path_map = {}

        def exact_path(value):
            source = Path(value)
            relative = source.relative_to(DEST)
            target = AUTHOR / relative
            assert source.read_bytes() == target.read_bytes()
            assert value not in path_map
            path_map[value] = str(target)
            return str(target)

        if stem == 'affine_four_parameter_extension_independent_audit':
            transported['base_inputs'] = {
                exact_path(path): digest
                for path, digest in raw['base_inputs'].items()
            }
            for chart in transported['charts']:
                for field in ['symbolic_input', 'symbolic_producer']:
                    chart[field] = exact_path(chart[field])
        else:
            transported['inputs'] = {
                exact_path(path): digest for path, digest in raw['inputs'].items()
            }
        assert len(path_map) == expected_path_count
        assert len(set(path_map.values())) == expected_path_count
        transformed = DEST / (stem + '_path_transport_output.json')
        dump(transformed, transported)
        assert transformed.read_bytes() == original.read_bytes()
        results.append({'status': 'PASS', 'checks': expected_checks,
                        'original': binding(original), 'replay': binding(output),
                        'raw_byte_identical': output.read_bytes() == original.read_bytes(),
                        'exact_path_bijection': path_map,
                        'path_transported_output_byte_identical': True,
                        'path_transported_output': binding(transformed),
                        **execution})

    # The unchanged exceptional program computes ROOT from parents[3].
    # Mirror exactly the four original input paths below a private root.
    mirror = DEST / 'exceptional_root'
    exceptional_paths = [
        'work/root/four_parameter_r1_exploration/independent_exceptional_words.py',
        'work/root/four_parameter_r1_exploration/forced_lifts_output.json',
        'work/part_a/code/affine_product_one_three_parameter_independent_audit.py',
        'work/part_a/code/full_cross_source_stage/marginal_braids.json',
    ]
    exceptional_copies = [copy_file(ROOT / name, mirror / name)
                          for name in exceptional_paths]
    exceptional_folder = mirror / 'work/root/four_parameter_r1_exploration'
    exceptional_execution = run(exceptional_folder / 'independent_exceptional_words.py',
                                exceptional_folder / 'independent_exceptional_words_stdout.txt',
                                exceptional_folder / 'independent_exceptional_words_stderr.txt')
    exceptional_output = exceptional_folder / 'independent_exceptional_words_output.json'
    exceptional_original = ROOT / 'work/root/four_parameter_r1_exploration/independent_exceptional_words_output.json'
    exceptional_data = json.loads(exceptional_output.read_text())
    assert exceptional_data['check_count'] == 20
    assert len(exceptional_data['checks']) == 20
    assert exceptional_data['residual'] == ['3*t-1', '-2', '0', '0', '0', '0']
    assert exceptional_output.read_bytes() == exceptional_original.read_bytes()
    exceptional = {'status': 'PASS', 'explicit_assertions': 20,
                   'internal_checks': exceptional_data['literal_word_internal_checks'],
                   'original': binding(exceptional_original),
                   'replay': binding(exceptional_output),
                   'raw_byte_identical': True, 'copied_inputs': exceptional_copies,
                   **exceptional_execution}
    after = manifest_check()
    assert before == after
    dump(DEST / 'manifest_validation_after.json', after)
    comparison = {'status': 'PASS', 'main_verifier_check_total': 4242,
                  'exceptional_explicit_assertions': 20,
                  'manifest_before': binding(DEST / 'manifest_validation_before.json'),
                  'manifest_after': binding(DEST / 'manifest_validation_after.json'),
                  'all_63_manifest_bindings_unchanged': True,
                  'copied_inputs': copies, 'verifiers': results,
                  'exceptional_verifier': exceptional,
                  'runner': binding(Path(__file__).resolve()),
                  'scope': 'Exact copies of the two independent F29 word-verifier programs and the separate exceptional three-word verifier; no symbolic producer or universal F24 certificate is rerun.'}
    dump(DEST / 'comparison.json', comparison)
    print(json.dumps({'status': 'PASS', 'main_checks': 4242,
                      'exceptional_assertions': 20, 'manifest_bindings': 63,
                      'comparison': binding(DEST / 'comparison.json')}, indent=2))


if __name__ == '__main__':
    main()
