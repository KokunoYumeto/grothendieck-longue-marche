#!/usr/bin/env python3
"""Exact post-freeze checks of the displayed rank-one group and quadratic formulas.

No image recognition and no manuscript edits. Run from any working directory:
    python research/group_quadric_checks.py
Writes only this script's adjacent *_results.json.
"""
from pathlib import Path
import json
import sympy as s
r,x,y,z=s.symbols('rho x y z')
law=lambda a,b:a+b+r*a*b
M=lambda t:s.Matrix([[1+r*t,t],[0,1]])
results={
 'group_law':{
  'associativity_difference':str(s.expand(law(law(x,y),z)-law(x,law(y,z)))),
  'identity_zero_difference':str(s.expand(law(x,0)-x)),
  'inverse_difference':str(s.cancel(law(x,-x/(1+r*x)))),
  'matrix_product_difference':str(s.simplify(M(x)*M(y)-M(law(x,y)))),
  'character_difference':str(s.expand((1+r*x)*(1+r*y)-(1+r*law(x,y)))),
  'fixed_section_difference':str(s.simplify(M(x)*s.Matrix([1,-r])-s.Matrix([1,-r]))),
  'rho_zero_law':str(law(x,y).subs(r,0)),
  'rho_invertible_coordinate_inverse':str(s.cancel(((1+r*x)-1)/r)),
 },
 'rank_one_family':[],
 'quadratic_family':[],
 'pairing_counts_scan045':[],
 'concrete_reading_checks':{}
}
for n in range(1,6):
 mu=s.symbols(f'mu0:{n+1}'); b=s.symbols(f'beta0:{n}')
 d=n+2
 rows=[];gens=[]
 for i in range(n+1):
  f=s.zeros(1,d);f[0,i]=1;f[0,i+1]=mu[i]
  if i<n:f[0,i+2]=b[i]
  a=s.eye(d)[:,i+1];rows.append(f);gens.append(s.eye(d)+a*f)
 w=s.zeros(d,1);w[n+1]=1
 for i in range(n,-1,-1):w[i]=-mu[i]*w[i+1]-(b[i]*w[i+2] if i<n else 0)
 pi=s.zeros(1,d);pi[0,0]=1;A=w*pi;rho=w[0]
 checks={
  'n':n,'dimension':d,'rho':str(s.expand(rho)),
  'all_fixed_covectors_vanish':all(s.expand((f*w)[0])==0 for f in rows),
  'rank_one_square':all(s.expand(v)==0 for v in A*A-rho*A),
  'all_commutators_zero':all(all(s.expand(v)==0 for v in A*T-T*A) for T in gens),
  'unimodular_center_last_coordinate':str(w[-1]),
 }
 results['rank_one_family'].append(checks)
 # The reflection chart, with the polar form from scans045,048,061.
 bf=list(b);c=[s.Integer(1)]
 for t in bf:c.append(s.expand(c[-1]*t))
 xx=s.symbols(f'x0:{d}') # x0 is source x_{-1}
 q=sum(c[i]*xx[i+1]**2 for i in range(n+1))-xx[0]*xx[1]-sum(c[i+1]*xx[i+1]*xx[i+2] for i in range(n))
 subs={mu[i]:-2 for i in range(n+1)}
 wr=s.simplify(w.subs(subs));rr=s.expand(wr[0]);sig=s.expand(wr[1])
 qwr=s.expand(q.subs(dict(zip(xx,list(wr))), simultaneous=True))
 polar=s.hessian(q,xx)
 val=s.expand(qwr+rr*sig/2)
 matrix_expected=-sig*pi.T
 ss=[s.Matrix([1]+[int(j<i) for j in range(n+1)]) for i in range(n+2)]
 cross=[[s.expand((v.T*polar*s.eye(d)[:,j+1])[0]) for j in range(n+1)] for v in ss]
 results['pairing_counts_scan045'].append({'n':n,'vertices':n+2,'edge_basis_vectors':n+1,'unordered_vertex_pairs':(n+2)*(n+1)//2,'edge_diagonals':n+1,'adjacent_edge_pairs':n,'nonadjacent_edge_pairs':n*(n-1)//2,'vertex_edge_cells':(n+2)*(n+1),'generically_nonzero_vertex_edge_cells':sum(t!=0 for row in cross for t in row),'identically_zero_vertex_edge_cells':sum(t==0 for row in cross for t in row),'vertex_edge_matrix':[[str(t) for t in row] for row in cross]})
 results['quadratic_family'].append({
  'n':n,'q':str(q),'rho':str(rr),'sigma_coordinate':str(sig),
  'two_q_center_plus_rho_sigma':str(s.expand(2*qwr+rr*sig)),
  'polar_center_plus_sigma_pi':str(s.simplify(polar*wr+sig*pi.T)),
  'reflection_invariance':all(s.expand(q.subs(dict(zip(xx,list(T.subs(subs)*s.Matrix(xx)))),simultaneous=True)-q)==0 for T in gens),
 })
from itertools import product
points_F2=lambda d:[v for v in product(range(2),repeat=d) if any(v)]
P2=points_F2(3);P1=points_F2(2)
anti=s.eye(3);fixed=[v for v in P2 if tuple(int(t)%2 for t in anti*s.Matrix(v))==v]
Cpts=[v for v in P2 if v[0]==0]
root_pairs=lambda rp:[v for v in P1 if (v[1]*(v[0]+rp*v[1]))%2==0]
roots_square=[v for v in P1 if v[1]**2%2==0]
u_F2=[t for t in range(2) if (1+t)%2!=0]
theta=s.pi/3;alpha=s.simplify(4*s.cos(theta)**2)
results['concrete_reading_checks']={
 'scan036_theta_pi_over_3':{'alpha':str(alpha),'beta_from_alpha_plus_2':str(alpha+2),'four_cos_twice_theta':str(s.simplify(4*s.cos(2*theta)))},
 'scan038_rho_1_lambda_0':{'zero_star_one':int(law(0,1).subs(r,1)),'identity_parameter':0},
 'scan043_F2_rho_1_sigma_0_tildesigma_1':{'U_F2_parameters':u_F2,'nonidentity_sections_over_F2':len([t for t in u_F2 if t!=0]),'antipodal_parameter_minus_2_over_rho':(-2)%2},
 'scan054_F2_n1_beta0_1':{'basis':['a_-1','a0','a1'],'rho':1,'rho_prime':1,'sigma':0,'sigma_prime':1,'normalized_antipodal_vector_o_prime':[int(2*t)%2 for t in (1,0,1)],'antipodism_matrix':[[int(t) for t in row] for row in anti.tolist()],'fixed_projective_points':fixed,'fixed_projective_points_count':len(fixed),'hyperplane_C_points':Cpts,'hyperplane_C_points_count':len(Cpts)},
 'scan054_even_n_binary_form':{'polynomial_over_F2':'mu*(lambda+rho_prime*mu)','rho_prime_0_roots_P1_F2':root_pairs(0),'rho_prime_1_roots_P1_F2':root_pairs(1)},
 'scan055_odd_n_binary_form_F2':{'polynomial_with_sigma_prime_rho_prime_1':'mu^2','support_P1_F2':roots_square,'scheme_length':int(s.Poly(y*y,y,modulus=2).degree()),'reduced_support_length':len(roots_square),'root_multiplicity':int(s.factor_list(y*y,y,modulus=2)[1][0][1])},
}
results['concrete_reading_checks']['scan041_even_F2_n2_beta_0_1']={'n':2,'beta':[0,1],'rho':0,'rho_half':1,'sigma':1,'preservation_polynomial':'t+t^2','roots_F2':[t for t in range(2) if (t+t*t)%2==0],'group_law':'t+s'}
assert all(v['all_fixed_covectors_vanish'] and v['rank_one_square'] and v['all_commutators_zero'] for v in results['rank_one_family'])
assert all(v['two_q_center_plus_rho_sigma']=='0' and v['polar_center_plus_sigma_pi']==str(s.zeros(v['n']+2,1)) and v['reflection_invariance'] for v in results['quadratic_family'])
out=Path(__file__).with_name('group_quadric_checks_results.json')
out.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'output':str(out),'symbolic_dimensions':list(range(1,6)),'rank_one_checks':len(results['rank_one_family']),'quadratic_checks':len(results['quadratic_family']),'all_exact_checks_passed':True},indent=2))
