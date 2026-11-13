#!/usr/bin/env python3
"""Finite N=2 consequence of Enriquez Theorem 8.1 for the CM witnesses.

We compute the exact image of [N_B,N_B]N_B^6 under
(q delta_2,c_2 mod6): H_2 -> H x Z/6, using N_B subset H_2.
This is a necessary finite distribution test for any full GT lift. A pass
is deliberately not certified as existence of such a lift.
"""
from contextlib import redirect_stdout
from collections import deque,Counter
from pathlib import Path
import io,json,runpy
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()): d=runpy.run_path(str(here/'de_verify_cm.py'))
Q,ss,rr,unit=d['Q'],d['ss'],d['rr'],d['unit']
times,inverse=d['times'],d['inverse']
adj,root,sv,rv=d['adj'],d['root'],d['sv'],d['rv']
chords,C=d['chords'],d['C']
qx,qy=d['xi'][0],d['yi'][0]
def binv(w):return [0 if a==0 else -a for a in w[::-1]]
def bpower(w,n):return w*n if n>=0 else binv(w)*(-n)
treepaths={root:[]};todo=deque([root])
while todo:
    v=todo.popleft()
    for w,e,sign in adj[v]:
        if w not in treepaths:treepaths[w]=treepaths[v]+[(e,sign)];todo.append(w)
def pathword(p):
    q=unit;w=[]
    for e,sign in p:
        qe=Q[e]
        if sign==1:
            if qe!=q: assert qe==times(q,ss);w.append(0)
        else:
            if qe==times(q,rr):w.append(1)
            elif qe==times(q,times(rr,rr)):w.append(-1)
            else:assert qe==q
        q=qe
    if q!=unit:assert q==ss;w.append(0)
    return w
Nwords=[]
for e in chords:
    p=treepaths[sv[Q[e]]]+[(e,1)]+[(a,-b) for a,b in treepaths[rv[Q[e]]][::-1]]
    Nwords.append(pathword(p))
Bpaths={unit:[]};todo=deque([unit])
while todo:
    q=todo.popleft()
    for letter,g in ((0,ss),(1,rr)):
        qg=times(q,g)
        if qg not in Bpaths:Bpaths[qg]=Bpaths[q]+[letter];todo.append(qg)

