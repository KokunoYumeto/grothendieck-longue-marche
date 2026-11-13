#!/usr/bin/env python3
"""Exact central stabilization and marked congruence comparisons for D49.

The arithmetic parameter is the actual h of D46.  Its nonzero G3 image
is proved by the centralizer argument in D49, not numerically guessed.
This program certifies the integral central-stabilization calculation,
the actual A5 quotient, the global-sign detector, and exact graph ranks.
"""
from collections import deque
from pathlib import Path
import argparse,hashlib,json,time
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
from sympy.polys.domains import ZZ

ap=argparse.ArgumentParser()
ap.add_argument('--source-code',type=Path,default=Path(__file__).resolve().parents[2]/'LM7_FERMAT_TOWER'/'code')
args=ap.parse_args();OUT=Path(__file__).resolve().parent;started=time.time()
source=args.source_code/'d_cm_central_mixed.json';D=json.loads(source.read_text())
rs,rr=D['E_right_s'],D['E_right_r'];size=len(rs);assert size==1152
v2=[(0,min(i,rs[i])) for i in range(size)]
v3=[(1,min(i,rr[i],rr[rr[i]])) for i in range(size)]
adj={v:[] for v in set(v2+v3)}
for e in range(size):
    adj[v2[e]].append((v3[e],e,1));adj[v3[e]].append((v2[e],e,-1))
paths={v2[0]:{}};queue=deque([v2[0]]);tree=set()
while queue:
    v=queue.popleft()
    for w,e,sg in adj[v]:
        if w not in paths:
            p=paths[v].copy();p[e]=p.get(e,0)+sg
            if not p[e]:del p[e]
            paths[w]=p;tree.add(e);queue.append(w)
ch=[e for e in range(size) if e not in tree];C=[]
assert ch==D['L_cycle_chords'] and len(ch)==193
for e in ch:
    c=paths[v2[e]].copy()
    for j,a in paths[v3[e]].items():
        c[j]=c.get(j,0)-a
        if not c[j]:del c[j]
    c[e]=c.get(e,0)+1
    if not c[e]:del c[e]
    C.append(c)
assert all([c.get(e,0) for e in ch]==[int(i==j) for i in range(193)]
           for j,c in enumerate(C))
words={0:[]};todo=[0]
for q in todo:
    for a,perm in [(0,rs),(1,rr)]:
        qq=perm[q]
        if qq not in words:words[qq]=words[q]+[a];todo.append(qq)
assert len(words)==size
def rw(q,w):
    for a in w:q=rs[q] if a==0 else rr[q]
    return q
ls=[rw(rs[0],words[q]) for q in range(size)]
lr=[rw(rr[0],words[q]) for q in range(size)]
assert sorted(ls)==sorted(lr)==list(range(size))
assert all(ls[ls[q]]==q and lr[lr[lr[q]]]==q for q in range(size))
assert all(left[right[q]]==right[left[q]] for left in [ls,lr]
           for right in [rs,rr] for q in range(size))
invleft=[]
for perm in [ls,lr]:
    iv=[0]*size
    for i,j in enumerate(perm):iv[j]=i
    invleft.append(iv)
cols=[];actions=[]
for perm,iv in zip([ls,lr],invleft):
    mat=[]
    for j,c in enumerate(C):
        row=[c.get(iv[e],0) for e in ch];mat.append(row)
        full={}
        for k,a in enumerate(row):
            if a:
                for e,b in C[k].items():full[e]=full.get(e,0)+a*b
        target={perm[e]:a for e,a in c.items()}
        assert all(full.get(e,0)==target.get(e,0) for e in set(full)|set(target))
        cols.append([int(i==j)-row[i] for i in range(193)])
    actions.append(mat)
A=sp.Matrix(193,386,lambda i,j:cols[j][i])
S=smith_normal_form(A,domain=ZZ)
diagonal=[abs(int(S[i,i])) for i in range(193)]
assert diagonal==[1]*193
assert hermite_normal_form(A)==sp.eye(193)

# The literal marked quotient B -> PSL2(F5) -> A5 on its five V4 subgroups.
n=5;I=(1,0,0,1)
def can(a,m):return min(tuple(x%m for x in a),tuple(-x%m for x in a))
def mul(a,b):
    return can((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]),n)
