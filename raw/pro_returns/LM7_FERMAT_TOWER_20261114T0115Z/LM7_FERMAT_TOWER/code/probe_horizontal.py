from pathlib import Path
import sys, json, importlib.util
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
ROOT=Path('/workspace/scratch/e34c61ec5a35')
def load(name,p):
 sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
a=load('e87',ROOT/'research_e87/code/a_abelian_kernel_obstruction.py')
sm=load('smith',ROOT/'research_e82/code/e_cusp_local_smith.py')
h=load('hall',ROOT/'LM7_FERMAT_TOWER/code/e_unramified_sections.py')
x=json.loads((ROOT/'LM7_FERMAT_TOWER/code/e_wild_layers.json').read_text())['layers']
z=json.loads((ROOT/'research_e87/code/a_abelian_kernel_obstruction.json').read_text())
T,J=(s.Matrix(x['1'][k]) for k in ('input_tau','input_c'));G=(s.eye(10)-T)*(s.eye(10)+J)
H=h.Hall(2);ids=[i for i,d in enumerate(H.degree) if d==2];row={i:j for j,i in enumerate(ids)}
B=s.zeros(45,10)
for i in range(10):
 for j,c in H.bracket(i,5).items():B[row[j],i]=7*c
import numpy as np
arc=np.load(ROOT/'LM7_FERMAT_TOWER/code/e_wild_layers_r2_transforms.npz')
L=s.Matrix(arc['left'].tolist());vals=[t['valuation'] for t in x['2']['elementary_operations']];sel=[i for i,v in enumerate(vals) if v];mods=[3**vals[i] for i in sel]
F=(L*B)[sel,:];F=s.Matrix([[int(F[i,j])%mods[i] for j in range(10)]for i in range(15)])
Q=s.eye(10)
for i,m in enumerate(mods):Q=hermite_normal_form(Q*a.row_kernel(F[i,:]*Q,m))
qs=sm.local_smith(Q.tolist());qg=sm.local_smith((Q.inv()*G).tolist());gs=sm.local_smith(G.tolist())
print('F',F.tolist());print('Q',Q.tolist());print('image',qs['valuations']);print('zero cohom',qg['valuations'],qg['free_rank']);print('index',Q.det())
print('QL1',Q.inv()*s.Matrix(gs['left_inverse']))
R=s.Matrix(z['first_degree_map']);print('RQ',R*Q)
SQl=s.Matrix(qg['left_inverse']);src=Q*SQl
print('source cohom repr map',src.tolist());print('target cohom',R*src)
print('QG',Q.inv()*G)
res={'F':a.encode(F),'Q':a.encode(Q),'Q_smith':sm.encode(qs),'gauge_smith':sm.encode(qg),'source_representative':a.encode(src),'target_horizontal':a.encode(R*src)}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
