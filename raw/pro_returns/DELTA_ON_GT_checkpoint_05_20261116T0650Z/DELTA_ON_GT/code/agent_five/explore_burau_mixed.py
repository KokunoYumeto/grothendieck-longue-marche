"""Exploratory exact projective Burau quotient; no GT lifting claim."""
from collections import Counter
import json,sys
N=int(sys.argv[1]) if len(sys.argv)>1 else 2
els=range(N*N)
def ab(x):return x%N,x//N
def enc(a,b):return a%N+N*(b%N)
ADD=[[enc(ab(x)[0]+ab(y)[0],ab(x)[1]+ab(y)[1])for y in els]for x in els]
MUL=[[enc(ab(x)[0]*ab(y)[0]-ab(x)[1]*ab(y)[1],ab(x)[0]*ab(y)[1]+ab(x)[1]*ab(y)[0]-ab(x)[1]*ab(y)[1])for y in els]for x in els]
NEG=[enc(-ab(x)[0],-ab(x)[1])for x in els]
INV={x:next(y for y in els if MUL[x][y]==1)for x in els if any(MUL[x][y]==1 for y in els)}
I=(1,0,0,0,1,0,0,0,1)
w=N

def mm(a,b):
    return tuple(ADD[ADD[MUL[a[3*i]][b[j]]][MUL[a[3*i+1]][b[3+j]]]][MUL[a[3*i+2]][b[6+j]]]for i in range(3)for j in range(3))
def norm(a):
    for x in a:
        if x in INV:return tuple(MUL[INV[x]][y]for y in a)
    raise RuntimeError('no unit')
def pm(a,b):return norm(mm(a,b))
def power(a,n):
    out=I
    for _ in range(n):out=pm(out,a)
    return out
def mi(a):
    m=[list(a[3*i:3*i+3])+[int(i==j)for j in range(3)]for i in range(3)]
    for j in range(3):
        ii=next(i for i in range(j,3)if m[i][j]in INV)
        m[j],m[ii]=m[ii],m[j]
        z=INV[m[j][j]];m[j]=[MUL[z][x]for x in m[j]]
        for i in range(3):
            if i!=j:
                z=m[i][j];m[i]=[ADD[x][NEG[MUL[z][y]]]for x,y in zip(m[i],m[j])]
    return norm(tuple(x for row in m for x in row[3:]))
def order(a):
    out=I
    for n in range(1,10000):
        out=pm(out,a)
        if out==I:return n
    raise RuntimeError('large order')
def group(gens,bound=100000):
    seen={I};todo=[I]
    while todo:
        a=todo.pop()
        for b in gens:
            c=pm(a,b)
            if c not in seen:
                seen.add(c);todo.append(c)
                if len(seen)>bound:return seen,False
    return seen,True

gens=(norm((ADD[1][NEG[w]],w,0,1,0,0,0,0,1)),norm((1,0,0,0,ADD[1][NEG[w]],w,0,1,0)),norm((1,0,NEG[1],0,1,NEG[1],0,0,NEG[w])))
a,b,c=gens
assert pm(pm(a,b),a)==pm(pm(b,a),b)
assert pm(pm(b,c),b)==pm(pm(c,b),c)
assert pm(a,c)==pm(c,a)
assert power(pm(pm(a,b),c),4)==I
X=(power(a,2),power(b,2),power(c,2),power(pm(pm(a,b),a),2),power(pm(pm(c,b),c),2))
print('modulus',N,'generatororders',[order(g)for g in gens],'Xiorders',[order(x)for x in X],flush=True)
G,complete=group(gens)
print('grouporder',len(G),'complete',complete,flush=True)
P,completeP=group(X)
print('pureorder',len(P),'complete',completeP,flush=True)
if complete:
 print('ordercounts',sorted(Counter(order(g)for g in G).items()),flush=True)
