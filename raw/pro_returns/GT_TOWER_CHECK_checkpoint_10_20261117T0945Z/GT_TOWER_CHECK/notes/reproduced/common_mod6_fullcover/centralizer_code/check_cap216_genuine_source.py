#!/usr/bin/env python3
"""Literal source maps for the genuine Delta-one cap216 survivor.

A0 is an auxiliary cubic-frame word.  It is not asserted to be a
gentle pair word.  The normalized pair is supplied by the separate
canonical-cover lifting proof, and has identity retained record.
"""
from pathlib import Path
from itertools import product
from math import gcd, lcm
import json
import numpy as np

HERE=Path(__file__).resolve().parent
data=np.load(HERE.parent/"ghost_code/check_main_mixed_capping.npz")
edges=data["capped_edges"].astype(int)
n=len(edges)
assert n==216
words=[None]*n
words[0]=()
queue=[0]
for a in queue:
    for j in range(2):
        b=int(edges[a,j])
        if words[b] is None:
            words[b]=words[a]+(j,)
            queue.append(b)
assert len(queue)==n
table=np.empty((n,n),dtype=int)
for a in range(n):
    for b,w in enumerate(words):
        c=a
        for j in w:
            c=int(edges[c,j])
        table[a,b]=c
inverse=[int(np.flatnonzero(table[a]==0)[0]) for a in range(n)]
D,V=map(int,edges[0])

def mul(a,b):
    return int(table[a,b])

def power(a,k):
    if k<0:
        return power(inverse[a],-k)
    z=0
    while k:
        if k&1:
            z=mul(z,a)
        a=mul(a,a)
        k>>=1
    return z

def order(a):
    z=a
    k=1
    while z:
        z=mul(z,a)
        k+=1
    return k

def subgroup(gens):
    out=[0]
    seen={0}
    for a in out:
        for b in gens:
            c=mul(a,b)
            if c not in seen:
                seen.add(c)
                out.append(c)
    return sorted(out)

comm=lambda a,b:mul(mul(mul(a,b),inverse[a]),inverse[b])
derived=subgroup([comm(a,b) for a in range(n) for b in (D,V)])
exponent=lcm(*(order(a) for a in range(n)))
assert len(derived)==27 and exponent==12
assert order(D)==12 and order(V)==4

def wi(w):
    return tuple(-a for a in reversed(w))

def wc(a,b):
    return a+b+wi(a)+wi(b)

def substitute(w,images):
    out=()
    for a in w:
        out+=images[abs(a)] if a>0 else wi(images[abs(a)])
    return out

X=(1,)
Y=(2,)
Z=wi(X+Y)
A0=wc(wc(X*4,Y*4),Z*4)*2
id_map={1:X,2:Y}
s_map={1:Y,2:X}
r_map={1:Y,2:Z}
def compose(a,b):
    return {i:substitute(b[i],a) for i in (1,2)}
r2=compose(r_map,r_map)
deck=[id_map,s_map,r_map,r2,compose(s_map,r_map),compose(s_map,r2)]

def evaluate(w,x,y):
    z=0
    for a in w:
        h=x if abs(a)==1 else y
        z=mul(z,h if a>0 else inverse[h])
    return z

def schreier(w,modulus=3):
    # Right transversal (1,x); basis x^2,y,xyx^-1.
    state=0
    count=[0,0,0]
    for a in w:
        if a==1:
            if state:
                count[0]+=1
            state^=1
        elif a==-1:
            if not state:
                count[0]-=1
            state^=1
        else:
            count[1+state]+=1 if a==2 else -1
    return (state,)+tuple(c%modulus for c in count)

rows=[]
for i,t in enumerate(deck):
    a=substitute(A0,t)
    eval1=evaluate(a,D,power(V,2))
    eval2=evaluate(a,V,power(D,2))
    sh=schreier(a)
    assert eval1==eval2==0 and sh==(0,0,0,0)
    rows.append({"deck_index":i,"A0_word":list(a),
                 "first_cap_value":eval1,"second_cap_value":eval2,
                 "Schreier_mod3":list(sh)})

# The two actual word evaluations in a single joint F image.
pair_x=(D,V)
pair_y=(power(V,2),power(D,2))
pair_group=[(0,0)]
pair_set={(0,0)}
for a in pair_group:
    for b in (pair_x,pair_y):
        c=(mul(a[0],b[0]),mul(a[1],b[1]))
        if c not in pair_set:
            pair_set.add(c)
            pair_group.append(c)

