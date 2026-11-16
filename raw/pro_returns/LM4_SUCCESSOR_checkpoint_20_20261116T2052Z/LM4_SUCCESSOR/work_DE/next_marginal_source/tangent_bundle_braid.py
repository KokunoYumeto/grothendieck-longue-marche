"""Exact eight-strand based monodromy for the unordered tangent-parabola model.

Seven actual fiber punctures plus the stationary source point T=1.
The ten lassos consist of six old base holes and four source crossings.
No source-kernel normality is inferred from the local types or output.
"""
from pathlib import Path
import json,itertools,time
import sympy as S
from quadratic_pencil_braid import (F,I,Q,X,ROT,u,EPS,frac,sy,red,invert,ppoly,parts,pval,padd,pneg,complex_sqrt,roots,lower_norm,peval,ppoly_from_record,Segment as OldSegment)
HERE=Path(__file__).resolve().parent

class Segment(OldSegment):
 def __init__(self,a,b,parameter_bound=5):
  self.a,self.b=a,b;self.t=S.expand(a+(b-a)*X);q=self.t
  rr=[S.cancel((q+v*v)/(2*v)) for v in u]+[S.Integer(1)]
  self.rational=[parts(ROT*z) for z in rr];self.raw_rational=rr
  self.center=parts(S.Integer(0));self.U=[];self.axis=[]
  A,B=parts(ROT*ROT*q);self.U.append((A,B));lower_norm(A,B,F(1,10**8))
  assert B.eval(0)!=0 and B.eval(1)!=0
  axis=[]
  for lo,hi,m in roots(B):
   ar=peval(A,(lo,hi));assert ar[0]>0 or ar[1]<0
   if ar[1]<0 and m%2:axis.append((lo,hi))
  self.axis.append(axis)
  self.parameter_bound=parameter_bound
  assert abs(S.re(a))+abs(S.im(a))<parameter_bound and abs(S.re(b))+abs(S.im(b))<parameter_bound
  self.derivative_bound=F(10**8)
  derivative=sum(abs(frac(c)) for c in A.diff().all_coeffs())+sum(abs(frac(c)) for c in B.diff().all_coeffs())
  assert derivative*5000<self.derivative_bound
  for r,s in itertools.combinations(rr,2):
   R,J=parts(r-s);lower_norm(R,J,F(1,10**12))
  for r in rr:
   R,J=parts(r*r-q);lower_norm(R,J,F(1,10**12))
  self.records=[];self.candidates=[]

 def point(self,label,x):
  if label<6:
   R,J=self.rational[label];a,b=pval(R,x),pval(J,x)
   return (a,a),(b,b)
  sign=1 if label==6 else -1
  for lo,hi in self.axis[0]:
   assert not lo<=x<=hi
   if hi<x:sign=-sign
  A,B=self.U[0];re,im=complex_sqrt(pval(A,x),pval(B,x))
  return (re,im) if sign>0 else (pneg(re),pneg(im))

 def order(self,x):
  vals=[self.point(i,x)[0] for i in range(8)]
  order=sorted(range(8),key=lambda i:vals[i][0])
  for i,j in zip(order,order[1:]):assert vals[i][1]<vals[j][0]
  return order
 def compute(self):
  for i,j in itertools.combinations(range(6),2):self.addpoly('rational',[i,j],self.rational[i][0]-self.rational[j][0])
  for k,(A,B) in enumerate(self.U):
   self.addpoly('quadratic_self',[k],B)
   for i in range(6):
    h=self.rational[i][0]-self.center[0]
    self.addpoly('quadratic_rational',[k,i],4*h*h*(h*h-A)-B*B)
  for i,j in itertools.combinations(range(1),2):
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
   assert len({a for p in pairs for a in p})==2*len(pairs),'non-generic simultaneous crossing'
   # Evaluate immediately before the event, outside the square-root cut
   # intervals, then enclose the full crossing interval by the derivative
   # bound.  Midpoint evaluation would straddle a principal-root cut at
   # exactly the self-crossings whose analytic branches remain regular.
   sample=g['lo']-max(g['hi']-g['lo'],frac(EPS))
   assert left<sample<g['lo']
   rad=self.derivative_bound*(g['hi']-sample)
   crossings=[]
   for a,b in sorted(pairs,key=lambda ab:at.index(ab[0])):
    j=at.index(a);assert at[j+1]==b
    ai=self.point(a,sample)[1];bi=self.point(b,sample)[1]
    difference=(ai[0]-bi[1]-2*rad,ai[1]-bi[0]+2*rad)
    assert difference[0]>0 or difference[1]<0,'uncertified crossing height'
    sign=-1 if difference[0]>0 else 1
    word.append(sign*(j+1));at[j],at[j+1]=at[j+1],at[j]
    crossings.append({'labels':[a,b],'generator':sign*(j+1),'imaginary_difference_bounds':[str(x) for x in difference]})
   assert at==oa
   events.append({'interval':[str(g['lo']),str(g['hi'])],'candidate_records':[e['record'] for e in g['events']],
                  'crossings':crossings})
  final=self.order(F(1));assert at==final
  return {'start':[str(S.re(self.a)),str(S.im(self.a))],'end':[str(S.re(self.b)),str(S.im(self.b))],
          'initial_order':initial,'final_order':final,'word':red(word),'crossing_count':len(word),
          'polynomials':self.records,'actual_events':events,
          'uniform_rational_difference_lower_bound':'1/10^12',
          'uniform_quadratic_residual_lower_bound':'1/10^12',
          'uniform_projected_square_norm_lower_bound':'1/10^8','derivative_bound':'100000000',
          **({'parameter_L1_bound':str(self.parameter_bound)} if self.parameter_bound!=5 else {})}

