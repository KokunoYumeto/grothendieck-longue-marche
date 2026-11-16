"""Literal inner-word certificate for faithful affine D-homology coordinates.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
from collections import deque
import numpy as np,json
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129.npz');A=np.load(ROOT/'ferrari_rank129_affine.npz')
edges=F['edges'];right=F['right'];chords=list(map(int,F['chords']));cycles=F['cycles'];tree=set(range(384))-set(chords)
direct={}
for k,(q,r,i)in enumerate(edges):direct[(int(q),int(i))]=(k,1);direct[(int(r),int(i))]=(k,-1)
words={0:()};todo=deque([0])
while todo:
    q=todo.popleft()
    for i in range(3):
        k,_=direct[(q,i)];r=int(right[q,i])
        if k in tree and r not in words:words[r]=words[q]+(i,);todo.append(r)
assert len(words)==256
q,r,i=map(int,edges[chords[0]]);d=words[q]+(i,)+words[r][::-1]
v=0;chain_d=np.zeros(384,dtype=np.int16)
for i in d:
    k,s=direct[(v,i)];chain_d[k]+=s;v=int(right[v,i])
assert v==0;chain_d%=3
e=np.zeros(129,dtype=np.int16);e[0]=1
assert np.array_equal(chain_d,cycles[:,0])
T=np.zeros((384,384),dtype=np.int16)
for k,(q,r,i)in enumerate(edges):
    v=int(q)
    for letter in d+(int(i),)+d[::-1]:
        j,s=direct[(v,letter)];T[j,k]+=s;v=int(right[v,letter])
    assert v==r
T%=3
assert np.array_equal(T@cycles%3,cycles)
u=A['edge_gauge'];translation=(u-T@u)%3
assert np.array_equal(translation,chain_d)
assert np.array_equal(translation[chords],e)
print(json.dumps({'inner_D_word_zero_based_involutions':d,'word_has_identity_image_in_Q256':True,
 'linear_H1_action_is_identity':True,'affine_translation_is_exact_first_homology_basis_vector':True,
 'source_chain_equals_chosen_chord_cycle':True,
 'scope':'Literal conjugated generator words and edge paths; verifies r_inner(d)=[d], not merely nonzero translation.'},indent=2))
