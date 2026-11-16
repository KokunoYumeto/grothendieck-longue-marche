"""Full rational class-three correction space of the tetrahedral subgroup.

All thirteen generator logarithms are included. The Lie subalgebra they
generate in nilpotency class3 is spanned by the generators, all78 binary
brackets, and all ternary brackets. A six-element basis of the degree-one
image suffices for the latter. Taking the kernel of the first two layers
therefore includes every source-abelian relation and every bracket
relation; it does not replace H_T intersect gamma3P by gamma3H_T.
"""
from pathlib import Path
import json,itertools,time
import sympy as s
from nilpotent_derivations import *
from magnus4 import log_parts4,self_test4
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
start=time.time();self_test4()
common=json.loads((HERE/'common_base_braid_words.json').read_text())
upper=json.loads((HERE/'degree3_upper_obstruction_certificate.json').read_text())
labels=common['initial_order_labels'];n=11;basis=grade3_basis(n)
parts=[]
for i in range(1,14):
 value=log_parts4(common['T'][str(i)],n)
 old=upper['generator_log_parts']['T'][str(i)]
 assert value[0]==decode_derivation(old['D1']) and value[1]==decode_derivation(old['twiceD2'])
 parts.append(value)
 print('PASS tetrahedral generator',i,'degree4 Magnus and logarithm; elapsed',round(time.time()-start,2),flush=True)
(HERE/'T_generator_log3.json').write_text(json.dumps({'description':'D1,twiceD2,24D3 of every common-base tetrahedral meridian',
 'initial_order_labels':labels,
 'generators':[{'index':i+1,'D1':encode_derivation(x),'twiceD2':encode_derivation(y),'24D3':encode_derivation(z)} for i,(x,y,z) in enumerate(parts)]},indent=2)+'\n')

lowers=[];uppers=[];names=[]
def low(one,two):
 out={}
 for degree,D in [(1,one),(2,two)]:
  for i,p in enumerate(D):
   for w,c in p.items():
    if c:out[(degree,i,w)]=c
 return out
for i,(x,y,z) in enumerate(parts):
 lowers.append(low(deriv_scale(x,24),deriv_scale(y,12)))
 uppers.append(z);names.append(['generator',i+1])
for i,j in itertools.combinations(range(13),2):
 x,x2,_=parts[i];y,y2,_=parts[j]
 lowers.append(low(deriv_zero(n),deriv_scale(bracket(x,y),24)))
 uppers.append(deriv_scale(deriv_add(bracket(x,y2),bracket(x2,y)),12))
 names.append(['Lie_bracket',i+1,j+1])
assert len(lowers)==91
keys=sorted(set().union(*(p.keys() for p in lowers)))
L=s.Matrix([[p.get(k,0) for p in lowers] for k in keys])
print('Lower-layer matrix',L.shape,'constructing exact fraction-free RREF',flush=True)
R,pivots=L.to_DM().convert_to(s.QQ).rref()
R=R.to_Matrix();rank=len(pivots)
null=[]
for j in range(91):
 if j in pivots:continue
 v=s.zeros(91,1);v[j]=1
 for i,p in enumerate(pivots):v[p]=-R[i,j]
 mult=s.ilcm(*[x.q for x in v]);v=v*mult
 divisor=s.igcd(*[int(x) for x in v]);v=v/divisor
 assert L*v==s.zeros(L.rows,1)
 null.append([int(x) for x in v])
assert len(null)==91-rank
print('PASS complete lower-layer kernel: rank',rank,'nullity',len(null),flush=True)

IT=[];correction_names=[]
for q,v in enumerate(null):
 D=deriv_zero(n)
 for c,U in zip(v,uppers):
  if c:D=deriv_add(D,deriv_scale(U,c))
 coeff=extract_grade3(D,n,basis,reconstruct=True)
 if any(coeff):IT.append(coeff);correction_names.append(['lower_relation',q])
print('PASS all lower-layer relations reconstructed in actual ambient grade3',flush=True)

