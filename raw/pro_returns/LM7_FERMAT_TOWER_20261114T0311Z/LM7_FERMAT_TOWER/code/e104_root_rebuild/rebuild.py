"""Fresh exact copied E104 run with complete byte comparisons."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / 'research_e104'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
code = HERE / 'code'
code.mkdir(exist_ok=True)
program = SOURCE / 'code/e_two_prime_full_family.py'
inp = ROOT / 'research_e100/code/a_s23_full.json'
assert sha(inp) == '9ed2ac3d9f612b757882d1c696e43c3a65c80f6dba8235d8d4f6883e36c480d1'
assert sha(SOURCE / 'sections/E_two_prime_full_family.tex') == 'a9d8bd8db19de52e1b4a44290626af971f0f30b30408633072e2966a40ec8e48'
for source in [program, inp]:
    assert not (code / source.name).exists()
    shutil.copyfile(source, code / source.name)
target = code / program.name
with target.with_suffix('.out').open('w') as out:
    result = subprocess.run([sys.executable, str(target), '--input', str(code / inp.name)],
                            cwd=HERE, stdout=out, stderr=subprocess.STDOUT, check=False)
assert result.returncode == 0
comparisons = []
for ext in ['.py', '.json', '.out']:
    a = program.with_suffix(ext)
    b = target.with_suffix(ext)
    assert a.read_bytes() == b.read_bytes(), ext
    comparisons.append({'file': a.name, 'sha256': sha(a), 'bytes': a.stat().st_size,
                        'complete_bytes_equal': True, 'excluded_fields': []})
assert sha(code / inp.name) == sha(inp)
record = {'status': 'PASS', 'complete_comparisons': comparisons,
          'input_sha256': sha(inp), 'section_sha256': sha(SOURCE / 'sections/E_two_prime_full_family.tex'),
          'command': ['python3', 'code/e_two_prime_full_family.py', '--input', 'code/a_s23_full.json'],
          'returncode': result.returncode}
(HERE / 'comparison.json').write_text(json.dumps(record, indent=2) + '\n')
print('PASS fresh E104 computation; complete program/JSON/stdout byte equality, no exclusions.', flush=True)
