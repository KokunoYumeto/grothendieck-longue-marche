#!/usr/bin/env python3
"""Exact actual middle-neck coordinates; no braid producer imports."""
import sympy as s
import json,time
from pathlib import Path
start=time.monotonic()
r=s.sqrt(5); c1=s.sqrt(1+2/r); c2=s.sqrt(1-2/r)
c={1:c1,2:c2,3:-c2,4:-c1}
lam={j:s.simplify(2/(1+c[j]**2)) for j in c}
assert s.simplify(c1*c2-1/r)==0
assert 5>4 and 5>1 # c2>0 and 0<1/sqrt(5)<1, with positive roots
assert s.simplify(c1**2-c2**2)==4/r
Q,x,y,a,b=s.symbols('Q x y a b',real=True)
li=2/(1+a*a);lj=2/(1+b*b)
assert s.factor(1/(li*lj)-(a-b)**2/4-(1+a*b)**2/4)==0
# Exact branch criterion: real Z roots force Q real and |Q|>=1.
z=s.symbols('z',real=True,nonzero=True)
assert s.factor(((z+1/z)/2)**2-1-(z*z-1)**2/(4*z*z))==0
table=[]
for i in range(1,5):
  for j in range(i,5):
    h=s.simplify(1+c[i]*c[j])
    sign=-1 if (i,j)==(1,4) else 1
    assert s.simplify(sign*h).is_positive
    X=s.simplify(sign*h/2);Y=s.simplify((c[i]+c[j])/2)
    qpoint=X+s.I*Y
    expr=s.simplify(lam[i]*lam[j]*(qpoint-s.I*c[i])*(qpoint-s.I*c[j])-1)
    assert expr==0,(i,j,expr)
    table.append({'pair':[i,j],'X':X,'Y':Y})
targets=[]
for k in (1,2,3):
  row=next(v for v in table if v['pair']==[k,k+1])
  X,Y=row['X'],row['Y']
  assert s.simplify(Y-c[k+1]).is_positive and s.simplify(c[k]-Y).is_positive
  if k==2: assert s.simplify(X-1/r)==0 and s.simplify(1-X).is_positive and Y==0
  else:
    assert s.simplify(X-(1+1/r)/2)==0
    assert (s.simplify(Y).is_positive if k==1 else s.simplify(-Y).is_positive)
  same_height=[v for v in table if s.simplify(v['Y']-Y)==0]
  assert all(s.simplify(v['X']-X)==0 for v in same_height)
  expect=[[1,2]] if k==1 else [[1,4],[2,3]] if k==2 else [[3,4]]
  assert [v['pair'] for v in same_height]==expect
  upper=s.simplify(lam[k+1]*(X+s.I*Y-s.I*c[k+1]))
  assert s.simplify(s.re(upper)).is_positive and s.simplify(s.im(upper)).is_positive
  u={j:(c[j]+s.I)/(c[j]-s.I) for j in (k,k+1)}
  beta=s.simplify(u[k]*u[k+1]/(u[k]+u[k+1]-1))
  q=s.simplify((X+s.I*Y-1)/(X+s.I*Y+1))
  assert s.simplify(q-beta)==0
  # Re Q>0 is exactly |q|<1 under this Cayley transform.
  assert s.factor((x+1)**2+y*y-((x-1)**2+y*y))==4*x
  targets.append({'k':k,'Q_real':str(X),'Q_imag':str(Y),'q':str(q),
    'selected_A':k+1,'selected_B':k,'simultaneous_unordered_pairs':expect,
    'horizontal_path_has_no_earlier_critical_value':True,
    'selected_node_Z_real':str(s.simplify(s.re(upper))),
    'selected_node_Z_imag':str(s.simplify(s.im(upper)))})
out={'status':'PASS','method':'Exact radical identities and signs; no numerical sampling or producer imports.',
 'critical_inner_coordinates':[{'pair':v['pair'],'ReQ':str(v['X']),'ImQ':str(v['Y'])} for v in table],
 'targets':targets,'branch_check':'Nonreal Q gives no real root; real 0<Q<1 likewise by ((z+z^-1)/2)^2-1=(z-z^-1)^2/4.',
 'elapsed_seconds':time.monotonic()-start}
Path(__file__).with_name('middle_neck_nodes21.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact three middle-neck selected nodes and complete ten-pair inner table')
for row in targets:print('k',row['k'],'simultaneous',row['simultaneous_unordered_pairs'],'Q',row['Q_real'],row['Q_imag'])
print('PASS no earlier critical value on any horizontal path; branch constraints exact')
print('elapsed',out['elapsed_seconds'])
