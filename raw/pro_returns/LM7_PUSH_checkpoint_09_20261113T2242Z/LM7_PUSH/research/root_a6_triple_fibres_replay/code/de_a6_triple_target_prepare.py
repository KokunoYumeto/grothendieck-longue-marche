#!/usr/bin/env python3
"""Exact joint target modulo the two perfect free Ferrari factors.

The actual killed subgroup is (3.A6)^53 times SL2(F5)^19.
The additional 1431-point block retains every central-three Nielsen
cross coefficient; the nine-point block retains the global free
abelian character. The old781-point quotient is retained literally.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json,time
import numpy as np
from de_a6_triple_model import FerrariA6Triple
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_sl2_5_solvable import quotient_permutation

HERE=Path(__file__).resolve().parent

def permutation(H,L,g,l):
    old=np.array(H.old.permutation(H.project_a6(g),True).array_form,dtype=np.int64)
    signed=np.array(quotient_permutation(L,l).array_form,dtype=np.int64)
    out=list(old)+list(530+signed)
    p=g[H.ps];alpha=g[H.cs];E=g[H.es].reshape(53,2)
    M=g[H.ms].reshape(2,2);det=int(round(np.linalg.det(M)))%3
    Mi=det*np.array([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]])%3
    points=list(product(range(3),repeat=2));index={v:i for i,v in enumerate(points)}
    for j in range(53):
        for z in range(3):
            for t in points:
                v=Mi@np.array(t)%3
                zz=int(H.character[alpha[j]]*(z-E[j]@v))%3
                out.append(781+27*int(p[j])+9*zz+index[tuple(v)])
    gi=H.inv(g);Mi=gi[H.ms].reshape(2,2);ti=gi[H.ts]
    out.extend(2212+index[tuple((Mi@np.array(v)+ti)%3)] for v in points)
    ans=np.asarray(out,dtype=np.uint16)
    assert np.array_equal(np.sort(ans),np.arange(2221))
    return ans

def main():
    started=time.time()
    names=['de_a6_triple_model.py','de_a6_triple_model.npz',
           'de_a6_gl_target_prepare.npz','de_ferrari_sl2_5_solvable.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    H=FerrariA6Triple();L=FerrariSL2Five()
    hg=[H.a,H.b,H.c];lg=[L.a,L.b,L.c]
    arrays=[permutation(H,L,g,l) for g,l in zip(hg,lg)]
    saved=np.load(HERE/names[2])
    for label,p in zip(['a','b','c'],arrays):assert np.array_equal(p[:781],saved[label])
    gs=hg+[H.inv(g) for g in hg];ls=lg+[L.inv(g) for g in lg]
    for g,l in zip(gs,ls):
        p=permutation(H,L,g,l)
        for h,m in zip(gs,ls):
            q=permutation(H,L,h,m)
            assert np.array_equal(q[p],permutation(H,L,H.mul(g,h),L.mul(l,m)))
    a,b,c=arrays
    assert np.array_equal(a[b[a]],b[a[b]])
    assert np.array_equal(b[c[b]],c[b[c]])
    assert np.array_equal(a[c],c[a])
    with (HERE/'de_a6_triple_target.input').open('w') as f:
        f.write('2221 3\n')
        for p in arrays:f.write(' '.join(map(str,p))+'\n')
    np.savez_compressed(HERE/'de_a6_triple_target_prepare.npz',a=a,b=b,c=c)
    out={'status':'PASS_EXACT_JOINT_TRIPLE_SIGNED_TARGET_QUOTIENT',
         'degree':2221,'retained_old_quotient_degree':781,
         'central_three_cross_block_degree':1431,'affine_three_block_degree':9,
         'all36_literal_generator_product_comparisons':True,
         'all_braid_relations_verified':True,
         'actual_perfect_free_kernel':'(3.A6)^53 times SL2(F5)^19',
         'old_quotient_original_arrays_retained_literally':True,
         'complete_order_and_derived_series_are_separate_certificates':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_target_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
