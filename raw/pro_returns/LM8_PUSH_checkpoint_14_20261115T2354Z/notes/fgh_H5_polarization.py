#!/usr/bin/env python3
"""Exploratory exact cellular H5 representation. Not a registered theorem.
Uses the same ordered triangular cup as A51, eliminating centre coboundaries.
"""
import sympy as s
import json,time
from pathlib import Path
from collections import deque
p=5
start=time.monotonic()
def log(msg): print(f'{time.monotonic()-start:.2f}s {msg}',flush=True)
G=[(a,b,c) for a in range(p) for b in range(p) for c in range(p)]
gi={g:i for i,g in enumerate(G)}
def mul(g,h):return ((g[0]+h[0])%p,(g[1]+h[1])%p,(g[2]+h[2]+g[0]*h[1])%p)
def inv(g):return ((-g[0])%p,(-g[1])%p,(-g[2]+g[0]*g[1])%p)
def alpha(g):a,b,c=g;return ((-b)%p,a,(c-a*b)%p)
def ainv(g):return alpha(alpha(alpha(g)))
x=(1,0,0);y=(0,1,0);c=(0,0,1)
def vertex(g):return p*g[0]+g[1]
def corners(g):return [vertex(g),vertex(mul(g,x)),vertex(mul(mul(g,x),y)),vertex(mul(g,y))]
edges=[(typ,g) for typ in ('h','v') for g in G]
ei={e:i for i,e in enumerate(edges)}
nv=p*p;ne=2*p**3;nf=p**3
endpoints=[(vertex(g),vertex(mul(g,x if typ=='h' else y))) for typ,g in edges]
D=s.zeros(ne,nf);Cup=s.zeros(ne,ne)
for g in G:
 cs=corners(g)
 h=ei[('h',g)];vr=ei[('v',mul(g,x))];ht=ei[('h',mul(g,y))];v=ei[('v',g)]
 boundary=[(h,1),(vr,1),(ht,-1),(v,-1)]
 # Set centre-to-lower-left radial cocycle to zero by a centre coboundary.
 # Other radials then equal h, h+v_right, and v, using the square relation.
 rad=[{}, {h:1}, {h:1,vr:1}, {v:1}]
 for k,(e,sgn) in enumerate(boundary):
  D[e,gi[g]]+=sgn
  high=(k+1)%4 if cs[k]<cs[(k+1)%4] else k
  for j,coeff in rad[high].items():Cup[e,j]-=sgn*coeff
adj=[[] for _ in range(nv)]
for j,(a,b) in enumerate(endpoints):adj[a].append((b,j,1));adj[b].append((a,j,-1))
seen={0};queue=deque([0]);tree=[];traverse=[]
while queue:
 a=queue.popleft()
 for b,j,sgn in adj[a]:
  if b not in seen:seen.add(b);queue.append(b);tree.append(j);traverse.append((a,b,j,sgn))
assert len(tree)==nv-1
constraints=D.T.col_join(s.eye(ne)[tree,:])
log(f'Built square complex {nv},{ne},{nf}; computing exact RREF.')
rr,piv=constraints.rref();free=[j for j in range(ne) if j not in piv]
Z=s.zeros(ne,len(free))
for col,j in enumerate(free):
 Z[j,col]=1
 for k,i in enumerate(piv):Z[i,col]=-rr[k,j]
assert len(free)==102 and constraints*Z==s.zeros(constraints.rows,102)
J=Z.T*Cup*Z
assert J+J.T==s.zeros(102) and J.det()!=0
log('H1 dimension102, exact nondegenerate skew cup computed.')
def action_image(e,g=None,tauinv=False):
 typ,h=e
 if not tauinv:return (typ,mul(inv(g),h)),1
 if typ=='h':return ('v',ainv(h)),-1
 return ('h',ainv(mul(h,inv(x)))),1

def action(g=None,tauinv=False):
 PZ=s.zeros(ne,102)
 for j,e in enumerate(edges):
  dst,sgn=action_image(e,g,tauinv);PZ[j,:]=sgn*Z[ei[dst],:]
 assert D.T*PZ==s.zeros(nf,102)
 potentials=[s.zeros(1,102) for _ in range(nv)]
 for a,b,j,sgn in traverse:potentials[b]=potentials[a]+sgn*PZ[j,:]
 QZ=s.zeros(ne,102)
 for j,(a,b) in enumerate(endpoints):QZ[j,:]=PZ[j,:]-potentials[b]+potentials[a]
 M=QZ[free,:]
 assert Z*M==QZ
 assert M.T*J*M==J
 return M
