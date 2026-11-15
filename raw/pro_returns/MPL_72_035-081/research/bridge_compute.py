#!/usr/bin/env python3
"""Exact finite arithmetic for the explicit B5 comparison; no manuscript files read or changed.

Run from anywhere: python3 bridge_compute.py
Inputs: levels listed in LEVELS; the integral matrices X,Y,R0,R1,R2 below.
Outputs: bridge_counts.csv, bridge_computation.json beside this script.
The counts are finite exhaustive computations; the accompanying note proves the maps.
"""
from __future__ import annotations
import csv,json,math
from collections import Counter,deque
from pathlib import Path
import sympy as sp

LEVELS=(2,3,4,5,6,7,8,9,10,12,15)
X=(0,1,-1,1)
Y=(1,1,0,1)
I2=(1,0,0,1)


def mul(a,b,n,d):
 return tuple(sum(a[d*i+k]*b[d*k+j] for k in range(d))%n for i in range(d) for j in range(d))
def neg(a,n):return tuple(-v%n for v in a)
def canon(a,n):
 a=tuple(v%n for v in a)
 return min(a,neg(a,n))
def adjoint(a,n):
 aa,b,c,d=a
 return tuple(v%n for v in (aa*d+b*c,-aa*c,b*d,-2*aa*b,aa*aa,-b*b,2*c*d,-c*c,d*d))
def ident(d):return tuple(int(i==j) for i in range(d) for j in range(d))
def act3(a,v,n):return tuple(sum(a[3*i+j]*v[j] for j in range(3))%n for i in range(3))
def row3(v,a,n):return tuple(sum(v[i]*a[3*i+j] for i in range(3))%n for j in range(3))
def cycles(group,h,n,d,canonical=False):
 pool=set(group);ans=[]
 while pool:
  first=min(pool);v=first;cycle=[]
  while v not in cycle:
   cycle.append(v);pool.remove(v)
   v=mul(v,h,n,d)
   if canonical:v=canon(v,n)
  assert v==first
  ans.append(cycle)
 return ans

def symbolic_checks():
 R=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[-1,1],[0,1]]),sp.Matrix([[-1,0],[0,1]])]
 basis=[R[0],-R[1],2*R[2]]
 coordinates=lambda B:sp.Matrix([B[0,0],B[0,1],B[1,0]])
 P=sp.Matrix.hstack(*(coordinates(B) for B in basis))
 T=[sp.Matrix.hstack(*(P.inv()*coordinates(-r*b*r.inv()) for b in basis)) for r in R]
 expected=[sp.Matrix([[-1,1,0],[0,1,0],[0,0,1]]),sp.Matrix([[1,0,0],[1,-1,4],[0,0,1]]),sp.Matrix([[1,0,0],[0,1,0],[0,1,-1]])]
 assert T==expected
 assert R[0]*R[1]==sp.Matrix(2,2,X) and R[1]*R[2]==sp.Matrix(2,2,Y)
 s0=sp.Matrix([0,1,sp.Rational(1,2)])
 assert T[0]*s0==s0+sp.Matrix([1,0,0])
 assert T[1]*s0==s0 and T[2]*s0==s0
 assert sum((s0[i]*basis[i] for i in range(3)),sp.zeros(2))==sp.Matrix([[0,-1],[0,0]])
 u0,u1,u2=sp.symbols('u0 u1 u2')
 B=sum((u*b for u,b in zip((u0,u1,u2),basis)),sp.zeros(2))
 q=sp.expand(-B.det())
 assert q==u0*u0+u1*u1+4*u2*u2-u0*u1-4*u1*u2
 for t in T:
  vv=t*sp.Matrix([u0,u1,u2]);assert sp.expand(q.subs(dict(zip((u0,u1,u2),vv)),simultaneous=True)-q)==0
 A=sp.Matrix([[-2,1,0],[1,-2,4],[0,1,-2]])
 assert A*s0==sp.Matrix([1,0,0]) and A.det()==2
 polar=sp.hessian(q,(u0,u1,u2))
 assert polar==sp.Matrix([[2,-1,0],[-1,2,-4],[0,-4,8]]) and polar.det()==-8
 assert q.subs({u0:0,u1:1,u2:sp.Rational(1,2)})==0
 aa,bb,cc,dd,ss,tt=sp.symbols('aa bb cc dd ss tt')
 gg=sp.Matrix([[aa,bb],[cc,dd]]);vv=sp.Matrix([ss,tt])
 M=lambda v:v*sp.Matrix([[v[1],-v[0]]])
 # Polynomial form of M(gv)=det(g) g M(v) g^{-1}, with no division.
 assert (M(gg*vv)-gg*M(vv)*gg.adjugate()).applyfunc(sp.expand)==sp.zeros(2)
 return {'basis_matrix':str(P),'basis_determinant':int(P.det()),'T_matrices':[str(t) for t in T],'X_in_root_basis':str(T[0]*T[1]),'Y_in_root_basis':str(T[1]*T[2]),'quadratic_form':str(q),'polar_matrix':str(polar),'polar_determinant':int(polar.det()),'s0_root_coordinates':str(s0),'s0_quadratic_value':0,'vertex_equivariance':'M(gv)=g M(v) adjugate(g), checked as a polynomial identity','rho':-2,'beta':[1,4],'mu':[-2,-2,-2],'symbolic_checks':'passed over Q; all identities have denominators powers of 2 and hold over Z[1/2]'}

