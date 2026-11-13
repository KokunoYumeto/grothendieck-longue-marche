#!/usr/bin/env python3
"""Resolve generator-choice differences, then finish the E45 replay.

The first audit is retained unchanged.  Two derived-subgroup generating
lists differ, so this driver proves equality by both subgroup inclusions
in the identical faithful permutation representation.  It checks every
other array literally and runs only the two previously unrun steps.
"""
from pathlib import Path
import json,subprocess,sys,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from audit_a6_kernel_root import HERE,STEPS,digest,stripped

REPLAY=HERE/'root_a6_kernel_replay'
def compare_npz(name):
    old=np.load(HERE/name);new=np.load(REPLAY/name)
    assert set(old.files)==set(new.files)
    records=[]
    for key in old.files:
        if np.array_equal(old[key],new[key]):
            records.append({'array':key,'literally_equal':True});continue
        assert key.endswith('generators'),(name,key)
        a,b=old[key],new[key]
        assert a.ndim==b.ndim==2 and a.shape[1]==b.shape[1]
        expected=np.arange(a.shape[1])
        assert np.all(np.sort(a,axis=1)==expected) and np.all(np.sort(b,axis=1)==expected)
        A=PermutationGroup([Permutation(p.tolist()) for p in a])
        B=PermutationGroup([Permutation(p.tolist()) for p in b])
        old_in_new=all(B.contains(g) for g in A.generators)
        new_in_old=all(A.contains(g) for g in B.generators)
        assert old_in_new and new_in_old
        ao,bo=int(A.order()),int(B.order());assert ao==bo
        records.append({'array':key,'literally_equal':False,'old_in_new':True,
                        'new_in_old':True,'common_subgroup_order':ao,
                        'old_generator_count':len(a),'new_generator_count':len(b)})
    return {'file':name,'all_arrays_mathematically_equal':True,'arrays':records}
def main():
    start=time.time();first=json.loads((HERE/'audit_a6_kernel_root.json').read_text())
    assert not first['all_passed'] and first['original_artifacts_unchanged']
    protected=first['protected_sha256']
    assert all(digest(HERE/n)==h for n,h in protected.items())
    records=[]
    for i,(stem,args,outstems) in enumerate(STEPS):
        row={'program':stem+'.py','arguments':args,'already_run':i<len(first['steps'])}
        if i>=len(first['steps']):
            logpath=REPLAY/(stem+('_outer' if args else '')+'_root_check.out')
            with logpath.open('x') as log:
                proc=subprocess.run([sys.executable,str(REPLAY/(stem+'.py')),*args],
                    cwd=REPLAY,stdout=log,stderr=subprocess.STDOUT)
            assert proc.returncode==0
        else:assert first['steps'][i]['exit_code']==0
        row['JSON_comparisons']=[];row['NPZ_comparisons']=[]
        for outstem in outstems:
            a=json.loads((HERE/(outstem+'.json')).read_text())
            b=json.loads((REPLAY/(outstem+'.json')).read_text())
            assert stripped(a)==stripped(b),outstem
            row['JSON_comparisons'].append({'file':outstem+'.json','mathematical_records_equal':True})
            for p in sorted(REPLAY.glob(outstem+'*.npz')):row['NPZ_comparisons'].append(compare_npz(p.name))
        records.append(row)
        print(json.dumps({'program':stem+'.py','arguments':args,'all_mathematical_records_equal':True,
                          'array_comparisons':[{'file':r['file'],'nonliteral_groups':[a for a in r['arrays']
                                               if not a['literally_equal']]} for r in row['NPZ_comparisons']]}),flush=True)
    unchanged=all(digest(HERE/n)==h for n,h in protected.items());assert unchanged
    result={'all_passed':True,'original_artifacts_unchanged':True,
            'initial_failed_guard_retained':True,'steps':records,
            'exact_resolution':'Different derived generating sets give the identical subgroup by both literal inclusions.',
            'protected_sha256':protected,'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ROOT_A6_KERNEL_AND_OUTER_COMPLETE_RESOLUTION_PASS',flush=True)

if __name__=='__main__':main()
