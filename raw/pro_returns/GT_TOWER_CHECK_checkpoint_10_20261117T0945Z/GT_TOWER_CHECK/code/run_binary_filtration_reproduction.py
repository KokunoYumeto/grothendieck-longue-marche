#!/usr/bin/env python3
"""Replay the actual torsion diagonals and the exact first-filtration map."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/binary_filtration'
DEST.mkdir(parents=True, exist_ok=True)
names = ['universal_relation_module_data.json',
         'check_universal_relation_module.py',
         'check_relation_small_quotients.py',
         'check_binary_torsion_diagonals.py',
         'check_binary_first_filtration.py']
records = []
for name in names:
    source = ROOT / 'code' / name
    shutil.copy2(source, DEST / name)
    records.append({'file': name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
for name in names[-2:]:
    program = DEST / name
    with program.with_suffix('.out').open('w') as output:
        result = subprocess.run([sys.executable, str(program)], cwd=DEST,
                                stdout=output, stderr=subprocess.STDOUT)
    print('PROGRAM', name, 'EXIT', result.returncode, flush=True)
    print(program.with_suffix('.out').read_text()[-2500:], flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
(DEST / 'reproduction_manifest.json').write_text(json.dumps(records, indent=2)+'\n')
print('PASS all torsion-diagonal spans and the actual H0/H1 comparison maps.')
