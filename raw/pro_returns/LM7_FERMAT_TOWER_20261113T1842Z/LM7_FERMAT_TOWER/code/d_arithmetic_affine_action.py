#!/usr/bin/env python3
"""The actual normalized arithmetic action on the marked order-3888 quotient.

The source and the parameter are the actual quotient of G3 certified by
d_arithmetic_affine_base.py.  No order-1080 surrogate enters this calculation.
All matrix columns and all state maps are retained.
"""
from pathlib import Path
from itertools import product
from collections import deque
import json,time

OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_affine_base.json').read_text())
M=[tuple(map(tuple,x)) for x in D['Q_linear_image_matrices']]
mi={a:i for i,a in enumerate(M)}
S=tuple(map(tuple,D['quotient_s_columns']))
R=tuple(map(tuple,D['quotient_r_columns']))
I=tuple(tuple(int(i==j) for i in range(4)) for j in range(4))
Z=(0,0,0,0)
vectors=list(product(range(3),repeat=4));vi={a:i for i,a in enumerate(vectors)}
def mv(A,v):return tuple(sum(v[j]*A[j][i] for j in range(4))%3 for i in range(4))
def mm(A,B):return tuple(mv(A,c) for c in B)
def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def neg(a):return tuple(-x%3 for x in a)
mt=[[mi[mm(a,b)] for b in M] for a in M]
ma=[[vi[mv(a,b)] for b in vectors] for a in M]
va=[[vi[add(a,b)] for b in vectors] for a in vectors]
def gm(a,b):
    aq,av=divmod(a,81);bq,bv=divmod(b,81)
    return 81*mt[aq][bq]+va[av][ma[aq][bv]]
invM=[next(j for j in range(48) if mt[i][j]==0) for i in range(48)]
def inverse(a):
    q,v=divmod(a,81);qi=invM[q]
    return 81*qi+vi[neg(mv(M[qi],vectors[v]))]
def power(a,k):
    out=0
    while k:
        if k&1:out=gm(out,a)
        a=gm(a,a);k//=2
    return out
s=81*mi[S]+vi[tuple(D['affine_s_translation'])]
r=81*mi[R]+vi[tuple(D['affine_r_translation'])]
t=gm(s,r);assert power(t,12)==0 and power(t,6)!=0
assert len(D['actual_parameter_s_r_candidates'])==1
av=tuple(D['actual_parameter_s_r_candidates'][0]);a=vi[av]
s_h=gm(s,a);r_h=gm(inverse(a),r)
assert gm(s_h,s_h)==0 and power(r_h,3)==0 and gm(s_h,r_h)==t

# The literal generator images determine a map on all3888 source states.
words={0:[]};image={0:0};queue=deque([0]);edge_checks=0
while queue:
    g=queue.popleft()
    for token,q,qh in [(0,s,s_h),(1,r,r_h)]:
        h=gm(g,q);ih=gm(image[g],qh)
        if h not in image:
            image[h]=ih;words[h]=words[g]+[token];queue.append(h)
        else:assert image[h]==ih
        edge_checks+=1
assert len(image)==3888 and len(set(image.values()))==3888
k=power(t,6);ki=inverse(k)
assert k==81*mi[tuple(tuple(-x%3 for x in c) for c in I)]+vi[(0,2,1,0)]
assert all(image[g]==gm(gm(k,g),ki) for g in range(3888))
T=[vectors[image[vi[tuple(int(i==j) for i in range(4))]]] for j in range(4)]
assert T==[tuple(-int(i==j)%3 for i in range(4)) for j in range(4)]

# Exact centralizers, with their actual affine, linear and translation maps.
def centralizer(q):return [g for g in range(3888) if gm(g,q)==gm(q,g)]
cs=centralizer(s);cr=centralizer(r);ct=centralizer(t)
assert len(ct)==12 and set(ct)=={power(t,j) for j in range(12)}
left_r_conjugators=[g for g in range(3888)
                   if gm(gm(inverse(g),r),g)==r_h]
left_s_conjugators=[g for g in range(3888)
                   if gm(gm(inverse(g),s),g)==s_h]
