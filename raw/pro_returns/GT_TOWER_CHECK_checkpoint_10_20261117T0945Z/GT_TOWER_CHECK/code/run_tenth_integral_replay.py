#!/usr/bin/env python3
"""Reproduce both integral target/source certificates in an isolated layout."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT.parent/'work'
OUT=ROOT/'notes/reproduced/tenth_integral'
assert not OUT.exists(), 'Preserve each earlier replay.'
OUT.mkdir(parents=True)
files=['ghost_code/fivepoint_signed_level_data.py',
 'ghost_code/check_fivepoint_binary_module.npz',
 'ghost_mod4/check_fivepoint_quartic_module.py',
 'ghost_mod4/check_fivepoint_quartic_mixed_module.npz',
 'ghost_mod4/check_target_integral_smith.py',
 'ghost_mod4/check_integral_eight_map.py']
manifest={'input_sha256':{},'runs':[]}
for name in files:
    dst=OUT/name;dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(WORK/name,dst)
    manifest['input_sha256'][name]=hashlib.sha256(dst.read_bytes()).hexdigest()
for name in ['check_target_integral_smith','check_integral_eight_map']:
    script=OUT/'ghost_mod4'/f'{name}.py'
    start=time.monotonic()
    with script.with_suffix('.out').open('w') as log:
        run=subprocess.run([sys.executable,str(script)],cwd=OUT,stdout=log,stderr=subprocess.STDOUT)
    row={'name':name,'returncode':run.returncode,'seconds':time.monotonic()-start}
    manifest['runs'].append(row)
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    assert run.returncode==0,row
    old=np.load(WORK/'ghost_mod4'/f'{name}.npz')
    new=np.load(script.with_suffix('.npz'))
    assert set(old.files)==set(new.files)
    row['arrays_identical']=[]
    for key in old.files:
        assert np.array_equal(old[key],new[key]),(name,key)
        row['arrays_identical'].append(key)
    row['maximum_absolute_saved_integer']=max(int(np.abs(new[key]).max())
      for key in new.files if np.issubdtype(new[key].dtype,np.integer) and new[key].size)
    print('PASS',name,'arrays',len(row['arrays_identical']),'seconds',round(row['seconds'],3),flush=True)
manifest['all_assertions_passed']=True
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('PASS full integral target Smith form and primitive actual eight-map common source.',flush=True)
