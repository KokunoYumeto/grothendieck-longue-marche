#!/usr/bin/env python3
"""Binary Ferrari core helpers with exact literal group arithmetic."""
import numpy as np
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_degree5_lift import apply_word,chunk_trie

class Span2:
    def __init__(self,n):self.n=n;self.rows={};self.basis=[];self.words=[]
    def reduce(self,v):
        v=v.copy()%2;c=np.zeros(self.n,dtype=np.int64)
        for p,(r,b) in sorted(self.rows.items()):
            if v[p]:v=(v+r)%2;c=(c+b)%2
        return v,c
    def add(self,v,w):
        r,c=self.reduce(v);nz=np.flatnonzero(r)
        if not len(nz):return False
        p=int(nz[0]);k=len(self.basis);b=c.copy();b[k]^=1
        self.rows[p]=(r,b);self.basis.append(v.copy()%2);self.words.append(w)
        return True
    def coordinates(self,v):
        r,c=self.reduce(v);assert not np.any(r)
        return c[:len(self.basis)]
    def matrix(self):
        return np.array(self.basis,dtype=np.int64).T if self.basis else np.zeros((self.n,0),dtype=np.int64)

def rref2(A):
    A=np.array(A,dtype=np.int64)%2;piv=[];row=0
    for col in range(A.shape[1]):
        possible=np.flatnonzero(A[row:,col])
        if not len(possible):continue
        i=row+int(possible[0]);A[[row,i]]=A[[i,row]]
        for j in range(A.shape[0]):
            if j!=row and A[j,col]:A[j]=(A[j]+A[row])%2
        piv.append(col);row+=1
        if row==A.shape[0]:break
    return A,piv

def solve2(A,b):
    A=np.array(A,dtype=np.int64)%2;b=np.array(b,dtype=np.int64)%2
    R,piv=rref2(np.column_stack((A,b)));n=A.shape[1]
    if n in piv:return None
    x=np.zeros(n,dtype=np.int64)
    for i,p in enumerate(piv):x[p]=R[i,n]
    free=[j for j in range(n) if j not in piv];K=np.zeros((n,len(free)),dtype=np.int64)
    for k,j in enumerate(free):
        K[j,k]=1
        for i,p in enumerate(piv):K[p,k]=R[i,j]
    assert np.array_equal(A@x%2,b) and not np.any(A@K%2)
    return x,K

class InducedTwo(InducedCombined):
    def __init__(self,H,d,lower_degree=4):
        self.chunks=None;self.lower_degree=lower_degree
        super().__init__(H,d)
        self.width=3*(H.n-(2**(lower_degree+1)-2))
    def word(self,w):
        return apply_word(self,w,self.letters,self.chunks)
    def vector(self,x):
        assert np.array_equal(x[0],self.id)
        return self.H.relative_kernel_vector(x[1],self.lower_degree).ravel()
    def element(self,v):
        return self.id,self.H.relative_kernel_element(v.reshape(6,6,self.width),self.lower_degree)
