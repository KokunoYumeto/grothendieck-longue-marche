#!/usr/bin/env python3
"""Emit exact affine parametrizations and measure the actual frame-image space."""
import test_fivepoint_cm_level as T
from pathlib import Path
import numpy as np
import json

def affine(A,b,p):
    A=(A%p).copy();b=(b%p).copy();r=0;piv=[]
    for col in range(A.shape[1]):
        nz=np.flatnonzero(A[r:,col])
        if not len(nz):continue
        q=r+int(nz[0]);A[[r,q]]=A[[q,r]];b[[r,q]]=b[[q,r]]
        z=pow(int(A[r,col]),-1,p);A[r]=A[r]*z%p;b[r]=b[r]*z%p
        nz=np.flatnonzero(A[:,col]);nz=nz[nz!=r];f=A[nz,col].copy()
        A[nz]=(A[nz]-f[:,None]*A[r])%p;b[nz]=(b[nz]-f*b[r])%p
        piv.append(col);r+=1
        if r==A.shape[0]:break
    assert not np.any(A[r:]) and not np.any(b[r:])
    free=[j for j in range(A.shape[1]) if j not in piv]
    sol=np.zeros(A.shape[1],dtype=np.int16);sol[piv]=b[:r]
    N=np.zeros((len(free),A.shape[1]),dtype=np.int16)
    N[:,free]=np.eye(len(free),dtype=np.int16);N[:,piv]=-A[:r,free].T;N%=p
    return sol,N

def equations(base,frame,p):
    As=[];bs=[]
    for name,tokens in T.expressions.items():
        A,b=T.expression_matrix(base,tokens,p);As.append(A);bs.append(b)
    As.append(T.abloops%p)
    bs.append(-T.abelian_base_coordinates(base)%p)
    A,b=T.frame_equations(base,frame,p);As.append(A);bs.append(b)
    return np.vstack(As),np.concatenate(bs)

frame=next(fr for fr in T.frames if fr["rho"]==0 and fr["T_sign"]==-1
           and fr["T_R_power"]==0 and fr["W_power"]==0)
out={"base":0,"frame":frame,"fields":{}}
arrays={}
for p in (2,3):
    A,b=equations(0,frame,p)
    sol,N=affine(A,b,p)
    assert np.all(A@sol%p==b) and np.all(A@N.T%p==0)
    images=N@T.bloopimages[p]%p
    basis,proj=T.row_space_projection(images,p)
    out["fields"][str(p)]={"parameter_dimension":len(N),
                           "actual_E0_image_dimension":len(basis)}
    arrays[f"A{p}"]=A;arrays[f"b{p}"]=b
    arrays[f"particular{p}"]=sol;arrays[f"nullspace{p}"]=N
    arrays[f"E0_image{p}"]=T.bloopimages[p]
    print("Field",p,"source affine dimension",len(N),
          "actual E0 image dimension",len(basis),flush=True)
np.savez_compressed(Path(__file__).with_suffix(".npz"),**arrays)
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
