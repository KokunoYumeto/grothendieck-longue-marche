#!/usr/bin/env python3
"""Exact component groups of the six A5 Ferrari evaluation morphisms."""
from pathlib import Path
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
from sympy.combinatorics import PermutationGroup,Permutation
from sympy import factorint
from de_ferrari_a5_model import FerrariA5
from de_ferrari_degree4_lift import InducedCombined

def main():
    start=time.time();here=Path(__file__).resolve().parent
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=FerrariA5();W=InducedCombined(H,d)
    N=[W.word(w) for w in d['Nwords']]
    q=PermutationGroup([Permutation(H.a[:H.n].tolist()),Permutation(H.b[:H.n].tolist())])
    print('kernel-factor permutation image',q.order(),factorint(q.order()),flush=True)
    rows=[]
    for i in range(6):
        at=time.time();F=PermutationGroup([H.permutation(H.x[i]),H.permutation(H.y[i])])
        fg=int(F.order());print('i',i,'F order',fg,flush=True)
        gens={tuple(n[1][W.root,i]) for n in N}
        selected=[];G=PermutationGroup([H.permutation(H.one)])
        for g in sorted(gens):
            pg=H.permutation(np.array(g,dtype=np.int64))
            if not G.contains(pg):selected.append(pg);G=PermutationGroup(selected)
        assert all(G.contains(H.permutation(np.array(g,dtype=np.int64))) for g in gens)
        ng=int(G.order());print('i',i,'N order',ng,'quotient',fg//ng,flush=True)
        D=G.derived_subgroup();dg=int(D.order());print('i',i,'derived order',dg,'abelian quotient',ng//dg,flush=True)
        row={'evaluation_index':i,'F_image_order':fg,'N_image_order':ng,'F_mod_N_image_order':fg//ng,
             'N_derived_order':dg,'N_abelianization_order':ng//dg,'distinct_N_generator_images':len(gens),
             'selected_N_generators':len(selected),
             'N_order_factorization':{str(p):e for p,e in factorint(ng).items()},
             'seconds':round(time.time()-at,3)}
        rows.append(row)
        here.joinpath('de_ferrari_a5_components.json').write_text(json.dumps({'records':rows,'seconds':round(time.time()-start,3)},indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_a5_components.npz',N_images=np.array([n[1] for n in N]),
                        s_perm=W.letters[0][0],s_values=W.letters[0][1],
                        r_perm=W.letters[1][0],r_values=W.letters[1][1])
    print('complete',round(time.time()-start,3),flush=True)

if __name__=='__main__':main()
