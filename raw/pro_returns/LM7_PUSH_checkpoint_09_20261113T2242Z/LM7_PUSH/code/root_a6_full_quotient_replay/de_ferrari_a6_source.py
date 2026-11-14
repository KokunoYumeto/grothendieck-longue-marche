#!/usr/bin/env python3
"""The complete induced source for the full A6 Ferrari quotient.

The faithful 1,060-point target action is induced through all six B/F
cosets for each of the six evaluation maps.  Explicit intertwiners of
transitive B-sets give a faithful compression of the 38,160-point source.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy import factorint
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_model import FerrariA6
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_kernel_source import compress
from de_ferrari_degree4_lift import InducedCombined

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();d=load_data();H=FerrariA6();W=InducedCombined(H,d)
    hd=20*H.n
    def permutation(e):
        out=[]
        for q in range(6):
            for i in range(6):
                out.extend((hd*(6*int(e[0][q])+i)+np.array(H.permutation(e[1][q,i]).array_form)).tolist())
        return Permutation(out)
    s,r=permutation(W.letters[0]),permutation(W.letters[1])
    one=Permutation(list(range(s.size)));assert s**2==one and r**3==one
    for a in (W.letters[0],W.letters[1],W.letters[-1]):
        for b in (W.letters[0],W.letters[1],W.letters[-1]):
            assert permutation(W.mul(a,b))==permutation(a)*permutation(b)
    np.savez_compressed(HERE/'de_ferrari_a6_source_generators.npz',s=np.array(s.array_form),r=np.array(r.array_form))
    new,metadata=compress(s.array_form,r.array_form)
    np.savez_compressed(HERE/'de_ferrari_a6_source_compressed_generators.npz',s=new[0],r=new[1])
    (HERE/'de_ferrari_a6_source_compression.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps({k:v for k,v in metadata.items() if k not in
        ('retained_original_canonical_orders','orbit_correspondences')},indent=2),flush=True)
    group=PermutationGroup([Permutation(p.tolist()) for p in new]);order=int(group.order())
    np.savez_compressed(HERE/'de_ferrari_a6_source_compressed.npz',s=new[0],r=new[1],
        strong_generators=np.array([p.array_form for p in group.strong_gens]),base=np.array(group.base))
    out={**metadata,'source_image_order':order,'source_image_order_factorization':factorint(order),
         'all_six_cosets_and_evaluation_maps_retained':True,
         'multiplication_and_C2_C3_relations_verified':True,'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_source.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in
        ('retained_original_canonical_orders','orbit_correspondences')},indent=2),flush=True)

if __name__=='__main__':main()
