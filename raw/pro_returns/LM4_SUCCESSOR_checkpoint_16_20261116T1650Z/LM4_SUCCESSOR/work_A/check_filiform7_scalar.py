"""Exact exploratory certificate for a two-stage scalar refinement.

This computes an actual odd filiform head, its characteristic-two modules,
and the two different exterior-square coinvariant spaces.  No full
involution or universal lifting theorem is inferred from this certificate.
"""
from collections import deque

P=7
POLY=0b1011
def fm(a,b):
 c=0
 while b:
  if b&1:c^=a
  b>>=1;a<<=1
  if a&8:a^=POLY
 return c
def fp(a,n):
 out=1
 while n:
  if n&1:out=fm(out,a)
  a=fm(a,a);n>>=1
 return out
ZETA=[fp(2,j) for j in range(7)]
def ev(x,v):
 y,z,w,t=v;x%=7
 return(y,(z+x*y)%7,(w+x*z+4*x*x*y)%7,
        (t+x*w+4*x*x*z+6*x*x*x*y)%7)
def hm(g,h):
 x,*v,d=g;u,*w,e=h
 aa=pow(3,d,7);bb=[pow(a,d,7) for a in(5,1,3,2)]
 w=ev(x,tuple(a*b%7 for a,b in zip(bb,w)))
 return((x+aa*u)%7,*tuple((a+b)%7 for a,b in zip(v,w)),(d+e)%6)
HI=(0,0,0,0,0,0)
def hp(g,n):
 out=HI
 while n:
  if n&1:out=hm(out,g)
  g=hm(g,g);n>>=1
 return out
def hinv(g):
 x,*v,d=g
 w=ev(-x,tuple(-a%7 for a in v))
 return(-x*pow(3,-d,7)%7,*tuple(a*pow(b,-d,7)%7 for a,b in zip(w,(5,1,3,2))),-d%6)
def hc_s(g):
 x,y,z,w,t,d=g
 return(-x%7,-y%7,z,-w%7,t,d)
s=(0,0,0,0,0,3);r0=(0,0,0,0,0,2)
n=(1,1,0,0,0,0);r=hm(hm(n,r0),hinv(n));tau=hm(s,r)
X=(1,0,0,0,0,0);Y=(0,1,0,0,0,0);T=(0,0,0,0,1,0)
assert hp(s,2)==hp(r,3)==HI
assert hm(n,hinv(n))==hm(hinv(n),n)==HI
seen={HI};queue=deque([HI])
while queue:
 g=queue.popleft()
 for h in(s,r):
  gh=hm(g,h)
  if gh not in seen:seen.add(gh);queue.append(gh)
assert len(seen)==6*7**5
print('Actual head H=N:C6 has order',len(seen),'with s=',s,'r=',r)
print('s^2=r^3=1 and the specified pair generates: PASS')

# The c-pullback head has generators s and s*r^-1*s.  The two top
# central directions are distinguished by actual commutator words.
rc=hm(hm(s,hinv(r)),s)
def cm(a,b):return hm(hm(hm(a,b),hinv(a)),hinv(b))
def pm(a,b):return tuple(hm(x,y) for x,y in zip(a,b))
def pp(a,k):return tuple(hp(x,k) for x in a)
def pc(a,b):return tuple(cm(x,y) for x,y in zip(a,b))
ss=(s,s);rs=(r,rc)
uu=pc(ss,rs);vv=pc(ss,tuple(hinv(a) for a in rs))
ab=[]
for target in((1,0),(0,1)):
 coeff=next((i,j) for i in range(7) for j in range(7)
            if ((i*uu[0][0]+j*vv[0][0])%7,
                (i*uu[0][1]+j*vv[0][1])%7)==target)
 ab.append(pm(pp(uu,coeff[0]),pp(vv,coeff[1])))
 print('An actual commutator eigenbasis word uses exponents',coeff,
       'and has head abelian coordinates',tuple((g[0],g[1]) for g in ab[-1]))
aa,bb=ab
t1=pc(aa,pc(aa,pc(aa,bb)))
t2=pc(bb,pc(bb,pc(bb,aa)))
assert t1[0][:4]==(0,0,0,0) and t1[0][4]!=0 and t1[0][5]==0 and t1[1]==HI
assert t2[1][:4]==(0,0,0,0) and t2[1][4]!=0 and t2[1][5]==0 and t2[0]==HI
print('Independent actual degree-four central directions in the c-paired heads:',t1,t2)
print('The c-paired module supports are distinct; no joint-head enumeration is assumed: PASS')

def ua(x,v,u,sgn=1):
 out=[0]*7
 for j in range(7):
  k=(j+x)%7;e=ev(-k,v);ex=sgn*(e[0]+e[3])%7
  out[k]=fm(ZETA[ex],u[j])
 return tuple(out)
def rr(u):
 out=[0]*7
 for j in range(7):out[2*j%7]=fp(u[j],4)
 return tuple(out)
def vrho(g,v,sgn=1):
 x,y,z,w,t,d=g;u=tuple(v[:7]);v=tuple(v[7:])
 for _ in range(2*d%3):u=rr(u);v=rr(v)
 if d%2:u,v=v,u
 return ua(x,(y,z,w,t),u,sgn)+ua(-x%7,(-y%7,z,-w%7,t),v,sgn)
