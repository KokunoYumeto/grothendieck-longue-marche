#!/usr/bin/env python3
"""All630 actual quartet/partition characters of pure sphere10 abelianization.

The weights are fixed by the independently enumerated cap216 map:
the three pure4 peripheral classes have C4 values1,2,1.  The distinguished
partition has value2 on its two opposite edges and1 on the other four.
This program checks the complete support census, sphere relations,
binary spanning and every label-generator transition.
"""
from itertools import combinations
from pathlib import Path
import json
import numpy as np

n=10
edges=list(combinations(range(n),2));ei={e:i for i,e in enumerate(edges)}
stars=np.array([[int(i in e) for e in edges] for i in range(n)],dtype=np.int64)
total=np.ones((1,len(edges)),dtype=np.int64)
relations=np.vstack((stars,total))
objects=[];characters=[]
for S in combinations(range(n),4):
    a,b,c,d=S
    for partition in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))):
        partition=tuple(sorted(tuple(sorted(e)) for e in partition))
        row=np.zeros(45,dtype=np.int64)
        for e in combinations(S,2):row[ei[e]]=2 if e in partition else 1
        assert np.all((relations@row)%4==0)
        assert set(np.flatnonzero(row))=={ei[e] for e in combinations(S,2)}
        assert sum(row==2)==2 and sum(row==1)==4
        objects.append((S,partition));characters.append(row)
characters=np.array(characters,dtype=np.int64)
assert len(objects)==630 and len(set(objects))==630
keys={tuple(v) for v in characters};negative={tuple((-v)%4) for v in characters}
assert len(keys)==630 and len(negative)==630 and not (keys&negative)

def binary_basis(rows):
    basis={};chosen=[]
    for i,vector in enumerate(rows):
        row=sum((int(v)&1)<<j for j,v in enumerate(vector))
        while row:
            p=row.bit_length()-1
            if p in basis:row^=basis[p]
            else:basis[p]=row;chosen.append(i);break
    return chosen

selected=binary_basis(characters)
assert len(selected)==35
assert len(binary_basis(relations))==10
index={o:i for i,o in enumerate(objects)}
actions=[]
for j in range(9):
    p=list(range(10));p[j],p[j+1]=p[j+1],p[j]
    action=[]
    for i,(S,partition) in enumerate(objects):
        target=(tuple(sorted(p[a] for a in S)),
                tuple(sorted(tuple(sorted(p[a] for a in edge)) for edge in partition)))
        k=index[target];action.append(k)
        moved=np.zeros(45,dtype=np.int64)
        for edge,value in zip(edges,characters[i]):
            moved[ei[tuple(sorted(p[a] for a in edge))]]=value
        assert np.array_equal(moved,characters[k])
    assert sorted(action)==list(range(630))
    actions.append(action)

# A unit35-minor modulo4 proves spanning of the full free C4 dual,
# after the35-dimensional binary quotient calculation.
A=characters[selected].copy()%4
pivots=[];r=0
for j in range(45):
    choices=[i for i in range(r,35) if A[i,j]%2]
    if not choices:continue
    k=choices[0];A[[r,k]]=A[[k,r]]
    A[r]=A[r]*int(A[r,j])%4
    for i in range(35):
        if i!=r:A[i]=(A[i]-A[i,j]*A[r])%4
    pivots.append(j);r+=1
    if r==35:break
assert r==35 and np.array_equal(A[:,pivots],np.eye(35,dtype=int))

out={'scope':'Exact actual pure4 character supports; the full joint-image and centralizer comparison require the accompanying proof.',
     'edges':edges,'objects':objects,'characters_mod4':characters.tolist(),
     'distinct_F9_character_pairs':630,'binary_rank':35,'relation_rank_mod2':10,
     'selected_character_rows':selected,'unit_minor_columns':pivots,
     'unit_reduced_rows':A.tolist(),'adjacent_label_actions':actions}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),characters=characters,
                    relations=relations,unit_reduced_rows=A)
print('PASS all630 quartet/partition characters satisfy every sphere relation modulo4.')
print('PASS all630 F9 character pairs are distinct, including every inverse comparison.')
print('PASS binary rank35 and explicit unit35-minor modulo4: full pure abelian quotient retained.')
print('PASS all5670 adjacent label-generator transitions on the actual character supports.')