def compute(n):
 sl={(a,b,c,d) for a in range(n) for b in range(n) for c in range(n) for d in range(n) if (a*d-b*c)%n==1}
 group={canon(a,n) for a in sl}
 xx,yy=canon(X,n),canon(Y,n);ss=canon(mul(xx,yy,n,2),n)
 reached={canon(I2,n)};todo=deque(reached)
 while todo:
  g=todo.popleft()
  for h in (xx,yy):
   gh=canon(mul(g,h,n,2),n)
   if gh not in reached:reached.add(gh);todo.append(gh)
 assert reached==group
 xc,yc,sc=(cycles(group,h,n,2,True) for h in (xx,yy,ss))
 assert {len(c) for c in xc}=={3}
 assert {len(c) for c in yc}=={n}
 assert {len(c) for c in sc}=={2}
 primitive={(a,c) for a in range(n) for c in range(n) if math.gcd(a,c,n)==1}
 vcanonical=lambda v:min(tuple(v),tuple(-x%n for x in v))
 vertices={vcanonical(v) for v in primitive}
 col_vertices={vcanonical((g[0],g[2])) for g in group}
 assert vertices==col_vertices and len(vertices)==len(yc)
 assert all(len({vcanonical((g[0],g[2])) for g in cyc})==1 for cyc in yc)
 units={a for a in range(n) if math.gcd(a,n)==1}
 roots={a for a in units if (a*a-1)%n==0}
 p1={min(tuple(u*x%n for x in v) for u in units) for v in primitive}
 nilpoints={(a*c%n,-a*a%n,c*c%n) for a,c in primitive}
 adset={adjoint(g,n) for g in group}
 kernel={g for g in group if adjoint(g,n)==ident(3)}
 scalar_kernel={canon((u,0,0,u),n) for u in roots}
 assert kernel==scalar_kernel
 assert len(adset)*len(kernel)==len(group)
 ax,ay,ass=(adjoint(g,n) for g in (xx,yy,ss))
 for g in group:
  for h,ah in ((xx,ax),(yy,ay)):
   assert adjoint(canon(mul(g,h,n,2),n),n)==mul(adjoint(g,n),ah,n,3)
 acx,acy,acs=(cycles(adset,h,n,3) for h in (ax,ay,ass))
 assert {len(c) for c in acx}=={3} and {len(c) for c in acy}=={n} and {len(c) for c in acs}=={2}
 assert len(acy)==len(nilpoints)
 # Right multiplication on darts and the first-column / nilpotent vertex maps.
 assert all((-g[1]%n,-g[4]%n,-g[7]%n) in nilpoints for g in adset)
 D,V,E,F=len(group),len(yc),len(sc),len(xc)
 D2,V2,E2,F2=len(adset),len(acy),len(acs),len(acx)
 assert (2-V+E-F)%2==0 and (2-V2+E2-F2)%2==0
 row={'N':n,'SL2_order':len(sl),'Farey_darts':D,'Farey_flags':2*D,'Farey_vertices':V,'Farey_edges':E,'Farey_faces':F,'Farey_genus':(2-V+E-F)//2,'primitive_columns':len(primitive),'units':len(units),'scalar_square_roots_of_1':len(roots),'adjoint_kernel_after_global_sign':len(kernel),'adjoint_darts':D2,'nilpotent_vertices':V2,'adjoint_edges':E2,'adjoint_faces':F2,'adjoint_genus':(2-V2+E2-F2)//2,'P1_points':len(p1),'manuscript_root_basis_comparison':'Z[1/2] comparison applies' if n%2 else 'basis determinant 2 is not a unit'}
 details={'N':n,'scalar_roots':sorted(roots),'kernel_representatives':sorted(kernel),'generator_cycle_lengths':{'X':3,'Y':n,'XY':2},'all_matrix_group_and_vertex_checks':'passed'}
 # The labelled coset cells have actual affine supporting subspaces.
 # Count that further map explicitly; it can have larger fibres than one.
 row.update({'affine_support_lines':'not claimed through the centred basis at even N','affine_support_planes':'not claimed through the centred basis at even N','labelled_edges_per_support_line':'','labelled_faces_per_support_plane':'','geometric_flag_triples':''})
 if n%2:
  supports={};line_set=set();plane_set=set();flags=set()
  for g in group:
   aa,bb,cc,dd=g;ag=adjoint(g,n);agi=adjoint((dd,-bb,-cc,aa),n)
   pt=act3(ag,(0,-1,0),n);direction=act3(ag,(0,1,1),n)
   line=tuple(sorted(tuple((pt[j]+t*direction[j])%n for j in range(3)) for t in range(n)))
   assert len(set(line))==n
   plane=row3((1,1,-1),agi,n);other_plane=row3((-1,1,-1),agi,n)
   assert sum(plane[j]*pt[j] for j in range(3))%n==n-1
   supports[ag]=(pt,line,plane)
   line_set.add(line);plane_set.add(plane)
   flags.add((pt,line,plane));flags.add((pt,line,other_plane))
  assert len(flags)==2*D2
  assert all(len({supports[a][1] for a in cyc})==1 for cyc in acs)
  assert all(len({supports[a][2] for a in cyc})==1 for cyc in acx)
  assert E2%len(line_set)==0 and F2%len(plane_set)==0
  assert set(Counter(supports[cyc[0]][1] for cyc in acs).values())=={E2//len(line_set)}
  assert set(Counter(supports[cyc[0]][2] for cyc in acx).values())=={F2//len(plane_set)}
  row.update({'affine_support_lines':len(line_set),'affine_support_planes':len(plane_set),'labelled_edges_per_support_line':E2//len(line_set),'labelled_faces_per_support_plane':F2//len(plane_set),'geometric_flag_triples':len(flags)})
  details['geometric_support_check']='All labelled edge/face cycles map to their displayed affine support; full geometric flag triples have trivial stabilizer.'
 if n==15:
  v=(1,0);w=(4,0)
  details['vertex_kernel_example']={'Farey_columns':[v,w],'distinct_mod_global_sign':vcanonical(v)!=vcanonical(w),'nilpotent_images':[(a*c%n,-a*a%n,c*c%n) for a,c in (v,w)],'scalar_matrix':[4,0,0,4]}
  line_stabilizer=(6,10,5,6);plane_stabilizer=(6,10,5,1)
  assert line_stabilizer in group and plane_stabilizer in group
  assert supports[adjoint(line_stabilizer,n)][1]==supports[ident(3)][1]
  assert supports[adjoint(plane_stabilizer,n)][2]==supports[ident(3)][2]
  details['additional_support_stabilizers']={'line_matrix':line_stabilizer,'plane_matrix':plane_stabilizer,'base_line_vertex_parameters':[t for t in range(n) if t*(t-1)%n==0],'line_support_fibre':E2//len(line_set),'plane_support_fibre':F2//len(plane_set)}
 return row,details

def main():
 symbolic=symbolic_checks();results=[compute(n) for n in LEVELS];rows=[v[0] for v in results]
 out=Path(__file__).resolve().parent
 with (out/'bridge_counts.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 report={'scope':'Post-freeze explicit construction; no source transcription changes','levels':LEVELS,'symbolic':symbolic,'counts':rows,'checks':[v[1] for v in results]}
 (out/'bridge_computation.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'levels':LEVELS,'rows':len(rows),'symbolic_checks':'passed','finite_checks':'passed','csv':str(out/'bridge_counts.csv'),'json':str(out/'bridge_computation.json')},indent=2))
 print('\nN D V E F g kernel AdD AdV P1')
 for r in rows:print(*(r[k] for k in ('N','Farey_darts','Farey_vertices','Farey_edges','Farey_faces','Farey_genus','adjoint_kernel_after_global_sign','adjoint_darts','nilpotent_vertices','P1_points')))
if __name__=='__main__':main()