# Ternary brackets depend only on the rank-six degree-one image.
h1=json.loads((BASE/'full_pair_linking_certificate.json').read_text())
M=s.Matrix(h1['full_matrix_rows_pairs_columns_basis']);_,chosen=M.rref();chosen=list(chosen)
assert len(chosen)==6
q=[parts[i][0] for i in chosen]
for w in lyndon_words(6,3):
 D=lyndon_bracket(w,q,bracket)
 coeff=extract_grade3(D,n,basis)
 if any(coeff):IT.append(coeff);correction_names.append(['ternary_Lyndon',list(w)])
IT=s.Matrix(IT).T
I5=s.Matrix(upper['I5_matrix']);J=IT.row_join(I5);d=s.Matrix(upper['delta_coefficients'])
print('Full tetrahedral correction spanning columns',IT.shape,'; combined',J.shape,flush=True)

def modular_pivots(M,p=101):
 a=[[int(x)%p for x in M.row(i)] for i in range(M.rows)]
 row_ids=list(range(M.rows));rows=[];cols=[];r=0
 for j in range(M.cols):
  pivot=next((i for i in range(r,M.rows) if a[i][j]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];row_ids[r],row_ids[pivot]=row_ids[pivot],row_ids[r]
  rows.append(row_ids[r]);cols.append(j)
  inv=pow(a[r][j],-1,p);a[r]=[(x*inv)%p for x in a[r]]
  nz=[k for k in range(j,M.cols) if a[r][k]]
  for i in range(r+1,M.rows):
   c=a[i][j]
   if c:
    for k in nz:a[i][k]=(a[i][k]-c*a[r][k])%p
  r+=1
  if r==M.rows:break
 return rows,cols
rows,cols=modular_pivots(J)
B=J[rows,cols]
print('Mod101 rank lower bound',len(cols),'computing exact pivot inverse',flush=True)
inv=B.inv(method='DM')
assert B*inv==s.eye(len(cols))
solution=inv*d[rows,:]
residual=d-J[:,cols]*solution
record={'description':__doc__,
 'lower_column_names':names,'lower_row_labels':[[degree,i,list(w)] for degree,i,w in keys],
 'lower_matrix':[[int(x) for x in L.row(i)] for i in range(L.rows)],
 'lower_rank':rank,'lower_pivot_columns':list(pivots),'lower_null_basis':null,
 'T_correction_names':correction_names,'T_ternary_source_generators':[i+1 for i in chosen],
 'T_correction_matrix':[[int(x) for x in IT.row(i)] for i in range(990)],
 'I5_matrix':upper['I5_matrix'],'delta_coefficients':upper['delta_coefficients'],
 'combined_mod101_rank':len(cols),'pivot_rows':rows,'pivot_columns':cols,
 'exact_pivot_inverse':[[str(x) for x in inv.row(i)] for i in range(inv.rows)]}
if any(residual):
 row=next(i for i,x in enumerate(residual) if x)
 alpha=J[row,cols]*inv
 assert alpha*J[rows,:]==J[row,:], 'modular rank underestimated; try another prime'
 witness=[-x for x in alpha];witness.append(s.Integer(1));wrows=rows+[row]
 den=s.ilcm(*[x.q for x in witness]);witness=[int(x*den) for x in witness]
 divisor=s.igcd(*witness);witness=[x//divisor for x in witness]
 W=s.Matrix([witness]);assert W*J[wrows,:]==s.zeros(1,J.cols)
 value=int((W*d[wrows,:])[0]);assert value
 record['outcome']='EXCLUDED';record['witness_rows']=wrows
 record['integer_left_witness']=witness;record['witness_value']=value
 print('EXCLUSION from actual rational correction space; integer witness value',value,flush=True)
else:
 full=s.zeros(J.cols,1)
 for j,x in zip(cols,solution):full[j]=x
 assert J*full==d
 record['outcome']='COMPATIBLE_OVER_Q'
 record['rational_correction_coefficients']=[str(x) for x in full]
 print('COMPATIBLE rational class3 correction; an integral common multiple must still be constructed or justified.',flush=True)
(HERE/'degree3_actual_correction_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed',round(time.time()-start,2),'seconds',flush=True)
