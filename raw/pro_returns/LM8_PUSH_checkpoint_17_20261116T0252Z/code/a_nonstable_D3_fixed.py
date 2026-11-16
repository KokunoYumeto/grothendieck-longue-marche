"""Exact map, Frobenius and symplectic-intersection certificates for A.32."""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

t=s.symbols('t')
maps=[]
for a in (6,-6):
    rhs=(t*t-4)*(t**3-3*t+a)
    x=(t**3-3*t+s.Rational(a,3))/4
    err=s.expand(rhs*(t*t-1)**2/64-(x**3-x))
    assert err==0
    maps.append({'a':a,'map_identity':str(err),'x_degree':int(s.degree(x,t))})

counts=[]
for p in (5,11):
    n=1+sum(sum((y*y-x**3+3*x-6)%p==0 for y in range(p)) for x in range(p))
    trace=p+1-n
    disc=trace*trace-4*p
    assert trace%p!=0
    counts.append({'p':p,'points':n,'trace':trace,'discriminant':disc})
assert [r['discriminant'] for r in counts]==[-19,-35]

# Basis order a1,a2,b1,b2; the component symplectic form is standard.
M=s.Matrix([[5,-1],[-2,4]])/3
N=M.inv().T
g=s.diag(M,N)
J=s.Matrix([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]])
assert g.T*J*g==J
A=s.Matrix([1,2,0,0]);B=s.Matrix([0,0,1,1])
C=s.Matrix([1,-1,0,0]);D=s.Matrix([0,0,2,-1])
assert g*A==A and g*B==B and g*C==2*C and g*D==D/2
assert (A.T*J*B)[0]==3 and (C.T*J*D)[0]==3
assert all((v.T*J*w)[0]==0 for v in (A,B) for w in (C,D))
pairs=list(combinations(range(4),2))
def wedge(v,w):return s.Matrix([v[i]*w[j]-v[j]*w[i] for i,j in pairs])
e=[s.eye(4)[:,i] for i in range(4)]
u1=wedge(e[0],e[2]);u2=wedge(e[1],e[3])
gu1=wedge(g*e[0],g*e[2]);gu2=wedge(g*e[1],g*e[3])
joint=s.Matrix.hstack(u1,u2,gu1,gu2)
assert joint.rank()==3 and gu1+gu2==u1+u2
out={'maps':maps,'ordinary_nonCM_counts':counts,
     'M':[[str(x) for x in row] for row in M.tolist()],
     'N':[[str(x) for x in row] for row in N.tolist()],
     'symplectic_identity':True,'original_factor_fixed':True,
     'complement_eigenvalues':['2','1/2'],
     'quadratic_joint_rank':joint.rank(),
     'quadratic_intersection_dimension':4-joint.rank(),
     'total_boundary_fixed':True,
     'scope':'Exact finite algebra accompanying the all-degree invariant and tensor proof; no claimed arithmetic realization of the chosen symplectic matrix.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
