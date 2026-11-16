"""First lower-central checks for the two actual cyclic rigid monodromies.

These are bounds on associated graded maps, never claims of injection
of a full discrete or profinite group.
"""
from pathlib import Path
import json,itertools
import sympy as s
HERE=Path(__file__).resolve().parent
j=json.loads((HERE/'rigid_restrictions.json').read_text())
pairs=list(itertools.combinations(range(6),2));triples=list(itertools.combinations(range(6),3));pi={t:i for i,t in enumerate(pairs)}
def links(w):
    order=list(range(6));c=[0]*15
    for a in w:
        k=abs(a)-1;c[pi[tuple(sorted(order[k:k+2]))]]+=1 if a>0 else -1
        order[k],order[k+1]=order[k+1],order[k]
    assert order==list(range(6)) and all(x%2==0 for x in c)
    return s.Matrix([x//2 for x in c])
def bracket(v,w):
    out=[]
    for i,j,k in triples:
        a,b,c=pi[i,j],pi[i,k],pi[j,k]
        out.append(v[a]*w[c]-v[c]*w[a]-v[a]*w[b]+v[b]*w[a]-v[b]*w[c]+v[c]*w[b])
    return s.Matrix(out)
rows={};Bs=[]
for name,fam in j['families'].items():
    M=s.Matrix.hstack(*[links(r['braid']) for r in fam.values()]);B=s.Matrix.hstack(*[bracket(M[:,a],M[:,b]) for a,b in pairs])
    rows[name]={'H1':list(M.tolist()),'degree2':list(B.tolist()),'rank1':M.rank(),'rank2':B.rank()};Bs.append(B)
    print(name,'H1 rank',M.rank(),'degree2 rank',B.rank(),'degree2 nullspace',[list(v) for v in B.nullspace()],flush=True)
M=s.Matrix.vstack(*Bs)
rows['joint_degree2_rank']=M.rank();rows['joint_degree2_kernel']=[list(v) for v in M.nullspace()]
print('joint degree2 rank',M.rank(),'kernel',rows['joint_degree2_kernel'],flush=True)
(HERE/'birman_first_checks.json').write_text(json.dumps(rows,default=int,indent=2)+'\n')
