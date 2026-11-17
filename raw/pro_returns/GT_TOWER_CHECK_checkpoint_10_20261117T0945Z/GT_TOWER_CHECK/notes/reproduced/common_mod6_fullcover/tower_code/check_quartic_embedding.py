#!/usr/bin/env python3
"""Exact words for the division-quartic modular pullback in B4/Z.

The braid/free-kernel isomorphism is checked algebraically. Identification
with the geometric division-quartic marking requires its peripheral
orientation comparison, which is recorded separately in the proof.
"""
from check_tower_braid_identities import artin,mul,inv,power,subst
from pathlib import Path
import json
a=(1,);b=(2,);c=(3,)
x=mul(c,inv(a));y=mul(a,b,a,inv(c),inv(b),inv(a))
u=mul(a,b,c);d=mul(a,a,b,c);omega=power(u,4)
s=power(u,2);r=inv(d);tau=mul(s,r)
p=mul(s,power(tau,-3));p1=mul(tau,p,inv(tau))
checks={
 'd cubed is full twist':(power(d,3),omega),
 'tau word':(tau,mul(a,b,c,inv(a))),
 'tau Ferrari form':(tau,mul(inv(y),a,b)),
 's Ferrari form':(s,mul(inv(x),inv(y),power(mul(a,b),3))),
 'p image':(p,mul(x,y)),
 'p1 image':(p1,mul(inv(y),x,y)),
 'recover y':(y,mul(p,inv(p1))),
 'recover x':(x,mul(p,p1,inv(p)))
}
for name,(left,right) in checks.items():
 assert artin(4,left)==artin(4,right),name
 print('PASS',name,flush=True)
# The peripheral word is read in the free Ferrari kernel after removing
# the central full twist. Find its exact based commutator comparison.
cusp=mul(power(tau,6),inv(omega))
comm=mul(x,y,inv(x),inv(y))
found=[]
for label,v in [('1',()),('x',x),('y',y),('xy',mul(x,y)),('yx',mul(y,x)),
                ('x^-1',inv(x)),('y^-1',inv(y)),('p',p),('p1',p1)]:
 for sign in (1,-1):
  w=mul(v,power(comm,sign),inv(v))
  if artin(4,cusp)==artin(4,w):found.append((label,sign))
# Exact Ferrari combing of the cusp, including a complete cyclic check.
def ferrari(w):
 k=();h=();action=((1,),(2,))
 for letter in w:
  typ=abs(letter);sgn=1 if letter>0 else -1
  if typ==3:k=mul(k,subst((sgn,),action))
  bg=1 if typ in (1,3) else 2
  psi=(((1,),(2,1)) if sgn>0 else ((1,),(2,-1))) if bg==1 else (((1,-2),(2,)) if sgn>0 else ((1,2),(2,)))
  action=tuple(subst(v,action) for v in psi)
  h=mul(h,(sgn*bg,))
 assert artin(4,w)==artin(4,mul(subst(k,(x,y)),h))
 return k,h
cusp_kernel,fold=ferrari(cusp)
assert artin(4,fold)==artin(4,())
stem=[];cyclic=list(cusp_kernel)
while len(cyclic)>1 and cyclic[0]==-cyclic[-1]:stem.append(cyclic.pop(0));cyclic.pop()
standard=(1,2,-1,-2)
orientation=[]
for sign in (1,-1):
 w=power(standard,sign)
 for j in range(len(w)):
  if tuple(cyclic)==w[j:]+w[:j]:orientation.append((sign,j))
assert len(orientation)==1
print('Exact cusp kernel word:',cusp_kernel,flush=True)
print('Cyclic commutator orientation and rotation:',orientation,flush=True)
print('Exact peripheral commutator matches:',found,flush=True)
out={'rho_s':s,'rho_r':r,'rho_tau':tau,'p_image':(1,2),'p1_image':(-2,1,2),
 'cusp_braid_word':cusp,'commutator_matches':found,'cusp_kernel_word':cusp_kernel,'cyclic_stem':stem,'cyclic_commutator_orientation':orientation,'checks':list(checks)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
