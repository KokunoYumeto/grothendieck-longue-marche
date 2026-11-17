#!/usr/bin/env python3
"""Literal marked identities for the isolated full-boundary corner."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
def red(w,cones=()):
    s=[]
    for x in w:
        x=abs(x) if abs(x) in cones else x
        if s and (s[-1]==-x or x in cones and s[-1]==x):s.pop()
        else:s.append(x)
    return tuple(s)
def inv(w):return tuple(-x for x in reversed(w))
def cat(*ws,cones=()):return red((x for w in ws for x in w),cones)
def sub(w,A):return red(x for j in w for x in(A[j] if j>0 else inv(A[-j])))
def comm(x,y,cones=()):return cat(x,y,inv(x),inv(y),cones=cones)
# Corner labels D=1, j=2, u=3, k=4; D and j are involutions.
D=(1,);j=(2,);u=(3,);k=(4,);cones=(1,2)
c=cat(j,D,j,cones=cones);T=cat(u,D,cones=cones)
boundary=cat(c,T,cones=cones)
rP=cat(j,boundary,j,boundary,cones=cones)
rU=cat(j,u,j,u,cones=cones)
assert rP==cat(D,rU,D,cones=cones)
rKT=comm(k,T,cones=cones)
rKU=comm(k,u,cones=cones);rKD=comm(k,D,cones=cones)
assert rKT==cat(rKU,u,rKD,inv(u),cones=cones)

e_path=P/'annular_neck_reflection23.json';E=json.loads(e_path.read_text())
eta={int(i):tuple(w) for i,w in E['eta_adapted_K_basis_a_barb_d_e_f'].items()}
P5=(1,2,5,3,4) # a B f d e, actual full ordinary boundary.
assert sub(P5,eta)==inv(P5)
t=(1,5,-1) # actual branch normalizer a f a^-1, distinct from full boundary.
etat=sub(t,eta)
assert etat!=inv(t)
assert comm(t,etat)
out={'status':'PASS_LITERAL_CORNER_IDENTITIES',
 'eta_input_sha256':hashlib.sha256(e_path.read_bytes()).hexdigest(),
 'corner_labels':{'1':'D=reflected cone','2':'j','3':'u','4':'k'},
 'selected_cone_c':c,'full_boundary_T':T,'ordinary_boundary_P5':boundary,
 'mirror_relator_equals_D_conjugate':{'jP5j_times_P5':rP,'j_u_j_times_u':rU},
 'base_relator_factorization':{'k_T_commutator':rKT,'k_u_commutator':rKU,'k_D_commutator':rKD},
 'actual_K_P5':P5,'eta_P5':sub(P5,eta),
 'branch_normalizer_t':t,'eta_branch_normalizer_t':etat,
 'nonzero_free_commutator_t_eta_t':comm(t,etat),
 'scope':'Literal identities for an auxiliary corner of the full presentation. Remaining regional and four mirror relations are not discarded; no post-filling injection claim.'}
(P/'boundary_corner24.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual eta(P5)=P5^-1.')
print('PASS mirror relator is the D-conjugate of juj*u.')
print('PASS [k,uD]=[k,u]*u[k,D]u^-1.')
print('PASS the actual branch normalizer and its eta image do not commute in K.')
