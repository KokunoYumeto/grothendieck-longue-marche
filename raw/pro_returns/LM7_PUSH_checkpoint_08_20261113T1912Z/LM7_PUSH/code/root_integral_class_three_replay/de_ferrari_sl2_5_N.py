#!/usr/bin/env python3
"""Complete image of the actual rank97 N in the SL2(F5) induced source."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation
from de_ferrari_sl2_5_source import Source
from de_lifted_schreier_extra import lifted_kernel

here=Path(__file__).resolve().parent

def main():
    start=time.time();model=Source();H,W,d=model.H,model.W,model.d
    old=json.loads((here/'de_ferrari_a5_corrections.json').read_text())
    oldimages=np.load(here/'de_ferrari_a5_corrections.npz')['N_images']
    N=[W.word(w) for w in d['Nwords']]
    perms=[Permutation(p.tolist()+list(range(1980,2124))) for p in oldimages]
    for n,p in zip(N,perms):assert model.permutation(n)==p
    selected=old['N_selected_generator_indices'];others=[i for i in range(97) if i not in selected]
    G,S,info=lifted_kernel(W,[N[i] for i in selected],[perms[i] for i in selected],
        model.vector,model.element,36*57,known_order=old['N_image_order'],
        extra_lifts=[(perms[i],N[i]) for i in others])
    out={**info,'actual_rank97_N_generators_retained':True,
         'selected_original_N_indices':selected,'extra_original_N_indices':others,
         'input_generator_literal_B_words':[d['Nwords'][i] for i in selected+others],
         'total_seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_sl2_5_N.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_sl2_5_N.npz',N_kernel_basis=S.matrix(),
                        N_component_images=np.array([n[1] for n in N]),
                        base_strong_generators=np.array([p.array_form for p in G.strong_gens]))
    print(json.dumps({k:v for k,v in out.items() if k not in ('literal_word_DAG','kernel_basis_word_nodes','input_generator_literal_B_words')},indent=2),flush=True)

if __name__=='__main__':main()
