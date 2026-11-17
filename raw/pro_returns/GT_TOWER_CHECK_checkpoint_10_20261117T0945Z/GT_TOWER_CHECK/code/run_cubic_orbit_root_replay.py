#!/usr/bin/env python3
"""Fresh-copy root replay of the complete marked cubic orbifold layer."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
source=ROOT.parent/'work/tower_code/cubic_orbit_orbifold.py'
dest=ROOT/'notes/reproduced/cubic_orbit_orbifold'
dest.mkdir(parents=True,exist_ok=True)
program=dest/source.name
shutil.copy2(source,program)
start=time.monotonic()
output=program.with_suffix('.out')
with output.open('w') as stream:
    run=subprocess.run([sys.executable,str(program)],cwd=dest,stdout=stream,stderr=subprocess.STDOUT)
record={'program':source.name,'exit':run.returncode,'seconds':round(time.monotonic()-start,3),
        'source_sha256':hashlib.sha256(program.read_bytes()).hexdigest()}
print(json.dumps(record));print(output.read_text())
assert run.returncode==0
(dest/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
