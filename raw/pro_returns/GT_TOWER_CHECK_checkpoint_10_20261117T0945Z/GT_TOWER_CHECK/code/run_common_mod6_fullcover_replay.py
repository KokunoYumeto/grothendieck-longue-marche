#!/usr/bin/env python3
"""Replay the selected actual automorphism and full integral cover correction."""
from pathlib import Path
import hashlib,json,shutil,subprocess,time
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
OUT=ROOT/'notes/reproduced/common_mod6_fullcover'
OUT.mkdir(parents=True,exist_ok=True)
for name in ['centralizer_code','ghost_code','tower_code']:
    shutil.copytree(WORK/name,OUT/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
records=[]
for name in ['check_common_mod6_liftable_automorphism.py','check_common_mod6_canonical_correction.py']:
    source=OUT/'centralizer_code'/name
    start=time.monotonic()
    proc=subprocess.run(['python3',str(source)],cwd=OUT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log=OUT/(source.stem+'.root.out');log.write_text(proc.stdout)
    record={'program':name,'exit':proc.returncode,'seconds':round(time.monotonic()-start,3),
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'output_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}
    records.append(record)
    (OUT/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(record),flush=True)
    print(proc.stdout,flush=True)
    assert proc.returncode==0
print('PASS selected common-mod6 automorphism and exact integral canonical-cover correction.',flush=True)
