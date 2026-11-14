#!/usr/bin/env python3
"""Record actual isolated process exits without rewriting historical bytes."""
from pathlib import Path
from hashlib import sha256
import json, shutil, subprocess, sys

dest = Path(__file__).resolve().parent
base = dest.parents[1]
names = [
    ('a_elliptic_tor_symbol_redundant_c_twist', 'a_elliptic_tor_symbol'),
    ('a_theta_principal_distribution_field_coercion', 'a_theta_principal_distribution'),
    ('a_principal_cubic_cover_QZ_conjugation', 'a_principal_cubic_cover'),
    ('a_principal_cubic_cover_handle_shape', 'a_principal_cubic_cover'),
]
inputs = ['a_e120_exact.py', 'a_local_smith.py',
          'a_handle_comparison.json', 'a_cusp_unit_symbols.json',
          'a_handle_torsion_gauge.json', 'a_elliptic_theta_pi.json',
          'a_elliptic_tor_symbol.json', 'a_theta_principal_distribution.json']

def info(p):
    data = p.read_bytes()
    return {'path': str(p.relative_to(base)), 'sha256': sha256(data).hexdigest(),
            'bytes': len(data)}

records = []
for historical, current in names:
    run = dest / historical
    run.mkdir(exist_ok=True)
    for name in inputs:
        shutil.copy2(base / 'code' / name, run / name)
    src = base / 'history' / (historical + '.py')
    shutil.copy2(src, run / (current + '.py'))
    result = subprocess.run([sys.executable, current + '.py'], cwd=run,
                            capture_output=True, timeout=60)
    (run / 'stdout.txt').write_bytes(result.stdout)
    (run / 'stderr.txt').write_bytes(result.stderr)
    assert result.returncode == 1 and result.stdout == b''
    records.append({'historical_source': info(src),
                    'historical_stdout': info(base/'history'/(historical+'.out')),
                    'historical_stderr': info(base/'history'/(historical+'.err')),
                    'replay_command': [sys.executable, current+'.py'],
                    'replay_cwd': str(run.relative_to(base)),
                    'observed_replay_exit_code': result.returncode,
                    'replay_stdout': info(run/'stdout.txt'),
                    'replay_stderr': info(run/'stderr.txt'),
                    'original_exit_artifact': None,
                    'provenance': 'Fresh execution of the unchanged historical source; not a reconstructed original terminal exit record.'})

helper = base/'code/a_e120_exact.py'
result = subprocess.run([sys.executable, str(helper)], capture_output=True,
                        timeout=60)
(dest/'helper_stdout.txt').write_bytes(result.stdout)
(dest/'helper_stderr.txt').write_bytes(result.stderr)
assert result.returncode == 0 and not result.stdout and not result.stderr
output = {'status': 'PASS', 'scope': 'Observed process status for isolated historical-source replays and a silent helper; original history and frozen inputs unchanged',
          'failed_history_replays': records,
          'silent_helper': {'source': info(helper), 'observed_exit_code': result.returncode,
                            'stdout': info(dest/'helper_stdout.txt'),
                            'stderr': info(dest/'helper_stderr.txt'),
                            'role': 'Imported exact arithmetic helper; a standalone silent execution is recorded here.'}}
(dest/'status.json').write_text(json.dumps(output, indent=2)+'\n')
print('PASS: four unchanged historical sources exited 1; the silent helper exited 0')
