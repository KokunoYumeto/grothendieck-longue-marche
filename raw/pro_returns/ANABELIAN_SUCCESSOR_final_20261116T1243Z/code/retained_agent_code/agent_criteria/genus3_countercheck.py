from itertools import product, combinations_with_replacement
import json
# Polynomials over F_2 encoded in binary.
def deg(a): return a.bit_length()-1
def mul(a,b):
 r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
 return r
def divmodp(a,b):
 q=0
 while a and deg(a)>=deg(b):
  s=deg(a)-deg(b);q^=1<<s;a^=b<<s
 return q,a
def mod(a,b):return divmodp(a,b)[1]
def gcdex(a,b):
 x0,x1,y0,y1=1,0,0,1
 while b:
  q,r=divmodp(a,b);a,b=b,r;x0,x1=x1,x0^mul(q,x1);y0,y1=y1,y0^mul(q,y1)
 return a,x0,y0
def exact(a,b):
 q,r=divmodp(a,b)
 assert not r,(a,b,r)
 return q
class Jac:
 def __init__(self,f,g):
  self.f=f;self.g=g; self.zero=(1,0)
  self.elts=[(u,v) for d in range(g+1) for u in range(1<<d,1<<(d+1)) for v in range(1<<d) if mod(mul(v,v)^v^f,u)==0]
  assert len(self.elts)==len(set(self.elts))
 def add(self,D,E):
  u1,v1=D;u2,v2=E
  d1,e1,e2=gcdex(u1,u2);d,c1,c2=gcdex(d1,v1^v2^1)
  s1=mul(c1,e1);s2=mul(c1,e2);s3=c2
  u=exact(mul(u1,u2),mul(d,d))
  num=mul(mul(s1,u1),v2)^mul(mul(s2,u2),v1)^mul(s3,mul(v1,v2)^self.f)
  v=mod(exact(num,d),u)
  while deg(u)>self.g:
   up=exact(mul(v,v)^v^self.f,u)
   v=mod(v^1,up);u=up
  return u,v
 def scale(self,D,n):
  R=self.zero
  while n:
   if n&1:R=self.add(R,D)
   n>>=1;D=self.add(D,D)
  return R
 def quotient3(self):
  H={self.scale(D,3) for D in self.elts}
  if len(H)*3!=len(self.elts):return None
  a=next(D for D in self.elts if D not in H)
  ca={self.add(a,h) for h in H}; cb={self.add(a,x) for x in ca}
  assert len(H|ca|cb)==len(self.elts)
  return {x:i for i,coset in enumerate((H,ca,cb)) for x in coset}
 def verify(self):
  S=set(self.elts)
  for a in S:
   assert self.add(a,self.zero)==a
   assert self.add(a,(a[0],mod(a[1]^1,a[0])))==self.zero
   for b in S:
    assert self.add(a,b) in S
    assert self.add(a,b)==self.add(b,a)
  for a,b,c in product(S,repeat=3):
   assert self.add(self.add(a,b),c)==self.add(a,self.add(b,c))
def bits_eval(f,x):
 r=0
 for i in range(deg(f),-1,-1):r=(r*x)^((f>>i)&1)
 return r

def example(f):
 J=Jac(f,3);chi=J.quotient3()
 if chi is None:return
 # points: infinity and pairs (x,0),(x,1) exactly when f(x)=0.
 points=[J.zero]+[(2|x,y) for x in range(2) if bits_eval(f,x)==0 for y in range(2)]
 N=[sum(chi[a]==i for a in points) for i in range(3)]
 # Closed points of degree two. Two kinds: rational-x hyperelliptic fibres,
 # and irreducible-x Mumford divisors (u=x^2+x+1).
 closed2=[J.zero for x in range(2) if bits_eval(f,x)==1]+[(7,v) for v in range(4) if mod(mul(v,v)^v^f,7)==0]
 E2=[J.add(a,b) for a,b in combinations_with_replacement(points,2)]+closed2
 c2=[sum(chi[a]==i for a in E2) for i in range(3)]
 # F_4 reduction: zeta^2=zeta+1. L(chi,1) = 1+S1+S2 mod2.
 reduce=lambda a:((a[0]-a[2]),(a[1]-a[2]))
 s1=reduce(N); s2=reduce(c2)
 point=((1+s1[0])%2,s1[1]%2)
 full=((1+s1[0]+s2[0])%2,(s1[1]+s2[1])%2)
 if full==(0,0) and point!=(0,0):
  J.verify()
  generator=(2,0)
  powers=[J.scale(generator,i) for i in range(27)]
  assert len(set(powers))==27 and J.scale(generator,27)==J.zero
  assert J.scale(generator,6)==(3,0)
  assert all(chi[J.add(a,b)]==(chi[a]+chi[b])%3 for a,b in product(J.elts,repeat=2))
  # all such f have kappa=0, so a_3=2*a_1(chi^-1), a_4=4.
  a1=s1;a2=s2;a3=(2*(N[0]-N[1]),2*(N[2]-N[1]));a4=(4,0)
  lv=(1+a1[0]+a2[0]+a3[0]+4,a1[1]+a2[1]+a3[1])
  norm=lv[0]*lv[0]-lv[0]*lv[1]+lv[1]*lv[1]
  return {'f_binary':f,'f_terms':[i for i in range(8) if (f>>i)&1],'J_order':len(J.elts),'points_Mumford':points,'chi_on_points':[chi[a] for a in points],'N_b':N,'degree2_counts':c2,'L_coeff_pairs_in_Z_zeta3':[(1,0),a1,a2,a3,a4],'L_at_1':lv,'relative_class_number':norm,'point_only_mod2':point,'correct_L_mod2_at_1':full,'generator_Mumford':generator,'generator_order':27,'point_1_0_discrete_log':6,'character_homomorphism_checks':len(J.elts)**2,'group_law_exhaustive_associativity_checks':len(J.elts)**3,'chi_table':[[*a,v] for a,v in chi.items()]}

out=[]
for f in range(128,256):
 r=example(f)
 if r:out.append(r);break
assert out
print(json.dumps(out,indent=2))
