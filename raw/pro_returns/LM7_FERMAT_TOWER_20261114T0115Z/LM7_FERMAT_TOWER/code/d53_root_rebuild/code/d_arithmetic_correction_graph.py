#!/usr/bin/env python3
"""Exact small-graph certificate for the actual arithmetic G3 correction space.

The group Q has576 states; G3 is its actual rank97 elementary-three
homology extension. Centralizer projections are tested in that extension
by their complete linear equations, without enumerating its huge order.
"""
from pathlib import Path
from collections import deque
from itertools import product
import json,time
OUT=Path(__file__).resolve().parent;started=time.time()
mod=12
def norm(a):return min(a,tuple(-v%mod for v in a))
def mm(a,b):
    x,y,z,w=a;p,q,r,s=b
    return norm(((x*p+y*r)%mod,(x*q+y*s)%mod,(z*p+w*r)%mod,(z*q+w*s)%mod))
I=norm((1,0,0,1));S=norm((0,1,11,0));R=norm((0,11,1,11))
states=[I];index={I:0};words=[[]]
for a in states:
    w=words[index[a]]
    for token,b in [(0,S),(1,R),(2,mm(R,R))]:
        c=mm(a,b)
        if c not in index:index[c]=len(states);states.append(c);words.append(w+[token])
assert len(states)==576
enumerated={norm(a) for a in product(range(12),repeat=4) if (a[0]*a[3]-a[1]*a[2])%12==1}
assert set(states)==enumerated
table=[[index[mm(a,b)] for b in states] for a in states]
s=index[S];r=index[R];t=table[s][r]
rs=[table[g][s] for g in range(576)]
rr=[table[g][r] for g in range(576)]
inverses=[index[norm((a[3],-a[1]%12,-a[2]%12,a[0]))] for a in states]
def inverse(word):return [0 if x==0 else 3-x for x in reversed(word)]
v2=[(0,min(g,rs[g])) for g in range(576)]
v3=[(1,min(g,rr[g],rr[rr[g]])) for g in range(576)]
adj={v:[] for v in set(v2+v3)}
for e in range(576):
    adj[v2[e]].append((v3[e],e));adj[v3[e]].append((v2[e],e))
paths={v2[0]:{}};queue=deque([v2[0]]);tree=set()
while queue:
    v=queue.popleft()
    for u,e in adj[v]:
        if u not in paths:
            c=paths[v].copy();c[e]=c.get(e,0)+(1 if v[0]==0 else -1)
            if not c[e]:del c[e]
            paths[u]=c;tree.add(e);queue.append(u)
chords=[e for e in range(576) if e not in tree]
cycles=[]
for e in chords:
    c=paths[v2[e]].copy()
    for j,a in paths[v3[e]].items():c[j]=c.get(j,0)-a
    c[e]=c.get(e,0)+1
    cycles.append({j:a for j,a in c.items() if a})
rho=len(cycles);assert rho==97
def action(g):
    cols=[]
    for c in cycles:
        d={}
        for j,a in c.items():d[table[g][j]]=(d.get(table[g][j],0)+a)%3
        cols.append([d.get(e,0) for e in chords])
    return cols
MS=action(s);MR=action(r)
def combine(cols,v):
    out=[0]*rho
    for a,col in zip(v,cols):
        if a:
            out=[(x+a*y)%3 for x,y in zip(out,col)]
    return out
def solver(cols):
    basis={}
    for j,col in enumerate(cols):
        v=[a%3 for a in col];w=[0]*len(cols);w[j]=1
        while any(v):
            p=max(i for i,a in enumerate(v) if a)
            if p not in basis:
                inv=1 if v[p]==1 else 2
                v=[a*inv%3 for a in v];w=[a*inv%3 for a in w]
                basis[p]=(v,w);break
            q,z=basis[p];a=v[p]
            v=[(x-a*y)%3 for x,y in zip(v,q)]
            w=[(x-a*y)%3 for x,y in zip(w,z)]
    def solve(rhs):
        v=[a%3 for a in rhs];w=[0]*len(cols)
        for p in sorted(basis,reverse=True):
            if v[p]:
                q,z=basis[p];a=v[p]
                v=[(x-a*y)%3 for x,y in zip(v,q)]
                w=[(x+a*y)%3 for x,y in zip(w,z)]
        return None if any(v) else w
    return solve,len(basis)
