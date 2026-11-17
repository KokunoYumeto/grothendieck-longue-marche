#!/usr/bin/env python3
"""Fresh root checks of the finite cusp graph and full harmonic matrix formula."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/eighth_hour_initial'
DEST.mkdir(parents=True, exist_ok=True)
tasks = [('tower_code', 'finite_cusp_cycle.py'),
         ('centralizer_code', 'check_full_harmonic_formula.py')]
for folder, name in tasks:
    shutil.copy2(ROOT.parent / 'work' / folder / name, DEST / name)

def run(task):
    _, name = task
    program = DEST / name
    output = program.with_suffix('.out')
    start = time.monotonic()
    with output.open('w') as stream:
        result = subprocess.run([sys.executable, str(program)], cwd=DEST,
                                stdout=stream, stderr=subprocess.STDOUT)
    return {'program': name, 'exit': result.returncode,
            'seconds': round(time.monotonic() - start, 3),
            'source_sha256': hashlib.sha256(program.read_bytes()).hexdigest(),
            'output_sha256': hashlib.sha256(output.read_bytes()).hexdigest()}

with ThreadPoolExecutor(max_workers=2) as executor:
    records = list(executor.map(run, tasks))
for record in records:
    print(json.dumps(record), flush=True)
    print((DEST / record['program']).with_suffix('.out').read_text(), flush=True)
    assert record['exit'] == 0
(DEST / 'manifest.json').write_text(json.dumps(records, indent=2) + '\n')
graph = json.loads((DEST / 'finite_cusp_cycle.json').read_text())
assert graph['maps_checked'] == 216
harmonic = json.loads((DEST / 'check_full_harmonic_formula.json').read_text())
assert len(harmonic['checks']) == 9 and harmonic['status'] == 'PASS'
assert harmonic['checks'][0]['full_pair_products_checked'] == 4096
assert harmonic['checks'][1]['full_pair_products_checked'] == 16384
print('PASS fresh root graph-cycle and signed whole-group harmonic checks.', flush=True)
