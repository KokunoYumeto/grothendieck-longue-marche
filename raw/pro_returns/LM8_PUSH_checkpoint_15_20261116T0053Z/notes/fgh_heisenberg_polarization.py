#!/usr/bin/env python3
"""Exploratory exact cellular cup pairing and residual surface polarization."""
import sympy as s
import json
from pathlib import Path
from collections import deque
G=[(a,b,c) for a in range(3) for b in range(3) for c in range(3)]
gi={g:i for i,g in enumerate(G)}
def mul(g,h):return ((g[0]+h[0])%3,(g[1]+h[1])%3,(g[2]+h[2]+g[0]*h[1])%3)
def inv(g):return ((-g[0])%3,(-g[1])%3,(-g[2]+g[0]*g[1])%3)
def alpha(g):a,b,c=g;return ((-b)%3,a,(c-a*b)%3)
def ainv(g):return alpha(alpha(alpha(g)))
x=(1,0,0);y=(0,1,0);c=(0,0,1)
def vertex(g):return 3*g[0]+g[1]
def corners(g):return [vertex(g),vertex(mul(g,x)),vertex(mul(mul(g,x),y)),vertex(mul(g,y))]
edges=[]
for typ in ['h','v']:
 for g in G:edges.append((typ,g))
for g in G:
 for k in range(4):edges.append(('r',g,k))
ei={e:i for i,e in enumerate(edges)}
endpoints=[]
for e in edges:
 if e[0]=='h':endpoints.append((vertex(e[1]),vertex(mul(e[1],x))))
 elif e[0]=='v':endpoints.append((vertex(e[1]),vertex(mul(e[1],y))))
 else:endpoints.append((9+gi[e[1]],corners(e[1])[e[2]]))
d1=s.zeros(36,162)
for i,(a,b) in enumerate(endpoints):d1[a,i]=-1;d1[b,i]=1
D=s.zeros(162,108);Cup=s.zeros(162,162)
for g in G:
 cs=corners(g)
 boundary=[(ei[('h',g)],1),(ei[('v',mul(g,x))],1),(ei[('h',mul(g,y))],-1),(ei[('v',g)],-1)]
 for k in range(4):
  col=4*gi[g]+k;e,sign=boundary[k];ra=ei[('r',g,k)];rb=ei[('r',g,(k+1)%4)]
  D[ra,col]+=1;D[e,col]+=sign;D[rb,col]-=1
  # Global vertex order: original vertices before the face centres.
  highrad=rb if cs[k]<cs[(k+1)%4] else ra
  Cup[e,highrad]-=sign
assert d1*D==s.zeros(36,108)
# Tree gauge kills all coboundaries and leaves exactly H^1.
adj=[[] for _ in range(36)]
for j,(a,b) in enumerate(endpoints):adj[a].append((b,j));adj[b].append((a,j))
seen={0};queue=deque([0]);tree=[]
while queue:
 a=queue.popleft()
 for b,j in adj[a]:
  if b not in seen:seen.add(b);queue.append(b);tree.append(j)
assert len(tree)==35
constraints=D.T.col_join(s.eye(162)[tree,:])
ns=constraints.nullspace();assert len(ns)==20
Z=s.Matrix.hstack(*ns);J=Z.T*Cup*Z
assert J+J.T==s.zeros(20) and J.det()!=0
Jinv=J.inv()
print('Cell complex and exact rank20 symplectic cup pairing PASS.',flush=True)
def action_image(e,g=None,tauinv=False):
 if not tauinv:
  h=mul(inv(g),e[1]);return ((e[0],h,e[2]) if e[0]=='r' else(e[0],h)),1
 h=e[1]
 if e[0]=='h':return ('v',ainv(h)),-1
 if e[0]=='v':return ('h',ainv(mul(h,inv(x)))),1
 return ('r',ainv(h),(e[2]-1)%4),1
def action(g=None,tauinv=False):
 PZ=s.zeros(162,20)
 for j,e in enumerate(edges):
  dst,sgn=action_image(e,g,tauinv);PZ[j,:]=sgn*Z[ei[dst],:]
 assert D.T*PZ==s.zeros(108,20)
 M=Jinv*(Z.T*Cup*PZ)
 assert M.T*J*M==J
 return M
U=action(x);V=action(y);C=action(c);Tau=action(tauinv=True);I=s.eye(20)
assert U**3==V**3==C**3==I
assert U*V==C*V*U
assert Tau**4==I
assert Tau*U*Tau.inv()==V and Tau*V*Tau.inv()==U**2
Pc=I-(I+C+C**2)/3;P0=(I+U+U**2)/3
assert Pc.rank()==18
A=s.zeros(20)
for j in range(3):
 for k in range(3):A+=C**((-j*k)%3)*V**j*P0*V**((-k)%3)
A=(I+2*C)*A*Pc/3
assert A**4==Pc and A*U==V*A and A*V==U**2*A
assert A.T*J*A==Pc.T*J*Pc
T=A**3*Tau*Pc
assert T*T==Pc and T.T*J*T==Pc.T*J*Pc
plus=(Pc+T)/2;minus=(Pc-T)/2
assert plus.rank()==6 and minus.rank()==12
Eb=P0*minus;assert Eb**2==Eb and Eb.rank()==4
basis=s.Matrix.hstack(*Eb.columnspace())
assert (basis.T*J*basis).det()!=0
v1=basis[:,0]
v2=next(basis[:,j] for j in range(1,4) if s.Matrix.hstack(v1,C*v1,basis[:,j],C*basis[:,j]).rank()==4)
K=C-C*C
h11=(v1.T*J*K*v1)[0]/2;h22=(v2.T*J*K*v2)[0]/2
hr=(v1.T*J*K*v2)[0]/2;hi=-(v1.T*J*v2)[0]/2
hd=s.factor(h11*h22-hr*hr-3*hi*hi)
delta=-hd
assert delta>0
num,den=s.fraction(delta)
def val(n,p):
 n=int(n);a=0
 while n%p==0:n//=p;a+=1
 return a,n
vn,un=val(num,3);vd,ud=val(den,3);unit3=un*pow(ud,-1,3)%3
Fb=s.Matrix.hstack(v1,C*v1,v2,C*v2)
Fcochains=Z*Fb
compressed=[[(str(edges[j]),str(Fcochains[j,k])) for j in range(162) if Fcochains[j,k]!=0] for k in range(4)]
assert Fb.T*J*Fb==s.diag(s.Matrix([[0,-s.Rational(1,6)],[s.Rational(1,6),0]]),s.Matrix([[0,s.Rational(1,3)],[-s.Rational(1,3),0]]))
res={'status':'PASS exact algebra, unregistered geometric deduction','F_basis_cocycle_representatives':compressed,'F_basis_cup_matrix':[[str(a) for a in row] for row in (Fb.T*J*Fb).tolist()],'vertices':36,'edges':162,'triangles':108,'H1_dimension':20,'cup_pairing_det':str(J.det()),'Prym_dimension':18,'CM_plus_dimension':6,'residual_dimension':12,'surface_dimension':4,'hermitian_matrix':[[str(h11),[str(hr),str(hi)]],[[str(hr),str(-hi)],str(h22)]],'hermitian_det':str(hd),'quaternion_parameter_delta':str(delta),'delta_3_adic_valuation':vn-vd,'delta_3_unit_residue':unit3,'quaternion_division_at3':unit3==2,'surface_symplectic_form':[[str(a) for a in row] for row in (basis.T*J*basis).tolist()]}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2),flush=True)
