"""Complete small-head pentagon probe for the specific A5 false-positive table.

Finite scope only. The normal F3 fiber of P4 maps either trivially or onto A5
in an epimorphism P4 -> A5. In the second case the three P3 images, if they
exist, are uniquely determined by their actions on a generating fiber triple.
This avoids enumerating arbitrary sextuples. Binary lifts are checked against
the exact pure Artin relations. No full canonical-word existence is asserted.
"""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from collections import Counter
with redirect_stdout(StringIO()):
    import check_a5_duality_orbits as G
L,m,iv,e,pr,li,qm,qiv,qe=G.L,G.m,G.iv,G.e,G.pr,G.li,G.qm,G.qiv,G.qe
qc=G.qcon;co=G.co
def mul(*xs):
 z=e
 for x in xs:z=m[z][x]
 return z
def qmul(*xs):
 z=qe
 for x in xs:z=qm[z][x]
 return z
def comm(x,y):return mul(x,y,iv[x],iv[y])
def qcomm(x,y):return qmul(x,y,qiv[x],qiv[y])
def generated(xs):
 h={qe};todo=[qe]
 while todo:
  a=todo.pop()
  for b in xs:
   c=qm[a][b]
   if c not in h:h.add(c);todo.append(c)
 return h
def pure_ok(v):
 a,b,c,d,ee,f=v
 return (
  co[iv[a]][b]==co[mul(b,c)][b] and co[iv[a]][c]==co[b][c]
  and co[iv[a]][f]==f and co[iv[c]][d]==d
  and co[iv[a]][d]==co[mul(d,ee)][d] and co[iv[a]][ee]==co[d][ee]
  and co[iv[b]][d]==co[mul(d,f)][d] and co[iv[b]][f]==co[d][f]
  and co[iv[b]][ee]==co[comm(d,f)][ee]
  and co[iv[c]][ee]==co[mul(ee,f)][ee] and co[iv[c]][f]==co[ee][f])

tab=[e]*19;tab[4]=G.ix[(0,2,2,0)];tab[10]=G.ix[(0,3,3,0)]
def value(a,b):
 if (pr[a],pr[b]) in G.orbits:
  j,au=G.orbits[pr[a],pr[b]]
  return au[tab[j]]
 return e

seen=set();counts=Counter();reps=[]
for triple in product(range(60),repeat=3):
 if triple in seen:continue
 orbit={tuple(au[x] for x in triple) for au in G.au_by_q}
 seen.update(orbit)
 counts['fiber_triple_orbits']+=1
 if len(generated(triple))!=60:continue
 counts['generating_fiber_triple_orbits']+=1
 d,ee,f=triple
 conjugators={tuple(qc[h][x] for x in triple):h for h in range(60)}
 assert len(conjugators)==60
 ta=(qc[qm[d][ee]][d],qc[d][ee],f)
 tb=(qc[qm[d][f]][d],qc[qcomm(d,f)][ee],qc[d][f])
 tc=(d,qc[qm[ee][f]][ee],qc[ee][f])
 if any(t not in conjugators for t in (ta,tb,tc)):continue
 a,b,c=(qiv[conjugators[t]] for t in (ta,tb,tc))
 # Check the P3 equations independently rather than relying on center-freeness.
 assert qc[qiv[a]][b]==qc[qm[b][c]][b]
 assert qc[qiv[a]][c]==qc[b][c]
 counts['projective_P4_epimorphism_orbits_nontrivial_fiber']+=1
 vv=tuple(li[x] for x in (a,b,c,d,ee,f))
 if not pure_ok(vv):
  counts['projective_orbits_without_binary_lift']+=1;continue
 counts['binary_P4_epimorphism_orbits_nontrivial_fiber']+=1
 reps.append(vv)
assert len(seen)==60**3
for a,b in G.canon:
 c=qiv[qm[a][b]]
 vv=tuple(li[x] for x in (a,b,c,qe,qe,qe))
 assert pure_ok(vv)
 reps.append(vv)
 counts['binary_P4_epimorphism_orbits_trivial_fiber']+=1

