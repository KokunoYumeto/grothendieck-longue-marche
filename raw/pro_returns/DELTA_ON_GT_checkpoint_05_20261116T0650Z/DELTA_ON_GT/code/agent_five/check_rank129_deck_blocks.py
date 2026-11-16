"""Exact character decomposition of the rank129 mixed-prime Ferrari target.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129.npz');Q=F['Q'];edges=F['edges'];cycles=F['cycles'];chords=F['chords'];n=129
I=np.eye(n,dtype=np.int16);idx={tuple(map(int,q)):i for i,q in enumerate(Q)}
direct={}
for k,(q,r,i)in enumerate(edges):direct[(int(q),int(i))]=(k,1);direct[(int(r),int(i))]=(k,-1)
bs=[];piv={}
for v,b in Q:
    if b:continue
    v=int(v);w=v
    for i,r in sorted(piv.items(),reverse=True):
        if w&(1<<i):w^=r
    if w:piv[w.bit_length()-1]=w;bs.append(v)
assert len(bs)==5
coordinates={0:0}
for mask in range(32):
    v=0
    for j,b in enumerate(bs):
        if mask&(1<<j):v^=b
    coordinates[v]=mask
assert len(coordinates)==32
deck=[]
for v in bs:
    P=np.array([idx[(int(q[0])^v,int(q[1]))]for q in Q],dtype=np.int16)
    C=np.zeros_like(cycles)
    for k,(q,r,i)in enumerate(edges):
        j,s=direct[(int(P[q]),int(i))];C[j]=s*cycles[k]%3
    M=C[chords];assert np.array_equal(cycles@M%3,C)
    assert np.array_equal(M@M%3,I);deck.append(M)
for a in deck:
    for b in deck:assert np.array_equal(a@b%3,b@a%3)
def colbasis(M):
    T=M.T.copy();piv=[];r=0
    for j in range(T.shape[1]):
        inds=np.flatnonzero(T[r:,j])
        if not len(inds):continue
        k=r+int(inds[0]);T[[r,k]]=T[[k,r]]
        if T[r,j]==2:T[r]=2*T[r]%3
        kk=np.flatnonzero(T[:,j]);kk=kk[kk!=r]
        T[kk]=(T[kk]-T[kk,j,None]*T[r])%3
        piv.append(j);r+=1
        if r==T.shape[0]:break
    # Nonzero rows now form a basis of the column space of original M.
    return T[:r].T
spaces={0:I}
for j,T in enumerate(deck):
    new={}
    for mask,B in spaces.items():
        for bit,s in ((0,1),(1,2)):
            U=colbasis((B+s*T@B)%3)
            if U.shape[1]:new[mask|(bit<<j)]=U
    spaces=new
assert len(spaces)==32
assert spaces[0].shape[1]==5 and all(B.shape[1]==4 for m,B in spaces.items()if m)
masks=sorted(spaces);S=np.concatenate([spaces[m]for m in masks],axis=1)
def inverse(M):
    T=np.concatenate((M.copy(),I),axis=1)
    for j in range(n):
        k=j+int(np.flatnonzero(T[j:,j])[0]);T[[j,k]]=T[[k,j]]
        if T[j,j]==2:T[j]=2*T[j]%3
        kk=np.flatnonzero(T[:,j]);kk=kk[kk!=j]
        T[kk]=(T[kk]-T[kk,j,None]*T[j])%3
    assert np.array_equal(T[:,:n],I);return T[:,n:]
Si=inverse(S)
offset={};start=0
for m in masks:offset[m]=(start,start+spaces[m].shape[1]);start+=spaces[m].shape[1]
for j,T in enumerate(deck):
    diag=Si@T@S%3
    expected=np.zeros((n,n),dtype=np.int16)
    for m in masks:
        a,b=offset[m];expected[a:b,a:b]=(2 if m&(1<<j)else 1)*np.eye(b-a,dtype=np.int16)
    assert np.array_equal(diag,expected)
ABC=np.stack([Si@F[key]@S%3 for key in ('A','B','C')]);XX=np.stack([Si@M@S%3 for M in F['X']])
def block_permutation(M):
    perm=[]
    for m in masks:
        a,b=offset[m];targets=[r for r in masks if np.any(M[offset[r][0]:offset[r][1],a:b])]
        assert len(targets)==1;perm.append(targets[0])
    assert len(set(perm))==32
    return tuple(perm)
abcperms=[block_permutation(M)for M in ABC]
xperms=[block_permutation(M)for M in XX]
def orbits(gens):
    remaining=set(masks);ans=[]
    while remaining:
        start=min(remaining);orb={start};todo=[start]
        while todo:
            a=todo.pop()
            for g in gens:
                b=g[a]
                if b not in orb:orb.add(b);todo.append(b)
        remaining-=orb;ans.append(sorted(orb))
    return ans
fullorbits=orbits(abcperms)
pairorbits={f'{i+1}{j+1}':orbits([xperms[i],xperms[j]])for i,j in ((0,1),(2,3),(3,4))}
np.savez_compressed(ROOT/'ferrari_rank129_blocks.npz',basis=S,basis_inverse=Si,
                    A=ABC[0],B=ABC[1],C=ABC[2],X=XX,deck=np.stack(deck),
                    offsets=np.array([offset[m]for m in masks],dtype=np.int16),
                    abc_permutations=np.array(abcperms,dtype=np.int16),x_permutations=np.array(xperms,dtype=np.int16),
                    deck_basis=np.array(bs,dtype=np.int16))
print(json.dumps({'deck_group_order':32,'deck_generators_cube_chains':bs,
 'character_dimensions':{m:int(spaces[m].shape[1])for m in masks},
 'full_L_character_orbits':fullorbits,
 'pair_character_orbits':pairorbits,
 'a_b_c_character_permutations':abcperms,
 'Xi_character_permutations':xperms,
 'exact_simultaneous_eigenbasis_verified':True,
 'scope':'All block restrictions retain the exact common source word evaluation.'},indent=2))
