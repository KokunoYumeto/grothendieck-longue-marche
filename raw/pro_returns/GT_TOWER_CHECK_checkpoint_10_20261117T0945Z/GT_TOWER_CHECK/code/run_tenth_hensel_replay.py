#!/usr/bin/env python3
"""Rebuild the integral affine lattice, honest seed and full canonical Jacobian."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT.parent/'work'
OUT=ROOT/'notes/reproduced/tenth_hensel'
assert not OUT.exists(),'Preserve prior replay bytes.'
OUT.mkdir(parents=True)
shutil.copytree(ROOT/'notes/reproduced/tenth_mod12/work',OUT/'work',
                ignore=shutil.ignore_patterns('__pycache__'))
shutil.copytree(WORK/'centralizer_mod4',OUT/'work/centralizer_mod4',dirs_exist_ok=True,
                ignore=shutil.ignore_patterns('__pycache__'))
for name in ['ghost_mod4/check_integral_eight_map.npz',
             'tower_code/check_integral_frame_jacobian.py']:
    target=OUT/'work'/name;target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(WORK/name,target)
programs=['centralizer_mod4/check_integral_affine_system',
          'centralizer_mod4/check_integral_affine_lattice',
          'tower_code/check_integral_frame_jacobian',
          'centralizer_mod4/check_honest_hensel_seed',
          'centralizer_mod4/check_honest_seed_jacobian']
manifest={'source_sha256':{},'runs':[]}
for name in programs:
    script=OUT/'work'/f'{name}.py'
    manifest['source_sha256'][name]=hashlib.sha256(script.read_bytes()).hexdigest()
    start=time.monotonic()
    with script.with_suffix('.out').open('w') as log:
        run=subprocess.run([sys.executable,str(script)],cwd=OUT,stdout=log,stderr=subprocess.STDOUT)
    record={'program':name,'returncode':run.returncode,'seconds':time.monotonic()-start}
    manifest['runs'].append(record)
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    assert run.returncode==0,record
    old=np.load(WORK/f'{name}.npz');new=np.load(script.with_suffix('.npz'))
    assert set(old.files)==set(new.files)
    record['arrays_identical']=[]
    for key in old.files:
        assert np.array_equal(old[key],new[key]),(name,key)
        record['arrays_identical'].append(key)
    print('PASS',name,'arrays',len(record['arrays_identical']),'seconds',round(record['seconds'],3),flush=True)
for name in ['integral_affine_lattice_exact.json','honest_hensel_seed_exact.json']:
    assert json.loads((WORK/'centralizer_mod4'/name).read_text())==json.loads((OUT/'work/centralizer_mod4'/name).read_text()),name
manifest['exact_integer_json_identical']=['integral_affine_lattice_exact.json','honest_hensel_seed_exact.json']
manifest['all_assertions_passed']=True
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('PASS entire integral source, honest seed, and exact constant rank-eight canonical Jacobian.',flush=True)