def run():
 base=Q(1,100);h=Q(1,1000)
 centers=[('old_zero',S.Integer(0))]+[('old_root_'+str(k),S.cancel(v*v)) for k,v in enumerate(u)]+[('cross_'+str(k),S.cancel(2*v-v*v)) for k,v in enumerate(u) if k]
 results=[];cache={};started=time.monotonic()
 initial=Segment(base,base+Q(1,10**7)*I).order(F(0));assert initial[-1]==5
 print('Initial order, source last:',initial,flush=True)
 for name,c in centers:
  corners=[c+h+h*I,c-h+h*I,c-h-h*I,c+h-h*I,c+h+h*I]
  path=[base]+corners;forward=[];records=[]
  for a,b in zip(path,path[1:]):
   key=(a,b)
   if key not in cache:
    rec=Segment(a,b).compute();cache[key]=rec
    print('segment',len(cache),'crossings',rec['crossing_count'],'elapsed',round(time.monotonic()-started,2),flush=True)
   rec=cache[key];records.append(rec);forward+=rec['word']
  word=red(forward+invert(records[0]['word']))
  perm=list(range(8))
  for x in word:perm[abs(x)-1],perm[abs(x)]=perm[abs(x)],perm[abs(x)-1]
  assert perm[7]==7
  if name!='old_zero':assert perm==list(range(8)),(name,perm)
  else:assert sum(a!=b for a,b in enumerate(perm))==2
  row={'name':name,'center':[str(S.re(c)),str(S.im(c))],'word':word,'permutation':perm,'forward_segments':records}
  results.append(row)
  print('loop',name,'length',len(word),'exponent',sum(1 if a>0 else -1 for a in word),flush=True)
 out={'description':__doc__,'base':['1/100','0'],'source_point':['1','0'],'rotation':['1','371/1000'],'coefficient_points':[[str(S.re(v)),str(S.im(v))] for v in u],'initial_order':initial,'loops':results,'segment_count':len(cache)}
 (HERE/'tangent_bundle_braids.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 (HERE/'tangent_bundle_words.json').write_text(json.dumps({k:v for k,v in out.items() if k!='loops'}|{'loops':[{k:v for k,v in r.items() if k!='forward_segments'} for r in results]},indent=2)+'\n')
 print('PASS ten exact tangent-bundle lassos; seconds',round(time.monotonic()-started,3),flush=True)

if __name__=='__main__':run()
