#!/usr/bin/env python3
"""Actual inclusion of the compact small-map kernel into whole compact coinvariants.
Only retained marked exterior-action columns are used; this is a finite-map
calculation. No source correction is inferred without a separate source map.
"""
from pathlib import Path
import json,time,hashlib
R=Path(__file__).resolve().parent;start=time.time()
p=R/'d_residual_compact_norm.json';N=json.loads(p.read_text())
c=R/'d_residual_compact_cusp.json';C=json.loads(c.read_text())
s=R/'d_compact_splitting_maps.json';S=json.loads(s.read_text())
t=R/'d_arithmetic_A4_twisted.json';T=json.loads(t.read_text())
def lin(cols,v):
 x=0
 while v:
  b=v&-v;x^=cols[b.bit_length()-1];v^=b
 return x

def eliminate(cols):
 piv={};ker=[]
 for i,v in enumerate(cols):
  mask=1<<i
  while v:
   j=v.bit_length()-1
   if j not in piv:piv[j]=(v,mask);break
   a,b=piv[j];v^=a;mask^=b
  if not v:ker.append(mask)
 def solve(v):
  mask=0
  while v:
   j=v.bit_length()-1
   if j not in piv:return None
   a,b=piv[j];v^=a;mask^=b
  return mask
 def quotient(v):
  for j in sorted(piv,reverse=True):
   if v>>j&1:v^=piv[j][0]
  return v
 return solve,quotient,len(piv),ker
rows=[]
for n in N['cases']:
 char=n['character'];cr=next(x for x in C['cases'] if x['character']==char)
 sp=next(x for x in S['cases'] if x['character']==char)
 b=next(x for x in T['character_blocks'] if x['character']==char)
 acts={int(g):[int(x,16) for x in cs] for g,cs in n['all_action_columns'].items()}
 gens=sorted(set(sp['ordered_stabilizer_generators']+[next(a['q_state'] for a in b['all_stabilizer_actions'] if a['flip'])]))
 columns=[acts[g][i]^(1<<i) for g in gens for i in range(256)]
 solve,q,rank,_=eliminate(columns)
 kb=[int(x,16) for x in n['kernel_basis']]
 free=cr['coinvariant_representatives_in_kernel_basis'];reps=[kb[i] for i in free]
 inc=[q(v) for v in reps];_,_,irank,ikernel=eliminate(inc)
 nc=[int(x,16) for x in cr['ordinary_norm_columns_on_coinvariants']]
 _,_,nrank,nkernel=eliminate(nc)
 answers=[]
 for k in nkernel:
  target=lin(reps,k);sol=solve(target)
  if sol is not None:assert lin(columns,sol)==target
  answers.append(None if sol is None else hex(sol))
 row={'character':char,'whole_coinvariant_dimension':256-rank,'kernel_coinvariant_dimension':len(reps),
      'actual_coinvariant_inclusion_columns':[hex(v) for v in inc],
      'coinvariant_inclusion_rank':irank,'coinvariant_inclusion_kernel':[hex(v) for v in ikernel],
      'ordinary_norm_kernel':[hex(v) for v in nkernel],
      'norm_kernel_killed_by_whole_augmentation':all(v is not None for v in answers),
      'stabilizer_generators':gens,'whole_augmentation_columns':[hex(v) for v in columns],
      'augmentation_solutions_on_norm_kernel':answers}
 rows.append(row);print(json.dumps({k:v for k,v in row.items() if k not in ['whole_augmentation_columns','augmentation_solutions_on_norm_kernel']}),flush=True)
out={'summary':{'status':'PASS','elapsed_seconds':time.time()-start},'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [p,c,s,t]}}
(R/'d_old_compact_relaxation.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print(json.dumps(out['summary'],indent=2),flush=True)
