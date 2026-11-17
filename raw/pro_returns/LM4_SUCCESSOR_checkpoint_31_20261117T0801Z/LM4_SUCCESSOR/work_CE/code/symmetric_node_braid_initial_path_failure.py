#!/usr/bin/env python3
"""Certified based nodal braids for the actual symmetric deletion family.

There are21 finite punctures plus infinity. The far regular Artin basepoint
is not identified silently with the fixed source. Rational cyclotomic
deformation is controlled by DE's independent critical-value certificate.
No full Fox matrix, source equality, or fixed-lifting conclusion is asserted.
"""
from pathlib import Path
import sys,itertools,json,time,hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
DE=ROOT/'work_DE'/'next_marginal_source'
sys.path.insert(0,str(DE))
import sympy as S
from quadratic_pencil_braid import (F,I,Q,X,ROT,u,EPS,frac,sy,red,invert,
    ppoly,parts,pval,pneg,complex_sqrt,roots,lower_norm,peval,
    ppoly_from_record,Segment as OldSegment)

OUT=HERE.parent/'next_symmetric_nodes'
OUT.mkdir(exist_ok=True)
NSTR=21
LABELS=[{'kind':'retained','name':s} for s in ('0','1','q')]
LABELS += [{'kind':'A','branch':'v','index':i} for i in range(1,5)]
LABELS += [{'kind':'A','branch':'w','index':i} for i in range(1,5)]
LABELS += [{'kind':'B','branch':'v','index':i} for i in range(1,5)]
LABELS += [{'kind':'B','branch':'w','index':i} for i in range(1,5)]
LABELS += [{'kind':'retained','name':s} for s in ('sqrt_plus','sqrt_minus')]
assert len(LABELS)==NSTR

def l1(z):return abs(S.re(z))+abs(S.im(z))
def dist2_segment(c,a,b):
 d=b-a;dd=S.re(d)**2+S.im(d)**2
 assert dd>0
 z=c-a;t=(S.re(z)*S.re(d)+S.im(z)*S.im(d))/dd
 t=max(S.Integer(0),min(S.Integer(1),t));w=z-t*d
 return S.cancel(S.re(w)**2+S.im(w)**2)