patterns=Counter();bad=0;witness=None;touches=Counter();forgetting_types=Counter()
dual_tests=0;reduction_types=Counter()
for v in reps:
 a,b,c,d,ee,f=v
 qa,qb,qc0,qd,qee,qf=(pr[x] for x in v)
 types=[]
 if qa==qb==qd==qe and qmul(qc0,qee,qf)==qe:types.append('forget strand 1')
 if qa==qc0==qee==qe and qmul(qb,qd,qf)==qe:types.append('forget strand 2')
 if qb==qc0==qf==qe and qmul(qa,qd,qee)==qe:types.append('forget strand 3')
 if qd==qee==qf==qe and qmul(qa,qb,qc0)==qe:types.append('forget strand 4')
 if qa==qf and qc0==qd and qb==qiv[qmul(qd,qf)] and qee==qiv[qmul(qf,qd)]:
  types.append('forget sphere point infinity')
 assert len(types)==1,(v,types)
 forgetting_types[types[0]]+=1
 ps=[(a,mul(c,ee)),(mul(b,c),f),(c,f),(mul(a,b),mul(ee,f)),(a,c)]
 vals=[value(*p) for p in ps]
 sig=[]
 for aa,bb in ps:
  if (pr[aa],pr[bb]) in G.orbits:
   j,_=G.orbits[pr[aa],pr[bb]];sig.append(('A5',j));touches[j]+=1
  else:sig.append(('proper',len(generated((pr[aa],pr[bb]))),mul(aa,bb)==mul(bb,aa)))
 patterns[tuple(sig)]+=1
 active=[i for i,(aa,bb) in enumerate(ps) if (pr[aa],pr[bb]) in G.orbits]
 assert len(active)==2
 i0,i1=active
 j0,au0=G.orbits[pr[ps[i0][0]],pr[ps[i0][1]]]
 j1,au1=G.orbits[pr[ps[i1][0]],pr[ps[i1][1]]]
 sj,sw=G.orbits[G.canon[j0][1],G.canon[j0][0]]
 assert j1 in (j0,sj)
 invsw=[0]*120
 for aa,bb in enumerate(sw):invsw[bb]=aa
 for uu in range(120):
  vv=invsw[iv[uu]]
  if sj==j0 and vv!=uu:continue
  testtab={j0:uu,sj:vv}
  values=[e]*5
  values[i0]=au0[testtab[j0]];values[i1]=au1[testtab[j1]]
  assert mul(values[0],values[1])==mul(values[2],values[3],values[4])
  dual_tests+=1
 reduction_types['same-side duality' if (i0<2)==(i1<2) else 'opposite-side equality']+=1
 lhs=mul(vals[0],vals[1]);rhs=mul(vals[2],vals[3],vals[4])
 if lhs!=rhs:
  bad+=1
  if witness is None:witness=(v,ps,vals,sig,lhs,rhs)
print('Exact reduction counts:',dict(counts))
print('Total binary P4 epimorphism orbits:',len(reps))
print('Explicit factorization through the five forgetful F2 maps:',dict(forgetting_types))
assert set(forgetting_types.values())=={19} and len(forgetting_types)==5
print('Pentagon argument-orbit patterns:',len(patterns))
print('Generating pair coordinates touched:',dict(sorted(touches.items())))
print('Failures of the specified finite table:',bad)
print('Every equation follows from binary duality with proper values 1:',dict(reduction_types),'tested assignments',dual_tests)
assert counts['generating_fiber_triple_orbits']==1668
assert counts['projective_P4_epimorphism_orbits_nontrivial_fiber']==76
assert len(reps)==95 and bad==0
if witness:
 v,ps,vals,sig,lhs,rhs=witness
 print('Witness pure generators:',[L[x] for x in v])
 print('Witness five pair signatures:',sig)
 print('Witness five values:',[L[x] for x in vals])
 print('Witness LHS,RHS:',L[lhs],L[rhs])
print('Proper projective images have all five values 1 for this table, so their pentagons hold automatically.')
print('This is a finite consistency test; it gives neither a full word nor a full involution.')
