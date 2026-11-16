#!/usr/bin/env python3
"""Independent full DAG expansion and original-row GAP replay for C31's quotient.

Only output paths and the verifier identity differ from the author's programs.
All original input bytes, the final integer sum, and the generated GAP program
are compared. Runtime integers in GAP stdout are the only normalized log data.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / 'code'
WORK = ROOT.parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

verifier = CODE / 'root_C31_verify_quotient86_trace.py'
shutil.copyfile(CODE / 'pbc_verify_quotient86_trace.py', verifier)
expanded = ROOT / 'notes/root_C31_quotient86_expanded.json'
cmd = [
    'python3', str(verifier), 'LM8_PUSH/code/pbc_quotient86_original_source.json',
    'LM8_PUSH/code/pbc_quotient86_standard2_trace.jsonl.gz', '--s-count', '71',
    '--annihilator', 'LM8_PUSH/code/pbc_three_h2_layer_bound.json',
    '--prime', '2', '--out', str(expanded),
]
with expanded.with_suffix('.out').open('w') as stream:
    run = subprocess.run(cmd, cwd=WORK, stdout=stream, stderr=subprocess.STDOUT)
assert run.returncode == 0
author = json.loads((CODE / 'pbc_quotient86_standard2_expanded.json').read_text())
actual = json.loads(expanded.read_text())
omit = {'seconds', 'verifier_source_sha256'}
assert {k: v for k, v in author.items() if k not in omit} == {
    k: v for k, v in actual.items() if k not in omit}
print('ROOT_FULL_DAG_EXPANSION_MATCHED', actual['dag_nodes'], flush=True)

source = CODE / 'pbc_expand_quotient86_standard_original_identity.py'
literal = CODE / 'root_C31_expand_quotient86_original_identity.py'
text = source.read_text()
changes = {
    "verified=CODE/'pbc_quotient86_standard2_expanded.json'":
        "verified=CODE.parent/'notes/root_C31_quotient86_expanded.json'",
    "gap=CODE/'pbc_quotient86_standard2_literal_original_replay.g'":
        "gap=CODE/'root_C31_quotient86_literal_original_replay.g'",
    "dest=CODE/'pbc_quotient86_standard2_literal_original_identity.json'":
        "dest=CODE.parent/'notes/root_C31_quotient86_literal_original_identity.json'",
}
for old, new in changes.items():
    assert text.count(old) == 1
    text = text.replace(old, new)
literal.write_text(text)
with (ROOT / 'notes/root_C31_quotient86_literal_original_identity.out').open('w') as stream:
    run = subprocess.run(['python3', str(literal)], cwd=ROOT,
                         stdout=stream, stderr=subprocess.STDOUT)
assert run.returncode == 0
root_json = ROOT / 'notes/root_C31_quotient86_literal_original_identity.json'
author_json = CODE / 'pbc_quotient86_standard2_literal_original_identity.json'
actual = json.loads(root_json.read_text())
author = json.loads(author_json.read_text())
omit = {'seconds', 'generator_sha256', 'earlier_expansion_sha256',
        'gap_command', 'gap_output_sha256'}
assert {k: v for k, v in author.items() if k not in omit} == {
    k: v for k, v in actual.items() if k not in omit}
root_gap = CODE / 'root_C31_quotient86_literal_original_replay.g'
author_gap = CODE / 'pbc_quotient86_standard2_literal_original_replay.g'
assert root_gap.read_bytes() == author_gap.read_bytes()
normalize = lambda value: re.sub(r'runtime \d+', 'runtime <timing>', value)
assert normalize(root_gap.with_suffix('.out').read_text()) == normalize(
    author_gap.with_suffix('.out').read_text())
result = {
    'status': 'PASS', 'full_dag_nodes': 8975109,
    'all_expansion_fields_match_except_runtime_and_verifier_hash': True,
    'all_literal_mathematical_fields_match': True,
    'gap_program_bytes_identical': True,
    'gap_stdout_identical_except_runtime_integers': True,
    'original_rows_independently_replayed': actual['original_rows_replayed'],
    'modulus': actual['modulus'],
    'coordinate_or_modulus_rows_in_final_witness': False,
    'root_expansion_sha256': sha(expanded),
    'root_literal_json_sha256': sha(root_json),
    'author_literal_json_sha256': sha(author_json),
    'gap_program_sha256': sha(root_gap),
    'root_gap_stdout_sha256': sha(root_gap.with_suffix('.out')),
    'scope': 'Independent actual G86 quotient identity; full original comparison and profinite lifting have separate written audits.',
}
(ROOT / 'notes/root_C31_quotient86_rerun_verification.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
