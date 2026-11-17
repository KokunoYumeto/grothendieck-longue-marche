#!/usr/bin/env python3
"""Fresh binary-source replay and exact common-kernel certificate for A.4.52."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work/ghost_code'
DEST=ROOT/'notes/reproduced/common_kernel'
DEST.mkdir(parents=True,exist_ok=True)
files=['fivepoint_signed_level_data.py','check_fivepoint_binary_module.py',
       'check_fivepoint_binary_vertex.py','check_fivepoint_binary_orders.py',
       'check_common_fivepoint_kernel.py','check_fivepoint_signed_retraction.json']
for name in files:shutil.copy2(WORK/name,DEST/name)
old=ROOT/'notes/reproduced/ninth_hour_sources/work/ghost_code'
for stem in ('check_fivepoint_signed_module','check_fivepoint_signed_vertex',
             'check_fivepoint_signed_orders'):
    for ext in ('.json','.npz'):shutil.copy2(old/(stem+ext),DEST/(stem+ext))
records=[]
for name in files[1:5]:
    program=DEST/name;output=program.with_suffix('.out');start=time.monotonic()
    with output.open('w') as stream:
        result=subprocess.run([sys.executable,str(program)],cwd=DEST,
                              stdout=stream,stderr=subprocess.STDOUT)
    record={'program':name,'exit':result.returncode,
            'seconds':round(time.monotonic()-start,3),
            'source_sha256':hashlib.sha256(program.read_bytes()).hexdigest()}
    records.append(record);print(json.dumps(record),flush=True)
    print(output.read_text(),flush=True)
    assert result.returncode==0
(DEST/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS exact common binary/ternary/mod6 kernel with all named source maps.',flush=True)
