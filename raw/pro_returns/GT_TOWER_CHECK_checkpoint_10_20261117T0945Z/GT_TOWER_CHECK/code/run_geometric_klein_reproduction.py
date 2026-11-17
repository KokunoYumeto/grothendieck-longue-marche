#!/usr/bin/env python3
"""Fresh-copy root replay of every exact rotation-path and image certificate."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'notes/reproduced/geometric_klein'
DEST.mkdir(parents=True,exist_ok=True)
SOURCE=ROOT.parent/'work/ghost_code/check_sphere10_geometric_klein.py'
program=DEST/SOURCE.name
shutil.copy2(SOURCE,program)
for name in ('check_sphere10_induced_capped.npz','check_sphere10_quaternary_extension.json'):
    shutil.copy2(ROOT/'notes/reproduced/seventh_hour_additional'/name,DEST/name)
output=program.with_suffix('.out')
start=time.monotonic()
with output.open('w') as f:
    run=subprocess.run([sys.executable,str(program)],cwd=DEST,stdout=f,stderr=subprocess.STDOUT)
record={'program':program.name,'exit':run.returncode,'seconds':round(time.monotonic()-start,3),
        'source_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),
        'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest()}
(DEST/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record));print(output.read_text())
assert run.returncode==0
data=json.loads(program.with_suffix('.json').read_text())
assert len(data['all_pair_polynomials'])==2
assert all(len(rows)==45 for rows in data['all_pair_polynomials'])
assert [len(rows) for rows in data['crossing_certificates']]==[38,34]
assert [len(word) for word in data['source_H_words']]==[90,86]
print('PASS all90 exact pair-polynomial records,72 signed events and full geometric H replay.')
