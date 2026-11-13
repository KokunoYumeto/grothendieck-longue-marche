#!/usr/bin/env python3
"""Faithful compression by exact isomorphisms of transitive B-sets.

Every discarded orbit is explicitly intertwined with a retained orbit
for both original generators.  This is an actual isomorphism of the
joint source image, with no quotient selected for convenience.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import PermutationGroup,Permutation

def main():
    start=time.time();here=Path(__file__).resolve().parent
    data=np.load(here/'de_ferrari_a5_source_generators.npz');s,r=data['s'],data['r']
    G=PermutationGroup([Permutation(s.tolist()),Permutation(r.tolist())]);orbits=G.orbits()
    unique={};representatives=[];records=[]
    for no,orbit in enumerate(orbits):
        pts=sorted(orbit);best=None;best_order=None;best_actions=None
        for base in pts:
            order=[base];index={base:0}
            for v in order:
                for p in (s,r):
                    w=int(p[v])
                    if w not in index:index[w]=len(order);order.append(w)
            assert len(order)==len(pts)
            actions=tuple(tuple(index[int(p[v])] for v in order) for p in (s,r))
            if best is None or actions<best:best=actions;best_order=order;best_actions=actions
        if best not in unique:
            unique[best]=len(representatives);representatives.append({'order':best_order,'actions':best_actions})
        j=unique[best];rep=representatives[j]
        correspondence={v:rep['order'][k] for k,v in enumerate(best_order)}
        assert all(correspondence[int(p[v])]==int(p[correspondence[v]]) for p in (s,r) for v in pts)
        records.append({'original_orbit_index':no,'retained_orbit_index':j,'original_canonical_order':best_order})
    new=[[],[]];offset=0
    for rep in representatives:
        for i in range(2):new[i].extend([offset+j for j in rep['actions'][i]])
        offset+=len(rep['order'])
    group=PermutationGroup([Permutation(p) for p in new]);order=int(group.order())
    expected=json.loads((here/'de_ferrari_a5_source.json').read_text())['induced_B_image_order'];assert order==expected
    np.savez_compressed(here/'de_ferrari_a5_source_compressed.npz',s=np.array(new[0]),r=np.array(new[1]),
                        strong_generators=np.array([p.array_form for p in group.strong_gens]),base=np.array(group.base))
    out={'original_degree':len(s),'faithful_compressed_degree':offset,'original_orbits':len(orbits),
         'distinct_transitive_B_sets':len(representatives),'retained_orbit_sizes':[len(x['order']) for x in representatives],
         'source_image_order':order,'all_discarded_orbits_explicitly_intertwined':True,
         'retained_original_canonical_orders':[rep['order'] for rep in representatives],
         'orbit_correspondences':records,'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_a5_source_compressed.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('orbit_correspondences','retained_original_canonical_orders')},indent=2),flush=True)

if __name__=='__main__':main()
