#!/usr/bin/env python3
"""Exact q_b to rational first-neck bridge for the already marked reflection."""
from pathlib import Path
from fractions import Fraction as F
import sympy as S,json,time,hashlib
H=Path(__file__).resolve().parent
D=json.loads((H/'annular_neck_reflection23.json').read_text());X=S.symbols('x',real=True);I=S.I
Q=lambda x:S.Rational(str(x))
U=[Q(z[0])+I*Q(z[1]) for z in D['unit_rational_u']]
q=Q('4/5')+I*(Q('1/2')+X/10);rot=1+I*Q('371/1000')
points=[S.Integer(0),q]+[S.cancel(((u*u+(1-2*u)*q)/(q+u*u-2*u))**2) for u in U]
def polys(z):
 n,d=S.fraction(S.cancel(z));num=S.expand(n*S.conjugate(d));den=S.expand(d*S.conjugate(d))
 return [S.Poly(S.re(num),X,domain=S.QQ),S.Poly(S.im(num),X,domain=S.QQ),S.Poly(den,X,domain=S.QQ)]
projected=[polys(rot*z) for z in points]
for R,J,E in projected:
 assert E.eval(0)>0 and E.eval(1)>0 and E.count_roots(0,1)==0
orders=[]
for t in(0,1):
 vals=[R.eval(t)/E.eval(t) for R,J,E in projected]
 order=sorted(range(6),key=lambda i:vals[i]);orders.append(order)
 assert min(vals[b]-vals[a] for a,b in zip(order,order[1:]))>Q('1/1000')
assert orders==[[2,0,5,3,4,1],[2,5,0,3,4,1]]
rows=[];events=[];start=time.monotonic()
for i in range(6):
 for j in range(i+1,6):
  # Cancel before taking real parts: much smaller exact norm polynomials.
  R,J,E=polys(rot*(points[i]-points[j]))
  iso=R.intervals(eps=Q('1e-45'))
  hits=[]
  for (lo,hi),m in iso:
   if hi<=0 or lo>=1:continue
   assert 0<lo<=hi<1 and m==1
   assert J.count_roots(lo,hi)==0
   sign=1 if J.eval((lo+hi)/2)>0 else -1
   hits.append({'box':[str(lo),str(hi)],'imag_sign_i_minus_j':sign})
  if hits:events.append({'pair':[i,j],'roots':hits})
  # Exact polynomial positivity proves uniform physical separation1/1000.
  R0,J0,E0=polys(points[i]-points[j])
  B=R0*R0+J0*J0-Q('1e-6')*E0*E0
  assert B.eval(0)>0 and B.eval(1)>0 and B.count_roots(0,1)==0,(i,j,'separation')
  rows.append({'pair':[i,j],'real_difference_degree':R.degree(),'projection_root_count':len(hits),
   'distance_lower_bound':'1/1000','norm_margin_degree':B.degree(),
   'norm_margin_coefficients':list(map(str,B.all_coeffs()))})
assert len(events)==1 and events[0]['pair']==[0,5]
assert events[0]['roots'][0]['imag_sign_i_minus_j']==-1
# Cone is initially left, ordinary h4 passes above to its left: +sigma2.
word=[2]
def inv(w):return tuple(-z for z in reversed(w))
def red(w):
 o=[]
 for z in w:
  if o and o[-1]==-z:o.pop()
  else:o.append(z)
 return tuple(o)
def sub(w,A):return red(z for v in w for z in(A[v] if v>0 else inv(A[-v])))
push={j:(j,) for j in range(1,7)};push[2]=(2,3,-2);push[3]=(2,)
back={j:(j,) for j in range(1,7)};back[2]=(3,);back[3]=(-3,2,3)
assert all(sub(push[j],back)==(j,) and sub(back[j],push)==(j,)for j in range(1,7))
assert [push[j]for j in [1,3,4,5,6]]==[(j,)for j in[1,2,4,5,6]]
out={'status':'PASS','q_start':['4/5','1/2'],'q_end':['4/5','3/5'],
 'orders':orders,'chronological_word':word,'positive_push':push,'back_transport':back,
 'ordinary_marking':'(x1,x3,x4,x5,x6) maps literally to endpoint cuts(1,2,4,5,6)',
 'events':events,'all15_pair_certificates':rows,
 'deformation':'Exact-unit u are Cayley rational approximations to true fifth roots; straight coefficient homotopy changes every y by<1e-26. Uniform distance>1/1000 and endpoint projection gaps>1/1000 preserve the based braid and cut marking.',
 'reflection_input_sha256':hashlib.sha256((H/'annular_neck_reflection23.json').read_bytes()).hexdigest(),
 'elapsed_seconds':time.monotonic()-start}
(H/'annular_neck_bridge23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all15 exact pair-separation inequalities and endpoint gaps')
print('PASS unique chronological crossing +sigma2; twelve inverse maps')
print('PASS the entire original ordinary K basis transports literally to the endpoint ordinary order')
print('Elapsed',time.monotonic()-start)
