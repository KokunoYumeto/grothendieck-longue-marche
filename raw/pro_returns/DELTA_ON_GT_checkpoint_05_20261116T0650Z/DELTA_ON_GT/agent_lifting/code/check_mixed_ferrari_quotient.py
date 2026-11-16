"""Explicit faithful affine model for C/(C''C'^3), C=C2*C2*C2.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from collections import deque
from pathlib import Path
import json

MASKS=(3,5,6,7,7)
zero=(0,)*5
one=(zero,0)
def signs(b):return tuple(1 if (b&m).bit_count()%2==0 else 2 for m in MASKS)
def mul(g,h):
    v,b=g;w,c=h;sg=signs(b)
    return (tuple((v[i]+sg[i]*w[i])%3 for i in range(5)),b^c)
def prod(*gg):
    out=one
    for g in gg:out=mul(out,g)
    return out
def inv(g):
    v,b=g;sg=signs(b)
    return (tuple(-sg[i]*v[i]%3 for i in range(5)),b)
t=(one,( (1,0,0,1,0),2),((0,1,1,0,1),4))
t=((zero,1),t[1],t[2])
assert all(mul(g,g)==one for g in t)
G=[one];indices={one:0};parent=[None];todo=0
while todo<len(G):
    g=G[todo]
    for j,h in enumerate(t):
        k=mul(g,h)
        if k not in indices:
            indices[k]=len(G);G.append(k);parent.append((todo,j))
    todo+=1
assert len(G)==1944

aim=(prod(t[0],t[1],t[0]),t[0],t[2])
bim=(t[2],t[1],prod(t[2],t[0],t[2]))
xi1=mul(t[1],t[0])
cim=tuple(prod(xi1,h,inv(xi1))for h in aim)
def automorphism(images):
    vals=[one]
    for j in range(1,len(G)):
        p,k=parent[j];vals.append(mul(vals[p],images[k]))
    assert len(set(vals))==1944
    for i,g in enumerate(G):
        for j,h in enumerate(t):
            assert vals[indices[mul(g,h)]]==mul(vals[i],images[j])
    return {g:vals[i]for i,g in enumerate(G)}
def matrix_from_auto(phi):
    cols=[]
    for j in range(5):
        e=tuple(int(i==j)for i in range(5));v,b=phi[(e,0)]
        assert b==0;cols.append(v)
    T=tuple(cols[j][i]for i in range(5)for j in range(5))
    sigma={b:phi[(zero,b)][1]for b in range(8)}
    u=[]
    for j in range(5):
        b=next(b for b in range(8)if signs(sigma[b])[j]==2)
        u.append(2*phi[(zero,b)][0][j]%3)
    for g in G:
        v,b=g;Tv=tuple(sum(T[5*i+j]*v[j]for j in range(5))%3 for i in range(5))
        sg=signs(sigma[b]);expected=(tuple((Tv[i]+u[i]-sg[i]*u[i])%3 for i in range(5)),sigma[b])
        assert phi[g]==expected
    rows=[list(T[5*i:5*i+5])+[u[i]]for i in range(5)]+[[0,0,0,0,0,1]]
    return tuple(x for row in rows for x in row),sigma
data=[matrix_from_auto(automorphism(im))for im in(aim,bim,cim)]
AA,BB,CC=[z[0]for z in data]
Id=tuple(int(i==j)for i in range(6)for j in range(6))
def mm(a,b):return tuple(sum(a[6*i+k]*b[6*k+j]for k in range(6))%3 for i in range(6)for j in range(6))
def mp(*gg):
    out=Id
    for g in gg:out=mm(out,g)
    return out
def power(a,n):
    out=Id
    for _ in range(n):out=mm(out,a)
    return out
assert mp(AA,BB,AA)==mp(BB,AA,BB)
assert mp(BB,CC,BB)==mp(CC,BB,CC)
assert mm(AA,CC)==mm(CC,AA)
assert power(mp(AA,BB,CC),4)==Id
XX=[power(AA,2),power(BB,2),power(CC,2),power(mp(AA,BB,AA),2),power(mp(CC,BB,CC),2)]
boundary_blocks=[];compact_blocks=[]
for X in XX:
    assert all(X[6*i+j]==int(i==j) for i in range(3)for j in range(3))
    assert all(X[6*i+j]==0 for i in range(3)for j in(3,4))
    assert all(X[6*i+j]==0 for i in(3,4)for j in range(3))
    boundary_blocks.append([X[6*i+5]for i in range(3)])
    compact_blocks.append([X[6*i+j]for i in(3,4,5)for j in(3,4,5)])
out={'C_quotient_order':1944,'C_abelian_quotient_order':8,'C_prime_homology_dimension':5,
     'character_masks':MASKS,'involution_generators':t,
     'a_matrix_6x6':AA,'b_matrix_6x6':BB,'c_matrix_6x6':CC,
     'base_V_actions':[z[1]for z in data],
     'all_relators_of_L_hold':True,
     'boundary_translation_parts_of_Xi':boundary_blocks,
     'all_Xi_boundary_linear_parts_are_one':True,
     'compact_affine_3x3_parts_of_Xi':compact_blocks,
     'scope':'Faithful affine model of C/(C_second_derived*C_prime^3); a,b,c act by the exact Ferrari conjugations. The three-dimensional boundary block is abelian on all five pure Xi, so every commutator-word pentagon factor is trivial there.'}
dest=Path(__file__).resolve().parents[1]/'records'/'mixed_ferrari_quotient.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
