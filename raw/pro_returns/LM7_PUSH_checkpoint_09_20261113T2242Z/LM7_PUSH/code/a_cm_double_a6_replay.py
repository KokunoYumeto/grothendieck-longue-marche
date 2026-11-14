#!/usr/bin/env python3
"""Independent isolated reproduction of the root literal SL2(F9) model."""
from pathlib import Path
from hashlib import sha256
import json,shutil,subprocess,time
import numpy as np

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();root=HERE.parent
    target=root/'research/audit_double_a6_group_arithmetic'
    target.mkdir(exist_ok=False)
    code='e_a6_double_cover_root.py';dep='de_ferrari_a6_kernels.npz'
    protected=[code,dep,'e_a6_double_cover_root.json','e_a6_double_cover_root.npz',
               'e_a6_double_cover_root.out','e_a6_double_cover_root.err']
    old={name:sha256((HERE/name).read_bytes()).hexdigest() for name in protected}
    for name in (code,dep):shutil.copyfile(HERE/name,target/name)
    with (target/'replay.out').open('w') as out,(target/'replay.err').open('w') as err:
        subprocess.run(['python',str(target/code)],cwd=target,stdout=out,stderr=err,check=True)
    original=json.loads((HERE/'e_a6_double_cover_root.json').read_text())
    new=json.loads((target/'e_a6_double_cover_root.json').read_text())
    elapsed=new.pop('seconds');original.pop('seconds');assert original==new
    a=np.load(HERE/'e_a6_double_cover_root.npz');b=np.load(target/'e_a6_double_cover_root.npz')
    assert set(a.files)==set(b.files)
    for key in a.files:assert np.array_equal(a[key],b[key]),key
    now={name:sha256((HERE/name).read_bytes()).hexdigest() for name in protected}
    assert old==now
    result={'status':'PASS_INDEPENDENT_ISOLATED_DOUBLE_A6_GROUP_REPLAY',
        'all_mathematical_JSON_fields_equal':True,'all_NPZ_arrays_equal':sorted(a.files),
        'all_protected_original_hashes_unchanged':old,'isolated_program_seconds':elapsed,
        'seconds':round(time.time()-start,3)}
    (target/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'a_cm_double_a6_replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
