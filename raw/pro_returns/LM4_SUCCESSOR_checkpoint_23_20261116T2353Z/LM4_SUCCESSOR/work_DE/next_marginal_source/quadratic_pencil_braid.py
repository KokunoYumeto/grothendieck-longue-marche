"""Exact crossing engine for the twenty-point polynomial ratio pencil.

All crossing candidates are roots of rational polynomials of degree<=6.
Rational nested-square-root bounds certify order and crossing heights.
The rational cyclotomic deformation and actual common marking are audited
separately; no source-kernel normality is inferred from the braid words.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt,ceil
import itertools,json,time
import sympy as S

HERE=Path(__file__).resolve().parent
X=S.Symbol('X',real=True);I=S.I;Q=S.Rational
ROT=1+Q(371,1000)*I
u=[S.Integer(1),
 (S.Integer(309016994374947424102293417183)+S.Integer(951056516295153572116439333379)*I)/10**30,
 (-S.Integer(809016994374947424102293417183)+S.Integer(587785252292473129168705954639)*I)/10**30,
 (-S.Integer(809016994374947424102293417183)-S.Integer(587785252292473129168705954639)*I)/10**30,
 (S.Integer(309016994374947424102293417183)-S.Integer(951056516295153572116439333379)*I)/10**30]
EPS=Q(1,10**65);SQRT_DIGITS=90

def frac(x):return F(int(S.numer(x)),int(S.denom(x)))
def sy(x):return Q(x.numerator,x.denominator) if isinstance(x,F) else S.sympify(x)
def red(w):
 r=[]
 for x in w:
  if r and r[-1]==-x:r.pop()
  else:r.append(int(x))
 return r
def invert(w):return [-x for x in w[::-1]]
def ppoly(x):return S.Poly(S.expand(x),X,domain=S.QQ)
def parts(x):
 x=S.expand(x);return ppoly(S.re(x)),ppoly(S.im(x))
def pval(p,x):return frac(p.eval(sy(x)))
def padd(a,b):return (a[0]+b[0],a[1]+b[1])
def pneg(a):return (-a[1],-a[0])
def pmul(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)
def peval(p,interval):
 out=(F(0),F(0))
 for c in p.all_coeffs():out=padd(pmul(out,interval),(frac(c),frac(c)))
 return out
def sqrt_interval(a):
 lo,hi=a;assert lo>=0
 m=10**SQRT_DIGITS
 l=isqrt(lo.numerator*m*m//lo.denominator)
 h=isqrt(hi.numerator*m*m//hi.denominator)+1
 return F(l,m),F(h,m)
def complex_sqrt(A,B):
 radius=sqrt_interval((A*A+B*B,A*A+B*B))
 rr=((radius[0]+A)/2,(radius[1]+A)/2)
 ii=((radius[0]-A)/2,(radius[1]-A)/2)
 rr=(max(F(0),rr[0]),max(F(0),rr[1]))
 ii=(max(F(0),ii[0]),max(F(0),ii[1]))
 re=sqrt_interval(rr);im=sqrt_interval(ii)
 if B<0:im=pneg(im)
 return re,im
def normalize(p):
 if not p:return p
 return p.clear_denoms()[1].primitive()[1]
def roots(p):
 p=normalize(p)
 assert p,'identically zero candidate polynomial'
 out=[]
 for (a,b),m in p.intervals(eps=EPS):
  if b<=0 or a>=1:continue
  assert a>0 and b<1,'root isolation unresolved at a segment endpoint'
  out.append((frac(a),frac(b),int(m)))
 return out
def positive_on_unit(p):
 assert p.eval(0)>0 and p.eval(1)>0
 assert p.count_roots(0,1)==0
def lower_norm(re,im,bound):
 positive_on_unit(re*re+im*im-ppoly(sy(bound)**2))

class Segment:
 def __init__(self,a,b,parameter_bound=5):
  self.a,self.b=a,b;self.t=S.expand(a+(b-a)*X)
  t=self.t
  # Labels0..3 are retained rational punctures;4..11 are the eight U
  # branches, with constant/moving pairs;12..19 are quadratic branches.
  rr=[S.Integer(0),-S.Integer(1),1-t,-t]
  for v in u[1:]:rr += [v-1,(v-1)*(t-1)]
  self.rational=[parts(ROT*z) for z in rr]
  self.raw_rational=rr
  self.center=parts(-ROT*t/2)
  self.U=[];self.axis=[]
  for q in u[1:]:
   D=S.expand(t*t-4*(t-1)*(1-q))
   A,B=parts(ROT*ROT*D/4);self.U.append((A,B))
   lower_norm(A,B,F(1,10**8))
   assert B.eval(0)!=0 and B.eval(1)!=0
   axis=[]
   if B:
    for lo,hi,m in roots(B):
     ar=peval(A,(lo,hi));assert ar[0]>0 or ar[1]<0
     if ar[1]<0 and m%2:axis.append((lo,hi))
   self.axis.append(axis)
  # Bounds for the geometric rational deformation and interval heights.
  self.parameter_bound=parameter_bound
  assert abs(S.re(a))+abs(S.im(a))<parameter_bound and abs(S.re(b))+abs(S.im(b))<parameter_bound
  self.derivative_bound=F(10**8)
  for A,B in self.U:
   derivative=sum(abs(frac(c)) for c in A.diff().all_coeffs())+sum(abs(frac(c)) for c in B.diff().all_coeffs())
   centerderivative=sum(abs(frac(c)) for p in self.center for c in p.diff().all_coeffs())
   assert centerderivative+derivative*5000<self.derivative_bound
  for p,q in itertools.combinations(rr,2):
   R,J=parts(p-q);lower_norm(R,J,F(1,10**12))
  for q in u[1:]:
   for r in rr:
    R,J=parts(r*r+t*r+(t-1)*(1-q));lower_norm(R,J,F(1,10**12))
  R,J=parts(t-1);lower_norm(R,J,F(1,10**8))
  self.records=[];self.candidates=[]

 def point(self,label,x):
  if label<12:
   R,J=self.rational[label];a,b=pval(R,x),pval(J,x)
   return (a,a),(b,b)
  k=(label-12)//2;sign=1 if (label-12)%2==0 else -1
  for lo,hi in self.axis[k]:
   assert not lo<=x<=hi,'sample meets an unresolved square-root branch interval'
   if hi<x:sign=-sign
  A,B=self.U[k];re,im=complex_sqrt(pval(A,x),pval(B,x))
  if sign<0:re,im=pneg(re),pneg(im)
  cr,ci=(pval(p,x) for p in self.center)
  return padd(re,(cr,cr)),padd(im,(ci,ci))

 def order(self,x):
  values=[self.point(i,x)[0] for i in range(20)]
  order=sorted(range(20),key=lambda i:values[i][0])
  for i,j in zip(order,order[1:]):assert values[i][1]<values[j][0],('projection tie at sample',x,i,j)
  return order

 def addpoly(self,kind,indices,p):
  p=normalize(p)
  if p.degree()<=0:return
  rr=roots(p);rid=len(self.records)
  self.records.append({'kind':kind,'indices':indices,'coefficients':[str(c) for c in p.all_coeffs()],
                       'intervals':[[str(lo),str(hi),m] for lo,hi,m in rr]})
  for lo,hi,m in rr:self.candidates.append({'lo':lo,'hi':hi,'record':rid,'multiplicity':m})

 def compute(self):
  for i,j in itertools.combinations(range(12),2):self.addpoly('rational',[i,j],self.rational[i][0]-self.rational[j][0])
  for k,(A,B) in enumerate(self.U):
   self.addpoly('quadratic_self',[k],B)
   for i in range(12):
    h=self.rational[i][0]-self.center[0]
    self.addpoly('quadratic_rational',[k,i],4*h*h*(h*h-A)-B*B)
  for i,j in itertools.combinations(range(4),2):
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

def ppoly_from_record(r):return S.Poly.from_list([S.Rational(c) for c in r['coefficients']],gens=X)

def run(names=('base1','base2')):
 base=Q(1,100)*I;h=Q(1,1000)
 centers={'base1':S.Integer(1),'base2':S.Integer(2)}
 for k,q in enumerate(u[1:],1):centers['b_triple_'+str(k)]=1-q
 results=[];cache={};started=time.monotonic()
 for name in names:
  c=centers[name];corners=[c+h+h*I,c-h+h*I,c-h-h*I,c+h-h*I,c+h+h*I]
  path=[base]+corners;forward=[];records=[]
  for a,b in zip(path,path[1:]):
   key=(a,b)
   if key not in cache:
    rec=Segment(a,b).compute();cache[key]=rec
    print('segment',len(cache),'crossings',rec['crossing_count'],'elapsed',round(time.monotonic()-started,2),flush=True)
   rec=cache[key];records.append(rec);forward+=rec['word']
  word=red(forward+invert(records[0]['word']))
  perm=list(range(20))
  for x in word:perm[abs(x)-1],perm[abs(x)]=perm[abs(x)],perm[abs(x)-1]
  assert perm==list(range(20)),('loop not pure',name,perm)
  row={'name':name,'center':[str(S.re(c)),str(S.im(c))],'word':word,'forward_segments':records}
  results.append(row)
  (HERE/'ratio_pencil_braids.partial.json').write_text(json.dumps({'base':['0','1/100'],'rotation':['1','371/1000'],'loops':results},separators=(',',':'))+'\n')
  print('loop',name,'length',len(word),'elapsed',round(time.monotonic()-started,2),flush=True)
 out={'description':__doc__,'base':['0','1/100'],'rotation':['1','371/1000'],
      'coefficient_points':[[str(S.re(q)),str(S.im(q))] for q in u],
      'initial_order':Segment(base,base+Q(1,10**7)).order(F(0)),
      'loops':results,'segment_count':len(cache)}
 (HERE/'ratio_pencil_braids.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 (HERE/'ratio_pencil_words.json').write_text(json.dumps({k:v for k,v in out.items() if k!='loops'}|{'loops':[{k:v for k,v in r.items() if k!='forward_segments'} for r in results]},indent=2)+'\n')
 print('PASS: exact twenty-strand braid words for',names,flush=True)

if __name__=='__main__':
 import sys
 run(tuple(sys.argv[1:]) or ('base1','base2'))
