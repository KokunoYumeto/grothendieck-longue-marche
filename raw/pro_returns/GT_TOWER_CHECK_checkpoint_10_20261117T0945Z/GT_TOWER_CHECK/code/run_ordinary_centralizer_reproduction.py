#!/usr/bin/env python3
"""Fresh root replay of the two exact source paths and ordinary image census."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes/reproduced/ordinary_centralizer'
DEST.mkdir(parents=True, exist_ok=True)
INPUT = ROOT / 'notes/reproduced/geometric_klein'
for name in ('check_sphere10_geometric_klein.json',
             'check_sphere10_geometric_klein.npz',
             'check_sphere10_induced_capped.npz',
             'check_sphere10_quaternary_extension.json'):
    shutil.copy2(INPUT / name, DEST / name)
names = ('check_sphere10_centralizer_motion.py',
         'check_sphere10_geometric_fixed_kernel.py',
         'check_sphere10_ordinary_centralizer_image.py')
for name in names:
    shutil.copy2(ROOT.parent / 'work/ghost_code' / name, DEST / name)

def execute(name):
    program = DEST / name
    output = program.with_suffix('.out')
    start = time.monotonic()
    with output.open('w') as f:
        run = subprocess.run([sys.executable, str(program)], cwd=DEST,
                             stdout=f, stderr=subprocess.STDOUT)
    return {'program': name, 'exit': run.returncode,
            'seconds': round(time.monotonic() - start, 3),
            'source_sha256': hashlib.sha256(program.read_bytes()).hexdigest(),
            'output_sha256': hashlib.sha256(output.read_bytes()).hexdigest()}

records = []
with ThreadPoolExecutor(max_workers=2) as executor:
    for record in executor.map(execute, names[:2]):
        records.append(record)
        print(json.dumps(record), flush=True)
        print((DEST / record['program']).with_suffix('.out').read_text(), flush=True)
        assert record['exit'] == 0
record = execute(names[2])
records.append(record)
print(json.dumps(record), flush=True)
print((DEST / record['program']).with_suffix('.out').read_text(), flush=True)
assert record['exit'] == 0
(DEST / 'manifest.json').write_text(json.dumps(records, indent=2) + '\n')
result = json.loads((DEST / names[2]).with_suffix('.json').read_text())
assert result['E4_motion_image_order'] == 4096
assert result['noncentral_rank'] == 198
assert result['initial_central_rank'] == 98
assert result['central_rank'] == 104
assert len(result['bracket_witnesses']) == 6
assert result['ordinary_image_two_exponent'] == 14
assert result['ordinary_image_three_exponent'] == 302
assert result['finite_centralizer_two_exponent'] == 27
assert result['finite_centralizer_three_exponent'] == 510
assert len(result['Schreier_words']) == 8192
print('PASS all exact path, fixed-kernel and 8192-edge ordinary-image certificates.', flush=True)