for pair in ((2,3),(4,0),(1,2),(3,4),(0,1)):
 H,comp=group([X[i]for i in pair])
 print('pair',pair,'order',len(H),'complete',comp,'productorder',order(pm(*[X[i]for i in pair])),flush=True)
s=pm(pm(a,b),a);r=pm(a,b)
H,comp=group((a,b));Hf,_=group((X[0],X[1]))
Cs=[g for g in Hf if pm(g,s)==pm(s,g)]
Cr=[g for g in Hf if pm(g,r)==pm(r,g)]
def reduce2(g):
 def enc2(z):
  x,y=ab(z);return x%2+2*(y%2)
 a2=tuple(enc2(z)for z in g)
 return a2
print('B3image',len(H),'Fimage',len(Hf),'sorder',order(s),'rorder',order(r),flush=True)
print('scentralizerinF',len(Cs),'rcentralizerinF',len(Cr),'r3inF',power(r,3)in Hf,'s2inF',power(s,2)in Hf,flush=True)
print('centralizer_reduction_counts',len({reduce2(g)for g in Cs}),len({reduce2(g)for g in Cr}),flush=True)
def comm(a,b):return pm(pm(pm(a,b),mi(a)),mi(b))
def normal_closure(base,ambientgens):
 gg=list(base)
 S,_=group(gg)
 while True:
  new=[]
  for s0 in S:
   for h in ambientgens:
    z=pm(pm(h,s0),mi(h))
    if z not in S:new.append(z)
  if not new:return S,gg
  gg+=new;S,_=group(gg)
def derived(H,hgens):
 return normal_closure([comm(g,h)for g in hgens for h in hgens],hgens)
def nilres_ngroup(hgens):
 H,_=group(hgens);DH,dgens=derived(H,hgens)
 NN,ngens=normal_closure(dgens+[power(g,3)for g in hgens],hgens)
 K=NN;kgen=ngens
 sizes=[len(K)]
 while True:
  K2,kg2=normal_closure([comm(g,h)for g in ngens for h in kgen],ngens)
  sizes.append(len(K2))
  if K2==K:break
  K,kgen=K2,kg2
 return H,NN,K,sizes
for pair in ((2,3),(4,0),(1,2),(3,4),(0,1)):
 H,NN,KK,sizes=nilres_ngroup([X[i]for i in pair])
 print('N=HprimeH3',pair,'Norder',len(NN),'lowercentral',sizes,'nilresorders',sorted(Counter(order(g)for g in KK).items()),flush=True)
Delta=pm(pm(pm(pm(pm(a,b),c),a),b),a)
assert power(Delta,2)==I
assert pm(pm(Delta,a),mi(Delta))==c and pm(pm(Delta,b),mi(Delta))==b
H34,_=group((X[2],X[3]))
Z34=[g for g in H34 if all(pm(g,h)==pm(h,g)for h in (X[2],X[3]))]
print('H34centreorder',len(Z34),'elementorders',sorted(Counter(order(g)for g in Z34).items()),flush=True)
z45=mi(pm(X[3],X[4]))
for zz in Z34:
 if order(zz)!=3:continue
 pp=pm(X[2],mi(zz));HH,_=group((pp,X[3]))
 print('stripcentral3',zz,'porder',order(pp),'pairorder',len(HH),'productorder',order(pm(pp,X[3])),flush=True)
 if len(HH)==48:
  cc=[h for h in G if pm(h,X[3])==pm(X[3],h) and pm(pm(h,pp),mi(h))==z45]
  print('conjugators_to_z45_fixX4',len(cc),cc[:1],flush=True)
# Joint isomorphism of the mod-two Burau group with the affine F3 group.
def m3(a,b):return tuple(sum(a[3*i+k]*b[3*k+j]for k in range(3))%3 for i in range(3)for j in range(3))
I3=(1,0,0,0,1,0,0,0,1)
ag=((1,1,0,0,1,0,0,0,1),(1,0,0,2,1,0,0,0,1),(1,1,1,0,1,0,0,0,1))
# Simultaneously retain an actual modulus-four lift for every mod-two matrix.
iso={reduce2(I):I3};lift={reduce2(I):I};todo=[I]
while todo:
 h=todo.pop();h2=reduce2(h);aa=iso[h2]
 for gg,ga in zip(gens,ag):
  z=pm(h,gg);z2=reduce2(z);za=m3(aa,ga)
  if z2 not in iso:iso[z2]=za;lift[z2]=z;todo.append(z)
  else:assert iso[z2]==za
