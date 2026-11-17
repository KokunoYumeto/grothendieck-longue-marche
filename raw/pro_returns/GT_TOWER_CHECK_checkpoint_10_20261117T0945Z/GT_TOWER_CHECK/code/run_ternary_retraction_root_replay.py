#!/usr/bin/env python3
"""Fresh root replay of the literal five-point retraction and modular gate."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work';DEST=ROOT/'notes/reproduced/ternary_retraction';LOCAL=DEST/'work'
files={'centralizer_code':['check_ternary_modular_centralizer.py'],
       'tower_code':['test_fivepoint_cm_level.py','build_fivepoint_cm_level.py'],
       'ghost_code':['check_fivepoint_signed_retraction.py']}
for directory,names in files.items():
    (LOCAL/directory).mkdir(parents=True,exist_ok=True)
    for name in names:shutil.copy2(WORK/directory/name,LOCAL/directory/name)
records=[]
for relative in ('ghost_code/check_fivepoint_signed_retraction.py',
                 'centralizer_code/check_ternary_modular_centralizer.py'):
    program=LOCAL/relative;output=program.with_suffix('.out');start=time.monotonic()
    with output.open('w') as stream:
        run=subprocess.run([sys.executable,str(program)],cwd=DEST,stdout=stream,stderr=subprocess.STDOUT)
    record={'program':program.name,'exit':run.returncode,'seconds':round(time.monotonic()-start,3),
            'source_sha256':hashlib.sha256(program.read_bytes()).hexdigest()}
    records.append(record);print(json.dumps(record),flush=True);print(output.read_text(),flush=True)
    assert run.returncode==0
(DEST/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
