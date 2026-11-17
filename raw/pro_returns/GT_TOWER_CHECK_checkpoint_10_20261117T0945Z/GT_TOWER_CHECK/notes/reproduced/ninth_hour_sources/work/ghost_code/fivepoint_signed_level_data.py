#!/usr/bin/env python3
"""Build exact finite input data for an abelian-cover pentagon detector.

This constructs an actual quotient of Gamma_0,5, and its five pentagon
insertion maps, from the faithful four-braid words. It computes no
assertion about survival or exclusion of full GT elements.
"""
from collections import deque
from pathlib import Path
import json
import numpy as np

M=12
I=(1,0,0,1)
def mul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%M
                 for i in range(2) for j in range(2))
def inv(a):return (a[3],-a[1]%M,-a[2]%M,a[0])
U=(1,1,0,1);L=(1,0,11,1)
braid={1:U,2:L,3:U}
def word_eval(w,gs):
    v=I
    for j in w:v=mul(v,gs[j-1] if j>0 else inv(gs[-j-1]))
    return v
def inverse(w):return tuple(-j for j in w[::-1])
def band(i,j):
    front=tuple(range(j-1,i,-1))
    return front+(i,i)+inverse(front)
bands={(i,j):word_eval(band(i,j),(U,L,U))
       for i in range(1,5) for j in range(i+1,5)}
gens=[bands[t] for t in ((1,3),(2,3),(1,4),(2,4),(3,4))]
def comm(u,v):return (-v,-u,v,u)
relations=[]
for left,right in [
 ((1,3,-1),(-5,3,5)),
 ((1,4,-1),comm(3,5)+(4,)+inverse(comm(3,5))),
 ((1,5,-1),comm(3,5)+(5,)),
 ((2,3,-2),(3,)),
 ((2,4,-2),(-5,4,5)),
 ((2,5,-2),comm(4,5)+(5,))]:
    rel=left+inverse(right);relations.append(rel)
    assert word_eval(rel,gens)==I
Q=[I];idx={I:0}
for q in Q:
    for g in gens:
        v=mul(q,g)
        if v not in idx:idx[v]=len(Q);Q.append(v)
print("computed quotient order",len(Q),flush=True)
assert len(Q)==192
print("PASS actual Gamma_0,5 quotient: order",len(Q),flush=True)
print("PASS all six free-by-free defining relators",flush=True)
table=np.array([[idx[mul(a,b)] for b in Q] for a in Q],dtype=np.uint8)
ig=[idx[g] for g in gens]
inverses=[idx[inv(g)] for g in Q]
trans=[[(int(table[q,ig[j]]),1) for j in range(5)] for q in range(len(Q))]
parent={0:None};order=[0];tree=set()
for q in order:
    for j in range(5):
        v=int(table[q,ig[j]])
        if v not in parent:
            parent[v]=(q,j);order.append(v);tree.add((q,j))
assert len(parent)==192 and len(tree)==191
chords=[(q,j) for q in range(len(Q)) for j in range(5) if (q,j) not in tree]
chordidx={e:k for k,e in enumerate(chords)}
assert len(chords)==769
rows=[]
for start in range(len(Q)):
    for rel in relations:
        row=np.zeros(769,dtype=np.int64);q=start
        for j in rel:
            if j>0:
                e=(q,j-1);q=int(table[q,ig[j-1]]);sgn=1
            else:
                q=int(table[q,inverses[ig[-j-1]]]);e=(q,-j-1);sgn=-1
            if e in chordidx:row[chordidx[e]]+=sgn
        assert q==start
        rows.append(row)
matrix=np.array(rows,dtype=np.int64)
def rank_mod(a,p):
    a=(a%p).copy();r=0
    for c in range(a.shape[1]):
        z=np.flatnonzero(a[r:,c])
        if len(z)==0:continue
        v=r+int(z[0]);a[[r,v]]=a[[v,r]]
        a[r]=(a[r]*pow(int(a[r,c]),-1,p))%p
        nonzero=np.flatnonzero(a[r+1:,c])+r+1
        if len(nonzero):
            a[nonzero]=(a[nonzero]-a[nonzero,c,None]*a[r])%p
        r+=1
        if r==a.shape[0]:break
    return r
ranks={str(p):rank_mod(matrix,p) for p in (2,3)}
dims={p:769-r for p,r in ranks.items()}
print("PASS finite-cover cellular boundary:",matrix.shape,"ranks",ranks,flush=True)
print("H1 dimensions over F2,F3:",dims,flush=True)

x12,x13,x23,x24,x34=[bands[k] for k in ((1,2),(1,3),(2,3),(2,4),(3,4))]
pentagon_pairs=[
 (x12,mul(x23,x24)),
 (mul(x13,x23),x34),
 (x23,x34),
 (mul(x12,x13),mul(x24,x34)),
 (x12,x23)]
# Keep both gentle three-cycle substitutions and the swap in the same
# finite source record as the five pentagon substitutions.
x,y=x12,x23;z=inv(mul(x,y))
pairs=pentagon_pairs+[(y,x),(z,x),(y,z)]
X=tuple(idx[a] for a,b in pairs);Y=tuple(idx[b] for a,b in pairs)
joint=[(0,)*len(pairs)];seen={joint[0]:0}
limit=500000
complete=True
for q in joint:
    for g in (X,Y):
        v=tuple(int(table[a,b]) for a,b in zip(q,g))
        if v not in seen:
            if len(joint)>=limit:
                complete=False;break
            seen[v]=len(joint);joint.append(v)
    if not complete:break
print("Joint finite source image:",len(joint),"complete",complete,flush=True)
out={"scope":"Actual finite quotient and finite-cover homology only; no pentagon exclusion assertion.",
     "modulus":M,"quotient_order":len(Q),"generator_matrices":gens,
     "relations":relations,"cover_chords":chords,
     "boundary_shape":list(matrix.shape),"ranks":ranks,"homology_dimensions":dims,
     "pentagon_pairs":pentagon_pairs,"joint_generator_indices":[X,Y],
     "joint_order_or_lower_bound":len(joint),"joint_complete":complete}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
