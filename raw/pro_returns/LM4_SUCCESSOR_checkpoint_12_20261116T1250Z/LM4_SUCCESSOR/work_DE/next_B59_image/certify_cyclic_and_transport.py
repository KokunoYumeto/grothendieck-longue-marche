"""Exact common marking, cyclic monodromy, and transport certificates.

Algebraic equality is verified in the degree-eight field Q(i,sqrt5,
sqrt((5+sqrt5)/2)). Rational interval arithmetic proves the actual and
rationally approximated base paths stay in one crossing-free cell.
A uniform rational distance estimate certifies the homotopy of the
entire cyclic family from exact roots of unity to rational constants.
All braid crossings of the rational family and both transports are
then certified by the same exact Sturm engine used for B56.
"""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,time
import sympy as s
import braid_engine as E
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
start=time.time()

class R:
 def __init__(self,lo,hi=None):
  self.lo=F(lo);self.hi=F(lo if hi is None else hi);assert self.lo<=self.hi
 def __add__(self,o):
  o=o if isinstance(o,R) else R(o);return R(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return R(-self.hi,-self.lo)
 def __sub__(self,o):return self+-rr(o)
 def __rsub__(self,o):return rr(o)+-self
 def __mul__(self,o):
  o=rr(o);v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)];return R(min(v),max(v))
 __rmul__=__mul__
 def inv(self):
  assert self.lo*self.hi>0
  return R(min(1/self.lo,1/self.hi),max(1/self.lo,1/self.hi))
 def __truediv__(self,o):return self*rr(o).inv()
 def sq(self):
  return R(0 if self.lo<=0<=self.hi else min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))
 def hull(self,o):o=rr(o);return R(min(self.lo,o.lo),max(self.hi,o.hi))
 def enc(self):return [str(self.lo),str(self.hi)]
def rr(x):return x if isinstance(x,R) else R(x)
class C:
 def __init__(self,re=0,im=0):self.re=rr(re);self.im=rr(im)
 def __add__(self,o):o=cc(o);return C(self.re+o.re,self.im+o.im)
 __radd__=__add__
 def __neg__(self):return C(-self.re,-self.im)
 def __sub__(self,o):return self+-cc(o)
 def __rsub__(self,o):return cc(o)+-self
 def __mul__(self,o):o=cc(o);return C(self.re*o.re-self.im*o.im,self.re*o.im+self.im*o.re)
 __rmul__=__mul__
 def inv(self):
  d=self.re.sq()+self.im.sq();assert d.lo>0
  return C(self.re/d,-self.im/d)
 def __truediv__(self,o):return self*cc(o).inv()
 def __rtruediv__(self,o):return cc(o)*self.inv()
 def __pow__(self,n):
  assert n>=0;v=C(1)
  for _ in range(n):v=v*self
  return v
 def hull(self,o):o=cc(o);return C(self.re.hull(o.re),self.im.hull(o.im))
 def enc(self):return [self.re.enc(),self.im.enc()]
def cc(x):return x if isinstance(x,C) else C(x)
def sym(z):return s.Rational(z.re.lo.numerator,z.re.lo.denominator)+s.I*s.Rational(z.im.lo.numerator,z.im.lo.denominator)
def exactc(z):
 z=s.expand(z)
 return C(F(str(s.re(z))),F(str(s.im(z))))

# Exact shared configuration and actual labelled action.
K=s.QQ.algebraic_field(s.I,s.sqrt(5),s.sqrt((5+s.sqrt(5))/2))
assert K.mod.degree()==8
one=K.one;j=K.from_sympy(s.I);ph=K.from_sympy((1+s.sqrt(5))/2)
rho=K.from_sympy(s.sqrt((5+s.sqrt(5))/2));u0=j*(ph+rho)
eta=(K.from_sympy(s.sqrt(5))-one)/4+j*rho/2;v0=-ph**2
assert eta**5==one and eta!=one
X=[2,6,12,9,4];Y=[5,7,11,10,8]
def orbit(u,J=1j):
 return [u,-u,1/u,(u+J)/(u-J),-1/u,-(u+J)/(u-J),
 (u-J)/(u+J),-(u-J)/(u+J),(u+1)/(-J*u+J),
 (u+1)/(J*u-J),(u-1)/(J*u+J),(u-1)/(-J*u-J)]
# ANP does not coerce Python integers through division, so use field constants.
zz=[u0,-u0,one/u0,(u0+j)/(u0-j),-one/u0,-(u0+j)/(u0-j),
 (u0-j)/(u0+j),-(u0-j)/(u0+j),(u0+one)/(-j*u0+j),
 (u0+one)/(j*u0-j),(u0-one)/(j*u0+j),(u0-one)/(-j*u0-j)]
q={1:K.zero};q.update({p:eta**i for i,p in enumerate(X)});q.update({p:v0*eta**i for i,p in enumerate(Y)})
fac=(eta-one)/(eta-eta**4)
for label in range(1,13):
 if label==2:continue
 zt=(zz[label-1]-zz[3])/(zz[label-1]-zz[1])*(zz[5]-zz[1])/(zz[5]-zz[3])
 zc=fac if label==3 else (q[label]-eta**4)/(q[label]-one)*fac
 assert zt==zc,label
