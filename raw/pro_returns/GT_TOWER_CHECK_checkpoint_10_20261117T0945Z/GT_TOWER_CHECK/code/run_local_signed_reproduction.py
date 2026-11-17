#!/usr/bin/env python3
"""Rebuild the actual local cover matrices and recompute both complete finite images."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'notes/reproduced/local_signed/work/tower_code'
DEST.mkdir(parents=True,exist_ok=True)
prior=ROOT/'notes/reproduced/sixth_hour_fusion/work/tower_code'
for p in prior.iterdir():
    if p.is_file() and p.suffix in ('.py','.json','.npz'):
        shutil.copy2(p,DEST/p.name)
records=[]
env=os.environ.copy()
runtime=ROOT.parent/'.gapruntime/root'
binary=runtime/'usr/lib/x86_64-linux-gnu/gap/gap'
if binary.exists():
    env['LD_LIBRARY_PATH']=str(runtime/'usr/lib/x86_64-linux-gnu')+(':'+env['LD_LIBRARY_PATH'] if env.get('LD_LIBRARY_PATH') else '')
    gap=[str(binary),'-q','-b','-l',str(runtime/'usr/share/gap')]
else:
    gap=[shutil.which('gap'),'-q','-b']
    assert gap[0]
for name in ('local_braid_quaternion_image','local_mixed_quaternion_census'):
    p=DEST/(name+'.py')
    shutil.copy2(ROOT/'code'/p.name,p)
    for command,output in [([sys.executable,str(p)],p.with_suffix('.out')),
                           (gap+[str(p.with_suffix('.g'))],p.with_suffix('.gap.out'))]:
        started=time.monotonic()
        with output.open('w') as f:
            result=subprocess.run(command,cwd=DEST,env=env,stdout=f,stderr=subprocess.STDOUT)
        transcript=output.read_text()
        errors=[l for l in transcript.splitlines() if l.startswith(('Error,','Syntax error:'))]
        record={'program':Path(command[-1]).name,'exit':result.returncode,
                'gap_errors':len(errors),'seconds':round(time.monotonic()-started,3),
                'source_sha256':hashlib.sha256(Path(command[-1]).read_bytes()).hexdigest()}
        records.append(record)
        print(json.dumps(record),flush=True)
        print(transcript[-4200:],flush=True)
        if result.returncode or errors:
            (DEST.parent.parent/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
            raise SystemExit(1)
(DEST.parent.parent/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS fresh literal source matrices and complete local and signed mixed group computations.')
