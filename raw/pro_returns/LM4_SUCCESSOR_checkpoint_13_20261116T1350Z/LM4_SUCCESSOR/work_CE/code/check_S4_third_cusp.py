"""Exact GL2(F3) finite necessary conditions for the canonical S4 third cusp.
We retain common S3 word values and impose binary duality, the negative
hexagon, involutivity, and the canonical norm. No full realization inferred.
"""
from itertools import product,permutations
from collections import Counter
P=3
def mm(a,b):return ((a[0]*b[0]+a[1]*b[2])%P,(a[0]*b[1]+a[1]*b[3])%P,(a[2]*b[0]+a[3]*b[2])%P,(a[2]*b[1]+a[3]*b[3])%P)
def dt(a):return (a[0]*a[3]-a[1]*a[2])%P
def mi(a):
 d=pow(dt(a),-1,P)
 return(a[3]*d%P,-a[1]*d%P,-a[2]*d%P,a[0]*d%P)
def neg(a):return tuple(-x%P for x in a)
G=[a for a in product(range(3),repeat=4) if dt(a)];ix={a:i for i,a in enumerate(G)}
e=ix[(1,0,0,1)];m=[[ix[mm(a,b)] for b in G] for a in G];iv=[ix[mi(a)] for a in G]
con=[[m[m[h][a]][iv[h]] for a in range(48)] for h in range(48)]
L=[a for a in range(48) if dt(G[a])==1]
Q=sorted({min(a,neg(a)) for a in G});qi={a:i for i,a in enumerate(Q)};li=[ix[a] for a in Q]
pr=[qi[min(a,neg(a))] for a in G];qe=pr[e]
qm=[[pr[m[a][b]] for b in li] for a in li];qiv=[pr[iv[a]] for a in li]
qc=[[qm[qm[h][a]][qiv[h]] for a in range(24)] for h in range(24)]
def pw(a,n):
 r=e
 for _ in range(n):r=m[r][a]
 return r
def qpow(a,n):return pr[pw(li[a],n)]
def order(a):
 b=qe
 for j in range(1,25):
  b=qm[b][a]
  if b==qe:return j
def sub(a,b):
 out={qe};todo=[qe]
 while todo:
  h=todo.pop()
  for t in(a,b):
   u=qm[h][t]
   if u not in out:out.add(u);todo.append(u)
 return out
V=[a for a in range(24) if a!=qe and order(a)==2 and dt(Q[a])==1]
assert len(V)==3
heads=[tuple(V.index(qc[pr[g]][a]) for a in V) for g in range(48)]
assert len(set(heads))==6
S3=list(permutations(range(3)))
def sm(a,b):return tuple(a[b[i]] for i in range(3))
def si(a):return tuple(a.index(i) for i in range(3))
def sc(h,a):return sm(sm(h,a),si(h))
se=(0,1,2);sa=(1,0,2);st=(1,2,0)
def sp(a,n):
 b=se
 for _ in range(n%6):b=sm(b,a)
 return b
def so(a):
 for j in range(1,7):
  if sp(a,j)==se:return j
def hev(a,b,k,l):
 oa,ob=so(a),so(b)
 if(oa,ob)==(2,2):base=(sa,sm(sa,st));val=sp(st,k)
 elif(oa,ob)==(3,2):base=(st,sa);val=sp(st,l)
 elif(oa,ob)==(2,3):base=(sa,st);val=sp(st,-l)
 else:raise ValueError((oa,ob))
 hh=next(h for h in S3 if(sc(h,base[0]),sc(h,base[1]))==(a,b))
 return sc(hh,val)
orbits={};reps=[]
for a,b in product(range(24),repeat=2):
 if (a,b) in orbits or len(sub(a,b))<24:continue
 j=len(reps);reps.append((a,b))
 for h in range(48):orbits[pr[con[h][li[a]]],pr[con[h][li[b]]]]=(j,con[h])
assert len(reps)==9 and len(orbits)==216
assert len({(order(a),order(b),order(qm[a][b])) for a,b in reps})==9
printed_C40_table=[
 ((0,1,1,0),(0,1,1,1)),
 ((0,1,1,0),(1,0,1,1)),
 ((0,1,1,1),(0,1,1,0)),
 ((0,1,1,1),(0,1,1,2)),
 ((0,1,1,1),(0,1,2,1)),
 ((0,1,1,1),(1,0,2,1)),
 ((0,1,2,1),(0,1,1,1)),
 ((0,1,2,1),(1,0,0,2)),
 ((0,1,2,1),(1,1,1,0))]
assert [(Q[a],Q[b]) for a,b in reps]==printed_C40_table
def evpair(a,b):return orbits[pr[a],pr[b]]
swap=[evpair(li[b],li[a]) for a,b in reps]
hexdata=[]
for a,b in reps:
 A,B=li[a],li[b];Z=iv[m[A][B]]
 hexdata.append((A,B,Z,evpair(Z,A),evpair(B,Z)))
