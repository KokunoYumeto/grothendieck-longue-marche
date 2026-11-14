#!/usr/bin/env python3
"""Root byte-exact replay of the frozen elliptic logarithm-torsor subresult."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys

W = Path(__file__).resolve().parents[1]
A = Path(__file__).resolve().parent
R = W / 'research_e120'
M = R / 'ledger/a_elliptic_log_torsor_manifest.json'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(M) == 'c288aafb2017b0fcc0da339ddc63e7c3404736e0b1a9bdd27d3241e7ab789d90'
m = json.loads(M.read_text())

def frozen():
    for row in m['owned'] + m['immutable_inputs']:
        p = R / row['path']
        assert p.stat().st_size == row['bytes'] and sha(p) == row['sha256'], row['path']

frozen()
work = A / 'log_torsor_fresh'
assert not work.exists()
work.mkdir()
for row in m['immutable_inputs']:
    dest = work / row['path']
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(R / row['path'], dest)
for name in ['a_log_torsor_pairing_probe', 'a_elliptic_log_torsor']:
    shutil.copyfile(R / 'code' / (name + '.py'), work / 'code' / (name + '.py'))
shutil.copyfile(M, A / 'log_torsor_author_manifest.json')
shutil.copyfile(R / 'notes/elliptic_log_torsor.md', A / 'log_torsor_author_note.md')
rows = []
for name in ['a_log_torsor_pairing_probe', 'a_elliptic_log_torsor']:
    with (work / 'code' / (name + '.out')).open('wb') as out, (work / 'code' / (name + '.err')).open('wb') as err:
        run = subprocess.run([sys.executable, 'code/' + name + '.py'], cwd=work, stdout=out, stderr=err)
    assert run.returncode == 0, (name, run.returncode, (work / 'code' / (name + '.err')).read_text())
    checks = []
    for suffix in ['.out', '.err', '.json']:
        p = work / 'code' / (name + suffix)
        reference = R / 'code' / p.name
        assert p.read_bytes() == reference.read_bytes(), p.name
        checks.append({'file': p.name, 'bytes': p.stat().st_size,
                       'sha256': sha(p), 'complete_byte_identity': True})
    row = {'program': name + '.py', 'exit_code': run.returncode, 'source_sha256': sha(work / 'code' / (name + '.py')), 'outputs': checks}
    rows.append(row)
    print(json.dumps(row), flush=True)
frozen()
result = {'status': 'PASS', 'frozen_manifest_sha256': sha(M),
          'whole_note_sha256': sha(A / 'log_torsor_author_note.md'),
          'owned_files_checked_before_and_after': len(m['owned']),
          'immutable_inputs_checked_before_and_after': len(m['immutable_inputs']),
          'programs': rows, 'excluded_fields': [], 'author_sources_modified': False}
text = json.dumps(result, indent=2) + '\n'
(A / 'log_torsor_replay_audit.json').write_text(text)
print(text, end='')
