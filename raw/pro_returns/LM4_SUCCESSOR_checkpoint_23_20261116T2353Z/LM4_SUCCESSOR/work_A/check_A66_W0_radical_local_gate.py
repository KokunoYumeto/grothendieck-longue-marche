"""Intersect the old-norm radical with the exact local W0 frame lists.
This script uses only saved finite linear data; no group witness is changed.
"""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
core=json.loads((HERE/'A66_zero_W_free_t_quadratic_core.json').read_text())
partial=json.loads((HERE/'A66_zero_W_free_t_partial.json').read_text())
old=json.loads((HERE.parent/'records/A63_zero_cusp_frame_feasibility.json').read_text())
allowed=json.loads((HERE.parent/'work_CE/A66_W0_joint_local_frame_pairs.json').read_text())
weights=(8,11,20,23)
def pack(vals):return sum(int(x)<<(3*i)for i,x in enumerate(vals))
def local_packed(full):
 return pack([(full>>(3*(36*i+w)))&7 for w in weights for i in range(4)])
lc=[local_packed(v>>108)for v in old['columns']]
def xor_sum(cols,mask):
 out=0
 while mask:
  bit=mask&-mask;out^=cols[bit.bit_length()-1];mask^=bit
 return out
fullrad=[xor_sum(core['homogeneous_kernel'],v)for v in core['radical']]
cols=[xor_sum(lc,v)for v in fullrad]
piv={}
for j,v in enumerate(cols):
 mask=1<<j
 while v:
  i=v.bit_length()-1
  if i in piv:v^=piv[i][0];mask^=piv[i][1]
  else:piv[i]=(v,mask);break
def solve(v):
 out=0
 while v:
  i=v.bit_length()-1
  if i not in piv:return None
  v^=piv[i][0];out^=piv[i][1]
 return out
base=pack([partial['normalized_cusp_frame_vectors'][i][w]for w in weights for i in range(4)])
lists=[r['right_corrections']for r in allowed['records']]
assert len(lists)==2 and all(len(a)==29 for a in lists)
answers=[]
for i,a in enumerate(lists[0]):
 for j,b in enumerate(lists[1]):
  target=pack(a[0]+a[1]+b[0]+b[1])
  sol=solve(base^target)
  if sol is not None:
   full=xor_sum(fullrad,sol)
   assert xor_sum(lc,full)==base^target
   answers.append(dict(local_indices=[i,j],radical_mask=sol,full360_mask=full,target_local=target))
out=dict(scope='Exact old central-norm radical variations of the stored W0 partial tuple',
 local_weights=weights,radical_dimension=len(cols),local_image_rank=len(piv),
 tested_pairs=841,feasible_pairs=len(answers),solutions=answers,
 initial_local=base,full360_radical_basis=fullrad,local_columns=cols)
(HERE/'A66_W0_radical_local_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print('Old norm radical dimension:',len(cols),'; local image rank:',len(piv))
print('Allowed local pairs tested:',841,'; compatible with the SAME old norm core:',len(answers))
if answers:print('First exact local indices and full correction:',answers[0])
print('This is a linear existence certificate; an actual adjusted group tuple still requires direct verification.')
