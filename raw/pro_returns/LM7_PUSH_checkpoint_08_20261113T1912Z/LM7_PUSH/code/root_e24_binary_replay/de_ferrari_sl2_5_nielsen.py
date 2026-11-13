#!/usr/bin/env python3
"""Complete Nielsen image in the universal SL2(F5) Ferrari model."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_lifted_schreier_kernel import lifted_kernel

def main():
    start=time.time();here=Path(__file__).resolve().parent;H=FerrariSL2Five()
    points=[(1,0),(0,1),(1,1)]
    def permutation(g):
        a=H.old.permutation(H.project_a5(g),True).array_form
        Mi=H.inv(g)[76:80].reshape(2,2)
        q=[points.index(tuple(Mi@np.array(v)%2)) for v in points]
        return Permutation(a+[95+j for j in q])
    ps=[permutation(H.a),permutation(H.b)]
    for a in (H.a,H.b,H.inv(H.a),H.inv(H.b)):
        for b in (H.a,H.b):assert permutation(H.mul(a,b))==permutation(a)*permutation(b)
    def vector(g):
        v=H.relative_kernel_vector(g);assert not np.any(v[:19]);return v[19:]
    def element(v):return H.relative_kernel_element(np.r_[np.zeros(19,dtype=np.int64),v])
    old=json.loads((here/'de_ferrari_a5_model.json').read_text())
    G,S,info=lifted_kernel(H,[H.a,H.b],ps,vector,element,38,3*old['Nielsen_image_order'])
    rank=len(S.basis);Torder=4*120**19*info['lifted_group_order']
    out={**info,'free_universal_kernel_order':4*120**19,
         'Nielsen_cross_term_kernel_dimension':rank,
         'four_strand_kernel_over_A5_and_S4_dimension':19+rank,
         'four_strand_target_order':Torder,
         'actual_four_strand_base_order':12*old['four_strand_image_order'],
         'actual_four_strand_kernel_is_elementary_abelian':True,
         'total_seconds':round(time.time()-start,3)}
    assert Torder==out['actual_four_strand_base_order']*2**(19+rank)
    here.joinpath('de_ferrari_sl2_5_nielsen.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_sl2_5_nielsen.npz',Nielsen_kernel_basis=S.matrix(),
                        base_strong_generators=np.array([p.array_form for p in G.strong_gens]))
    print(json.dumps({k:v for k,v in out.items() if k not in ('literal_word_DAG','kernel_basis_word_nodes')},indent=2),flush=True)

if __name__=='__main__':main()