def red2(a):return tuple(v%2 for v in a)
def mul2(a,b):return tuple(v%2 for v in (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
Q2=sorted(set(map(red2,Q)));s2=red2(ss);r2=red2(rr);r22=mul2(r2,r2)
sv2={q:('s',min(q,mul2(q,s2))) for q in Q2}
rv2={q:('r',min(q,mul2(q,r2),mul2(q,r22))) for q in Q2}
adj2={v:[] for v in set(sv2.values())|set(rv2.values())}
for q in Q2:adj2[sv2[q]].append((rv2[q],q));adj2[rv2[q]].append((sv2[q],q))
seen={sv2[unit]};tree2=set();todo=deque(seen)
while todo:
    v=todo.popleft()
    for w,q in adj2[v]:
        if w not in seen:seen.add(w);tree2.add(q);todo.append(w)
fc={q:i+1 for i,q in enumerate(sorted(set(Q2)-tree2))}
assert len(fc)==2
def freered(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return tuple(out)
def finv(w):return tuple(-a for a in w[::-1])
def graphword(w):
    q=unit;out=[]
    for a in w:
        qn=mul2(q,s2 if a==0 else r2 if a==1 else r22)
        if a:
            if q in fc:out.append(fc[q])
            if qn in fc:out.append(-fc[qn])
        q=qn
    assert q==unit
    return freered(out)
xword=[-1,0,-1,0];yword=[0,-1,0,-1]
gx,gy=graphword(xword),graphword(yword)
gimages={1:gx,-1:finv(gx),2:gy,-2:finv(gy)}
expr={():()};todo=deque([()]);inverse_basis={}
while todo and len(inverse_basis)<2:
    val=todo.popleft();w=expr[val]
    if val in [(1,),(2,)]:inverse_basis[val[0]]=w
    if len(w)>=8:continue
    for a in (1,-1,2,-2):
        if w and w[-1]==-a:continue
        nxt=freered(val+gimages[a])
        if nxt not in expr:expr[nxt]=w+(a,);todo.append(nxt)
assert len(inverse_basis)==2
def fword(w):
    out=()
    for a in graphword(w):
        z=inverse_basis[abs(a)];out+=z if a>0 else finv(z)
    return freered(out)
assert fword(xword)==(1,) and fword(yword)==(2,)
def delta(w,n=2):
    position=0;q=unit;c=0
    for a in w:
        if a==1:
            if position==n-1:q=times(q,qx)
            position=(position+1)%n
        elif a==-1:
            if position==0:q=times(q,inverse(qx))
            position=(position-1)%n
        elif position==0:
            q=times(q,qy if a==2 else inverse(qy));c+=1 if a==2 else -1
    assert position==0
    return q,c%6
def mul(a,b):return times(a[0],b[0]),(a[1]+b[1])%6
def inv(a):return inverse(a[0]),-a[1]%6
one=(unit,0)
def power(a,n):
    out=one
    for k in range(n):out=mul(out,a)
    return out
def closure(gens):
    gens=list(set(gens));seen={one};queue=[one]
    for a in queue:
        for b in gens:
            c=mul(a,b)
            if c not in seen:seen.add(c);queue.append(c)
    return seen
Nfwords=[fword(w) for w in Nwords]
assert all(sum((1 if a==1 else -1 if a==-1 else 0) for a in w)%2==0 for w in Nfwords)
Nimage=closure([delta(w) for w in Nfwords])
derived={mul(mul(mul(a,b),inv(a)),inv(b)) for a in Nimage for b in Nimage}
Kimage=closure(derived|{power(a,6) for a in Nimage})
cert=json.loads((here/'de_source/d_cm_shadow.json').read_text())['pairs']
gcert=json.loads((here/'de_verify_cm.json').read_text())['certificates']
gauge_by_pair={(d['representative'](x['A']),d['representative'](x['beta'])):x['integral_gauge_k'] for x in gcert}
results=[];words_for_further_tests=[]
for rec in cert:
    if 'mod6_beta_cycles' not in rec:continue
    a,b=d['representative'](rec['A']),d['representative'](rec['beta'])
    beta=[]
    for j,w in enumerate(Nwords):beta+=w*rec['mod6_beta_cycles'].get(str(j),0)
    beta+=Bpaths[b]
    bfw=fword(beta)
    ex=sum(1 if t==1 else -1 if t==-1 else 0 for t in bfw)
    ey=sum(1 if t==2 else -1 if t==-2 else 0 for t in bfw)
    k=ey-ex;assert k==gauge_by_pair[a,b]
    beta1=bpower(xword,k)+beta
    fw=fword([0]+beta1+[0]+binv(beta1))
    assert sum(1 if t==1 else -1 if t==-1 else 0 for t in fw)==0
    assert sum(1 if t==2 else -1 if t==-2 else 0 for t in fw)==0
    qf=unit
    for t in fw:qf=times(qf, qx if t==1 else inverse(qx) if t==-1 else qy if t==2 else inverse(qy))
    words_for_further_tests.append((fw,qf,rec['missing_coset']))
    value=delta(fw);coset={mul(value,z) for z in Kimage}
    targets=set();yc=unit
    for c in range(6):targets.add((times(yc,qf),c));yc=times(yc,qy)
    hits=coset&targets
    results.append({'A':rec['A'],'beta':rec['beta'],'missing_coset':rec['missing_coset'],
                    'f_word_length':len(fw),'delta_2_image':[list(value[0]),value[1]],
                    'compatible_corrections':len(hits),'passes':bool(hits)})
out={'N':2,'target':'q(delta_2(f)) and c_2(f) mod6 in H x Z/6',
     'image_N_B_order':len(Nimage),'image_kernel_G6_order':len(Kimage),
     'tested_shadows':len(results),'pass_counts_by_CM_coset':{str(j):sum(r['passes'] and r['missing_coset']==bool(j) for r in results) for j in (0,1)},
     'scope':'Exact necessary test allowing corrections from ker(B->G6); it does not certify any full GT lift.',
     'records':results}
(here/'de_distribution_test.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
print('PASS: all finite images and coset-intersection tests computed exactly.')
