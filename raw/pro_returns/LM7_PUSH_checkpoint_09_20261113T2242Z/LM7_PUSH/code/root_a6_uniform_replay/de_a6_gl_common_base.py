#!/usr/bin/env python3
"""The literal common A6/A5 quotient on shared transitive B-sets.

The maps are restrictions through explicit canonical point bijections.
The complete joint-source order supplies an independent maximality check.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent


def last(name):return json.loads((HERE/name).read_text().splitlines()[-1])


def main():
    started=time.time()
    names=['de_a6_schreier_full_ordered.npz','de_ferrari_a5_source_compressed.npz',
           'de_a6_a5_common_source.json','de_a6_a5_common_source_order.out',
           'de_a6_schreier_full_ordered.out','de_ferrari_a5_source.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    A=np.load(HERE/names[0]);B=np.load(HERE/names[1]);na=len(A['s'])
    metadata=json.loads((HERE/names[2]).read_text())
    corrs=metadata['orbit_correspondences']
    left={r['retained_orbit_index']:r['original_canonical_order'] for r in corrs
          if min(r['original_canonical_order'])<na}
    right={r['retained_orbit_index']:[i-na for i in r['original_canonical_order']] for r in corrs
           if min(r['original_canonical_order'])>=na}
    common=sorted(left.keys()&right.keys())
    lp=np.array([x for i in common for x in left[i]],dtype=np.int64)
    rp=np.array([x for i in common for x in right[i]],dtype=np.int64)
    assert len(lp)==len(rp)==432
    def restrict(data,points):
        inv=np.full(len(data['s']),-1,dtype=np.int64);inv[points]=np.arange(len(points))
        value=np.array([inv[data[a][points]] for a in ('s','r')])
        assert np.all(value>=0)
        for a,p in zip(('s','r'),value):assert np.array_equal(points[p],data[a][points])
        return value
    ps=restrict(A,lp);assert np.array_equal(ps,restrict(B,rp))
    G=PermutationGroup([Permutation(p.tolist()) for p in ps]);order=int(G.order())
    g6=int(last(names[4])['order'])
    ga=int(json.loads((HERE/names[5]).read_text())['induced_B_image_order'])
    joint=int(last(names[3])['order']);assert g6*ga%joint==0
    maximum=g6*ga//joint
    assert maximum%order==0
    d=load_data();letters={0:ps[0],1:ps[1],-1:ps[1][ps[1]]}
    def word(w):
        out=np.arange(len(lp))
        for a in w:out=letters[a][out]
        return Permutation(out.tolist())
    F=PermutationGroup([word(d['xword']),word(d['yword'])])
    N=PermutationGroup([word(w) for w in d['Nwords']])
    E=F.derived_subgroup();C=N.derived_subgroup()
    cp=C.derived_subgroup()
    values={'G':order,'F':int(F.order()),'N':int(N.order()),
            'F_prime':int(E.order()),'N_prime':int(C.order()),
            'N_primeprime':int(cp.order())}
    out={'status':'PASS_EXACT_COMMON_B_SET_MAP','shared_B_set_indices':common,
         'shared_B_set_sizes':[len(left[i]) for i in common],
         'faithful_common_degree':len(lp),'actual_common_quotient_order':order,
         'maximum_common_order_from_complete_joint_source':maximum,
         'entire_maximum_common_quotient':order==maximum,
         'actual_subgroup_orders':values,
         'N_prime_is_perfect':values['N_prime']==values['N_primeprime'],
         'source_maps':'actual point restrictions on both sources, with all s/r intertwiners checked',
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_gl_common_base.npz',s=ps[0],r=ps[1],
                        A6_retained_points=lp,A5_retained_points=rp,
                        N_derived_generators=np.array([p.array_form for p in C.generators]))
    (HERE/'de_a6_gl_common_base.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
