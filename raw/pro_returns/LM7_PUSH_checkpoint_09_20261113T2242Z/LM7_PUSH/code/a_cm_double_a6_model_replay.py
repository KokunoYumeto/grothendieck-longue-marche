#!/usr/bin/env python3
"""Independent isolated reproduction of the root central-double Ferrari model."""
from pathlib import Path
from hashlib import sha256
import ast,json,shutil,subprocess,time
import numpy as np

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();root=HERE.parent
    target=root/'research/audit_double_a6_model_arithmetic';target.mkdir(exist_ok=False)
    main=HERE/'e_a6_double_model_root.py';inputs={main};queue=[main]
    for path in queue:
        for node in ast.walk(ast.parse(path.read_text())):
            mods=[]
            if isinstance(node,ast.Import):mods=[a.name.split('.')[0] for a in node.names]
            elif isinstance(node,ast.ImportFrom) and node.module:mods=[node.module.split('.')[0]]
            for mod in mods:
                p=HERE/(mod+'.py')
                if p.exists() and p not in inputs:inputs.add(p);queue.append(p)
    inputs |= {HERE/n for n in ('e_a6_double_cover_root.npz','de_ferrari_a6_kernels.npz','de_ferrari_a6_model.npz')}
    protected=inputs | {HERE/('e_a6_double_model_root'+s) for s in ('.json','.npz','.out','.err')}
    hashes={p.name:sha256(p.read_bytes()).hexdigest() for p in protected}
    for p in inputs:shutil.copyfile(p,target/p.name)
    with (target/'replay.out').open('w') as out,(target/'replay.err').open('w') as err:
        subprocess.run(['python',str(target/main.name)],cwd=target,stdout=out,stderr=err,check=True)
    old=json.loads((HERE/'e_a6_double_model_root.json').read_text())
    new=json.loads((target/'e_a6_double_model_root.json').read_text())
    seconds=new.pop('seconds');old.pop('seconds');assert old==new
    a=np.load(HERE/'e_a6_double_model_root.npz');b=np.load(target/'e_a6_double_model_root.npz')
    assert set(a.files)==set(b.files)
    for key in a.files:assert np.array_equal(a[key],b[key]),key
    assert hashes=={p.name:sha256(p.read_bytes()).hexdigest() for p in protected}
    result={'status':'PASS_INDEPENDENT_ISOLATED_DOUBLE_A6_FERRARI_REPLAY',
        'all_mathematical_JSON_fields_equal':True,'all_NPZ_arrays_equal':sorted(a.files),
        'all_protected_original_hashes_unchanged':hashes,'isolated_program_seconds':seconds,
        'seconds':round(time.time()-start,3)}
    (target/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'a_cm_double_a6_model_replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
