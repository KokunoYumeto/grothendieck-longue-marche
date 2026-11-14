#!/usr/bin/env python3
"""Resolve the provenance-only replay difference and complete E44 audit.

The initial guard is retained. Two input JSON files have distinct hashes
because the earlier isolated replays contain their own elapsed times.
Each declared hash is verified against its actual local file; every
mathematical input and output is compared before provenance is separated.
"""
from pathlib import Path
import json,subprocess,sys,time
import numpy as np
from audit_twoadic_integral_root import digest,mathematical

HERE=Path(__file__).resolve().parent
REPLAY=HERE/'root_e24_binary_replay'
STEMS=('bc_fermat_class_three_burnside','bc_fermat_class_three_norms',
       'bc_fermat_class_three_tower_comparison')

def compare_file(a,b):
    if a.suffix=='.json':
        assert mathematical(json.loads(a.read_text()))==mathematical(json.loads(b.read_text())),a.name
    elif a.suffix=='.npz':
        with np.load(a) as x,np.load(b) as y:
            assert set(x.files)==set(y.files)
            assert all(np.array_equal(x[k],y[k]) for k in x.files),a.name
    else:assert a.read_bytes()==b.read_bytes(),a.name

def compare_output(stem):
    a=json.loads((HERE/(stem+'.json')).read_text())
    b=json.loads((REPLAY/(stem+'.json')).read_text())
    pa,pb=a.get('protected_input_hashes',{}),b.get('protected_input_hashes',{})
    assert pa.keys()==pb.keys()
    differences=[]
    for name in pa:
        assert digest(HERE/name)==pa[name]
        assert digest(REPLAY/name)==pb[name]
        compare_file(HERE/name,REPLAY/name)
        if pa[name]!=pb[name]:differences.append(name)
    aa,bb=mathematical(a),mathematical(b)
    aa.pop('protected_input_hashes',None);bb.pop('protected_input_hashes',None)
    assert aa==bb
    compare_file(HERE/(stem+'.npz'),REPLAY/(stem+'.npz'))
    return {'program':stem+'.py','all_mathematical_records_equal':True,
            'all_NPZ_arrays_equal':True,'all_declared_provenance_hashes_verified':True,
            'input_JSON_hashes_differing_only_in_elapsed_time':differences}

def main():
    at=time.time();initial=json.loads((HERE/'audit_class_three_boundary_root.json').read_text())
    assert not initial['all_passed'] and initial['original_artifacts_unchanged']
    assert len(initial['programs'])==2 and all(r['exit_code']==0 for r in initial['programs'])
    before=initial['protected_sha256']
    assert all(digest(HERE/n)==h for n,h in before.items())
    rows=[compare_output(s) for s in STEMS[:2]]
    stem=STEMS[2];out=REPLAY/(stem+'_root_check.out')
    with out.open('x') as stream:
        run=subprocess.run([sys.executable,'-u',str(REPLAY/(stem+'.py'))],
                            cwd=REPLAY,stdout=stream,stderr=subprocess.STDOUT)
    assert run.returncode==0
    rows.append(compare_output(stem))
    assert all(digest(HERE/n)==h for n,h in before.items())
    result={'all_passed':True,'original_artifacts_unchanged':True,
            'initial_failed_guard_retained':True,'programs':rows,
            'exact_resolution':'Independently rerun input JSON elapsed times; no mathematical difference.',
            'protected_sha256':before,'seconds':round(time.time()-at,3)}
    (HERE/'audit_class_three_resolution_root.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='protected_sha256'},indent=2))
    print('ROOT_CLASS_THREE_BOUNDARY_COMPLETE_AUDIT_PASS')

if __name__=='__main__':main()
