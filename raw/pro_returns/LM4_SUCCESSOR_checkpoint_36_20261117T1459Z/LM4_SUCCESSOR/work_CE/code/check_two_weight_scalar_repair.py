"""A two-fixed-weight Z/T correction for the actual full128 scalar frame.

Uses the already verified closed scalar formula. A separate original-law
check is still required when importing this correction into the full group.
"""
from pathlib import Path
import json,itertools
HERE=Path(__file__).resolve().parent
source=(HERE/'verify_full_scalar_norm_formula.py').read_text()
exec(compile(source.split("oldm=p['old_center_projection_columns']")[0],
             str(HERE/'verify_full_scalar_norm_formula.py'),'exec'))
oldm=p['old_center_projection_columns']
def solve(cols,target):
 piv={}
 for i,x in enumerate(cols):
  mask=1<<i
  while x:
   j=x.bit_length()-1
   if j not in piv:piv[j]=(x,mask);break
   x^=piv[j][0];mask^=piv[j][1]
 mask=0;x=target
 for j in sorted(piv,reverse=True):
  if x>>j&1:x^=piv[j][0];mask^=piv[j][1]
 return(None if x else mask),len(piv)
cols=[];labels=[]
for i in range(16):
 for weight in(8,11):
  for scalar in(1,2,4):
   z=[[0]*36 for _ in range(16)];z[i][weight]=scalar
   cols.append(pack(znorm(z)));labels.append(('Z',i,weight,scalar))
for ii,v in enumerate(p['old_center_norm_kernel_basis']):
 for scalar in(1,2,4):
  m=apply(oldm,[mul(scalar,x)for x in v])
  cols.append(pack(mnorm(m)));labels.append(('M',ii,-1,scalar))
target=pack(p['scalar_frame_square']);sol,rank=solve(cols,target)
assert rank==90 and sol is not None
z=[[0]*36 for _ in range(16)];m=[0]*10
for i,(kind,k,w,s)in enumerate(labels):
 if not(sol>>i&1):continue
 if kind=='Z':z[k][w]^=s
 else:m=[a^b for a,b in zip(m,apply(oldm,[mul(s,x)for x in p['old_center_norm_kernel_basis'][k]]))]
assert pack([a^b for a,b in zip(znorm(z),mnorm(m))])==target
J=json.loads((HERE.parent/'A66_UT4_frame_surjection.json').read_text())['J']
uz=[[xor(mul(J[i][j],z[j][k])for j in range(16))for k in range(36)]for i in range(4)]
pairs=list(itertools.combinations(range(4),2));pi={x:i for i,x in enumerate(pairs)}
triples4=list(itertools.combinations(range(4),3))
def tmap(a,t):return [mul(a[i],t[pi[j,k]])^mul(t[pi[i,j]],a[k])for i,j,k in triples4]
tc=[[0]*36 for _ in range(6)];ranks=[]
for weight in(8,11):
 a=[row[weight]for row in avec]
 ct=[];tl=[]
 for i in range(6):
  for scalar in(1,2,4):
   v=[0]*6;v[i]=scalar;ct.append(pack(tmap(a,v)));tl.append((i,scalar))
 u=[row[weight]for row in uz];ts,rr=solve(ct,pack(u));assert rr==12 and ts is not None
 ranks.append(rr)
 for j,(i,scalar)in enumerate(tl):
  if ts>>j&1:tc[i][weight]^=scalar
 assert tmap(a,[row[weight]for row in tc])==u
assert not any(uz[i][j]for i in range(4)for j in range(36)if j not in(8,11))
print('96 fixed-weight Z directions plus87 old-M directions: rank90, target attained: PASS')
print('At each ofweights8,11 the sixT->fourUT4 map has k-rank4: PASS')
print('The chosen T correction cancels the entire JZ residue; no U correction needed.')
out=dict(scope='Exact closed-form full128 frame correction for current[6,0] affine witness; original-law import check separate',
 weights=[8,11],scalar_correction_rank=rank,solution_mask=sol,labels=labels,
 ordinary_Z_correction=z,old_M_correction=m,lower_T_correction=tc,
 initial_UT4_residue=uz,pointwise_T_binary_ranks=ranks,
 scalar_equation=True,UT4_equation=True)
(HERE.parent/'two_weight_scalar_repair.json').write_text(json.dumps(out,indent=2)+'\n')
