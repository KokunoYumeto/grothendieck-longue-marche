"""Isolated unchanged replay of the frozen F.32 literal-word audit.

Copies exactly the checker and its twelve output-listed inputs.  No producer is
executed.  The sole output comparison transport is the bijection on the twelve
absolute input-path keys; the stdout transport is the consequent output hash.
"""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'work/part_a/code'
DEST = ROOT / 'work/part_c/f32_independent_replay'
CHECKER = 'affine_nonproduct_r1_independent_audit.py'
OUTPUT = 'affine_nonproduct_r1_independent_audit_output.json'
STDOUT = 'affine_nonproduct_r1_independent_audit_stdout.txt'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def binding(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': sha256(data).hexdigest()}


def main():
    assert not DEST.exists(), 'Use a fresh replay directory; never overwrite evidence.'
    DEST.mkdir(parents=True)
    reference = json.loads((SOURCE/OUTPUT).read_text())
    assert reference['total_exact_checks'] == 1088
    assert reference['verifier_sha256'] == digest(SOURCE/CHECKER)
    assert len(reference['inputs']) == 12
    records = []
    path_map = {}
    for original, expected in reference['inputs'].items():
        source = Path(original)
        assert source.is_relative_to(SOURCE)
        assert digest(source) == expected
        copied = DEST / source.relative_to(SOURCE)
        copied.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, copied)
        assert copied.read_bytes() == source.read_bytes()
        records.append({'source': binding(source), 'isolated_copy': binding(copied),
                        'whole_bytes_equal': True})
        path_map[str(copied)] = original
    shutil.copyfile(SOURCE/CHECKER, DEST/CHECKER)
    assert (DEST/CHECKER).read_bytes() == (SOURCE/CHECKER).read_bytes()
    started = time.time()
    with (DEST/'stdout.txt').open('wb') as stdout, (DEST/'stderr.txt').open('wb') as stderr:
        run = subprocess.run([sys.executable, str(DEST/CHECKER)], cwd=DEST,
                             stdout=stdout, stderr=stderr, check=False)
    elapsed = time.time()-started
    assert run.returncode == 0, f'Checker exit {run.returncode}'
    assert (DEST/'stderr.txt').read_bytes() == b''
    result = json.loads((DEST/OUTPUT).read_text())
    assert set(result['inputs']) == set(path_map)
    assert len(set(path_map.values())) == 12
    transported = dict(result)
    transported['inputs'] = {path_map[path]: value for path, value in result['inputs'].items()}
    transported_bytes = (json.dumps(transported, indent=2)+'\n').encode()
    assert transported_bytes == (SOURCE/OUTPUT).read_bytes()
    (DEST/'output_with_exact_input_key_transport.json').write_bytes(transported_bytes)
    stdout_transport = None
    if (SOURCE/STDOUT).exists():
        old_hash, new_hash = digest(SOURCE/OUTPUT), digest(DEST/OUTPUT)
        observed = (DEST/'stdout.txt').read_bytes()
        assert observed.count(new_hash.encode()) == 1
        transported_stdout = observed.replace(new_hash.encode(), old_hash.encode())
        assert transported_stdout == (SOURCE/STDOUT).read_bytes()
        (DEST/'stdout_with_exact_output_hash_transport.txt').write_bytes(transported_stdout)
        stdout_transport = {'source_stdout': binding(SOURCE/STDOUT),
                            'substitution_from': new_hash, 'substitution_to': old_hash,
                            'occurrences': 1, 'whole_bytes_equal_after_transport': True}
    for item in records:
        source = ROOT/item['source']['path']
        copied = ROOT/item['isolated_copy']['path']
        assert digest(source) == item['source']['sha256']
        assert source.read_bytes() == copied.read_bytes()
    assert (DEST/CHECKER).read_bytes() == (SOURCE/CHECKER).read_bytes()
    comparison = {
        'status': 'PASS_F32_UNCHANGED_ISOLATED_LITERAL_WORD_REPLAY',
        'runner': binding(Path(__file__).resolve()),
        'python_version': sys.version, 'exit_code': run.returncode,
        'elapsed_seconds': elapsed, 'stderr_bytes': 0,
        'checker_source': binding(SOURCE/CHECKER), 'checker_copy': binding(DEST/CHECKER),
        'checker_whole_bytes_equal': True,
        'copied_input_count': len(records), 'input_bindings': records,
        'input_path_bijection': path_map,
        'only_output_transport': 'Replace the twelve isolated absolute inputs keys by their twelve exact original keys, retaining insertion order and every value; serialize with indent=2 and one trailing newline.',
        'whole_output_bytes_equal_after_exact_key_transport': True,
        'source_output': binding(SOURCE/OUTPUT), 'isolated_output': binding(DEST/OUTPUT),
        'transported_output': binding(DEST/'output_with_exact_input_key_transport.json'),
        'stdout': binding(DEST/'stdout.txt'), 'stderr': binding(DEST/'stderr.txt'),
        'stdout_transport': stdout_transport,
        'checks': result['checks'], 'check_total': result['check_total'],
        'word_parser_checks': result['reviewed_word_and_parser_checks'],
        'word_parser_check_total': result['reviewed_word_and_parser_check_total'],
        'total_exact_checks': result['total_exact_checks'],
        'literal_word_count': result['literal_word_count'],
        'moving_source_count': result['moving_source_count'],
        'character_chart': result['character_chart'],
        'quotient_characters': result['quotient_characters'],
        'determinants': result['determinants'],
        'all_original_files_unchanged_after_replay': True,
        'scope': 'Recomputes every declared integral matrix identity from the original words. The independent mathematical report separately checks finite-field nonvanishing, minimal-type separation, source membership, trace reduction and sign transport.'}
    (DEST/'comparison.json').write_text(json.dumps(comparison, indent=2)+'\n')
    print(json.dumps({'status': comparison['status'], 'total_exact_checks': result['total_exact_checks'],
                      'comparison': binding(DEST/'comparison.json')}, indent=2))


if __name__ == '__main__':
    main()
