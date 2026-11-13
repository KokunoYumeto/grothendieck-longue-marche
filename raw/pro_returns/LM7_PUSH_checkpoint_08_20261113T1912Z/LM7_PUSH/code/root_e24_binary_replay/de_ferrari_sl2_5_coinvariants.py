#!/usr/bin/env python3
"""Complete action coinvariants in the new Nprime elementary kernel.

This records the central directions for which module commutators alone
do not prove perfection; the full second-derived computation is needed.
"""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_sl2_5_source import Source
from de_ferrari_two_core import Span2

def main():
    start=time.time();here=Path(__file__).resolve().parent
    M=Source();W=M.W
    cert=np.load(here/'de_ferrari_sl2_5_Nprime.npz')
    V=cert['kernel_basis'];S=Span2(36*57)
    gs=[(W.id,g) for g in cert['chosen_component_images']]
    for i,v in enumerate(V.T):
        k=M.element(v)
        for j,g in enumerate(gs):S.add(M.vector(W.comm(g,k)),[i,j])
    out={'Nprime_kernel_dimension':V.shape[1],
         'Nprime_kernel_commutator_dimension':len(S.basis),
         'coinvariant_dimension':V.shape[1]-len(S.basis),
         'all_basis_commutators_checked':V.shape[1]*len(gs),
         'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_sl2_5_coinvariants.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_sl2_5_coinvariants.npz',
                        commutator_basis=S.matrix(),basis_input_pairs=np.array(S.words))
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