# The signed original modular frame is retained separately.
def mm(a,b,m=12):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m
                 for i in range(2) for j in range(2))
def mi(a,m=12):
    return (a[3]%m,-a[1]%m,-a[2]%m,a[0]%m)
def mp(a,k,m=12):
    if k<0:
        return mp(mi(a,m),-k,m)
    out=(1,0,0,1)
    for _ in range(k):
        out=mm(out,a,m)
    return out
u=(1,1,0,1)
l=(1,0,-1,1)
mx,my=mp(u,2),mp(l,2)
def matrix_word(w):
    a=(1,0,0,1)
    for b in w:
        v=mx if abs(b)==1 else my
        a=mm(a,v if b>0 else mi(v))
    return a
for row in rows:
    row["signed_mod12"]=list(matrix_word(tuple(row["A0_word"])))
    assert row["signed_mod12"]==[5,0,0,5]

# Export the literal finite F source for an independent GAP B-core check:
# two regular cap blocks, Schreier quotient54, signed matrix block20,
# and the actual abelian quotient C12^2.  No formal tuple extension occurs.
states=list(product(range(2),range(3),range(3),range(3)))
state_index={a:i for i,a in enumerate(states)}
sx=[];sy=[]
for e,a,b,c in states:
    sx.append(state_index[(1-e,(a+e)%3,b,c)])
    sy.append(state_index[(e,a,(b+1-e)%3,(c+e)%3)])

v4=[a for a in product(range(4),repeat=2) if gcd(gcd(a[0],a[1]),4)==1]
v3=[a for a in product(range(3),repeat=2) if a!=(0,0)]
def matperm(a,m,vs,projective=False):
    index={v:i for i,v in enumerate(vs)}
    out=[]
    for x,y in vs:
        w=((x*a[0]+y*a[2])%m,(x*a[1]+y*a[3])%m)
        if projective:
            w=min(w,tuple(-z%m for z in w))
        out.append(index[w])
    return out
def disjoint(blocks):
    result=[];offset=0
    for b in blocks:
        result.extend(offset+j for j in b)
        offset+=len(b)
    return result
def block20(a):
    return disjoint([matperm(a,4,v4),matperm(a,3,v3)])
ab=list(product(range(12),repeat=2))
ab_index={a:i for i,a in enumerate(ab)}
abx=[ab_index[((a+1)%12,b)] for a,b in ab]
aby=[ab_index[(a,(b+1)%12)] for a,b in ab]
xF=disjoint([table[:,D].tolist(),table[:,V].tolist(),sx,block20(mx),abx])
yF=disjoint([table[:,power(V,2)].tolist(),table[:,power(D,2)].tolist(),sy,block20(my),aby])
assert len(xF)==len(yF)==650
canon=lambda a:min(a,tuple(-v%12 for v in a))
v12=sorted({canon(a) for a in product(range(12),repeat=2)
            if gcd(gcd(a[0],a[1]),12)==1})
assert len(v12)==48
S=(0,1,11,0);R=(0,11,1,11)
qs=matperm(S,12,v12,True);qr=matperm(R,12,v12,True)
export=HERE/"cap216_genuine_source_data.g"
with export.open("w") as f:
    for name,value in (("capX",xF),("capY",yF),("capQS",qs),("capQR",qr)):
        f.write(name+":=PermList("+str([v+1 for v in value])+");;\n")
    f.write("capSourceDegree:=650;;\n")

result={"scope":"Actual finite source maps and auxiliary frame word; normalized gentle existence is proved by the canonical central-cover certificate.",
        "cap_order":n,"cap_exponent":exponent,"cap_derived_order":len(derived),
        "D":D,"V":V,"generator_orders":[order(D),order(V)],
        "two_evaluation_joint_F_image_order":len(pair_group),
        "source_F_permutation_degree":650,
        "Schreier_modulus":3,"abelian_normalization_modulus":12,
        "deck_checks":rows,"gap_source_data":str(export),
        "status":"PASS"}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print("PASS cap216: exponent12, derivedHeisenberg27, marked generator orders12,4")
print("PASS two actual f-evaluation maps have joint F image order",len(pair_group))
print("PASS all six literal deck images of auxiliary A0 are identity in both cap maps and the Schreier54 quotient")
print("PASS all six signed original mod12 A0 matrices are5I")
print("PASS exported actual F source of permutation degree650, retaining C12^2 normalization")
print("No equality of the auxiliary frame word A0 with the normalized pair word f is asserted.")
