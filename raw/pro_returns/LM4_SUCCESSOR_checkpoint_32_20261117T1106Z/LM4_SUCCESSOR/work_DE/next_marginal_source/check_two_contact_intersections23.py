#!/usr/bin/env python3
"""Independent complete finite folding replay, with no producer imports."""
from pathlib import Path
from collections import deque
import hashlib, json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CE = ROOT / 'work_CE/next_symmetric_nodes'

def red(w):
    a=[]
    for x in w:
        if a and a[-1] == -x: a.pop()
        else: a.append(x)
    return tuple(a)

def inv(w): return tuple(-x for x in reversed(w))
def sub(w, images):
    out=()
    for x in w:
        out=red(out+(images[x] if x>0 else inv(images[-x])))
    return out

def fold(words):
    # Start with the literal based bouquet of subdivided word circles.
    parent=[0]; edges=[]
    def new():
        i=len(parent); parent.append(i); return i
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    for w in words:
        u=0
        for j,x in enumerate(w):
            v=0 if j==len(w)-1 else new()
            edges.extend([(u,x,v),(v,-x,u)]); u=v
    while True:
        changed=False; seen={}
        for u,x,v in edges:
            u,v=find(u),find(v); key=(u,x)
            if key in seen:
                a,b=find(seen[key]),v
                if a!=b:
                    parent[max(a,b)]=min(a,b); changed=True; break
            else: seen[key]=v
        if not changed: break
    g={find(i):{} for i in range(len(parent))}
    for u,x,v in edges:
        u,v=find(u),find(v)
        assert x not in g[u] or g[u][x]==v
        g[u][x]=v
    for u,row in g.items():
        for x,v in row.items(): assert g[v][-x]==u
    base=find(0)
    for w in words:
        v=base
        for x in w: v=g[v][x]
        assert v==base
    return base,g

def product(G,H):
    gb,g=G; hb,h=H; b=(gb,hb)
    ids={b:0}; todo=deque([b]); out={}
    while todo:
        v=todo.popleft(); row={}
        for x in sorted(set(g[v[0]]) & set(h[v[1]])):
            w=(g[v[0]][x],h[v[1]][x])
            if w not in ids:
                ids[w]=len(ids); todo.append(w)
            row[x]=ids[w]
        out[ids[v]]=row
    edges=sum(len(row) for row in out.values())//2
    assert sum(len(row) for row in out.values())==2*edges
    return out, edges, edges-len(out)+1

eta_path=HERE/'annular_neck_reflection23.json'
raw=json.loads(eta_path.read_text())
eta={int(k):tuple(v) for k,v in raw['eta_adapted_K_basis_a_barb_d_e_f'].items()}
for j in range(1,6): assert sub(eta[j],eta)==(j,)
L=((1,),(3,),(4,),(-5,2,5))
Q1=((1,),(3,),(4,))
Q2=tuple(red((1,)+w+(-1,)) for w in ((2,),(5,3,-5),(5,4,-5)))
checks=[]
for name,Q,source,key in [
    ('first_complete_block',Q1,'annular_contact_intersection23.json','Q_basis_eta_adE'),
    ('second_gap_conjugated_complete_block',Q2,'annular_second_contact_intersection23.json','Q_basis_eta_gap_Q2')]:
    ce_path=CE/source; ce=json.loads(ce_path.read_text())
    R=tuple(sub(w,eta) for w in Q)
    assert [list(w) for w in R]==ce[key]
    assert [list(w) for w in L]==ce['L_basis']
    gf,hf=fold(L),fold(R)
    graph,edges,rank=product(gf,hf)
    canonical={str(v):{str(x):w for x,w in row.items()} for v,row in graph.items()}
    assert canonical==ce['product_graph']
    assert [len(gf[1]),len(hf[1]),len(graph),edges,rank]==[
        ce['left_vertices'],ce['right_vertices'],ce['product_vertices'],ce['product_edges'],ce['intersection_rank']]
    assert rank==0
    checks.append({'name':name,'source_sha256':hashlib.sha256(ce_path.read_bytes()).hexdigest(),
      'left_vertices':len(gf[1]),'right_vertices':len(hf[1]),'complete_product_graph':canonical,
      'product_vertices':len(graph),'product_edges':edges,'intersection_rank':rank})
    print(name, 'PASS', 'vertices/edges/rank=',len(graph),edges,rank)
result={'status':'PASS_INDEPENDENT_COMPLETE_FOLDING',
 'eta_sha256':hashlib.sha256(eta_path.read_bytes()).hexdigest(),'checks':checks,
 'scope':'Exactly the two specified full free-subgroup intersections; no truncation, no finite-group quotient, no post-cross-quotient inference.'}
(HERE/'two_contact_intersections_independent23.json').write_text(json.dumps(result,indent=2)+'\n')
print('Both full based product automata are trees, so both intersections are trivial.')
