"""Finite A5/2.A5 necessary constraints; no full-word existence claim."""
from contextlib import redirect_stdout
from io import StringIO
with redirect_stdout(StringIO()):
 import check_a5_duality_orbits as G
L,m,iv,e,pr,li,qm,qiv,qe=G.L,G.m,G.iv,G.e,G.pr,G.li,G.qm,G.qiv,G.qe
canon,orbits=G.canon,G.orbits
au_by_q=G.au_by_q
def evdesc(a,b):
 """Value of any commutator word at inputs a,b in L."""
 j,au=orbits[pr[a],pr[b]]
 return j,au
def pw(a,n):
 r=e
 for _ in range(n):r=m[r][a]
 return r
def sameq(a,b):return G.sameclass(pr[a],pr[b])
domains=[]
for j,(a,b) in enumerate(canon):
 A,B=li[a],li[b];local=[]
 for F in range(120):
  Ap=iv[A];Bp=m[m[iv[F]][iv[B]]][F]
  if (pr[Ap],pr[Bp]) not in orbits:continue
  jj,au=evdesc(Ap,Bp)
  if jj!=j:continue
  if not sameq(m[Ap][Bp],iv[m[A][B]]):continue
  if m[F][au[F]]!=e:continue
  us=[U for U in range(120) if U==m[F][au[U]]]
  if not us:continue
  local.append((F,au,us))
 domains.append(local)
 print('orbit',j,'F-domain',len(local),'U-norm total',sum(len(x[2]) for x in local),'U distinct',len(set(u for x in local for u in x[2])))
 # Actual involution must preserve the full binary word identities, but
 # we have not yet coupled the 19 coordinates by duality/hexagon.
print('Domain sizes:',[len(x) for x in domains])

print('\nFIXED-c / BINARY-DUALITY FINITE CONSISTENCY TEST')
used=set();examples=[]
for j,(a,b) in enumerate(canon):
 if j in used:continue
 sj,sw=orbits[b,a];used.add(j);used.add(sj)
 F=e
 da={ff:(au,us) for ff,au,us in domains[j]}
 db={ff:(au,us) for ff,au,us in domains[sj]}
 if e not in da or e not in db:continue
 invsw=[0]*120
 for k,v in enumerate(sw):invsw[v]=k
 for U in da[e][1]:
  V=invsw[iv[U]]
  if V not in db[e][1]:continue
  if sj==j and V!=U:continue
  amap=qconj=lambda aa,uu:G.qcon[G.qiv[pr[uu]]][aa]
  bp=amap(b,U);a2,b2=canon[sj];bp2=amap(b2,V)
  if (a,bp) not in orbits or (a2,bp2) not in orbits:continue
  tj=orbits[a,bp][0];ts=orbits[a2,bp2][0]
  if tj!=j or ts!=sj:
   examples.append((j,sj,tj,ts,U,V))
   print('source swap orbit',(j,sj),'maps to',(tj,ts),'U,V',L[U],L[V])
   break
print('finite fixed-c duality tables with changed kernels:',len(examples))
if examples:
 j,sj,tj,ts,U,V=examples[0]
 print('A global table with these two entries and U=1 on all other factors merges a coordinate if target outside source:',tj not in (j,sj))
 print('This does NOT lift full c-fixedness: C_F(c)=1 forbids it for a canonical full word.')
