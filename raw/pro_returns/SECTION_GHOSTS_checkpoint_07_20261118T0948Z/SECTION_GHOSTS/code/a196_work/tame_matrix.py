from itertools import product
class F:
 def __init__(self,q):self.q=q
 def add(self,a,b):return ((a[0]+b[0])%self.q,(a[1]+b[1])%self.q)
 def neg(self,a):return(-a[0]%self.q,-a[1]%self.q)
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
  q=self.q;return ((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%q)
 def pow(self,a,n):
  if n<0:return self.pow(self.pow(a,self.q*self.q-2),-n)
  r=(1,0)
  while n:
   if n&1:r=self.mul(r,a)
   a=self.mul(a,a);n//=2
  return r
 def div(self,a,b):return self.mul(a,self.pow(b,-1))
 def scale(self,a,n):return(a[0]*n%self.q,a[1]*n%self.q)
 def logcub(self,a):
  r=self.pow(a,(self.q*self.q-1)//3)
  return next(i for i in range(3) if self.pow((0,1),i)==r)
 def g(self,q,a):
  if q==2:return self.sub(a,(1,0))
  if q==11:return self.add(a,(2,0))
  if q==59:return self.sub(self.add((2,0),self.scale(a,2)),self.pow(a,2))
  raise ValueError(q)

rows=[]
for q,r in [(2,1),(11,-2),(59,49)]:
 f=F(q);z=(0,1)
 for j in range(3):
  a=f.scale(f.pow(z,j),r)
  beta=f.div(f.pow(a,2),(1,2))
  eta=f.neg(f.add(f.add(f.scale(f.pow(beta,3),pow(2,-1,q)) if q!=2 else (0,0),f.pow(beta,2)),f.add(beta,(pow(2,-1,q),0) if q!=2 else (0,0)))) if q!=2 else None
  # eta = eps/tau eps with eps=1+beta-z beta^2; tau(beta)=-beta,tau(z)=z²
  eps=f.sub(f.add((1,0),beta),f.mul(z,f.pow(beta,2)))
  taueps=f.sub(f.sub((1,0),beta),f.mul(f.pow(z,2),f.pow(beta,2)))
  eta=f.div(eps,taueps)
  bvals=[(0,z),(0,eta)]
  for p in [2,11,59]:
   gp=[f.g(p,f.mul(a,f.pow(z,i))) for i in range(3)]
   if p!=q:
    bvals.append((0,f.div(gp[1],gp[2])))
   elif gp[1]==(0,0):
    bvals.append((1,f.pow(f.mul(gp[0],f.pow(gp[2],2)),-1)))
   elif gp[2]==(0,0):
    bvals.append((-1,f.mul(gp[0],f.pow(gp[1],2))))
   else:bvals.append((0,f.div(gp[1],gp[2])))
  va=8 if q in (11,59) else 0
  au=f.scale(a,pow(649//q,8,q)) if va else f.scale(a,pow(649,8,q))
  row=[f.logcub(f.div(f.pow(au,vb),f.pow(bu,va))) for vb,bu in bvals]
  rows.append(row)
  print(q,j,'alpha',a,'Aunit',au,'bvaluations',[v for v,_ in bvals],'row',row)

def rank(m):
 m=[r[:] for r in m];i=0
 for j in range(len(m[0])):
  for k in range(i,len(m)):
   if m[k][j]%3:break
  else:continue
  m[k],m[i]=m[i],m[k];u=pow(m[i][j],-1,3);m[i]=[x*u%3 for x in m[i]]
  for k in range(len(m)):
   if k!=i:
    u=m[k][j];m[k]=[(a-u*b)%3 for a,b in zip(m[k],m[i])]
  i+=1
 return i,m
print('rank',rank(rows))
