"""Exact pure character pair groups modulo four in the integral F5 basis."""
import json
import numpy as np
from check_ferrari_d4_fox import ROOT, INPUT

data=json.loads(INPUT.read_text());I=np.eye(5,dtype=np.int16)
def mul(a,b):return a@b%4
def power(g,n):
    h=I
    while n:
        if n&1:h=mul(h,g)
        g=mul(g,g);n//=2
    return h
def inverse(g):return power(g,31)
def comm(a,b):return mul(mul(mul(a,b),inverse(a)),inverse(b))
def closure(gs):
    gs=list({g.tobytes():g for g in gs}.values());G=[I];seen={I.tobytes()}
    for h in G:
        for g in gs:
            v=mul(h,g);k=v.tobytes()
            if k not in seen:seen.add(k);G.append(v)
        assert len(G)<=32
    return G
A,B,C=[np.array(data['abelianization_matrices'][s],dtype=np.int16)%4 for s in ('a','b','c')]
X=[power(A,2),power(B,2),power(C,2),power(A@B@A%4,2),power(C@B@C%4,2)]
out=[]
for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    G=closure([X[i],X[j]])
    assert all(np.array_equal(mul(g,inverse(g)),I) for g in G)
    K=G;lower=[len(K)]
    while len(K)>1:
        K=closure([comm(k,g) for k in K for g in G]);lower.append(len(K));assert len(lower)<5
    K=G;derived=[len(K)]
    while len(K)>1:
        K=closure([comm(k,g) for k in K for g in K]);derived.append(len(K));assert len(derived)<5
    out.append({'pair':[i+1,j+1],'order':len(G),'lower_central_orders':lower,'derived_orders':derived})
(ROOT/'d4_character_pair_groups.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
