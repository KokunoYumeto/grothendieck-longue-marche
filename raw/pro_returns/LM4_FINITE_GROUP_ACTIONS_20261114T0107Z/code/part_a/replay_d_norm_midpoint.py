"""Unchanged isolated peer replay of the actual D odd-local midpoint code."""
from hashlib import sha256
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time


def main():
    root = Path(__file__).resolve().parents[3]
    folder = root/'work/part_a/review_d_norm_replay'
    folder.mkdir(exist_ok=True)
    author = root/'work/part_d_attack'
    metadata = author/'actual_norm_branches_and_odd_local_coefficients_result.json'
    result = json.loads(metadata.read_text())

    def binding(path):
        return {'path': str(path.relative_to(root)), 'bytes': path.stat().st_size,
                'sha256': sha256(path.read_bytes()).hexdigest()}

    protected = [metadata]+[root/item['path'] for item in result['files']+result['dependencies']]
    before = [binding(path) for path in protected]
    for item in result['files']+result['dependencies']:
        assert sha256((root/item['path']).read_bytes()).hexdigest() == item['sha256'], item['path']
    source = author/'code/actual_odd_local_midpoint.py'
    copied = folder/source.name
    shutil.copyfile(source, copied)
    assert copied.read_bytes() == source.read_bytes()
    start = time.monotonic()
    completed = subprocess.run([sys.executable, copied.name], cwd=folder,
                               capture_output=True, check=False)
    elapsed = time.monotonic()-start
    stdout, stderr = folder/'stdout.txt', folder/'stderr.txt'
    stdout.write_bytes(completed.stdout)
    stderr.write_bytes(completed.stderr)
    assert completed.returncode == 0 and not completed.stderr
    output = folder/'actual_odd_local_midpoint_output.json'
    original_output = author/'code/actual_odd_local_midpoint_output.json'
    original_stdout = author/'code/actual_odd_local_midpoint_stdout.txt'
    assert output.read_bytes() == stdout.read_bytes() == original_output.read_bytes() == original_stdout.read_bytes()
    audit = json.loads(output.read_text())
    assert audit['status'] == 'PASS' and audit['assertion_count'] == 27
    assert audit['actual_image_order'] == 3125 and len(audit['rows']) == 5
    assert all(item['passed'] for item in audit['checks'])
    assert all(len(row['unit_parameter_tests']) == 4 for row in audit['rows'])
    assert all(not item['full_finite_D_is_identity'] and not item['square_equation_mod_5']
               for item in audit['rows'][1]['unit_parameter_tests'])
    after = [binding(path) for path in protected]
    assert before == after
    summary = {'status': 'PASS_UNCHANGED_ISOLATED_D_NORM_MIDPOINT_REPLAY',
               'runner': binding(Path(__file__).resolve()), 'author_program': binding(source),
               'isolated_program': binding(copied), 'program_bytes_identical': True,
               'exit_code': completed.returncode, 'elapsed_seconds': elapsed,
               'raw_output': binding(output), 'captured_stdout': binding(stdout),
               'captured_stderr': binding(stderr),
               'original_output': binding(original_output), 'original_stdout': binding(original_stdout),
               'whole_raw_output_and_stdout_bytes_identical': True,
               'named_checks': 27, 'actual_finite_image_order': 3125,
               'local_coefficients': 5, 'unit_parameter_rows': 20,
               'all_author_and_dependency_bindings_unchanged': True,
               'protected_bindings': before,
               'scope': 'Actual finite pro-5 image and the exact local midpoint formulas. The mathematical norm-branch and original/local image comparisons are reviewed separately; original full nonemptiness is not asserted.'}
    comparison = folder/'comparison.json'
    comparison.write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps({'status': summary['status'], 'checks': 27,
                      'comparison': binding(comparison)}, indent=2))


if __name__ == '__main__':
    main()
