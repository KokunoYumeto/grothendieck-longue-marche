"""Exact1+3 open-Prym splitting of the24 two-branch character spaces.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129.npz');B=np.load(ROOT/'ferrari_rank129_blocks.npz');D=np.load(ROOT/'ferrari_rank129_boundary.npz')
meta=json.loads((ROOT/'check_rank129_prym.out').read_text());chars=meta['two_branch_characters'];Q=F['Q'];edges=F['edges'];cycles=F['cycles'];chords=F['chords'];off=B['offsets']
idx={tuple(map(int,q)):i for i,q in enumerate(Q)}
edge_labels=[(i,q)for i in range(3)for q in range(8)if not(q&(1<<i))];ei={e:j for j,e in enumerate(edge_labels)}
acts=[]
for i in range(3):
    p=[ei[(j,(q^(1<<i))&~(1<<j))]for j,q in edge_labels];tab=[0]*4096
    for v in range(1,4096):
        low=v&-v;k=low.bit_length()-1;tab[v]=tab[v^low]^(1<<p[k])
    acts.append(tab)
direct={}
for k,(q,r,i)in enumerate(edges):direct[(int(q),int(i))]=(k,1);direct[(int(r),int(i))]=(k,-1)
deck=[]
for i in range(3):
    v0=1<<ei[(i,0)];perm=np.array([idx[(v0^acts[i][int(q[0])],(1<<i)^int(q[1]))]for q in Q])
    image=np.zeros_like(cycles)
    for k,(q,r,j)in enumerate(edges):
        l,s=direct[(int(perm[q]),int(j))];image[l]=s*cycles[k]%3
    M=image[chords];assert np.array_equal(cycles@M%3,image)
    N=D['basis_inverse']@B['basis_inverse']@M@B['basis']@D['basis']%3
    assert np.array_equal(N@N%3,np.eye(129,dtype=np.int16));deck.append(N)
def colbasis(M):
    R=M.T.copy();r=0
    for j in range(R.shape[1]):
        ix=np.flatnonzero(R[r:,j])
        if not len(ix):continue
        k=r+int(ix[0]);R[[r,k]]=R[[k,r]]
        if R[r,j]==2:R[r]=2*R[r]%3
        kk=np.flatnonzero(R[:,j]);kk=kk[kk!=r]
        R[kk]=(R[kk]-R[kk,j,None]*R[r])%3;r+=1
        if r==R.shape[0]:break
    return R[:r].T
def inverse(M):
    n=M.shape[0];R=np.concatenate((M.copy(),np.eye(n,dtype=np.int16)),axis=1)
    for j in range(n):
        k=j+int(np.flatnonzero(R[j:,j])[0]);R[[j,k]]=R[[k,j]]
        if R[j,j]==2:R[j]=2*R[j]%3
        kk=np.flatnonzero(R[:,j]);kk=kk[kk!=j]
        R[kk]=(R[kk]-R[kk,j,None]*R[j])%3
    return R[:,n:]
T=np.eye(129,dtype=np.int16);Ti=T.copy();records=[];extra=[];open_ix=[]
I4=np.eye(4,dtype=np.int16)
for m in chars:
    a,b=off[m];stabilizers=[]
    for i,N in enumerate(deck):
        rows=[j for j in range(129)if j<a or j>=b]
        if not np.any(N[np.ix_(rows,range(a,b))]):
            K=N[a:b,a:b];plus=colbasis((I4+K)%3);minus=colbasis((I4-K)%3)
            stabilizers.append((i,K,plus,minus))
    possibilities=[r for r in stabilizers if sorted((r[2].shape[1],r[3].shape[1]))==[1,3]]
    assert len(possibilities)==1
    i,K,plus,minus=possibilities[0]
    small,large,e=(plus,minus,2)if plus.shape[1]==1 else(minus,plus,1)
    assert not np.any(small[2:])
    boundary=colbasis((I4+e*K)[:,:2]%3)
    assert boundary.shape[1]==1 and not np.any(boundary[2:])
    cols=[boundary[:,0]]
    for j in range(3):
        v=large[:,j]
        if colbasis(np.array(cols+[v]).T).shape[1]>len(cols):cols.append(v)
    assert len(cols)==3
    S=np.concatenate((small,np.array(cols).T),axis=1)
    assert S.shape==(4,4)
    T[a:b,a:b]=S;Ti[a:b,a:b]=inverse(S)
    extra.append(a);open_ix.extend(range(a+1,b))
    records.append({'character':m,'hyperelliptic_involution_generator':i,
                    'three_dimensional_eigenvalue':e,'boundary_dimension_in_three_block':1})
ABC=np.stack([Ti@D[k]@T%3 for k in ('A','B','C')]);XX=np.stack([Ti@M@T%3 for M in D['X']])
alltwo=sorted(extra+open_ix)
for M in ABC:
    assert not np.any(M[np.ix_(extra,open_ix)])
    assert not np.any(M[np.ix_(open_ix,extra)])
    assert not np.any(M[np.ix_([i for i in range(129)if i not in alltwo],alltwo)])
openABC=np.stack([M[np.ix_(open_ix,open_ix)]for M in ABC]);openX=np.stack([M[np.ix_(open_ix,open_ix)]for M in XX])
np.savez_compressed(ROOT/'ferrari_open_prym72.npz',A=openABC[0],B=openABC[1],C=openABC[2],X=openX,
                    character_list=np.array(chars,dtype=np.int16),source_basis=T,source_basis_inverse=Ti,
                    extra_indices=np.array(extra,dtype=np.int16),open_indices=np.array(open_ix,dtype=np.int16))
np.savez_compressed(ROOT/'ferrari_rank129_open_split.npz',A=ABC[0],B=ABC[1],C=ABC[2],X=XX,basis=T,basis_inverse=Ti)
print(json.dumps({'two_branch_character_count':24,'invariant_extra_boundary_rank':24,
 'open_Prym_rank':72,'block_decomposition':'one boundary line plus a rank3 extension of properH1(rank2) by one boundary line',
 'all_L_generators_preserve_the_exact1_plus3_splitting':True,
 'character_records':records,
 'fixed_character1_Xi_blocks':[
   {'generator':j+1,'target_character':int(B['x_permutations'][j,1]),
    'rank3_block':XX[j,off[int(B['x_permutations'][j,1])][0]+1:off[int(B['x_permutations'][j,1])][1],off[1][0]+1:off[1][1]].tolist()}
   for j in range(5)],
 'scope':'Exact deck-involution eigenspaces; no geometric identification is substituted for a matrix identity.'},indent=2))
