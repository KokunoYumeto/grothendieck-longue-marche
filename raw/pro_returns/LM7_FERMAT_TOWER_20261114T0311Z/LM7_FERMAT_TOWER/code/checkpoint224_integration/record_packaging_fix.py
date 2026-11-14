"""Preserve a failed archive check and identify a captured in-progress stdout.

The E121 amendment script copied its own tree before its final print. The
copied empty stdout is retained byte for byte and linked to the completed run.
"""
from pathlib import Path
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parents[2]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

history = BASE / 'code/checkpoint224_integration/history/first_package_attempt'
assert not history.exists()
history.mkdir(parents=True)
for source, target in [
    (BASE / 'code/package.py', 'package.py'),
    (BASE.parent / 'root_package224.out', 'package.out'),
    (BASE.parent / 'root_package224.err', 'package.err'),
]:
    shutil.copy2(source, history / target)
assert (history / 'package.out').stat().st_size == 0
assert (history / 'package.err').stat().st_size > 0
status = {
    'status': 'failed before result', 'exit_code': 1,
    'reason': 'Archive validation encountered the amendment script stdout copied while that same run was in progress, before its final print.',
    'stderr_path': 'package.err', 'stderr_sha256': sha(history / 'package.err'),
    'source_sha256': sha(history / 'package.py'),
}
(history / 'package_status.json').write_text(json.dumps(status, indent=2) + '\n')

snapshot = 'code/e121_bundle/audit/pre_final_typing/full_tree/code/e53_final_typing_amend.py'
completed = 'code/e121_bundle/code/e53_final_typing_amend.py'
actual_stdout = str(Path(completed).with_suffix('.out'))
assert sha(BASE / snapshot) == sha(BASE / completed)
assert (BASE / Path(snapshot).with_suffix('.out')).stat().st_size == 0
assert (BASE / actual_stdout).stat().st_size > 0
actual = json.loads((BASE / actual_stdout).read_text())
assert actual['status'] == 'PASS'
assert actual == json.loads((BASE / 'code/e121_bundle/audit/e121_final_typing.json').read_text())
entry = {
    'status': 'copied during a subsequently completed run',
    'reason': 'shutil.copytree(ROOT, stage) copied the already redirected stdout before the amendment script reached its final print. This is a historical filesystem snapshot, not a separate execution or its completed output.',
    'source_sha256': sha(BASE / snapshot),
    'snapshot_stdout_sha256': sha(BASE / Path(snapshot).with_suffix('.out')),
    'completed_program': completed,
    'completed_stdout': actual_stdout,
    'completed_stdout_sha256': sha(BASE / actual_stdout),
    'completed_result_status': 'PASS',
    'evidence': 'The preserved identical source executes copytree before writing the two proof changes, audit record and final JSON stdout. The completed stdout equals that audit record exactly.',
}
registry = BASE / 'ledger/execution_snapshot_outputs.json'
assert not registry.exists()
registry.write_text(json.dumps({snapshot: entry}, indent=2) + '\n')
print(json.dumps({
    'status': 'PASS', 'failed_package_attempt_preserved': str(history.relative_to(BASE)),
    'snapshot_registry': str(registry.relative_to(BASE)),
    'snapshot_registry_sha256': sha(registry),
    'original_snapshot_and_author_freeze_unchanged': True,
    'completed_stdout_sha256': entry['completed_stdout_sha256'],
}, indent=2))
