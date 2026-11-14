#!/usr/bin/env python3
"""Independent full class-two word checks for the actual correction formulas.

The groups tested have abelian exponent4/8 and commutator exponent2/4.
The marked cyclic action has t^36=Int(c), keeping the actual cusp term.
This is a universal word verification, not an exponent-eight arithmetic lift.
"""
from pathlib import Path
import json,time
import numpy as np

OUT=Path(__file__).resolve().parent
start=time.time()

class Hall:
 def __init__(self,d,e):
  self.d=d;self.e=e;self.m=e//2
  self.pairs=[(i,j) for i in range(d) for j in range(i+1,d)]
 def identity(self):return (np.zeros(self.d,dtype=np.int64),np.zeros(len(self.pairs),dtype=np.int64))
 def generator(self,i):
  a,c=self.identity();a[i]=1;return a,c
 def product(self,x,y):
  a,c=x;b,d=y
  cross=np.array([int(a[i])*int(b[j]) for i,j in self.pairs],dtype=np.int64)
  return (a+b)%self.e,(c+d+cross)%self.m
 def inverse(self,x):
  a,c=x
  return (-a)%self.e,(-c+np.array([int(a[i])*int(a[j]) for i,j in self.pairs]))%self.m
 def equal(self,x,y):return np.array_equal(x[0],y[0]) and np.array_equal(x[1],y[1])
 def products(self,words):
  v=self.identity()
  for w in words:v=self.product(v,w)
  return v
 def conjugate(self,a,b):return self.products([a,b,self.inverse(a)])
 def commutator(self,a,b):return self.products([a,b,self.inverse(a),self.inverse(b)])
 def power(self,a,n):
  if n<0:return self.power(self.inverse(a),-n)
  out=self.identity()
  for _ in range(n):out=self.product(out,a)
  return out
 def serialize(self,x):return {'abelian':x[0].tolist(),'commutator':x[1].tolist()}

rows=[]
for exponent in [4,8]:
 H=Hall(37,exponent);u=[H.generator(i) for i in range(36)];c=H.generator(36)
 # A literal cyclic word with the actual nontrivial cusp conjugation at wrap.
 images=u[1:]+[H.conjugate(c,u[0])]
 b=H.products(u);tb=H.products(images)
 delta=H.product(b,H.inverse(tb))
 expected=H.product(H.commutator(u[0],H.products(u[1:])),H.inverse(H.commutator(c,u[0])))
 assert H.equal(delta,expected)
 assert not np.any(delta[0])
 # Full signs are checked by the Hall columns, before reducing the cusp term.
 central=np.zeros(len(H.pairs),dtype=np.int64)
 for k,pair in enumerate(H.pairs):
  if pair[0]==0 and 1<=pair[1]<=35:central[k]=1
  if pair==(0,36):central[k]=1
 assert np.array_equal(delta[1],central%H.m)
 # The torsion correction uses an actual swap of the two marked generators.
 bs=H.product(u[0],u[1]);sbs=H.product(u[1],u[0])
 ds=H.product(bs,H.inverse(sbs));assert H.equal(ds,H.commutator(u[0],u[1]))
 # Verify that no higher commutator or square term was silently discarded.
 rng=np.random.default_rng(0xD62+exponent)
 associativity=0;commutator_bilinearity=0;exponent_checks=0
 for _ in range(40):
  xs=[]
  for j in range(3):
   xs.append((rng.integers(0,exponent,37,dtype=np.int64),rng.integers(0,H.m,len(H.pairs),dtype=np.int64)))
  x,y,z=xs
  assert H.equal(H.product(H.product(x,y),z),H.product(x,H.product(y,z)));associativity+=1
  assert H.equal(H.commutator(x,H.product(y,z)),H.product(H.commutator(x,y),H.commutator(x,z)));commutator_bilinearity+=1
  assert H.equal(H.power(x,exponent),H.identity());exponent_checks+=1
  assert H.equal(H.product(x,H.inverse(x)),H.identity())
 rec={'abelian_exponent':exponent,'commutator_exponent':H.m,'free_generators':37,
  'cyclic_word_factors':36,'cusp_wrap_kept':True,'cusp_word_identity_checked':True,
  'source_s_word_identity_checked':True,'actual_cusp_correction':H.serialize(delta),
  'actual_s_correction':H.serialize(ds),'associativity_checks':associativity,
  'commutator_bilinearity_checks':commutator_bilinearity,'exponent_checks':exponent_checks}
 rows.append(rec)
 print(json.dumps({k:v for k,v in rec.items() if not isinstance(v,dict)}),flush=True)

result={'summary':{'status':'PASS','coefficient_exponents':[4,8],
 'exact_cusp_and_involution_word_identities':True,
 'commutator_convention':'[a,b]=a*b*a^(-1)*b^(-1)',
 'scope':'Universal class-two identities; no exponent-eight arithmetic lift asserted.',
 'elapsed_seconds':time.time()-start},'cases':rows}
(OUT/'d_self_wedge_word_identities.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
