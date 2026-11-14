#!/usr/bin/env python3
"""Exact Q0 dessin, peripheral maps, and elliptic homology comparison."""
from pathlib import Path
from contextlib import redirect_stdout
from collections import deque
from itertools import combinations,product
import io,runpy,json,time
import numpy as np
import sympy as sp
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
Q,m,e,s,r=(R[k] for k in ('Q0','m0','e','s','r'));rr=m(r,r);t=m(s,r)
ix={q:i for i,q in enumerate(Q)}
reps={e:[]};queue=deque([e])
while queue:
    q=queue.popleft()
    for a,g in ((0,s),(1,r)):
        qq=m(q,g)
        if qq not in reps:reps[qq]=reps[q]+[a];queue.append(qq)
def inv(w):return [0 if a==0 else 3-a for a in reversed(w)]
def reduceB(w):
    ans=[]
    for a in w:
        if ans and (ans[-1]==0)==(a==0):
            last=ans.pop()
            if a!=0 and (last+a)%3:ans.append((last+a)%3)
        else:ans.append(a)
    return ans
def cycles(g):
    seen=set();out=[]
    for q in Q:
        if q in seen:continue
        cc=[];qq=q
        while qq not in seen:seen.add(qq);cc.append(ix[qq]);qq=m(qq,g)
        out.append(cc)
    return out
cs,cr,ct=cycles(s),cycles(r),cycles(t)
assert sorted(map(len,cs))==[2]*9 and sorted(map(len,cr))==[3]*6 and sorted(map(len,ct))==[6]*3
assert 9+6-18+3==0

def pc(a,b):return tuple(a[b[i]] for i in range(3))
ps=(1,0,2);pr=(1,2,0);pid=(0,1,2)
eps={};perms={}
for q,w in reps.items():
    a=0;p=pid
    for x in w:
        if x==0:p=pc(p,ps)
        else:a=(a+x)%3;p=pc(p,pr if x==1 else pc(pr,pr))
    eps[q]=a;perms[q]=p
assert len({(eps[q],perms[q]) for q in Q})==18
for a,b in product(Q,repeat=2):
    assert eps[m(a,b)]==(eps[a]+eps[b])%3
    assert perms[m(a,b)]==pc(perms[a],perms[b])
tp=[];q=e
while q not in tp:tp.append(q);q=m(q,t)
assert len(tp)==6
cusp_reps=[e]
for q in Q:
    if all(perms[q][0]!=perms[c][0] for c in cusp_reps):cusp_reps.append(q)
assert len(cusp_reps)==3
cw=[reps[q]+[0,1]*6+inv(reps[q]) for q in cusp_reps]
Kc=[];Cv=[]
for w in cw:
    q,kw=R['collapse'](w);assert q==e;Kc.append(kw)
    v=np.array([sum((1 if a>0 else -1) for a in kw if abs(a)==j+1) for j in range(4)],dtype=np.int64)
    Cv.append(v)
assert np.array_equal(sum(Cv),np.zeros(4,dtype=np.int64))
M={}
for q in Q:
    a=np.zeros_like(R['C']);a[[ix[m(q,x)] for x in Q]]=R['C']
    M[q]=a[R['chords']].astype(np.int64)
assert len({tuple((M[q]%2).ravel()) for q in Q})==18
v0=Cv[0]%2;assert v0.tolist()==[1,1,0,1]
stab=[q for q in Q if np.array_equal(M[q]@v0%2,v0)]
assert set(stab)==set(tp)

# Every deck transformation and every cusp has its actual K-conjugator.
boundary=[]
for h in Q:
    for i,q in enumerate(cusp_reps):
        hq=m(h,q);j=next(j for j,c in enumerate(cusp_reps) if perms[c][0]==perms[hq][0])
        power=next(a for a,u in enumerate(tp) if m(cusp_reps[j],u)==hq)
        k=reps[h]+reps[q]+[2,0]*power+inv(reps[cusp_reps[j]])
        qk,kw=R['collapse'](k);assert qk==e
        lhs=reps[h]+cw[i]+inv(reps[h])
        rhs=k+cw[j]+inv(k)
        assert not reduceB(lhs+inv(rhs))
        boundary.append({'q_index':ix[h],'cusp_from':i,'cusp_to':j,'t_power':power,'K_conjugator':kw})
assert len(boundary)==54

# The section cocycle specifies the exact outer Q0 action on K.
cocycles=[]
for a,b in product(Q,repeat=2):
    k=reps[a]+reps[b]+inv(reps[m(a,b)])
    q,kw=R['collapse'](k);assert q==e
    for g in R['Kwords']:
        lhs=reps[a]+reps[b]+g+inv(reps[b])+inv(reps[a])
        rhs=k+reps[m(a,b)]+g+inv(reps[m(a,b)])+inv(k)
        assert not reduceB(lhs+inv(rhs))
    cocycles.append({'left':ix[a],'right':ix[b],'K_word':kw})

# Integral filling map onto the compact elliptic homology lattice.
C=np.stack(Cv[:2],axis=1);chosen=None
for i,j in combinations(range(4),2):
    B=np.column_stack([C,np.eye(4,dtype=np.int64)[:,i],np.eye(4,dtype=np.int64)[:,j]])
    if abs(int(sp.Matrix(B).det()))==1:chosen=B;break
