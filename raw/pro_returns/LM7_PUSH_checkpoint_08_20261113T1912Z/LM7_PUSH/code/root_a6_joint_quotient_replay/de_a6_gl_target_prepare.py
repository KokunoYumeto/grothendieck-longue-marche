#!/usr/bin/env python3
"""Literal joint four-strand quotient after its perfect free Ferrari factor.

The killed free subgroup is A6^53 times SL2(F5)^19.  The retained
quotient combines the actual A6 Nielsen action with the signed
Ferrari quotient on251 points, including all binary cross terms.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_ferrari_a6_model import FerrariA6
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_sl2_5_solvable import quotient_permutation

HERE=Path(__file__).resolve().parent


def main():
    started=time.time();names=['de_ferrari_a6_model.py','de_ferrari_sl2_5_model.py',
        'de_ferrari_sl2_5_solvable.py','de_ferrari_sl2_5_solvable.npz',
        'de_ferrari_sl2_5_solvable.json','de_ferrari_a6_target_derived.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    A=FerrariA6();L=FerrariSL2Five();saved=np.load(HERE/names[3]);arrays={}
    ags=[A.a,A.b,A.c];lgs=[L.a,L.b,L.c]
    for name,a,l in zip(('a','b','c'),ags,lgs):
        pa=np.array(A.permutation(a,True).array_form,dtype=np.int64)
        pl=np.array(quotient_permutation(L,l).array_form,dtype=np.int64)
        assert len(pa)==530 and len(pl)==251 and np.array_equal(pl,saved[name])
        arrays[name]=np.r_[pa,530+pl]
    for i in range(3):
        for j in range(3):
            ap=np.array(A.permutation(A.mul(ags[i],ags[j]),True).array_form)
            lp=np.array(quotient_permutation(L,L.mul(lgs[i],lgs[j])).array_form)
            assert np.array_equal(arrays[('a','b','c')[j]][arrays[('a','b','c')[i]]],np.r_[ap,530+lp])
    a,b,c=[arrays[k] for k in ('a','b','c')]
    assert np.array_equal(a[b[a]],b[a[b]]) and np.array_equal(b[c[b]],c[b[c]])
    assert np.array_equal(a[c],c[a])
    with (HERE/'de_a6_gl_target.input').open('w') as f:
        f.write('781 3\n')
        for k in ('a','b','c'):f.write(' '.join(map(str,arrays[k]))+'\n')
    np.savez_compressed(HERE/'de_a6_gl_target_prepare.npz',**arrays)
    out={'status':'PASS_LITERAL_JOINT_TARGET_QUOTIENT','degree':781,
         'actual_A6_Nielsen_degree':530,'actual_signed_solvable_model_degree':251,
         'quotient_kernel_in_full_joint_target':'the actual perfect free image A6^53 times SL2(F5)^19',
         'all_generator_products_and_braid_relations_verified':True,
         'old_GL_quotient_projection_point_range':[530,781],
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_gl_target_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
