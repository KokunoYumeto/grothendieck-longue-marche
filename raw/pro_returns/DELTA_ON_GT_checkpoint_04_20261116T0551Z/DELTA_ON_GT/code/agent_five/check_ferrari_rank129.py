"""Literal rank129 homology action after the characteristic two-cover of C'.

C=C2*C2*C2; D=C''(C')^2, so C/D has order256 and D is free rank129.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
from collections import deque
import json
import numpy as np

ROOT=Path(__file__).resolve().parent

# C/D is the mod2 path-chain extension of the three-cube.
# There are twelve unoriented cube edges; signs disappear in characteristic2.
edge_labels=[(i,q)for i in range(3)for q in range(8)if not(q&(1<<i))]
ei={e:j for j,e in enumerate(edge_labels)}
perms=[]
for a in range(8):
    perms.append([ei[(i,(q^a)&~(1<<i))]for i,q in edge_labels])
act2=[]
for a in range(8):
    table=[0]*4096
    for v in range(1,4096):
        low=v&-v;j=low.bit_length()-1
        table[v]=table[v^low]^(1<<perms[a][j])
    act2.append(table)
one=(0,0)
t=tuple((1<<ei[(i,0)],1<<i)for i in range(3))
def mul(g,h):return(g[0]^act2[g[1]][h[0]],g[1]^h[1])
def inv(g):return(act2[g[1]][g[0]],g[1])
def prod(*gg):
    g=one
    for h in gg:g=mul(g,h)
    return g
assert all(mul(g,g)==one for g in t)
Q=[one];idx={one:0};parents=[None];pos=0
while pos<len(Q):
    q=Q[pos];pos+=1
    for i,g in enumerate(t):
        h=mul(q,g)
        if h not in idx:idx[h]=len(Q);Q.append(h);parents.append((pos-1,i))
assert len(Q)==256
qgens=[idx[g]for g in t]
right=np.array([[idx[mul(q,g)]for g in t]for q in Q],dtype=np.int16)

# Exact word actions a,b,c on the three involutions, in zero-based letters.
words_a=((0,1,0),(0,),(2,))
words_b=((2,),(1,),(2,0,2))
words_c=((1,),(1,0,1),(1,0,2,0,1))
def qword(w):return prod(*(t[i]for i in w))
def auto(images):
    vals=[one]
    for p,i in parents[1:]:vals.append(mul(vals[p],images[i]))
    assert len(set(vals))==256
    for q,k in enumerate(vals):
        for i,g in enumerate(t):assert vals[int(right[q,i])]==mul(k,images[i])
    return np.array([idx[g]for g in vals],dtype=np.int16)
autos=[auto([qword(w)for w in words])for words in (words_a,words_b,words_c)]
qa,qb,qc=autos
assert np.array_equal(qa[qb[qa]],qb[qa[qb]])
assert np.array_equal(qb[qc[qb]],qc[qb[qc]])
assert np.array_equal(qa[qc],qc[qa])
qd=qa[qb[qc]]
assert np.array_equal(qd[qd[qd[qd]]],np.arange(256))

# The Schreier graph has256 vertices and384 unoriented edges.
edges=[];direct={}
for q in range(256):
    for i in range(3):
        r=int(right[q,i])
        if q<r:
            k=len(edges);edges.append((q,r,i))
            direct[(q,i)]=(k,1);direct[(r,i)]=(k,-1)
assert len(edges)==384
tree=set();tree_parent=[None]*256;seen={0};todo=deque([0])
while todo:
    q=todo.popleft()
    for i in range(3):
        r=int(right[q,i]);k,sgn=direct[(q,i)]
        if r not in seen:
            seen.add(r);tree.add(k);tree_parent[r]=(q,k,sgn);todo.append(r)
assert len(tree)==255
chords=[i for i in range(384)if i not in tree]
assert len(chords)==129
paths=np.zeros((384,256),dtype=np.int16)
for q in range(1,256):
    # parent indices need not increase in this separate BFS.
    r=q
    while r:
        p,k,s=tree_parent[r];paths[k,q]+=s;r=p
cycles=np.zeros((384,129),dtype=np.int16)
for j,k in enumerate(chords):
    q,r,i=edges[k];cycles[:,j]=paths[:,q]-paths[:,r];cycles[k,j]+=1
cycles%=3
assert np.array_equal(cycles[chords],np.eye(129,dtype=np.int16))
boundary=np.zeros((256,384),dtype=np.int16)
for k,(q,r,i)in enumerate(edges):boundary[q,k]=-1;boundary[r,k]=1
boundary%=3
assert not np.any(boundary@cycles%3)

matrices=[];chainmaps=[]
for vertex_auto,words in zip(autos,(words_a,words_b,words_c)):
    chain=np.zeros((384,384),dtype=np.int16)
    for k,(q,r,i)in enumerate(edges):
        v=int(vertex_auto[q])
        for letter in words[i]:
            e,s=direct[(v,letter)];chain[e,k]+=s;v=int(right[v,letter])
        assert v==int(vertex_auto[r])
    chain%=3
    image=chain@cycles%3
    assert not np.any(boundary@image%3)
    M=image[chords]
    assert np.array_equal(cycles@M%3,image)
    matrices.append(M)
    chainmaps.append(chain)
A,B,C=matrices;Id=np.eye(129,dtype=np.int16)
def mm(A,B):return A@B%3
def mp(*gg):
    M=Id
    for g in gg:M=mm(M,g)
    return M
def power(M,n):
    ans=Id
    while n:
        if n&1:ans=mm(ans,M)
        M=mm(M,M);n//=2
    return ans
def inverse(M):
    rows=np.concatenate((M.copy(),Id),axis=1)
    for j in range(129):
        k=j+int(np.flatnonzero(rows[j:,j])[0]);rows[[j,k]]=rows[[k,j]]
        if rows[j,j]==2:rows[j]=2*rows[j]%3
        kk=np.flatnonzero(rows[:,j]);kk=kk[kk!=j]
        rows[kk]=(rows[kk]-rows[kk,j,None]*rows[j])%3
    assert np.array_equal(rows[:,:129],Id)
    return rows[:,129:]
assert np.array_equal(mp(A,B,A),mp(B,A,B))
assert np.array_equal(mp(B,C,B),mp(C,B,C))
assert np.array_equal(mm(A,C),mm(C,A))
assert np.array_equal(power(mp(A,B,C),4),Id)
Ai,Bi,Ci=[inverse(M)for M in matrices]
assert all(np.array_equal(mm(M,Mi),Id)for M,Mi in zip(matrices,(Ai,Bi,Ci)))
X=np.stack((power(A,2),power(B,2),power(C,2),power(mp(A,B,A),2),power(mp(C,B,C),2)))
# A canonical Schur--Zassenhaus gauge from the mean of all rooted paths.
# 256=1 inF3; d(u)=e_identity-mean(vertices).
u=(-np.sum(paths,axis=1))%3
expected=(-np.ones(256,dtype=np.int16))%3;expected[0]=(expected[0]+1)%3
assert np.array_equal(boundary@u%3,expected)
translations=[]
for chain,M in zip(chainmaps,matrices):
    r=(u-chain@u)%3;assert not np.any(boundary@r%3)
    v=r[chords];assert np.array_equal(cycles@v%3,r);translations.append(v)
def affine_mul(g,h):return((g[0]+g[1]@h[0])%3,mm(g[1],h[1]))
affine_identity=(np.zeros(129,dtype=np.int16),Id)
def affine_prod(*gg):
    out=affine_identity
    for g in gg:out=affine_mul(out,g)
    return out
def affine_power(g,k):
    out=affine_identity
    while k:
        if k&1:out=affine_mul(out,g)
        g=affine_mul(g,g);k//=2
    return out
def affine_equal(g,h):return np.array_equal(g[0],h[0])and np.array_equal(g[1],h[1])
ag=list(zip(translations,matrices))
assert affine_equal(affine_prod(ag[0],ag[1],ag[0]),affine_prod(ag[1],ag[0],ag[1]))
assert affine_equal(affine_prod(ag[1],ag[2],ag[1]),affine_prod(ag[2],ag[1],ag[2]))
assert affine_equal(affine_prod(ag[0],ag[2]),affine_prod(ag[2],ag[0]))
assert affine_equal(affine_power(affine_prod(*ag),4),affine_identity)
ax=[affine_power(ag[0],2),affine_power(ag[1],2),affine_power(ag[2],2),affine_power(affine_prod(ag[0],ag[1],ag[0]),2),affine_power(affine_prod(ag[2],ag[1],ag[2]),2)]
affine_orders=[]
for g in ax:
    h=affine_identity
    for k in range(1,129):
        h=affine_mul(h,g)
        if affine_equal(h,affine_identity):break
    else:k=None
    affine_orders.append(k)
linear_orders=[]
for x in X:
    value=Id
    for n in range(1,257):
        value=mm(value,x)
        if np.array_equal(value,Id):break
    else:n=None
    linear_orders.append(n)

np.savez_compressed(ROOT/'ferrari_rank129.npz',A=A,B=B,C=C,Ai=Ai,Bi=Bi,Ci=Ci,X=X,
                    Q=np.array(Q,dtype=np.int16),right=right,edges=np.array(edges,dtype=np.int16),
                    cycles=cycles,chords=np.array(chords,dtype=np.int16),vertex_actions=np.stack(autos))
np.savez_compressed(ROOT/'ferrari_rank129_affine.npz',A=A,B=B,C=C,
                    generator_translations=np.stack(translations),X=X,
                    Xi_translations=np.stack([g[0]for g in ax]),
                    edge_gauge=u,chainmaps=np.stack(chainmaps))
out={'base_group_order':len(Q),'graph_vertices':256,'graph_edges':384,
     'kernel_free_rank':129,'homology_characteristic':3,
     'exact_word_action_on_every_base_element_verified':True,
     'all_graph_cycles_and_chain_maps_verified':True,
     'all_braid_and_full_twist_relators_verified_on_homology':True,
     'Xi_matrix_orders':linear_orders,
     'affine_Xi_orders':affine_orders,
     'all_L_relators_verified_in_the_actual_affine_extension':True,
     'source':'C=C2*C2*C2, D=C_second_derived*C_prime_squared; literal a,b,c action on H1(D,F3)',
     'scope':'Actual finite linear L quotient. No stability under a gentle pair or GT lifting is presumed.'}
print(json.dumps(out,indent=2))
