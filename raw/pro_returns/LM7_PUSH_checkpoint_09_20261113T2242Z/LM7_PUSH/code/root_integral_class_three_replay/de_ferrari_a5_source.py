#!/usr/bin/env python3
"""Exact permutation image of the full six-coset/six-map A5 source."""
from pathlib import Path
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
from sympy.combinatorics import PermutationGroup,Permutation
from de_ferrari_a5_model import FerrariA5
from de_ferrari_degree4_lift import InducedCombined

def main():
    start=time.time();here=Path(__file__).resolve().parent
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=FerrariA5();W=InducedCombined(H,d)
    def induced_permutation(e):
        out=[];hd=10*H.n
        for q in range(6):
            for i in range(6):
                p=H.permutation(e[1][q,i]).array_form
                out.extend((hd*(6*int(e[0][q])+i)+np.array(p)).tolist())
        return Permutation(out)
    s,r=induced_permutation(W.letters[0]),induced_permutation(W.letters[1])
    assert s**2==Permutation(list(range(s.size))) and r**3==Permutation(list(range(r.size)))
    for a in (W.letters[0],W.letters[1],W.letters[-1]):
        for b in (W.letters[0],W.letters[1],W.letters[-1]):
            assert induced_permutation(W.mul(a,b))==induced_permutation(a)*induced_permutation(b)
    G=PermutationGroup([s,r]);orbit_sizes=sorted(map(len,G.orbits()))
    np.savez_compressed(here/'de_ferrari_a5_source_generators.npz',s=np.array(s.array_form),r=np.array(r.array_form))
    print('faithful degree',s.size,'orbit sizes',orbit_sizes,flush=True)
    order=int(G.order());print('full induced source order',order,flush=True)
    out={'faithful_permutation_degree':s.size,'orbit_sizes':orbit_sizes,'induced_B_image_order':order,
         'all_six_cosets_and_evaluation_maps_retained':True,'multiplication_and_C2_C3_relations_verified':True,
         'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_a5_source.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
