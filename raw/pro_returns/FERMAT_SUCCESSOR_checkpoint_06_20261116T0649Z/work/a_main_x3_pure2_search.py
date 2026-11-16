import sympy as s

def add(P,Q,q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v+1)%q==0:return None
 m=(3*x*x*pow(2*y+1,-1,q) if P==Q else (v-y)*pow(u-x,-1,q))%q
 z=(m*m-x-u)%q
 w=(-y-1+m*(x-z))%q
 return z,w
def mul(n,P,q):
 out=None
 while n:
  if n&1:out=add(out,P,q)
  P=add(P,P,q);n//=2
 return out
def order(P,q):
 n=1;Q=P
 while Q is not None:
  Q=add(Q,P,q);n+=1
 return n
found=0
for q in s.primerange(5,10000):
 if q%3!=1:continue
 bs=[x for x in range(q) if pow(x,3,q)==3%q]
 if not bs:continue
 zs=[x for x in range(2,q) if (x*x+x+1)%q==0]
 P=(1,0);m=order(P,q);mp=m;two=1
 while mp%2==0:mp//=2;two*=2
 if two==1:continue
 coeff=mp*pow(mp,-1,two)%m
 T=mul(coeff,P,q)
 for b in bs:
  for z in zs:
   def g(A):
    if A is None:return 1
    x,y=A
    return ((b*b*z*z*x-y-2)*pow((b*b*x-y-2)%q,-1,q))%q
   val=g(T)
   if pow(val,(q-1)//2,q)==q-1:
    print('q,b,zeta,ordP,two_part,P,T2,gT=',q,b,z,m,two,P,T,val)
    found+=1
    break
  else:continue
  break
 if found>=6:break
print('witnesses_found=',found)