class Segment(OldSegment):
 def __init__(self,a,b):
  self.a,self.b=a,b;q=S.expand(a+(b-a)*X)
  self.t=q
  assert l1(a)<6 and l1(b)<6
  # Möbius coefficients (n1,n0,d1,d0), without clearing constants into
  # huge integers: denominator norms then retain literal metric meaning.
  self.mobius=[(0,0,0,1),(0,1,0,1),(1,0,0,1)]
  self.mobius += [(0,v,0,1) for v in u[1:]]
  self.mobius += [(1,0,0,v) for v in u[1:]]
  self.mobius += [(-1,v,0,v-1) for v in u[1:]]
  self.mobius += [(1-v,0,1,-v) for v in u[1:]]
  self.rational=[]
  for n1,n0,d1,d0 in self.mobius:
   num=S.expand(ROT*(n1*q+n0));den=S.expand(d1*q+d0)
   dr,di=parts(den);lower_norm(dr,di,F(1,10**6))
   R,J=parts(S.expand(num*S.conjugate(den)))
   D=ppoly(S.expand(den*S.conjugate(den)))
   assert D.eval(0)>0 and D.eval(1)>0
   self.rational.append((R,J,D))
   # |d ROT(n1 q+n0)/(d1 q+d0)/dX| < 10^16 follows
   # from this exact numerator bound and |den|>10^-6.
   deriv=ROT*(n1*d0-n0*d1)*(b-a)
   assert l1(deriv)<10**4
  assert len(self.rational)==19
  A,B=parts(ROT*ROT*q);self.U=[(A,B)]
  lower_norm(A,B,F(1,10**8))
  assert B.eval(0)!=0 and B.eval(1)!=0
  axis=[]
  for lo,hi,m in roots(B):
   ar=peval(A,(lo,hi));assert ar[0]>0 or ar[1]<0
   if ar[1]<0 and m%2:axis.append((lo,hi))
  self.axis=[axis];self.derivative_bound=F(10**16)
  self.records=[];self.candidates=[]

 def point(self,label,x):
  if label<19:
   R,J,D=self.rational[label];d=pval(D,x);assert d>0
   a,b=pval(R,x)/d,pval(J,x)/d
   return (a,a),(b,b)
  sign=1 if label==19 else -1
  for lo,hi in self.axis[0]:
   assert not lo<=x<=hi
   if hi<x:sign=-sign
  A,B=self.U[0];re,im=complex_sqrt(pval(A,x),pval(B,x))
  return (re,im) if sign>0 else (pneg(re),pneg(im))

 def order(self,x):
  vals=[self.point(i,x)[0] for i in range(NSTR)]
  out=sorted(range(NSTR),key=lambda i:vals[i][0])
  for i,j in zip(out,out[1:]):assert vals[i][1]<vals[j][0],('projection tie',x,i,j)
  return out

 def compute(self):
  for i,j in itertools.combinations(range(19),2):
   R,_,D=self.rational[i];T,_,E=self.rational[j]
   self.addpoly('rational',[i,j],R*E-T*D)
  A,B=self.U[0]
  self.addpoly('quadratic_self',[0],B)
  for i,(h,_,d) in enumerate(self.rational):
   self.addpoly('quadratic_rational',[0,i],4*h*h*(h*h-A*d*d)-B*B*d**4)
  self.candidates.sort(key=lambda e:e['lo']);groups=[]
  for e in self.candidates:
   if groups and e['lo']<=groups[-1]['hi']:
    groups[-1]['hi']=max(groups[-1]['hi'],e['hi']);groups[-1]['events'].append(e)
   else:groups.append({'lo':e['lo'],'hi':e['hi'],'events':[e]})
  for g in groups:
   for e,f in itertools.combinations(g['events'],2):
    assert e['record']!=f['record']
    p=ppoly_from_record(self.records[e['record']]);q=ppoly_from_record(self.records[f['record']])
    gg=S.gcd(p,q)
    assert gg.degree()>0 and gg.count_roots(sy(g['lo']),sy(g['hi']))>0
  initial=self.order(F(0));at=list(initial);word=[];events=[]
  for gi,g in enumerate(groups):
   left=F(0) if gi==0 else groups[gi-1]['hi']
   right=F(1) if gi+1==len(groups) else groups[gi+1]['lo']
   before=(left+g['lo'])/2;after=(g['hi']+right)/2
   ob=self.order(before);oa=self.order(after);assert at==ob
   positions={a:i for i,a in enumerate(oa)}
   pairs=[(a,b) for i,a in enumerate(ob) for b in ob[i+1:] if positions[a]>positions[b]]
   if not pairs:continue
   sample=g['lo']-max(g['hi']-g['lo'],frac(EPS))
   assert left<sample<g['lo']
   rad=self.derivative_bound*(g['hi']-sample)
   clusters=[]
   for a,b in pairs:
    touching=[c for c in clusters if a in c or b in c];merged={a,b}
    for c in touching:merged.update(c);clusters.remove(c)
    clusters.append(merged)
   for c in clusters:
    for a,b in itertools.combinations(sorted(c),2):
     ai=self.point(a,sample)[1];bi=self.point(b,sample)[1]
     gap=(ai[0]-bi[1]-2*rad,ai[1]-bi[0]+2*rad)
     assert gap[0]>0 or gap[1]<0,('unresolved cluster heights',a,b)
   crossings=[];remaining=len(pairs)
   while at!=oa:
    j=next(j for j in range(len(at)-1) if positions[at[j]]>positions[at[j+1]])
    a,b=at[j],at[j+1]
    ai=self.point(a,sample)[1];bi=self.point(b,sample)[1]
    gap=(ai[0]-bi[1]-2*rad,ai[1]-bi[0]+2*rad)
    assert gap[0]>0 or gap[1]<0,('unresolved crossing height',a,b)
    sign=-1 if gap[0]>0 else 1
    word.append(sign*(j+1));at[j],at[j+1]=at[j+1],at[j]
    crossings.append({'labels':[a,b],'generator':sign*(j+1),'imaginary_difference_bounds':[str(z) for z in gap]})
    remaining-=1
   assert remaining==0
   events.append({'interval':[str(g['lo']),str(g['hi'])],
    'candidate_records':[e['record'] for e in g['events']],
    'crossings':crossings,'cluster_sizes':[len(c) for c in clusters]})
  final=self.order(F(1));assert at==final
  return {'start':[str(S.re(self.a)),str(S.im(self.a))],
    'end':[str(S.re(self.b)),str(S.im(self.b))],
    'initial_order':initial,'final_order':final,'word':red(word),
    'crossing_count':len(word),'polynomials':self.records,'actual_events':events,
    'literal_mobius_denominator_lower_bound':'1/10^6',
    'uniform_derivative_bound':'10^16','interval_root_precision':str(EPS)}

