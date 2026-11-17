#!/usr/bin/env python3
"""Fresh-copy root replay of the prime Cartans and finite action source words."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'notes/reproduced/seventh_hour_final'
DEST.mkdir(parents=True,exist_ok=True)
records=[]
for sub,name in (('centralizer_code','check_prime_harmonic_cartans.py'),
                 ('tower_code','finite_pentagon_action_words.py')):
    source=DEST/name
    shutil.copy2(ROOT.parent/'work'/sub/name,source)
    output=source.with_suffix('.out')
    start=time.monotonic()
    with output.open('w') as f:
        run=subprocess.run([sys.executable,str(source)],cwd=DEST,stdout=f,stderr=subprocess.STDOUT)
    record={'program':name,'exit':run.returncode,'seconds':round(time.monotonic()-start,3),
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest()}
    records.append(record)
    print(json.dumps(record));print(output.read_text(),flush=True)
    assert run.returncode==0
(DEST/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS both fresh root finite-action and prime-character certificates.')
