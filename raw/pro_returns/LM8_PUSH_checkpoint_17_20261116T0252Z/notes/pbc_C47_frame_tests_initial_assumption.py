#!/usr/bin/env python3
"""All eight signed central frame tests; these are finite compatibility only."""
from pathlib import Path
import importlib.util,json,hashlib
from collections import deque
root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('detector',root/'pbc_finite_parity_detector.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
D=m.Detector()

def graph_solution(rhs,part):
    p=(2,3)[part];n=len(rhs)
    assert sum(rhs)%p==0
    ps=D.permutation(D.s,part);pr=D.permutation(D.r,part)
    graph=[[] for _ in range(n)]
    for j in range(n):
        for kind,u,v in [('b',j,ps[j]),('a',ps[j],ps[pr[j]])]:
            graph[u].append((v,kind,j,1));graph[v].append((u,kind,j,-1))
    prev={0:None};todo=deque([0])
    while todo:
        u=todo.popleft()
        for v,kind,j,sgn in graph[u]:
            if v not in prev:prev[v]=(u,kind,j,sgn);todo.append(v)
    assert len(prev)==n
    a=[0]*n;b=[0]*n
    for endpoint,value in enumerate(rhs):
        if endpoint==0 or value%p==0:continue
        coeff=-value%p;node=endpoint
        while node:
            old,kind,j,sgn=prev[node]
            arr=a if kind=='a' else b;arr[j]=(arr[j]+coeff*sgn)%p
            node=old
    lhs=[]
    sb=D.act(D.s,tuple(b),part)
    ra=D.act(D.r,tuple(a),part)
    sa_minus_sra=D.act(D.s,tuple((x-y)%p for x,y in zip(a,ra)),part)
    lhs=tuple((x-y+z)%p for x,y,z in zip(b,sb,sa_minus_sra))
    assert lhs==tuple(x%p for x in rhs)
    return tuple(a),tuple(b)

As=[a for a in D.pure if m.mul(a,D.r)==m.mul(D.r,a)]
Bs=[]
for b in D.pure:
    if m.mul(b,D.s)!=m.mul(D.s,b):continue
    try:D.signed_mod3(b)
    except ValueError:continue
    Bs.append(b)
assert len(As)==2 and len(Bs)==4
rows=[]
for A0 in As:
 for B0 in Bs:
    av=[];bv=[]
    for part,p in enumerate((2,3)):
        vs,vr=D.shat[part],D.rhat[part]
        bvs=D.act(B0,vs,part)
        avr=D.act(A0,vr,part)
        diff=D.act(D.s,tuple((x-y)%p for x,y in zip(vr,avr)),part)
        rhs=tuple((x-y+z)%p for x,y,z in zip(vs,bvs,diff))
        a,b=graph_solution(rhs,part);av.append(a);bv.append(b)
    A=(av[0],av[1],A0);B=(bv[0],bv[1],B0)
    sp=D.gmul(D.gmul(B,D.shat),D.ginv(B))
    rp=D.gmul(D.gmul(A,D.rhat),D.ginv(A))
    assert D.gmul(sp,rp)==D.tauhat
    f=D.gmul(D.shat,sp)
    ans=D.evaluate(f)
    assert ans['r_frame_base']==A0 and ans['s_frame_base']==B0
    assert ans['intertwiner_t_mod12']==0
    rows.append({'r_frame':A0,'s_frame':B0,'evaluation':ans})
assert sum(x['evaluation']['delta'] for x in rows)==4
out={'status':'PASS','scope':'Eight exact finite frame-compatible tuples only. No assertion that these particular residues lift to full gentle elements. The actual nonzero full witness is separately proved in C46.','rows':rows,'detector_source_sha256':hashlib.sha256((root/'pbc_finite_parity_detector.py').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
