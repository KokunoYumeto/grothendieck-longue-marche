#!/usr/bin/env python3
"""All multiplier lifts and full gentle norm equations at the 2-refinement.
Includes the exact commutator-image condition through F^ab, and verifies
both order equations for every retained solution. Generation follows from
the original invertible action on the Frattini quotient of the pure kernel.
"""
from contextlib import redirect_stdout
from pathlib import Path
import ctypes,io,json,runpy,time
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_class2_two.py'))
n,nw,up=d['n'],d['nw'],d['upper'];R,S=d['R'],d['S'];D=d['D'];R2=R@R%2
DR2=np.zeros((nw,nw),dtype=np.uint8);DR2[:n,:n]=R2.T
for i in range(n):DR2[i,i]^=1
for col,(i,j) in enumerate(zip(*up),n):
    DR2[:n,col]=R2[i]*R2[j]
    DR2[n:,col]=(np.outer(R2[i],R2[j])+np.outer(R2[j],R2[i]))[up]%2;DR2[col,col]^=1
matrix=np.zeros((2*nw+2,nw+48),dtype=np.uint8)
matrix[:nw,:nw]=D[:nw].T
matrix[nw:2*nw,:nw]=D[nw:].T^DR2.T
for i in range(nw):matrix[nw+i,i]^=1
base=d['d'];v=d['v']
abel=np.array([[sum(1 if a==letter else -1 if a==-letter else 0 for a in w) for w in base['Nfwords']] for letter in (1,2)],dtype=np.int64)
H=hermite_normal_form(sp.Matrix(abel.tolist()));coords=H.inv()*sp.Matrix(abel.tolist())
assert all(x.q==1 for x in coords);abel_coords=np.array(coords.tolist(),dtype=np.int64)
matrix[2*nw:,:n]=abel_coords%2
print('F-abelian image lattice of N_B:',H.tolist(),flush=True)
cert=[r for r in d['cert'] if 'mod6_beta_cycles' in r];errors=[]
for j,rec in enumerate(cert):
    beta=v['representative'](rec['beta']);wb=[]
    for i,w in enumerate(base['Nwords']):wb+=w*rec['mod6_beta_cycles'].get(str(i),0)
    wb+=base['Bpaths'][beta]
    for h in range(2):
        Rword=wb+[0]+base['binv'](wb)+[0,1]*(1+72*h)
        err=d['kernel_coordinate'](Rword*3);errors.append(err);matrix[nw:2*nw,nw+2*j+h]=err
original=matrix[:,:nw].copy();piv=np.zeros(nw+48,dtype=np.int32)
print('Solving full gentle equations for 24 shadows and both multiplier residues.',flush=True);start=time.time()
rank=d['gf'](matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*matrix.shape,piv.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
piv=piv[:rank].tolist();dom=[p for p in piv if p<nw];ra=len(dom);records=[];counts=[0,0]
for j,rec in enumerate(cert):
    choices=[]
    for h in range(2):
        col=nw+2*j+h;passes=not np.any(matrix[ra:,col]);item={'lambda_mod144':1+72*h,'passes':passes}
        if passes:
            k=np.zeros(nw,dtype=np.uint8);k[dom]=matrix[:ra,col]
            rhs=np.concatenate((np.zeros(nw,dtype=np.uint8),errors[2*j+h],np.zeros(2,dtype=np.uint8)))
            assert np.array_equal(original.astype(np.uint16)@k.astype(np.uint16)%2,rhs)
            item['central_correction_sparse']={str(i):int(a) for i,a in enumerate(k) if a}
        choices.append(item)
    success=any(x['passes'] for x in choices);missing=bool(rec['missing_coset']);counts[int(missing)]+=success
    row={'certificate_index':j,'missing_coset':missing,'gentle_shadow_lift_exists':success,'multiplier_choices':choices};records.append(row)
    print(json.dumps({k:v for k,v in row.items() if k!='multiplier_choices'}),flush=True)
out={'F_abelian_image_lattice':[[int(x) for x in row] for row in H.tolist()],'full_norm_and_commutator_rank':ra,'augmented_rank':rank,'pass_counts':counts,'elapsed_seconds':round(time.time()-start,3),'records':records,'scope':'Exact finite gentle shadow fibres over the 24 recorded base shadows, both multiplier residues modulo144, exact commutator image; generation follows from Frattini-quotient invertibility.'}
(here/'de_class2_two_gentle.json').write_text(json.dumps(out,indent=2)+'\n');print('Completed full gentle test:',counts,flush=True)
