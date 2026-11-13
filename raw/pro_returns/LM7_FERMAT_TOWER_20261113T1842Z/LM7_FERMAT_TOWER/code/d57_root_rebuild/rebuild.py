"""Fresh root replay of all six final D57 stages and their literal outputs."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'D57_EXPERIMENTS'
MANIFEST = AUTHOR / 'ledger/d_arithmetic_class2_repair_manifest.json'
EXPECTED = 'f213a0d93c952965e97a6064a04e4960ce669368e01a24e596f5138ebf093aff'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(MANIFEST) == EXPECTED
manifest = json.loads(MANIFEST.read_text())
all_files = manifest['files'] + manifest['immutable_inputs']
for item in all_files:
    p = AUTHOR / item['path']
    assert p.stat().st_size == item['bytes'], item['path']
    assert sha(p) == item['sha256'], item['path']
copy_paths = [x['path'] for x in manifest['immutable_inputs']]
copy_paths += ['code/' + name for name in manifest['run_order']]
copy_paths += ['sections/D_arithmetic_class2_repair.tex']
for relative in copy_paths:
    dest = HERE / relative
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(AUTHOR / relative, dest)

def without_elapsed(obj):
    if isinstance(obj, dict):
        return {k:without_elapsed(v) for k,v in obj.items() if k != 'elapsed_seconds'}
    if isinstance(obj, list):
        return [without_elapsed(v) for v in obj]
    return obj

elapsed = re.compile(r'("elapsed_seconds"\s*:\s*)[0-9]+(?:\.[0-9]+)?')
checks = []
for name in manifest['run_order']:
    path = HERE / 'code' / name
    command = [sys.executable, str(path)]
    with path.with_suffix('.out').open('w') as stream:
        run = subprocess.run(command, cwd=HERE, stdout=stream, stderr=subprocess.STDOUT)
    assert run.returncode == 0, (name, run.returncode)
    fresh_json = json.loads(path.with_suffix('.json').read_text())
    author_json = json.loads((AUTHOR / 'code' / name).with_suffix('.json').read_text())
    assert without_elapsed(fresh_json) == without_elapsed(author_json), name + ' complete JSON'
    fresh_out = path.with_suffix('.out').read_text()
    author_out = (AUTHOR / 'code' / name).with_suffix('.out').read_text()
    assert elapsed.sub(r'\1<elapsed>', fresh_out) == elapsed.sub(r'\1<elapsed>', author_out), name + ' complete stdout'
    assert len(elapsed.findall(fresh_out)) == len(elapsed.findall(author_out))
    item = {'program':name, 'command':command, 'exit_code':run.returncode,
            'source_sha256':sha(path), 'fresh_json_sha256':sha(path.with_suffix('.json')),
            'fresh_stdout_sha256':sha(path.with_suffix('.out')),
            'entire_json_equal_except_elapsed_seconds':True,
            'entire_stdout_equal_except_elapsed_seconds':True,
            'stdout_elapsed_value_count':len(elapsed.findall(fresh_out)),
            'fresh_elapsed_seconds':fresh_json['summary']['elapsed_seconds']}
    checks.append(item)
    print(json.dumps(item), flush=True)

for item in all_files:
    assert sha(AUTHOR / item['path']) == item['sha256'], item['path']
assert sha(MANIFEST) == EXPECTED
result = {'status':'PASS', 'statement':'D.57', 'manifest_sha256':EXPECTED,
          'proof_sha256':sha(HERE / 'sections/D_arithmetic_class2_repair.tex'),
          'all_manifested_files_and_inputs_checked':len(all_files),
          'copied_complete_inputs':manifest['immutable_inputs'], 'checks':checks,
          'excluded_fields':['elapsed_seconds'], 'author_sources_unchanged':True,
          'scope':'Every mathematical source, all two immutable D56 inputs and the final proof were copied. The six dependent stages ran in the frozen order. Every complete JSON and stdout agrees except the explicitly named runtime values. No polynomial coefficient, matrix, word, local correction, framing case or failed-attempt metadata is excluded.'}
(HERE / 'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
