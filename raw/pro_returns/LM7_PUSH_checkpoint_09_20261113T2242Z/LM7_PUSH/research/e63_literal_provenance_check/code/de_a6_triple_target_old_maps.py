#!/usr/bin/env python3
"""Literal old T23 arrows to the new target's specified solvable maps."""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_mod9_lift import Jacobi
from de_a6_triple_model import FerrariA6Triple

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    names=['de_ferrari_degree6_kernel.py','de_ferrari_degree4_lift.py',
           'de_ferrari_two_model.py','de_a6_triple_target_quotient.json',
           'de_a6_triple_target_quotient.npz']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    F=FerrariTwo(6);B=FerrariTwo(2);J=Jacobi(9);H=FerrariA6Triple()
    old=np.load(HERE/names[-1]);binary={tuple(a):int(q) for a,q in
          zip(old['binary_class_two_elements'],old['binary_to_signed_values'])}
    fg=[F.a,F.b,F.c];bg=[B.a,B.b,B.c];jg=[J.a,J.b,J.c];hg=[H.a,H.b,H.c]
    for f,b,j,h in zip(fg,bg,jg,hg):
        assert np.array_equal(F.to_lower(f,B),b)
        assert tuple(b) in binary
        assert np.array_equal(j[:6]%3,H.project_affine3(h))
    ff=fg+[F.inv(g) for g in fg];bb=bg+[B.inv(g) for g in bg]
    jj=jg+[J.inv(g) for g in jg];hh=hg+[H.inv(g) for g in hg]
    for f,b,j,h in zip(ff,bb,jj,hh):
        for g,c,k,l in zip(ff,bb,jj,hh):
            assert np.array_equal(F.to_lower(F.mul(f,g),B),B.mul(b,c))
            assert np.array_equal(J.mul(j,k)[:6]%3,H.project_affine3(H.mul(h,l)))
    for f,b,j,h in zip(F.x,B.x,J.x,H.x):
        assert np.array_equal(F.to_lower(f,B),b)
        assert np.array_equal(j[:6]%3,H.project_affine3(h))
    for f,b,j,h in zip(F.y,B.y,J.y,H.y):
        assert np.array_equal(F.to_lower(f,B),b)
        assert np.array_equal(j[:6]%3,H.project_affine3(h))
    q=json.loads((HERE/names[-2]).read_text())
    assert q['actual_joint_order']==20736
    out={'status':'PASS_LITERAL_T23_TO_SIGNED_TIMES_AFFINE3',
         'binary_arrow':'degree-six Magnus quotient to degree-two truncation, then the saved1536-element map to S_L',
         'ternary_arrow':'retained Jacobi(Z/9) coordinate to its affine first-six coordinates modulo3',
         'all3_braid_generator_arrows_verified':True,
         'all36_signed_generator_products_verified':True,
         'all6_pure_substitution_pairs_verified_under_both_arrows':True,
         'joint_quotient_order':20736,
         'joint_surjectivity_uses_complete_actual_three_generator_Cayley_closure':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_target_old_maps.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
