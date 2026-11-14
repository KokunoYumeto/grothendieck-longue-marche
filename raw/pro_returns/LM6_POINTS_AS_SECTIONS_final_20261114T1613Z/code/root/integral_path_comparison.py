#!/usr/bin/env python3
"""Exact finite kernel of the compact-and-unit comparison in E.39.

This computes a coefficient comparison and its connecting cocycles.
It does not choose an actual integral tangential path class.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

here=Path(__file__).parent
d=json.loads((here/'class_three_fibre_output.json').read_text())
T=s.Matrix(d['A_tau']); C=s.Matrix(d['C_V'])
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=s.Matrix([(v,-u) for u,v in coords])
J=s.eye(10)
J[2:,:2]=-U
J[2:,2:]=3*s.eye(8)
TN=s.diag(T[:2,:2],7*s.eye(8))
CN=s.diag(C[:2,:2],C[2:,2:])
assert J*T==TN*J
assert J*C==CN*J
S=smith_normal_form(J,domain=ZZ)
smith=[abs(int(S[i,i])) for i in range(10)]
assert smith==[1,1]+[3]*8

Q=s.zeros(8,10)
Q[:,:2]=U; Q[:,2:]=s.eye(8)
assert all(int(x)%3==0 for x in Q*J)
CT=C[2:,2:]
assert all(int(x)%3==0 for x in Q*TN-Q)
assert all(int(x)%3==0 for x in Q*CN-CT*Q)
fixed=[]
for i,j in [(1,2),(4,5),(6,7)]:
    v=s.zeros(8,1);v[i]=1;v[j]=-1
    assert CT*v==v
    fixed.append(v)
assert CT.trace()==-2
assert (8+int(CT.trace()))//2==3

connecting=[]
Tp=C*T*C
for i in range(8):
    v=s.zeros(10,1);v[i+2]=s.Rational(1,3)
    bt=(T-s.eye(10))*v
    btp=(Tp-s.eye(10))*v
    assert bt==btp
    assert bt[i+2]==2 and sum(abs(x) for x in bt)==2
    connecting.append(list(map(int,bt)))
out={
 'claim':'Integral compact-and-unit comparison and its finite cohomology kernel',
 'domain_order':['f1','f2','A0','A1','A2','B0','B1','B2','C1','C2'],
 'comparison_matrix':list(map(list,J.tolist())),
 'Smith_invariant_factors':smith,
 'coefficient_cokernel_over_K':'(Z/3)^8, trivial action for K=Q(zeta3)',
 'complex_conjugation_on_cokernel':CT.tolist(),
 'fixed_dimension_over_Q':3,
 'fixed_basis':[['A1',1,'A2',-1],['B1',1,'B2',-1],['C1',1,'C2',-1]],
 'connecting_cocycles_at_tau_and_tau_prime':connecting,
 'cohomology_kernel_proof':'H0 of target is zero; the connecting map from H0 of the finite cokernel is injective and has image ker H1(comparison)',
 'actual_integral_path_class_evaluated':False,
 'checks_passed':True
}
(here/'integral_path_comparison_output.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['comparison_matrix','complex_conjugation_on_cokernel','connecting_cocycles_at_tau_and_tau_prime']},indent=2))
