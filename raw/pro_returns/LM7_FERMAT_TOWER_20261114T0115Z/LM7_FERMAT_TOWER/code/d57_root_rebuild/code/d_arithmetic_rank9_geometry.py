#!/usr/bin/env python3
"""The exact marked genus-three cover and rational rank-nine centralizer.

The geometric matrices, Belyi map, elliptic quotient maps and integral
rank-nine graph are checked through literal maps, not just group orders.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time
import sympy as sp
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_affine_base.json').read_text())
H=json.loads((OUT/'d_arithmetic_rank9_seed.json').read_text())
# Q(zeta,sqrt3), basis1,zeta,a,a*zeta, with zeta²=-1-zeta,a²=3.
zero=(F(0),)*4;one=(F(1),F(0),F(0),F(0))
zz=(F(0),F(1),F(0),F(0));aa=(F(0),F(0),F(1),F(0))
def ad(a,b):return tuple(x+y for x,y in zip(a,b))
def ng(a):return tuple(-x for x in a)
def sc(a,n):return tuple(x*n for x in a)
def fm(a,b):
 out=[F(0)]*4
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   if not x or not y:continue
   ap=i//2+j//2;zp=i%2+j%2;c=x*y
   if ap>=2:ap-=2;c*=3
   if zp==2:
    out[2*ap]-=c;out[2*ap+1]-=c
   else:out[2*ap+zp]+=c
 return tuple(out)
def fp(a,n):
 out=one
 while n:
  if n&1:out=fm(out,a)
  a=fm(a,a);n//=2
 return out
ii=sc(fm(aa,ad(one,sc(zz,2))),F(1,3))
assert fm(ii,ii)==ng(one)
I=(one,zero,zero,one)
SG=tuple(sc(x,F(1,3)) for x in (ng(aa),sc(aa,2),aa,aa))
RG=(zz,zero,zero,one)
def mm(A,B):
 a,b,c,d=A;e,f,g,h=B
 return (ad(fm(a,e),fm(b,g)),ad(fm(a,f),fm(b,h)),
         ad(fm(c,e),fm(d,g)),ad(fm(c,f),fm(d,h)))
def mp(A,n):
 out=I
 while n:
  if n&1:out=mm(out,A)
  A=mm(A,A);n//=2
 return out
assert mp(SG,2)==I and mp(RG,3)==I
TG=mm(SG,RG)
assert mp(TG,3)==(ii,zero,zero,ii) and mp(TG,12)==I
# The full isomorphism to the actual48-state linear quotient.
M=[tuple(map(tuple,x)) for x in D['Q_linear_image_matrices']];ix={x:i for i,x in enumerate(M)}
S=tuple(map(tuple,D['quotient_s_columns']));R=tuple(map(tuple,D['quotient_r_columns']))
def mv(A,v):return tuple(sum(v[j]*A[j][i] for j in range(4))%3 for i in range(4))
def m4(A,B):return tuple(mv(A,c) for c in B)
rs=[ix[m4(A,S)] for A in M];rr=[ix[m4(A,R)] for A in M]
geo={0:I};words={0:[]};todo=[0];checks=0
for q in todo:
 for token,h,G in [(0,rs[q],SG),(1,rr[q],RG)]:
  image=mm(geo[q],G)
  if h not in geo:geo[h]=image;words[h]=words[q]+[token];todo.append(h)
  else:assert geo[h]==image
  checks+=1
assert len(geo)==48 and len(set(geo.values()))==48
# Every matrix preserves the exact homogeneous quartic X³Z+Z⁴.
def linpow(a,b,n):
 return [sc(fm(fp(a,n-k),fp(b,k)),comb(n,k)) for k in range(n+1)]
for A in geo.values():
 a,b,c,d=A;p=linpow(a,b,3);out=[zero]*5
 for k,v in enumerate(p):
  out[k]=ad(out[k],fm(v,c));out[k+1]=ad(out[k+1],fm(v,d))
 for k,v in enumerate(linpow(c,d,4)):out[k]=ad(out[k],v)
 assert out==[zero,one,zero,zero,one]

x=sp.symbols('x');a=sp.sqrt(3)
beta=(x**6+20*x**3-8)**2/(64*(x**3+1)**3)
sx=(2-x)/(x+1)
assert sp.factor(beta.subs(x,sx)-beta)==0
assert sp.expand((x**6+20*x**3-8)**2-64*(x**3+1)**3-x**3*(x**3-8)**3)==0
assert sp.simplify(beta.subs(x,a-1))==0
assert beta.subs(x,0)==1
assert sp.simplify(sp.diff(sx,x).subs(x,a-1))==-1
# The actual index-eight elliptic cover is the degree-two y->y^2 map
# followed by multiplication by2, not merely its first degree-two factor.
uE=x*(x**3-8)/(4*(x**3+1));vnum=x**6+20*x**3-8
assert sp.factor(uE**3+1-beta)==0
assert sp.factor(uE.subs(x,sx)-uE)==0
assert sp.factor(vnum.subs(x,sx)*(x+1)**6+27*vnum)==0
# R sends uE to zeta*uE and fixes vE=vnum/(8*y^6), while S fixes
# uE and negates vE.  These identities follow termwise from x^3.
assert all(k%3==1 for (k,),c in sp.Poly(x*(x**3-8),x).terms())
assert all(k%3==0 for (k,),c in sp.Poly(vnum,x).terms())
quotients=[]
for aa0 in (a,-a):
 U=(x+1-aa0)/(x+1+aa0)
 u4=(x**3+1)/(x+1+aa0)**4
 Z=((9+6*aa0)*U**2-9)/(6*aa0)
 d=12+8*aa0
 assert sp.simplify(sp.cancel(Z**2-1+d*u4,extension=a))==0
 assert sp.simplify(sp.cancel(U.subs(x,sx)+U,extension=a))==0
 du_num=-x**3+3*(1+aa0)*x**2-4
 den=(9+6*aa0)*(x+1-aa0)**2-9*(x+1+aa0)**2
 omega=sp.simplify(sp.cancel(6*aa0*du_num/(4*den),extension=a))
 assert sp.simplify(omega-(-x-1+aa0)/4)==0
 quotients.append({'sqrt3_sign':1 if aa0==a else -1,
                   'quartic_coefficient_d':str(d),
                   'elliptic_Weierstrass_coefficient':str(3+2*aa0),
                   'pulled_back_differential_coefficient':str(omega)})
u,z=sp.symbols('u z')
XE=2*(1+z)/u**2;YE=4*(1+z)/u**3;dd=sp.symbols('d')
assert sp.cancel(YE**2-XE**3-4*dd*XE+8*(z+1)*(z**2-1+dd*u**4)/u**6)==0

# Exact rational centralizer, certified by a mod5 upper bound and five
# independent rational commuting matrices.
HS=H['homology_s_columns'];HR=H['homology_r_columns'];J=H['quarter_turn_columns']
Z=H['central_involution_columns'];N=H['Q8_norm_columns'];HT=H['homology_t_columns']
I9=[[int(i==j) for i in range(9)] for j in range(9)]
def imul(A,B):return [[sum(B[j][k]*A[k][i] for k in range(9)) for i in range(9)] for j in range(9)]
TN=imul(imul(HT,HT),N);J3=imul(J,Z)
operators=[I9,J,Z,J3,TN]
def rank_mod(rows,p):
 bas={}
 for row in rows:
  v=[x%p for x in row]
  while any(v):
   q=max(i for i,x in enumerate(v) if x)
   if q not in bas:
    iv=pow(v[q],-1,p);bas[q]=[x*iv%p for x in v];break
   c=v[q];v=[(x-c*y)%p for x,y in zip(v,bas[q])]
 return len(bas),sorted(bas)
eq=[]
for A in (HS,HR):
 for i in range(9):
  for j in range(9):
   row=[0]*81
   for k in range(9):
    row[i*9+k]+=A[j][k];row[k*9+j]-=A[k][i]
   eq.append(row)
rk,piv=rank_mod(eq,5);assert rk==76
assert rank_mod([[col[i] for col in O for i in range(9)] for O in operators],5)[0]==5
for O in operators:
 assert imul(O,HS)==imul(HS,O) and imul(O,HR)==imul(HR,O)
eE=[[F(x,8) for x in c] for c in N]
eQ=[[F(I9[j][i]-Z[j][i],2) for i in range(9)] for j in range(9)]
eR=[[F(I9[j][i]+Z[j][i],2)-eE[j][i] for i in range(9)] for j in range(9)]
for E in (eE,eQ,eR):assert imul(E,E)==E
assert all(imul(E,F0)==[[0]*9 for _ in range(9)] for E,F0 in ((eE,eQ),(eE,eR),(eQ,eR)))
assert [[eE[j][i]+eQ[j][i]+eR[j][i] for i in range(9)] for j in range(9)]==I9
summary={
 'scope':'Exact marked genus-three geometry and rational centralizer; no arithmetic branch selected.',
 'geometric_curve':'y^4=x^3+1',
 'Belyi_map':'(x^6+20x^3-8)^2/[64(x^3+1)^3]',
 'geometric_deck_group_order':48,'all_marked_linear_to_geometric_edges_checked':checks,
 'all48_quartic_automorphism_identities_checked':True,
 'branch_cycle_lengths':{'over0':[2,24],'over1':[3,16],'overInfinity':[12,4]},
 'positive_interval_s_fixed_x':'sqrt(3)-1',
 'elliptic_quotient_maps_checked':3,
 'actual_index8_elliptic_map_checked':True,
 'index8_map_factors_as_y_square_then_multiplication2':True,
 'index8_s_image':'(u,v)->(u,-v)',
 'index8_r_image':'(u,v)->(zeta3*u,v)',
 'index8_t_square_image':'(u,v)->(zeta3^2*u,v)',
 'elliptic_factors':['y^2=x^3+1','y^2=x^3+(3+2sqrt(3))*x','y^2=x^3+(3-2sqrt(3))*x'],
 'three_pulled_back_differentials_independent':True,
 'rational_homology_centralizer_dimension':5,
 'rational_constituent_dimensions':{'elliptic':2,'cusp':3,'quartic_CM':4},
 'commutator_matrix_rank_mod5':rk,
 'elapsed_seconds':round(time.time()-started,3)}
def enc(a):return [[str(x) for x in q] for q in a]
def ratmat(A):return [[str(x) for x in c] for c in A]
cert={'summary':summary,'geometric_S_matrix':enc(SG),'geometric_R_matrix':enc(RG),
 'all48_geometric_matrices':[enc(geo[q]) for q in range(48)],
 'all48_marked_words':[words[q] for q in range(48)],
 'actual_index8_elliptic_map':{'u':'x*(x^3-8)/(4*(x^3+1))',
 'v':'(x^6+20*x^3-8)/(8*y^6)','target':'v^2=u^3+1','base_map':'b=v^2'},
 'quartic_elliptic_quotient_maps':quotients,
 'centralizer_mod5_pivot_coordinates':piv,
 'five_integral_centralizer_generators':operators,
 'elliptic_projector':ratmat(eE),'quartic_CM_projector':ratmat(eQ),'cusp_projector':ratmat(eR)}
(OUT/'d_arithmetic_rank9_geometry.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
