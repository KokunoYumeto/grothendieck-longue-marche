#!/usr/bin/env python3
"""Exact joint four-strand target with the new prime-seven representation.

All three original braid generators are paired with the Ferrari SL2
model.  The full central binary kernel is recovered by the complete
Schreier presentation above the actual combined permutation quotient.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_lifted_schreier_kernel import lifted_kernel

HERE=Path(__file__).resolve().parent
class Joint:
    def __init__(self,H):self.H=H;self.one=(H.one,np.arange(2400,dtype=np.int64))
    def mul(self,a,b):return self.H.mul(a[0],b[0]),b[1][a[1]]
    def inv(self,a):return self.H.inv(a[0]),np.argsort(a[1])
    def conj(self,a,b):return self.mul(self.mul(a,b),self.inv(a))
def main():
    started=time.time()
    names=['de_ferrari_sl2_5_nielsen.json','bc_symplectic_five_p7_model.npz',
           'de_ferrari_sl2_5_model.py','de_lifted_schreier_kernel.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    H=FerrariSL2Five();joint=Joint(H)
    sym=np.load(HERE/'bc_symplectic_five_p7_model.npz')['sigma']
    gs=list(zip((H.a,H.b,H.c),sym[:3]))
    points=[(0,0),(1,0),(0,1),(1,1)]
    def permutation(e):
        h,p=e;old=H.old.permutation(H.project_a5(h)).array_form
        inv=H.inv(h);M=inv[76:80].reshape(2,2);t=inv[99:]
        affine=[points.index(tuple((M@np.array(v)+t)%2)) for v in points]
        return Permutation(old+[190+i for i in affine]+[194+int(i) for i in p])
    ps=[permutation(g) for g in gs]
    for a in gs:
        for b in gs:assert permutation(joint.mul(a,b))==permutation(a)*permutation(b)
    def vector(e):
        assert np.array_equal(e[1],np.arange(2400,dtype=np.int64))
        return H.relative_kernel_vector(e[0])
    def element(v):return H.relative_kernel_element(v),np.arange(2400,dtype=np.int64)
    G,S,info=lifted_kernel(joint,gs,ps,vector,element,57)
    old=json.loads((HERE/'de_ferrari_sl2_5_nielsen.json').read_text())
    oldorder=int(old['four_strand_target_order']);neworder=115248
    order=int(info['lifted_group_order'])
    assert oldorder*neworder%order==0
    common=oldorder*neworder//order
    out={**info,'status':'PASS_COMPLETE_P7_JOINT_FOUR_STRAND_TARGET',
         'old_Ferrari_target_order':oldorder,'new_four_strand_image_order':neworder,
         'exact_joint_target_order':order,'actual_common_quotient_order':common,
         'all_three_literal_braid_maps_retained':True,
         'input_sha256':hashes,'total_seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p7_target'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(target.with_suffix('.npz'),kernel_basis=S.matrix(),
                        a=np.array(ps[0].array_form),b=np.array(ps[1].array_form),c=np.array(ps[2].array_form))
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in ('input_sha256','literal_word_DAG','kernel_basis_word_nodes')},indent=2),flush=True)
if __name__=='__main__':main()
