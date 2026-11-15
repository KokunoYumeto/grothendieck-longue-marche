"""Exact parabolic extraction in the central quotient of A(D4).
Positive orthogonal fraction reduction strips common left atoms. Every
step is checked by the classical Garside normal form. No membership
claim is made when the finite central-exponent search returns None.
"""
from pathlib import Path
import importlib.util,json
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('d4',P/'d_artin_d4.py')
D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
def positive_word(nf):
 p,f=nf
 assert p>=0
 return D.DELTA*p+tuple(x for a in f for x in D.reps[D.W[a]])
def left_atoms(w):
 p,f=D.normal(tuple(w))
 assert p>=0
 if p:return set(range(1,5))
 if not f:return set()
 return {i+1 for i,g in enumerate(D.gen) if g in D.leftdiv[f[0]]}
def orthogonal(w):
 p,f=D.normal(tuple(w))
 if p>=0:return (),positive_word((p,f))
 u=D.DELTA*(-p);v=positive_word((0,f))
 while True:
  common=left_atoms(u)&left_atoms(v)
  if not common:break
  a=min(common)
  u=positive_word(D.normal((-a,)+u))
  v=positive_word(D.normal((-a,)+v))
 assert D.equal(D.cat(D.inv(u),v),tuple(w),False)
 return u,v
def extract(w,allowed,central_bound=5):
 for k in sorted(range(-central_bound,central_bound+1),key=lambda k:(abs(k),k)):
  word=D.cat(tuple(w),D.DELTA*k if k>=0 else D.inv(D.DELTA)*(-k))
  u,v=orthogonal(word)
  if set(u+v)<=set(allowed):
   out=D.cat(D.inv(u),v)
   assert D.equal(out,tuple(w))
   return out,k
 return None
if __name__=='__main__':
 q1=(2,4,3,2,4,2);q2=(1,4,3,1,4,1);q3=(1,4,2,1,4,1)
 source=D.cat(D.inv(q2),D.inv(q3));ans=extract(source,(2,3,4))
 print('S1 q2^-1 q3^-1 =',ans,flush=True)
 if ans:
  out=dict(source=source,target_word=ans[0],central_adjustment=ans[1],verified=True)
  (P/'b_d4_parabolic.json').write_text(json.dumps(out,indent=2)+'\n')
