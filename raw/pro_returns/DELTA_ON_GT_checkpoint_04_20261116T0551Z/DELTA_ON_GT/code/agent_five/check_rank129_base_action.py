"""The exact gentle-relevant pair actions on the order256 Ferrari base.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129.npz');a,b,c=[tuple(map(int,g))for g in F['vertex_actions']];I=tuple(range(256))
def mul(g,h):return tuple(g[i]for i in h)
def prod(*gg):
    q=I
    for g in gg:q=mul(q,g)
    return q
def inv(g):
    q=[0]*256
    for i,j in enumerate(g):q[j]=i
    return tuple(q)
def comm(g,h):return prod(g,h,inv(g),inv(h))
def closure(gg):
    G=[I];seen={I}
    for g in G:
        for h in gg:
            z=mul(g,h)
            if z not in seen:seen.add(z);G.append(z)
    return G
X=[prod(a,a),prod(b,b),prod(c,c),prod(a,b,a,a,b,a),prod(c,b,c,c,b,c)]
reports=[]
for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    gg=[X[i],X[j]];K=closure(gg);orders=[len(K)]
    while len(K)>1:
        K=closure(list({comm(k,g)for k in K for g in gg}));orders.append(len(K))
    assert len(orders)<=3
    reports.append({'pair':[i+1,j+1],'lower_central_series':orders})
Q=F['Q'];index={tuple(map(int,q)):i for i,q in enumerate(Q)}
labels=[(i,q)for i in range(3)for q in range(8)if not(q&(1<<i))];ei={e:j for j,e in enumerate(labels)}
left=[]
for i in range(3):
    p=[ei[(j,(q^(1<<i))&~(1<<j))]for j,q in labels];acts=[0]*4096
    for v in range(1,4096):
        low=v&-v;k=low.bit_length()-1;acts[v]=acts[v^low]^(1<<p[k])
    vt=1<<ei[(i,0)]
    left.append([index[(vt^acts[int(v)],(1<<i)^int(b))]for v,b in Q])
center=[q for q in range(256)if all(left[i][q]==int(F['right'][q,i])for i in range(3))]
print(json.dumps({'base_order':256,'base_center_order':len(center),
 'base_center_elements_in_cube_chain_coordinates':[list(map(int,Q[q]))for q in center],
 'pair_action_reports':reports,
 'consequence':'Every actual gentleH f belongs gamma3F and acts trivially in each of these Aut(Q) pair evaluations.',
 'scope':'Trivial conjugation action on Q does not by itself imply a chosen automorphism fixes Q pointwise, because Q has a nontrivial centre.'},indent=2))
