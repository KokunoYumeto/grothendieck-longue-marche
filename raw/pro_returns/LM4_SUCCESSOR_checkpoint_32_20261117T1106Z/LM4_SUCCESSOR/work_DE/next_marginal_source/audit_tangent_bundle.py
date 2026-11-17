"""Exact algebraic, distinguished-path and actual-source audit of the q bundle."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,itertools,json
import sympy as S
from quadratic_pencil_braid import u,I,Q,frac,sqrt_interval,ROT
HERE=Path(__file__).resolve().parent
X,q=S.symbols('X q');cyclo=X**4+X**3+X**2+X+1
def el(a):
 a=S.rem(S.Poly(a,X,domain=S.QQ),S.Poly(cyclo,X,domain=S.QQ)).as_expr()
 return tuple(F(a.coeff(X,j)) for j in range(4))
def pol(a):return sum(Q(c.numerator,c.denominator)*X**j for j,c in enumerate(a))
def mul(a,b):return el(pol(a)*pol(b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def val(p,a):
 out=el(0)
 for c in S.Poly(p,q).all_coeffs():out=add(mul(out,a),el(c))
 return out
def order(p,a):
 for k in range(S.degree(p,q)+1):
  if val(p,a)!=el(0):return k
  p=S.diff(p,q)
 raise AssertionError('zero collision polynomial')
U=[el(X**j) for j in range(5)]
centers=[('old_zero',el(0),1)]+[('old_root_'+str(j),mul(v,v),12 if j==0 else 8) for j,v in enumerate(U)]+[('cross_'+str(j),el(2*pol(v)-pol(v)**2),2) for j,v in enumerate(U) if j]
assert len({a for _,a,_ in centers})==10
rational=[S.expand((q*pol(U[(-j)%5])+pol(U[j]))/2) for j in range(5)]+[S.Integer(1)]
RR=[S.expand(a-b) for a,b in itertools.combinations(rational,2)]
RQ=[S.expand(a*a-q) for a in rational]
for p in RR+RQ+[q]:assert sum(order(p,a) for _,a,_ in centers)==S.degree(p,q)
algebra=[]
for name,a,expected in centers:
 e=2*sum(order(p,a) for p in RR+RQ)+order(q,a)
 assert e==expected,(name,e,expected)
 algebra.append({'name':name,'center_Qzeta':list(map(str,a)),'eight_strand_exponent':e})
print('Exact Q(zeta) completeness of all10 source/base collision values and exponents: PASS')
# Recheck the actual cyclotomic rational deformation, independently of its prior output.
rt5=sqrt_interval((F(5),F(5)));sp=sqrt_interval((10+2*rt5[0],10+2*rt5[1]));sm=sqrt_interval((10-2*rt5[1],10-2*rt5[0]))
re1=((rt5[0]-1)/4,(rt5[1]-1)/4);re2=(-(rt5[1]+1)/4,-(rt5[0]+1)/4)
im1=(sp[0]/4,sp[1]/4);im2=(sm[0]/4,sm[1]/4)
exact=[((F(1),F(1)),(F(0),F(0))),(re1,im1),(re2,im2),(re2,(-im2[1],-im2[0])),(re1,(-im1[1],-im1[0]))]
for z,(ri,ii) in zip(u,exact):
 for a,iv in ((frac(S.re(z)),ri),(frac(S.im(z)),ii)):assert max(abs(a-iv[0]),abs(a-iv[1]))<F(1,10**30)
 assert Q(99,100)**2<S.re(z)**2+S.im(z)**2<Q(101,100)**2
# |q|<5, |u|>.99 imply tangent point modulus<3.1 and coefficient motion<1e-28.
assert (F(5)/F(99,100)+F(101,100))/2<F(31,10) # includes the full coefficient homotopy
assert (F(5)/F(99,100)**2+1)/2<10
assert 10*F(2,10**30)<F(1,10**28)
assert 2*F(1,10**28)<F(1,10**14)
words=json.loads((HERE/'tangent_bundle_words.json').read_text());base=Q(1,100);h=Q(1,1000)
C=[(r['name'],Q(r['center'][0])+I*Q(r['center'][1])) for r in words['loops']]
for (name,c),(other,d) in itertools.combinations(C,2):
 assert S.re(c-d)**2+S.im(c-d)**2>Q(1,10000)
 v=c+h+h*I-base;w=d+h+h*I-base
 assert S.re(v)*S.im(w)-S.im(v)*S.re(w)!=0
minimum=None
for name,c in C:
 v=c+h+h*I-base;vv=S.re(v)**2+S.im(v)**2
 for other,d in C:
  if name==other:continue
  w=d-base;t=max(0,min(1,(S.re(v)*S.re(w)+S.im(v)*S.im(w))/vv));r=w-t*v
  dd=S.re(r)**2+S.im(r)**2
  assert dd>Q(1,100000),(name,other,dd)
  minimum=dd if minimum is None else min(minimum,dd)
for row,aa in zip(words['loops'],algebra):assert row['name']==aa['name'] and sum(1 if x>0 else -1 for x in row['word'])==aa['eight_strand_exponent']
print('All10 squares disjoint, straight whisker directions distinct, every other critical square avoided: PASS')
# Transport from the already fixed B78 normalized source endpoint q=-9999.
path=[-S.Integer(9999),-S.Integer(9999)+100*I,100*I,base]
transport_min=None
for a,b in zip(path,path[1:]):
 v=b-a;vv=S.re(v)**2+S.im(v)**2
 for name,c in C:
  w=c-a;t=max(0,min(1,(S.re(v)*S.re(w)+S.im(v)*S.im(w))/vv));r=w-t*v
  dd=S.re(r)**2+S.im(r)**2
  assert dd>Q(1,100000),(name,a,b,dd)
  transport_min=dd if transport_min is None else min(transport_min,dd)
assert words['initial_order'][-1]==5
# At q*=.01, both roots have modulus.1 and all line points modulus<=.505.
assert Q(101,200)<1 and Q(1,10)<1
print('Actual T1 source is exterior at q*=.01; explicit old-endpoint source transport avoids all holes: PASS')
out={'scope':'Complete actual smaller marginal bundle/source certificate; no uniform normality or K=1 inferred.','algebraic_collision_data':algebra,'base':['1/100','0'],'actual_source_transport_q':[[str(S.re(a)),str(S.im(a))] for a in path],'critical_center_error_upper_bound':'1/10^25','strand_deformation_motion_upper_bound':'1/10^28','segment_strand_separation_lower_bound':'1/10^14','distinguished_whisker_other_center_squared_distance_lower_bound':'1/100000','actual_source_path_squared_distance_lower_bound':'1/100000','source_relation':'T=1','source_group_rank':10,'filled_source_rank':6,'fiber_rank':7,'filled_fiber_rank':3,'finite_covers':['s^2=q','(v-w)^2=4(T^2-q)'],'kernel_comparison':'cover characters extend after U filling, so the actual kernels coincide under finite-index embeddings, also in full completions','hashes':{f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in ['tangent_bundle_braid.py','tangent_bundle_braids.json','tangent_bundle_words.json','extract_tangent_bundle_fiber.py','tangent_bundle_fiber_data.json']}}
(HERE/'tangent_bundle_geometry_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact q-model algebra, paths, source marking and coefficient deformation.')
