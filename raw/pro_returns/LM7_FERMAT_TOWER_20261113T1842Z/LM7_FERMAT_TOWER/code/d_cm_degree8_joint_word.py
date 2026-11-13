#!/usr/bin/env python3
"""Evaluate the complete joint replacement words in both full finite models."""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import chain
import io,runpy,json,time
import numpy as np
import d_cm_degree8_magnus as G
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
from d_cm_degree8_reconstruct import joint_words
J=joint_words(R)
beta,A,bc,ac,lam=(J[k] for k in ('beta','A','beta_correction','A_correction','lambda'))
def inviter(w):return (0 if a==0 else 3-a for a in reversed(w))
def cusp():return chain(beta,[0],inviter(beta),A,[1],inviter(A),[2,0]*lam)
length=2*(len(beta)+len(A))+2+2*lam
print('Complete corrected cusp:',length,'B letters; lambda',lam,flush=True)
q,kw=R['collapse'](cusp());assert q==R['e']
print('Exact freely reduced K word:',len(kw),flush=True)
P=R['poly'](kw,8);assert all(not p.any() for p in P[1:])
print('PASS: complete rank-four Magnus degrees one through eight.',flush=True)

# Independently collapse the full same word into the 97-generator N graph.
ch={j:i for i,j in enumerate(R['chN'])};q=R['one'];nw=[]
def add(edge,sign):
    i=ch.get(edge)
    if i is None:return
    a=sign*(i+1)
    if nw and nw[-1]==-a:nw.pop()
    else:nw.append(a)
for a in cusp():
    if a==0:q=R['qm'](q,R['qs'])
    else:
        qq=R['qm'](q,R['qr'] if a==1 else R['qr2'])
        add(R['ixQ'][q],1);add(R['ixQ'][qq],-1);q=qq
assert q==R['one']
v=np.zeros(97,dtype=np.int16);w=np.zeros((97,97),dtype=np.int16)
for a in nw:
    i=abs(a)-1;sgn=1 if a>0 else -1
    w[:,i]=(w[:,i]+sgn*v)%4
    if sgn<0:w[i,i]=(w[i,i]+1)%4
    v[i]=(v[i]+sgn)%4
assert not np.any(v) and not np.any(w)
print('PASS: complete rank-97 Z/4 Magnus identity;',len(nw),'N letters.',flush=True)

# The lower action is explicitly replaced, not carried through unchanged.
q,cw=R['collapse'](bc);assert q==R['e'];CP=R['poly'](cw,7)
b=(0,)+tuple(R['bitpoly'](CP[i]) if i<=7 else 0 for i in range(1,9))
kvals=json.loads((OUT/'d_cm_degree8_gamma3.json').read_text())['actual_S_inner_factor_degrees2_3']
k=(0,0,int(kvals[0],16),int(kvals[1],16))+ (0,)*5
sb=G.mul(G.mul(k,G.involution(b)),G.inverse(k));diff=G.mul(b,G.inverse(sb))
first=next((n for n in range(1,8) if diff[n]),None);assert first is not None
summary={'complete_corrected_B_cusp_word_length':length,'K_cusp_word_length':len(kw),
 'N_cusp_word_length':len(nw),'lambda':lam,
 'full_K_Magnus_degrees_one_through_eight_zero':True,'full_N_Z4_Magnus_identity':True,
 's_action_first_differs_from_recorded_D31_in_degree':first,
 'same_N_Frattini_action_and_CM_pair':True,
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_degree8_joint_word.json').write_text(json.dumps({'summary':summary,
 's_action_difference_through_degree7':[hex(diff[n]) for n in range(1,8)]},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
