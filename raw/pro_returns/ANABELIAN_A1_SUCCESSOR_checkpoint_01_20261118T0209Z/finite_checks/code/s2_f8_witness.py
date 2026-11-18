"""Exact F8 cyclic-19 class-number certificate for every rational base point.

Curve y^2+(x^2+x)y=x^5+1.  Generalized Cantor arithmetic in characteristic
two is implemented here directly, independently of the checkpoint code.
The finite group is exhaustively enumerated and its entire table checked.
"""
from pathlib import Path
import json,itertools,time
import sympy as sp
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx

out=Path(__file__).resolve().parent;t0=time.time()
Fp=fmpz_mod_poly_ctx(2);mod=Fp([1,1,0,1])
k=fq_default_ctx(modulus=mod,var='t',fq_type='FQ_NMOD');R=fq_default_poly_ctx(k);x=R.gen()
els=[k([(a>>i)&1 for i in range(3)]) for a in range(8)]
def enc(a):return sum(int(c)<<i for i,c in enumerate(a.to_list()))
def ep(a):return tuple(enc(c) for c in a.coeffs())
def key(D):return ep(D[0]),ep(D[1])
h=x*x+x;f=x**5+1;O=(R(1),R(0))
def exact(a,b):
 q,r=divmod(a,b);assert not r;return q
def valid(D):
 u,v=D
 return u.is_monic() and u.degree()<=2 and v.degree()<u.degree() and not ((v*v+h*v+f)%u)
def add(D,E):
 u1,v1=D;u2,v2=E
 d0,e1,e2=u1.xgcd(u2)
 d,c1,c2=d0.xgcd(v1+v2+h)
 a1=c1*e1;a2=c1*e2;a3=c2
 u=exact(u1*u2,d*d)
 v=exact(a1*u1*v2+a2*u2*v1+a3*(v1*v2+f),d)%u
 while u.degree()>2:
  u=exact(f+h*v+v*v,u).monic();v=(h+v)%u
 u=u.monic();v=v%u
 assert valid((u,v))
 return u,v
def neg(D):return D[0],(h+D[1])%D[0]
def scale(D,n):
 z=O
 while n:
  if n&1:z=add(z,D)
  D=add(D,D);n>>=1
 return z

# Full set of reduced Mumford representatives, including nonsplit supports.
J=[O]
for d in (1,2):
 for aa in itertools.product(els,repeat=d):
  u=R(list(aa)+[k(1)])
  for bb in itertools.product(els,repeat=d):
   v=R(list(bb))
   if not ((v*v+h*v+f)%u):J.append((u,v))
assert len(J)==76
index={key(D):i for i,D in enumerate(J)};assert len(index)==76
table=[[index[key(add(D,E))] for E in J] for D in J]
for i in range(76):
 assert table[0][i]==i==table[i][0]
 assert table[i][index[key(neg(J[i]))]]==0
 for j in range(76):
  assert table[i][j]==table[j][i]
  for z in range(76):assert table[table[i][j]][z]==table[i][table[j][z]]
def ptD(pt):return O if pt is None else (x+els[pt[0]],R(els[pt[1]]))
points=[(enc(a),enc(b)) for a in els for b in els if b*b+(a*a+a)*b==a**5+1]+[None]
assert len(points)==9 and (0,1) in points and (1,0) in points
four=[scale(D,4) for D in J];odd=set(map(key,four));assert len(odd)==19
H=[D for D in J if key(scale(D,4))==key(O)];assert len(H)==4
G=next(D for D in four if key(D)!=key(O))
logs={key(scale(G,j)):j for j in range(19)};assert len(logs)==19
chi=[logs[key(scale(D,4))] for D in J]
for i in range(76):
 for j in range(76):assert chi[table[i][j]]==(chi[i]+chi[j])%19

z,T=sp.symbols('z T');phi=sum(z**j for j in range(19));certs=[]
for base in points:
 B=ptD(base); exps=[chi[index[key(add(ptD(pt),neg(B)))]] for pt in points]
 occ=[exps.count(j) for j in range(19)]
 kap=chi[index[key(neg(scale(B,2)))]] # K ~2 O.
 L1=1+sum(z**j for j in exps)+8*z**kap
 rel=int(sp.resultant(phi,L1,z));assert rel>0 and rel%2
 theta=sp.Poly(1+sum(z**j for j in exps),z, modulus=2)
 assert sp.gcd(sp.Poly(phi,z,modulus=2),theta).degree()==0
 certs.append({'base_point':base,'points':points,'exponents':exps,'occupancies':occ,
  'canonical_twist_exponent':kap,'L_at_1_coefficients':[int(sp.expand(L1).coeff(z,i)) for i in range(19)],
  'relative_class_number':str(rel),'total_cover_class_number':str(76*rel),
  'relative_class_number_mod2':rel%2})

# Independent elementary point counts in binary polynomial fields, F8 and F64.
def gf_mul(a,b,poly):
 ans=0;d=poly.bit_length()-1
 while b:
  if b&1:ans^=a
  a<<=1;b>>=1
  if a>>d:a^=poly
 return ans
def gp(a,n,poly):
 y=1
 while n:
  if n&1:y=gf_mul(y,a,poly)
  a=gf_mul(a,a,poly);n>>=1
 return y
def count(poly):
 q=1<<(poly.bit_length()-1)
 assert all(gp(a,q-1,poly)==1 for a in range(1,q))
 return 1+sum(gf_mul(b,b,poly)^gf_mul(gf_mul(a,a,poly)^a,b,poly)==gp(a,5,poly)^1 for a in range(q) for b in range(q))
counts={str(n):count(poly) for n,poly in [(1,3),(2,7),(3,11),(6,67)]}
assert counts=={'1':3,'2':3,'3':9,'6':87}
assert (counts['3']**2+counts['6'])//2-8==76
PQ=add(ptD((0,1)),neg(ptD((1,0))))
assert key(PQ)!=key(O) and key(scale(PQ,2))==key(O)
answer={'verified':True,'curve':'y^2+(x^2+x)y=x^5+1','field_modulus':[1,1,0,1],
 'field_encoding':'integer binary coefficients in 1,t,t^2','point_counts':counts,
 'jacobian_order':76,'genus':2,'cover_degree':19,'cover_genus':20,
 'primitive_root_order_2_mod_19':next(n for n in range(1,19) if pow(2,n,19)==1),
 'Mumford_representatives':[key(D) for D in J],'addition_table':table,
 'two_primary_subgroup':[key(D) for D in H],'odd_generator':key(G),'character_table':chi,
 'P_minus_Q':key(PQ),'P_minus_Q_order':2,'certificates':certs,'seconds':time.time()-t0,
 'cover_specification':'Pull back (F_8-1):J/H -> J along R |-> [R-B], where H=J(F8)[2^infinity] acts on the Lang source by translations; degree 19, choose 0+H above B.'}
(out/'s2_f8_witness.json').write_text(json.dumps(answer,indent=2)+'\n')
print('ALL CHECKS PASS; #C(F8)=9; #C(F64)=87; #J(F8)=76; cyclic degree19 cover genus20')
for c in certs:print('BASE',c['base_point'],'EXPONENTS',c['exponents'],'RELATIVE CLASS NUMBER',c['relative_class_number'])
print('seconds',time.time()-t0)
