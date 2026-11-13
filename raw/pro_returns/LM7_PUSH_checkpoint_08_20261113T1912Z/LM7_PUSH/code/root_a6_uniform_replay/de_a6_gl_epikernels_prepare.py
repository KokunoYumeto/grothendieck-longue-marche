#!/usr/bin/env python3
"""Actual B-induced quotients of all19 A5 epikernels of the source F."""
from pathlib import Path
from collections import deque
import json
import numpy as np
from de_ferrari_a5_model import FerrariA5
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent
H=FerrariA5();d=load_data();Q=sorted(d['Q2']);ix={q:i for i,q in enumerate(Q)}
section={d['unit']:[]};todo=deque(section)
while todo:
    q=todo.popleft()
    for a,g in ((0,d['s2']),(1,d['r2'])):
        qn=d['mul2'](q,g)
        if qn not in section:section[qn]=section[q]+[a];todo.append(qn)
pairs=np.array(H.generating_pairs,dtype=np.int64)
letters={1:pairs[:,0],2:pairs[:,1],-1:H.si[pairs[:,0]],-2:H.si[pairs[:,1]]}
def fword(w):
    out=np.zeros(19,dtype=np.int64)
    for a in w:out=H.sm[out,letters[a]]
    return out
perms=[]
for a,g in ((0,d['s2']),(1,d['r2'])):
    p=np.empty(570,dtype=np.int64)
    for q in Q:
        qn=d['mul2'](q,g)
        vals=fword(d['fword'](section[q]+[a]+d['binv'](section[qn])))
        for j,v in enumerate(vals):
            p[30*j+5*ix[q]:30*j+5*ix[q]+5]=30*j+5*ix[qn]+np.array(H.permutations[H.si[v]])
    assert np.array_equal(np.sort(p),np.arange(570));perms.append(p)
s,r=perms;identity=np.arange(570);assert np.array_equal(s[s],identity) and np.array_equal(r[r[r]],identity)
bl={0:s,1:r,-1:r[r]}
def bword(w):
    ans=identity.copy()
    for a in w:ans=bl[a][ans]
    return ans
fx,fy=bword(d['xword']),bword(d['yword']);root=ix[d['unit']]
for j,(g,h) in enumerate(pairs):
    points=np.arange(30*j+5*root,30*j+5*root+5)
    assert np.array_equal(fx[points],points[np.array(H.permutations[H.si[g]])])
    assert np.array_equal(fy[points],points[np.array(H.permutations[H.si[h]])])
coordinate={}
for j,(g,h) in enumerate(pairs):
    for a in range(120):coordinate[(int(H.sm[H.sm[a,g],H.si[a]]),int(H.sm[H.sm[a,h],H.si[a]]))]=j
ps=[];pr=[]
for g,h in pairs:
    ps.append(coordinate[(int(h),int(g))]);pr.append(coordinate[(int(h),int(H.si[H.sm[g,h]]))])
orbits=[];seen=set()
for j in range(19):
    if j in seen:continue
    queue=[j];seen.add(j)
    for a in queue:
        for p in (ps,pr):
            if p[a] not in seen:seen.add(p[a]);queue.append(p[a])
    orbits.append(sorted(queue))
with (HERE/'de_a6_gl_epikernels.input').open('w') as f:
    f.write('570 2\n')
    for p in perms:f.write(' '.join(map(str,p))+'\n')
np.savez_compressed(HERE/'de_a6_gl_epikernels.npz',s=s,r=r,x=fx,y=fy,
                    generating_pairs=pairs,source_s_action=np.array(ps),source_r_action=np.array(pr))
with (HERE/'de_a6_gl_A5_source.input').open('w') as f:
    A=np.load(HERE/'de_ferrari_a5_source_compressed.npz');f.write(f'{len(A["s"])} 2\n')
    for k in ('s','r'):f.write(' '.join(map(str,A[k]))+'\n')
out={'status':'PASS_LITERAL_A5_EPIKERNEL_SOURCE','degree':570,'epikernels':19,
     'B_conjugation_orbits':orbits,'root_coset_index':root,
     'all_literal_F_generator_values_verified':True,'all_B_torsion_relations_verified':True}
(HERE/'de_a6_gl_epikernels_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
