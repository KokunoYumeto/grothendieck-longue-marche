#!/usr/bin/env python3
"""Fresh root replays of the common source, full harmonic frame, and odd join.

The widened integer replay is retained separately. It checks that no finite
integer overflow can affect the modular matrix factorizations used in A.4.48.
"""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent / 'work'
DEST = ROOT / 'notes/reproduced/ninth_hour_sources'
LOCAL = DEST / 'work'
files = {
    'ghost_code': ['fivepoint_signed_level_data.py',
                   'check_fivepoint_signed_module.py',
                   'check_fivepoint_signed_vertex.py',
                   'check_fivepoint_signed_orders.py',
                   'check_fivepoint_signed_retraction.json',
                   'check_cap_odd_join.py',
                   'check_main_mixed_capping.npz'],
    'centralizer_code': ['check_modular_harmonic_base_frame.g',
                         'check_central_certificate_replay.g',
                         'cap216_genuine_source_data.g'],
}
for directory, names in files.items():
    (LOCAL / directory).mkdir(parents=True, exist_ok=True)
    for name in names:
        shutil.copy2(WORK / directory / name, LOCAL / directory / name)

runtime = ROOT.parent / '.gapruntime/root'
env = os.environ.copy()
env['LD_LIBRARY_PATH'] = str(runtime / 'usr/lib/x86_64-linux-gnu') + (
    ':' + env['LD_LIBRARY_PATH'] if env.get('LD_LIBRARY_PATH') else '')
gap = [str(runtime / 'usr/lib/x86_64-linux-gnu/gap/gap'),
       '-q', '-b', '-l', str(runtime / 'usr/share/gap')]


def run_program(command, output, cwd=DEST):
    start = time.monotonic()
    with output.open('w') as stream:
        result = subprocess.run(command, cwd=cwd, env=env,
                                stdout=stream, stderr=subprocess.STDOUT)
    transcript = output.read_text()
    errors = [line for line in transcript.splitlines()
              if line.startswith(('Error,', 'Syntax error:'))]
    record = {'program': str(Path(command[-1]).relative_to(DEST)),
              'exit': result.returncode, 'gap_errors': len(errors),
              'seconds': round(time.monotonic() - start, 3),
              'source_sha256': hashlib.sha256(Path(command[-1]).read_bytes()).hexdigest()}
    print(json.dumps(record), flush=True)
    print(transcript[-6500:], flush=True)
    assert result.returncode == 0 and not errors
    return record


def source_replay():
    records = []
    for name in ('check_fivepoint_signed_module.py',
                 'check_fivepoint_signed_vertex.py',
                 'check_fivepoint_signed_orders.py',
                 'check_cap_odd_join.py'):
        program = LOCAL / 'ghost_code' / name
        records.append(run_program([sys.executable, str(program)], program.with_suffix('.out')))
    wide = DEST / 'int64_replay'
    wide.mkdir(exist_ok=True)
    for name in files['ghost_code'][:5]:
        source = LOCAL / 'ghost_code' / name
        if source.suffix == '.py':
            (wide / name).write_text(source.read_text().replace('np.int16', 'np.int64'))
        else:
            shutil.copy2(source, wide / name)
    for name in ('check_fivepoint_signed_module.py',
                 'check_fivepoint_signed_vertex.py',
                 'check_fivepoint_signed_orders.py'):
        program = wide / name
        records.append(run_program([sys.executable, str(program)], program.with_suffix('.out')))
    import numpy as np
    compared = {}
    for stem in ('check_fivepoint_signed_module', 'check_fivepoint_signed_vertex',
                 'check_fivepoint_signed_orders'):
        with np.load(LOCAL / 'ghost_code' / (stem + '.npz')) as first, \
             np.load(wide / (stem + '.npz')) as second:
            assert set(first.files) == set(second.files)
            for key in first.files:
                assert np.array_equal(first[key], second[key]), (stem, key)
            compared[stem] = len(first.files)
    (DEST / 'int64_exact_comparison.json').write_text(json.dumps(compared, indent=2) + '\n')
    print('PASS independent int64 replay reproduces every retained exact matrix.', flush=True)
    return records


def harmonic_replay():
    program = LOCAL / 'centralizer_code/check_modular_harmonic_base_frame.g'
    return [run_program(gap + [str(program)], program.with_suffix('.out'))]


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    futures = [pool.submit(source_replay), pool.submit(harmonic_replay)]
    records = [record for future in futures for record in future.result()]
(DEST / 'manifest.json').write_text(json.dumps(records, indent=2) + '\n')
print('PASS exact source module, orders, odd join, and full canonical harmonic-frame projection.', flush=True)
