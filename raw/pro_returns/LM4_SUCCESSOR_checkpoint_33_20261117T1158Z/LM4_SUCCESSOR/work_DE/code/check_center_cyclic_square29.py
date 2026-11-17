#!/usr/bin/env python3
"""Exact marked words and symbolic inverse recurrence; no orbit census."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def red(w):
 r=[]
 for x in w:
  if r and r[-1]==-x:r.pop()
  else:r.append(x)
 return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
def conj(a,b):return mul(a,b,inv(a))
def test(name,ok):
 assert ok,name
 checks.append(name)
 print('PASS',name)
def member(w):
 state=0
 for x in red(w):
  if abs(x)==1:state=1-state
  elif state==0:pass
  else:return False
 return state==0
reps=[]
def cid(w):
 w=red(w)
 for i,v in enumerate(reps):
  if member(mul(inv(v),w)):return i+1
 reps.append(w);return len(reps)
def act(t,n):return red((1 if x>0 else -1)*cid(mul(t,reps[abs(x)-1])) for x in n)
def pmul(p,q):return (mul(p[0],act(p[1],q[0])),mul(p[1],q[1]))
def pinv(p):
 t=inv(p[1]);return (act(t,inv(p[0])),t)
def peval(w,ims):
 o=((),())
 for x in w:o=pmul(o,ims[x] if x>0 else pinv(ims[-x]))
 return o
# Auxiliary free basis h,a,d,e,V=1,2,3,4,5.
h=((),(1,));a=((),(2,));d=((),(3,));e=((),(4,));V=((),(5,));k=((cid(()),),())
f=pmul(h,pinv(k));B=pmul(pmul(f,V),pinv(f))
test('B=h V h^-1 in the exact coset semidirect model',B==((),(1,5,-1)))
for name,g in [('h^2',pmul(h,h)),('a',a),('d',d),('e',e),('V',V)]:
 test('actual centralizing relation k/'+name,pmul(k,g)==pmul(g,k))
# Original K basis a,B,d,e,f=1,2,3,4,5.
A=(1,);BB=(2,);DD=(3,);EE=(4,);FF=(5,)
VV=mul(inv(FF),BB,FF);D=conj(DD,EE)
w=mul(A,FF,VV,inv(FF),inv(A),FF,D,inv(FF),inv(DD))
eta_a=mul(A,BB,inv(A),inv(BB),inv(A))
P=mul(A,BB,FF,DD,EE,inv(DD),inv(FF),inv(DD))
eta_f=conj(P,inv(FF));eta_ell=conj(eta_a,eta_f)
test('whole marked eta(ell)=w f^-1 w^-1',eta_ell==conj(w,inv(FF)))
W=(2,1,5,-1,-2,1,3,4,-3,-1,-3)
ims={1:a,2:B,3:d,4:e,5:f}
test('entire w has zero center correction',peval(w,ims)==((),W))
q=peval(inv(eta_ell),ims);r=conj(W,(1,));Y0=cid(W);Y1=cid(mul(W,(1,)))
test('actual square q=Y1^-1 r',q==((-Y1,),r))
test('r exchanges the two correction cosets',cid(mul(r,W))==Y1 and cid(mul(r,W,(1,)))==Y0)
test('correction cosets distinct',Y0!=Y1)
test('core input h2 belongs while h does not',member((1,1)) and not member((1,)))
test('W is reduced with exact missing-edge prefix and final d inverse',red(W)==W and W[:3]==(2,1,5) and W[-1]==-3)
test('W and Wh are outside the core subgroup',not member(W) and not member(mul(W,(1,))))
# Generic inverse recurrence. c_n has formal generator 100+n; u0,u1 are1,2.
c=lambda n:(100+n,)
u0=(1,);u1=(2,)
beta_u1=mul(inv(c(1)),inv(u1),inv(c(0)),u0,c(0),u1,c(1))
betainv_u0=conj(mul(c(-1),u0,c(0)),u1)
def apply(w,sgn):
 images={1:u1 if sgn==1 else betainv_u0,2:beta_u1 if sgn==1 else u0}
 for n in range(-4,5):images[100+n]=c(n+sgn)
 return mul(*(images[x] if x>0 else inv(images[-x]) for x in w))
for name,u in [('u0',u0),('u1',u1)]:
 test('beta beta^-1 on '+name,apply(apply(u,-1),1)==u)
 test('beta^-1 beta on '+name,apply(apply(u,1),-1)==u)
test('exact generic mixed square recurrence',conj(mul(c(0),u1,c(1)),beta_u1)==u0)
proof=ROOT/'work_DE/next_marginal_source/center_cyclic_square_normalization29.md'
out={'status':'PASS_EXACT_MARKED_INPUT_AND_SYMBOLIC_RECURRENCE','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'checks':checks,'original_K_basis':['a','B','d','e','f'],'w':w,'eta_a':eta_a,'eta_f':eta_f,'eta_ell':eta_ell,'auxiliary_basis':['h','a','d','e','V'],'W':W,'r':r,'q_center_word':q[0],'q_retained_word':q[1],'coset_representatives':reps,'beta_u1':beta_u1,'beta_inverse_u0':betainv_u0,'scope':'No exponent/depth census. The all-integer coset separation, basis change, discontinuity and complete-presentation conclusions are proved in the companion source.'}
p=ROOT/'work_DE/next_marginal_source/center_cyclic_square29.json'
assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('TOTAL',len(checks))
