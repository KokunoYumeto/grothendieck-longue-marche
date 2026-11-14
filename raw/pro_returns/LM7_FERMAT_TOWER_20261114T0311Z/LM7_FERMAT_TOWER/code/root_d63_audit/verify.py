#!/usr/bin/env python3
"""Replay all four frozen D63 sources and compare complete mathematical output."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys

here = Path(__file__).resolve().parent
author = here.parent / 'D63_EXPERIMENTS'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = author / 'ledger/d_compact_orthogonal_cross_manifest.json'
assert sha(manifest) == '91bace632be9d7fbad254e749e73b3c83e14165cd22bfaa847cc18c53a407786'
m = json.loads(manifest.read_text())
assert m['section_sha256'] == 'ee3649710aa1ec1bff151d9b8c9c5298f04cd6faa6815e0c93fc2264a1cbb789'
for row in m['owned_files'] + m['immutable_inputs']:
    p = author / row['path']
    assert sha(p) == row['sha256'], row['path']
    if 'bytes' in row:
        assert p.stat().st_size == row['bytes'], row['path']
fresh = here / 'fresh'
assert not fresh.exists()
fresh.mkdir()

def without_elapsed(obj):
    if isinstance(obj, dict):
        return {k: without_elapsed(v) for k, v in obj.items() if k != 'elapsed_seconds'}
    if isinstance(obj, list):
        return [without_elapsed(v) for v in obj]
    return obj

def stdout_without_elapsed(raw):
    return re.sub(rb'("elapsed_seconds"\s*:\s*)[0-9.eE+-]+', rb'\1<elapsed_seconds>', raw)

runs = []
for stem in m['programs']:
    dest = fresh / stem
    dest.mkdir()
    source = author / 'code' / (stem + '.py')
    shutil.copy2(source, dest / source.name)
    deps = [Path(row['path']).name for row in m['immutable_inputs']]
    if stem != 'd_remaining_compact_modules':
        deps.append('d_remaining_compact_modules.json')
    inputs = []
    for name in deps:
        p = author / 'code' / name
        shutil.copy2(p, dest / name)
        inputs.append({'file': name, 'sha256': sha(p), 'bytes': p.stat().st_size})
    command = [sys.executable, str(dest / source.name)]
    run = subprocess.run(command, cwd=dest, capture_output=True)
    out = dest / (stem + '.out')
    err = dest / (stem + '.err')
    out.write_bytes(run.stdout)
    err.write_bytes(run.stderr)
    assert run.returncode == 0 and not run.stderr, (stem, run.returncode, run.stderr.decode())
    baseline = source.with_suffix('.json')
    reproduced = dest / baseline.name
    assert without_elapsed(json.loads(baseline.read_text())) == without_elapsed(json.loads(reproduced.read_text())), stem + ' complete JSON'
    original_out = source.with_suffix('.out')
    assert stdout_without_elapsed(original_out.read_bytes()) == stdout_without_elapsed(run.stdout), stem + ' complete stdout'
    assert source.read_bytes() == (dest / source.name).read_bytes()
    assert all(sha(dest / dep['file']) == dep['sha256'] for dep in inputs)
    rec = {'program': source.name, 'actual_command': command, 'actual_exit_code': run.returncode,
           'source_sha256': sha(source), 'inputs': inputs,
           'complete_JSON_equal_except_elapsed_seconds': True,
           'complete_stdout_equal_except_elapsed_seconds': True,
           'stderr_bytes': len(run.stderr), 'copied_source_and_inputs_unchanged': True,
           'author_json_sha256': sha(baseline), 'fresh_json_sha256': sha(reproduced),
           'author_stdout_sha256': sha(original_out), 'fresh_stdout_sha256': sha(out),
           'only_excluded_field': 'elapsed_seconds'}
    runs.append(rec)
    print(json.dumps(rec), flush=True)
for row in m['owned_files'] + m['immutable_inputs']:
    assert sha(author / row['path']) == row['sha256'], row['path']
result = {'status': 'PASS', 'statement': 'D.63', 'manifest_sha256': sha(manifest),
          'proof_sha256': m['section_sha256'], 'owned_files_verified': len(m['owned_files']),
          'immutable_inputs_verified': len(m['immutable_inputs']),
          'all_frozen_author_files_unchanged': True, 'complete_fresh_programs': runs,
          'only_excluded_field': 'elapsed_seconds',
          'scope': 'Four complete sources replayed in four fresh copied directories. Every entire JSON and stdout compared. The frozen derived module input is copied exactly and its producer separately fully replayed. Mathematical proof/source audit and peer independent-map execution are recorded separately.'}
(here / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'programs': len(runs), 'record_sha256': sha(here / 'verification.json')}, indent=2), flush=True)
