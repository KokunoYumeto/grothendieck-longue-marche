#!/usr/bin/env python3
"""Rebuild the exact mixed coefficient-four target and both insertion maps."""
from pathlib import Path
import hashlib,json,shutil,subprocess,time
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
OUT=ROOT/'notes/reproduced/tenth_quartic'
files=['ghost_code/fivepoint_signed_level_data.py','ghost_code/check_fivepoint_binary_module.npz',
       'ghost_mod4/check_fivepoint_quartic_module.py','ghost_mod4/check_fivepoint_quartic_mixed_module.py']
hashes={}
for name in files:
    target=OUT/name;target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(WORK/name,target)
    hashes[name]=hashlib.sha256(target.read_bytes()).hexdigest()
source=OUT/files[-1]
start=time.monotonic()
proc=subprocess.run(['python3',str(source)],cwd=OUT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(OUT/'replay.out').write_text(proc.stdout)
record={'source_hashes':hashes,'exit':proc.returncode,'seconds':round(time.monotonic()-start,3)}
assert proc.returncode==0,proc.stdout
original=np.load(WORK/'ghost_mod4/check_fivepoint_quartic_mixed_module.npz',allow_pickle=True)
fresh=np.load(source.with_suffix('.npz'),allow_pickle=True)
assert original.files==fresh.files
record['exact_array_comparison']={key:bool(np.array_equal(original[key],fresh[key])) for key in original.files}
assert all(record['exact_array_comparison'].values())
(OUT/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(proc.stdout)
print(json.dumps(record,indent=2))
print('PASS complete mixed target and both-direction common coefficient-four source maps.')
