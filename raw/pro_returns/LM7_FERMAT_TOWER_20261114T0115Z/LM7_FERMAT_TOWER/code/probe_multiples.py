from pathlib import Path
import importlib.util,json,sympy as s,numpy as np
from sympy.matrices.normalforms import hermite_normal_form
root=Path('/workspace/scratch/e34c61ec5a35')
def load(n,p):
 sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
h=load('h',root/'LM7_FERMAT_TOWER/code/e_unramified_sections.py');a=load('a',root/'research_e89/code/a_horizontal_full.py');sm=load('sm',root/'LM7_FERMAT_TOWER/code/e_cusp_local_smith.py')
x=json.loads((root/'LM7_FERMAT_TOWER/code/e_wild_layers.json').read_text())['layers'];rel=json.loads((root/'LM7_FERMAT_TOWER/code/a_wild_kernel.json').read_text())['layers']['2'];z=json.loads((root/'research_e89/code/a_horizontal_full.json').read_text());R=s.Matrix(json.loads((root/'LM7_FERMAT_TOWER/code/a_abelian_kernel_obstruction.json').read_text())['first_degree_map'])
T1,J1=(s.Matrix(x['1'][k])for k in('input_tau','input_c'));T2,J2=(s.Matrix(x['2'][k])for k in('input_tau','input_c'));G=(s.eye(10)-T1)*(s.eye(10)+J1)
Q3=hermite_normal_form(a.row_kernel(R[1,:],3));print('Q3',Q3.tolist());ss=sm.local_smith((Q3.inv()*G).tolist());print('case3coh',ss['valuations'],ss['free_rank'])
Br=s.Matrix(z['full_horizontal_defect']);omega=(s.eye(45)-J2)*Br
Lt=a.decode(rel['left_transform']);Rt=a.decode(rel['domain_transform']);D=a.decode(rel['diagonal']);Bt=a.decode(rel['split_inverse'])[rel['plus_rank']:,:]
A=-Rt[:,:23]*s.diag(*[1/D[i,i]for i in range(23)])*(Lt*Bt*omega)[:23,:]
print('denoms',sorted(set(int(q.q)for q in A)));assert a.integral3(3*A*Q3);assert a.integral3(9*A)
F2=s.Matrix(json.loads((root/'LM7_FERMAT_TOWER/code/a_compatible_joint_fibre.json').read_text())['degree_two_pair_map']);ast=s.Matrix(json.loads((root/'LM7_FERMAT_TOWER/code/a_compatible_joint_fibre.json').read_text())['explicit_scaled_sigma_section'])
B=A-ast*((F2*A)[0,:]+(F2*A)[1,:])/6
print('adjusteddenoms',sorted(set(int(q.q)for q in B)));assert a.integral3(3*B*Q3);assert a.integral3(9*B)
print('jointB',F2*B);print('expected',R[2,:]/4-R[1,:]/6)
print('nonzeroB')
for i in range(B.rows):
 if any(B[i,j]for j in range(B.cols)):print(i,list(B[i,:]))
Path(__file__).with_suffix('.json').write_text(json.dumps({'Q3':a.encode(Q3),'case3_gauge_smith':sm.encode(ss),'universal_particular_correction':a.encode(B),'joint_correction':a.encode(F2*B)},indent=2)+'\n')
