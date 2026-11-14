#!/usr/bin/env python3
"""Isolated replay of the actual A5-to-Hurwitz source projection."""
from pathlib import Path
from hashlib import sha256
import json,shutil,subprocess,sys,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).resolve().parent
def digest(p):return sha256(p.read_bytes()).hexdigest()
def main():
    start=time.time();replay=HERE/'root_hurwitz_five_replay'
    stem='e_hurwitz_five_a5_common_root'
    names=[stem+'.py',stem+'.json',stem+'.npz',stem+'.out',
           'de_ferrari_a5_source_compressed.npz','de_ferrari_a5_source_compressed.json',
           'e_hurwitz_five_source_root_compressed.npz','e_hurwitz_five_source_root.json']
    protected={n:digest(HERE/n) for n in names}
    for n in [stem+'.py','de_ferrari_a5_source_compressed.npz','de_ferrari_a5_source_compressed.json']:
        assert not (replay/n).exists();shutil.copy2(HERE/n,replay/n)
    with (replay/(stem+'_root_check.out')).open('x') as log:
        proc=subprocess.run([sys.executable,str(replay/(stem+'.py'))],cwd=replay,
                            stdout=log,stderr=subprocess.STDOUT)
    assert proc.returncode==0
    a=json.loads((HERE/(stem+'.json')).read_text());b=json.loads((replay/(stem+'.json')).read_text())
    for loc,d in [(HERE,a),(replay,b)]:
        for n,h in d['input_sha256'].items():assert digest(loc/n)==h
    mathematical=lambda d:{k:v for k,v in d.items() if k not in ('seconds','input_sha256')}
    assert mathematical(a)==mathematical(b)
    aa,bb=np.load(HERE/(stem+'.npz')),np.load(replay/(stem+'.npz'))
    assert set(aa.files)==set(bb.files)
    for key in ('s','r'):assert np.array_equal(aa[key],bb[key])
    gens_same=np.array_equal(aa['strong_generators'],bb['strong_generators'])
    subgroup=None
    if not gens_same:
        A=PermutationGroup([Permutation(g.tolist()) for g in aa['strong_generators']])
        B=PermutationGroup([Permutation(g.tolist()) for g in bb['strong_generators']])
        assert all(B.contains(g) for g in A.generators) and all(A.contains(g) for g in B.generators)
        subgroup=int(A.order());assert subgroup==int(B.order())==a['actual_joint_source_order']
    else:assert np.array_equal(aa['base'],bb['base'])
    assert a['actual_joint_source_order']==a['old_source_order']
    assert a['actual_A5_source_maps_onto_Hurwitz_source']
    assert all(digest(HERE/n)==h for n,h in protected.items())
    result={'all_passed':True,'all_mathematical_JSON_records_equal':True,
            'literal_source_arrays_equal':True,'strong_generator_arrays_equal':gens_same,
            'nonliteral_strong_generator_common_group_order':subgroup,
            'actual_joint_order_equals_A5_source_order':a['actual_joint_source_order'],
            'actual_A5_to_Hurwitz_projection_surjective':True,
            'original_artifacts_unchanged':True,'all_declared_input_hashes_verified':True,
            'protected_sha256':protected,'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='protected_sha256'},indent=2))
    print('ROOT_ACTUAL_A5_TO_HURWITZ_SOURCE_PROJECTION_PASS')

if __name__=='__main__':main()
