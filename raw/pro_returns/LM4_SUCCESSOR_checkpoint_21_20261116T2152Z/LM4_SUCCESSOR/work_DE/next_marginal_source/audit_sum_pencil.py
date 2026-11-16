"""Exact cyclotomic critical-value, collision and discriminant audit."""
from pathlib import Path
from fractions import Fraction as F
import itertools,json
import sympy as S
HERE=Path(__file__).resolve().parent
X,T,Z=S.symbols('X T Z');cyclo=X**4+X**3+X**2+X+1
def el(p):
 p=S.rem(S.Poly(p,X,domain=S.QQ),S.Poly(cyclo,X,domain=S.QQ)).as_expr()
 return tuple(F(p.coeff(X,j)) for j in range(4))
def pol(a):return sum(S.Rational(x.numerator,x.denominator)*X**j for j,x in enumerate(a))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):return el(pol(a)*pol(b))
def scale(q,a):return tuple(F(q)*x for x in a)
zero=el(0);one=el(1);U=[el(X**j) for j in range(5)]
def val(p,a):
 out=zero
 for c in S.Poly(p,T).all_coeffs():out=add(mul(out,a),el(c))
 return out
def order(p,a):
 if not S.expand(p):return None
 for k in range(S.degree(p,T)+1):
  if val(p,a)!=zero:return k
  p=S.diff(p,T)
 raise AssertionError('nonzero polynomial vanished to excessive order')
rows=[('zero',zero,21,6)]
rows +=[(f'positive_{j}',u,19,13) for j,u in enumerate(U)]
rows +=[(f'negative_{j}',neg(u),21,3) for j,u in enumerate(U)]
rows +=[(f'half_{j}',scale(F(1,2),u),21,4) for j,u in enumerate(U)]
rows +=[(f'pair_{j}_{k}',scale(F(1,2),add(U[j],U[k])),19,12) for j in range(5) for k in range(j+1,5)]
assert len(rows)==26 and len({r[1] for r in rows})==26
rational=[-S.Integer(1),2*T-1,T-1]+[pol(u)-1 for u in U]+[2*T-1-pol(u) for u in U]
RR=[S.expand(a-b) for a,b in itertools.combinations(rational,2)]
RQ=[S.expand(r*r-2*(T-1)*r+pol(q)-(2*T-1)) for q in U for r in rational]
QD=[T*T-pol(q) for q in U]
# Completeness: every nonconstant collision polynomial's complete degree
# is accounted for, with multiplicity, at the26 displayed field values.
for p in RR+RQ+QD:
 assert p!=0
 degree=S.degree(p,T)
 assert sum(order(p,a) for _,a,_,_ in rows)==degree
data=[]
for name,a,expected_count,expected_exp in rows:
 rv=set(val(r,a) for r in rational);count=len(rv);quadratics=[]
 for q in U:
  discr=add(mul(a,a),neg(q));number=1 if discr==zero else 2
  hits=[r for r in rv if add(add(mul(r,r),scale(-2,mul(add(a,neg(one)),r))),add(q,neg(add(scale(2,a),neg(one)))))==zero]
  assert len(hits)<=number
  count+=number-len(hits)
  quadratics.append({'q':list(map(str,q)),'distinct_roots':number,'rational_hits':len(hits)})
 exponent=2*sum(order(p,a) for p in RR)+2*sum(order(p,a) for p in RQ)+sum(order(p,a) for p in QD)
 assert count==expected_count and exponent==expected_exp,(name,count,exponent)
 data.append({'name':name,'critical_value':list(map(str,a)),'distinct_fiber_punctures':count,
              'loss':23-count,'braid_exponent':exponent,'quadratic_data':quadratics})
 print(name,'punctures',count,'loss',23-count,'exponent',exponent)
assert sum(r['loss'] for r in data)==82
(HERE/'sum_pencil_critical_audit.json').write_text(json.dumps({'field':'Q[X]/Phi5(X)','generic_punctures':23,
 'critical_values':data,'loss_sum':82,'Euler_characteristic':1-23+82,
 'scope':'Complete algebraic collision audit; no special-fiber source-kernel surjectivity inferred.'},indent=2)+'\n')
print('PASS: all26 critical values, no omitted finite collision, all local exponents, total loss82 and Euler60.')
