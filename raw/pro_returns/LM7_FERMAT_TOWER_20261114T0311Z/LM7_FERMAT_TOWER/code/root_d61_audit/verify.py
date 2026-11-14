"""Independent root replay of all four complete frozen D.61 programs."""
from pathlib import Path
import subprocess, shutil, json, hashlib, re, sys

ROOT = Path(__file__).resolve().parents[1]
AUDIT = Path(__file__).resolve().parent
SOURCE = ROOT / 'D61_EXPERIMENTS'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = SOURCE / 'ledger/d_remaining_projective_rows_manifest.json'
assert sha(manifest) == '2685a1c4f9ca12f7c285bcee1f5dcfe875e64e26e084faff7532cd35d8677bde'
data = json.loads(manifest.read_text())
allfiles = data['files'] + data['immutable_inputs']
for row in allfiles:
    p = SOURCE / row['path']
    assert sha(p) == row['sha256'] and p.stat().st_size == row['bytes'], row['path']
before_author = {row['path']: sha(SOURCE / row['path']) for row in allfiles}

def omit_time(x):
    if isinstance(x, dict):
        return {k: omit_time(v) for k, v in x.items() if k != 'elapsed_seconds'}
    if isinstance(x, list):
        return [omit_time(v) for v in x]
    return x

def omit_stdout_time(s):
    return re.sub(r'("elapsed_seconds"\s*:\s*)[0-9.eE+-]+', r'\1<elapsed>', s)

rows = []
for name in data['run_order']:
    target = AUDIT / 'replay' / Path(name).stem
    target.mkdir(parents=True, exist_ok=False)
    files = [name] + data['replay_dependencies'][name]
    for f in files:
        shutil.copy2(SOURCE / 'code' / f, target / f)
    before = {f: sha(target / f) for f in files}
    out = target / Path(name).with_suffix('.out')
    js = target / Path(name).with_suffix('.json')
    with out.open('wb') as log:
        run = subprocess.run([sys.executable, str(target / name)], cwd=target,
                             stdout=log, stderr=subprocess.STDOUT)
    assert run.returncode == 0, (name, run.returncode)
    a = json.loads(js.read_text())
    b = json.loads((SOURCE / 'code' / js.name).read_text())
    row = {
        'program': name, 'actual_exit_code': run.returncode,
        'entire_json_equal_except_elapsed_seconds': omit_time(a) == omit_time(b),
        'entire_stdout_equal_except_elapsed_seconds':
            omit_stdout_time(out.read_text()) == omit_stdout_time((SOURCE / 'code' / out.name).read_text()),
        'source_and_input_sha256': before,
        'source_inputs_unchanged': before == {f: sha(target / f) for f in files},
        'output_sha256': sha(out), 'json_sha256': sha(js)
    }
    assert all(row[k] for k in ['entire_json_equal_except_elapsed_seconds',
                               'entire_stdout_equal_except_elapsed_seconds',
                               'source_inputs_unchanged']), name
    rows.append(row)
    print(json.dumps(row), flush=True)
assert all(sha(SOURCE / rel) == value for rel, value in before_author.items())
record = {
    'statement': 'D.61', 'status': 'PASS', 'author_manifest_sha256': sha(manifest),
    'author_manifest_files_verified': len(data['files']),
    'immutable_inputs_verified': len(data['immutable_inputs']),
    'method': 'Each complete program in a separate copied directory with its exact frozen inputs. The stage-three upstream certificate is freshly rebuilt and fully compared; stage four reads its frozen bytes so the input hash is also compared exactly.',
    'programs': rows, 'only_excluded_key': 'elapsed_seconds',
    'author_files_unchanged': True,
    'proof_verification_claimed_by_this_program': False
}
(AUDIT / 'verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'programs': len(rows)}), flush=True)
