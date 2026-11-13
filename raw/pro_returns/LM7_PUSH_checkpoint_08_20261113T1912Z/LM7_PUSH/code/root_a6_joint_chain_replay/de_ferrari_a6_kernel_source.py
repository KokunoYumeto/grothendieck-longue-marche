#!/usr/bin/env python3
"""Full induced sources of the A6 kernel and exceptional-outer targets.

All six F-evaluations and six B/F cosets are retained.  Compression discards
only duplicate transitive B-sets, with an explicit intertwiner for both
original generators on every discarded orbit; hence it has exactly the
same kernel as the uncompressed source homomorphism.
"""
from pathlib import Path
from collections import Counter
import argparse,json,time
import numpy as np
from sympy.combinatorics import PermutationGroup,Permutation
from sympy import factorint
from de_ferrari_a6_kernels import FerrariA6Kernel
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined

HERE=Path(__file__).resolve().parent

def induced_permutation(H,e):
    hd=H.n*(4 if H.outer else 1);out=[]
    for q in range(6):
        for i in range(6):
            p=H.permutation(e[1][q,i]).array_form
            out.extend((hd*(6*int(e[0][q])+i)+np.array(p)).tolist())
    return Permutation(out)

def compress(s,r):
    """Produce a faithful source with explicit B-set intertwiners."""
    s=np.asarray(s,dtype=np.int64);r=np.asarray(r,dtype=np.int64)
    unseen=set(range(len(s)));orbits=[]
    while unseen:
        root=min(unseen);queue=[root];unseen.remove(root)
        for v in queue:
            for p in (s,r):
                w=int(p[v])
                if w in unseen:unseen.remove(w);queue.append(w)
        orbits.append(sorted(queue))
    unique={};representatives=[];records=[]
    for no,pts in enumerate(orbits):
        best=None;best_order=None
        for base in pts:
            order=[base];index={base:0}
            for v in order:
                for p in (s,r):
                    w=int(p[v])
                    if w not in index:index[w]=len(order);order.append(w)
            assert len(order)==len(pts)
            actions=tuple(tuple(index[int(p[v])] for v in order) for p in (s,r))
            if best is None or actions<best:best=actions;best_order=order
        if best not in unique:
            unique[best]=len(representatives)
            representatives.append({'order':best_order,'actions':best})
        j=unique[best];rep=representatives[j]
        correspondence={v:rep['order'][k] for k,v in enumerate(best_order)}
        assert len(set(correspondence.values()))==len(pts)
        assert all(correspondence[int(p[v])]==int(p[correspondence[v]])
                   for p in (s,r) for v in pts)
        records.append({'original_orbit_index':no,'retained_orbit_index':j,
                        'original_canonical_order':best_order})
    new=[[],[]];offset=0
    for rep in representatives:
        for i in range(2):new[i].extend(offset+j for j in rep['actions'][i])
        offset+=len(rep['order'])
    out={'original_degree':len(s),'faithful_compressed_degree':offset,
         'original_orbit_count':len(orbits),'original_orbit_size_counts':dict(Counter(map(len,orbits))),
         'distinct_transitive_B_sets':len(representatives),
         'retained_orbit_sizes':[len(x['order']) for x in representatives],
         'all_discarded_orbits_explicitly_intertwined':True,
         'retained_original_canonical_orders':[rep['order'] for rep in representatives],
         'orbit_correspondences':records}
    return np.array(new,dtype=np.int64),out

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--outer',action='store_true')
    args=parser.parse_args();start=time.time();d=load_data();H=FerrariA6Kernel(args.outer)
    W=InducedCombined(H,d)
    s,r=induced_permutation(H,W.letters[0]),induced_permutation(H,W.letters[1])
    one=Permutation(list(range(s.size)))
    assert s**2==one and r**3==one
    for a in (W.letters[0],W.letters[1],W.letters[-1]):
        for b in (W.letters[0],W.letters[1],W.letters[-1]):
            assert induced_permutation(H,W.mul(a,b))==induced_permutation(H,a)*induced_permutation(H,b)
    prefix='de_ferrari_a6_'+('outer' if args.outer else 'perm')+'_source'
    np.savez_compressed(HERE/(prefix+'_generators.npz'),s=np.array(s.array_form),r=np.array(r.array_form))
    new,metadata=compress(s.array_form,r.array_form)
    print(json.dumps({k:v for k,v in metadata.items() if k not in
       ('retained_original_canonical_orders','orbit_correspondences')},indent=2),flush=True)
    group=PermutationGroup([Permutation(p.tolist()) for p in new]);order=int(group.order())
    np.savez_compressed(HERE/(prefix+'_compressed.npz'),s=new[0],r=new[1],
                       strong_generators=np.array([p.array_form for p in group.strong_gens]),
                       base=np.array(group.base))
    out={**metadata,'source_image_order':order,'source_image_order_factorization':factorint(order),
         'all_six_cosets_and_evaluation_maps_retained':True,
         'multiplication_and_C2_C3_relations_verified':True,
         'seconds':round(time.time()-start,3)}
    (HERE/(prefix+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in
       ('retained_original_canonical_orders','orbit_correspondences')},indent=2),flush=True)

if __name__=='__main__':main()
