#!/usr/bin/env python3
"""Full multiplier-one gentle shadow equations at the exponent-three cover.
Uses (S0*k)^2=1 and (k^-1*R0)^3=1, with S0*R0=t and k in M.
This explicitly tests the finite torsion-conjugacy issue in the preceding
peripheral obstruction computation, with generation proved from N_ab/3.
"""
from contextlib import redirect_stdout
from pathlib import Path
import ctypes,io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_class2_refinement.py'))
S,R=d['S'],d['R'];R2=R@R%3;up=d['upper'];nw=len(up[0]);I=np.eye(97,dtype=np.int64)
operators=[I,S,R,R@S%3,R2,R2@S%3];signs=[1,-1,1,-1,1,-1]
matrix=np.zeros((nw,nw+24),dtype=np.uint8)
for col,(i,j) in enumerate(zip(*up)):
    vec=np.zeros(nw,dtype=np.int64)
    for a,sign in zip(operators,signs):vec+=sign*(np.outer(a[:,i],a[:,j])-np.outer(a[:,j],a[:,i]))[up]
    matrix[:,col]=vec%3
base=d['d'];v=d['v'];cert=[a for a in d['cert'] if 'mod6_beta_cycles' in a]
errors=[]
for j,rec in enumerate(cert):
    beta=v['representative'](rec['beta']);wb=[]
    for i,w in enumerate(base['Nwords']):wb+=w*rec['mod6_beta_cycles'].get(str(i),0)
    wb+=base['Bpaths'][beta]
    Rword=wb+[0]+base['binv'](wb)+[0,1]
    E=d['class2'](Rword*3);errors.append(E);matrix[:,nw+j]=E[up]
print('Solving all 24 complete gentle norm systems.',flush=True)
start=time.time();piv=np.zeros(nw,dtype=np.int32)
rank=d['gf'](matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*matrix.shape,piv.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
piv=piv[:rank].tolist();domain_piv=[p for p in piv if p<nw];rankA=len(domain_piv)
counts=[0,0];records=[]
for j,rec in enumerate(cert):
    passes=not np.any(matrix[rankA:,nw+j]);missing=bool(rec['missing_coset']);counts[int(missing)]+=passes
    row={'certificate_index':j,'missing_coset':missing,'gentle_shadow_lift_exists':passes}
    if passes:
        w=np.zeros(nw,dtype=np.int64);w[domain_piv]=matrix[:rankA,nw+j]
        W=np.zeros((97,97),dtype=np.int64);W[up]=w;W=(W-W.T)%3
        K=(W-S@W@S.T)%3
        assert not np.any((K+S@K@S.T)%3)
        assert np.array_equal((K+R@K@R.T+R2@K@R2.T)%3,errors[j])
        row['central_correction_sparse']={str(i):int(c) for i,c in enumerate(K[up]) if c}
    records.append(row);print(json.dumps({k:v for k,v in row.items() if k!='central_correction_sparse'}),flush=True)
out={'norm_map_rank':rankA,'augmented_rank':rank,'pass_counts':counts,'elapsed_seconds':round(time.time()-start,3),'records':records,'scope':'Exact multiplier-one gentle finite shadow lifts; each passing lift has generation because its map on N_ab/3 is the recorded invertible map.'}
(here/'de_class2_gentle.json').write_text(json.dumps(out,indent=2)+'\n');print('Completed gentle test:',counts,flush=True)
