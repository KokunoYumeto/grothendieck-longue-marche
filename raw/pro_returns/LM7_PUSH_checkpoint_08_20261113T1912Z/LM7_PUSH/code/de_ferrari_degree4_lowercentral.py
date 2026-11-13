#!/usr/bin/env python3
"""Exact lower-central images in the degree-four Ferrari induced core."""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy
import numpy as np
from de_ferrari_degree4_lift import Combined,InducedCombined,Span

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
H=Combined();W=InducedCombined(H,d)
q=np.load(here/'de_ferrari_degree4_module.npz')
meta=json.loads(here.joinpath('de_ferrari_degree4_module.json').read_text())
N=[W.word(w) for w in d['Nwords']]
C=q['F_prime_correction_image_basis'][:,:meta['commutator_normal_image_dimension']]
dimensions=[C.shape[1]];cert={'lower_central_image_2':C};witness=None
for weight in range(3,9):
    S=Span(C.shape[0])
    for j,v in enumerate(C.T):
        element=W.element(v)
        for i,n in enumerate(N):
            change=(W.vector(W.conj(n,element))-v)%3
            if np.any(change) and witness is None:
                witness={'weight':weight,'previous_basis_column':j,'conjugating_N_generator':i,
                         'nonzero_change_coordinates':{str(k):int(c) for k,c in enumerate(change) if c}}
            S.add(change,[])
    C=S.matrix();dimensions.append(len(S.basis));cert[f'lower_central_image_{weight}']=C
    print('gamma',weight,'image dimension',len(S.basis),flush=True)
    if not len(S.basis):break
out={'successive_N_lower_central_image_dimensions_from_weight2':dimensions,
     'first_further_nonzero_commutator':witness,
     'scope':'Exact images in the actual combined induced B-core, computed from full N conjugation on the complete normal commutator image.'}
here.joinpath('de_ferrari_degree4_lowercentral.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(here/'de_ferrari_degree4_lowercentral_certificate.npz',**cert)
print(json.dumps(out,indent=2))
