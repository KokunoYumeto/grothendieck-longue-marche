#!/usr/bin/env python3
"""Independently rerun the two exact quaternion certificates in a fresh directory.

No precomputed JSON or NPZ input is copied. The first program reconstructs
the free-word action, and the second consumes that newly generated output.
Every transcript and generated certificate is retained under notes/reproduced.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/quaternion_surface'
DEST.mkdir(parents=True, exist_ok=True)
names = ['modular_quaternion_surface.py', 'modular_quaternion_class2.py']
records = []
for name in names:
    source = ROOT / 'code' / name
    target = DEST / name
    shutil.copy2(source, target)
    start = time.monotonic()
    with target.with_suffix('.out').open('w') as stream:
        result = subprocess.run([sys.executable, str(target)], cwd=DEST,
                                stdout=stream, stderr=subprocess.STDOUT)
    record = {'program': name,
              'program_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
              'exit': result.returncode,
              'elapsed_seconds': round(time.monotonic() - start, 3)}
    records.append(record)
    print(json.dumps(record), flush=True)
    if result.returncode:
        print(target.with_suffix('.out').read_text(), flush=True)
        raise SystemExit(result.returncode)

data = json.loads((DEST / 'modular_quaternion_class2.json').read_text())
assert data['joint_linear_base_order'] == 9216
assert data['normal_deck_order'] == 8
assert data['actual_modular_IA_rank'] == 8
assert len(data['records']) == data['CM_base_candidates'] == 36
survivors = [row['mod12_matrix'] for row in data['records']
             if row['lifts_to_CM_centralizer']]
def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) % 12
             for j in range(2)] for i in range(2)]
power = [[1, 0], [0, 1]]
expected = []
for _ in range(6):
    expected.append(power)
    power = multiply(power, [[0, 1], [11, 1]])
assert len(survivors) == 6
assert sorted(survivors) == sorted(expected)
assert [[5, 0], [0, 5]] not in survivors
print('PASS all36 residues; exactly the six literal CM powers survive; 5I excluded.', flush=True)
(DEST / 'reproduction_manifest.json').write_text(json.dumps(records, indent=2)+'\n')
