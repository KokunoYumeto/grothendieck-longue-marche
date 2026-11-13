#!/usr/bin/env python3
"""Exact abelian-pure GT-shadow audit. Python standard library only.
Q_n(m)=B_n/([PB_n,PB_n] PB_n^m).
A braid is its endpoint permutation and signed crossing vector modulo 2m.
For each unordered pair of initial labels, the crossing parity is prescribed
by the endpoint permutation. Thus |Q_n(m)|=n! m^(n choose 2).
This executes every Q_3(m) of order <=1000, i.e. m=1,...,5.
It does NOT claim to enumerate all finite quotients of B_3 of that order.
"""
import itertools,math,json,pathlib,time
start=time.time()
class Q:
 def __init__(self,n,m):
  self.n,self.m,self.mod=n,m,2*m
  self.pairs=list(itertools.combinations(range(n),2));self.idx={p:i for i,p in enumerate(self.pairs)}
  self.one=(tuple(range(n)),(0,)*len(self.pairs))
  self.gs=[]
  for i in range(n-1):
   p=list(range(n));p[i],p[i+1]=p[i+1],p[i]
   v=[0]*len(self.pairs);v[self.idx[(i,i+1)]]=1
   self.gs.append((tuple(p),tuple(v)))
 def mul(self,g,h):
  p,c=g;q,d=h
  out=list(c)
  for (i,j),v in zip(self.pairs,d):out[self.idx[tuple(sorted((p[i],p[j])))]]+=v
  return tuple(p[q[i]] for i in range(self.n)),tuple(v%self.mod for v in out)
 def inv(self,g):
  p,c=g;q=[0]*self.n
  for i,j in enumerate(p):q[j]=i
  out=[0]*len(self.pairs)
  for (i,j),v in zip(self.pairs,c):out[self.idx[tuple(sorted((q[i],q[j])))]]=-v%self.mod
  return tuple(q),tuple(out)
 def power(self,g,k):
  if k<0:g,k=self.inv(g),-k
  z=self.one
  while k:
   if k&1:z=self.mul(z,g)
   g=self.mul(g,g);k//=2
  return z
 def product(self,*gs):
  z=self.one
  for g in gs:z=self.mul(z,g)
  return z
 def scale(self,g,lam):return g[0],tuple(lam*v%self.mod for v in g[1])
 def elements(self):
  seen={self.one};seq=[self.one]
  for g in seq:
   for a in self.gs:
    h=self.mul(g,a)
    if h not in seen:seen.add(h);seq.append(h)
  return seq
rows=[]
for m in range(1,6):
 q=Q(3,m);els=q.elements();a,b=q.gs
 assert len(els)==6*m**3<=1000
 assert q.product(a,b,a)==q.product(b,a,b)
 x12=q.power(a,2);x23=q.power(b,2);x13=q.product(b,x12,q.inv(b))
 z=q.power(q.mul(a,b),3)
 actual=[];checks=0
 for k in range(m):
  lam=2*k+1
  if math.gcd(lam,m)!=1:continue
  assert math.gcd(lam,2*m)==1
  images=[q.scale(g,lam) for g in els]
  assert len(set(images))==len(els)
  for g in els:
   for s in q.gs:
    assert q.scale(q.mul(g,s),lam)==q.mul(q.scale(g,lam),q.power(s,lam));checks+=1
  assert q.scale(z,lam)==q.power(z,lam)
  # Exact two hexagons in the abelian pure setting (DLL Appendix B).
  assert q.product(a,q.power(x12,k),b,q.power(x23,k))==q.product(a,b,q.power(q.mul(x13,x23),k))
  assert q.product(b,q.power(x23,k),a,q.power(x12,k))==q.product(b,a,q.power(q.mul(x12,x13),k))
  # Arity four: f=1 makes the pentagon literally 1=1; scalar crossing
  # multiplication is a homomorphism and commutes with crossing duplication
  # under cabling. Verify braid/commutation relations and all generators.
  q4=Q(4,m)
  for i in range(2):
   s,t=q4.gs[i:i+2]
   assert q4.product(s,t,s)==q4.product(t,s,t)
   assert q4.scale(q4.product(s,t,s),lam)==q4.product(q4.power(s,lam),q4.power(t,lam),q4.power(s,lam))
  assert q4.mul(q4.gs[0],q4.gs[2])==q4.mul(q4.gs[2],q4.gs[0])
  for s in q4.gs:assert q4.scale(s,lam)==q4.power(s,lam)
  actual.append({'m_parameter':k,'lambda_mod_2m':lam,'f':'identity','genuine':True})
 row={'m':m,'B3_quotient_order':len(els),'B4_compatible_quotient_order':24*m**6,'N_ord':m,'all_charming_shadows':actual,'number_of_shadows':len(actual),'all_are_genuine':'DLL Appendix B theorem; independently via cyclotomic surjectivity','Cayley_edge_checks':checks,'hexagons':True,'pentagon_f_equals_1':True,'full_twist_formula':True}
 rows.append(row);print(row)
result={'family':'B_n / ([PB_n,PB_n] PB_n^m)','B3_bound':1000,'m_values':[1,2,3,4,5],'first_excluded_order':6*6**3,'scope':'All charming shadows, hence all genuine shadows, in this declared family; not all finite quotients of B3. Non-charming fake shadows are not enumerated.','rows':rows,'seconds':round(time.time()-start,4)}
base=pathlib.Path(__file__).with_suffix('');base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Total genuine shadows:',sum(r['number_of_shadows'] for r in rows),'seconds',result['seconds'])
