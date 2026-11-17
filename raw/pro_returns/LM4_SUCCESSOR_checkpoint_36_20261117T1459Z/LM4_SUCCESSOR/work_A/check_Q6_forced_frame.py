"""Exploratory actual seven-primary head over Q6=S3 x A4.

The cycle module is H1 of the finite Bass--Serre graph, dimension13.
This only prepares an exact forced-frame norm test; it proves no lift.
"""
from itertools import permutations,product
P=7
def pm(a,b):return tuple(a[b[i]] for i in range(len(a)))
def pi(a):return tuple(a.index(i) for i in range(len(a)))
def parity(a):return sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2
S3=list(permutations(range(3)));A4=[a for a in permutations(range(4)) if not parity(a)]
Q=list(product(S3,A4));ix={g:i for i,g in enumerate(Q)}
def qm(g,h):return(pm(g[0],h[0]),pm(g[1],h[1]))
def qi(g):return(pi(g[0]),pi(g[1]))
e=ix[((0,1,2),(0,1,2,3))]
ss=((1,0,2),(1,0,3,2));rr=((1,2,0),(1,2,0,3));be=((0,1,2),(1,0,3,2))
s,r,beta=map(ix.get,(ss,rr,be));mul=[[ix[qm(a,b)]for b in Q]for a in Q];inv=[ix[qi(a)]for a in Q]
c4=next(h for h in permutations(range(4)) if parity(h) and pm(h,h)==(0,1,2,3)
        and pm(pm(h,ss[1]),pi(h))==ss[1]
        and pm(pm(h,rr[1]),pi(h))==pm(pm(ss[1],pi(rr[1])),ss[1]))
kappa=[ix[(g[0],pm(pm(c4,g[1]),pi(c4)))]for g in Q]
assert kappa[s]==s and kappa[r]==mul[mul[s][inv[r]]][s]
assert kappa[beta]==beta
AC=sorted({tuple(sorted((g,mul[g][s])))for g in range(72)})
BC=sorted({tuple(sorted((g,mul[g][r],mul[mul[g][r]][r])))for g in range(72)})
ai={g:i for i,c in enumerate(AC)for g in c};bi={g:i for i,c in enumerate(BC)for g in c}
boundary=[[0]*72 for _ in range(60)]
for g in range(72):boundary[ai[g]][g]=-1%7;boundary[36+bi[g]][g]=1
def rref(rows):
 a=[list(row) for row in rows];pivs=[];k=0
 for j in range(len(a[0])):
  z=next((i for i in range(k,len(a)) if a[i][j]),None)
  if z is None:continue
  a[k],a[z]=a[z],a[k];iv=pow(a[k][j],-1,7);a[k]=[x*iv%7 for x in a[k]]
  for i in range(len(a)):
   if i!=k and a[i][j]:
    v=a[i][j];a[i]=[(x-v*y)%7 for x,y in zip(a[i],a[k])]
  pivs.append(j);k+=1
  if k==len(a):break
 return a,pivs
def kernel(rows):
 a,p=rref(rows);free=[j for j in range(len(a[0]))if j not in p];out=[]
 for j in free:
  v=[0]*len(a[0]);v[j]=1
  for i,k in enumerate(p):v[k]=-a[i][j]%7
  out.append(tuple(v))
 return out,free
NB,free=kernel(boundary);assert len(NB)==13
def va(a,b):return tuple((x+y)%7 for x,y in zip(a,b))
def vs(a,b):return tuple((x-y)%7 for x,y in zip(a,b))
def sm(a,v):return tuple(a*x%7 for x in v)
def actedge(g,v):
 out=[0]*72
 for i,x in enumerate(v):out[mul[g][i]]=x
 return tuple(out)
def cedge(v):
 out=[0]*72
 for i,x in enumerate(v):out[mul[kappa[i]][s]]=x
 return tuple(out)
def ntov(n):
 out=(0,)*72
 for a,b in zip(n,NB):out=va(out,sm(a,b))
 return out
def vton(v):
 n=tuple(v[i]for i in free);assert ntov(n)==v
 return n
