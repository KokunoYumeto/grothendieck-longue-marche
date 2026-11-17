"""Exploratory exact F8 Schrödinger/frame calculation after A.49.

No enumeration of the huge affine/central group is attempted. Field,
module, cocycle, central-cover and c-norm identities are exact.
"""
P=7;N=7;POLY=0b1011

def fm(a,b):
 c=0
 while b:
  if b&1:c^=a
  b>>=1;a<<=1
  if a&8:a^=POLY
 return c

def fp(a,k):
 if k<0:k%=7
 b=1
 for _ in range(k):b=fm(b,a)
 return b
zeta=2
assert [fp(zeta,i) for i in range(7)]==[1,2,4,3,6,7,5]
def va(v,w):return tuple(a^b for a,b in zip(v,w))
def vz():return (0,)*N
def basis(i,a=1):return tuple(a if j==i else 0 for j in range(N))
def sm(a,v):return tuple(fm(a,x) for x in v)
def hm(g,h,mod=6):
 x,y,z,d=g;u,v,w,e=h
 u=u*pow(3,d,7)%7;v=v*pow(3,-d,7)%7
 return((x+u)%7,(y+v)%7,(z+w+4*(x*v-y*u))%7,(d+e)%mod)
HI=(0,0,0,0)
def hp(g,k):
 h=HI
 for _ in range(k):h=hm(h,g)
 return h

def hc(g):
 x,y,z,d=g
 return(4*y%7,2*x%7,-z%7,-d%6)

def rho(g,v):
 x,y,z,d=g;a=pow(3,d,7);out=[0]*7
 for j in range(7):
  e=(-z+4*x*y+y*a*j)%7
  out[(a*j+x)%7]=fm(fp(zeta,e),v[j])
 return tuple(out)

def rhom(g,v):return rho(hc(g),v)

def dot(v,w):
 out=0
 for i in range(7):
  for j in range(7):out^=fm(fm(v[i],fp(zeta,(-2*i*j)%7)),w[j])
 return out

def rank_cols(cols):
 # F8 linear rank.
 piv={}
 for col in cols:
  v=list(col)
  for i in sorted(piv):
   if v[i]:
    c=v[i];v=[a^fm(c,b) for a,b in zip(v,piv[i])]
  try:i=next(i for i,a in enumerate(v) if a)
  except StopIteration:continue
  inv=fp(v[i],6);piv[i]=tuple(fm(inv,a) for a in v)
 return len(piv)

def solve(cols,target):
 rows=[[cols[j][i] for j in range(7)]+[target[i]] for i in range(7)]
 for j in range(7):
  k=next(i for i in range(j,7) if rows[i][j]);rows[j],rows[k]=rows[k],rows[j]
  iv=fp(rows[j][j],6);rows[j]=[fm(iv,a) for a in rows[j]]
  for i in range(7):
   if i!=j and rows[i][j]:
    a=rows[i][j];rows[i]=[x^fm(a,y) for x,y in zip(rows[i],rows[j])]
 return tuple(rows[i][7] for i in range(7))

s=(0,0,0,3);r=(1,1,2,2);tau=hm(s,r)
X=(1,0,0,0);Y=(0,1,0,0);Z=(0,0,1,0)
for g,h in ((s,r),(X,Y),(r,X),(s,Y),(tau,tau)):
 for e in range(7):assert rho(hm(g,h),basis(e))==rho(g,rho(h,basis(e)))
for g in(s,r,X,Y):
 for i in range(7):
  for j in range(7):assert dot(rho(g,basis(i)),rhom(g,basis(j)))==dot(basis(i),basis(j))
assert rank_cols([tuple(fp(zeta,(-2*i*j)%7) for i in range(7)) for j in range(7)])==7
print('Exact F8 Schrödinger action and nondegenerate symmetric Fourier pairing: PASS')
ns=[va(basis(i),rho(s,basis(i))) for i in range(7)]
nr=[va(va(basis(i),rho(r,basis(i))),rho(hp(r,2),basis(i))) for i in range(7)]
assert rank_cols(ns)==rank_cols(nr)==3
assert rank_cols(ns+[basis(0)])==4
print('Norm kernels: dimensions4,4; coboundary dimension7; H1(Pi,V) dimension1 overF8.')
print('The s-torsion H1 direction is nonzero and represented by e0: PASS')
cols=[va(basis(i),rho(tau,basis(i))) for i in range(7)]
assert rank_cols(cols)==7
k=solve(cols,basis(0))
vs=va(basis(0),va(k,rho(s,k)));vr=va(k,rho(r,k))
assert va(vs,rho(s,vr))==vz()
assert va(vs,rhom(s,vr))==vz()
assert va(vr,va(rho(r,vr),rho(hp(r,2),vr)))==vz()
assert va(vr,va(rhom(r,vr),rhom(hp(r,2),vr)))==vz()
assert dot(vs,vs)==1
print('Unique cusp normalization k=',k)
print('Normalized vectors vs=',vs,'vr=',vr,'quadratic s-square=',dot(vs,vs))
print('tau-1 invertible; both c-paired cusp vector coordinates vanish: PASS')

