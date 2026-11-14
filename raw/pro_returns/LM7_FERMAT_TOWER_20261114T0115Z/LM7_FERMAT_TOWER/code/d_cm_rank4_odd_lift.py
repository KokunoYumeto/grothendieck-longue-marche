#!/usr/bin/env python3
"""Exact marked surface basis and homology-generating peripheral automorphisms."""
from pathlib import Path
from collections import deque
import json,time
import sympy as sp
OUT=Path(__file__).resolve().parent;started=time.time()
def red(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out
def inv(w):return [-a for a in reversed(w)]
def comm(a,b):return red(a+b+inv(a)+inv(b))
def sub(w,images):
    out=[]
    for a in w:out=red(out+(images[abs(a)-1] if a>0 else inv(images[abs(a)-1])))
    return out
def comp(a,b):return [sub(w,a) for w in b]
I=[[1],[2],[3],[4]]
new=[[1],[-2],[1,-4,3,-1],[1,-3,1,2,-1]]
old=[[1],[-2],[1,-2,-1,-4,1],[1,-2,-1,-4,-3,1]]
assert comp(new,old)==I and comp(old,new)==I
J=json.loads((OUT/'d_cm_rank4_structure.json').read_text())
c0,c1,c2=J['cusp_K_words']
assert sub(c0,old)==[3,4]+comm([1],[2])
assert sub(c1,old)==[-2,-1,-4,1,2]
assert sub(c2,old)==[-1,-3,1]
R=comm([1],[2])+[3,4]
U=[[1],[2,1],[3],[4]];Ui=[[1],[2,-1],[3],[4]]
L=[[1,2],[2],[3],[4]];Li=[[1,-2],[2],[3],[4]]
H=[[1],[2],[4],[-4,3,4]];Hi=[[1],[2],[3,4,-3],[3]]
theta=[[3,1],[2],[2,3,-2],[3,4,-3]]
thetai=[[-2,-3,2,1],[2],[-2,3,2],[-2,-3,2,4,-2,3,2]]
for a,b in ((U,Ui),(L,Li),(H,Hi),(theta,thetai)):
    assert comp(a,b)==I and comp(b,a)==I
for a in (U,L,H):assert sub(R,a)==R
assert sub(R,theta)==[3]+R+[-3]
rotation=comp(comp(U,Li),U);rotationi=comp(comp(Ui,L),Ui)
assert comp(rotation,rotationi)==I
other=comp(comp(H,theta),Hi)
shears=[theta,comp(comp(rotation,theta),rotationi),other,comp(comp(rotation,other),rotationi)]
def hom(a):
    return sp.Matrix([[sum((1 if x>0 else -1) for x in w if abs(x)==i+1) for w in a] for i in range(4)])
vec=[]
for a in shears:
    M=hom(a)-sp.eye(4)
    assert all(M[i,j]==0 for i in range(4) for j in range(4) if not(i>=2 and j<2))
    vec.append([M[i,j] for i in (2,3) for j in (0,1)])
assert abs(int(sp.Matrix(vec).det()))==1

def mm(a,b):
    x,y,z,w=a;p,q,r,s=b
    return ((x*p+y*r)%16,(x*q+y*s)%16,(z*p+w*r)%16,(z*q+w*s)%16)
gs=[(1,1,0,1),(1,0,1,1)];seen={(1,0,0,1)};queue=deque(seen)
while queue:
    a=queue.popleft()
    for b in gs:
        c=mm(a,b)
        if c not in seen:seen.add(c);queue.append(c)
assert len(seen)==3072
Z=sp.Matrix(J['summary']['central_order3_elliptic_matrix'])
eta=(-3*sp.eye(2)-8*Z)/7
assert eta.det()==1
E16=sp.Matrix(J['summary']['D33_elliptic_Tate16_matrix'])
assert all((int(x.p)*pow(int(x.q),-1,16)-int(y))%16==0 for x,y in zip(eta,E16))
# Actual Frobenius roots on E3 and their complete principal-unit image mod8.
frob=[];gens=[]
for p,roots in ((7,[(-1,2),(-3,-2)]),(13,[(3,4),(-1,-4)])):
    points=[(x,y) for x in range(p) for y in range(p) if (y*y-x*x*x-1)%p==0]
    order=1+len(points);trace=p+1-order
    assert order==12
    for a,b in roots:
        assert 2*a-b==trace and a*a-a*b+b*b==p
        assert a%2==1 and b%2==0
    frob.append({'p':p,'affine_points':points,'point_count':order,
                 'trace':trace,'CM_roots_a_b':roots})
    gens.extend((a%8,b%8) for a,b in roots)
def om(a,b):
    x,y=a;z,w=b
    return ((x*z-y*w)%8,(x*w+y*z-y*w)%8)
units={(1,0)};queue=deque(units)
while queue:
    a=queue.popleft()
    for b in gens:
        c=om(a,b)
        if c not in units:units.add(c);queue.append(c)
assert units=={(a,b) for a in range(1,8,2) for b in range(0,8,2)}
summary={'marked_free_basis_and_inverse_verified':True,
 'three_exact_boundary_word_comparisons':True,
 'peripheral_generator_automorphisms_verified':4,
 'independent_integral_cusp_shears':4,
 'SL2_mod16_generated_order':len(seen),
 'norm_one_CM_lift':'(-3-8*zeta^2)/7',
 'norm_one_CM_lift_matrix':[[str(x) for x in eta.row(i)] for i in range(2)],
 'matches_D33_compact_Tate16':True,
 'actual_E3_Frobenius_point_counts':[v['point_count'] for v in frob],
 'actual_E3_Frobenius_traces':[v['trace'] for v in frob],
 'principal_units_mod8_generated_order':len(units),
 'scope':'The exact homological inputs support odd-deck lifting. The actual Frobenius generation plus the independent cubic twist proves the full compact CM torus image of G_Q(zeta3), hence of the full deck centralizer. Equality with the complete D33 action or the prescribed second CM factor is not asserted.',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_rank4_odd_lift.json').write_text(json.dumps({'summary':summary,
 'new_surface_basis_in_original_K':new,'original_K_basis_in_surface_basis':old,
 'surface_outer_boundary':R,'handle_upper':U,'handle_lower':L,
 'cusp_interchange':H,'cusp_shear':theta,'cusp_shear_inverse':thetai,
 'four_shear_homology_vectors':[[int(x) for x in v] for v in vec],
 'Frobenius_point_counts_and_CM_roots':frob,
 'generated_principal_units_mod8':sorted(units)},indent=2)+'\n')
print(json.dumps(summary,indent=2))