print('PASS exact common icosahedral configuration and labelled Dcycles in degree8 field',flush=True)

# Rational enclosures of the two positive radicals.
r5=R('2.236067977499','2.236067977500')
assert r5.lo**2<5<r5.hi**2
rh=R('1.90211303258','1.90211303260')
assert rh.lo**2<(5+r5.lo)/2 and rh.hi**2>(5+r5.hi)/2
phi=(1+r5)/2;ET=C((r5-1)/4,rh/2);V0=-(phi*phi)
U0=C(0,phi+rh)
roots=[C(1),C('0.30901699','0.95105652'),C('-0.80901699','0.58778525'),
       C('-0.80901699','-0.58778525'),C('0.30901699','-0.95105652')]
error=F(1,10**7)
for i,a in enumerate(roots):
 d=(ET**i)-a
 assert max(abs(d.re.lo),abs(d.re.hi))+max(abs(d.im.lo),abs(d.im.hi))<error
for i,j in itertools.combinations(range(5),2):
 gap=ET**i-ET**j
 assert (gap.re.sq()+gap.im.sq()).lo>1
u1=s.I*s.Rational(352014702,10**8);v1=-s.Rational(261803399,10**8)
rotation=C(1,F(317,1000))
U=U0.hull(exactc(u1));zt=orbit(U,C(0,1))
normT={lab:(zt[lab-1]-zt[3])/(zt[lab-1]-zt[1])*(zt[5]-zt[1])/(zt[5]-zt[3])
       for lab in range(1,13) if lab!=2}
RH=[(ET**i).hull(roots[i]) for i in range(5)]
VH=C(V0).hull(exactc(v1))
qq={1:C(0)};qq.update({p:RH[i] for i,p in enumerate(X)});qq.update({p:VH*RH[i] for i,p in enumerate(Y)})
FAC=(RH[1]-1)/(RH[1]-RH[4])
normC={lab:FAC if lab==3 else (qq[lab]-RH[4])/(qq[lab]-1)*FAC for lab in range(1,13) if lab!=2}
def interval_order(vals):
 re={lab:(rotation*z).re for lab,z in vals.items()}
 order=sorted(re,key=lambda lab:re[lab].lo+re[lab].hi)
 assert all(re[a].hi<re[b].lo for a,b in zip(order,order[1:])),[(lab,re[lab].enc()) for lab in order]
 return order,re
orderT,reT=interval_order(normT);orderC,reC=interval_order(normC)
assert orderT==orderC
ico_order=orderT
print('PASS both algebraic-to-rational base homotopies stay in the same crossing-free cell',ico_order,flush=True)

# Exact T transport from the previous common meridian base to near u0.
old=json.loads((HERE/'full11_braid_words.json').read_text())
tbase=s.Rational(371,100)+s.I*s.Rational(237,100)
tword,trecord=E.segment(tbase,u1)
print('PASS exact Ttransport, crossings',len(tword),flush=True)

# Cyclic rational approximating family, still normalized labels2,4,6.
v=E.u;rrs=[sym(z) for z in roots]
qs={1:s.Integer(0)};qs.update({p:rrs[i] for i,p in enumerate(X)});qs.update({p:v*rrs[i] for i,p in enumerate(Y)})
factor=s.cancel((rrs[1]-1)/(rrs[1]-rrs[4]))
functions={lab:factor if lab==3 else s.cancel((qs[lab]-rrs[4])/(qs[lab]-1)*factor)
           for lab in range(1,13) if lab!=2}
finite_labels=old['finite_labels']
E.fun=[functions[lab] for lab in finite_labels]
E.exceptional=s.Integer(1);E.cache={}
cbase=tbase;epsilon=s.Rational(1,100)
centres=[s.Integer(0)]+rrs
def xy(z):return s.re(z),s.im(z)
def box(c):x,y=xy(c);return (x-epsilon,x+epsilon,y-epsilon,y+epsilon)
def hit(a,b,rect):
 lo=s.Integer(0);hi=s.Integer(1)
 for x,dx,mn,mx in [(s.re(a),s.re(b-a),rect[0],rect[1]),(s.im(a),s.im(b-a),rect[2],rect[3])]:
  if dx==0:
   if not mn<=x<=mx:return None
  else:
   l=(mn-x)/dx;h=(mx-x)/dx
   if l>h:l,h=h,l
   lo=max(lo,l);hi=min(hi,h)
   if lo>hi:return None
 return lo,hi
rects=[box(c) for c in centres]
slopes=[];paths=[]
for i,c in enumerate(centres):
 corner=c+epsilon*(1+s.I)
 assert hit(cbase,corner,rects[i])==(1,1)
 slopes.append(s.im(corner-cbase)/s.re(corner-cbase))
 for j,rect in enumerate(rects):
  if j!=i:assert hit(cbase,corner,rect) is None,('stem meets another petal',i,j)
 for j in range(i):
  a,b=rects[i],rects[j]
  assert a[1]<b[0] or b[1]<a[0] or a[3]<b[2] or b[3]<a[2]
 paths.append([cbase,c+epsilon*(1+s.I),c+epsilon*(-1+s.I),c-epsilon*(1+s.I),c+epsilon*(1-s.I),c+epsilon*(1+s.I),cbase])
