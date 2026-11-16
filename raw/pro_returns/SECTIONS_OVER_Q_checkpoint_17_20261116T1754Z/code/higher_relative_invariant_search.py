#!/usr/bin/env python3
"""The initial finite invariant-space search, retained as actually run."""
import numpy as np
from math import comb
from pathlib import Path

out=[]
for n in range(1,8):
    d=3**(n-1)
    a=np.zeros((d,d),dtype=np.int16)
    for j in range(1,d):
        for k in range(1,min(j+1,d-j)):
            a[j+k,j]=comb(j,k)%3
    row=0
    for col in range(d):
        inds=np.flatnonzero(a[row:,col])
        if len(inds)==0:
            continue
        pivot=row+int(inds[0])
        a[[row,pivot]]=a[[pivot,row]]
        if a[row,col]==2:
            a[row]=a[row]*2%3
        below=np.flatnonzero(a[row+1:,col])+row+1
        if len(below):
            a[below]=(a[below]-a[below,col,None]*a[row])%3
        row+=1
        if row==d:
            break
    out.append({'n':n,'d':d,'invariant_dimension':d-row,
                'exhibited_monomial_powers':[d-3**j for j in range(n)]})
    print(out[-1],flush=True)
Path(__file__).with_name('higher_relative_invariant_search_output.txt').write_text(
    '\n'.join(map(str,out))+'\n')
