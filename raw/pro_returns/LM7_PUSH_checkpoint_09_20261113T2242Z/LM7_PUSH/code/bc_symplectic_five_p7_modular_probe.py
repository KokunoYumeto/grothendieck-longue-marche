#!/usr/bin/env python3
"""Literal level-seven projective map compared with the old A5 source.

This is an independent finite map computation.  It does not assume a
uniform description of the new symplectic induced source.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).resolve().parent
def main():
    started=time.time()
    names=['de_ferrari_a5_source_compressed.npz','de_ferrari_a5_source_compressed.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    points=[(1,i) for i in range(7)]+[(0,1)];ix={v:i for i,v in enumerate(points)}
    def normal(v):
        a,b=map(int,v%7)
        return (1,b*pow(a,-1,7)%7) if a else (0,1)
    def perm(A):return np.array([ix[normal(np.array(v)@A%7)] for v in points],dtype=np.int64)
    s=np.array([[0,1],[-1,0]],dtype=np.int64)%7
    r=np.array([[0,-1],[1,-1]],dtype=np.int64)%7
    allsl=[np.array(a,dtype=np.int64).reshape(2,2) for a in product(range(7),repeat=4)
           if (a[0]*a[3]-a[1]*a[2])%7==1]
    psl={tuple(perm(a)) for a in allsl};assert len(allsl)==336 and len(psl)==168
    ps,pr=perm(s),perm(r);one=np.arange(8)
    assert np.array_equal(ps[ps],one) and np.array_equal(pr[pr[pr]],one)
    G=PermutationGroup([Permutation(ps.tolist()),Permutation(pr.tolist())]);assert int(G.order())==168
    old=np.load(HERE/names[0]);oldorder=int(json.loads((HERE/names[1]).read_text())['source_image_order'])
    degree=len(old['s']);joint=PermutationGroup([Permutation(np.r_[old['s'],degree+ps].tolist()),
                                               Permutation(np.r_[old['r'],degree+pr].tolist())])
    print('Computing the actual G_A/projective-level7 joint source',flush=True)
    order=int(joint.order());assert order%oldorder==0 and 168%(order//oldorder)==0
    out={'status':'PASS_ACTUAL_PROJECTIVE_LEVEL7_SOURCE_COMPARISON','prime':7,
         'SL2_order':336,'projective_order':168,'projective_line_points':points,
         'literal_s_matrix':s.tolist(),'literal_r_matrix':r.tolist(),
         'old_A5_source_order':oldorder,'actual_joint_order':order,
         'joint_index':order//oldorder,'level7_factors_through_G_A':order==oldorder,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p7_modular_probe'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(target.with_suffix('.npz'),s=ps,r=pr,all_projective_actions=np.array(sorted(psl),dtype=np.int64))
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k!='input_sha256'},indent=2),flush=True)
if __name__=='__main__':main()
