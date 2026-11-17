#!/usr/bin/env python3
"""Retain exact integral Γ(3) words for every ordered branch assignment."""
from pathlib import Path
from itertools import permutations
import json
HERE=Path(__file__).resolve().parent
I=((1,0),(0,1));U=((1,3),(0,1));L=((1,0),(3,1))
def mul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def act(A,v):return tuple(sum(A[i][j]*v[j] for j in range(2))%2 for i in range(2))
words=[(),('U',),('L',),('U','L'),('L','U'),('U','L','U')]
vectors=((1,0),(0,1),(1,1))
matrices=[]
for word in words:
    A=I
    for letter in word:A=mul(A,{'U':U,'L':L}[letter])
    assert A[0][0]*A[1][1]-A[0][1]*A[1][0]==1
    assert all((A[i][j]-I[i][j])%3==0 for i in range(2) for j in range(2))
    matrices.append({'word':list(word),'matrix':A,'permutation':[vectors.index(act(A,v)) for v in vectors]})
assert len({tuple(x['permutation']) for x in matrices})==6
records=[]
for n in range(9,13):
    length=n-9
    reference=vectors[:length]
    witnesses=[]
    for target in permutations(vectors,length):
        row=next(x for x in matrices if tuple(act(x['matrix'],v) for v in reference)==target)
        witnesses.append({'target':target,'word':row['word'],'matrix':row['matrix']})
    assert len(witnesses)==[1,3,6,6][n-9]
    records.append({'n':n,'reference':reference,'witnesses':witnesses})
out={'generators':{'U':U,'L':L},'all_six_integral_words':matrices,'configurations':records,'all_assertions_passed':True}
HERE.joinpath('check_involution_fusion_assignments.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS six determinant-one integral Γ(3) words give all permutations of the three nonzero two-torsion points.')
print('PASS exact positive assignment witnesses for n=9,10,11,12: component counts1,3,6,6.')
