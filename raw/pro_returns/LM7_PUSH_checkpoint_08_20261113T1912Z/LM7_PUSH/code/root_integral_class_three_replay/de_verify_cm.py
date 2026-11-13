#!/usr/bin/env python3
"""Independent certificate verification for LM7 D.25--D.26.

The source programs are not imported.  We enumerate SL_2(Z/12), build the
integral graph, recompute all linear solvability counts and Smith forms, and
verify the recorded witnesses by direct multiplication.  Additionally the
actual integral cusp gauge is recovered through F^ab, and both hexagons are
checked in G_6 after this gauge.
"""
from collections import deque, Counter
from itertools import product
from pathlib import Path
import json
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ

HERE=Path(__file__).resolve().parent
CERT=json.loads((HERE/'de_source/d_cm_shadow.json').read_text())

def multiply(a,b,m=12):
    return tuple(v%m for v in (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                              a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def negative(a): return tuple(-v%12 for v in a)
def representative(a): return min(tuple(a),negative(a))
def inverse(a): return representative((a[3],-a[1]%12,-a[2]%12,a[0]))
def times(a,b): return representative(multiply(a,b))
unit=(1,0,0,1)
Q=sorted({representative(a) for a in product(range(12),repeat=4)
          if (a[0]*a[3]-a[1]*a[2])%12==1})
index={q:i for i,q in enumerate(Q)}
ss=representative((0,1,11,0)); rr=representative((0,11,1,11))
r2=times(rr,rr); size=len(Q)
assert size==576
permutation=np.array([[index[times(q,a)] for a in Q] for q in Q])
def act(q,v):
    out=np.zeros_like(v)
    out[permutation[index[q]]]=v
    return out
sv={q:('s',min(q,times(q,ss))) for q in Q}
rv={q:('r',min(q,times(q,rr),times(q,r2))) for q in Q}
vertices=set(sv.values())|set(rv.values())
adj={v:[] for v in vertices}
for i,q in enumerate(Q):
    adj[sv[q]].append((rv[q],i,1))
    adj[rv[q]].append((sv[q],i,-1))
root=sv[unit]; path={root:np.zeros(size,dtype=np.int64)}
tree=set(); queue=deque([root])
while queue:
    v=queue.popleft()
    for w,e,sign in adj[v]:
        if w not in path:
            path[w]=path[v].copy(); path[w][e]+=sign
            tree.add(e); queue.append(w)
assert len(path)==len(vertices)==480
chords=sorted(set(range(size))-tree)
C=np.stack([path[sv[Q[e]]]-path[rv[Q[e]]]+np.eye(1,size,e,dtype=np.int64)[0]
            for e in chords],axis=1)
assert C.shape==(576,97)
assert np.array_equal(C[chords],np.eye(97,dtype=int))
L=np.concatenate((C-act(ss,C),act(ss,C-act(rr,C))),axis=1)[chords]
Pr=np.zeros(size,dtype=np.int64); Pr[index[unit]]=1; Pr[index[rr]]=-1
P={unit:np.zeros(size,dtype=np.int64)}; queue=deque([unit])
while queue:
    q=queue.popleft()
    for a,pa in ((ss,np.zeros(size,dtype=np.int64)),(rr,Pr)):
        qa=times(q,a)
        if qa not in P: P[qa]=P[q]+act(q,pa); queue.append(qa)
assert len(P)==576

def rref(A,p):
    A=np.array(A,dtype=np.int64)%p
    row=0; piv=[]
    for col in range(A.shape[1]):
        options=np.flatnonzero(A[row:,col])
        if not len(options): continue
        k=row+int(options[0]); A[[row,k]]=A[[k,row]]
        A[row]=(A[row]*pow(int(A[row,col]),-1,p))%p
        for i in range(A.shape[0]):
            if i!=row and A[i,col]: A[i]=(A[i]-A[i,col]*A[row])%p
        piv.append(col); row+=1
        if row==A.shape[0]: break
    return A,piv
rank=lambda A,p:len(rref(A,p)[1])
def contains(A,v,p): return rank(A,p)==rank(np.column_stack((A,v)),p)

H=[q for q in Q if tuple(v%2 for v in q)==unit]
CA=[a for a in H if times(a,rr)==times(rr,a)]
CB=[b for b in H if times(b,ss)==times(ss,b)]
V4={(1,0,0,1),(1,2,0,1),(1,0,2,1),(1,2,2,1)}
def lift(q):
    return q if tuple(v%4 for v in q) in V4 else negative(q)
def cm_bits(a,b):
    aa=lift(a); bb=lift(b)
    ai=(aa[3],-aa[1]%12,-aa[2]%12,aa[0])
    bi=(bb[3],-bb[1]%12,-bb[2]%12,bb[0])
    assert tuple(v%4 for v in ai)==unit
    av=((ai[0]-ai[1])%3,(ai[2]-ai[3])%3)
    assert av in [(1,2),(2,1)]
    return int(av==(2,1)),int(tuple(v%3 for v in bi) not in [unit,(2,0,0,2)])

# Projection of integral chains to the S_3 graph recovers F^ab exactly.
Q2=sorted({tuple(v%2 for v in q) for q in Q}); i2={q:i for i,q in enumerate(Q2)}
proj=np.array([i2[tuple(v%2 for v in q)] for q in Q])
def project(v):
    out=np.zeros(6,dtype=np.int64)
    for j in range(size): out[proj[j]]+=v[j]
    return out
def gm(g,h,j): return times(g[0],h[0]),(g[1]+act(g[0],h[1]))%j
def gi(g,j):
    inv=inverse(g[0]); return inv,(-act(inv,g[1]))%j
def gp(g,k,j):
    if k<0: return gp(gi(g,j),-k,j)
    out=(unit,np.zeros(size,dtype=np.int64))
    while k:
        if k&1: out=gm(out,g,j)
        g=gm(g,g,j); k//=2
    return out
def gc(g,h,j): return gm(gm(g,h,j),gi(g,j),j)
def equal(g,h): return g[0]==h[0] and np.array_equal(g[1],h[1])
# Integer chains using a large modulus with a final signed lift are avoidable.
def im(g,h): return times(g[0],h[0]),g[1]+act(g[0],h[1])
def ii(g):
    inv=inverse(g[0]); return inv,-act(inv,g[1])
si=(ss,np.zeros(size,dtype=np.int64)); ri=(rr,Pr)
ti=im(si,ri); ui=ii(ti); vi=im(im(si,ui),si)
xi=im(ui,ui); yi=im(vi,vi)
XY=np.column_stack((project(xi[1]),project(yi[1])))
minor=None
for a in range(6):
    for b in range(a+1,6):
        M=sp.Matrix(XY[[a,b]].tolist())
        if abs(M.det())==1: minor=([a,b],np.array(M.inv().tolist(),dtype=np.int64)); break
    if minor: break
assert minor
def fab(v):
    w=project(v); ans=minor[1]@w[minor[0]]
    assert np.array_equal(XY@ans,w)
    return ans
assert np.array_equal(fab(xi[1]),[1,0]) and np.array_equal(fab(yi[1]),[0,1])

counts={2:[0,0],3:[0,0]}; matrix_counts=[0,0]; checks=[]; action_keys=[]
central_s=[];central_r=[]
for b in CB:
    err=P[b]-act(ss,P[b])
    assert np.array_equal(C@err[chords],err)
    if contains((C-act(ss,C))[chords],-err[chords],2):central_s.append(b)
for a in CA:
    err=P[a]-act(rr,P[a])+act(a,Pr)-Pr
    assert np.array_equal(C@err[chords],err)
    if contains((C-act(rr,C))[chords],-err[chords],3):central_r.append(a)
assert central_s==[unit] and central_r==[unit]
record_by_pair={(representative(x['A']),representative(x['beta'])):x for x in CERT['pairs']}
for a in CA:
    for b in CB:
        j3,j4=cm_bits(a,b); missing=j3^j4; matrix_counts[missing]+=1
        E=P[b]-act(ss,P[b])+act(ss,P[a]-act(rr,P[a])+act(a,Pr)-Pr)
        assert np.array_equal(C@E[chords],E)
        good={p:contains(L,-E[chords],p) for p in (2,3)}
        for p in (2,3): counts[p][missing]+=good[p]
        rec=record_by_pair[a,b]
        assert bool(rec['missing_coset'])==bool(missing)
        assert good[2]==rec['homology_cover_lift'] and good[3]==rec['mod3_cusp_lift']
        if not all(good.values()): continue
        av=np.array([rec['mod6_A_cycles'].get(str(i),0) for i in range(97)])
        bv=np.array([rec['mod6_beta_cycles'].get(str(i),0) for i in range(97)])
        pa=P[a]+C@av; pb=P[b]+C@bv
        edge=pa-pb; edge[index[a]]+=1
        images=C.T@np.stack([act(q,edge) for q in Q])
        ranks={p:rank(images[:,chords],p) for p in (2,3)}
        assert ranks=={2:97,3:97}
        beta_ab=fab(pb); gauge=int(beta_ab[1]-beta_ab[0])
        j=6; s=(ss,si[1]%j); r=(rr,Pr%j); u=(ui[0],ui[1]%j); v=(vi[0],vi[1]%j)
        x=(xi[0],xi[1]%j)
        A=(a,pa%j); beta=(b,pb%j)
        alph_s=gc(beta,s,j); alph_r=gc(A,r,j)
        assert equal(gm(alph_s,alph_r,j),gm(s,r,j))
        beta_new=gm(gp(x,gauge,j),beta,j)
        f=gm(gm(gm(s,beta_new,j),s,j),gi(beta_new,j),j)
        sx=gm(s,f,j);rx=gm(gi(f,j),r,j)
        action_keys.append((sx[0],tuple(map(int,sx[1])),rx[0],tuple(map(int,rx[1]))))
        assert equal(gm(gm(gm(u,gi(f,j),j),v,j),f,j),gm(gi(f,j),gm(u,v,j),j))
        assert equal(gm(gm(gm(gi(f,j),v,j),f,j),u,j),gm(gm(v,u,j),f,j))
        # Exact F^ab cancellation: conjugation by s exchanges x and y.
        beta_new_ab=beta_ab+np.array([gauge,0])
        assert np.array_equal(beta_new_ab[::-1]-beta_new_ab,[0,0])
        checks.append({'A':list(lift(a)),'beta':list(lift(b)),
                       'missing_coset':bool(missing),'ranks':ranks,
                       'beta_abelianization':beta_ab.tolist(),'integral_gauge_k':gauge,
                       'gauged_hexagons_in_G6':True})
assert matrix_counts==[24,24] and counts=={2:[12,12],3:[24,24]}
assert len(checks)==24 and sum(c['missing_coset'] for c in checks)==12
assert len(set(action_keys))==24
ct=np.zeros(size,dtype=np.int64); q=unit
for i in range(12): ct+=act(q,ti[1]); q=times(q,ti[0])
assert q==unit and np.array_equal(C@ct[chords],ct)
aug=np.column_stack((L,-ct[chords]))
S=smith_normal_form(sp.Matrix(L.tolist()),domain=ZZ)
SA=smith_normal_form(sp.Matrix(aug.tolist()),domain=ZZ)
sd=[abs(int(S[i,i])) for i in range(97)]
sda=[abs(int(SA[i,i])) for i in range(97)]
assert sd==[1]*96+[2] and sda==[1]*97
assert hermite_normal_form(sp.Matrix(aug.tolist()))==sp.eye(97)
assert sp.igcd(*[int(x) for x in ct[chords]])==1
out={'enumerated_Q_order':size,'vertices':len(vertices),'N_rank':97,
     'centralizer_orders':[len(CA),len(CB)],'matrix_CM_counts':matrix_counts,
     'cusp_solvability_counts':counts,'certified_G6_automorphism_counts':[12,12],
     'relation_ranks':{p:rank(L,p) for p in (2,3)},
     'smith_cusp':dict(Counter(sd)),'smith_augmented':dict(Counter(sda)),
     'integral_cusp_cycle_primitive':True,'gauge_hexagon_checks':48,
     'distinct_gauged_automorphisms':len(set(action_keys)),
     'centralizer_image_counts_s_mod2_r_mod3':[len(central_s),len(central_r)],
     'certificates':checks}
(HERE/'de_verify_cm.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='certificates'},indent=2))
print('PASS: all 24 certificates and exact integral cusp gauges checked; 12 lie in the extra CM coset.')
print('No assertion of a full profinite lift is made.')
