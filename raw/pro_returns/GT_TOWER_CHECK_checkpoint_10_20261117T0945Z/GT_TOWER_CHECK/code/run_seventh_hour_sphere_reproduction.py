#!/usr/bin/env python3
"""Fresh root replays of the actual sphere10 binary and cubic certificates."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
DEST=ROOT/'notes/reproduced/seventh_hour_sphere'
DEST.mkdir(parents=True,exist_ok=True)
tasks=[('ghost_code','check_sphere10_binary_extension.py'),
       ('tower_code','sphere10_class3_peripheral.py')]
def replay(task):
    origin,name=task
    target=DEST/origin/name
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(WORK/origin/name,target)
    started=time.monotonic()
    with target.with_suffix('.out').open('w') as f:
        result=subprocess.run([sys.executable,str(target)],cwd=target.parent,
                              stdout=f,stderr=subprocess.STDOUT)
    record={'program':name,'source_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
            'exit':result.returncode,'seconds':round(time.monotonic()-started,3),
            'transcript':str(target.with_suffix('.out').relative_to(ROOT))}
    print(json.dumps(record),flush=True)
    print(target.with_suffix('.out').read_text()[-5000:],flush=True)
    return record
with ThreadPoolExecutor(max_workers=2) as pool:
    records=list(pool.map(replay,tasks))
(DEST/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
assert all(r['exit']==0 for r in records)
print('PASS both fresh literal sphere10 source certificates.')
