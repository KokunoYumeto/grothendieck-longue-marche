"""Exact Britton reductions of the other eight triple variations.

The partial group includes the special node, four b triples and eight
retained discriminants. Its edge groups have rank17. This calculation
does not assume that subsequent relations preserve an HNN decomposition.
"""
from pathlib import Path
import json,hashlib
from weighted_stallings import WeightedFold,reduce_word as red,inverse as iv,multiply as mul,substitute as sub
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
B=json.loads((ROOT/'work_CE/four_triple_normality_gap.json').read_text())
C=json.loads((ROOT/'work_CE/discriminant_partial_hnn.json').read_text())
D=json.loads((HERE/'remaining_pencil_braids.json').read_text())
phi={int(k):tuple(v) for k,v in B['nielsen_basis'].items()}
keys=[6,12,1,19,20,2,15,9]
AD=[(10,)]+[phi[i] for i in keys];AR=[(10,)]
for j in range(0,8,2):
 P,Q=AD[j+1],AD[j+2];R=mul(P,Q)
 AR.extend([mul(iv(R),P,R),mul(iv(R),Q,R)])
DD=AD+[tuple(r['domain_V']) for r in C['rows']]
RR=AR+[tuple(r['range_W']) for r in C['rows']]
FD,FR=WeightedFold(DD),WeightedFold(RR)
dimages={i+1:w for i,w in enumerate(DD)};rimages={i+1:w for i,w in enumerate(RR)}
for j,w in enumerate(DD,1):
 assert FD.rewrite(w)==(j,)
 assert FR.rewrite(RR[j-1])==(j,)

def britton(w):
 w=red(w);steps=[]
 while True:
  pos=[i for i,x in enumerate(w) if abs(x)==11];change=False
  for left,right in zip(pos,pos[1:]):
   if w[left]!=-w[right]:continue
   h=w[left+1:right];fold=FD if w[left]==11 else FR
   expr=fold.rewrite(h)
   if expr is None:continue
   replaced=sub(expr,rimages if w[left]==11 else dimages)
   steps.append({'sign':w[left]//11,'H_word':h,'edge_basis_word':expr,'replacement':replaced})
   w=mul(w[:left],replaced,w[right+1:]);change=True;break
  if not change:return w,steps

def cyclic_britton(w):
 w,steps=britton(w);history=[{'rotation_prefix':(),'steps':steps}]
 while True:
  # Removing a common first/last inverse is conjugation, not an equality;
  # it is legitimate here because the input is a defining relator.
  prefix=[]
  while len(w)>1 and w[0]==-w[-1]:prefix.append(w[0]);w=w[1:-1]
  if prefix:history.append({'cyclic_peel_prefix':tuple(prefix)})
  oldcount=sum(abs(x)==11 for x in w);changed=False
  for pos,x in enumerate(w):
   if abs(x)!=11:continue
   rotated=mul(w[pos:],w[:pos]);r,s=britton(rotated)
   if sum(abs(x)==11 for x in r)<oldcount:
    history.append({'rotation_prefix':w[:pos],'steps':s});w=r;changed=True;break
  if not changed:return w,history

def art(w):
 A={i:(i,) for i in range(1,21)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(mul(a,b,iv(a)),a) if x>0 else (b,mul(iv(b),a,b))
 return A
new={i:(i,) for i in range(1,21)};new[10]=(10,-11)
rows=[]
for row in D['loops']:
 if not row['name'].startswith('other_triple_'):continue
 A=art(row['word']);Ai=art(iv(row['word']))
 for i in range(1,21):assert sub(A[i],Ai)==(i,)==sub(Ai[i],A)
 rels=[]
 for i in range(1,21):
  original=sub(mul(A[i],(-i,)),new)
  if not original:continue
  linear,steps=britton(original);result,history=cyclic_britton(linear)
  rels.append({'generic_index':i,'original':original,'linear_result':linear,'result':result,
               'remaining_b_letters':sum(abs(x)==11 for x in result),'steps':steps,'cyclic_history':history})
 rows.append({'name':row['name'],'variations':rels})
 print(row['name'],'nonempty variations',len(rels),'remaining b counts',[r['remaining_b_letters'] for r in rels],
       'result lengths',[len(r['result']) for r in rels],flush=True)
out={'scope':__doc__,'edge_domain_basis':DD,'edge_range_basis':RR,'rows':rows,
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
 [ROOT/'work_CE/four_triple_normality_gap.json',ROOT/'work_CE/discriminant_partial_hnn.json',HERE/'remaining_pencil_braids.json']}}
(HERE/'other_triple_hnn_reductions.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact inverse edge-basis rewrites, linear pinches and certified cyclic Britton reductions of all eight triple variations.')
