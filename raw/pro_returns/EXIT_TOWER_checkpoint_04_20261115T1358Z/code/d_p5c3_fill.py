"""Exact relator certificates for the compact26-relator Gamma0,6 presentation.
Returns a normal form and a list of conjugate relators whose free product
is word * normal_form^-1. Every relator index is D.25's fixed index.
"""
from pathlib import Path
from functools import lru_cache
import json,ast,random
P=Path(__file__).resolve().parent
B={};tree=ast.parse((P/'b_genus_zero.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'b_genus_zero','exec'),B)
red,inv,subst=B['red'],B['inv'],B['subst']
def cat(*ws):return red(x for w in ws for x in w)
data=json.loads((P/'d_p5c3_identities.json').read_text());RELS=list(map(tuple,data['relators']))
compact=json.loads((P/'b_genus_zero.json').read_text())['compact']
def conjugate(c,S):return tuple((cat(c,p),j,e) for p,j,e in S)
def inverse(S):return tuple((p,j,-e) for p,j,e in reversed(S))
def reduce_sequence(S):
 out=[]
 for a in S:
  if out and out[-1][:2]==a[:2] and out[-1][2]==-a[2]:out.pop()
  else:out.append(a)
 return tuple(out)
def expanded(S):return red(x for c,j,e in S for x in c+(RELS[j] if e>0 else inv(RELS[j]))+inv(c))
# Global-letter actions at the two free-by-free stages.
phi5={}
for h in (1,2):
 phi5[h]=[inv(RELS[3*(h-1)+u][3:]) for u in range(3)]
 hbraid=tuple(compact['M05_braid_words'][h-1]);ivs=[]
 for u in range(3):
  ubraid=tuple(compact['M05_braid_words'][u+2]);w=cat(inv(hbraid),ubraid,hbraid)
  cw=B['comb'](4,w);assert all(j==4 for i,j,e in cw)
  ivs.append(tuple((i+2)*e for i,j,e in cw))
 phi5[-h]=ivs
phi9={}
for h in range(1,6):
 for sign,key in ((1,'M06_actions'),(-1,'M06_inverse_actions')):
  phi9[sign*h]=[tuple((abs(x)+5)*(1 if x>0 else -1) for x in w) for w in compact[key][h-1]]
class Stage:
 def __init__(self,first,last,ph,indices,lower):self.first=first;self.last=last;self.ph=ph;self.indices=indices;self.lower=lower
 def phi(self,h,w):return cat(*(self.ph[h][abs(x)-self.first] if x>0 else inv(self.ph[h][abs(x)-self.first]) for x in w))
 @lru_cache(maxsize=100000)
 def D(self,h,v):
  if h<0:return conjugate((h,),inverse(self.D(-h,self.phi(h,v))))
  out=[];prefix=()
  for x in v:
   z=self.phi(h,(abs(x),));idx=self.indices[h,abs(x)]
   out.append((prefix if x>0 else cat(prefix,inv(z)),idx,1 if x>0 else -1))
   prefix=cat(prefix,self.phi(h,(x,)))
  return tuple(out)
 @lru_cache(maxsize=100000)
 def normalize(self,w):
  u=();v=();cert=[]
  for x in w:
   if abs(x)>=self.first:v=cat(v,(x,));continue
   vnew=self.phi(-x,v)
   cert.extend(conjugate(u,inverse(self.D(x,vnew))))
   u,basecert=self.lower(cat(u,(x,)));cert.extend(basecert)
   v=vnew
  return cat(u,v),reduce_sequence(cert)
def free_normal(w):return red(w),()
S5=Stage(3,5,phi5,{(h,u):3*(h-1)+u-3 for h in (1,2) for u in range(3,6)},free_normal)
S9=Stage(6,9,phi9,{(h,u):6+4*(h-1)+u-6 for h in range(1,6) for u in range(6,10)},S5.normalize)
def normal(w):return S9.normalize(red(w))
def fill(w):
 w=red(w);nf,cert=normal(w);assert not nf,('word is not identity',w,nf)
 assert expanded(cert)==w,('certificate failed',w)
 return cert
if __name__=='__main__':
 for h in (1,2):
  for u in range(3,6):
   assert S5.phi(h,S5.phi(-h,(u,)))==(u,)
   assert S5.phi(-h,S5.phi(h,(u,)))==(u,)
 for h in range(1,6):
  for u in range(6,10):
   assert S9.phi(h,S9.phi(-h,(u,)))==(u,)
   assert S9.phi(-h,S9.phi(h,(u,)))==(u,)
 sizes=[]
 for r in RELS:sizes.append(len(fill(r)))
 rng=random.Random(63024)
 for z in range(20):
  w=tuple(rng.choice(tuple(range(1,10))+tuple(range(-9,0))) for _ in range(8));nf,cert=normal(w)
  assert expanded(cert)==cat(w,inv(nf));assert normal(nf)[0]==nf
  r=RELS[rng.randrange(26)];p=rng.randrange(len(w)+1);other=cat(w[:p],r,w[p:])
  assert normal(other)[0]==nf
 out={'relators':RELS,'defining_relator_certificate_sizes':sizes,'random_contextual_checks':20,'convention':'certificate expansion is word*normal^-1; normal is F2 word followed by F3 word followed by F4 word'}
 (P/'d_p5c3_fill.json').write_text(json.dumps(out,indent=2)+'\n')
 print('All26 compact relators have exact freely checked certificates; sizes:',sizes)
 print('All52 signed action inverses and20 seeded full normal-form/certificate/context checks passed.')
