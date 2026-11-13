#!/usr/bin/env python3
"""Exact lower central series of N in the complete binary E24 B-core."""
from pathlib import Path
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo,Span2,chunk_trie

def main():
    start=time.time();here=Path(__file__).resolve().parent
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=FerrariTwo(6);W=InducedTwo(H,d,4)
    N=[W.word(w) for w in d['Nwords']];W.chunks=chunk_trie(d,N,W)
    metadata=json.loads((here/'de_ferrari_two_degree6_module.json').read_text())
    data=np.load(here/'de_ferrari_two_degree6_module.npz')
    commrank=metadata['commutator_normal_image_dimension']
    basis=data['F_prime_basis'][:,:commrank]
    # The first commrank entries are the complete normal commutator
    # image, before the independent sixth-power/F-prime contributions.
    assert commrank==6
    levels=[basis];ranks=[basis.shape[1]]
    while levels[-1].shape[1]:
        S=Span2(36*W.width)
        for v in levels[-1].T:
            e=W.element(v)
            for n in N:S.add(W.vector(W.comm(n,e)),[])
        # Exact normal closure; all operations lie in the proved
        # elementary abelian degree-five/six congruence kernel.
        at=0
        while at<len(S.basis):
            e=W.element(S.basis[at])
            for n in N:S.add(W.vector(W.conj(n,e)),[])
            at+=1
        levels.append(S.matrix());ranks.append(len(S.basis))
        print('gamma',len(levels)+1,'rank',len(S.basis),flush=True)
        assert len(levels)<=41
    out={'relative_group':'image of N in all 36 components of the induced binary degree-six core',
         'gamma2_and_following_ranks':ranks,'first_trivial_lower_central_term':len(ranks)+1,
         'complete_normal_commutator_image_input':True,
         'all_97_N_conjugations_retained':True,'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_two_lowercentral.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_two_lowercentral.npz',**{f'gamma_{j+2}':b for j,b in enumerate(levels)})
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