edges=[{j,swap[j][0],hexdata[j][3][0],hexdata[j][4][0]} for j in range(9)]
components=[];unused=set(range(9))
while unused:
 C={min(unused)}
 while True:
  D=set().union(*(edges[j] for j in C))
  if D<=C:break
  C|=D
 components.append(sorted(C));unused-=C
print('Nine S4 passports:',[(order(a),order(b),order(qm[a][b])) for a,b in reps])
for j,(a,b) in enumerate(reps):print('representative',j,'A=',Q[a],'B=',Q[b])
print('Hexagon/duality components:',components)
for k in(0,2):
 for l in range(3):
  mu=1 if k==0 else 5
  dom=[]
  for j,(a,b) in enumerate(reps):
   A,B=li[a],li[b];wantF=hev(heads[A],heads[B],0,2*l);wantU=hev(heads[A],heads[B],k,l)
   d={}
   for F in L:
    if heads[F]!=wantF:continue
    Ap=iv[A];Bp=m[m[iv[F]][iv[B]]][F]
    if(pr[Ap],pr[Bp]) not in orbits:continue
    jj,au=evpair(Ap,Bp)
    if jj!=j or m[F][au[F]]!=e:continue
    if pr[m[Ap][Bp]] not in {qc[h][qiv[qm[a][b]]] for h in range(24)}:continue
    us=[]
    for U in L:
     if heads[U]!=wantU or U!=m[F][au[U]]:continue
     bp=pr[m[m[iv[U]][B]][U]]
     if(a,bp) not in orbits:continue # C39 proved generation
     us.append(U)
    if us:d[F]=us
   dom.append(d)
  print('\nhead(k,l),mu=',(k,l),mu,'F domain sizes',[len(d) for d in dom])
  for C in components:
   sr=[j for j in C if j<=swap[j][0]]
   choices=[]
   for j in sr:
    sj,au=swap[j];invau=[0]*48
    for a,b in enumerate(au):invau[b]=a
    opts=[]
    for F,us in dom[j].items():
     F2=invau[iv[F]]
     if F2 not in dom[sj] or (sj==j and F2!=F):continue
     uopts=[]
     for U in us:
      U2=invau[iv[U]]
      if U2 not in dom[sj][F2] or(sj==j and U2!=U):continue
      uopts.append((U,U2))
     if uopts:opts.append((F,F2,uopts))
    choices.append(opts)
   countF=countU=bad=0;example=None;maps=Counter()
   allowedF={j:set() for j in C};allowedU={j:set() for j in C}
   for fs in product(*choices):
    Ft={}
    for j,(F,F2,us) in zip(sr,fs):Ft[j]=F;Ft[swap[j][0]]=F2
    good=True
    for j in C:
     A,B,Z,(j1,au1),(j2,au2)=hexdata[j]
     val=e
     for z in(Ft[j],iv[A],au1[Ft[j1]],iv[Z],au2[Ft[j2]],iv[B]):val=m[val][z]
     if val!=e:good=False;break
    if not good:continue
    countF+=1
    for us in product(*(v[2] for v in fs)):
     Ut={}
     for j,(U,U2) in zip(sr,us):Ut[j]=U;Ut[swap[j][0]]=U2
     countU+=1
     for j in C:allowedF[j].add(Ft[j]);allowedU[j].add(Ut[j])
     passes=True;changes=[]
     for j in C:
      a,b=reps[j];A,B=li[a],li[b];U=Ut[j]
      val=m[m[m[pw(A,mu)][iv[U]]][pw(B,mu)]][U]
      old=pw(m[A][B],mu)
      ok=pr[val] in {qc[h][pr[old]] for h in range(24)}
      if not ok:passes=False;changes.append((j,order(pr[val]),order(pr[old])))
     if not passes:
      bad+=1
      if example is None:example=(Ft.copy(),Ut.copy(),changes)
   print('component',C,'F tables',countF,'(F,U) tables',countU,'third-cusp failures',bad)
   assert countF==(4 if len(C)==6 else 2)
   assert countU==(64 if len(C)==6 else 16)
   assert bad==0
   if l==0:
    for j in C:
     if (order(reps[j][0]),order(reps[j][1]))==(3,4):
      print(' (3,4) orbit',j,'allowed F=',[G[a] for a in sorted(allowedF[j])],'allowed U=',[G[a] for a in sorted(allowedU[j])])
   if example:
    Ft,Ut,changes=example
    print(' finite failure changes',changes,'F=',{j:G[v] for j,v in Ft.items()},'U=',{j:G[v] for j,v in Ut.items()})
print('\nEvery necessary finite table satisfies the correctly normalized S4 third cusp: PASS')
print('No assertion that an arbitrary finite table is a full canonical word is used or inferred.')
