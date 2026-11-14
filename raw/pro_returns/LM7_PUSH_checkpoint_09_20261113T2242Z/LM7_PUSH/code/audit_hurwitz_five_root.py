#!/usr/bin/env python3
"""Isolated replay of every E46 target, source and comparison map.

Every literal array is compared exactly.  Differing subgroup generating
lists must define the same subgroup by both inclusions in the faithful
permutation representation.  Each provenance hash is checked against
its own actual input file before elapsed-time metadata are separated.
"""
from pathlib import Path
from hashlib import sha256
import ast,json,shutil,subprocess,sys,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).resolve().parent
STEPS=['e_hurwitz_five_a5_model_root','e_hurwitz_five_source_root',
       'e_hurwitz_five_corrections_root','e_hurwitz_five_compare_root',
       'e_hurwitz_five_boundary_root']
INPUTS=['e_hurwitz_five_a5_order_pure_root.json','e_hurwitz_five_a5_order_pure_root.npz',
        'de_ferrari_sl2_5_N.json','de_ferrari_mod9_module.npz','de_ferrari_fibres.json',
        'de_ferrari_two_lift.json','de_ferrari_degree6_kernel.json',
        'de_ferrari_two_degree6_module.json','de_fermat_schreier.json']
def digest(p):return sha256(p.read_bytes()).hexdigest()
def mathematical(obj):
    if isinstance(obj,dict):return {k:mathematical(v) for k,v in obj.items()
                                  if k not in ('seconds','input_sha256')}
    if isinstance(obj,list):return [mathematical(v) for v in obj]
    return obj
def dependencies():
    seen=set();todo=list(STEPS)
    while todo:
        stem=todo.pop();p=HERE/(stem+'.py')
        if stem in seen or not p.exists():continue
        seen.add(stem)
        for n in ast.walk(ast.parse(p.read_text())):
            if isinstance(n,ast.Import):todo.extend(a.name for a in n.names)
            elif isinstance(n,ast.ImportFrom) and n.module:todo.append(n.module)
    return sorted(seen)
def main():
    start=time.time();replay=HERE/'root_hurwitz_five_replay';replay.mkdir(exist_ok=False)
    inputs=[stem+'.py' for stem in dependencies()]+INPUTS
    protected={n:digest(HERE/n) for n in inputs}
    for stem in STEPS:
        protected.update({p.name:digest(p) for p in HERE.glob(stem+'*') if p.is_file()})
    for n in inputs:shutil.copy2(HERE/n,replay/n)
    rows=[]
    for stem in STEPS:
        t=time.time()
        with (replay/(stem+'_root_check.out')).open('x') as log:
            proc=subprocess.run([sys.executable,str(replay/(stem+'.py'))],cwd=replay,
                                stdout=log,stderr=subprocess.STDOUT)
        assert proc.returncode==0,stem
        old=json.loads((HERE/(stem+'.json')).read_text())
        new=json.loads((replay/(stem+'.json')).read_text())
        provenance=[]
        for location,data in ((HERE,old),(replay,new)):
            for n,h in data.get('input_sha256',{}).items():
                assert digest(location/n)==h,(stem,str(location),n)
                provenance.append(n)
        assert mathematical(old)==mathematical(new),stem
        arrays=[]
        for p in sorted(replay.glob(stem+'*.npz')):
            a,b=np.load(HERE/p.name),np.load(p);assert set(a.files)==set(b.files)
            records=[]
            for key in a.files:
                if np.array_equal(a[key],b[key]):
                    records.append({'array':key,'literally_equal':True});continue
                assert key.endswith('generators'),(p.name,key)
                aa,bb=a[key],b[key]
                assert aa.ndim==bb.ndim==2 and aa.shape[1]==bb.shape[1]
                expected=np.arange(aa.shape[1])
                assert np.all(np.sort(aa,axis=1)==expected) and np.all(np.sort(bb,axis=1)==expected)
                A=PermutationGroup([Permutation(g.tolist()) for g in aa])
                B=PermutationGroup([Permutation(g.tolist()) for g in bb])
                assert all(B.contains(g) for g in A.generators)
                assert all(A.contains(g) for g in B.generators)
                ao,bo=int(A.order()),int(B.order());assert ao==bo
                records.append({'array':key,'literally_equal':False,
                    'old_in_new':True,'new_in_old':True,'common_subgroup_order':ao})
            arrays.append({'file':p.name,'all_arrays_mathematically_equal':True,'arrays':records})
        row={'program':stem+'.py','exit_code':0,'all_mathematical_records_equal':True,
             'all_declared_input_hashes_verified':True,
             'provenance_files':sorted(set(provenance)),'NPZ_comparisons':arrays,
             'seconds':round(time.time()-t,3)}
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ('NPZ_comparisons','provenance_files')}),flush=True)
    unchanged=all(digest(HERE/n)==h for n,h in protected.items());assert unchanged
    result={'all_passed':True,'steps':rows,'original_artifacts_unchanged':True,
            'protected_sha256':protected,'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ROOT_FIVE_POINT_HURWITZ_COMPLETE_AUDIT_PASS',flush=True)

if __name__=='__main__':main()
