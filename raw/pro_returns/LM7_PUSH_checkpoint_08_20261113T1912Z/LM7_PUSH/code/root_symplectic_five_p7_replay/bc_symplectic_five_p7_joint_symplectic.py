#!/usr/bin/env python3
"""Exact simultaneous prime-five/prime-seven braid target maps.

The same literal generators are paired before computing the image.
Both the four-strand restrictions and the full five-strand targets
are retained; no product conclusion is inferred from separate orders.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).resolve().parent
def main():
    started=time.time()
    names=['e_symplectic_five_p5_model_root.npz','bc_symplectic_five_p7_model.npz',
           'e_symplectic_five_p5_model_root.json','bc_symplectic_five_p7_model.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    a=np.load(HERE/names[0])['sigma'];b=np.load(HERE/names[1])['sigma']
    am=json.loads((HERE/names[2]).read_text());bm=json.loads((HERE/names[3]).read_text())
    joint=np.stack([np.r_[x,len(x)+y] for x,y in zip(a,b)])
    records=[]
    for n in (3,4):
        G=PermutationGroup([Permutation(x.tolist()) for x in joint[:n]])
        order=int(G.order())
        label='first_four_strand_image_order' if n==3 else 'full_image_order'
        product_order=int(am[label])*int(bm[label])
        assert order==product_order
        records.append({'braid_strands':n+1,'prime5_order':int(am[label]),
                        'prime7_order':int(bm[label]),'actual_joint_order':order,
                        'actual_joint_is_full_product':True})
        print(records[-1],flush=True)
    out={'status':'PASS_ACTUAL_P5_P7_JOINT_BRAID_TARGETS','records':records,
         'all_four_literal_generator_pairs_retained':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p7_joint_symplectic'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(target.with_suffix('.npz'),sigma=joint)
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k!='input_sha256'},indent=2),flush=True)

if __name__=='__main__':main()
