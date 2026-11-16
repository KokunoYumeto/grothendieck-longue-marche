#!/usr/bin/env python3
"""Exploratory exact bilinear maps on the mod-three coinvariant kernel."""
from math import comb
from pathlib import Path
import numpy as np

def nullspace(matrix):
    A=np.array(matrix,dtype=np.int64,copy=True)%3
    pivots=[];row=0
    for col in range(A.shape[1]):
        candidates=np.flatnonzero(A[row:,col])
        if not len(candidates):continue
        p=row+int(candidates[0]);A[[row,p]]=A[[p,row]]
        if A[row,col]==2:A[row]=2*A[row]%3
        nonzero=np.flatnonzero(A[:,col]);nonzero=nonzero[nonzero!=row]
        A[nonzero]=(A[nonzero]-A[nonzero,col,None]*A[row])%3
        pivots.append(col);row+=1
        if row==A.shape[0]:break
    out=[]
    for col in range(A.shape[1]):
        if col in pivots:continue
        v=np.zeros(A.shape[1],dtype=np.int64);v[col]=1
        for i,p in enumerate(pivots):v[p]=-A[i,col]%3
        out.append(v)
    return out

lines=[]
for n in range(1,4):
    N=3**n;start=N//3+1;length=N-start
    tau=np.eye(length,dtype=np.int64)
    for i in range(length-1):tau[i+1,i]=1
    sigma=np.zeros((length,length),dtype=np.int64)
    for col in range(length):
        k=start+col
        for j in range(k+1):
            row=k+j-start
            if 0<=row<length:
                sigma[row,col]=(2*comb(k,j)*pow(2,k-j,3))%3
    equations=[]
    for matrix,character in [(tau,1),(sigma,2)]:
        for i in range(length):
            for j in range(length):
                row=np.kron(matrix[:,i],matrix[:,j])
                row[i*length+j]-=character
                equations.append(row%3)
    basis=nullspace(equations)
    alt=all(np.all((b.reshape(length,length)+b.reshape(length,length).T)%3==0)
            for b in basis)
    lines.append(f'n={n}: kernel dimension {length}; equivariant bilinear dimension '
                 f'{len(basis)}; every basis form alternating={alt}.')
    print(lines[-1],flush=True)
Path(__file__).with_name('relative_coinvariant_kernel_probe_output.txt').write_text(
    '\n'.join(lines)+'\n')
