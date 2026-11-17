#!/usr/bin/env python3
"""Reproduce the exact Bass--Serre module ranks after the GAP export check."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/universal_relation_module'
DEST.mkdir(parents=True, exist_ok=True)
files = ['check_universal_relation_module.py',
         'universal_relation_module_data.json']
manifest = []
for name in files:
    source = ROOT / 'code' / name
    target = DEST / name
    shutil.copy2(source, target)
    manifest.append({'file': name,
                     'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
program = DEST / files[0]
with program.with_suffix('.out').open('w') as output:
    result = subprocess.run([sys.executable, str(program)], cwd=DEST,
                            stdout=output, stderr=subprocess.STDOUT)
print('Exact module program exit:', result.returncode)
print(program.with_suffix('.out').read_text())
if result.returncode:
    raise SystemExit(result.returncode)
actual = json.loads(program.with_suffix('.json').read_text())
expected = json.loads((ROOT / 'code' / program.with_suffix('.json').name).read_text())
assert actual == expected
print('PASS exact agreement of all graph, homology and matching-coinvariant tables.')
(DEST / 'reproduction_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
