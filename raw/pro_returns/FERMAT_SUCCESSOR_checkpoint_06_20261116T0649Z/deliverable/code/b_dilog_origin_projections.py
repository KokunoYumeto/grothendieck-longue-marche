#!/usr/bin/env python3
"""The two exact integral functionals on homogeneous cusp-origin changes."""
import json
from pathlib import Path
import numpy as np

j=json.loads(Path('deliverable/code/b_unit_pencils.json').read_text())
a=np.load('deliverable/code/b_arbitrary_action_analysis_matrices.npz')
glob=np.load('deliverable/code/b_global_action_ambiguity_matrices.npz')
bpairs=[(i,j) for i in range(8) for j in range(i)]
def wedge(M):
    return np.array([[int(M[a,i])*int(M[b,j])-int(M[a,j])*int(M[b,i])
                     for i,j in bpairs] for a,b in bpairs],dtype=np.int64)
records=[]
for triple,P in [([0,2,12],0),([0,10,18],6)]:
    r=next(r for r in j['records'] if r['lines']==triple)
    PV=np.array(r['V_map'],dtype=np.int64);PW=PV[:,2:]
    T=next(g for g in glob['projective_automorphisms']
           if np.array_equal(g[:2,:2],np.eye(2,dtype=np.int64))
           and np.array_equal(-g[2:,2:]@np.ones(8,dtype=np.int64),np.eye(8,dtype=np.int64)[:,P]))
    F=np.array([PW[1,i]*PW[0,k]-PW[0,i]*PW[1,k] for i,k in bpairs],dtype=np.int64)
    vals=[int(F@(3*(wedge(T[2:,2:])-np.eye(28,dtype=np.int64))
                 @a['boundary_bracket_parameters'][:,gen])) for gen in range(2)]
    assert vals==([9,0] if P==0 else [0,54])
    rec={'lines':triple,'endpoint':P,'V_map':PV.tolist(),
         'Lambda2_W_functional':F.tolist(),'origin_shift_scalars':vals,
         'value_at_O':r['value_at_O'],'function':r['function']}
    records.append(rec)
    print(json.dumps(rec),flush=True)
Path('deliverable/code/b_dilog_origin_projections.json').write_text(json.dumps(records,indent=2)+'\n')
