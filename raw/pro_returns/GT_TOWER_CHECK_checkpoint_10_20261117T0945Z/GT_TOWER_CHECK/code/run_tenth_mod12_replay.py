#!/usr/bin/env python3
"""Fresh selected modulus-twelve gate replay in an isolated minimal layout."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
OUT=ROOT/'notes/reproduced/tenth_mod12'
assert not OUT.exists(), 'Preserve prior replay bytes; use a new directory.'
OUT.mkdir(parents=True)
paths=[
 'tower_code/test_fivepoint_cm_level.py',
 'tower_code/build_fivepoint_cm_level.py',
 'ghost_mod4/check_fivepoint_quartic_mixed_module.npz',
 'ghost_code/check_fivepoint_binary_module.npz',
 'centralizer_code/check_common_mod6_liftable_automorphism.npz',
 'centralizer_code/check_common_mod6_canonical_correction.npz',
 'centralizer_mod4/lift_mask31_mod4.py',
 'centralizer_mod4/lift_mask31_mod4.npz',
 'centralizer_mod4/check_modular_quaternary_central_model.npz',
 'centralizer_mod4/check_mod4_canonical_lift.py',
 'centralizer_mod4/check_selected_mod4_automorphism.py']
manifest={'inputs':{},'runs':[]}
for rel in paths:
    src=WORK/rel;dst=OUT/'work'/rel
    dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,dst)
    manifest['inputs'][rel]=hashlib.sha256(src.read_bytes()).hexdigest()
for name in ['check_mod4_canonical_lift','check_selected_mod4_automorphism']:
    script=OUT/'work/centralizer_mod4'/f'{name}.py'
    start=time.monotonic()
    with script.with_suffix('.out').open('w') as log:
        done=subprocess.run([sys.executable,str(script)],cwd=OUT,stdout=log,stderr=subprocess.STDOUT)
    record={'program':name,'returncode':done.returncode,'seconds':time.monotonic()-start}
    manifest['runs'].append(record)
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    assert done.returncode==0,record
    expected=np.load(WORK/'centralizer_mod4'/f'{name}.npz')
    actual=np.load(script.with_suffix('.npz'))
    assert set(expected.files)==set(actual.files)
    matched=[]
    for key in expected.files:
        assert np.array_equal(expected[key],actual[key]),(name,key)
        matched.append(key)
    record['all_arrays_identical']=matched
    record['output_sha256']=hashlib.sha256(script.with_suffix('.npz').read_bytes()).hexdigest()
    print('PASS',name,'arrays',len(matched),'seconds',round(record['seconds'],3),flush=True)
manifest['all_assertions_passed']=True
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('PASS full integral canonical defect and actual finite automorphism replay.',flush=True)