NC=[[vton(actedge(g,b))for b in NB]for g in range(72)]
CC=[vton(cedge(b))for b in NB]
def lin(cols,v):
 out=(0,)*len(cols[0])
 for a,c in zip(v,cols):out=va(out,sm(a,c))
 return out
def dualrow(v,cols):return tuple(sum(a*b for a,b in zip(v,c))%7 for c in cols)
def fixeddual(cols,sign=1):
 return [[(cols[j][i]-(sign if i==j else 0))%7 for i in range(13)]for j in range(13)]
assert all(lin(CC,lin(CC,b))==b for b in [(tuple(int(i==j)for i in range(13)))for j in range(13)])
fs,_=kernel(fixeddual(NC[s]));fc,_=kernel(fixeddual(CC));fb,_=kernel(fixeddual(NC[beta]))
fsc,_=kernel(fixeddual(NC[s])+fixeddual(CC))
fsac,_=kernel(fixeddual(NC[s])+fixeddual(CC,-1))
print('Q6 order72, Bass--Serre cycle rank13; c_A4=',c4)
print('Dual fixed dimensions: s=',len(fs),'c=',len(fc),'beta=',len(fb),'s,c=',len(fsc),'s,-c=',len(fsac))
def fixedvector(cols,sign=1):
 return [[(cols[j][i]-(sign if i==j else 0))%7 for j in range(13)]for i in range(13)]
BC=[lin(NC[beta],v)for v in CC]
allowed_translations,_=kernel(fixedvector(NC[s])+fixedvector(BC,-1))
for nn in allowed_translations:
 tt=sm(4,lin(NC[beta],nn))
 assert lin(NC[s],tt)==tt and vs(lin(NC[beta],tt),lin(CC,tt))==nn
print('All permissible retained beta translations have dimension',len(allowed_translations),
      'overF7; t=beta*n/2 removes them in the intermediate frame: PASS')

# A splitting of the odd extension, chosen invariant under s and c.
target=[0]*60
for i in range(36):target[i]=-pow(36,-1,7)%7
target[ai[e]]=(target[ai[e]]+1)%7
aug=[row+[t]for row,t in zip(boundary,target)];ar,piv=rref(aug)
assert 72 not in piv
b=[0]*72
for i,j in enumerate(piv):b[j]=ar[i][-1]
b=tuple(b);b=sm(2,va(va(b,actedge(s,b)),va(cedge(b),actedge(s,cedge(b)))))
assert actedge(s,b)==cedge(b)==b
dr=[0]*72;dr[e]=1;dr[r]=-1%7
dr=vton(va(vs(tuple(dr),actedge(r,b)),b))
assert va(va(dr,lin(NC[r],dr)),lin(NC[mul[r][r]],dr))==(0,)*13
ta=mul[s][r];dt=lin(NC[s],dr);dt6=(0,)*13;power=e
for _ in range(6):dt6=va(dt6,lin(NC[power],dt));power=mul[power][ta]
assert power==e and dt6!=(0,)*13
print('Actual normalized r-vector in N coordinates:',dr)
print('Actual tau^6 vector:',dt6)

def frombasis(coeff,bas):
 out=(0,)*13
 for a,b in zip(coeff,bas):out=va(out,sm(a,b))
 return out
