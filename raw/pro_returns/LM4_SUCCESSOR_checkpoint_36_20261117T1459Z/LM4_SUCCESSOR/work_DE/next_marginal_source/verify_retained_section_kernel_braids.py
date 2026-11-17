#!/usr/bin/env python3
"""Independent quadratic crossing and based-action audit of the three F4 lassos."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,time
import sympy as S
H=Path(__file__).resolve().parent;R=H.parents[1]
p=R/'work_CE/next_symmetric_nodes/retained_section_kernel_braids.json';d=json.loads(p.read_text())
start=time.monotonic();t=S.symbols('t');eps=S.Rational(1,10**50);rot=(Q(1),Q(371,1000))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sc(c,a):return c*a[0],c*a[1]
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def enc(a):return list(map(str,a))
def red(w):
 z=[]
 for k in w:
  if z and z[-1]==-k:z.pop()
  else:z.append(k)
 return tuple(z)
def iv(w):return tuple(-x for x in w[::-1])
def sub(w,f):return red(y for k in w for y in(f[abs(k)] if k>0 else iv(f[abs(k)])))
def mul(*w):return red(k for a in w for k in a)
def push(word):
 A={j:(j,) for j in range(1,5)}
 for k in word:
  i=abs(k);f={j:(j,) for j in range(1,5)}
  f[i],f[i+1]=((i,i+1,-i),(i,)) if k>0 else ((i+1,),(-i-1,i,i+1))
  A={j:sub(A[j],f) for j in range(1,5)}
 return A
def mp(a):return {int(k):tuple(v) for k,v in a.items()}
def val(a,x):return a[0]+x*(a[1]+x*a[2])
def sympoly(a):return S.Poly(sum(S.Rational(c.numerator,c.denominator)*t**j for j,c in enumerate(a)),t)
cache={};summ=[]
def segment(s):
 key=(tuple(s['start']),tuple(s['end']))
 if key in cache:return cache[key]
 a=tuple(map(Q,s['start']));b=tuple(map(Q,s['end']));v=add(b,sc(-1,a));zero=(Q(0),Q(0));one=(Q(1),Q(0))
 polys=[(zero,zero,zero),(one,zero,zero),(a,v,zero),(cm(a,a),sc(2,cm(a,v)),cm(v,v))]
 rs=[tuple(cm(rot,z)[0] for z in pp) for pp in polys];js=[tuple(cm(rot,z)[1] for z in pp) for pp in polys]
 def order(x):
  vals=[val(q,x) for q in rs];assert len(set(vals))==4;return sorted(range(4),key=lambda j:vals[j])
 events=[]
 for i in range(4):
  for j in range(i+1,4):
   rr=tuple(rs[i][k]-rs[j][k] for k in range(3));jj=tuple(js[i][k]-js[j][k] for k in range(3));P=sympoly(rr)
   assert not P.is_zero
   for (lo,hi),m in P.intervals(eps=eps):
    lo=Q(lo);hi=Q(hi)
    if hi<=0 or lo>=1:continue
    assert 0<lo<=hi<1
    x=(lo+hi)/2;h=val(jj,x);bound=(abs(jj[1])+2*abs(jj[2]))*(hi-lo)/2
    assert abs(h)>bound,('collision or unresolved height',key,i,j)
    events.append({'lo':lo,'hi':hi,'pair':(i,j),'P':P})
 events.sort(key=lambda e:e['lo']);groups=[]
 for e in events:
  if groups and e['lo']<=groups[-1]['hi']:
   g=groups[-1]
   for f in g['events']:assert S.gcd(e['P'],f['P']).degree()>0
   g['hi']=max(g['hi'],e['hi']);g['events'].append(e)
  else:groups.append({'lo':e['lo'],'hi':e['hi'],'events':[e]})
 initial=order(Q(0));at=initial[:];word=[]
 for k,g in enumerate(groups):
  before=(Q(0) if k==0 else groups[k-1]['hi'])
  after=(Q(1) if k+1==len(groups) else groups[k+1]['lo'])
  ob=order((before+g['lo'])/2);oa=order((g['hi']+after)/2);assert at==ob
  pos={i:j for j,i in enumerate(oa)};x=(g['lo']+g['hi'])/2
  # Resolve from the RIGHT, independently of the producer's leftmost rule.
  while at!=oa:
   j=max(j for j in range(3) if pos[at[j]]>pos[at[j+1]])
   i,l=at[j:j+2];jj=tuple(js[i][k]-js[l][k] for k in range(3));h=val(jj,x);bound=(abs(jj[1])+2*abs(jj[2]))*(g['hi']-g['lo'])/2
   assert abs(h)>bound
   word.append((j+1) if h<0 else -(j+1));at[j],at[j+1]=at[j+1],at[j]
 assert at==order(Q(1))
 assert initial==s['initial_order'] and at==s['final_order']
 assert push(word)==push(s['word']),('segment braid action mismatch',key)
 cache[key]=tuple(word);summ.append({'start':list(key[0]),'end':list(key[1]),'root_groups':len(groups),'independent_chronological_word':word,'action_matches':True});return tuple(word)
for row in d['loops']:
 W=mul(*(segment(s) for s in row['forward_segments']));L=mul(*(segment(s) for s in row['local_segments']));w=mul(W,L,iv(W));A=push(w);B=push(iv(w))
 assert A==mp(row['geometric_push']) and B==mp(row['geometric_pullback'])
 for j in range(1,5):assert sub(A[j],B)==sub(B[j],A)==(j,)
 assert sub((1,2,3,4),A)==(1,2,3,4)
 # Base lassos are positive peripheral basis loops:their whiskers have Im(v)>0,
 # while all three deleted parameter points lie on the real axis.
 pp=[tuple(map(Q,z)) for z in row['whisker_vertices']];assert all(z[1]>0 for z in pp)
 cc=[tuple(map(Q,z)) for z in row['corners']];assert cc[0]==cc[-1]
 assert sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(cc,cc[1:]))>0
 print('PASS independent quadratic segments and chronological push/pull',row['name'],flush=True)
A0=mp(d['loops'][0]['geometric_push']);A1=mp(d['loops'][1]['geometric_push'])
abc=(1,2,3);Tbc=push((2,2));simple0={j:mul(abc,Tbc[j],iv(abc)) if j<4 else (4,) for j in range(1,5)}
assert A0==simple0
C=(2,3,-2);Z=(-4,2,4);K=mul((1,),C,(4,));basis=[(1,),C,(4,),Z]
for z in basis[:3]:assert sub(z,A1)==mul(K,z,iv(K))
assert sub(Z,A1)==Z
# Explicit inverse for the alternate basis(a,C,d,Z).
fwd={i+1:z for i,z in enumerate(basis)}
bnew=(3,4,-3);invbasis={1:(1,),2:bnew,3:mul(iv(bnew),(2,),bnew),4:(3,)}
for i in range(1,5):assert sub(fwd[i],invbasis)==sub(invbasis[i],fwd)==(i,)
fill={1:(),2:(1,),3:(),4:(2,)}
for A in(A0,A1,mp(d['loops'][0]['geometric_pullback']),mp(d['loops'][1]['geometric_pullback'])):
 for j in range(1,5):assert sub(A[j],fill)==fill[j]
print('PASS both concise local normal forms,both basis directions,and exact q-retained filling invariance.')
out={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'segments_checked':len(cache),'segment_checks':summ,'normal_forms':{'phi0':'Inn(abc) after positive(b,c) full twist on<a,b,c>;fixd','phi1':'Inn(a C d) on<a,C=bcb^-1,d>;fixZ=d^-1bd'},'alternate_basis_forward':fwd,'alternate_basis_inverse':invbasis,'q_retained_filling_invariant':True,'scope':'complete actual two-operator and one-node marking;no full-column consequence','elapsed_seconds':time.monotonic()-start}
(H/'retained_section_kernel_braids_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all17 distinct segments; elapsed',round(out['elapsed_seconds'],3))
