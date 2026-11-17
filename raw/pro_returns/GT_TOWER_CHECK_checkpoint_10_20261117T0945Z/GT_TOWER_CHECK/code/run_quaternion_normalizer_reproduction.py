#!/usr/bin/env python3
"""Independently rebuild the marked ordinary first-order normalizer image."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/quaternion_normalizer/work'
TOWER, GHOST = DEST / 'tower_code', DEST / 'ghost_code'
TOWER.mkdir(parents=True, exist_ok=True)
GHOST.mkdir(parents=True, exist_ok=True)
for previous in ('quaternion_homology', 'quaternion_compact'):
    directory = ROOT / 'notes/reproduced' / previous / 'work/tower_code'
    for source in directory.iterdir():
        if source.is_file() and source.suffix in ('.py', '.json', '.npz'):
            shutil.copy2(source, TOWER / source.name)
for name in ('check_main_orthogonal_generation.py',
             'check_main_faithful_detector.py', 'check_main_spinor_correction.py'):
    shutil.copy2(ROOT / 'code' / name, GHOST / name)
records = []
for name, directory in [('quaternion_compact_normalizer_joint.py', TOWER),
                        ('quaternion_compact_normalizer_bridge.py', TOWER),
                        ('check_main_normalizer_joint.py', GHOST)]:
    program = directory / name
    shutil.copy2(ROOT / 'code' / name, program)
    started = time.monotonic()
    with program.with_suffix('.out').open('w') as output:
        result = subprocess.run([sys.executable, str(program)], cwd=DEST.parent,
                                stdout=output, stderr=subprocess.STDOUT)
    record = {'program': name, 'exit': result.returncode,
              'seconds': round(time.monotonic()-started, 3),
              'sha256': hashlib.sha256(program.read_bytes()).hexdigest()}
    records.append(record)
    print(json.dumps(record), flush=True)
    print(program.with_suffix('.out').read_text()[-3500:], flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
(DEST.parent / 'reproduction_manifest.json').write_text(json.dumps(records, indent=2)+'\n')
print('PASS every literal map, all96 source words, all36864 edges and the exact order384*3^6.')