chosen_characters={}
for typ,bas in(('c-fixed',fsc),('c-antifixed',fsac)):
 found=None
 for coeff in product(range(7),repeat=len(bas)):
  if not any(coeff):continue
  lam=frombasis(coeff,bas)
  stabilizer=[g for g in range(72)if dualrow(lam,NC[g])==lam]
  if set(stabilizer)!={e,s}:continue
  if dualrow(lam,NC[beta])==lam:continue
  found=lam;break
 if found is None:
  print(typ,': no character with stabilizer exactly<s> in this fixed subspace')
  continue
 chosen_characters[typ]=found
 vals=[sum(a*b for a,b in zip(found,lin(NC[inv[g]],dt6)))%7 for g in range(72)]
 zero_cosets=sum(v==0 for v in vals)//2
 print(typ,'character lambda=',found,'stabilizer exactly<s>; beta moves it')
 print(' tau^6 zero values on',zero_cosets,'of36 induced cosets; tau fixed dimension=',zero_cosets//6)
 normal=[(g,a)for g in range(72)for a in(1,2,4)if dualrow(found,NC[g])==sm(a,found)]
 print(' Frobenius-character normalizer size=',len(normal),'(2 means End_H=F8)')
 dualnormal=[(g,a)for g in range(72)for a in(3,5,6)if dualrow(found,NC[g])==sm(a,found)]
 print(' Dual Frobenius orbit intersects the head orbit:',bool(dualnormal))
print('Exact Q6 head preparation PASS; no equivariant lift or norm conclusion is claimed.')

# The c-fixed character gives an honest c-stable irreducible F8-module.
# Compute the full s/cusp restriction map on H1(Pi,V), not merely ranks
# of separate boundary spaces.
POLY=0b1011
def fm(a,b):
 out=0
 while b:
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=POLY
 return out
def fp(a,n):
 out=1
 while n:
  if n&1:out=fm(out,a)
  a=fm(a,a);n>>=1
 return out
zz=[fp(2,j)for j in range(7)]
def fva(v,w):return tuple(a^b for a,b in zip(v,w))
def fsm(a,v):return tuple(fm(a,b)for b in v)
def fbasis(i,n=36):return tuple(int(i==j)for j in range(n))
def flin(cs,v):
 out=(0,)*len(cs[0])
 for a,c in zip(v,cs):out=fva(out,fsm(a,c))
 return out
def frref(rows):
 a=[list(row)for row in rows];p=[];k=0
 for j in range(len(a[0])):
  z=next((i for i in range(k,len(a))if a[i][j]),None)
  if z is None:continue
  a[k],a[z]=a[z],a[k];iv=fp(a[k][j],6);a[k]=list(fsm(iv,a[k]))
  for i in range(len(a)):
   if i!=k and a[i][j]:a[i]=list(fva(a[i],fsm(a[i][j],a[k])))
  p.append(j);k+=1
  if k==len(a):break
 return a,p
def frank(cs):
 if not cs:return 0
 return len(frref(list(map(list,zip(*cs))))[1])
def fkernel(cs):
 rows,p=frref(list(map(list,zip(*cs))));free=[j for j in range(len(cs))if j not in p];out=[]
 for j in free:
  v=[0]*len(cs);v[j]=1
  for i,k in enumerate(p):v[k]=rows[i][j]
  out.append(tuple(v))
 return out
def independent(cs):
 out=[]
 for v in cs:
  if frank(out+[v])>len(out):out.append(v)
 return out
def coordinates(cs,v):
 rows=[list(row)+[t]for row,t in zip(zip(*cs),v)];rows,p=frref(rows)
 assert len(p)==len(cs) and len(cs)not in p
 return tuple(rows[i][-1]for i in range(len(cs)))
lam=chosen_characters['c-fixed'];reps=[c[0]for c in AC]
chars=[dualrow(lam,NC[inv[g]])for g in reps]
def vaction(n,g,v):
 out=[0]*36
 for j,a in enumerate(v):
  k=ai[mul[g][reps[j]]];ex=sum(x*y for x,y in zip(chars[k],n))%7
  out[k]=fm(zz[ex],a)
 return tuple(out)
VB=[fbasis(i)for i in range(36)];zero=(0,)*13
S=[vaction(zero,s,v)for v in VB];R=[vaction(dr,r,v)for v in VB]
T=[flin(S,v)for v in R];BETA=[vaction(zero,beta,v)for v in VB]
CV=[]
for j in range(36):CV.append(fbasis(ai[kappa[reps[j]]]))
print('Preliminary module relation failure counts:',
      sum(flin(S,S[i])!=VB[i]for i in range(36)),
      sum(flin(R,flin(R,R[i]))!=VB[i]for i in range(36)),
      sum(flin(CV,CV[i])!=VB[i]for i in range(36)))
assert all(flin(S,S[i])==VB[i]and flin(R,flin(R,R[i]))==VB[i]and flin(CV,CV[i])==VB[i]for i in range(36))
assert all(flin(CV,flin(S,flin(CV,v)))==flin(S,v)for v in VB)
assert all(flin(CV,flin(R,flin(CV,v)))==flin(S,flin(R,flin(R,flin(S,v))))for v in VB)
NS=[fva(v,w)for v,w in zip(VB,S)];MR=[fva(v,w)for v,w in zip(VB,R)];MT=[fva(v,w)for v,w in zip(VB,T)]
SF=fkernel(NS);RF=fkernel(MR);COB=independent([flin(NS,v)for v in RF])
FULL=independent(COB+SF);EB=FULL[len(COB):]
SB0=independent(NS);SB=independent(SB0+SF)
TB0=independent(MT);TB=independent(TB0+VB)
assert(len(SF),len(RF),len(COB),len(EB),len(SB)-len(SB0),len(TB)-len(TB0))==(20,12,12,8,4,4)
def sres(v):return coordinates(SB,v)[len(SB0):]
def tres(v):return coordinates(TB,v)[len(TB0):]
RES=[sres(v)+tres(v)for v in EB]
print('F8 dimensions: H1(Pi,V)=8, H1(<s>,V)=4, H1(<tau>,V)=4')
print('Joint s/cusp restriction rank=',frank(RES),'of8')
BS=[sres(flin(BETA,v))for v in SB[len(SB0):]]
CS=[sres(flin(CV,v))for v in SB[len(SB0):]]
CT=[tres(flin(CV,v))for v in TB[len(TB0):]]
assert all(flin(BS,BS[i])==fbasis(i,4)and flin(CS,CS[i])==fbasis(i,4)and flin(CT,CT[i])==fbasis(i,4)for i in range(4))
assert all(flin(BS,CS[i])==flin(CS,BS[i])for i in range(4))
print('Forced beta action on s-cohomology rank(beta-1)=',frank([fva(fbasis(i,4),BS[i])for i in range(4)]))
print('Standard c ranks on s/cusp=',frank([fva(fbasis(i,4),CS[i])for i in range(4)]),frank([fva(fbasis(i,4),CT[i])for i in range(4)]))
if frank(RES)==8:
 POS=[];NEG=[];CE=[]
 for v in RES:
  POS.append(coordinates(RES,flin(BS,v[:4])+v[4:]))
  NEG.append(coordinates(RES,flin(BS,flin(CS,v[:4]))+flin(CT,v[4:])))
  CE.append(coordinates(RES,flin(CS,v[:4])+flin(CT,v[4:])))
 assert all(flin(NEG,NEG[i])==fbasis(i,8)for i in range(8))
 assert all(flin(CE,CE[i])==fbasis(i,8)and flin(CE,POS[i])==NEG[i]for i in range(8))
 print('Unique boundary-forced action on H1 has an involutory negative companion: PASS')
 # Now compute the actual affine inner terms on the universal module
 # A=V tensor H1(Pi,V)^vee.  All eight cocycles have r-value0.
 def fsolve(cs,target):
  rows=[list(row)+[t]for row,t in zip(zip(*cs),target)];rows,p=frref(rows)
  n=len(cs)
  if n in p:return None
  out=[0]*n
  for i,j in enumerate(p):out[j]=rows[i][-1]
  assert flin(cs,tuple(out))==target
  return tuple(out)
 def mix(coh,values):
  return tuple(flin(values,col)for col in coh)
 def ga(values):return tuple(flin(CV,v)for v in mix(CE,values))
 def la(values):return mix(POS,values)
 def ba(values):return la(ga(values))
 def av(a,b):return tuple(fva(x,y)for x,y in zip(a,b))
 def flat(a):return tuple(x for v in a for x in v)
 def unflat(a):return tuple(tuple(a[36*j:36*(j+1)])for j in range(8))
 DVAL=tuple(EB);GD=ga(DVAL)
 RC=[flin(S,flin(R,flin(R,flin(S,v))))for v in VB]
 SYSC=[NS[i]+fva(VB[i],RC[i])for i in range(36)]
 assert frank(SYSC)==36
 WC=[]
 for j in range(8):
  target=fva(DVAL[j],GD[j])+fva(DVAL[j],flin(S,flin(R,flin(R,DVAL[j]))))
  v=fsolve(SYSC,target);assert v is not None;WC.append(v)
 WC=tuple(WC)
 assert av(WC,ga(WC))==((0,)*36,)*8
 print('Actual c-affine term is uniquely determined and has zero norm: PASS')
 LD=la(DVAL);W=[]
 for j in range(8):
  v=fsolve(MT,fva(LD[j],DVAL[j]));assert v is not None;W.append(v)
 W=tuple(W);Q0=av(W,la(WC));OB=av(Q0,ba(Q0))
 assert all(flin(T,v)==v for v in OB)
 TF=fkernel(MT);corrections=[]
 for j in range(8):
  for v in TF:
   a=[(0,)*36 for _ in range(8)];a[j]=v;a=tuple(a)
   corrections.append(flat(av(a,ba(a))))
 print('Actual cusp-fixed correction space dimension',len(corrections),
       '; norm rank=',frank(corrections),
       '; rank with actual obstruction=',frank(corrections+[flat(OB)]))
 print('The uncorrected actual inner-square vector is nonzero:',any(flat(OB)))
 sol=fsolve(corrections,flat(OB))
 if sol is None:
  print('UNRESOLVED CHECK: the displayed actual norm is outside the cusp-fixed norm image.')
 else:
  corr=[(0,)*36 for _ in range(8)]
  for j in range(8):
   for k,v in enumerate(TF):corr[j]=fva(corr[j],fsm(sol[j*len(TF)+k],v))
  W=av(W,tuple(corr));QQ=av(W,la(WC))
  assert av(QQ,ba(QQ))==((0,)*36,)*8
  assert all(fva(LD[j],flin(MT,W[j]))==DVAL[j]for j in range(8))
  # The actual s-frame equation has the prescribed finite head beta.
  for j in range(8):
   target=fva(fva(LD[j],flin(NS,W[j])),flin(BETA,DVAL[j]))
   assert fsolve(NS,target) is not None
  print('Actual affine negative norm cancels while fixing the cusp and retaining the forced beta frame: PASS')
  # Stronger framed test: the associated s-normalizer must itself be
  # an involution centralizing the actual s, with prescribed base image.
  def betaa(values):return tuple(flin(BETA,v)for v in values)
  def sb(values):return betaa(ba(values))
  target=av(av(DVAL,betaa(ba(DVAL))),betaa(tuple(flin(NS,v)for v in QQ)))
  AA=[]
  for v in target:
   z=fsolve(NS,v);assert z is not None;AA.append(z)
  AA=tuple(AA)
  ONS=av(av(AA,sb(AA)),av(QQ,betaa(QQ)))
  assert all(flin(S,v)==v for v in ONS)
  scorrections=[]
  for j in range(8):
   for v in SF:
    a=[(0,)*36 for _ in range(8)];a[j]=v;a=tuple(a)
    scorrections.append(flat(av(a,sb(a))))
  srank=frank(scorrections);saug=frank(scorrections+[flat(ONS)])
  print('Actual s-normalizer involution test: centralizer dimension',len(scorrections),
        '; norm rank=',srank,'; rank with actual obstruction=',saug)
  ssol=fsolve(scorrections,flat(ONS))
  if ssol is None:
   print('UNRESOLVED CHECK: actual s-normalizer square is outside the centralizer norm image.')
  else:
   acorr=[(0,)*36 for _ in range(8)]
   for j in range(8):
    for k,v in enumerate(SF):acorr[j]=fva(acorr[j],fsm(ssol[j*len(SF)+k],v))
   AA=av(AA,tuple(acorr))
   assert av(av(AA,sb(AA)),av(QQ,betaa(QQ)))==((0,)*36,)*8
   assert tuple(flin(NS,v)for v in AA)==target
   print('The actual C2 x C2 s-normalizer with the forced base frame exists: PASS')
else:
 print('Restriction has a kernel; no linear lift or norm assertion inferred.')
print('This is an actual affine-quotient calculation; its central refinement and realization by a full lift are not asserted.')