def minus_identity(cols):
    return [[(a-int(i==j))%3 for i,a in enumerate(c)] for j,c in enumerate(cols)]
NS=minus_identity(MS);NR=minus_identity(MR)
_,rank_s=solver(NS);_,rank_r=solver(NR)
_,rank_r2=solver([combine(NR,c) for c in NR])
assert rank_s==52 and rank_r==63 and rank_r2==29
assert all(combine(MS,c)==[int(i==j) for i in range(rho)] for j,c in enumerate(MS))
assert all(combine(MR,combine(MR,c))==[int(i==j) for i in range(rho)] for j,c in enumerate(MR))
def path(word):
    q=0;v=[0]*576
    for a in word:
        if a==0:q=rs[q]
        else:
            h=rr[q] if a==1 else rr[rr[q]]
            v[q]=(v[q]+1)%3;v[h]=(v[h]-1)%3;q=h
    return q,[v[e] for e in chords]
def centralizer(q):return [g for g in range(576) if table[g][q]==table[q][g]]
CS=centralizer(s);CR=centralizer(r)
assert len(CS)==16 and len(CR)==18
centralizer_records={}
for name,q,token,M,C in [('s',s,0,MS,CS),('r',r,1,MR,CR)]:
    columns=[[(int(i==j)-a)%3 for i,a in enumerate(c)] for j,c in enumerate(M)]
    solve,rank=solver(columns);records=[]
    for g in C:
        w=words[g];end,defect=path(w+[token]+inverse(w)+inverse([token]))
        assert end==0
        correction=solve([(-a)%3 for a in defect])
        if correction is not None:
            assert [(a+b)%3 for a,b in zip(combine(columns,correction),defect)]==[0]*rho
        records.append({'q_state':g,'q_matrix':list(states[g]),'defect':defect,'correction':correction})
    centralizer_records[name]=records
assert sum(x['correction'] is not None for x in centralizer_records['s'])==16
liftable_r=[x['q_state'] for x in centralizer_records['r'] if x['correction'] is not None]
assert set(liftable_r)=={0,r,table[r][r]}
tc=[0];a=t
while a:
    tc.append(a);a=table[a][t]
assert len(tc)==12
def conjugacy(q):return {table[table[g][q]][inverses[g]] for g in range(576)}
cls=conjugacy(s);clr=conjugacy(r);clr2=conjugacy(table[r][r])
assert not set(tc)&(cls|clr|clr2)
assert table[r][r] not in clr
tword=[0,1]
end,t12=path(tword*12);assert end==0 and any(t12)
assert path(tword*36)==(0,[0]*rho)
g3_order=576*3**97
lower=80*3**95-4*3**45-4*3**34
assert lower>0
summary={
 'scope':'Actual Q and actual G3 homology extension; no finite surrogate for the arithmetic subgroup A.',
 'Q_order':576,'N_mod3_homology_dimension':97,
 'Q_s_centralizer_order':16,'Q_r_centralizer_order':18,
 's_fixed_dimension_on_N_mod3':45,'r_fixed_dimension_on_N_mod3':34,
 'r_Jordan_blocks_length3':29,'r_Jordan_blocks_length2':5,'r_Jordan_blocks_length1':0,
 's_centralizer_Q_images_lifted':16,'r_centralizer_Q_images_lifted':3,
 'G3_s_centralizer_order_formula':'16*3^45',
 'G3_r_centralizer_order_formula':'3^35',
 'Q_cusp_order':12,'G3_cusp_order':36,
 'Q_cusp_cyclic_group_avoids_all_elliptic_conjugacy_classes':True,
 'G3_order':str(g3_order),
 'actual_arithmetic_peripheral_correction_dimension_lower_bound':str(lower),
 'dimension_lower_bound_formula':'80*3^95-4*3^45-4*3^34',
 'dimension_lower_bound_positive':True,
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'Q_states':[list(a) for a in states],
 'right_s':rs,'right_r':rr,'cycle_chords':chords,
 'mod3_s_columns':MS,'mod3_r_columns':MR,
 'complete_centralizer_lifting_equations':centralizer_records,
 'actual_cusp_t12_mod3_cycle':t12}
(OUT/'d_arithmetic_correction_graph.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
