"""Exact degree-three obstruction with the proved upper bound I_T <= V^T.

All words use the certified common geometric base.  The cyclic correction
space I5 is the actual image of the seventy free-Lie degree-three classes,
because its degree-one and degree-two maps are injective.  Exclusion from
V^T+I5 would exclude the larger space and hence the true correction space.
Inclusion in this upper bound alone is explicitly inconclusive.
"""
from pathlib import Path
from collections import defaultdict
import itertools,json,time
import sympy as s
from nilpotent_derivations import *
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
start=time.time();self_test()
data=json.loads((HERE/'common_base_braid_words.json').read_text())
labels=data['initial_order_labels'];n=len(labels);assert n==11
li={p:i for i,p in enumerate(labels)}
parts={}
for family in ['T','C5']:
 parts[family]={}
 for key,word in data[family].items():
  parts[family][int(key)]=log_parts(word,n)
 print('PASS exact Magnus/logarithm parts for',family,'generators',len(parts[family]),flush=True)

pairdata=json.loads((BASE/'full_pair_linking_certificate.json').read_text())
ps=[tuple(p) for p in pairdata['pair_rows']]
PD={p:pair_derivation(li[p[0]],li[p[1]],n) for p in ps}
def linear_derivation(weights):
 out=deriv_zero(n)
 for p,c in zip(ps,weights):
  if c:out=deriv_add(out,deriv_scale(PD[p],c))
 return out
for j,(D,_) in parts['T'].items():
 assert D==linear_derivation([row[j-1] for row in pairdata['full_matrix_rows_pairs_columns_basis']])
cyc=json.loads((HERE/'cyclic_bracket_span.json').read_text())
h1=json.loads((BASE/'ambient_rigid7_abelian_certificate.json').read_text())
ap=[tuple(p) for p in h1['ambient_pair_basis']]
cyclic_weights=[]
for j,(D,_) in sorted(parts['C5'].items()):
 vals=dict(zip(ap,cyc['meridian_ambient_H1_columns'][j]));vals[(4,6)]=0
 weights=[vals[p] for p in ps];cyclic_weights.append(weights)
 assert D==linear_derivation(weights)
print('PASS all19 first logarithmic derivations equal independent55-pair linkings',flush=True)

T=parts['T'];F=parts['C5']
negative=lambda x:(deriv_scale(x[0],-1),deriv_scale(x[1],-1))
t=product_log_parts([T[1],negative(T[2]),T[3]])
a2,a3twice=commutator_parts(t,T[5])
factors=[(0,1,-2),(0,2,-1),(0,3,-1),(0,4,-1),(0,5,-1),(1,2,1),(1,5,1)]
b2=deriv_zero(n);b3twice=deriv_zero(n)
for i,j,c in factors:
 x,y=commutator_parts(F[i],F[j]);b2=deriv_add(b2,deriv_scale(x,c));b3twice=deriv_add(b3twice,deriv_scale(y,c))