assert len(left_r_conjugators)==len(cr) and len(left_s_conjugators)==len(cs)
minusI=mi[tuple(tuple(-x%3 for x in c) for c in I)]
r_over_minusI=[g for g in left_r_conjugators if g//81==minusI]
assert len(r_over_minusI)==9

# Compute the exact endomorphism ring of the actual F3^4 module.
eq=[]
for H in (S,R):
    for i in range(4):
        for j in range(4):
            row=[0]*16
            for q in range(4):
                row[i*4+q]=(row[i*4+q]+H[j][q])%3
                row[q*4+j]=(row[q*4+j]-H[q][i])%3
            eq.append(row)
bas={}
for row in eq:
    row=row[:]
    while any(row):
        p=max(i for i,a0 in enumerate(row) if a0)
        if p not in bas:
            iv=pow(row[p],-1,3);bas[p]=[x*iv%3 for x in row];break
        q=row[p];row=[(x-q*y)%3 for x,y in zip(row,bas[p])]
free=[j for j in range(16) if j not in bas];nb=[]
for f in free:
    v=[0]*16;v[f]=1
    for p in sorted(bas):v[p]=-sum(x*y for j,(x,y) in enumerate(zip(bas[p],v)) if j!=p)%3
    assert all(sum(x*y for x,y in zip(row,v))%3==0 for row in eq);nb.append(v)
assert len(nb)==2
endo=[]
for ab in product(range(3),repeat=2):
    v=[sum(ab[j]*nb[j][i] for j in range(2))%3 for i in range(16)]
    mat=tuple(tuple(v[i*4+j] for i in range(4)) for j in range(4))
    assert mm(mat,S)==mm(S,mat) and mm(mat,R)==mm(R,mat);endo.append(mat)
zero=tuple(Z for j in range(4))
assert all(any(mm(a0,b)==I for b in endo) for a0 in endo if a0!=zero)
roots=[A for A in endo if mm(A,A)==M[minusI]]
assert len(roots)==2

# Actual stabilizers of the40 order-three character pairs.
def normalize(v):
    f=next(x for x in v if x)
    return tuple(x*pow(f,-1,3)%3 for x in v)
lines={normalize(v) for v in vectors if any(v)}
orbits=[];stabilizers=[]
while lines:
    v=min(lines)
    orbit=sorted({normalize(tuple(sum(v[i]*col[i] for i in range(4))%3 for col in A))
                  for A in M})
    stab=[i for i,A in enumerate(M)
          if normalize(tuple(sum(v[j]*col[j] for j in range(4))%3 for col in A))==v]
    assert len(orbit)*len(stab)==48
    orbits.append(orbit);stabilizers.append(stab);lines-=set(orbit)
assert [len(x) for x in orbits]==[8,12,12,8]
center=[i for i in range(48) if all(mt[i][j]==mt[j][i] for j in range(48))]
assert len(center)==4
derived={0};comm=[]
for i in range(48):
    for j in range(48):
        c=mt[mt[mt[i][j]][invM[i]]][invM[j]]
        if c not in comm:comm.append(c)
todo=[0]
for g in todo:
    for h in comm:
        a0=mt[g][h]
        if a0 not in derived:derived.add(a0);todo.append(a0)
assert len(derived)==8
# The order48 linear group has derived subgroup Q8 and quotient C6.
assert {mt[i][i] for i in derived if i not in (0,minusI)}=={minusI}
assert set(center)&derived=={0,minusI}
summary={
 'scope':'The genuine normalized arithmetic parameter and action on the actual G3 quotient.',
 'quotient_order':3888,'actual_parameter':list(av),
 'actual_action_cayley_edges_checked':edge_checks,
 'actual_action_is_automorphism':True,
 'actual_action_is_conjugation_by_cusp_sixth_power':True,
 'actual_action_on_translation_module':'minus identity',
 'cusp_sixth_power_translation':[0,2,1,0],
 's_centralizer_order':len(cs),'r_centralizer_order':len(cr),
 't_centralizer_order':len(ct),
 'r_conjugator_lifts_over_minus_identity':len(r_over_minusI),
 'module_endomorphism_ring_order':len(endo),'module_endomorphism_ring_is_field':True,
 'linear_group_center_order':len(center),'linear_group_derived_order':len(derived),
 'dual_character_pair_orbits':[len(x) for x in orbits],
 'dual_character_pair_stabilizers':[len(x) for x in stabilizers],
 'elapsed_seconds':round(time.time()-started,3)}
cert={
 'summary':summary,'actual_action_all_states':[image[g] for g in range(3888)],
 'actual_action_translation_columns':T,
 'cusp_sixth_power_state':k,
 's_centralizer_states':cs,'r_centralizer_states':cr,'t_centralizer_states':ct,
 'all_r_conjugators_over_minus_identity':r_over_minusI,
 'all_s_conjugator_states':left_s_conjugators,
 'all_r_conjugator_states':left_r_conjugators,
 'module_endomorphism_field_matrices':endo,'square_roots_of_minus_identity':roots,
 'linear_center_states':center,'linear_derived_states':sorted(derived),
 'all_dual_character_pair_orbits':orbits,'all_dual_character_pair_stabilizers':stabilizers}
(OUT/'d_arithmetic_affine_action.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
