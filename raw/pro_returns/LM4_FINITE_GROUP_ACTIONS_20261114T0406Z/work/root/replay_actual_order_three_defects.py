#!/usr/bin/env python3
"""Execute the unchanged D order-three verifier in a fresh isolated directory."""
from pathlib import Path
from hashlib import sha256
import datetime
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sha = lambda p: sha256(p.read_bytes()).hexdigest()
def binding(p):
    return {'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size, 'sha256': sha(p)}

source = ROOT / 'work/part_d_attack/code/actual_order_three_defects.py'
author_output = source.with_name('actual_order_three_defects_output.json')
author_stdout = source.with_name('actual_order_three_defects_stdout.txt')
assert sha(source) == 'ca6b10f52c3be47e6835d8fec7ea45faf63f62474338d86df54496661806e5eb'
expected = '634910286efa79d802c6c08efa0f131b987b9ea2f329bccb0e0b22927fe6a5d4'
assert sha(author_output) == sha(author_stdout) == expected
folder = ROOT / 'work/root/actual_order_three_defects_independent_replay'
assert not folder.exists()
folder.mkdir()
copied = folder / source.name
copied.write_bytes(source.read_bytes())
assert copied.read_bytes() == source.read_bytes()
proc = subprocess.run([sys.executable, str(copied)], cwd=folder, capture_output=True)
stdout = folder / 'stdout.txt'
stderr = folder / 'stderr.txt'
stdout.write_bytes(proc.stdout)
stderr.write_bytes(proc.stderr)
assert proc.returncode == 0 and not proc.stderr
output = folder / author_output.name
assert output.read_bytes() == stdout.read_bytes() == author_output.read_bytes() == author_stdout.read_bytes()
result = json.loads(output.read_text())
assert result['status'] == 'PASS' and result['assertion_count'] == 24
assert len(result['checks']) == 24 and all(x['passed'] for x in result['checks'])
assert result['defect_case_count'] == 644 and result['c_word_count'] == 161
assert result['finite_nonzero_separations_by_prime'] == {'3': 598, '5': 44}
assert result['simultaneous_solutions_in_corpus'] == [
    {'nu': -1, 'epsilon': 1, 'c': 'y'}, {'nu': 1, 'epsilon': -1, 'c': 'x^-1'}]
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
    'named_checks': 24, 'reduced_original_words': 161, 'defect_cases': 644,
    'finite_nonzero_separations': 642, 'finite_separations_by_prime': {'3': 598, '5': 44},
    'exact_zero_triples': result['simultaneous_solutions_in_corpus'],
    'scope': 'Actual standard h=1,g=x^-1,w=x and full units nu=-1,+1; aggregate counts and the first finite witness in each branch are serialized, and the deterministic verifier checks every case. No remaining original h is assigned.'}
comparison = folder / 'comparison.json'
comparison.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': record['status'], 'checks': 24, 'cases': 644,
                  'finite_separations': 642, 'comparison': binding(comparison)}, indent=2))
