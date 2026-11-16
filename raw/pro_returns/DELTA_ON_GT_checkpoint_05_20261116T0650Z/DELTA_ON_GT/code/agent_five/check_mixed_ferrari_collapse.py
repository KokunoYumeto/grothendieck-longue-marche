"""Exact collapse of the first mixed Ferrari homology test.

Written by GPT-6 Astra, OpenAI, 16 November 2026.
The actual C1944 quotient and its automorphisms are independently constructed
by agent_lifting/code/check_mixed_ferrari_quotient.py.
"""
from pathlib import Path
import json

src=Path(__file__).resolve().parents[1]/'agent_lifting/records/mixed_ferrari_quotient.json'
D=json.loads(src.read_text())
def mm(a,b,n,p=3):
    return tuple(sum(a[n*i+k]*b[n*k+j]for k in range(n))%p
                 for i in range(n)for j in range(n))
def identity(n):return tuple(int(i==j)for i in range(n)for j in range(n))
def prod(gg,n,p=3):
    a=identity(n)
    for g in gg:a=mm(a,g,n,p)
    return a
def inverse(a,n,p=3):
    A=[list(a[n*i:n*i+n])+[int(i==j)for j in range(n)]for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n)if A[k][j]);A[j],A[k]=A[k],A[j]
        u=pow(A[j][j],-1,p);A[j]=[(u*x)%p for x in A[j]]
        for k in range(n):
            if k!=j:
                u=A[k][j];A[k]=[(x-u*y)%p for x,y in zip(A[k],A[j])]
    return tuple(x for row in A for x in row[n:])
def closure(gens,n):
    G=[identity(n)];seen=set(G);pos=0
    while pos<len(G):
        g=G[pos];pos+=1
        for h in gens:
            z=mm(g,h,n)
            if z not in seen:seen.add(z);G.append(z)
    return G
def derived(G,gens,n):
    gi=[inverse(g,n)for g in gens]
    comms=[]
    for h in G:
        hi=inverse(h,n)
        for g,gii in zip(gens,gi):comms.append(prod((h,g,hi,gii),n))
    return closure(list(set(comms)),n)

abc=[tuple(D[k+'_matrix_6x6'])for k in ('a','b','c')]
compact=[tuple(g[6*i+j]for i in (3,4,5)for j in (3,4,5))for g in abc]
linear=[tuple(g[6*i+j]for i in range(5)for j in range(5))for g in abc]
Hab=closure(linear[:2],5)
Hab1=derived(Hab,linear[:2],5)
Hab2=derived(Hab1,Hab1,5)
assert (len(Hab),len(Hab1),len(Hab2))==(144,24,2)
central_braid=prod((linear[0],linear[1])*3,5)
central_expected=tuple((1 if i<3 else 2)if i==j else 0 for i in range(5)for j in range(5))
assert central_braid==central_expected
assert set(Hab2)=={identity(5),central_braid}
T=(1,0,1,0,1,1,0,0,1)
Ti=inverse(T,3)
eta=((1,1,0,0,1,0,0,0,1),
     (1,0,0,2,1,0,0,0,1),
     (1,1,1,0,1,0,0,0,1))
assert tuple(prod((T,g,Ti),3)for g in compact)==eta
assert len(closure(eta,3))==216
words=((0,0),(1,1),(2,2),(0,1,0)*2,(2,1,2)*2)
Xi6=[prod([abc[j]for j in word],6)for word in words]
Xi=[prod([eta[j]for j in word],3)for word in words]
boundary=[]
for X in Xi6:
    assert all(X[6*i+j]==int(i==j)for i in range(3)for j in range(3))
    assert all(X[6*i+j]==0 for i in range(3)for j in (3,4))
    assert all(X[6*i+j]==0 for i in (3,4)for j in range(3))
    boundary.append([X[6*i+5]for i in range(3)])
series=[]
for i,j in ((0,1),(1,2),(2,3),(4,0),(3,4)):
    gens=[Xi[i],Xi[j]];G=closure(gens,3);orders=[len(G)]
    while len(G)>1:
        G=derived(G,gens,3);orders.append(len(G));gens=G
    assert len(orders)<=4
    series.append({'pair':[i+1,j+1],'compact_derived_series':orders})
print(json.dumps({'source_C_quotient_order':1944,
 'rank_five_characters':D['character_masks'],
 'compact_conjugating_translation':[1,1],
 'conjugated_compact_a_b_c':eta,
 'compact_image_order':216,
 'full_ab_linear_derived_series':[144,24,2,1],
 'central_braid_linear_image':central_braid,
 'all_Xi_boundary_linear_parts_are_identity':True,
 'boundary_translation_parts':boundary,
 'pair_series':series,
 'consequence':'Every commutator-word evaluation has trivial boundary block. The complete pentagon condition is precisely that of eta3; adjoining a forgetful q12 factor adds no pentagon condition.',
 'actual_lifting_scope':'The actual LI8 element with f in F third derived and Delta=1 kills every pair image here and in the joint q12 quotient.'},indent=2))