U=action(x);log('U action.')
V=action(y);log('V action.')
C=action(c);log('Z action.')
Tau=action(tauinv=True);log('Tau action.')
I=s.eye(102)
Up=[I];Vp=[I];Cp=[I]
for k in range(1,p):Up.append(Up[-1]*U);Vp.append(Vp[-1]*V);Cp.append(Cp[-1]*C)
assert Up[-1]*U==Vp[-1]*V==Cp[-1]*C==I
assert U*V==C*V*U
assert Tau**4==I and Tau*U*Tau**3==V and Tau*V*Tau**3==Up[-1]
Pc=I-sum(Cp,s.zeros(102))/p;P0=sum(Up,s.zeros(102))/p
assert Pc.rank()==100
log('Group identities and central Prym rank100.')
# Fourier denominator sqrt(5)=1+2(zeta5+zeta5^-1), inverse sqrt(5)/5.
A=s.zeros(102)
for j in range(p):
 for k in range(p):A+=Cp[(-j*k)%p]*Vp[j]*P0*Vp[(-k)%p]
A=(I+2*C+2*Cp[4])*A*Pc/p
assert A**4==Pc and A*U==V*A and A*V==Up[-1]*A
assert A.T*J*A==Pc.T*J*Pc
T=A**3*Tau*Pc
assert T**4==Pc and T.T*J*T==Pc.T*J*Pc
assert T*U==U*T and T*V==V*T and T*C==C*T
log('Exact normalized Fourier and residual T identities.')
Pcm=(Pc+T**2)/2;P8=(Pc-T**2)/2
assert Pcm**2==Pcm and P8**2==P8
assert s.trace(Pcm)==20 and s.trace(P8)==80
assert T*Pcm==-Pcm
Ecm=P0*Pcm;E8=P0*P8
assert Ecm**2==Ecm and E8**2==E8
assert s.trace(Ecm)==4 and s.trace(E8)==16
basis=s.Matrix.hstack(*E8.columnspace())
assert (basis.T*J*basis).det()!=0
log('Primitive factors: CM surface H1rank4 and B8 H1rank16.')
# The CM field Q(zeta5,i) acts through C,T on E8.
# Find two vectors giving a basis over that degree-eight field.
def orbit(v):return [Cp[j]*(T**k)*v for k in range(2) for j in range(4)]
v1=basis[:,0];o1=orbit(v1);assert s.Matrix.hstack(*o1).rank()==8
v2=next(basis[:,j] for j in range(1,16) if s.Matrix.hstack(*(o1+orbit(basis[:,j]))).rank()==16)
Fb=s.Matrix.hstack(*(o1+orbit(v2)));assert Fb.rank()==16
Jb=Fb.T*J*Fb
log('Found exact rank-two Q(zeta20) basis; cup matrix ready.')
Fcochains=Z*Fb
res={'status':'PASS exploratory exact representation','p':p,'H1_dimension':102,'cup_det':str(J.det()),
     'Prym_dimension':100,'CM_isotypic_rank':20,'remaining_isotypic_rank':80,
     'CM_surface_H1_rank':4,'remaining_B8_H1_rank':16,
     'field_basis_order':'v1,Cv1,C2v1,C3v1,Tv1,CTv1,C2Tv1,C3Tv1; then same forv2',
     'field_basis_cup_matrix':[[str(a) for a in row] for row in Jb.tolist()],
     'field_basis_cochains': [[(str(edges[j]),str(Fcochains[j,k])) for j in range(ne) if Fcochains[j,k]!=0] for k in range(16)]}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
# Retain small field actions and full projection data for subsequent exact Hermitian extraction.
full={'J':[[str(a) for a in row] for row in Jb.tolist()],
      'C':[[str(a) for a in row] for row in ((Jb.inv())*Fb.T*J*C*Fb).tolist()],
      'T':[[str(a) for a in row] for row in ((Jb.inv())*Fb.T*J*T*Fb).tolist()]}
Path(__file__).with_name('fgh_H5_field_pairing.json').write_text(json.dumps(full,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k not in ('field_basis_cochains','field_basis_cup_matrix')},indent=2),flush=True)
print(Jb,flush=True)
log('COMPLETE')
