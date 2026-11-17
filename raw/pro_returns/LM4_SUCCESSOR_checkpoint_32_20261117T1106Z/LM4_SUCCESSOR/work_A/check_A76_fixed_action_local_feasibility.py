"""Exhaust all four local six-cup solution sets in the complete fixed-action frame class space."""
from pathlib import Path
import json,itertools
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'A76_fixed_action_frame_space.json').read_text());L=json.loads((HERE.parent/'work_CE/original_A56_six_cup_local_frames.json').read_text())
P={int(k):tuple(v)for k,v in D['pivots'].items()}
def reduce(v):
 sol=0
 for k in sorted(P,reverse=True):
  if v>>k&1:v^=P[k][0];sol^=P[k][1]
 return v,sol
def pack(v):return sum(x<<(3*i)for i,x in enumerate(v))
sets=[r['allowed_right_free_values']for r in L['records']]
assert [r['weight']for r in L['records']]==D['weights']==[8,11,20,23]
sy=[[reduce(pack(v)<<(108+12*i))[0]for v in sets[i]]for i in range(4)]
left={}
for i,j in itertools.product(range(29),repeat=2):left.setdefault(sy[0][i]^sy[1][j],[]).append((i,j))
solutions=[]
for k,l in itertools.product(range(29),repeat=2):
 for i,j in left.get(sy[2][k]^sy[3][l],[]):
  vals=[sets[0][i],sets[1][j],sets[2][k],sets[3][l]];target=pack([x for v in vals for x in v])<<108
  rem,mask=reduce(target);assert not rem
  chk=0
  for b,c in enumerate(D['columns']):
   if mask>>b&1:chk^=c
  assert chk==target
  solutions.append(dict(local_indices=[i,j,k,l],values=vals,affine_mask=mask))
out=dict(scope='All29^4 local six-cup norm choices intersected with the full276-bit fixed-action old s-class space; old quadratic center norm remains to be imposed.',
 candidates=29**4,solutions=solutions,solution_count=len(solutions),left_syndrome_count=len(left),
 local_sets=sets,syndromes=sy,source='original_A56_six_cup_local_frames.json')
(HERE/'A76_fixed_action_local_feasibility.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact29^4 local candidates',29**4,'; oldclass-compatible tuples',len(solutions),'; left syndromes',len(left))
