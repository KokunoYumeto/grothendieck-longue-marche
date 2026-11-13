#!/usr/bin/env python3
"""Exact maximal solvable quotient of the A5 Ferrari four-strand target.

The complete derived series is computed in the faithful paired-block
permutation representation.  This supplies the common-quotient comparison
needed for simultaneous generation with the existing solvable targets.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import PermutationGroup
from de_ferrari_a5_model import FerrariA5

def main():
    start=time.time();H=FerrariA5()
    T=PermutationGroup([H.permutation(g) for g in (H.a,H.b,H.c)])
    order=int(T.order());D=T;orders=[order];selected=[]
    for stage in range(1,12):
        # Remove redundant generators before forming the next derived group.
        chosen=[];C=PermutationGroup([H.permutation(H.one)])
        for g in sorted(D.generators,key=lambda g:int(g.order()),reverse=True):
            if not C.contains(g):
                chosen.append(g);C=PermutationGroup(chosen)
                if int(C.order())==orders[-1]:break
        assert int(C.order())==orders[-1] and all(C.contains(g) for g in D.generators)
        selected.append(len(chosen));E=C.derived_subgroup();eo=int(E.order())
        orders.append(eo)
        print('derived stage',stage,'order',eo,'index in T',order//eo,flush=True)
        if eo==orders[-2]:D=E;break
        D=E
    else:raise AssertionError('Derived series not stabilized')
    # The images of a,b,c in the quotient are equal precisely when their
    # pairwise ratios lie in the terminal perfect subgroup.
    equal=all(D.contains(H.permutation(H.mul(g,H.inv(H.a)))) for g in (H.b,H.c))
    quotient_order=order//int(D.order())
    power_order=next(n for n in range(1,121) if D.contains(H.permutation(H.power(H.a,n))))
    if equal:assert power_order==quotient_order
    out={'four_strand_target_order':order,'complete_derived_orders':orders,
         'selected_generator_counts':selected,'terminal_subgroup_is_perfect':True,
         'maximal_solvable_quotient_order':quotient_order,
         'three_braid_generators_have_equal_solvable_image':equal,
         'braid_generator_order_in_solvable_quotient':power_order,
         'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(Path(__file__).with_suffix('.npz'),
                        terminal_perfect_generators=np.array([p.array_form for p in D.generators]))
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
