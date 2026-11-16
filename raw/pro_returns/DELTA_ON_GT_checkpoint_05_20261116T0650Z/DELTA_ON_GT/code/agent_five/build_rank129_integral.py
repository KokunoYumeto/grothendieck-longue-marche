"""Exact integral chain maps and3-adically saturated boundary coordinates.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
No coefficient is lifted from an arbitrary mod3 homology matrix.
"""
from pathlib import Path
from collections import deque
import numpy as np,json
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129.npz');Q=F['Q'];right=F['right'];edges=F['edges'];chords=list(map(int,F['chords']));autos=F['vertex_actions']
direct={}
for k,(q,r,i)in enumerate(edges):direct[(int(q),int(i))]=(k,1);direct[(int(r),int(i))]=(k,-1)
tree=set(range(384))-set(chords);parents={0:None};todo=deque([0])
while todo:
    q=todo.popleft()
    for i in range(3):
        k,s=direct[(q,i)];r=int(right[q,i])
        if k in tree and r not in parents:parents[r]=(q,k,s);todo.append(r)
assert len(parents)==256
paths=np.zeros((384,256),dtype=np.int64)
for q in range(1,256):
    r=q
    while r:
        p,k,s=parents[r];paths[k,q]+=s;r=p
cycles=np.zeros((384,129),dtype=np.int64)
for j,k in enumerate(chords):
    q,r,i=map(int,edges[k]);cycles[:,j]=paths[:,q]-paths[:,r];cycles[k,j]+=1
assert np.array_equal(cycles[chords],np.eye(129,dtype=np.int64))
boundary=np.zeros((256,384),dtype=np.int64)
for k,(q,r,i)in enumerate(edges):boundary[q,k]=-1;boundary[r,k]=1
assert not np.any(boundary@cycles)
words=(((0,1,0),(0,),(2,)),((2,),(1,),(2,0,2)),((1,),(1,0,1),(1,0,2,0,1)))
chains=[];matrices=[]
for perm,images in zip(autos,words):
    T=np.zeros((384,384),dtype=np.int64)
    for k,(q,r,i)in enumerate(edges):
        v=int(perm[q])
        for letter in images[i]:
            j,s=direct[(v,letter)];T[j,k]+=s;v=int(right[v,letter])
        assert v==perm[r]
    image=T@cycles;M=image[chords]
    assert np.array_equal(cycles@M,image);chains.append(T);matrices.append(M)
A,B,C=matrices;I=np.eye(129,dtype=np.int64)
assert np.array_equal(A@B@A,B@A@B)
assert np.array_equal(B@C@B,C@B@C)
assert np.array_equal(A@C,C@A)
abc=A@B@C;assert np.array_equal(abc@abc@abc@abc,I)
u_num=-np.sum(paths,axis=1)
expected=-np.ones(256,dtype=np.int64);expected[0]+=256
assert np.array_equal(boundary@u_num,expected)
rnum=[]
for T,M in zip(chains,matrices):
    r=u_num-T@u_num;assert not np.any(boundary@r)
    v=r[chords];assert np.array_equal(cycles@v,r);rnum.append(v)
affine=[(r,M)for r,M in zip(rnum,matrices)]
def am(g,h):return(g[0]+g[1]@h[0],g[1]@h[1])
def ap(*gg):
    g=(np.zeros(129,dtype=np.int64),I)
    for h in gg:g=am(g,h)
    return g
def ae(g,h):return np.array_equal(g[0],h[0])and np.array_equal(g[1],h[1])
assert ae(ap(affine[0],affine[1],affine[0]),ap(affine[1],affine[0],affine[1]))
assert ae(ap(affine[1],affine[2],affine[1]),ap(affine[2],affine[1],affine[2]))
assert ae(ap(affine[0],affine[2]),ap(affine[2],affine[0]))
assert ae(ap(*(affine*4)),(np.zeros(129,dtype=np.int64),I))

#64 actual integral cusp cycles; their sum is the single oriented relation.
w=(1,0,2)
def end(q,word):
    for i in word:q=int(right[q,i])
    return q
remaining=set(range(256));cusp=[]
while remaining:
    q=min(remaining);orb={end(q,w*i)for i in range(4)};assert len(orb)==4;remaining-=orb
    v=q;chain=np.zeros(384,dtype=np.int64)
    for i in w*4:
        k,s=direct[(v,i)];chain[k]+=s;v=int(right[v,i])
    assert v==q;cusp.append(chain[chords])
Cusp=np.array(cusp,dtype=np.int64).T;assert Cusp.shape==(129,64)
assert not np.any(np.sum(Cusp,axis=1))
lookup={tuple(Cusp[:,i]):i for i in range(64)};assert len(lookup)==64
cusp_perms=[]
for M in matrices:
    p=[lookup[tuple(M@Cusp[:,i])]for i in range(64)];assert len(set(p))==64;cusp_perms.append(p)

def mod3_pivcols(M):
    R=M.copy()%3;r=0;out=[]
    for j in range(R.shape[1]):
        ix=np.flatnonzero(R[r:,j])
        if not len(ix):continue
        k=r+int(ix[0]);R[[r,k]]=R[[k,r]]
        if R[r,j]==2:R[r]=2*R[r]%3
        ii=np.flatnonzero(R[:,j]);ii=ii[ii!=r]
        R[ii]=(R[ii]-R[ii,j,None]*R[r])%3
        out.append(j);r+=1
        if r==R.shape[0]:break
    return out
assert len(mod3_pivcols(Cusp[:,:63]))==63
candidate=np.concatenate((Cusp[:,:63],I),axis=1)
piv=mod3_pivcols(candidate);assert len(piv)==129 and piv[:63]==list(range(63))
T=candidate[:,piv]
assert len(mod3_pivcols(T))==129
np.savez_compressed(ROOT/'ferrari_rank129_integral.npz',A=A,B=B,C=C,
                    translation_numerators=np.stack(rnum),translation_denominator=np.array(256),
                    cycles=cycles,chainmaps=np.stack(chains),edge_gauge_numerator=u_num,
                    cusp_cycles=Cusp,boundary_adapted_basis=T,
                    cusp_permutations=np.array(cusp_perms,dtype=np.int16))
print(json.dumps({'coefficient_ring':'Z forchain/linear data; Z[1/256] foraffine translations',
 'exact_integral_braid_and_full_twist_relators_verified':True,
 'exact_affine_relators_verified_over_Z_1_over256':True,
 'all_chain_cycle_identities_verified_over_Z':True,
 'affine_translation_denominator':256,
 'cusp_count':64,'boundary_rank':63,
 'oriented_sum_of_all_cusp_cycles_is_zero_over_Z':True,
 'each_generator_permutes_the64_integral_cusp_cycles':True,
 'first63_cusp_vectors_independent_mod3':True,
 'boundary_adapted_basis_invertible_over_Z3':True,
 'max_absolute_generator_matrix_entry':max(int(np.max(np.abs(M)))for M in matrices),
 'max_absolute_translation_numerator':max(int(np.max(np.abs(v)))for v in rnum),
 'scope':'Exact integer graph computation; the boundary basis is built from integral cusp loops and a3-adicunit complement.'},indent=2))