assert chosen is not None
Bi=np.array(sp.Matrix(chosen).inv(),dtype=np.int64)
P=Bi[2:];J=chosen[:,2:]
assert np.array_equal(P@J,np.eye(2,dtype=np.int64))
EM={q:P@M[q]@J for q in Q}
for q in Q:assert not np.any(P@M[q]@C)
assert np.array_equal(EM[s],-np.eye(2,dtype=np.int64))
zq=m(t,t);Z=EM[zq];assert np.array_equal(Z@Z+Z+np.eye(2,dtype=np.int64),np.zeros((2,2),dtype=np.int64))
assert sum(np.array_equal(EM[q],np.eye(2,dtype=np.int64)) for q in Q)==3
projector=np.eye(4,dtype=np.int64)+M[zq]+M[m(zq,zq)]
assert not np.any(projector@projector-3*projector)
assert np.array_equal(projector@C,3*C)
assert not np.any(P@projector)

# Actual D33 action on H1(K,Z/16), which T3 retains completely.
from d_cm_degree8_reconstruct import joint_words
W=joint_words(R)
def ab(word):
    q,ww=R['collapse'](word);assert q==e
    return np.array([sum((1 if a>0 else -1) for a in ww if abs(a)==j+1) for j in range(4)],dtype=np.int64)
vb=ab(W['beta']);va=ab(W['A'])
deltas={0:(np.eye(4,dtype=np.int64)-M[s])@vb,
        1:(np.eye(4,dtype=np.int64)-M[r])@va,
        2:(np.eye(4,dtype=np.int64)-M[rr])@va}
AM=np.eye(4,dtype=np.int64)
for i,w in enumerate(R['Kwords']):
    q=e
    for letter in w:
        AM[:,i]+=M[q]@deltas[letter]
        q=m(q,s if letter==0 else r if letter==1 else rr)
    assert q==e
AM%=16
for q in Q:assert not np.any((AM@M[q]-M[q]@AM)%16)
assert not np.any((AM@C-C)%16)
EA=P@AM@J%16
assert int(sp.Matrix(EA).det())%16==1
coeff=next((a,b) for a,b in product(range(16),repeat=2) if not np.any((a*np.eye(2,dtype=np.int64)+b*Z-EA)%16))
assert (coeff[0]**2-coeff[0]*coeff[1]+coeff[1]**2)%16==1

# The explicit algebraic cyclic cover and its six base transformations.
zz=sp.symbols('z')
def compose(a,b):return (sp.cancel(a[0].subs(zz,b[0])),sp.cancel(a[1].subs(zz,b[0])*b[1]))
I=(zz,sp.Integer(1));S=(1-zz,sp.Integer(1));R0=(1/(1-zz),-1/(1-zz))
def same(a,b):return all(sp.cancel(x-y)==0 for x,y in zip(a,b))
assert same(compose(S,S),I) and same(compose(compose(R0,R0),R0),I)
assert same(compose(compose(S,R0),compose(S,R0)),I)
for f,g in (S,R0):assert sp.cancel(g**3*zz*(zz-1)-f*(f-1))==0
beta=4*(zz**2-zz+1)**3/(27*zz**2*(1-zz)**2)
for f,g in (S,R0):assert sp.cancel(beta.subs(zz,f)-beta)==0
xx=sp.symbols('x')
u=sp.symbols('u')
assert sp.expand((u+4)**3-27*u*u)==sp.expand((u-8)**2*(u+1))

summary={'Q0_order':18,'s_cycle_lengths':[len(c) for c in cs],
 'r_cycle_lengths':[len(c) for c in cr],'cusp_cycle_lengths':[len(c) for c in ct],
 'compact_genus':1,'punctures':3,'cusp_width':6,
 'faithful_Q0_homology_matrices_mod2':18,
 't6_homology_vector':Cv[0].tolist(),'t6_vector_stabilizer_order':len(stab),
 'stabilizer_equals_t_image':True,'exact_cusp_conjugacies_checked':54,
 'exact_outer_action_cocycle_checks':18*18*4,
 'elliptic_homology_kernel_order_in_Q0':3,
 'central_order3_elliptic_matrix':Z.tolist(),
 'D33_elliptic_Tate16_matrix':EA.tolist(),
 'D33_CM_coefficients_a_b_mod16':list(coeff),
 'D33_CM_norm_mod16':1,
 'cyclic_cover':'w^3=z(z-1)',
 'compact_elliptic_map':'(x,y)=(4^(1/3) w,2z-1)',
 'Belyi_map_on_y2_x3_plus1':'(x^3+4)^3/(27*x^6)',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_rank4_structure.json').write_text(json.dumps({'summary':summary,
 'Q0_elements':Q,'Q0_B_section_words':[reps[q] for q in Q],
 'Q0_to_S3_times_C3':[{'permutation':perms[q],'C3_exponent':eps[q]} for q in Q],
 'cusp_representatives':[ix[q] for q in cusp_reps],
 'cusp_lambda_values':[('0','1','infinity')[perms[q][0]] for q in cusp_reps],
 'cusp_K_words':Kc,'boundary_maps':boundary,'section_cocycles':cocycles,
 'K_homology_matrices':[M[q].tolist() for q in Q],
 'cusp_lattice_basis':C.tolist(),'compact_filling_matrix':P.tolist(),
 'compact_lattice_section':J.tolist(),'D33_K_homology_mod16':AM.tolist()},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
