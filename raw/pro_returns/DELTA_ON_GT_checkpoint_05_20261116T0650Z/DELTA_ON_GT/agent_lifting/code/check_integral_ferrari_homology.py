"""Exact integral H1(C') matrices from the eight-vertex cube cover.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
No reduction modulo three is used to infer an all-prime identity.
"""
from pathlib import Path
import json
import sympy as sy

sections={v:tuple(i for i in range(3)if v&(1<<i))for v in range(8)}
tree=set()
for word in sections.values():
    v=0
    for i in word:
        w=v^(1<<i);tree.add((min(v,w),max(v,w)));v=w
edges=sorted({(min(v,v^(1<<i)),max(v,v^(1<<i)))for v in range(8)for i in range(3)})
chords=[e for e in edges if e not in tree]
assert len(tree)==7 and len(chords)==5
idx={e:i for i,e in enumerate(chords)}
basis=[]
for v,w in chords:
    i=(v^w).bit_length()-1
    basis.append(sections[v]+(i,)+tuple(reversed(sections[w])))
def abelianize(word):
    v=0;out=[0]*5
    for i in word:
        w=v^(1<<i);edge=(min(v,w),max(v,w))
        if edge in idx:out[idx[edge]]+=1 if v<w else -1
        v=w
    assert v==0
    return out
assert [abelianize(w)for w in basis]==[[int(i==j)for i in range(5)]for j in range(5)]
def substitute(word,images):return tuple(x for i in word for x in images[i])
def matrix(images):return sy.Matrix.hstack(*(sy.Matrix(abelianize(substitute(w,images)))for w in basis))
ai=((0,1,0),(0,),(2,));bi=((2,),(1,),(2,0,2))
xi1=(1,0);xi2=(2,0)
ci=tuple(xi1+w+tuple(reversed(xi1))for w in ai)
A=matrix(ai);B=matrix(bi);C=matrix(ci);I=sy.eye(5)
assert A*B*A==B*A*B and B*C*B==C*B*C and A*C==C*A
assert (A*B*C)**4==I
def inner(word):return matrix(tuple(word+(i,)+tuple(reversed(word))for i in range(3)))
T1=inner(xi1);T2=inner(xi2)
assert T1*T2==T2*T1 and T1*T1==T2*T2==I
E4=I+T1+T2+T1*T2
assert E4*E4==4*E4 and E4.rank()==2
assert all(M*E4==E4*M for M in(A,B,C))
X=[A*A,B*B,C*C,(A*B*A)**2,(C*B*C)**2]
assert all((M-I)*(4*I-E4)==sy.zeros(5)for M in X)
assert all((M-I)**2*E4==sy.zeros(5)for M in X[:3])
assert all((M+I)*E4==sy.zeros(5)for M in X[3:])
z3=(A*B)**3
assert z3*(4*I-E4)==4*I-E4 and z3*E4==-E4

def flat(M):return [int(x)for x in list(M)]
out={'cube_vertices':8,'cube_edges':12,'tree_edges':sorted(tree),'non_tree_edges':chords,
     'free_rank':5,'free_basis_in_involutions':basis,
     'a_integer_matrix_5x5':flat(A),'b_integer_matrix_5x5':flat(B),'c_integer_matrix_5x5':flat(C),
     'four_times_compact_projector':flat(E4),'compact_projector_rank':2,
     'all_Xi_boundary_action_identity_over_Z_one_half':True,
     'first_three_Xi_compact_square_zero_unipotent':True,
     'last_two_Xi_compact_negative_identity':True,
     'central_z3_boundary_identity_compact_negative_identity':True,
     'scope':'Exact integral identities imply the stated linear orders at every odd prime. The compact projector only uses division by4.'}
dest=Path(__file__).resolve().parents[1]/'records'/'integral_ferrari_homology.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
