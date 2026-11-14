"""Fresh root execution of the frozen, convention-corrected E107 certificate."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
AUTHOR = ROOT / 'research_e107'
MANIFEST = 'ledger/e_stable_ordinary_manifest.json'
MANIFEST_HASH = 'c0591a02aa9f6e17086c31586cb18e7d156e2859457244bdda06b567856a5c8e'
PROOF_HASH = '2686dbb24643f5f0c083f6d4e1ba6883b08d3fd37f8ebae12cc29219d5838198'
PROGRAM_HASH = 'b86c0a9287659e916f1e4f722aabb119a3cb2842f5ad50f1d3957bece53d95d1'
OUTPUT_HASH = '36909d98ef57ba5849503ea8ff1f60a2c7e01fe4694719f431b65bdf346a5c64'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

assert sha(AUTHOR / MANIFEST) == MANIFEST_HASH
manifest = json.loads((AUTHOR / MANIFEST).read_text())
assert manifest['statement'] == 'E.107'
assert len(manifest['files']) == 22
expected = {}
for item in manifest['files']:
    source = AUTHOR / item['path']
    assert source.stat().st_size == item['bytes'], item['path']
    assert sha(source) == item['sha256'], item['path']
    expected[item['path']] = item['sha256']
assert expected['sections/E_stable_ordinary_phase.tex'] == PROOF_HASH
assert expected['code/e_stable_ordinary_phase.py'] == PROGRAM_HASH
assert expected['code/e_stable_ordinary_phase.json'] == OUTPUT_HASH
assert expected['code/e_stable_ordinary_phase.out'] == OUTPUT_HASH

for relative in ('sections/E_stable_ordinary_phase.tex', 'code/e_stable_ordinary_phase.py',
                 'inputs/e107_e106_complete.json', 'inputs/e107_e88_divisors.json',
                 'inputs/e107_e88_prime_classes.out'):
    destination = HERE / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(AUTHOR / relative, destination)

command = [sys.executable, str(HERE / 'code/e_stable_ordinary_phase.py')]
with (HERE / 'code/e_stable_ordinary_phase.out').open('w') as stream:
    run = subprocess.run(command, cwd=HERE, stdout=stream, stderr=subprocess.STDOUT)
assert run.returncode == 0, run.returncode
comparisons = []
for relative in ('code/e_stable_ordinary_phase.out', 'code/e_stable_ordinary_phase.json'):
    fresh = (HERE / relative).read_bytes()
    frozen = (AUTHOR / relative).read_bytes()
    assert fresh == frozen, relative
    assert sha(HERE / relative) == OUTPUT_HASH
    comparisons.append({'path': relative, 'bytes': len(fresh), 'sha256': sha(HERE / relative),
                        'entire_file_byte_identical': True})
for relative, digest in expected.items():
    assert sha(AUTHOR / relative) == digest, relative
assert sha(AUTHOR / MANIFEST) == MANIFEST_HASH

result = {
    'status': 'PASS', 'statement': 'E.107', 'command': command, 'exit_code': run.returncode,
    'manifest_sha256': MANIFEST_HASH, 'manifest_files_checked': len(expected),
    'proof_sha256': PROOF_HASH, 'program_sha256': PROGRAM_HASH,
    'frozen_input_and_source_sha256': expected, 'comparisons': comparisons,
    'excluded_fields': [], 'author_sources_unchanged': True,
    'scope': ('Fresh copied final Python source and all three complete frozen inputs. '
              'The complete JSON and stdout are byte identical. The final toric tests use '
              'the theorem raw exponent b=3*B17/2 and check both 2*b/3=B17 and 2*b=3*B17. '
              'All 22 manifested author files, including the retained prior convention '
              'and its amendment, were hash checked before and after the replay. '
              'The finite certificate supports the separate all-level proof; it does '
              'not replace that proof.')
}
(HERE / 'comparison.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
