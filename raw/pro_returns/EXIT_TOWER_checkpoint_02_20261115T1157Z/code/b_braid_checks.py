"""Exact Artin-action verification of braid words used in Section B.
The Artin action B_n -> Aut(F_n) is faithful; words are freely reduced.
This program verifies identities, not completeness of a presentation.
"""
from functools import reduce

def red(w):
 s=[]
 for a in w:
  if s and s[-1]==-a:s.pop()
  else:s.append(a)
 return tuple(s)
def inv(w):return tuple(-a for a in reversed(w))
def subst(w, imgs):
 return red(a for k in w for a in (imgs[k-1] if k>0 else inv(imgs[-k-1])))
def action(n,w):
 imgs=tuple((i,) for i in range(1,n+1))
 for j in w:
  i=abs(j); gen=[(k,) for k in range(1,n+1)]
  if j>0: gen[i-1]=(i,i+1,-i);gen[i]=(i,)
  else: gen[i-1]=(i+1,);gen[i]=(-(i+1),i,i+1)
  imgs=tuple(subst(x,gen) for x in imgs)
 return imgs
def eq(n,u,v):return action(n,u)==action(n,v)
def conj(u,v):return u+v+inv(u)
def comm(u,v):return u+v+inv(u)+inv(v)
a=(1,);b=(2,);c=(3,);delta=a+b+c;D=a+b+c+a+b+a
s=a+b+a;r=inv(s)+D+s;h=(a+b)*3
checks={
 'a b a = b a b':eq(4,a+b+a,b+a+b),
 'b c b = c b c':eq(4,b+c+b,c+b+c),
 'a c = c a':eq(4,a+c,c+a),
 'Delta^2 = delta^4':eq(4,D*2,delta*4),
 's a s^-1 = b':eq(4,conj(s,a),b),
 'r a r^-1 = a':eq(4,conj(r,a),a),
 'r^2 = delta^4':eq(4,r*2,delta*4),
 'delta^2 a delta^-2 = c':eq(4,conj(delta*2,a),c),
 'delta^2 c delta^-2 = a':eq(4,conj(delta*2,c),a),
 'h a h^-1 = a':eq(4,conj(h,a),a),
 'h = a c^-1 r':eq(4,h,a+inv(c)+r),
 'forget(delta^4) = (a b)^6':eq(3,(a+b+a)*4,(a+b)*6),
}
for k,v in checks.items():print(k,':',v)
assert all(checks.values())
for x in (-2,-1,0,1,2):
 for y in (-2,-1,0,1,2):
  word=(a*x if x>=0 else inv(a)*-x)+r+(c*y if y>=0 else inv(c)*-y)
  if eq(4,h,word): print('additional identity h = a^%d r c^%d'%(x,y))
print('Number of verified identities:',len(checks))
