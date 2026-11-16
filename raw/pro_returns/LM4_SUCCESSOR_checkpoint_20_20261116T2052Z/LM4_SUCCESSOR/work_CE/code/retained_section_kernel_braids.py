#!/usr/bin/env python3
"""Exact two-operator/one-relator retained-section kernel presentation inputs.

Four polynomial q punctures0,1,v,v^2 over the v-plane.  The three actual
base lassos are about0,1,-1; only the last is filled.  No source-orbit search.
The rational crossing routine is copied from the previously audited
w-pencil engine, reduced to four strands without changing its conventions.
"""
from pathlib import Path
from collections import defaultdict
import itertools,json,time,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
DE=ROOT/'work_DE/next_marginal_source';sys.path.insert(0,str(DE))
import sympy as S
from w_pencil_braid import (F,I,Q,X,ROT,u,EPS,frac,sy,red,invert,parts,pval,roots,lower_norm,ppoly_from_record,Segment as OldSegment)
P=ROOT/'work_CE/next_symmetric_nodes'

class Segment(OldSegment):
 def __init__(self,a,b):
  self.a,self.b=a,b;v=S.expand(a+(b-a)*X);self.t=v
  rr=[S.Integer(0),S.Integer(1),v,S.expand(v*v)]
  self.raw_rational=rr;self.rational=[parts(ROT*z) for z in rr]
  self.U=[];self.axis=[];self.center=parts(S.Integer(0));self.parameter_bound=3
  assert abs(S.re(a))+abs(S.im(a))<3 and abs(S.re(b))+abs(S.im(b))<3
  self.derivative_bound=F(10**8)
  for R,J in self.rational:
   assert sum(abs(frac(c)) for pp in [R.diff(),J.diff()] for c in pp.all_coeffs())<10**6
  for r,t in itertools.combinations(rr,2):
   R,J=parts(r-t);lower_norm(R,J,F(1,10**12))
  self.records=[];self.candidates=[]
 def point(self,label,x):
  R,J=self.rational[label];a,b=pval(R,x),pval(J,x)
  return (a,a),(b,b)
 def order(self,x):
  vals=[self.point(i,x)[0] for i in range(4)]
  ans=sorted(range(4),key=lambda i:vals[i][0])
  for i,j in zip(ans,ans[1:]):assert vals[i][1]<vals[j][0],('projection tie',x,i,j)
  return ans
 def compute(self):
  for i,j in itertools.combinations(range(4),2):self.addpoly('rational',[i,j],self.rational[i][0]-self.rational[j][0])
  for k,(A,B) in enumerate(self.U):
   self.addpoly('quadratic_self',[k],B)
   for i in range(4):
    h=self.rational[i][0]-self.center[0]
    self.addpoly('quadratic_rational',[k,i],4*h*h*(h*h-A)-B*B)
  for i,j in itertools.combinations(range(len(self.U)),2):
   A,B=self.U[i];C,D=self.U[j];delta=C-A;N=B*B-D*D
   self.addpoly('quadratic_pair',[i,j],N*N-4*A*N*delta-4*B*B*delta*delta)
  self.candidates.sort(key=lambda e:e['lo']);groups=[]
  for e in self.candidates:
   if groups and e['lo']<=groups[-1]['hi']:
    groups[-1]['hi']=max(groups[-1]['hi'],e['hi']);groups[-1]['events'].append(e)
   else:groups.append({'lo':e['lo'],'hi':e['hi'],'events':[e]})
  # Overlaps must be genuine common roots, not unresolved nearby events.
  for g in groups:
   for e,f in itertools.combinations(g['events'],2):
    if e['record']==f['record']:raise AssertionError('two roots from one polynomial overlap')
    p=ppoly_from_record(self.records[e['record']]);q=ppoly_from_record(self.records[f['record']])
    gcd=S.gcd(p,q)
    assert gcd.degree()>0 and gcd.count_roots(sy(g['lo']),sy(g['hi']))>0
  initial=self.order(F(0));at=list(initial);word=[];events=[]
  for gi,g in enumerate(groups):
   left=F(0) if gi==0 else groups[gi-1]['hi']
   right=F(1) if gi+1==len(groups) else groups[gi+1]['lo']
   before=(left+g['lo'])/2;after=(g['hi']+right)/2
   ob=self.order(before);oa=self.order(after);assert at==ob
   positions={a:i for i,a in enumerate(oa)}
   pairs=[(a,b) for i,a in enumerate(ob) for b in ob[i+1:] if positions[a]>positions[b]]
   if not pairs:continue
   # The source and diagonal have midpoint w among the rational strands.
   # Three-strand vertical events are therefore unavoidable for a linear
   # projection. Resolve them inside disjoint certified height disks.
   # Adjacent inversions give a reduced sorting word; consistent total
   # height ordering makes different choices braid-equivalent.
   # Evaluate immediately before the event, outside the square-root cut
   # intervals, then enclose the full crossing interval by the derivative
   # bound.  Midpoint evaluation would straddle a principal-root cut at
   # exactly the self-crossings whose analytic branches remain regular.
   sample=g['lo']-max(g['hi']-g['lo'],frac(EPS))
   assert left<sample<g['lo']
   rad=self.derivative_bound*(g['hi']-sample)
   crossings=[];remaining=len(pairs)
   # Certify all heights in every connected inversion cluster, including
   # pairs that do not themselves change horizontal order.
   clusters=[]
   for a,b in pairs:
    touching=[c for c in clusters if a in c or b in c]
    merged={a,b}
    for c in touching:merged.update(c);clusters.remove(c)
    clusters.append(merged)
   for cluster in clusters:
    for a,b in itertools.combinations(sorted(cluster),2):
     ai=self.point(a,sample)[1];bi=self.point(b,sample)[1]
     gap=(ai[0]-bi[1]-2*rad,ai[1]-bi[0]+2*rad)
     assert gap[0]>0 or gap[1]<0,'uncertified distinct cluster heights'
   while at!=oa:
    j=next(j for j in range(len(at)-1) if positions[at[j]]>positions[at[j+1]])
    a,b=at[j],at[j+1]
    ai=self.point(a,sample)[1];bi=self.point(b,sample)[1]
    difference=(ai[0]-bi[1]-2*rad,ai[1]-bi[0]+2*rad)
    assert difference[0]>0 or difference[1]<0,'uncertified crossing height'
    sign=-1 if difference[0]>0 else 1
    word.append(sign*(j+1));at[j],at[j+1]=at[j+1],at[j]
    crossings.append({'labels':[a,b],'generator':sign*(j+1),'imaginary_difference_bounds':[str(x) for x in difference]})
    remaining-=1
   assert remaining==0
   assert at==oa
   events.append({'interval':[str(g['lo']),str(g['hi'])],'candidate_records':[e['record'] for e in g['events']],
                  'crossings':crossings,'resolved_cluster_sizes':[len(c) for c in clusters]})
  final=self.order(F(1));assert at==final
  return {'start':[str(S.re(self.a)),str(S.im(self.a))],'end':[str(S.re(self.b)),str(S.im(self.b))],
          'initial_order':initial,'final_order':final,'word':red(word),'crossing_count':len(word),
          'polynomials':self.records,'actual_events':events,
          'uniform_rational_difference_lower_bound':'1/10^12',
          'uniform_quadratic_residual_lower_bound':'1/10^12',
          'uniform_projected_square_norm_lower_bound':'1/10^8','derivative_bound':'100000000',
          **({'parameter_L1_bound':str(self.parameter_bound)} if self.parameter_bound!=5 else {})}

