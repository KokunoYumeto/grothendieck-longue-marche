#!/usr/bin/env python3
"""Adjoin all five parity coordinates before the F3 homology extension.

The new finite base is C2^5 x SL2(F3), of order 768. Its F3 cellular
complex splits into the 32 C2^5 character blocks, each with 120 edges
and 144 relation vectors. This is an exact decomposition of an actual
finite quotient, not a graded substitution.
"""
import test_fivepoint_cm_level as T
from pathlib import Path
import numpy as np
from collections import Counter
import json

I=(1,0,0,1)
def mul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%3
                 for i in range(2) for j in range(2))
def inv(a):return (a[3],-a[1]%3,-a[2]%3,a[0])
gens=[tuple(v%3 for v in g) for g in T.C.gens]
Q=[I];idx={I:0}
for q in Q:
    for g in gens:
        h=mul(q,g)
        if h not in idx:idx[h]=len(Q);Q.append(h)
assert len(Q)==24
tab=np.array([[idx[mul(a,b)] for b in Q] for a in Q],dtype=np.int16)
ig=[idx[g] for g in gens];inverses=[idx[inv(q)] for q in Q]
def parity(w):
    a=0
    for j in w:a^=1<<(abs(j)-1)
    return a
# The 768 base elements are all present, verified by an actual BFS.
base=[(0,0)];seen={base[0]}
for a,q in base:
    for j,g in enumerate(ig):
        h=(a^(1<<j),int(tab[q,g]))
        if h not in seen:seen.add(h);base.append(h)
assert len(base)==768
assert all(sum(1 if j==k else -1 if j==-k else 0 for j in w)%2==0
           for w in T.jloops for k in (1,2))
assert all(parity(T.subst(w,pair))==0 for w in T.jloops for pair in T.pairwords)
print("PASS refined base C2^5 x SL2(F3), order 768; same rank-289 joint source",flush=True)

def chain(start,w,character):
    a,q=start;v=np.zeros(120,dtype=np.int16)
    for j in w:
        k=abs(j)-1
        if j>0:
            sign=-1 if (a&character).bit_count()%2 else 1
            v[5*q+k]+=sign
            a^=1<<k;q=int(tab[q,ig[k]])
        else:
            a^=1<<k;q=int(tab[q,inverses[ig[k]]])
            sign=-1 if (a&character).bit_count()%2 else 1
            v[5*q+k]-=sign
    return (a,q),v
projections={};dimensions={};ranks={}
for ch in range(32):
    rows=[]
    for q in range(24):
        for rel in T.C.relations:
            end,v=chain((0,q),rel,ch);assert end==(0,q);rows.append(v)
    basis,P=T.row_space_projection(rows,3);projections[ch]=P
    boundary=np.zeros((120,24),dtype=np.int16)
    for q in range(24):
        for j,g in enumerate(ig):
            boundary[5*q+j,q]-=1
            boundary[5*q+j,int(tab[q,g])]+=(-1 if ch&(1<<j) else 1)
    rb,_=T.row_space_projection(boundary,3)
    assert np.all(np.array(rows,dtype=np.int16)@boundary%3==0)
    ranks[ch]=len(basis)
    dimensions[ch]=120-len(basis)-len(rb)
print("Exact 32 character-block H1 dimensions:",dimensions,flush=True)
print("Total H1 dimension:",sum(dimensions.values()),flush=True)

loopcache={}
def loops_at(ch,i,start):
    key=(ch,i,start)
    if key not in loopcache:
        rows=[]
        for w in T.mappedloops[i]:
            end,v=chain(start,w,ch);assert end==start;rows.append(v)
        loopcache[key]=np.array(rows,dtype=np.int16)
    return loopcache[key]
def expression_matrix(base,tokens):
    As=[];bs=[]
    for ch in range(32):
        current=(0,0);linear=np.zeros((T.nv,120),dtype=np.int32)
        constant=np.zeros(120,dtype=np.int32)
        for token in tokens:
            if isinstance(token,tuple):
                current,v=chain(current,token,ch);constant+=v;continue
            i=abs(token)-1;w=T.subst(T.jpaths[base],T.pairwords[i])
            if token>0:
                linear+=loops_at(ch,i,current)
                current,v=chain(current,w,ch);constant+=v
            else:
                current,v=chain(current,T.inverse(w),ch);constant+=v
                linear-=loops_at(ch,i,current)
        if current!=(0,0):return None
        P=projections[ch]
        As.append((linear@P).T%3);bs.append(-constant@P%3)
    return np.vstack(As),np.concatenate(bs)

records=[];base_records=[]
for base in sorted(T.derived):
    qf=T.Q[T.JQ[base][4]]
    fs=[fr for fr in T.frames if fr["qf"]==qf]
    if not fs:continue
    results={}
    valid=True
    for p in (2,3):
        As=[];bs0=[]
        for name,tokens in T.expressions.items():
            result=(T.expression_matrix(base,tokens,2) if p==2
                    else expression_matrix(base,tokens))
            if result is None:valid=False;break
            A,b=result;As.append(A);bs0.append(b)
        if not valid:break
        abbase=T.abelian_base_coordinates(base)
        As.append(T.abloops%p);bs0.append(-abbase%p)
        firstA,_=T.frame_equations(base,fs[0],p)
        As.append(firstA);A=np.vstack(As);fixed_rhs=np.concatenate(bs0)
        Bs=[]
        for fr in fs:
            Af,bf=T.frame_equations(base,fr,p);assert np.array_equal(Af,firstA)
            Bs.append(np.concatenate((fixed_rhs,bf)))
        rank,good=T.solve_many(A,np.stack(Bs,axis=1),p)
        results[p]={"rank":rank,"good":good.tolist(),"rows":len(A)}
    if not valid:continue
    base_records.append({"base":base,"word":T.jpaths[base],
        "ranks":{str(p):results[p]["rank"] for p in (2,3)},
        "rows":{str(p):results[p]["rows"] for p in (2,3)}})
    for j,fr in enumerate(fs):
        if all(results[p]["good"][j] for p in (2,3)):
            rec=dict(fr);rec["base"]=base
            rec["free_dimensions"]={str(p):T.nv-results[p]["rank"] for p in (2,3)}
            records.append(rec)
    print("Refined base",base,"ranks",[results[p]["rank"] for p in (2,3)],
          "surviving",sum(all(results[p]["good"][j] for p in (2,3))
                          for j in range(len(fs))),flush=True)
hist=Counter(r["parity"] for r in records)
print("Refined complete framed finite census:",dict(hist),flush=True)
out={"scope":"Actual finite homology quotient and all necessary framed finite shadows; no global lifting assertion.",
 "refined_base_order":768,"character_H1_dimensions":dimensions,
 "refined_H1_dimension":sum(dimensions.values()),
 "target":"joint old mod-2 homology quotient and refined mod-3 homology quotient",
 "source_order":"288*6^289","base_records":base_records,
 "surviving_residues":records,"parity_counts":dict(hist)}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
