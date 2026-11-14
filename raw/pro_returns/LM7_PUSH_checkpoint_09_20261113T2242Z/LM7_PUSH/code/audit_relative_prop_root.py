#!/usr/bin/env python3
"""Isolated replay of D41's literal maps and exact elementary-generator gates."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def main():
    start = time.time()
    stem = 'a_relative_prop'
    names = ['a_peripheral_count.py']+[stem+ext for ext in ('.py','.out','.json')]
    protected = {name:digest(HERE/name) for name in names}
    replay = HERE/'root_relative_prop_replay'
    replay.mkdir(exist_ok=False)
    for name in ['a_peripheral_count.py',stem+'.py']:
        shutil.copy2(HERE/name,replay/name)
    with (replay/(stem+'_root_check.out')).open('x') as log:
        run = subprocess.run([sys.executable,str(replay/(stem+'.py'))],
                             cwd=replay,stdout=log,stderr=subprocess.STDOUT)
    assert run.returncode == 0
    original,repeated=HERE/(stem+'.json'),replay/(stem+'.json')
    assert json.loads(original.read_text())==json.loads(repeated.read_text())
    assert original.read_bytes()==repeated.read_bytes()
    data=json.loads(repeated.read_text())
    orders=[r['generated_order'] for r in data['full_finite_symplectic_generation']]
    assert orders==[720,24]
    assert all(digest(HERE/name)==value for name,value in protected.items())
    result={'all_passed':True,'entire_JSON_byte_identical':True,
            'actual_word_maps_and_inverses_replayed':True,
            'elementary_symplectic_generator_orders':orders,
            'original_artifacts_unchanged':True,
            'protected_sha256':protected,
            'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
