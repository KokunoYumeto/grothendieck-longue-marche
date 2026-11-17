#!/usr/bin/env python3
"""Replay post-freeze joint-period and spinor certificates, without a paper claim."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / 'notes/reproduced/quaternion_homology/work'
DEST = ROOT / 'notes/reproduced/quaternion_joint/work'
records = []
for folder in ('tower_code', 'ghost_code'):
    (DEST / folder).mkdir(parents=True, exist_ok=True)
for name in ('translation_quaternion_homology.json',
             'translation_quaternion_homology.npz',
             'translation_quaternion_image.npz',
             'translation_quaternion_radical_certificate.json'):
    shutil.copy2(OLD / 'tower_code' / name, DEST / 'tower_code' / name)
shutil.copy2(OLD / 'ghost_code/check_main_orthogonal_generation.py',
             DEST / 'ghost_code/check_main_orthogonal_generation.py')
for name, folder in [('translation_quaternion_joint_period.py', 'tower_code'),
                     ('check_main_spinor_correction.py', 'ghost_code')]:
    program = DEST / folder / name
    shutil.copy2(ROOT / 'code' / name, program)
    with program.with_suffix('.out').open('w') as output:
        result = subprocess.run([sys.executable, str(program)], cwd=DEST.parent,
                                stdout=output, stderr=subprocess.STDOUT)
    records.append({'program': name, 'exit': result.returncode,
                    'sha256': hashlib.sha256(program.read_bytes()).hexdigest()})
    print(program.with_suffix('.out').read_text(), flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
(DEST.parent / 'reproduction_manifest.json').write_text(json.dumps(records, indent=2)+'\n')
print('PASS pending joint-period and spinor certificates; not added to checkpoint05 paper.')
