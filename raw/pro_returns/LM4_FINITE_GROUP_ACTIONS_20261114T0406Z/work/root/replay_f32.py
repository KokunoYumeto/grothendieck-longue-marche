#!/usr/bin/env python3
"""Run the frozen F32 literal-word audit in an isolated input directory."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path('/workspace/scratch/64cb59721884')
CODE = ROOT / 'work/part_a/code'
DEST = ROOT / 'work/root/f32_independent_replay'
DEST.mkdir(exist_ok=True)

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def bind(p):
    data = p.read_bytes()
    return {'path': str(p.relative_to(ROOT)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}

checker = CODE / 'affine_nonproduct_r1_independent_audit.py'
reference_path = CODE / 'affine_nonproduct_r1_independent_audit_output.json'
assert digest(checker) == '584b3f7de2e2093ac9c8b04c1c03b962d71b2a4fac7a75545fb9956c0e361482'
assert digest(reference_path) == 'c159761cb68c7750eb54a5be31e8fd41cf25b1a0ba3a0463ad4eab8809eec92a'
reference_bytes = reference_path.read_bytes()
reference = json.loads(reference_bytes)
assert len(reference['inputs']) == 12
input_map = {}
copied = []
for original, expected in reference['inputs'].items():
    src = Path(original)
    assert src.is_relative_to(CODE)
    assert digest(src) == expected
    relative = Path('full_cross_source_stage') / src.name if src.name == 'marginal_braids.json' else Path(src.name)
    target = DEST / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    assert not target.exists(), str(target)
    shutil.copy2(src, target)
    assert target.read_bytes() == src.read_bytes()
    input_map[original] = str(target)
    copied.append(bind(target))
assert len(set(input_map.values())) == 12
target_checker = DEST / checker.name
shutil.copy2(checker, target_checker)
assert target_checker.read_bytes() == checker.read_bytes()
run = subprocess.run([sys.executable, str(target_checker)], cwd=DEST,
                     text=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout_path = DEST / 'stdout.txt'
stderr_path = DEST / 'stderr.txt'
stdout_path.write_bytes(run.stdout)
stderr_path.write_bytes(run.stderr)
assert run.returncode == 0, run.stderr.decode(errors='replace')
actual_path = DEST / reference_path.name
actual_bytes = actual_path.read_bytes()
actual = json.loads(actual_bytes)
assert actual['total_exact_checks'] == 1088
assert actual['check_total'] == 710
assert actual['reviewed_word_and_parser_check_total'] == 378
assert set(actual['inputs']) == set(input_map.values())
inverse_map = {v: k for k, v in input_map.items()}
transported_actual = dict(actual)
transported_actual['inputs'] = {inverse_map[p]: h for p, h in actual['inputs'].items()}
transported_reference = dict(reference)
transported_reference['inputs'] = {input_map[p]: h for p, h in reference['inputs'].items()}
encoded = lambda v: (json.dumps(v, indent=2) + '\n').encode()
assert encoded(transported_actual) == reference_bytes
assert encoded(transported_reference) == actual_bytes
assert actual_bytes != reference_bytes
record = {
    'status': 'PASS', 'exit_code': run.returncode,
    'total_exact_checks': 1088, 'module_checks': 710, 'word_and_parser_checks': 378,
    'raw_output_byte_identical': False,
    'only_difference': 'Exactly the twelve input dictionary keys under the displayed path bijection.',
    'complete_forward_output_byte_equality': True,
    'complete_inverse_output_byte_equality': True,
    'path_map': input_map, 'inverse_path_map': inverse_map,
    'reference': bind(reference_path), 'actual': bind(actual_path),
    'checker': bind(target_checker), 'copied_inputs': copied,
    'stdout': bind(stdout_path), 'stderr': bind(stderr_path),
    'runner': bind(Path(__file__).resolve()),
}
comparison_path = DEST / 'comparison.json'
comparison_path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'checks': 1088,
                  'comparison': bind(comparison_path),
                  'raw_output': bind(actual_path),
                  'whole_output_forward_and_inverse_byte_comparisons': True}, indent=2))
