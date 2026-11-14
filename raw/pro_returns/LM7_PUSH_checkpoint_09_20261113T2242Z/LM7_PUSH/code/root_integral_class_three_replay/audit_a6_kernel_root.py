#!/usr/bin/env python3
"""Isolated exact replay of E45 kernel-permutation and outer-bit sources."""
from pathlib import Path
from hashlib import sha256
import ast,json,shutil,subprocess,sys,time
import numpy as np

HERE=Path(__file__).resolve().parent
PROGRAMS=['de_ferrari_a6_kernels','de_ferrari_a6_source_data',
          'de_ferrari_a6_kernel_source','de_ferrari_a6_kernel_corrections',
          'de_ferrari_a6_kernel_compare']
INPUTS=['a_peripheral_a6_outer.json','de_ferrari_sl2_5_N.json','de_ferrari_mod9_module.npz']
STEPS=[('de_ferrari_a6_kernels',[],['de_ferrari_a6_kernels','de_ferrari_a6_kernel_targets']),
       ('de_ferrari_a6_kernel_source',[],['de_ferrari_a6_perm_source']),
       ('de_ferrari_a6_kernel_source',['--outer'],['de_ferrari_a6_outer_source']),
       ('de_ferrari_a6_kernel_corrections',[],['de_ferrari_a6_perm_corrections']),
       ('de_ferrari_a6_kernel_corrections',['--outer'],['de_ferrari_a6_outer_corrections']),
       ('de_ferrari_a6_kernel_compare',[],['de_ferrari_a6_kernel_compare'])]
def digest(p):return sha256(p.read_bytes()).hexdigest()
def stripped(obj):
    if isinstance(obj,dict):return {k:stripped(v) for k,v in obj.items() if k!='seconds'}
    if isinstance(obj,list):return [stripped(v) for v in obj]
    return obj
def dependencies():
    seen=set();todo=list(PROGRAMS)
    while todo:
        name=todo.pop();p=HERE/(name+'.py')
        if name in seen or not p.exists():continue
        seen.add(name)
        for node in ast.walk(ast.parse(p.read_text())):
            if isinstance(node,ast.Import):todo.extend(a.name for a in node.names)
            elif isinstance(node,ast.ImportFrom) and node.module:todo.append(node.module)
    return sorted(seen)
def main():
    start=time.time();replay=HERE/'root_a6_kernel_replay';replay.mkdir(exist_ok=False)
    names=[stem+'.py' for stem in dependencies()]+INPUTS
    protected={name:digest(HERE/name) for name in names}
    outputs=[]
    for _,_,stems in STEPS:
        for stem in stems:
            outputs.extend(p.name for p in HERE.glob(stem+'*')
                if p.is_file() and p.suffix in ('.json','.npz','.out'))
    protected.update({name:digest(HERE/name) for name in outputs})
    for name in names:shutil.copy2(HERE/name,replay/name)
    rows=[];good=True
    for no,(stem,args,outstems) in enumerate(STEPS):
        t=time.time();outpath=replay/(stem+('_outer' if args else '')+'_root_check.out')
        with outpath.open('x') as log:
            proc=subprocess.run([sys.executable,str(replay/(stem+'.py')),*args],
                                cwd=replay,stdout=log,stderr=subprocess.STDOUT)
        row={'program':stem+'.py','arguments':args,'exit_code':proc.returncode,
             'seconds':round(time.time()-t,3),'JSON_comparisons':[],'NPZ_comparisons':[]}
        if proc.returncode:good=False
        else:
            for outstem in outstems:
                a=json.loads((HERE/(outstem+'.json')).read_text())
                b=json.loads((replay/(outstem+'.json')).read_text())
                equal=stripped(a)==stripped(b)
                row['JSON_comparisons'].append({'file':outstem+'.json','mathematical_records_equal':equal})
                good=good and equal
                for p in sorted(replay.glob(outstem+'*.npz')):
                    old=np.load(HERE/p.name);new=np.load(p)
                    assert set(old.files)==set(new.files)
                    changes=[key for key in old.files if not np.array_equal(old[key],new[key])]
                    row['NPZ_comparisons'].append({'file':p.name,'all_arrays_equal':not changes,
                                                   'differing_arrays':changes})
                    good=good and not changes
        rows.append(row);print(json.dumps(row),flush=True)
        if not good:break
    unchanged=all(digest(HERE/n)==h for n,h in protected.items())
    result={'all_passed':good and len(rows)==len(STEPS),'steps':rows,
            'original_artifacts_unchanged':unchanged,'protected_sha256':protected,
            'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    assert result['all_passed'] and unchanged
    print('ROOT_COMPLETE_A6_KERNEL_AND_OUTER_AUDIT_PASS',flush=True)

if __name__=='__main__':main()
