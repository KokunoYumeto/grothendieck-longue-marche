#!/usr/bin/env python3
"""Identify the new degree7 seed's reduction to the earlier H^(1) target."""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json
import numpy as np
OUT=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):D=runpy.run_path(str(OUT/'d_cm_shadow.py'))
chords=[i for i in range(len(D['Q'])) if i not in D['tree']]
assert len(chords)==97
M=np.zeros((97,97),dtype=np.int16)
for j,c in enumerate(D['cycles']):
 v=D['act'](c,D['qs'])
 for i,e in enumerate(chords):M[i,j]=(v>>e)&1
J=json.loads((OUT/'d_cm_rank4_degree7.json').read_text())['witness']
mask=int(J['lower_beta_change'],16);Z=np.zeros((97,97),dtype=np.int16)
pairs=[(i,j) for i in range(97) for j in range(i,97)]
for k,(i,j) in enumerate(pairs):
 if (mask>>k)&1:Z[i,j]=Z[j,i]=1
defect=(Z+M@Z@M.T)%2
bits=sum(1<<k for k,(i,j) in enumerate(pairs) if defect[i,j])
assert bits
result={'new_seed_changes_D30_H1_action':True,
 'changed_generator':'s','nonzero_central_difference':hex(bits),
 'formula':'(1-Ad(s)) on the lower beta central correction in N-class2 exponent4',
 'why_other_changes_vanish':'upper twice-central corrections and gamma3N corrections vanish in H^(1)',
 'scope':'The new target canonically projects to D30 target, but the recorded automorphism is an explicitly different central representative with the same G6 homology data.'}
(OUT/'d_cm_degree7_reduction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='nonzero_central_difference'},indent=2))
