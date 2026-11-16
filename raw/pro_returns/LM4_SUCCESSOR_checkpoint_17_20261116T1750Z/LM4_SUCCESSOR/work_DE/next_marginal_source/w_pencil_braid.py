"""Exact source-preserving polynomial w-pencil transport for the missing normalizer gate."""
from pathlib import Path
import itertools,json,time
import sympy as S
from sum_pencil_braid import (F,I,Q,X,ROT,u,EPS,frac,sy,red,invert,parts,pval,roots,lower_norm,ppoly_from_record,Segment as SumSegment)
HERE=Path(__file__).resolve().parent

class Segment(SumSegment):
 def __init__(self,a,b,parameter_bound=6):
  self.a,self.b=a,b;w=S.expand(a+(b-a)*X);self.t=w
  rr=[S.Integer(0)]+[S.expand(w*v) for v in u]+[S.expand(w*w)]+list(u)+[S.expand(w*(2-w))]
  assert len(rr)==13
  self.raw_rational=rr;self.rational=[parts(ROT*z) for z in rr]
  self.U=[];self.axis=[];self.center=parts(S.Integer(0))
  self.parameter_bound=parameter_bound
  assert abs(S.re(a))+abs(S.im(a))<parameter_bound and abs(S.re(b))+abs(S.im(b))<parameter_bound
  self.derivative_bound=F(10**8)
  for R,J in self.rational:
   assert sum(abs(frac(c)) for P in [R.diff(),J.diff()] for c in P.all_coeffs())<10**6
  for r,t in itertools.combinations(rr,2):
   R,J=parts(r-t);lower_norm(R,J,F(1,10**12))
  self.records=[];self.candidates=[]
 def point(self,label,x):
  R,J=self.rational[label];a,b=pval(R,x),pval(J,x)
  return (a,a),(b,b)
 def order(self,x):
  values=[self.point(i,x)[0] for i in range(13)]
  ans=sorted(range(13),key=lambda i:values[i][0])
  for i,j in zip(ans,ans[1:]):assert values[i][1]<values[j][0],('projection tie',x,i,j)
  return ans
 def compute(self):
  for i,j in itertools.combinations(range(13),2):self.addpoly('rational',[i,j],self.rational[i][0]-self.rational[j][0])
  for k,(A,B) in enumerate(self.U):
   self.addpoly('quadratic_self',[k],B)
   for i in range(13):
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

def approx_complex(z):
 a=S.N(S.re(z),80);b=S.N(S.im(z),80);scale=10**30
 return Q(int(S.floor(a*scale+Q(1,2))),scale)+I*Q(int(S.floor(b*scale+Q(1,2))),scale)

def make_centers():
 cs=[('base_zero',S.Integer(0),58,'old')]
 cs += [(f'base_positive_{j}',v,22 if j==0 else 14,'old') for j,v in enumerate(u)]
 cs += [(f'filled_negative_{j}',-v,2,'filled') for j,v in enumerate(u)]
 cs += [('source_zero_v',S.Integer(2),2,'source')]
 cs += [(f'source_constant_{j}',2-v,2,'source_constant') for j,v in enumerate(u) if j]
 for j,v in enumerate(u):
  if not j:continue
  r=approx_complex(S.sqrt(1-v))
  cs += [(f'source_product_{j}_plus',1+r,2,'source_product'),(f'source_product_{j}_minus',1-r,2,'source_product')]
 assert len(cs)==24
 return cs

def run():
 base=Q(1,200);hub=base+Q(1,100)*I;h=Q(1,10000);cs=make_centers()
 for a,c,_,_ in cs:assert S.re(c-base)**2+S.im(c-base)**2>Q(1,10**8)
 for (a,c,_,_),(b,d,_,_) in itertools.combinations(cs,2):
  assert S.re(c-d)**2+S.im(c-d)**2>100*h*h,(a,b)
  x=c+h+h*I-hub;y=d+h+h*I-hub
  assert S.re(x)*S.im(y)-S.im(x)*S.re(y)!=0,(a,b,'collinear rays')
 for name,c,_,_ in cs:
  d=c+h+h*I-hub;dd=S.re(d)**2+S.im(d)**2
  for other,o,_,_ in cs:
   if name==other:continue
   v=o-hub;t=max(0,min(1,(S.re(v)*S.re(d)+S.im(v)*S.im(d))/dd));z=v-t*d
   assert S.re(z)**2+S.im(z)**2>3*h*h,(name,other,'whisker disk')
 started=time.monotonic();common=Segment(base,hub).compute();initial=common['initial_order'];source_pos=initial.index(12)
 print('Initial order',initial,'source position',source_pos+1,flush=True)
 print('Common source trunk',len(common['word']),'crossings',flush=True)
 cache={};rows=[]
 for name,c,exponent,kind in cs:
  corners=[c+h+h*I,c-h+h*I,c-h-h*I,c+h-h*I,c+h+h*I]
  path=[hub]+corners;forward=[];records=[]
  for a,b in zip(path,path[1:]):
   key=(a,b)
   if key not in cache:
    rec=Segment(a,b).compute();cache[key]=rec
    print('segment',len(cache),'crossings',rec['crossing_count'],'elapsed',round(time.monotonic()-started,2),flush=True)
   rec=cache[key];records.append(rec);forward+=rec['word']
  beta=red(common['word']+forward+invert(records[0]['word'])+invert(common['word']))
  assert sum(1 if x>0 else -1 for x in beta)==exponent,(name,'exponent',sum(1 if x>0 else -1 for x in beta),exponent)
  perm=list(range(13))
  for x in beta:perm[abs(x)-1],perm[abs(x)]=perm[abs(x)],perm[abs(x)-1]
  assert perm==list(range(13)),(name,'not pure')
  row={'name':name,'kind':kind,'center':[str(S.re(c)),str(S.im(c))],'expected_exponent':exponent,'word':beta,'permutation':perm,'forward_segments':records}
  rows.append(row)
  (HERE/'w_pencil_braids.partial.json').write_text(json.dumps({'common_trunk':common,'initial_order':initial,'source_position':source_pos,'loops':rows},separators=(',',':'))+'\n')
  print('loop',name,'length',len(beta),'exponent',exponent,flush=True)
 out={'description':__doc__,'base':['1/200','0'],'hub':['1/200','1/100'],'critical_square_halfside':'1/10000','projection':['1','371/1000'],'coefficient_points':[[str(S.re(v)),str(S.im(v))] for v in u],'initial_order':initial,'source_position':source_pos,'common_trunk':common,'loops':rows,'segment_count':1+len(cache),'source':'z=w(2-w)','scope':'Actual based transport data; full partial-source normality remains unresolved.'}
 (HERE/'w_pencil_braids.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 (HERE/'w_pencil_words.json').write_text(json.dumps({k:v for k,v in out.items() if k not in ['loops','common_trunk']}|{'common_trunk_word':common['word'],'loops':[{k:v for k,v in r.items() if k!='forward_segments'} for r in rows]},indent=2)+'\n')
 print('PASS all24 source-preserving w lassos; seconds',round(time.monotonic()-started,3),flush=True)

if __name__=='__main__':run()
