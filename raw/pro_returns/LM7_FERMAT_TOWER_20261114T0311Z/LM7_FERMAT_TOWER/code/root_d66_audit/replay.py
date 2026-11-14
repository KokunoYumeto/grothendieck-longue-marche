#!/usr/bin/env python3
"""Root fresh replay of every frozen D66 finite calculation."""
from pathlib import Path
import hashlib, json, re, shutil, subprocess, sys, time

W = Path(__file__).resolve().parents[1]
A = Path(__file__).resolve().parent
R = W / 'D66_EXPERIMENTS'
M = R / 'ledger/d_quadratic_compact_source_manifest.json'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(M) == '1d77562247b199c5c78f1a4a8b71d4474a3e7d9d3031f43c3dce7ff5ddb71ada'
m = json.loads(M.read_text())
inputs = json.loads((R / 'input_manifest.json').read_text())

def frozen():
    for row in m['owned_files']:
        p = R / row['path']
        assert p.stat().st_size == row['bytes'] and sha(p) == row['sha256'], row['path']
    for row in inputs:
        assert sha(R / row['path']) == sha(W / row['source']) == row['sha256'], row

frozen()
work = A / 'fresh/code'
fresh = A / 'fresh_outputs'
assert not work.exists() and not fresh.exists()
work.mkdir(parents=True)
fresh.mkdir()
programs = ['d_old_compact_integral', 'd_old_compact_secondary',
            'd_old_compact_relaxation', 'd_old_compact_tate_action',
            'd_old_compact_all_isometries', 'd_old_compact_source_cochain',
            'd_old_compact_quadratic_source', 'd_old_compact_relative_correction',
            'd_old_compact_global_kernel']
for row in inputs:
    shutil.copyfile(R / row['path'], work / Path(row['path']).name)
for name in programs:
    shutil.copyfile(R / 'code' / (name + '.py'), work / (name + '.py'))
shutil.copyfile(M, A / 'author_manifest.json')
shutil.copyfile(R / m['section'], A / 'author_proof.tex')

def without_clock(value):
    result = json.loads(json.dumps(value))
    result['summary'].pop('elapsed_seconds')
    return result

def stdout_without_clock(value):
    return re.sub(r'("elapsed_seconds"\s*:\s*)[-+0-9.eE]+',
                  r'\1<actual elapsed_seconds retained separately>', value)

rows = []
for name in programs:
    start = time.monotonic()
    with (fresh / (name + '.out')).open('wb') as out, (fresh / (name + '.err')).open('wb') as err:
        run = subprocess.run([sys.executable, str(work / (name + '.py'))],
                             cwd=work, stdout=out, stderr=err)
    assert run.returncode == 0, (name, run.returncode, (fresh / (name + '.err')).read_text())
    assert (fresh / (name + '.err')).stat().st_size == 0, name
    j = work / (name + '.json')
    shutil.copyfile(j, fresh / j.name)
    actual = json.loads(j.read_text())
    expected = json.loads((R / 'code' / j.name).read_text())
    assert without_clock(actual) == without_clock(expected), name + ' entire JSON'
    assert stdout_without_clock((fresh / (name + '.out')).read_text()) == stdout_without_clock((R / 'code' / (name + '.out')).read_text()), name + ' entire stdout'
    row = {'program': name + '.py', 'source_sha256': sha(work / (name + '.py')),
           'exit_code': run.returncode, 'entire_JSON_identity_except_summary_elapsed_seconds': True,
           'entire_stdout_identity_except_elapsed_seconds_value': True,
           'fresh_json_sha256': sha(fresh / j.name),
           'fresh_stdout_sha256': sha(fresh / (name + '.out')),
           'fresh_stderr_bytes': 0, 'actual_elapsed_seconds': actual['summary']['elapsed_seconds'],
           'author_elapsed_seconds': expected['summary']['elapsed_seconds'],
           'root_elapsed_seconds': time.monotonic() - start}
    rows.append(row)
    print(json.dumps(row), flush=True)
    # After the complete comparison, restore the frozen raw dependency for
    # the next consumer's exact input hashes. All fresh bytes remain above.
    shutil.copyfile(R / 'code' / j.name, j)

frozen()
result = {'status': 'PASS', 'statement': 'D.66', 'manifest_sha256': sha(M),
          'whole_proof_sha256': sha(A / 'author_proof.tex'),
          'owned_files_checked_before_and_after': len(m['owned_files']),
          'immutable_inputs_checked_before_and_after': inputs,
          'mathematical_programs': rows,
          'excluded_JSON_paths': ['/summary/elapsed_seconds'],
          'excluded_stdout_values': ['elapsed_seconds'],
          'excluded_mathematical_fields_or_input_hashes': [],
          'author_sources_modified': False,
          'downstream_policy': 'Only after entire-result equality is the frozen raw JSON restored for a downstream declared hash; every fresh JSON and stdout/stderr is retained separately.'}
text = json.dumps(result, indent=2) + '\n'
(A / 'replay_audit.json').write_text(text)
print(text, end='')