assert len(set(slopes))==6
segments=[(v1,cbase)]+[(a,b) for path in paths for a,b in zip(path,path[1:])]
def distance_sq(a,b,c):
 d=b-a;den=s.re(d*s.conjugate(d));assert den>0
 t=s.re((c-a)*s.conjugate(d))/den;t=max(0,min(1,t))
 z=s.expand(a+t*d-c);return s.re(z)**2+s.im(z)**2
minimum=min(distance_sq(a,b,c) for a,b in segments for c in centres)
assert minimum>s.Rational(1,1000)**2
assert minimum==s.Rational(1,10000)
assert all(abs(s.re(z))+abs(s.im(z))<7 for path in paths for z in path)
assert abs(v1)<7
# Actual root distance exceeds0.001-error, perturbation <=error*(1+|v|).
assert F(1,1000)-error>8*error
print('PASS six-meridian tree and entire root-approximation homotopy; minimum squared centre distance',minimum,flush=True)

cword,crecord=E.segment(v1,cbase)
print('PASS exact cyclic transport, crossings',len(cword),flush=True)
def point_order(parameter):
 vals=[s.re(s.cancel(E.rotation*f.subs(v,parameter))) for f in E.fun]
 assert len(set(vals))==11
 return [finite_labels[i] for i in sorted(range(11),key=lambda i:vals[i])]
assert point_order(v1)==ico_order
c_order=point_order(cbase)
records=[]
for i,path in enumerate(paths):
 word=[];segs=[]
 for a,b in zip(path,path[1:]):
  w,rec=E.segment(a,b);word+=w;segs.append(rec)
 word=E.red(word)
 records.append({'index':i,'centre':E.point_json(centres[i]),'path':[E.point_json(z) for z in path],'word':word,'segments':segs})
 print('PASS cyclic meridian',i,'braid length',len(word),'elapsed',round(time.time()-start,2),flush=True)

pairdata=json.loads((BASE/'full_pair_linking_certificate.json').read_text())
pairs=[tuple(p) for p in pairdata['pair_rows']];pi={p:i for i,p in enumerate(pairs)}
ambient=json.loads((BASE/'ambient_rigid7_abelian_certificate.json').read_text())
ap=[tuple(p) for p in ambient['ambient_pair_basis']]
cyclic=json.loads((HERE/'cyclic_bracket_span.json').read_text())
def links(word,initial):
 labels=initial[:];counts=[0]*55
 for a in word:
  k=abs(a)-1;counts[pi[tuple(sorted((labels[k],labels[k+1])))]]+=1 if a>0 else -1
  labels[k],labels[k+1]=labels[k+1],labels[k]
 assert labels==initial and all(x%2==0 for x in counts)
 return [x//2 for x in counts]
for rec in records:
 l=links(rec['word'],c_order)
 expected=dict(zip(ap,cyclic['meridian_ambient_H1_columns'][rec['index']]))
 expected[(4,6)]=0
 assert l==[expected[p] for p in pairs]
 rec['pair_linking']=l
T={row['index']:E.mul(E.inv(tword),row['word'],tword) for row in old['basis']}
C5={rec['index']:E.mul(cword,rec['word'],E.inv(cword)) for rec in records}
for row in old['basis']:
 assert links(T[row['index']],ico_order)==[r[row['index']-1] for r in pairdata['full_matrix_rows_pairs_columns_basis']]
for rec in records:assert links(C5[rec['index']],ico_order)==rec['pair_linking']
print('PASS all transported words pure at the same exact marking and all pair-linking checks',flush=True)
cert={'description':__doc__,'exact_configuration':{'u0':'i*(phi+sqrt(phi+2))','eta':'(sqrt5-1)/4+i*sqrt(phi+2)/2','v0':'-phi^2','field_degree':8},
 'sqrt5_interval':r5.enc(),'rho_interval':rh.enc(),'root_error_bound':str(error),
 'root_approximations':[E.point_json(z) for z in rrs],
 'common_order_labels':ico_order,'T_base_cell_intervals':{str(k):v.enc() for k,v in reT.items()},
 'cyclic_base_cell_intervals':{str(k):v.enc() for k,v in reC.items()},
 'minimum_squared_path_to_centre':str(minimum),'uniform_parameter_bound':7,
 'T_transport':trecord,'cyclic_transport':crecord,'cyclic_meridians':records,
 'completed':True}
(HERE/'cyclic_and_transport_exact_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
(HERE/'common_base_braid_words.json').write_text(json.dumps({'initial_order_labels':ico_order,
 'T':{str(k):v for k,v in T.items()},'C5':{str(k):v for k,v in C5.items()}},indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed',round(time.time()-start,2),'seconds',flush=True)
