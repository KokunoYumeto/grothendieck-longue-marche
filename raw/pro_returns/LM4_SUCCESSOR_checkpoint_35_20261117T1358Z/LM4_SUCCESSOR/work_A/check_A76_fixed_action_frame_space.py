"""Exact complete affine frame space for the original A56 positive action.
No old quadratic or new cup norm conclusion follows from this linear data.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):G=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
D=json.loads((HERE/'A76_fixed_action_frame_class_space.json').read_text())
E=tuple(tuple(row)for row in json.loads((HERE.parent/'work_CE/Q6_integral_affine_data.json').read_text())['new_basis_columns_in_old_EB'][:4])
W=(8,11,20,23)
def pack(v):return sum(x<<(3*i)for i,x in enumerate(v))
cols=[];vectors=[]
for c,(_,i,a)in zip(D['columns'],D['labels']):
 v=tuple(G['fsm'](a,row)for row in G['SBASE'][i]);vectors.append(v);q=G['mix'](E,v)
 loc=tuple(q[i][j]for j in W for i in range(4));cols.append(c|(pack(loc)<<108))
piv={};ker=[]
for j,v in enumerate(cols):
 mask=1<<j
 while v:
  k=v.bit_length()-1
  if k in piv:v^=piv[k][0];mask^=piv[k][1]
  else:piv[k]=(v,mask);break
 if not v:ker.append(mask)
print('All right-frame bits276; old class rank54; joint class/local rank',len(piv),'; local-preserving kernel',len(ker))
out=dict(scope='Original positive action fixed; complete right-frame affine space above the initialC frame; oldclass plus four local free-Q values.',
 weights=W,labels=D['labels'],columns=cols,pivots={str(k):v for k,v in piv.items()},kernel_masks=ker,rank=len(piv),
 old_class_kernel_masks=D['kernel_masks'],frame_basis_vectors=vectors)
(HERE/'A76_fixed_action_frame_space.json').write_text(json.dumps(out,indent=2)+'\n')
