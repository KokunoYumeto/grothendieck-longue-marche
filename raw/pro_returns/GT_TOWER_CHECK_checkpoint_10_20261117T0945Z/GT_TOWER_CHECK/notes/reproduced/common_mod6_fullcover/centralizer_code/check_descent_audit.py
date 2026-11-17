#!/usr/bin/env python3
"""Checks the concrete marking and kernel-word ingredients of DELTA A60-A80."""
from itertools import product
from collections import deque

def fmul(a,b):
 out=list(a)
 for factor,e in b:
  mod=2 if factor=='s' else 3
  if out and out[-1][0]==factor:
   e=(out.pop()[1]+e)%mod
  if e:out.append((factor,e))
 return tuple(out)
def finv(a):return tuple((s,(-e)%(2 if s=='s' else 3)) for s,e in a[::-1])
def fpow(a,n):
 if n<0:return fpow(finv(a),-n)
 ans=()
 for _ in range(n):ans=fmul(ans,a)
 return ans
def fcomm(a,b):return fmul(fmul(fmul(a,b),finv(a)),finv(b))
s=(('s',1),);r=(('r',1),);tau=fmul(s,r)
x=fpow(tau,-2);y=fmul(fmul(s,x),s);z=finv(fmul(x,y))
assert fmul(fmul(r,x),finv(r))==y
assert fmul(fmul(r,y),finv(r))==z
assert fpow(fmul(r,s),2)==finv(y)
assert fpow(tau,2)==finv(x)
print('Current/LM2 free-basis conversion verified in C2*C3.')
# Deck outer action on free words represented in generators x,y; z=(xy)^-1.
def reduce_free(w):
 a=[]
 for t in w:
  if a and a[-1]==-t:a.pop()
  else:a.append(t)
 return tuple(a)
def inv_free(w):return tuple(-t for t in reversed(w))
def subst(w,im):
 a=()
 for t in w:a=reduce_free(a+(im[t] if t>0 else inv_free(im[-t])))
 return a
def permute(im,action):return {k:subst(w,action) for k,w in im.items()}
I={1:(1,),2:(2,)}
S={1:(2,),2:(1,)}
R={1:(2,),2:(-2,-1)}
reps=[I,R,permute(R,R),S,permute(S,R),permute(permute(S,R),R)]
def eval_word(w):
 v=()
 for t in w:
  g=s if abs(t)==1 else tau
  v=fmul(v,g if t>0 else finv(g))
 return v
for k,T in enumerate(reps):
 X=eval_word(T[1]);Y=eval_word(T[2]);Z=finv(fmul(X,Y))
 W=fpow(fcomm(fcomm(fpow(X,4),fpow(Y,4)),fpow(Z,4)),2)
 assert W==(),(k,W)
 print('Full C2*C3 identity for core substitution',k+1,': identity')

def mul(A,B,n):return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%n for i in range(2) for j in range(2))
def inv(A,n):a,b,c,d=A;return (d%n,-b%n,-c%n,a%n)
def power(A,k,n):
 if k<0:return power(inv(A,n),-k,n)
 ans=(1,0,0,1)
 for _ in range(k):ans=mul(ans,A,n)
 return ans
def comm(A,B,n):return mul(mul(mul(A,B,n),inv(A,n),n),inv(B,n),n)
U=(1,1,0,1);L=(1,0,-1,1)
X=power(U,2,12);Y=power(L,2,12);Z=inv(mul(X,Y,12),12)
A0=power(comm(comm(power(X,4,12),power(Y,4,12),12),power(Z,4,12),12),2,12)
assert A0==(5,0,0,5)
print('Signed original inclusion: A0 mod12 =',A0)
# q12(U0) with U0=F' F^3. Generate q(F), then commutators and cubes.
def group(gens,n):
 E=(1,0,0,1);seen={E};todo=[E]
 while todo:
  a=todo.pop()
  for b in gens:
   c=mul(a,b,n)
   if c not in seen:seen.add(c);todo.append(c)
 return seen
GF=group([X,Y],12)
# Closure under conjugation gives the derived subgroup from generator commutators.
Dgens={comm(X,Y,12)}
Dgens|={mul(mul(g,h,12),inv(g,12),12) for g in GF for h in list(Dgens)}
Gprime=group(list(Dgens),12)
U0=group(list(Gprime)+[power(g,3,12) for g in GF],12)
# Signed map q(F) is injected in SL2; projectivization may halve its size.
canon=lambda a:min(a,tuple((-x)%12 for x in a))
proj={canon(a) for a in U0}
assert len(proj)==32 and canon(A0) in proj
print('|q12(U0)| in PSL2(Z/12) =',len(proj),'(two-group), contains [5I].')
# Degree sixteen Kummer Galois group.
G={(v,b) for v in [1,3,5,7] for b in range(8) if b%2==(0 if v in[1,7] else 1)}
gmul=lambda g,h:(g[0]*h[0]%8,(g[1]+g[0]*h[1])%8)
ginv=lambda g:(g[0],(-g[0]*g[1])%8)
gcomm=lambda g,h:gmul(gmul(gmul(g,h),ginv(g)),ginv(h))
assert len(G)==16
assert all(gmul(g,h) in G for g in G for h in G)
D={gcomm(g,h) for g in G for h in G}
assert D=={(1,0),(1,2),(1,4),(1,6)}
witness=next((g,h) for g in sorted(G) for h in sorted(G) if gcomm(g,h)==(1,2))
c=(7,0);sig=(1,2)
assert gmul(gmul(c,sig),c)==(1,6)
print('Kummer group order:',len(G))
print('Derived subgroup:',sorted(D))
print('Explicit commutator giving (1,2):',witness)
print('Conjugation by c=(7,0): (1,2) ->',gmul(gmul(c,sig),c))
print('ALL CHECKS PASSED')
