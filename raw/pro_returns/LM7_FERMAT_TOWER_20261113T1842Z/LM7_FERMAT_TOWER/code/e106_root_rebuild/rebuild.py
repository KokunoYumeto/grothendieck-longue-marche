"""Fresh independent execution of the frozen E106 mathematical certificate."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
AUTHOR = ROOT / 'research_e106'
GP = ROOT / 'research_e52/vendor/pari-2.19.0/gp'
expected = {
 'sections/E_next_ordinary_classes.tex':'efff588437574576cdd3cb823c671eccd59da2d5faa8a09f98a6002a8459c249',
 'code/e_next_unit_characters.py':'dcc98681e4200bbd4bc563f619044d2303e5395914a243e2041f2464f854e457',
 'code/e_next_prime_maps.gp':'a6968cc12a75ec565945281eb592f66a1176ca7121b24d888cc1fd73b930f1e0',
 'code/e_next_unit_characters.json':'c2ab58a8a059c7564f9032277627a09daa8f3c0811603d40a32c0650ca5dd9da',
 'code/e_next_unit_characters.out':'c2ab58a8a059c7564f9032277627a09daa8f3c0811603d40a32c0650ca5dd9da',
 'code/e_next_prime_maps.out':'a5f7d5bace308762adf8bc99aae3b0a663099f87c029c751a5c47687d3dbcb46',
}
dependencies = json.loads((AUTHOR / 'ledger/e_next_ordinary_dependencies.json').read_text())
for item in dependencies['input_files']:
    expected[item['path']] = item['sha256']
assert len(dependencies['input_files']) == 6
for relative,digest in expected.items():
    assert hashlib.sha256((AUTHOR / relative).read_bytes()).hexdigest() == digest, relative
    dest = HERE / relative
    dest.parent.mkdir(parents=True, exist_ok=True)
    if relative.startswith(('inputs/','sections/')) or relative.endswith(('.py','.gp')):
        shutil.copy2(AUTHOR / relative, dest)

command = [sys.executable, str(HERE / 'code/e_next_unit_characters.py'), '--gp', str(GP)]
with (HERE / 'code/e_next_unit_characters.out').open('w') as stream:
    run = subprocess.run(command, cwd=HERE, stdout=stream, stderr=subprocess.STDOUT)
assert run.returncode == 0, run.returncode
comparison = []
for relative in ('code/e_next_unit_characters.out','code/e_next_unit_characters.json','code/e_next_prime_maps.out'):
    actual = (HERE / relative).read_bytes()
    frozen = (AUTHOR / relative).read_bytes()
    assert actual == frozen, relative
    comparison.append({'path':relative, 'bytes':len(actual), 'sha256':hashlib.sha256(actual).hexdigest(),
                       'entire_file_byte_identical':True})
for relative,digest in expected.items():
    assert hashlib.sha256((AUTHOR / relative).read_bytes()).hexdigest() == digest, relative
result = {'status':'PASS', 'command':command, 'exit_code':run.returncode,
          'proof_sha256':expected['sections/E_next_ordinary_classes.tex'],
          'frozen_input_and_source_sha256':expected,
          'comparisons':comparison, 'excluded_fields':[],
          'scope':'Fresh copied final Python/GP sources and all six complete frozen inputs. PARI recertified B1 and recomputed literal prime7/73 ray Frobenii. The full Python pipeline rechecked all19683 character residues and every finite class map. Complete JSON and both entire stdout files agree byte for byte. No upper BNF was computed.'}
(HERE / 'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
