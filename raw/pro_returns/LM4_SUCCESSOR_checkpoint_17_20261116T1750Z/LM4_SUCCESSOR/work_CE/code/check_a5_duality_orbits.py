"""Small exact A5 generation/duality reconnaissance.
This classifies19 automorphism orbits and tests only necessary binary
icosahedral duality constraints. It makes no full-word existence assertion.
"""
from itertools import product
P=5
def mm(a,b):return((a[0]*b[0]+a[1]*b[2])%P,(a[0]*b[1]+a[1]*b[3])%P,(a[2]*b[0]+a[3]*b[2])%P,(a[2]*b[1]+a[3]*b[3])%P)
def dt(a):return(a[0]*a[3]-a[1]*a[2])%P
def mi(a):
 d=pow(dt(a),-1,P);return(a[3]*d%P,-a[1]*d%P,-a[2]*d%P,a[0]*d%P)
def ng(a):return tuple(-x%P for x in a)
L=[a for a in product(range(P),repeat=4) if dt(a)==1];ix={a:i for i,a in enumerate(L)}
e=ix[(1,0,0,1)];m=[[ix[mm(a,b)] for b in L] for a in L];iv=[ix[mi(a)] for a in L]
co=[[m[m[a][b]][iv[a]] for b in range(120)] for a in range(120)]
Q=sorted({min(a,ng(a)) for a in L});qi={a:i for i,a in enumerate(Q)};pr=[qi[min(a,ng(a))] for a in L];li=[ix[a] for a in Q];qe=pr[e]
qm=[[pr[m[a][b]] for b in li] for a in li];qiv=[pr[iv[a]] for a in li]
def subgroup(a,b):
 h={qe};todo=[qe]
 while todo:
  g=todo.pop()
  for s in (a,b):
   v=qm[g][s]
   if v not in h:h.add(v);todo.append(v)
 return h
def order(a):
 v=qe
 for j in range(1,61):
  v=qm[v][a]
  if v==qe:return j
au_by_q={}
for h in product(range(P),repeat=4):
 if not dt(h):continue
 au=[ix[mm(mm(h,a),mi(h))] for a in L];aq=tuple(pr[au[a]] for a in li)
 au_by_q[aq]=au
assert len(au_by_q)==120
orbits={};canon=[]
for a,b in product(range(60),repeat=2):
 if (a,b) in orbits or len(subgroup(a,b))<60:continue
 j=len(canon);canon.append((a,b))
 for aq,au in au_by_q.items():orbits[aq[a],aq[b]]=(j,au)
assert len(canon)==19
print('Generating A5 pair orbits:',len(canon),'totalpairs:',len(orbits))
for j,(a,b) in enumerate(canon):
 passport=(order(a),order(b),order(qm[a][b]));swapj,swap=orbits[b,a]
 if swapj==j:allowed=[u for u in range(120) if m[u][swap[u]]==e]
 else:allowed=list(range(120))
 counts={}
 for u in allowed:
  bb=pr[co[iv[u]][li[b]]];n=len(subgroup(a,bb));counts[n]=counts.get(n,0)+1
 print('orbit',j,'passport',passport,'swap-orbit',swapj,'binary duality image orders',counts,'A=',Q[a],'B=',Q[b])

# Full finite certificate for the proposed nineteen-orbit proof. Only
# necessary conditions on genuine full alpha,u are used. The final two
# exclusions are the section-class arguments proved separately in notes.
qcon=[[qm[qm[g][a]][qiv[g]] for a in range(60)] for g in range(60)]
inner={tuple(qcon[h]):h for h in range(60)}
def qaut(au):return tuple(pr[au[a]] for a in li)
def sameclass(a,b):return b in {qcon[h][a] for h in range(60)}
critical=[]
print('\nEXACT PASSPORT / NEGATIVE-KERNEL CERTIFICATE')
for j,(a,b) in enumerate(canon):
 oa,ob,oz=order(a),order(b),order(qm[a][b]);sc=sameclass(a,b) if oa==ob==5 else None
 needsinner=(2 in (oa,ob)) or (oa==ob==3) or (oa==ob==5 and sc)
 if needsinner:
  count=0
  target={qcon[h][qiv[qm[a][b]]] for h in range(60)}
  for f in range(60):
   aa=qiv[a];bb=qcon[qiv[f]][qiv[b]]
   if qm[aa][bb] not in target or (aa,bb) not in orbits:continue
   jj,au=orbits[aa,bb]
   assert jj==j,(j,jj,'negative kernel changes')
   assert qaut(au) in inner,(j,'negative action outer')
   count+=1
  assert count
  critical.append(j)
  print('orbit',j,'passport',(oa,ob,oz),'same5class',sc,'all negative peripheral candidates inner:',count)
 sj,sw=orbits[b,a]
 if oa==ob:
  assert sj==j
  assert (qaut(sw) in inner)==(oa==3 or sc)

print('\nEXACT PROPER-IMAGE ELIMINATION CERTIFICATE')
from collections import Counter
summary=Counter()
for j,(a,b) in enumerate(canon):
 oa,ob,oz=order(a),order(b),order(qm[a][b]);sj,sw=orbits[b,a]
 allowed=[u for u in range(120) if sj!=j or m[u][sw[u]]==e]
 stats=Counter()
 for u in allowed:
  qu=pr[u];bb=qcon[qiv[qu]][b];M=subgroup(a,bb)
  if len(M)==60:stats['generated']+=1;continue
  stats['proper_candidates']+=1
  assert j in critical,(j,'proper image outside proved inner-action cases')
  hs=[h for h in range(60) if qm[h][h]==qe and qcon[h][a]==qiv[a] and qcon[h][bb]==qiv[bb]]
  if not hs:
   stats['no_inverting_inner_involution']+=1;continue
  if 2 in (oa,ob):
   invol=a if oa==2 else bb
   assert all(h==invol for h in hs)
   assert oz>2
   stats['central_section_third_cusp_contradiction']+=1
   continue
  # Residual equal-order case. If a3/3 image were A4, no such h exists.
  assert len(M)==oa and oa in (3,5)
  rr=None
  for r in range(1,oa):
   value=qe
   for _ in range(r):value=qm[value][a]
   if value==bb:rr=r;break
  assert rr in (1,oa-1)
  # The plus case is already excluded by the full binary duality norm.
  assert rr==oa-1,(j,'plus-collapse survived binary duality')
  sq=qaut(sw);vq=tuple(qcon[qiv[qu]][sq[g]] for g in range(60))
  assert vq in inner
  vh=inner[vq]
  assert qcon[vh][a]==bb and qcon[vh][bb]==a and qm[vh][vh]==qe
  commuting=[h for h in hs if qm[h][vh]==qm[vh][h]]
  assert commuting and all(h==vh for h in commuting)
  assert oz>1
  stats['one_section_third_cusp_contradiction']+=1
 print('orbit',j,dict(stats))
 summary.update(stats)
print('TOTAL NECESSARY-CONDITION COUNTS:',dict(summary))
print('Every proper-image candidate is excluded by an explicit proved mechanism:',True)
assert summary['proper_candidates']==sum(summary[k] for k in ('no_inverting_inner_involution','central_section_third_cusp_contradiction','one_section_third_cusp_contradiction'))
