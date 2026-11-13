#!/usr/bin/env python3
"""Actual joint A5-Ferrari/five-point-Hurwitz source and quotient map.

First retain both literal B actions and their disjoint union.  Every
compression intertwiner is verified pointwise.  A repeated B-set gives
a direct restriction certificate; otherwise an exact joint group order
determines the maximal common quotient with these specific source maps.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from sympy import factorint
from de_ferrari_a6_kernel_source import compress

HERE=Path(__file__).resolve().parent
def main():
    start=time.time()
    names=['de_ferrari_a5_source_compressed.npz','de_ferrari_a5_source_compressed.json',
           'e_hurwitz_five_source_root_compressed.npz','e_hurwitz_five_source_root.json']
    protected={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    A=np.load(HERE/names[0]);B=np.load(HERE/names[2]);na,nb=len(A['s']),len(B['s'])
    s=np.concatenate([A['s'],na+B['s']]);r=np.concatenate([A['r'],na+B['r']])
    for p in (s,r):assert np.array_equal(np.sort(p),np.arange(na+nb))
    assert np.array_equal(s[s],np.arange(na+nb)) and np.array_equal(r[r[r]],np.arange(na+nb))
    new,meta=compress(s,r)
    retained=meta['retained_original_canonical_orders']
    old_classes={rec['retained_orbit_index'] for rec in meta['orbit_correspondences']
                 if min(rec['original_canonical_order'])<na}
    new_classes={rec['retained_orbit_index'] for rec in meta['orbit_correspondences']
                 if min(rec['original_canonical_order'])>=na}
    all_new_orbits_repeated=new_classes<=old_classes
    oa=json.loads((HERE/names[1]).read_text())['source_image_order']
    ob=json.loads((HERE/names[3]).read_text())['source_image_order']
    print(json.dumps({'original_degrees':[na,nb],
                     'faithful_joint_degree':meta['faithful_compressed_degree'],
                     'old_B_set_classes':len(old_classes),'new_B_set_classes':len(new_classes),
                     'new_classes_not_in_old':sorted(new_classes-old_classes),
                     'all_new_B_sets_repeated_in_old':all_new_orbits_repeated}),flush=True)
    if all_new_orbits_repeated:
        # Every target orbit is a specified B-set copy of an old one.
        # Hence every old kernel word acts trivially on the target.
        joint_order=oa;strong=[];base=[]
    else:
        G=PermutationGroup([Permutation(p.tolist()) for p in new]);joint_order=int(G.order())
        strong=[p.array_form for p in G.strong_gens];base=G.base
    assert joint_order%oa==joint_order%ob==0
    common_order=oa*ob//joint_order
    projection=joint_order==oa
    out={**meta,'old_source_order':oa,'Hurwitz_source_order':ob,
         'actual_joint_source_order':joint_order,'actual_common_quotient_order':common_order,
         'actual_common_quotient_factorization':factorint(common_order),
         'all_Hurwitz_B_sets_are_repeated_old_B_sets':all_new_orbits_repeated,
         'actual_A5_source_maps_onto_Hurwitz_source':projection,
         'quotient_map':'rho_A(b) -> rho_5(b) for every literal B word b' if projection else None,
         'input_sha256':protected,'seconds':round(time.time()-start,3)}
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in protected.items())
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(Path(__file__).with_suffix('.npz'),s=new[0],r=new[1],
                        strong_generators=np.array(strong,dtype=np.int64),base=np.array(base,dtype=np.int64))
    print(json.dumps({k:v for k,v in out.items() if k not in
        ('retained_original_canonical_orders','orbit_correspondences','input_sha256')},indent=2),flush=True)
    print('PASS: actual joint-source comparison with all quotient maps retained.',flush=True)

if __name__=='__main__':main()
