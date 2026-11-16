"""Add the actual rigid-seven class-three vanishing condition.

For a lift from H_T, vanishing of this one rigid restriction implies
vanishing of all twelve conjugate restrictions. The target contains
the normalized infinity point and the two fixed points; its degree3
map is a literal coordinate projection in the common ordered Hall basis.
"""
from pathlib import Path
import json,itertools,time
import sympy as s
from nilpotent_derivations import *
HERE=Path(__file__).resolve().parent;start=time.time()
d=json.loads((HERE/'degree3_actual_correction_certificate.json').read_text())
words=json.loads((HERE/'common_base_braid_words.json').read_text())
labels=words['initial_order_labels'];n=11;basis=grade3_basis(n)
keep={4,6,1,3,9,12};target_labels=[p for p in labels if p in keep]
target_pos={labels.index(p):i for i,p in enumerate(target_labels)}
target_basis=grade3_basis(6);assert len(target_basis)==70
tb={x:i for i,x in enumerate(target_basis)}
source_rows=[None]*70
for j,(k,w) in enumerate(basis):
 if k in target_pos and all(i in target_pos for i in w):
  image=(target_pos[k],tuple(target_pos[i] for i in w))
  i=tb[image];assert source_rows[i] is None;source_rows[i]=j
assert all(i is not None for i in source_rows)
def project(word):
 at=labels[:];out=[]
 for a in word:
  k=abs(a)-1
  if at[k] in keep and at[k+1] in keep:
   p=sum(v in keep for v in at[:k]);out.append((1 if a>0 else -1)*(p+1))
  at[k],at[k+1]=at[k+1],at[k]
 assert at==labels
 return out
T={i:log_parts(project(words['T'][str(i)]),6) for i in [1,2,3,5]}
negative=lambda v:(deriv_scale(v[0],-1),deriv_scale(v[1],-1))
t=product_log_parts([T[1],negative(T[2]),T[3]])
a2,twice_a3=commutator_parts(t,T[5])
assert not any(a2)
assert all(c%2==0 for p in twice_a3 for c in p.values())
a3=[{w:c//2 for w,c in p.items()} for p in twice_a3]
alpha=extract_grade3(a3,6,target_basis,reconstruct=True)
assert any(alpha)
IT=s.Matrix(d['T_correction_matrix']);I5=s.Matrix(d['I5_matrix'])
J=IT.row_join(I5);delta=s.Matrix(d['delta_coefficients'])
constraint=IT[source_rows,:].row_join(s.zeros(70,I5.cols))
C=J.col_join(constraint);b=delta.col_join(s.Matrix(alpha))
print('PASS exact projected a has zero layers1,2 and nonzero integral layer3',flush=True)
print('Rigid projection selects exactly70 source Hall coordinates',flush=True)

def pivots_mod(M,p=101):
 a=[[int(x)%p for x in M.row(i)] for i in range(M.rows)]
 ids=list(range(M.rows));rows=[];cols=[];r=0
 for j in range(M.cols):
  pos=next((i for i in range(r,M.rows) if a[i][j]),None)
  if pos is None:continue
  a[r],a[pos]=a[pos],a[r];ids[r],ids[pos]=ids[pos],ids[r]
  rows.append(ids[r]);cols.append(j)
  inv=pow(a[r][j],-1,p);a[r]=[(x*inv)%p for x in a[r]]
  nz=[k for k in range(j,M.cols) if a[r][k]]
  for i in range(r+1,M.rows):
   c=a[i][j]
   if c:
    for k in nz:a[i][k]=(a[i][k]-c*a[r][k])%p
  r+=1
 return rows,cols
tr,tc=pivots_mod(IT)
rows,cols=pivots_mod(C)
print('T correction rank mod101:',len(tc),'combined constrained rank:',len(cols),flush=True)
B=C[rows,cols];inv=B.inv(method='DM');assert B*inv==s.eye(len(cols))
sol=inv*b[rows,:];residual=b-C[:,cols]*sol
record={'description':__doc__,'target_order_labels':target_labels,
 'source_projection_rows':source_rows,'projected_a_grade3':alpha,
 'T_correction_rank_mod101':len(tc),'constrained_rank_mod101':len(cols),
 'pivot_rows':rows,'pivot_columns':cols,
 'exact_pivot_inverse':[[str(x) for x in inv.row(i)] for i in range(inv.rows)]}
if any(residual):
 row=next(i for i,x in enumerate(residual) if x)
 weights=C[row,cols]*inv
 assert weights*C[rows,:]==C[row,:]
 w=[-x for x in weights]+[s.Integer(1)];wrows=rows+[row]
 den=s.ilcm(*[x.q for x in w]);w=[int(x*den) for x in w]
 g=s.igcd(*w);w=[x//g for x in w]
 W=s.Matrix([w]);assert W*C[wrows,:]==s.zeros(1,C.cols)
 value=int((W*b[wrows,:])[0]);assert value
 record.update({'outcome':'EXCLUDED','witness_rows':wrows,'integer_left_witness':w,'witness_value':value})
 print('EXCLUSION after the rigid class3 condition; integer annihilator value',value,flush=True)
else:
 full=s.zeros(C.cols,1)
 for j,x in zip(cols,sol):full[j]=x
 assert C*full==b
 record.update({'outcome':'COMPATIBLE_OVER_Q','rational_correction_coefficients':[str(x) for x in full]})
 print('COMPATIBLE rational class3 lift satisfying the rigid-seven condition.',flush=True)
(HERE/'degree3_rigid_obstruction_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed',round(time.time()-start,2),'seconds',flush=True)
