#!/usr/bin/env python3
"""Check the actual Artin free-fiber action used to transfer the finite pentagon.
Uses inverse Artin convention beta_i(a_i)=a_(i+1),
beta_i(a_(i+1))=a_(i+1)^(-1) a_i a_(i+1), preserving a b c.
No associator or braid formality is used.
"""
from pathlib import Path
from graded_dimensions import add,bracket

def red(w):
 r=[]
 for v in w:
  if r and r[-1]==-v:r.pop()
  else:r.append(v)
 return tuple(r)
def inv(w):return tuple(-v for v in reversed(w))
def apply(w,A):
 r=()
 for v in w:r=red(r+(A[abs(v)-1] if v>0 else inv(A[abs(v)-1])))
 return r
def comp(A,B):return tuple(apply(w,A) for w in B)
E=((1,),(2,),(3,))
def beta(i):
 A=list(E);A[i]=(i+2,);A[i+1]=(-(i+2),i+1,i+2);return tuple(A)
def beta_inv(i):
 A=list(E);A[i]=(i+1,i+2,-(i+1));A[i+1]=(i+1,);return tuple(A)
b1,b2=beta(0),beta(1)
assert comp(comp(b1,b2),b1)==comp(comp(b2,b1),b2)
assert comp(b1,beta_inv(0))==E and comp(b2,beta_inv(1))==E
A12=comp(b1,b1);A23=comp(b2,b2);A13=comp(comp(b2,A12),beta_inv(1))
w=(1,2,3);t=comp(b1,b2);full=comp(comp(t,t),t)
assert full==tuple(red(inv(w)+(i,)+w) for i in range(1,4))
print('Inverse Artin braid relation verified as exact reduced free words.')
print('Base full twist acts by conjugation with (abc)^(-1).')
# Fibre conjugation by abc therefore kills the full four-strand central twist.
innerw=tuple(red(w+(i,)+inv(w)) for i in range(1,4))
assert comp(innerw,full)==E
print('Fibre abc times base full twist acts identically: PB4 central quotient compatibility checked.')

def mul2(a,b):
 r={}
 for u,c in a.items():
  for v,d in b.items():
   if len(u)+len(v)<=2:r[u+v]=r.get(u+v,0)+c*d
 return {w:c for w,c in r.items() if c}
def magnus2(w):
 r={():1}
 for v in w:
  i=abs(v)-1;q={():1,(i,):1} if v>0 else {():1,(i,):-1,(i,i):1}
  r=mul2(r,q)
 return r
G=[{(i,):1} for i in range(3)]
for label,A,i,j in [('12',A12,0,1),('13',A13,0,2),('23',A23,1,2)]:
 for k in range(3):
  q={v:c for v,c in magnus2(A[k]).items() if len(v)==2}
  expect=bracket(G[i],G[j]) if k==i else bracket(G[j],G[i]) if k==j else {}
  assert q==expect,(label,k,q,expect)
 print('Actual pure braid A'+label+' has the required degree-one derivation on all three fibre generators.')
for i in range(3):
 A=tuple(red((i+1,)+(k+1,)+(-(i+1),)) for k in range(3))
 for k in range(3):assert {w:c for w,c in magnus2(A[k]).items() if len(w)==2}==bracket(G[i],G[k])
print('All three fibre braid generators act in degree one by ad(a_i).')
print('The finite target is IA of the class8 exponent13 free fibre BCH group: class<=7, exponent13.')
print('The already verified degree7 pentagon defect is 16=3 mod13 on a word of length8, and higher-degree corrections vanish in this target.')
