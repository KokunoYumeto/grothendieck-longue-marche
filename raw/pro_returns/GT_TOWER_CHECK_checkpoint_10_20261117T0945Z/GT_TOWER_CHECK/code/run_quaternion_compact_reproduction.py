#!/usr/bin/env python3
"""Reproduce the actual compact quaternion target and its source-word map."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/quaternion_compact'
TOWER = DEST / 'work/tower_code'
GHOST = DEST / 'work/ghost_code'
TOWER.mkdir(parents=True, exist_ok=True)
GHOST.mkdir(parents=True, exist_ok=True)
inputs = ['modular_quaternion_surface.py', 'modular_quaternion_surface.json',
          'modular_quaternion_homology_compressed.npz',
          'translation_cover_basis.json',
          'translation_quaternion_homology.json',
          'translation_quaternion_homology.npz']
records = []
for name in inputs:
    source = ROOT / 'code' / name
    shutil.copy2(source, TOWER / name)
    records.append({'input': name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
programs = [('modular_quaternion_compact_setup.py', TOWER),
            ('modular_quaternion_compact_census.py', TOWER),
            ('modular_quaternion_compact_faithful.py', TOWER),
            ('check_main_faithful_detector.py', GHOST)]
for name, directory in programs:
    program = directory / name
    shutil.copy2(ROOT / 'code' / name, program)
    started = time.monotonic()
    with program.with_suffix('.out').open('w') as output:
        result = subprocess.run([sys.executable, str(program)], cwd=DEST,
                                stdout=output, stderr=subprocess.STDOUT)
    record = {'program': name, 'exit': result.returncode,
              'seconds': round(time.monotonic()-started, 3),
              'sha256': hashlib.sha256(program.read_bytes()).hexdigest()}
    records.append(record)
    print(json.dumps(record), flush=True)
    print(program.with_suffix('.out').read_text()[-2500:], flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
(DEST / 'reproduction_manifest.json').write_text(json.dumps(records, indent=2)+'\n')
print('PASS compact ideal, complete CM census, literal map, all36 boundaries and intrinsic kernel.')
