#!/usr/bin/env python3
"""Root isolated replay of D47's composite and nonsplit certificates."""
from hashlib import sha256
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent


def digest(path):return sha256(path.read_bytes()).hexdigest()


def main():
    start=time.time()
    stems=['a_cyclic_outer_composite','a_cyclic_outer_nonsplit']
    dependencies=[s+'.py' for s in stems]+['a_relative_prop.py','a_peripheral_count.py']
    names=dependencies+[s+x for s in stems for x in ('.json','.out')]+['a_cyclic_outer_nonsplit_certificate.npz']
    hashes={name:digest(HERE/name) for name in names}
    proof=HERE.parent/'sections/D_cyclic_composite_agent.tex'
    proof_hash=digest(proof)
    replay=HERE/'root_cyclic_composite_replay'
    replay.mkdir(exist_ok=False)
    for name in dependencies:shutil.copy2(HERE/name,replay/name)
    steps=[]
    for stem in stems:
        tick=time.time()
        with (replay/(stem+'_root_check.out')).open('x') as log:
            run=subprocess.run([sys.executable,str(replay/(stem+'.py'))],cwd=replay,
                               stdout=log,stderr=subprocess.STDOUT)
        assert run.returncode==0,stem
        assert (HERE/(stem+'.json')).read_bytes()==(replay/(stem+'.json')).read_bytes()
        if stem.endswith('nonsplit'):
            a,b=np.load(HERE/(stem+'_certificate.npz')),np.load(replay/(stem+'_certificate.npz'))
            assert set(a.files)==set(b.files)
            assert all(np.array_equal(a[key],b[key]) for key in a.files)
        step={'program':stem,'entire_JSON_byte_identical':True,'all_saved_arrays_literal':True,
              'seconds':round(time.time()-tick,3)}
        steps.append(step);print(json.dumps(step),flush=True)
    assert digest(proof)==proof_hash
    assert all(digest(HERE/name)==value for name,value in hashes.items())
    result={'all_passed':True,'original_artifacts_unchanged':True,'proof_sha256':proof_hash,
            'steps':steps,'protected_sha256':hashes,'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