def bits(v):return sum(a<<(3*i) for i,a in enumerate(v))
def unbits(b,n=14):return tuple((b>>(3*i))&7 for i in range(n))
VB=[unbits(1<<i) for i in range(42)]
def cols(g,sgn=1):return [bits(vrho(g,v,sgn)) for v in VB]
def lin(cs,v):
 out=0
 while v:
  b=v&-v;out^=cs[b.bit_length()-1];v^=b
 return out
def rank(cs):
 piv={}
 for v in cs:
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 return len(piv)
for g,h in((X,Y),(r0,X),(r0,Y),(s,X),(s,Y),(s,r0),(s,r),(r,r)):
 for sg in(1,-1):
  cg,ch,cgh=cols(g,sg),cols(h,sg),cols(hm(g,h),sg)
  assert [lin(cg,t) for t in ch]==cgh
print('Exact F2-linear induced module and dual action: PASS')

def ker(cs,n):
 piv={};out=[]
 for j,v in enumerate(cs):
  aux=1<<j
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i][0];aux^=piv[i][1]
   else:piv[i]=(v,aux);break
  if not v:out.append(aux)
 assert len(out)==n-rank(cs)
 return out

cocycles=[]
for sg in(1,-1):
 S,R=cols(s,sg),cols(r,sg)
 ns=[(1<<i)^S[i] for i in range(42)]
 nr=[(1<<i)^R[i]^lin(R,R[i]) for i in range(42)]
 fs=ker(ns,42);kr=ker(nr,42)
 cob=[v^lin(R,v) for v in fs]
 assert len(fs)==21 and len(kr)==28 and rank(cob)==21
 chosen=next(v for v in kr if rank(cob+[v])==22)
 second=next(v for v in kr if rank(cob+[chosen,v])==23)
 assert lin(nr,chosen)==0
 assert lin(nr,second)==0
 cocycles.append(chosen)
 print('Sign',sg,': kerNs=',len(fs),'kerNr=',len(kr),'cob(s=0)=',rank(cob),'H1 dimension7; chosen r-vector=',unbits(chosen))
 print(' Independent next r-vector=',unbits(second),
       '; coboundaries plus the two classes have rank23: PASS')

# Pair the two induced summands with their duals. The two individual
# trace pairings are J-invariant and are exchanged by s.
def tr(a):return a^fp(a,2)^fp(a,4)
def pair(v,w,half):
 out=0
 for i in range(7*half,7*half+7):out^=tr(fm(v[i],w[i]))
 assert out in(0,1)
 return out
for g in(X,Y,r0,s):
 for i in range(42):
  for j in range(42):
   a,b=vrho(g,VB[i]),vrho(g,VB[j],-1)
   for half in(0,1):
    assert pair(a,b,half)==pair(VB[i],VB[j],half^(g[5]%2))
print('Two hyperbolic trace pairings: J-invariant and s-exchanged: PASS')

pairs=[(i,j) for i in range(84) for j in range(i+1,84)]
indices={p:k for k,p in enumerate(pairs)}
def wedge(a,b):
 ia=[];ib=[]
 while a:
  t=a&-a;ia.append(t.bit_length()-1);a^=t
 while b:
  t=b&-b;ib.append(t.bit_length()-1);b^=t
 out=0
 for i in ia:
  for j in ib:
   if i!=j:out^=1<<indices[min(i,j),max(i,j)]
 return out
piv={}
for g in(X,Y,r0,s):
 cs=cols(g)+[v<<42 for v in cols(g,-1)]
 for k,(i,j) in enumerate(pairs):
  v=(1<<k)^wedge(cs[i],cs[j])
  while v:
   b=v.bit_length()-1
   if b in piv:v^=piv[b]
   else:piv[b]=v;break
 if g==r0:
  assert len(piv)==3484
  print('Odd J exterior-square rank',len(piv),'of3486; coinvariant dimension2: PASS')
assert len(piv)==3485
print('Full H exterior-square rank',len(piv),'of3486; coinvariant dimension1: PASS')

# P=P1 x P2 has its two central coordinates retained. H acts on the
# center by swapping them exactly when d is odd.
ZERO=(0,)*14
ONE=(ZERO,ZERO,(0,0),HI)
def gm(a,b):
 v,w,t,g=a;u,z,q,h=b
 ru,rz=vrho(g,u),vrho(g,z,-1)
 if g[5]%2:q=q[::-1]
 return(tuple(a^b for a,b in zip(v,ru)),tuple(a^b for a,b in zip(w,rz)),
        tuple(t[i]^q[i]^pair(v,rz,i) for i in(0,1)),hm(g,h))
def gp(a,n):
 out=ONE
 while n:
  if n&1:out=gm(out,a)
  a=gm(a,a);n>>=1
 return out
S=(ZERO,ZERO,(0,0),s)
R=(unbits(cocycles[0]),unbits(cocycles[1]),(0,0),r)
cube=gp(R,3)
assert cube[0]==cube[1]==ZERO and cube[3]==HI
R=(R[0],R[1],cube[2],r)
assert gp(S,2)==gp(R,3)==ONE
z1=(ZERO,ZERO,(1,0),HI);z2=(ZERO,ZERO,(0,1),HI)
assert gm(gm(S,z1),S)==z2
assert gm(z1,z2)==(ZERO,ZERO,(1,1),HI)
print('Actual two-center cover admits order2/order3 lifts; r central correction=',cube[2],': PASS')
print('s exchanges z1,z2, so [center,H]=<z1 z2> is nontrivial and central: PASS')
print('All exact filiform module/scalar-layer checks PASS; no norm obstruction is asserted.')
