#!/usr/bin/env python3
"""Actual lower-A6/A5 common source, for comparison with the full source.

Both maps are retained through exact B-set intertwiners.  No claim about
the signed GL extension is made by this base calculation.
"""
from pathlib import Path
from hashlib import sha256
import json,struct,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_kernel_source import compress

HERE=Path(__file__).resolve().parent


def main():
    start=time.time()
    names=['de_ferrari_a6_perm_source_compressed.npz',
           'de_ferrari_a5_source_compressed.npz',
           'de_ferrari_a6_perm_source.json','de_ferrari_a5_source.json',
           'de_a6_gl_model.bin']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    A=np.load(HERE/names[0]);B=np.load(HERE/names[1]);na=len(A['s'])
    ps,metadata=compress(np.r_[A['s'],na+B['s']],np.r_[A['r'],na+B['r']])
    sizes=metadata['retained_orbit_sizes'];starts=np.r_[0,np.cumsum(sizes)]
    order=sorted(range(len(sizes)),key=lambda i:sizes[i],reverse=True)
    points=np.concatenate([np.arange(starts[i],starts[i+1]) for i in order])
    inverse=np.argsort(points);ps=inverse[ps[:,points]]
    print('exact joint lower degree',len(points),flush=True)
    G=PermutationGroup([Permutation(p.tolist()) for p in ps]);joint=int(G.order())
    a=json.loads((HERE/names[2]).read_text());b=json.loads((HERE/names[3]).read_text())
    print('orders metadata',list(a),flush=True)
    oa=int(a['induced_B_image_order']);ob=int(b['induced_B_image_order'])
    assert oa*ob%joint==0
    np.savez_compressed(HERE/'de_a6_gl_lower.npz',s=ps[0],r=ps[1],
                        point_order=points,point_order_inverse=inverse)
    with (HERE/'de_a6_gl_lower.input').open('w') as f:
        f.write(f'{len(points)} 2\n')
        for p in ps:f.write(' '.join(map(str,p))+'\n')
    raw=(HERE/'de_a6_gl_model.bin').read_bytes()
    # The final field is exactly the exported original two base permutations.
    tail=8+2*11010*2
    assert struct.unpack_from('<II',raw,len(raw)-tail)==(11010,2)
    small=raw[:-tail]+struct.pack('<II',len(points),2)+ps.astype('<u2').tobytes()
    (HERE/'de_a6_gl_lower_model.bin').write_bytes(small)
    result={**metadata,'status':'PASS_EXACT_LOWER_BASE_SOURCE',
            'lower_A6_source_order':oa,'A5_source_order':ob,'joint_source_order':joint,
            'maximum_common_order':oa*ob//joint,
            'input_sha256':hashes,'model_export_sha256':sha256(small).hexdigest(),
            'seconds':round(time.time()-start,3)}
    (HERE/'de_a6_gl_lower.json').write_text(json.dumps(result,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in result.items() if k not in
                     ('retained_original_canonical_orders','orbit_correspondences','input_sha256')},indent=2),flush=True)


if __name__=='__main__':main()
