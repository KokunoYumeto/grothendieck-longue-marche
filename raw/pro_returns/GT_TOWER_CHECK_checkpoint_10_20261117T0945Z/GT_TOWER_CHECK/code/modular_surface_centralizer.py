#!/usr/bin/env python3
"""Exact CM-centralizer image in the actual K4 class-two surface target."""
import modular_level_surface_class2 as M
import numpy as np,json
from pathlib import Path
W=M.W;h=M.mul(M.gens[0],M.gens[1]);Mh=h[1]
DW=np.array([(w-M.act(Mh,w))%3 for w in W])
R,piv=M.rref(DW);free=[i for i in range(M.odim) if i not in piv]
def obstruction(v):return (v[free]-v[piv]@R[:,free])%3
records=[]
for qi,q in enumerate(M.linear):
 rep=M.reps[qi]
 if not np.array_equal(rep[1]@Mh%3,Mh@rep[1]%3):continue
 rhs=(h[0]+M.act(Mh,rep[0])-rep[0]-M.act(rep[1],h[0]))%3
 obs=obstruction(rhs)
 records.append({'mod12_matrix':q.tolist(),'representative_index':qi,
                 'lifts_to_CM_centralizer':bool(not np.any(obs)),
                 'obstruction_nonzero_entries':[[int(i),int(x)] for i,x in enumerate(obs) if x]})
print('CM centralizer base residues:',len(records),flush=True)
print('CM centralizer base survivors in actual surface target:',sum(r['lifts_to_CM_centralizer'] for r in records),flush=True)
print('Centralizer kernel dimension:',len(W)-len(R),flush=True)
for r in records:
 if r['lifts_to_CM_centralizer']:print('SURVIVOR',r['mod12_matrix'],flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Actual characteristic surface quotient centralizer census',
 'surface_quotient_order':'16*3^153','actual_modular_IA_rank':len(W),
 'centralizer_base_residues':len(records),'centralizer_base_survivors':sum(r['lifts_to_CM_centralizer'] for r in records),
 'centralizer_kernel_dimension':len(W)-len(R),'records':records},indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),CM_C=h[0],CM_M=h[1],coboundaries=DW,
 reduced_coboundaries=R,pivots=np.array(piv),free=np.array(free))
