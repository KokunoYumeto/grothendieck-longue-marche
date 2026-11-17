#!/usr/bin/env python3
"""Exact actual-presentation map into the proposed cone-bearing HNN.

This checks all defining relations and both map conventions.  The
reverse presentation proof (redundancy of added graph edges) is a
separate two-sided algebra argument; a successful forward map alone
does not identify the groups or their centralizers.
"""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
inp=P/'inner_q0_adapted_basis22.json';D=json.loads(inp.read_text())
# a=1,b=2,c=3,d=5,e=6,h=7,p=8,q=9,k=10; f=h k^-1.
ordinary=(1,2,5,6,8,9,10)
V=tuple((i,b) for i in ordinary for b in (0,1))
def bar(v):return (v[0],v[1]^1)
edges=set()
def edge(u,v):assert u!=v;edges.add(frozenset((u,v)))
for i in (1,2,5,6,8,9):edge((i,0),(i,1))
cross=[((1,0),(2,0)),((1,1),(5,0)),((1,1),(6,0)),
       ((5,0),(6,1)),((2,0),(8,0)),((2,0),(9,0)),
       ((8,0),(9,1))]
cross += [((10,0),(i,0)) for i in (1,2,5,6)]
cross += [((10,1),(i,0)) for i in (8,9)]
for u,v in cross:edge(u,v);edge(bar(u),bar(v))
assert len(edges)==32
NON={v:tuple(u for u in V if u!=v and frozenset((u,v)) not in edges) for v in V}
def red(w):
    a=[]
    for x in w:
        x=3 if abs(x)==3 else int(x)
        if a and (a[-1]==-x or a[-1]==x==3):a.pop()
        else:a.append(x)
    return tuple(a)
def mul(*ww):return red(x for w in ww for x in w)
def inv(w):return red(-x for x in w[::-1])
def sub(w,A):return mul(*(A[abs(x)] if x>0 else inv(A[-x]) for x in w))
def comm(a,b):return mul(a,b,inv(a),inv(b))
def normal(letters):
    stacks={v:[] for v in V}
    for v,s in letters:
        if stacks[v] and stacks[v][-1]==-s:
            stacks[v].pop()
            for u in NON[v]:assert stacks[u].pop()==0
        else:
            stacks[v].append(s)
            for u in NON[v]:stacks[u].append(0)
    rev=[]
    while any(stacks.values()):
        v=next(v for v in V if stacks[v] and stacks[v][-1])
        s=stacks[v].pop();rev.append((v,s))
        for u in NON[v]:assert stacks[u].pop()==0
    return tuple(reversed(rev))
def base(w):
    a=[];p=0
    for x in w:
        if abs(x)==3:p^=1
        else:assert abs(x) in ordinary;a.append(((abs(x),p),1 if x>0 else -1))
    return normal(a),p
def bm(*vals):
    a=[];p=0
    for ls,q in vals:a.extend((((i,b^p),s) for (i,b),s in ls));p^=q
    return normal(a),p
def bw(g):
    ls,p=g;w=[]
    for (i,b),s in ls:w.extend((3,s*i,3) if b else (s*i,))
    if p:w.append(3)
    return red(w)
src={(i,b) for i in (10,5,6) for b in (0,1)}
dst={(i,b) for i in (10,8,9) for b in (0,1)}
def vertex_map(v,sign):
    i,b=v
    if i==10:return (10,b^1)
    return ({5:8,6:9}[i] if sign>0 else {8:5,9:6}[i],b)
src_edges={e for e in edges if e<=src}
dst_edges={e for e in edges if e<=dst}
assert {frozenset(vertex_map(v,1) for v in e) for e in src_edges}==dst_edges
for v in src:assert vertex_map(vertex_map(v,1),-1)==v
def evaluate(word):
    bases=[];ss=[];part=[]
    for x in word:
        if abs(x)==7:bases.append(base(part));part=[];ss.append(1 if x>0 else -1)
        else:part.append(x)
    bases.append(base(part));steps=[]
    while True:
        at=None
        for j in range(len(ss)-1):
            if ss[j+1]!=-ss[j]:continue
            domain=src if ss[j]>0 else dst
            if all(v in domain for v,s in bases[j+1][0]):at=j;break
        if at is None:break
        j=at;ls,par=bases[j+1]
        val=(normal([(vertex_map(v,ss[j]),s) for v,s in ls]),par)
        steps.append({'position':j,'sign':ss[j],'input':bw(bases[j+1]),'output':bw(val)})
        bases[j:j+3]=[bm(bases[j],val,bases[j+2])];ss[j:j+2]=[]
    return {'trivial':not ss and bases[0]==((),0),'stable_signs':ss,
            'base_words':[bw(g) for g in bases],'steps':steps}
Ymap={1:(1,),2:(2,),3:(3,),4:(7,-10),5:(5,),6:(6,)}
checks=[]
for row in D['all_ten_relations']:
    word=sub(tuple(row['new_relation']),Ymap);nf=evaluate(word)
    checks.append({'kind':'actual_node','name':row['name'],'physical_labels':row['physical_labels'],
                   'word':word,'normal_form':nf})
    assert nf['trivial'],('node',row['name'],nf)
    print('PASS actual node',row['name'],row['physical_labels'],len(nf['steps']),'pinches')
sigma={int(k):tuple(v) for k,v in D['source_h_action'].items()}
for i in range(1,7):
    word=mul((-7,),Ymap[i],(7,),inv(sub(sigma[i],Ymap)))
    nf=evaluate(word);assert nf['trivial'],('source action',i,nf)
    checks.append({'kind':'actual_source_action','generator':i,'word':word,'normal_form':nf})
for v in src:
    vw=bw((((v,1),),0));im=bw((((vertex_map(v,1),1),),0))
    assert evaluate(mul((7,),vw,(-7,),inv(im)))['trivial']
assert evaluate((7,3,-7,3))['trivial']
out={'status':'PASS','input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
 'base_vertices':V,'base_edges':[sorted(e) for e in sorted(edges,key=lambda e:sorted(e))],
 'source_vertices':sorted(src),'target_vertices':sorted(dst),'source_contains_c':True,
 'stable_letter':7,'stable_direction':'h domain h^-1 = range',
 'Y_generators_in_candidate':Ymap,'checks':checks,
 'scope':'All actual annular defining relators map to the proposed HNN; reverse redundancy proof still required before an identification.'}
(P/'annular_candidate_HNN22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all ten actual nodes and six actual source-action equations')
print('PASS edge full-subgraph isomorphism; forward presentation map only')
