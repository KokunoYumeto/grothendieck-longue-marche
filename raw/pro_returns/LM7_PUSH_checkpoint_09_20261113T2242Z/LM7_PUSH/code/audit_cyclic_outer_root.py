#!/usr/bin/env python3
"""Isolated root replay of both D45 literal cyclic-outer certificates."""
from hashlib import sha256
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    start = time.time()
    stems = ['a_cyclic_outer_phase', 'a_cyclic_outer_shapiro']
    dependencies = ['a_relative_prop.py', 'a_peripheral_count.py']+[s+'.py' for s in stems]
    artifacts = [s+suffix for s in stems for suffix in ('.out','.json','_certificate.npz')]
    proof = HERE.parent/'sections/D_cyclic_outer_agent.tex'
    protected = {name:digest(HERE/name) for name in dependencies+artifacts}
    proof_hash = digest(proof)
    replay = HERE/'root_cyclic_outer_replay'
    replay.mkdir(exist_ok=False)
    for name in dependencies:
        shutil.copy2(HERE/name,replay/name)
    steps = []
    for stem in stems:
        tick = time.time()
        with (replay/(stem+'_root_check.out')).open('x') as log:
            result = subprocess.run([sys.executable,str(replay/(stem+'.py'))],
                                    cwd=replay,stdout=log,stderr=subprocess.STDOUT)
        assert result.returncode == 0, stem
        assert (HERE/(stem+'.json')).read_bytes() == (replay/(stem+'.json')).read_bytes(), stem
        old,new = np.load(HERE/(stem+'_certificate.npz')),np.load(replay/(stem+'_certificate.npz'))
        assert set(old.files) == set(new.files)
        for key in old.files:
            assert np.array_equal(old[key],new[key]), (stem,key)
        step = {'program':stem,'JSON_byte_identical':True,
                'all_NPZ_arrays_literal':True,'array_names':old.files,
                'seconds':round(time.time()-tick,3)}
        steps.append(step)
        print(json.dumps(step),flush=True)
    assert all(digest(HERE/name)==value for name,value in protected.items())
    assert digest(proof)==proof_hash
    result = {'all_passed':True,'steps':steps,'proof_sha256':proof_hash,
              'protected_sha256':protected,'original_artifacts_unchanged':True,
              'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__ == '__main__':
    main()
