#!/usr/bin/env python3
"""Fresh root replays of the quaternary, induced and quaternion certificates."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, time

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
DEST=ROOT/'notes/reproduced/seventh_hour_additional'
DEST.mkdir(parents=True,exist_ok=True)
sources=[
    (WORK/'ghost_code', 'check_sphere10_quaternary_extension.py'),
    (WORK/'ghost_code', 'check_sphere10_binary_extension.json'),
    (WORK/'ghost_code', 'check_sphere10_induced_capped.py'),
    (WORK/'ghost_code', 'check_main_mixed_capping.npz'),
    (WORK/'centralizer_code', 'check_source_affine_brunnian.py'),
]
for parent,name in sources:
    shutil.copy2(parent/name,DEST/name)
records=[]
for name in ('check_sphere10_quaternary_extension.py',
             'check_sphere10_induced_capped.py',
             'check_source_affine_brunnian.py'):
    source=DEST/name
    output=source.with_suffix('.out')
    start=time.monotonic()
    with output.open('w') as f:
        result=subprocess.run([sys.executable,str(source)],cwd=DEST,
                              stdout=f,stderr=subprocess.STDOUT)
    record={'program':name,'exit':result.returncode,
            'seconds':round(time.monotonic()-start,3),
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest()}
    records.append(record)
    print(json.dumps(record),flush=True)
    print(output.read_text()[-3500:],flush=True)
    assert result.returncode==0
(DEST/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS all three independently copied additional certificates.')