# Central cover: P overF8 with cocycle dot(v,w'), compensated by C12/C6.
# Canonical representatives use head d in0,...,5; C12 carry adds1 inF8.
ONE=(vz(),vz(),0,HI)
def gm(a,b):
 v,w,t,g=a;u,z,q,h=b;ru=rho(g,u);rz=rhom(g,z)
 return(va(v,ru),va(w,rz),t^q^dot(v,rz)^int(g[3]+h[3]>=6),hm(g,h))
def gp(a,k):
 b=ONE
 for _ in range(k):b=gm(b,a)
 return b

def gi(a):
 v,w,t,g=a
 h=hp(g,41) # exponent of H divides42
 assert hm(g,h)==HI
 u=rho(h,v);z=rhom(h,w)
 q=t^dot(v,w)^int(g[3]+h[3]>=6)
 out=(u,z,q,h);assert gm(a,out)==gm(out,a)==ONE
 return out

def gc(a):
 v,w,t,g=a
 return(w,v,t^dot(v,w)^int(g[3]!=0),hc(g))
S=(vs,vs,0,s);R0=(vr,vr,0,r);rr=gp(R0,3);assert rr[0]==rr[1]==vz() and rr[3]==HI
R=(vr,vr,rr[2],r);T=gm(S,R)
assert gp(S,2)==gp(R,3)==ONE
assert T[0]==T[1]==vz()
assert gc(S)==S and gc(R)==gm(gm(S,gi(R)),S)
assert gc(T)==gi(T)
print('Compensating C12 central extension: actual s²=r³=1, r central correction=',rr[2],': PASS')
print('Actual c on the central cover fixes s, maps r to sr^-1s and tau to tau^-1: PASS')
# Exact automorphism equations on central/group generators, by checking
# bilinear action and the C12 carry cocycle above; sample all basis pairs.
gens=[S,R]+[(basis(i,a),vz(),0,HI) for i in range(7) for a in(1,2,4)]+[(vz(),basis(i,a),0,HI) for i in range(7) for a in(1,2,4)]+[(vz(),vz(),a,HI) for a in(1,2,4)]
for a in gens:
 assert gc(gc(a))==a
 for b in gens:assert gc(gm(a,b))==gm(gc(a),gc(b))
for j in range(7):
 beta=(vz(),vz(),0,(0,0,j,0))
 assert gp(beta,7)==ONE
 assert gm(beta,T)==gm(T,beta)
 assert gc(beta)==gi(beta)
 for a in gens:
  def neg(t):return gm(gm(beta,gc(t)),gi(beta))
  assert neg(neg(a))==a
print('For every beta_H=z^j: specified odd lift centralizes tau and (Inn(beta)c)^2=1: PASS')

# Restrict42-dimensional F2 module to odd J=Heis7:C3; wedge rank must858.
def tobits(v,w):return sum(a<<(3*i) for i,a in enumerate(v))+sum(a<<(21+3*i) for i,a in enumerate(w))
fb=[]
for half in range(2):
 for i in range(7):
  for a in(1,2,4):fb.append((basis(i,a),vz()) if half==0 else(vz(),basis(i,a)))
pairs=[(i,j) for i in range(42) for j in range(i+1,42)];pi={pair:k for k,pair in enumerate(pairs)}
def wedge(a,b):
 ia=[i for i in range(42) if a>>i&1];ib=[i for i in range(42) if b>>i&1];out=0
 for i in ia:
  for j in ib:
   if i!=j:out^=1<<pi[min(i,j),max(i,j)]
 return out
piv={}
for g in(X,Y,r):
 cols=[tobits(rho(g,v),rhom(g,w)) for v,w in fb]
 for k,(i,j) in enumerate(pairs):
  v=(1<<k)^wedge(cols[i],cols[j])
  while v:
   b=v.bit_length()-1
   if b in piv:v^=piv[b]
   else:piv[b]=v;break
assert len(piv)==858
print('Odd J wedge-square rank:',len(piv),'of861, coinvariant dimension3: PASS')
print('All exact module/frame/central-cover checks PASS. No full lifting theorem is inferred by this script.')
