"""Compare independent certificates with the four unmodified rerun programs."""
from pathlib import Path
import json
from collections import deque
import numpy as np
import sympy as sp
root=Path(__file__).resolve().parent;old=root.parent/'originals'
def read(p):return json.loads(p.read_text())
a=read(root/'A_CF6_independent.json');b=read(old/'configuration_finite_certificates.json')
# Reconstruct independent positive-edge tree; compare full integral actions
# after a genuine change of Schreier basis, not just restricted matrices.
one=(0,0,0);gg=[(1,0,0),(0,1,0),one,one]
def gm(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3,(a[2]+b[2]+a[0]*b[1])%3)
def gi(a):return (-a[0]%3,-a[1]%3,(-a[2]+a[0]*a[1])%3)
reps={one:()};todo=deque([one]);tree=set()
while todo:
 v=todo.popleft()
 for j in range(4):
  w=gm(v,gg[j])
  if w not in reps:reps[w]=reps[v]+(j+1,);todo.append(w);tree.add((v,j))
edges=[(v,j) for v in reps for j in range(4) if (v,j) not in tree];ix={e:i for i,e in enumerate(edges)}
def chain(word):
 v=one;z=np.zeros(82,dtype=np.int64)
 for j in word:
  w=gm(v,gg[j-1] if j>0 else gi(gg[-j-1]));e=(v,j-1) if j>0 else (w,-j-1)
  if e in ix:z[ix[e]]+=1 if j>0 else -1
  v=w
 assert v==one
 return z
U=np.column_stack([chain(w['word']) for w in b['schreier_basis']]);det=int(sp.Matrix(U).det());assert abs(det)==1
for i,key in [('MC_columns','C3_integral_matrix'),('MD_columns','D3_integral_matrix')]:
 assert np.array_equal(np.array(a[i]).T@U,U@np.array(b[key]))
assert a['restricted_C']==b['small_C3_matrix'] and a['restricted_D']==b['small_D3_matrix']
assert a['fibre_quotient_order']==str(b['finite_fibre_quotient_order'])
np.testing.assert_array_equal(np.array(a['eigenvector']),U@np.array(b['v']))
res={'A.CF6':{'all_full_integral_matrix_entries_agree_after_basis_change':True,'change_of_basis_determinant':det,
             'difference_explained':'Positive-generator-only breadth-first tree versus signed-generator breadth-first tree; matrices are integrally conjugate.'}}
(root/'s6_CF6_change_of_basis.json').write_text(json.dumps(U.tolist())+'\n')
a=read(root/'A_CF11_independent.json');b=read(old/'configuration_symplectic_crosscheck.json')
for g,v in zip(a['generators'],b['generators'].values()):assert g==[x for row in v for x in row]
assert a['generated_order']==b['group_order']==51840
assert a['order_five_matrix']==[x for row in b['order5_matrix'] for x in row]
res['A.CF11']={'five_restricted_matrices_agree_exactly':True,'generated_order':51840,'order_five_word_and_matrix_agree':True,
 'independence_scope':'Independent geometric-transvection computation; original program separately rerun for full Schreier reduction.'}
a=read(root/'A_CR14_independent.json');b=read(old/'criterion_negative_controls.json')['single_prime_genus_two']
assert a['orbit']==b['Frobenius_orbit'];assert a['total_points']==b['N7'];assert a['GL4_3']==b['GL4_F3_order']
assert a['degree_seven_closed_points']==b['degree7_closed_points']
res['A.CR14']={'field_points_orbit_group_order_agree':True,'scope':'Finite arithmetic only; whole-group collision needs the separate group-theoretic proof.'}
a=read(root/'A_R6_independent.json');b=read(old/'frattini_two_prime.json')
assert a['modulus']==b['field_modulus_bits'] and a['zeta']==b['zeta9_bits'] and a['lambda_value']==b['lambda7_bits']
assert a['generated_order']==b['group_order'] and a['commutator_image_size']==b['derived_group_order']
res['A.R6']={'all_finite_invariants_agree':True,'group_order':576,'checked_automorphism_products':576**2}
result={'verified':True,'comparison':res}
(root/'s6_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
