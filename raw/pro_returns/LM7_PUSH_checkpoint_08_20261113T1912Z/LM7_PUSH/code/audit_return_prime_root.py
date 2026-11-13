#!/usr/bin/env python3
"""Root replay of the complete D46 kernel and centralizer certificates."""
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


def mathematics(value):
    if isinstance(value,dict):
        return {key:(sorted(item) if key=='input_sha256' else mathematics(item))
                for key,item in value.items() if key!='seconds'}
    if isinstance(value,list):
        return [mathematics(item) for item in value]
    return value


def validate_inputs(value, directory):
    for name, expected in value.get('input_sha256',{}).items():
        assert digest(directory/name)==expected, (str(directory),name)


def main():
    start = time.time()
    dependencies = ['bc_return_prime_model.py','bc_return_prime_centralizers.py',
                    'de_ferrari_a6_source_data.py','de_ferrari_sl2_5_N.json']
    stems = [f'bc_return_prime_l{ell}_p{p}{suffix}'
             for ell,p in ((5,7),(7,5)) for suffix in ('','_centralizers')]
    names = dependencies+[stem+suffix for stem in stems for suffix in ('.out','.json','.npz')]
    protected = {name:digest(HERE/name) for name in names}
    proof = HERE.parent/'sections/D_return_prime_agent.tex'
    proof_hash = digest(proof)
    replay = HERE/'root_return_prime_replay'
    replay.mkdir(exist_ok=False)
    for name in dependencies:
        shutil.copy2(HERE/name,replay/name)
    steps = []
    for ell,p in ((5,7),(7,5)):
        for program,suffix in (('bc_return_prime_model',''),('bc_return_prime_centralizers','_centralizers')):
            stem = f'bc_return_prime_l{ell}_p{p}{suffix}'
            tick = time.time()
            with (replay/(stem+'_root_check.out')).open('x') as log:
                run = subprocess.run([sys.executable,str(replay/(program+'.py')),
                                      '--ell',str(ell),'--prime',str(p)],cwd=replay,
                                     stdout=log,stderr=subprocess.STDOUT)
            assert run.returncode==0, stem
            old = json.loads((HERE/(stem+'.json')).read_text())
            new = json.loads((replay/(stem+'.json')).read_text())
            validate_inputs(old,HERE)
            validate_inputs(new,replay)
            assert mathematics(old)==mathematics(new), stem
            a,b = np.load(HERE/(stem+'.npz')),np.load(replay/(stem+'.npz'))
            assert set(a.files)==set(b.files)
            for key in a.files:
                assert np.array_equal(a[key],b[key]), (stem,key)
            step = {'program':program,'ell':ell,'prime':p,'all_mathematical_JSON_equal':True,
                    'all_NPZ_arrays_literal':True,'own_location_input_hashes_verified':True,
                    'seconds':round(time.time()-tick,3)}
            steps.append(step)
            print(json.dumps(step),flush=True)
    assert all(digest(HERE/name)==value for name,value in protected.items())
    assert digest(proof)==proof_hash
    result = {'all_passed':True,'steps':steps,'proof_sha256':proof_hash,
              'original_artifacts_unchanged':True,'protected_sha256':protected,
              'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__ == '__main__':
    main()
