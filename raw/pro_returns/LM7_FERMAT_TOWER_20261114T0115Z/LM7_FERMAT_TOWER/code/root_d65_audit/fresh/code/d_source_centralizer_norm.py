#!/usr/bin/env python3
"""Literal finite maps used in the source-centralizer Tate comparison.

The arithmetic group above the order-46656 quotient has an odd kernel;
its coprime centralizer lifting and the integral Tate argument are proved
in the theorem. This program checks every finite centralizer coset and
both actual vertex-freeness claims, without replacing the full source.
"""
from pathlib import Path
from itertools import product
import json,hashlib,time
import numpy as np
OUT=Path(__file__).resolve().parent;start=time.time()
paths=[OUT/'d_arithmetic_A4_twisted.json',OUT/'d_arithmetic_affine_base.json']
D,A=[json.loads(p.read_text()) for p in paths]
T=np.array(D['Q_multiplication'],dtype=np.int16);to=A['Q_to_linear_image']
matrices=np.array([np.array(x,dtype=np.int16).T for x in A['Q_linear_image_matrices']],dtype=np.int16)
Q=np.array([matrices[j] for j in to],dtype=np.int16)
mi={tuple(x.ravel()):i for i,x in enumerate(matrices)}
Ts=np.array([[mi[tuple((x@y%3).ravel())] for y in matrices] for x in matrices],dtype=np.int16)
S,R=1,2;ss,rs=to[S],to[R];vr=np.array(A['affine_r_translation'],dtype=np.int16)
def inverse(table,g):return next(j for j in range(len(table)) if table[g,j]==0)
def conjugacy(table,g):return sorted({int(table[table[q,g],inverse(table,q)]) for q in range(len(table))})
def power(table,g,n):
 a=0
 for i in range(n):a=int(table[a,g])
 return a
C=[g for g in range(576) if T[g,S]==T[S,g]];Cs=[g for g in range(48) if Ts[g,ss]==Ts[ss,g]]
assert sorted({to[g] for g in C})==Cs
vectors=list(product(range(3),repeat=4));fix=[v for v in vectors if tuple(Q[S]@v%3)==v]
CD=[(q,v) for q in C for v in fix];CS=[(q,v) for q in Cs for v in fix]
projection={(to[q],v) for q,v in CD};assert projection==set(CS)
# The fixed s-vertices are literal right cosets of <s> in these
# centralizers; the projection of their augmentation kernels is onto.
def quotient_cosets(els,table,s):
 return sorted({min((q,v),(int(table[q,s]),v)) for q,v in els})
VD=quotient_cosets(CD,T,S);VS=quotient_cosets(CS,Ts,ss)
vsindex={x:i for i,x in enumerate(VS)}
vp=[vsindex[min((to[q],v),(int(Ts[to[q],ss]),v))] for q,v in VD]
assert set(vp)==set(range(len(VS)))
counts=[vp.count(i) for i in range(len(VS))];assert len(set(counts))==1
lift=[vp.index(i) for i in range(len(VS))]
# A literal basis e_i-e_0 is lifted to e_lift(i)-e_lift(0).
assert all(vp[lift[i]]==i and vp[lift[0]]==0 for i in range(1,len(VS)))
t=int(T[S,R]);ts=int(Ts[ss,rs]);involution=power(T,t,6);involution_star=power(Ts,ts,6)
sclass=conjugacy(T,S);istar=conjugacy(T,involution);small_sclass=conjugacy(Ts,ss);small_iclass=conjugacy(Ts,involution_star)
assert involution not in sclass and involution_star not in small_sclass
assert power(T,t,12)==0 and power(T,t,6)!=0
# The literal affine cusp word, with all twelve intermediate states.
q=0;v=np.zeros(4,dtype=np.int16);powers=[{'power':0,'q':0,'translation':v.tolist()}]
for j in range(1,13):
 q=int(T[q,S]);v=(v+Q[q]@vr)%3;q=int(T[q,R]);powers.append({'power':j,'q':q,'translation':v.tolist()})
assert q==0 and not np.any(v)
assert powers[6]['q']==314 and powers[6]['translation']==[0,2,1,0]
result={'summary':{'status':'PASS','Q_centralizer_order':len(C),'Qstar_centralizer_order':len(Cs),
 'Q_centralizer_projection_onto':True,'arithmetic_affine_fixed_vectors':len(fix),
 'Gdagger_centralizer_order':len(CD),'Gstar_centralizer_order':len(CS),
 'Gdagger_fixed_s_vertices':len(VD),'Gstar_fixed_s_vertices':len(VS),
 'fixed_vertex_projection_fibre_order':counts[0],
 'reduced_fixed_vertex_projection_rank':len(VS)-1,
 'actual_cusp_Sylow4_free_on_both_vertex_types':True,'elapsed_seconds':time.time()-start},
 'Q_centralizer_states':C,'Qstar_centralizer_states':Cs,'fixed_translation_vectors':[list(v) for v in fix],
 'source_fixed_vertices':[[q,list(v)] for q,v in VD],'target_fixed_vertices':[[q,list(v)] for q,v in VS],
 'fixed_vertex_projection':vp,'chosen_fixed_vertex_lifts':lift,
 'source_s_class':sclass,'source_cusp_involution_class':istar,
 'target_s_class':small_sclass,'target_cusp_involution_class':small_iclass,
 'literal_affine_cusp_powers':powers,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_source_centralizer_norm.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
