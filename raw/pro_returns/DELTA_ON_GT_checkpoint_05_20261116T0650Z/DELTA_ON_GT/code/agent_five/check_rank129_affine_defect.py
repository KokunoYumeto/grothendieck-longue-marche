"""Exact first probes of the actual affine rank129 pentagon target.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
D=np.load(ROOT/'ferrari_rank129_affine.npz');n=129;I=np.eye(n,dtype=np.int16);zero=np.zeros(n,dtype=np.int16);one=(zero,I)
X=list(zip(D['Xi_translations'],D['X']))
def mul(g,h):return((g[0]+g[1]@h[0])%3,g[1]@h[1]%3)
def inverse_matrix(M):
    R=np.concatenate((M.copy(),I),axis=1)
    for j in range(n):
        k=j+int(np.flatnonzero(R[j:,j])[0]);R[[j,k]]=R[[k,j]]
        if R[j,j]==2:R[j]=2*R[j]%3
        ii=np.flatnonzero(R[:,j]);ii=ii[ii!=j]
        R[ii]=(R[ii]-R[ii,j,None]*R[j])%3
    return R[:,n:]
def inv(g):
    M=inverse_matrix(g[1]);return((-M@g[0])%3,M)
def prod(*gg):
    g=one
    for h in gg:g=mul(g,h)
    return g
def comm(g,h):return prod(g,h,inv(g),inv(h))
def word(g,h,w):
    images={1:g,2:h,-1:inv(g),-2:inv(h)}
    return prod(*(images[i]for i in w))
def wi(w):return tuple(-i for i in reversed(w))
def wc(u,v):return u+v+wi(u)+wi(v)
def swap(w):return tuple((2 if abs(i)==1 else 1)*(1 if i>0 else -1)for i in w)
c=wc((1,),(2,));h=wc(c,(1,)+c+(-1,));f=h+wi(swap(h))
assert swap(f)==wi(f)
pentagon=prod(*(word(X[i],X[j],f)for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1))))
brunnian=comm(comm(X[0],X[1]),comm(X[2],X[3]))
def record(g):return{'linear_part_is_identity':bool(np.array_equal(g[1],I)),
                     'translation_nonzero_coordinates':[[int(i),int(g[0][i])]for i in np.flatnonzero(g[0])],
                     'translation_is_nonzero':bool(np.any(g[0]))}
print(json.dumps({'affine_Xi_orders':[6,6,6,12,12],
 'Brunnian_word':'[[X1,X2],[X3,X4]]','Brunnian_image':record(brunnian),
 'test_word':list(f),'test_word_properties':['belongs to F second derived','satisfies the2-cycle identically'],
 'test_pentagon_image':record(pentagon),
 'scope':'The test word is NOT asserted to satisfy the gentle3-cycle or to define any GT0 element. This only checks that the actual affine representation retains source relation information.'},indent=2))
