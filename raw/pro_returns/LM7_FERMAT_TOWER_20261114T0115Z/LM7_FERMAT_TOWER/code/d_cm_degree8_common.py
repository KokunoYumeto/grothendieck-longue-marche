#!/usr/bin/env python3
"""An actual N basis adapted to K degree, and the exact new common quotient."""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import product
import io,runpy,json,time
import numpy as np
import d_cm_degree8_magnus as G
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
ch={j:i for i,j in enumerate(R['chN'])}
def hom(word):
    q=R['one'];v=0
    for a in word:
        if a==0:q=R['qm'](q,R['qs'])
        else:
            qq=R['qm'](q,R['qr'] if a==1 else R['qr2'])
            for j in (R['ixQ'][q],R['ixQ'][qq]):
                if j in ch:v^=1<<ch[j]
            q=qq
    return q,v
bas={};basis=[]
def add(word,n,label):
    q,v=hom(word);assert q==R['one'];vv=v
    while vv:
        k=vv.bit_length()-1
        if k not in bas:
            bas[k]=vv;basis.append({'weight':n,'word':word,'homology':hex(v),'label':label});return True
        vv^=bas[k]
    return False
# Choose deepest layers first. A generator with a low leading K degree
# can carry independent higher N-homology coordinates, so ascending
# independence would not give a basis adapted to the filtration.
for n in range(7,2,-1):
    power=1
    while n%power==0:
        d=n//power
        for w in product(range(4),repeat=d):
            if not R['lyndon'](w):continue
            add(R['lieword'](w)*power,n,[list(w),power])
        power*=2
    print('Weighted N basis in degree at least',n,':',len(basis),flush=True)
for i,w in enumerate(R['relwords']):assert add(w,2,['relation',i])
basis.sort(key=lambda b:b['weight'])
assert len(basis)==97
weights=[b['weight'] for b in basis]
counts={n:weights.count(n) for n in range(2,8)}
assert counts=={2:9,3:20,4:25,5:24,6:15,7:4}

def bracket(a,da,b,db):return G.mp(a,da,b,db)^G.mp(b,db,a,da)
L3=[R['lie'](w) for w in R['L3']]
L4=[]
for power,d in [(1,4),(2,2),(4,1)]:
    for w in product(range(4),repeat=d):
        if not R['lyndon'](w):continue
        p=R['lie'](w);dd=d;k=1
        while k<power:p=G.mp(p,dd,p,dd);dd*=2;k*=2
        L4.append(p)
assert len(L4)==70
W={};indices=[]
def add8(v,index):
    while v:
        k=v.bit_length()-1
        if k not in W:W[k]=v;indices.append(index);return
        v^=W[k]
for i,j,k in product(range(9),range(9),range(70)):
    add8(bracket(R['rel'][i],2,bracket(R['rel'][j],2,L4[k],4),6),['224',i,j,k])
print('R2,R2,L4 rank:',len(W),flush=True)
for j,i,k in product(range(20),range(9),range(20)):
    add8(bracket(L3[j],3,bracket(R['rel'][i],2,L3[k],3),5),['323',j,i,k])
print('Full gamma3N degree8 rank:',len(W),flush=True)
assert len(W)==7245

W4={}
for i,j,k,l in product(range(9),repeat=4):
    v=bracket(R['rel'][i],2,bracket(R['rel'][j],2,bracket(R['rel'][k],2,R['rel'][l],2),4),6)
    while v:
        p=v.bit_length()-1
        if p not in W4:W4[p]=v;break
        v^=W4[p]
assert len(W4)==1620
pairweights=[weights[i]+weights[j] for i in range(97) for j in range(i,97)]
low=sum(w<=4 for w in pairweights);middle=sum(5<=w<=8 for w in pairweights);high=sum(w>=9 for w in pairweights)
assert (low,middle,high)==(45,2271,2437)
common=97+sum(w<=8 for w in pairweights)+sum(w<=4 for w in pairweights)
assert common==2458 and 11563-(240+1620+len(W))==common
summary={'weighted_N_basis_counts':counts,'N_Frattini_rank':len(basis),
 'gamma3N_degree8_dimension':len(W),'gamma3N_total_dimension':240+1620+len(W),
 'gamma4N_degree8_dimension':len(W4),'common_quotient_order':'576 * 2^2458',
 'kernel_H2_to_common_order4_generators':high,
 'kernel_H2_to_common_order2_generators':middle,
 'kernel_H2_to_common_log2_order':2*high+middle,
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_degree8_common.json').write_text(json.dumps({'summary':summary,
 'actual_weighted_N_basis':basis,'degree8_gamma3_basis_indices':indices},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