def inv(a):return can((a[3],-a[1],-a[2],a[0]),n)
s=can((0,1,-1,0),n);r=can((0,-1,1,-1),n)
G=[I];seen={I}
for a in G:
    for b in [s,r]:
        c=mul(a,b)
        if c not in seen:seen.add(c);G.append(c)
assert len(G)==60 and mul(s,s)==I and mul(mul(r,r),r)==I
invol=[a for a in G if a!=I and mul(a,a)==I];assert len(invol)==15
V4=sorted({tuple(sorted({I,a,b,mul(a,b)})) for a in invol for b in invol
           if a!=b and mul(a,b)==mul(b,a)})
assert len(V4)==5 and all(len(v)==4 for v in V4)
def perm(a):
    return tuple(V4.index(tuple(sorted(mul(mul(a,b),inv(a)) for b in v))) for v in V4)
perms=[perm(a) for a in G];assert len(set(perms))==60
def parity(p):return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2
assert all(parity(p)==0 for p in perms)
assert any(mul(a,b)!=mul(b,a) for a in G for b in G)
classes=[];unused=set(G)
while unused:
    a=next(iter(unused));c={mul(mul(b,a),inv(b)) for b in G}
    classes.append(c);unused-=c
classes.sort(key=lambda c:(len(c),sorted(c)))
assert sorted(len(c) for c in classes)==[1,12,12,15,20]
normal_union_orders=[]
for mask in range(1<<(len(classes)-1)):
    order=1+sum(len(classes[j+1]) for j in range(len(classes)-1) if mask>>j&1)
    if 60%order==0:normal_union_orders.append(order)
assert sorted(normal_union_orders)==[1,60]

# The independent local projective signs have exactly one residual C2;
# the retained Q12 data detect it, so their actual joint map recovers
# the full global-sign congruence quotient at all levels.
fibers={}
for q in map(tuple,D['Q']):
    key=(can(q,4),can(q,3));fibers.setdefault(key,[]).append(q)
assert len(fibers)==288 and all(len(v)==2 for v in fibers.values())
sign_kernel=sorted(fibers[(I,I)])
assert sign_kernel==[I,(5,0,0,5)]

g3_order=576*3**97
rank_full=1+g3_order//6
rank_move=g3_order//9
assert rank_move==64*3**97
summary={'input_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'L_rank':193,'central_augmentation_shape':[193,386],
 'central_augmentation_Smith_multiplicities':{'1':193},
 'central_augmentation_Hermite_is_identity':True,
 'actual_integral_cycle_actions_verified':386,'central_stabilization':'[L,Bhat]=L',
 'literal_PSL2_F5_order':60,'A5_s_permutation_zero_based':list(perm(s)),
 'A5_r_permutation_zero_based':list(perm(r)),
 'five_V4_action_is_faithful_and_even':True,'A5_normal_class_union_orders':normal_union_orders,
 'Q12_to_independent_local_projective_image_order':288,
 'Q12_relative_sign_kernel':[list(q) for q in sign_kernel],
 'Q12_detects_entire_residual_global_sign_C2':True,
 'G3_order':g3_order,'relative_G3_mod2_homology_dimension':rank_full,
 'nonzero_actual_parameter_order_in_G3':3,
 'explicit_cyclic_moving_subspace_dimension':rank_move,
 'full_moving_subspace_formula':'|G3|/6 * (1 - 1/|A|), where A is the actual Q-span of f_h mod G3',
 'parameter_scope':'Nonvanishing of the actual f_h in G3 and the residual-subspace formula are proved in D49; no numerical vector for that arithmetic parameter or its Q-span dimension is asserted by this certificate.',
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'central_augmentation_matrix_rows':[[int(x) for x in row] for row in A.tolist()],
 'central_augmentation_Smith_diagonal':diagonal,
 'actual_E_left_s':ls,'actual_E_left_r':lr,
 'A5_matrices':[list(a) for a in G],'A5_permutations':[list(a) for a in perms],
 'A5_five_V4_subgroups':[[list(a) for a in v] for v in V4],
 'A5_conjugacy_classes':[[list(a) for a in sorted(c)] for c in classes],
 'Q12_local_projective_fibers':[{'mod4':list(k[0]),'mod3':list(k[1]),
                               'full_Q12':list(map(list,v))} for k,v in sorted(fibers.items())]}
(OUT/'d_cm_fixed_parameter.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
