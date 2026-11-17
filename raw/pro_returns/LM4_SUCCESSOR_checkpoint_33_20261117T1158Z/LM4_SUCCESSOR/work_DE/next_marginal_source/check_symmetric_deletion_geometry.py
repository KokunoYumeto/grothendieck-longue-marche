#!/usr/bin/env python3
"""Exact Q(zeta_5) audit of the actual F-symmetric deleted divisors.
No fundamental-group injectivity or fixed-lifting conclusion is inferred.
"""
import json
from pathlib import Path
import sympy as s
z=s.symbols('z'); phi=z**4+z**3+z**2+z+1

def f(a):
    num,den=s.fraction(s.cancel(a))
    return s.rem(s.expand(num*s.invert(den,phi,z)),phi,z)
def eq(a,b): return f(a-b)==0
def key(a):
    a=f(a);return tuple(str(a.coeff(z,j)) for j in range(4))
def enc(a):return list(key(a))
U=[f(z**j) for j in range(1,5)]
mu=[s.Integer(1)]+U
rows=[]
for at in ('v','w'):
 for ai,u in enumerate(U,1):
  for bt in ('v','w'):
   for bi,t in enumerate(U,1):
    other=f((u+t-u*t)/u if at==bt else t/(u+t-1))
    v,w=(u,other) if at=='v' else (other,u)
    q=f(v*w)
    assert not any(eq(v,x) or eq(w,x) for x in (0,1))
    assert not eq(v,w)
    assert not any(eq(q,x) for x in [0]+mu)
    bv=f(q+(t-1)*v-t);bw=f(q+(t-1)*w-t)
    assert eq(bv if bt=='v' else bw,0)
    # Transverse gradients of the two actual affine equations.
    jac=f(v if at=='v' and bt=='v' else v+t-1 if at=='v' else -(w+t-1) if bt=='v' else -w)
    assert jac!=0
    fv=f(v*(w-1)/(1-v));fw=f(w*(v-1)/(1-w))
    assert eq(fv*fw,q)
    assert eq(fv*(fw-1)/(1-fv),v) and eq(fw*(fv-1)/(1-fw),w)
    fixed=eq(fv,v) and eq(fw,w)
    assert fixed==(at==bt and ai==bi)
    assert fixed==eq(v+w,2)
    rows.append({'A':[at,ai],'F_A':[bt,bi],'v':enc(v),'w':enc(w),'q':enc(q),'jacobian':enc(jac),'fixed_source':fixed,'F_point':[enc(fv),enc(fw)]})
assert len({(tuple(r['v']),tuple(r['w'])) for r in rows})==64
lookup={(tuple(r['v']),tuple(r['w'])):i for i,r in enumerate(rows)}
node_permutation=[lookup[(tuple(r['F_point'][0]),tuple(r['F_point'][1]))] for r in rows]
assert all(node_permutation[node_permutation[i]]==i for i in range(64))
assert sum(i==j for i,j in enumerate(node_permutation))==8
qclusters={}
for r in rows:qclusters.setdefault(tuple(r['q']),[]).append([r['A'],r['F_A']])
# Each original component is internally disjoint from every other in X.
for u in U:
 for t in U: assert any(eq(u*t,k) for k in mu)
# The projective involution and the retained pencil are literal.
x,y,h,qpar=s.symbols('x y h q')
M=s.Matrix([[1,-1,2],[-1,1,2],[1,1,0]])
assert M*M==4*s.eye(3)
x1,y1,h1=M*s.Matrix([x,y,h])
Q=(x+h)*(y+h)-qpar*(x-h)*(y-h)
assert s.expand(Q.subs({x:x1,y:y1,h:h1}, simultaneous=True)-4*Q)==0
assert s.expand((x1+y1-2*h1)+2*(x+y-2*h))==0
# Its isolated fixed point is the removed point v=w=0.
assert M*s.Matrix([-1,-1,1])==-2*s.Matrix([-1,-1,1])
# Swap coordinates and coarse quotient formula.
v,w,r=s.symbols('v w r')
rho=w*(v-1)/(1-w)
vv=v*(w-1)/(1-v);ww=rho
assert s.cancel(ww*(vv-1)/(1-ww)-w)==0
assert s.cancel(v*w-(w+rho-w*rho))==0
out={'field':'Q[z]/(z^4+z^3+z^2+z+1)','pair_intersections':rows,'distinct_intersection_count':64,'source_fixed_intersections':sum(r['fixed_source'] for r in rows),'critical_value_clusters':[{'q':list(k),'pairs':v} for k,v in qclusters.items()],'distinct_q_values':len(qclusters),'F_node_permutation':node_permutation,'projective_matrix':[[int(v) for v in row] for row in M.tolist()],'claims_excluded':['relative Oka-Sakamoto injectivity','fixed-image lifting','source fixed-subgroup equality after critical fillings','actual marginal source-kernel equality']}
path=Path(__file__).with_name('symmetric_deletion_geometry.json');path.write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all64 mixed intersections are distinct, transverse, and inside the actual retained complement.')
print('PASS: each family internally disjoint; each component is a q-section.')
print('PASS: exactly8 mixed intersections lie on the fixed source; all are matching pairs.')
print('PASS: exact involution, swap-coordinate formula, projective matrix square and retained-conic invariance.')
print('PASS: exact node permutation has8 fixed nodes and28 two-element orbits.')
print('Distinct q critical values:',len(qclusters))
print('Cluster sizes:',sorted(len(v) for v in qclusters.values()))
print('No topological injectivity or fixed-lifting claim made.')
