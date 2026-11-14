#!/usr/bin/env python3
"""Run the frozen four-candidate checker unchanged in a new root directory."""
from pathlib import Path
from hashlib import sha256
import datetime
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
def binding(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': sha256(data).hexdigest()}

source = ROOT / 'work/part_d_attack/code/actual_four_order_three_standard.py'
author_output = source.with_name('actual_four_order_three_standard_output.json')
author_stdout = source.with_name('actual_four_order_three_standard_stdout.txt')
assert binding(source)['sha256'] == '8aa61eef553c18b74fd78491d1f2c3c124660237e63a7d8209c03b5a8693d7c5'
expected = '10af2c129561226b60ee444abf5dc5270428686fbf3bdb8d0ce36912cbdf8497'
assert binding(author_output)['sha256'] == binding(author_stdout)['sha256'] == expected
folder = ROOT / 'work/root/actual_four_order_three_standard_independent_replay'
assert not folder.exists()
folder.mkdir()
copied = folder / source.name
copied.write_bytes(source.read_bytes())
assert copied.read_bytes() == source.read_bytes()
proc = subprocess.run([sys.executable, str(copied)], cwd=folder, capture_output=True)
stdout, stderr = folder / 'stdout.txt', folder / 'stderr.txt'
stdout.write_bytes(proc.stdout)
stderr.write_bytes(proc.stderr)
assert proc.returncode == 0 and not proc.stderr
output = folder / author_output.name
assert output.read_bytes() == stdout.read_bytes() == author_output.read_bytes() == author_stdout.read_bytes()
result = json.loads(output.read_text())
assert result['status'] == 'PASS' and result['assertion_count'] == 22
assert len(result['checks']) == 22 and all(row['passed'] for row in result['checks'])
assert result['actual_finite_image_order'] == 1080
assert [row['epsilon_in_M_over_F'] for row in result['rows']] == [1, -1, -1, 1]
assert [row['sigma_in_M_abelianization'] for row in result['rows']] == [1, -1, 1, -1]
assert [row['original_standard_nu'] for row in result['rows']] == [1, -1, 1, -1]
assert [row['original_cusp_word_is_identity_in_this_image'] for row in result['rows']] == [False, False, True, True]
record = {
    'status': 'PASS_UNCHANGED_ISOLATED_ROOT_REPLAY',
    'executed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'command': [sys.executable, str(copied)], 'cwd': str(folder), 'exit_code': proc.returncode,
    'source': binding(source), 'executed_copy': binding(copied),
    'author_output': binding(author_output), 'author_stdout': binding(author_stdout),
    'output': binding(output), 'stdout': binding(stdout), 'stderr': binding(stderr),
    'source_copy_whole_bytes_identical': True,
    'all_four_output_and_stdout_whole_bytes_identical': True,
    'forward_output_transport': 'identity on the complete byte string',
    'inverse_output_transport': 'identity on the complete byte string',
    'named_checks': 22, 'actual_standard_finite_image_order': 1080,
    'epsilon_signs': [1, -1, -1, 1], 'sigma_signs': [1, -1, 1, -1],
    'coefficient_values': [1, -1, 1, -1],
    'finite_nonzero_cusp_witnesses': result['rows'][:2],
    'scope': 'The actual standard h=1,t=tau,w=x is retained. The finite image verifies the named words and witnesses the two failed standard cusp equalities. The full four-point completeness and general-input image statements are assessed in the proof review.'}
comparison = folder / 'comparison.json'
comparison.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'status': record['status'], 'checks': 22, 'image_order': 1080,
                  'comparison': binding(comparison)}, indent=2))
