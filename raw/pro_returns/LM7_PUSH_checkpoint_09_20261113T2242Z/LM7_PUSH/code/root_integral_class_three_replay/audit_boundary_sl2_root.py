#!/usr/bin/env python3
"""Independent isolated replay of the actual P20-to-SL2-source quotient map."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time
import numpy as np
from audit_sl2_source_root import digest, mathematical

HERE = Path(__file__).resolve().parent
REPLAY = HERE/'root_e43_replay'
STEM = 'de_sl2_boundary_quotient'
INPUTS = ('de_ferrari_a5_source_compressed.npz',
          'de_ferrari_sl2_5_source.json', 'de_ferrari_sl2_5_derived.json',
          'de_ferrari_sl2_5_Nprime.json', 'de_ferrari_sl2_5_Fprime.json',
          'de_fermat_schreier.json')


def main():
    assert not REPLAY.exists()
    REPLAY.mkdir()
    protected = [HERE/n for n in (*INPUTS, STEM+'.py', STEM+'.json', STEM+'.npz', STEM+'.out')]
    before = {p.name:digest(p) for p in protected}
    for name in (*INPUTS, STEM+'.py'):
        shutil.copy2(HERE/name,REPLAY/name)
    output = REPLAY/(STEM+'_root_check.out')
    start = time.time()
    with output.open('x') as stream:
        run = subprocess.run([sys.executable,'-u',str(REPLAY/(STEM+'.py'))],
                             cwd=REPLAY,stdout=stream,stderr=subprocess.STDOUT)
    assert run.returncode == 0
    a = mathematical(json.loads((HERE/(STEM+'.json')).read_text()))
    b = mathematical(json.loads((REPLAY/(STEM+'.json')).read_text()))
    assert a == b
    with np.load(HERE/(STEM+'.npz')) as original,np.load(REPLAY/(STEM+'.npz')) as fresh:
        assert set(original.files) == set(fresh.files)
        assert all(np.array_equal(original[k],fresh[k]) for k in original.files)
    assert all(digest(HERE/n) == h for n,h in before.items())
    result = {'all_passed':True,'original_artifacts_unchanged':True,
              'all_mathematical_json_and_npz_equal':True,
              'source_model_elements':a['all_F_model_elements_enumerated'],
              'H_image_order':a['H_image_order'],'H_exponent':a['H_exponent'],
              'actual_B_map_factors_through_P20':a['actual_B_map_factors_through_P20'],
              'protected_sha256':before,'output_sha256':digest(output),
              'elapsed_seconds':round(time.time()-start,3)}
    (HERE/'audit_boundary_sl2_root.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='protected_sha256'},indent=2))
    print('ROOT_SL2_FULL_BOUNDARY_QUOTIENT_AUDIT_PASS')


if __name__ == '__main__':
    main()
