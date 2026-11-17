#!/usr/bin/env python3
"""Fresh exact reproduction of the quaternion homology and orthogonal proofs."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/quaternion_homology'
TOWER = DEST / 'work/tower_code'
GHOST = DEST / 'work/ghost_code'
TOWER.mkdir(parents=True, exist_ok=True)
GHOST.mkdir(parents=True, exist_ok=True)
for name in ('translation_cover_basis.json', 'translation_class2_image.json'):
    shutil.copy2(ROOT / 'code' / name, TOWER / name)
shutil.copy2(ROOT / 'notes/reproduced/quaternion_surface/modular_quaternion_surface.json',
             TOWER / 'modular_quaternion_surface.json')
programs = [
    ('modular_quaternion_homology_compressed.py', TOWER),
    ('translation_quaternion_homology.py', TOWER),
    ('translation_quaternion_image.py', TOWER),
    ('translation_quaternion_radical.py', TOWER),
    ('translation_quaternion_radical_certificate.py', TOWER),
    ('check_main_orthogonal_generation.py', GHOST),
]
records = []
for name, directory in programs:
    target = directory / name
    shutil.copy2(ROOT / 'code' / name, target)
    started = time.monotonic()
    with target.with_suffix('.out').open('w') as output:
        result = subprocess.run([sys.executable, str(target)], cwd=DEST,
                                stdout=output, stderr=subprocess.STDOUT)
    record = {'program': name, 'exit': result.returncode,
              'seconds': round(time.monotonic()-started, 3),
              'source_sha256': hashlib.sha256(target.read_bytes()).hexdigest()}
    records.append(record)
    print(json.dumps(record), flush=True)
    if result.returncode:
        print(target.with_suffix('.out').read_text(), flush=True)
        raise SystemExit(result.returncode)
    print(target.with_suffix('.out').read_text()[-2000:], flush=True)
(DEST / 'reproduction_manifest.json').write_text(json.dumps(records, indent=2)+'\n')
print('PASS all six independent reproduction stages.', flush=True)