def rmul(*ws):return tuple(red(itertools.chain.from_iterable(ws)))
def rinv(w):return tuple(-x for x in w[::-1])
def sub(w,A):return rmul(*(A[x] if x>0 else rinv(A[-x]) for x in w))
def art(w):
 A={i:(i,) for i in range(1,NSTR+1)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(rmul(a,b,rinv(a)),a) if x>0 else (b,rmul(rinv(b),a,b))
 return A
def comm(a,b):return rmul(a,b,rinv(a),rinv(b))
def peel(w):
 c=[];w=list(w)
 while len(w)>1 and w[0]==-w[-1]:c.append(w.pop(0));w.pop()
 assert len(w)==1 and w[0]>0,('not a positive meridian',w)
 return c,w[0]

def plan():
 deformation=json.loads((DE/'symmetric_critical_deformation.json').read_text())
 geometry=json.loads((DE/'symmetric_deletion_geometry.json').read_text())
 centers=[]
 for d in deformation['centers']:
  v=Q(d['center'][0])+I*Q(d['center'][1]);centers.append((d,v))
 geom={tuple(r['q']):r['pairs'] for r in geometry['critical_value_clusters']}
 mixed=[dict(d,center_complex=c,pairs=geom[tuple(d['key'])]) for d,c in centers if d['kind']=='mixed']
 base=Q(1,100);h=Q(1,10000);chosen=None;failures=[]
 for hh in (Q(13,1000),Q(17,1000),Q(19,1000),Q(23,1000),Q(29,1000)):
  hub=base+I*hh;bad=[];allsegments=[(base,hub,'trunk')]
  for i,d in enumerate(mixed):
   c=d['center_complex'];corners=[c+h+I*h,c-h+I*h,c-h-I*h,c+h-I*h,c+h+I*h]
   allsegments.extend((a,b,str(i)) for a,b in zip([hub]+corners,corners))
  margins=[]
  for a,b,name in allsegments:
   for d,c in centers:
    dd=dist2_segment(c,a,b)
    limit=Q(1,5000)**2 if d['kind']=='old' else h*h/Q(4)
    if dd<=limit:bad.append((name,d.get('name',d.get('key')),str(dd)))
    margins.append(dd)
  if not bad:chosen=(hub,min(margins));break
  failures.append({'hub_imaginary':str(hh),'failures':bad})
 assert chosen,('no certified common whisker hub',failures)
 hub,margin=chosen
 return base,hub,h,mixed,{'base':['1/100','0'],
  'hub':[str(S.re(hub)),str(S.im(hub))],'square_halfside':str(h),
  'minimum_all_center_distance_squared':str(margin),
  'old_pole_margin_strictly_greater_than':'1/5000',
  'rejected_hub_records':failures,
  'deformation_certificate_sha256':hashlib.sha256((DE/'symmetric_critical_deformation.json').read_bytes()).hexdigest(),
  'geometry_certificate_sha256':hashlib.sha256((DE/'symmetric_deletion_geometry.json').read_bytes()).hexdigest()}

def run(indices):
 base,hub,h,mixed,planned=plan();started=time.monotonic()
 (OUT/'symmetric_node_path_plan.json').write_text(json.dumps(planned,indent=2)+'\n')
 print('PATH PLAN PASS; hub',planned['hub'],'old-pole margin >1/5000',flush=True)
 cache={}
 def segment(a,b):
  key=(a,b)
  if key not in cache:
   rec=Segment(a,b).compute();cache[key]=rec
   print('segment',len(cache),'crossings',rec['crossing_count'],'elapsed',round(time.monotonic()-started,3),flush=True)
  return cache[key]
 trunk=segment(base,hub);initial=trunk['initial_order'];rows=[]
 print('INITIAL PHYSICAL LABEL ORDER',initial,flush=True)
 for idx in indices:
  d=mixed[idx];c=d['center_complex'];corners=[c+h+I*h,c-h+I*h,c-h-I*h,c+h-I*h,c+h+I*h]
  records=[segment(a,b) for a,b in zip([hub]+corners,corners)]
  whisker=rmul(trunk['word'],records[0]['word'])
  local=rmul(*(r['word'] for r in records[1:]))
  beta=rmul(whisker,local,rinv(whisker))
  expected=2*len(d['pairs']);assert sum(1 if x>0 else -1 for x in beta)==expected
  perm=list(initial);link={}
  for x in beta:
   j=abs(x)-1;a,b=perm[j],perm[j+1];k=tuple(sorted((a,b)))
   link[k]=link.get(k,0)+(1 if x>0 else -1)
   perm[j],perm[j+1]=perm[j+1],perm[j]
  assert perm==initial,('not pure',idx)
  expected_pairs=[]
  for aa,bb in d['pairs']:
   ai=(3 if aa[0]=='v' else 7)+aa[1]-1
   bi=(11 if bb[0]=='v' else 15)+bb[1]-1
   expected_pairs.append(tuple(sorted((ai,bi))))
  actual_link={k:v for k,v in link.items() if v}
  assert actual_link=={k:2 for k in expected_pairs},('wrong node-linking matrix',idx,actual_link,expected_pairs)
  # Absorb an initial local prefix if projection crossings place the
  # disjoint local node blocks in a different corner marking.
  found=None
  for cut in range(len(local)+1):
   pref=local[:cut];rotated=rmul(local[cut:],pref);A=art(rotated)
   support=[i for i in A if A[i]!=(i,)]
   if len(support)!=2*len(expected_pairs):continue
   blocks=[support[i:i+2] for i in range(0,len(support),2)]
   if any(b[1]!=b[0]+1 for b in blocks):continue
   std=tuple(x for b in blocks for x in (b[0],b[0]))
   if A==art(std):found=(pref,blocks,std);break
  assert found,('no disjoint full-twist local normal form',idx,local)
  pref,blocks,std=found;W=rmul(whisker,pref);A=art(W);Ai=art(rinv(W))
  for i in range(1,NSTR+1):assert sub(A[i],Ai)==(i,)==sub(Ai[i],A)
  assert art(beta)==art(rmul(W,std,rinv(W)))
  nodes=[]
  for j,k in blocks:
   ca,ga=peel(A[j]);cb,gb=peel(A[k]);la,lb=initial[ga-1],initial[gb-1]
   assert tuple(sorted((la,lb))) in expected_pairs
   nodes.append({'local_positions':[j,k],'physical_labels':[la,lb],
    'meridians':[A[j],A[k]],'conjugators':[ca,cb],
    'cores':[ga,gb],'commutator':comm(A[j],A[k])})
  row={'index':idx,'key':d['key'],'center':[str(S.re(c)),str(S.im(c))],
   'expected_node_pairs':d['pairs'],'expected_exponent':expected,'word':beta,
   'forward_segments':records,'local_word':local,'absorbed_prefix':pref,
   'standard_local_braid':std,'whisker':W,'nodes':nodes,
   'pair_linking_twice':[{'labels':list(k),'crossing_sum':v} for k,v in sorted(actual_link.items())]}
  rows.append(row)
  out={'scope':__doc__,'path_plan':planned,'labels':LABELS,'initial_order':initial,
   'common_trunk':trunk,'loops':rows,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
   'basepoint_scope':'Far regular Artin basepoint; actual fixed-source comparison remains separate.',
   'elapsed_seconds':round(time.monotonic()-started,6)}
  (OUT/'symmetric_node_braids.partial.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
  print('LOOP',idx,'PASS; nodes',len(nodes),'braid length',len(beta),'exponent',expected,'prefix',len(pref),flush=True)
 (OUT/'symmetric_node_braids.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 compact={k:v for k,v in out.items() if k not in ('common_trunk','loops')}
 compact['common_trunk_word']=trunk['word']
 compact['loops']=[{k:v for k,v in r.items() if k!='forward_segments'} for r in rows]
 (OUT/'symmetric_node_words.json').write_text(json.dumps(compact,indent=2)+'\n')
 print('PASS requested actual nodal lassos:',indices,'elapsed',round(time.monotonic()-started,3),flush=True)

if __name__=='__main__':
 run(list(range(18)) if '--all' in sys.argv else [int(x) for x in sys.argv[1:]] or [0])