assert len(iso)==216

def lin(h):
 z=iso[reduce2(h)];return (z[0],z[1],z[3],z[4])
def mul2(a,b):return ((a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,(a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3)
def inv2(a):return (a[3],-a[1]%3,-a[2]%3,a[0])
S3=(0,1,2,0)
S_pows=[(1,0,0,1)]
for j in range(1,4):S_pows.append(mul2(S_pows[-1],S3))
Fchoices={}
for rrho in range(3):
 VV=(1,2*rrho%3,0,1);targetF=(1,rrho,rrho,(1+rrho*rrho)%3)
 choices={}
 for beta in Hf:
  WW=mul2(inv2(lin(beta)),VV)
  if WW not in S_pows:continue
  fone=pm(pm(pm(mi(s),beta),s),mi(beta))
  if lin(fone)!=targetF:continue
  eps=S_pows.index(WW)%2
  assert fone not in choices or choices[fone]==eps
  choices[fone]=eps
 Fchoices[rrho]=choices
 assert len(choices)==4
D34,_=derived(H34,[X[2],X[3]])
assert len(D34)==12
zstrip=next(zz for zz in Z34 if order(zz)==3 and len(group((pm(X[2],mi(zz)),X[3]))[0])==48)
pp=pm(X[2],mi(zstrip))
C0=next(h for h in sorted(G)if pm(h,X[3])==pm(X[3],h)and pm(pm(h,pp),mi(h))==z45)
assert pm(pm(z45,X[3]),mi(z45))==pm(power(X[3],2),X[4]) or True
results=[]
for rrho in range(3):
 rchoices=[h for h in D34 if iso[reduce2(h)]==(1,0,-rrho%3,0,1,0,0,0,1)]
 assert len(rchoices)==4
 for jj,rrr in enumerate(sorted(rchoices)):
  HH=pm(pm(C0,rrr),mi(C0))
  GG=pm(pm(pm(mi(z45),HH),z45),mi(HH))
  # Verify the three-cycle expression derived by conjugating x to -y.
  ff=[]
  for ff1,eps in Fchoices[rrho].items():
   total=pm(pm(pm(pm(rrr,pm(pm(Delta,mi(rrr)),Delta)),pm(pm(Delta,mi(ff1)),Delta)),GG),ff1)
   ff.append((eps,total==I))
  results.append({'rho':rrho,'r_index':jj,'solutions_by_harmonic_bit':dict(Counter(e for e,ok in ff if ok)),'candidate_bits':dict(Counter(e for e,_ in ff))})
print('pentagon_reduced_candidates',json.dumps(results),flush=True)
if N==4:
 ec=(1,10,0,8,3,0,0,0,11)
 uu=pm(ec,power(X[3],2))
 report=[]
 for rrho in range(3):
  for ee in range(2):
   RRR=pm(power(uu,ee),power(pp,rrho))
   assert RRR in D34
   HH=pm(pm(C0,RRR),mi(C0))
   GG=pm(pm(pm(mi(z45),HH),z45),mi(HH))
   signs=[]
   for FF,eps in Fchoices[rrho].items():
    PP=pm(pm(pm(pm(RRR,pm(pm(Delta,mi(RRR)),Delta)),pm(pm(Delta,mi(FF)),Delta)),GG),FF)
    if PP==I:signs.append(eps)
   report.append({'rho':rrho,'S4_bit':ee,'allowed_harmonic_bits':signs})
 print('S4_bit_comparison',json.dumps(report),flush=True)