assert a2==deriv_scale(b2,2)
raw=deriv_add(a3twice,deriv_scale(b3twice,-2))
assert all(c%2==0 for p in raw for c in p.values())
delta=[{w:c//2 for w,c in p.items()} for p in raw]
basis=grade3_basis(n);assert len(basis)==990
d=extract_grade3(delta,n,basis,reconstruct=True)
assert any(d)
print('PASS matching degree2 images; integral delta reconstructed in990-dimensional degree3 basis',flush=True)
print('Delta nonzero coordinates',sum(x!=0 for x in d),'max absolute coefficient',max(abs(x) for x in d),flush=True)

free6=lyndon_words(6,3);assert len(free6)==70
I5=[]
q=[F[i][0] for i in range(6)]
for w in free6:
 der=lyndon_bracket(w,q,bracket)
 I5.append(extract_grade3(der,n,basis))
I5=s.Matrix(I5).T;assert I5.shape==(990,70)
print('Actual cyclic degree3 correction matrix shape',I5.shape,'rank',I5.rank(),flush=True)

geom=json.loads((BASE/'rigid7_subsets.json').read_text())
generators=[geom['T_permutations'][1],geom['T_permutations'][3]]
constraints=[];rhs=[];action_records=[]
for gi,permutation in enumerate(generators,1):
 def pair_image(p):
  x,y=[permutation[j-1]+1 for j in p]
  if x!=2 and y!=2:return PD[tuple(sorted((x,y)))]
  other=y if x==2 else x
  out=deriv_zero(n)
  for k in labels:
   if k!=other:out=deriv_add(out,deriv_scale(PD[tuple(sorted((other,k)))],-1))
  return out
 images={p:pair_image(p) for p in ps}
 def action_linear(weights):
  out=deriv_zero(n)
  for p,c in zip(ps,weights):
   if c:out=deriv_add(out,deriv_scale(images[p],c))
  return out
 # Act on delta through its certified free-Lie basis expression.
 acted=deriv_zero(n)
 gens_by_k={k:[images[tuple(sorted((labels[i],labels[k])))] for i in range(k)] for k in range(1,n)}
 for (k,w),c in zip(basis,d):
  if c:acted=deriv_add(acted,deriv_scale(lyndon_bracket(w,gens_by_k[k],bracket),c))
 acted_d=extract_grade3(acted,n,basis,reconstruct=True)
 acted_q=[action_linear(weights) for weights in cyclic_weights]
 acted_cols=[extract_grade3(lyndon_bracket(w,acted_q,bracket),n,basis) for w in free6]
 acted_I=s.Matrix(acted_cols).T
 constraints.append(acted_I-I5)
 rhs.append(s.Matrix(acted_d)-s.Matrix(d))
 action_records.append({'permutation_zero_based':permutation,
                        'delta_action':[int(x) for x in acted_d],
                        'I5_action':[[int(x) for x in acted_I.row(i)] for i in range(990)]})
 print('PASS Tgenerator',gi,'graded actions and delta reconstruction; elapsed',round(time.time()-start,2),flush=True)
C=s.Matrix.vstack(*constraints);b=s.Matrix.vstack(*rhs)
r=C.rank();aug=C.row_join(b).rank()
print('Tfixed upper-bound constraint shape',C.shape,'rank',r,'augmented rank',aug,flush=True)
record={'description':__doc__,'common_geometric_order_labels':labels,
 'graded_basis':[{'last_position':k,'lyndon_word':list(w)} for k,w in basis],
 'delta_coefficients':[int(x) for x in d],
 'delta_derivation':encode_derivation(delta),
 'I5_matrix':[[int(x) for x in I5.row(i)] for i in range(990)],
 'I5_lyndon_words':[list(w) for w in free6],
 'T_actions_on_needed_vectors':action_records,
 'constraint_matrix':[[int(x) for x in C.row(i)] for i in range(C.rows)],
 'constraint_rhs':[int(x) for x in b],
 'rank':r,'augmented_rank':aug}
if aug>r:
 _,cols=C.rref();_,rows=C.row_join(b).T.rref()
 rows=list(rows)
 restricted=C[rows,list(cols)]
 witness=restricted.T.nullspace()[0]
 multiple=s.ilcm(*[x.q for x in witness]);witness=witness*multiple
 divisor=s.igcd(*[int(x) for x in witness]);witness=witness/divisor
 assert witness.T*C[rows,:]==s.zeros(1,C.cols)
 value=(witness.T*b[rows,:])[0];assert value
 record['witness_rows']=rows;record['integer_left_witness']=[int(x) for x in witness]
 record['witness_value']=int(value)
 print('EXCLUSION: delta is outside V^T+I5; integer witness value',value,flush=True)
else:
 sol,parameters=C.gauss_jordan_solve(b);sol=sol.subs({p:0 for p in parameters})
 assert C*sol==b
 correction=I5*sol
 record['rational_cyclic_correction']=[str(x) for x in sol]
 record['rational_Tfixed_remainder']=[str(x) for x in s.Matrix(d)-correction]
 print('INCONCLUSIVE upper bound: delta belongs to V^T+I5. Actual I_T must still be computed.',flush=True)
record['generator_log_parts']={family:{str(k):{'D1':encode_derivation(x),'twiceD2':encode_derivation(y)} for k,(x,y) in values.items()} for family,values in parts.items()}
(HERE/'degree3_upper_obstruction_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed',round(time.time()-start,2),'seconds',flush=True)