def rmul(*words):return tuple(red(x for w in words for x in w))
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return rmul(*(A[x] if x>0 else inv(A[-x]) for x in w))
def art(w):
 A={i:(i,) for i in range(1,5)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(rmul(a,b,inv(a)),a) if x>0 else (b,rmul(inv(b),a,b))
 return A

def run():
 started=time.monotonic();base=u[2];hub=-Q(1,5)+I*Q(2,5);mid=-Q(4,5)+I*Q(1,5);h=Q(1,1000)
 cases=[('v0',S.Integer(0),[base,hub,-h+I*h],8,{(0,2):2,(0,3):4,(2,3):2}),
        ('v1',S.Integer(1),[base,hub,1-h+I*h],6,{(1,2):2,(1,3):2,(2,3):2}),
        ('vminus1',-S.Integer(1),[base,mid,-1+h+I*h],2,{(1,3):2})]
 cache={};rows=[];initial=None
 def segment(a,b):
  nonlocal initial
  if (a,b) not in cache:
   r=Segment(a,b).compute();cache[a,b]=r
   if initial is None:initial=r['initial_order'];assert initial==[2,0,3,1]
   print('segment',len(cache),'crossings',r['crossing_count'],'elapsed',round(time.monotonic()-started,3),flush=True)
  return cache[a,b]
 for name,center,path,exponent,want in cases:
  corners=[center+h+I*h,center-h+I*h,center-h-I*h,center+h-I*h]
  k=next(i for i,z in enumerate(corners) if z==path[-1]);corners=[corners[(k+j)%4] for j in range(5)]
  forward=[segment(a,b) for a,b in zip(path,path[1:])]
  local=[segment(a,b) for a,b in zip(corners,corners[1:])]
  W=rmul(*(r['word'] for r in forward));L=rmul(*(r['word'] for r in local));word=rmul(W,L,inv(W))
  assert sum(1 if x>0 else -1 for x in word)==exponent
  perm=list(initial);link=defaultdict(int)
  for x in word:
   i=abs(x)-1;a,b=perm[i:i+2];link[tuple(sorted((a,b)))]+=1 if x>0 else -1
   perm[i],perm[i+1]=perm[i+1],perm[i]
  assert perm==initial
  assert {k:v for k,v in link.items() if v}==want
  push=art(tuple(reversed(word)));pull=art(tuple(-x for x in word))
  for i in range(1,5):assert sub(push[i],pull)==sub(pull[i],push)==(i,)
  assert sub((1,2,3,4),push)==sub((1,2,3,4),pull)==(1,2,3,4)
  if name=='vminus1':
   assert W==() and art(tuple(reversed(L)))==art((3,3))
   assert push==art((3,3))
  # Every whisker lies in the upper half v-plane; a downward-cut reading
  # makes these the three actual positive peripheral basis loops.
  assert all(S.im(z)>0 for z in path)
  rows.append({'name':name,'center':[str(S.re(center)),str(S.im(center))],
    'whisker_vertices':[[str(S.re(z)),str(S.im(z))] for z in path],
    'corners':[[str(S.re(z)),str(S.im(z))] for z in corners],
    'forward_segments':forward,'local_segments':local,'whisker_word':W,'local_word':L,
    'chronological_braid':word,'geometric_push':push,'geometric_pullback':pull,
    'exponent':exponent,'pair_crossing_sums':[{'labels':list(k),'sum':v} for k,v in sorted(want.items())]})
  print('PASS',name,'word',list(word),'push',push,flush=True)
 conversion=json.loads((DE/'old_lassos_far_cut_conversion.json').read_text())
 filling={1:(1,),2:(),3:(),4:(2,),5:(3,),6:(4,)}
 old_to_four={int(j):sub(w,filling) for j,w in conversion['forward_old_to_far'].items()}
 assert old_to_four=={1:(2,),2:(4,),3:(),4:(1,),5:(),6:(3,)}
 r=(3,4,-3,-4);assert sub(conversion['old_commutator'],old_to_four)==r
 delta={1:(),2:(1,),3:(),4:(2,)}
 ops={r['name']:{int(k):tuple(v) for k,v in r['geometric_push'].items()} for r in rows}
 L=(1,2,3);M=(1,2,3,2,3)
 g0={1:rmul(L,(1,),inv(L)),2:rmul(M,(2,),inv(M)),3:rmul(M,(3,),inv(M)),4:(4,)}
 assert ops['v0']==g0
 new_to_old={1:(1,),2:(2,3,-2),3:(4,),4:(-4,2,4)}
 old_to_new={1:(1,),2:(3,4,-3),3:(3,-4,-3,2,3,4,-3),4:(3,)}
 for i in range(1,5):
  assert sub(new_to_old[i],old_to_new)==sub(old_to_new[i],new_to_old)==(i,)
  desired=rmul((1,2,3),(i,),(-3,-2,-1)) if i<=3 else (4,)
  assert sub(new_to_old[i],ops['v1'])==sub(desired,new_to_old)
 for row in rows[:2]:
  for field in ['geometric_push','geometric_pullback']:
   action={int(k):tuple(v) for k,v in row[field].items()}
   for i in range(1,5):assert sub(action[i],delta)==delta[i]
 normalforms={'gamma0':{'L':L,'M':M,'images':g0},
              'gamma1':{'new_to_old':new_to_old,'old_to_new':old_to_new,'new_K':[1,2,3],
                        'rule':'conjugate first three new basis elements by new_K; fix fourth'},
              'both_actions_and_inverses_induce_identity_after_q_filling':True}
 out={'scope':__doc__,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'copied_crossing_engine_sha256':hashlib.sha256((DE/'w_pencil_braid.py').read_bytes()).hexdigest(),
  'static_conversion_sha256':hashlib.sha256((DE/'old_lassos_far_cut_conversion.json').read_bytes()).hexdigest(),
  'base_v':[str(S.re(base)),str(S.im(base))],'projection':['1','371/1000'],
  'far_q_projected_point':['10','0'],'q_labels':['0','1','v','v^2'],'initial_order':initial,
  'four_cut_basis_in_old_six_cut_basis':[1,4,5,6],
  'old_named_lassos_to_four_cut_basis':old_to_four,
  'old_to_q_retained_filling':{1:[1],2:[2],3:[],4:[],5:[],6:[]},
  'four_cut_to_q_retained_filling':{1:[],2:[1],3:[],4:[2]},
  'filled_local_relator_four_cut':r,'filled_local_relator_old_named':[6,2,-6,-2],
  'compact_operator_normalforms':normalforms,'loops':rows,'segment_count':len(cache),'elapsed_seconds':time.monotonic()-started,
  'actual_kernel_formula':'ker(F4 -> pi1(X0)) is the F4-normal closure of the orbit of [x3,x4] under the two actual retained v-base operators and their inverses.',
  'claims_excluded':['unfilled section noninjectivity','full G-column stabilizer','global kappa','I=R']}
 (P/'retained_section_kernel_braids.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS all three actual four-strand lassos, actions, inverse maps and literal old-base filling; elapsed',round(out['elapsed_seconds'],3),flush=True)

if __name__=='__main__':run()
