#!/usr/bin/env python3
"""Exact finite-field rank certificates for the C.7c homogeneous derivation lemma."""
from itertools import product
from pathlib import Path
import json

def derivation_column(word,r,weights,mod):
    out={}
    for k,i in enumerate(word):
        for j in range(r):
            if i==j:continue
            c=weights[i][j]%mod
            for pair,sign in (((j,i),1),((i,j),-1)):
                z=word[:k]+pair+word[k+1:]
                val=(out.get(z,0)+sign*c)%mod
                if val:out[z]=val
                elif z in out:del out[z]
    return out

def rank_columns(columns,mod):
    pivots={}
    for vec in columns:
        v=dict(vec)
        while v:
            lead=min(v)
            if lead not in pivots:
                q=pow(v[lead],-1,mod)
                pivots[lead]={k:(c*q)%mod for k,c in v.items()}
                break
            c=v[lead]
            for k,d in pivots[lead].items():
                val=(v.get(k,0)-c*d)%mod
                if val:v[k]=val
                elif k in v:del v[k]
    return len(pivots)

cases=[]
for p,n,degs in [(2,1,range(1,8)),(2,2,range(1,5)),(2,3,range(1,4)),(3,2,range(1,4)),(5,1,range(1,4))]:
    r=p**n
    weights=[]
    for i in range(r):
        row=[]
        for j in range(r):
            if i==j:row.append(0);continue
            z=abs(i-j);v=1
            while z%p==0:z//=p;v*=p
            row.append(v)
        weights.append(row)
    for d in degs:
        cols=[derivation_column(w,r,weights,101) for w in product(range(r),repeat=d)]
        total={}
        for v in cols:
            for k,c in v.items():total[k]=(total.get(k,0)+c)%101
        assert not any(total.values()) # D(S^d)=0
        rank=rank_columns(cols,101)
        assert rank==r**d-1,(p,n,d,rank)
        cases.append({'p':p,'n':n,'variables':r,'degree':d,'domain_dimension':r**d,'rank_mod101':rank,'kernel_dimension':1})
# Any nonzero reduction determinant certifies the same lower bound over Q.
out={'checks':[{'name':'Ultrametric first derivations have only the S-power kernel in the tested homogeneous degrees','passed':True,'cases':cases}], 'passed':1,'scope':'Exact modulo101 ranks give rational rank certificates for these finite cases. The general proof is the block-length tensor argument in C.7c.'}
path=Path(__file__).with_name('BC_local_derivation_checks_output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
