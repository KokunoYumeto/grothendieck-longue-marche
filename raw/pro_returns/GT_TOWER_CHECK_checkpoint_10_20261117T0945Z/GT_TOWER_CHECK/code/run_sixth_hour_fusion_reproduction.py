#!/usr/bin/env python3
"""Fresh boundary-form, full period-spinor and literal braid-bridge reproduction."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/sixth_hour_fusion/work'
TOWER, GHOST = DEST / 'tower_code', DEST / 'ghost_code'
TOWER.mkdir(parents=True, exist_ok=True)
GHOST.mkdir(parents=True, exist_ok=True)
previous = ROOT / 'notes/reproduced/sixth_hour_joint/work'
for name, target in [('tower_code', TOWER), ('ghost_code', GHOST)]:
    for source in (previous / name).iterdir():
        if source.is_file() and source.suffix in ('.py', '.json', '.npz'):
            shutil.copy2(source, target / source.name)
records = []
for name, directory in [
    ('check_main_pure_radicals.py', GHOST),
    ('check_main_cover_form.py', GHOST),
    ('check_finite_braid_bridge.py', TOWER),
]:
    program = directory / name
    shutil.copy2(ROOT / 'code' / name, program)
    started = time.monotonic()
    with program.with_suffix('.out').open('w') as output:
        result = subprocess.run([sys.executable, str(program)], cwd=directory,
                                stdout=output, stderr=subprocess.STDOUT)
    record = {'program': name, 'exit': result.returncode,
              'seconds': round(time.monotonic()-started, 3),
              'sha256': hashlib.sha256(program.read_bytes()).hexdigest()}
    records.append(record)
    print(json.dumps(record), flush=True)
    print(program.with_suffix('.out').read_text()[-4500:], flush=True)
    if result.returncode:
        (DEST.parent / 'reproduction_manifest.json').write_text(
            json.dumps(records, indent=2)+'\n')
        raise SystemExit(result.returncode)
(DEST.parent / 'reproduction_manifest.json').write_text(json.dumps(records, indent=2)+'\n')
print('PASS all360 period-spinor pairs, literal cover form, dyadic quotient and all12 braid identities.')
