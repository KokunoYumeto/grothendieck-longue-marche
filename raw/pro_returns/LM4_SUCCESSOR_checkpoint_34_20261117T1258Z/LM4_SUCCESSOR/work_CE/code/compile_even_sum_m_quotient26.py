#!/usr/bin/env python3
"""Exact index-two free-seven quotient, retaining the actual signed m maps."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json'
S=json.loads(p.read_text())
def red(w):
 o=[]
 for a in w:
  if o and o[-1]==-a:o.pop()
  else:o.append(a)
 return o
def inv(w):return [-a for a in w[::-1]]
def mul(*ws):return red(a for w in ws for a in w)
def sub(w,im):return mul(*(im[abs(a)] if a>0 else inv(im[-a]) for a in w))
# Surviving target: B,Dbar,t=f²,u=gf^-1,v0=fg,x,y=fxf^-1.
lookup={(0,2):1,(0,8):2,(1,5):3,(0,10):4,(1,10):5,(0,11):6,(1,11):7}
def scan(w):
 e=0;o=[]
 for a in w:
  j=abs(a);ep=e^(j in (5,10))
  k=lookup.get((e,j),0) if a>0 else -lookup.get((ep,j),0)
  if k:o.append(k)
  e=ep
 assert e==0
 return red(o)
basis=[[2],[8],[5,5],[10,-5],[5,10],[11],[5,11,-5]]
assert [scan(w) for w in basis]==[[i] for i in range(1,8)]
all_rs=[]
for e in (0,1):
 for i in range(1,12):
  ep=e^(i in (5,10))
  w=mul([5]*e,[i],[-5]*ep)
  if w:all_rs.append(w)
assert len(all_rs)==21
actions={}
for name in ('m','m_inverse'):
 im={int(k):v for k,v in S['source_ordinary_actions'][name].items()}
 action={i:scan(sub(w,im)) for i,w in enumerate(basis,1)}
 for w in all_rs:
  assert scan(sub(w,im))==sub(scan(w),action)
 actions[name]=action
 print(name,'all21 Schreier generator diagrams PASS; action',list(action.values()))
for i in range(1,8):
 assert sub(actions['m'][i],actions['m_inverse'])==[i]
 assert sub(actions['m_inverse'][i],actions['m'])==[i]
print('All14 signed free-seven inverse compositions PASS.')
# Replace Dbar by D0=x Dbar x^-1, leaving B and all five retained generators.
new_to_old={i:[i] for i in range(1,8)};new_to_old[2]=[6,2,-6]
old_to_new={i:[i] for i in range(1,8)};old_to_new[2]=[-6,2,6]
for i in range(1,8):
 assert sub(new_to_old[i],old_to_new)==[i]
 assert sub(old_to_new[i],new_to_old)==[i]
adapted={name:{i:sub(sub(new_to_old[i],a),old_to_new) for i in range(1,8)}
         for name,a in actions.items()}
assert adapted['m'][2]==adapted['m_inverse'][2]==[2]
assert adapted['m'][1]==[-3,5,1,-5,3]
assert adapted['m_inverse'][1]==[4,1,-4]
assert all(abs(a)>=3 for name in adapted for i in range(3,8) for a in adapted[name][i])
raw=[r['fiber11'] for r in S['actual_six_source_normal_forms'][:4]]
Ds=mul(raw[1],raw[0],inv(raw[2]),inv(raw[0]),inv(raw[1]))
source_D=scan(Ds)
assert source_D==[-1,6,2,-6,1]
assert sub(source_D,old_to_new)==[-1,2,1]
print('Actual D_s maps literally to B^-1 D0 B; both signed m maps fix D0.')
# Exact retained subgroup formulas: no finite orbit assertion is used.
small={1:[-1,2,1],2:[1],3:[3,-2,1]} # f,g,x, positive m
smallinv={1:[2],2:[2,1,-2],3:[3,1,-2]}
retbasis=[[1,1],[2,-1],[1,2],[3],[1,3,-1]]
fmap={1:5,2:10,3:11}
for name,am in [('m',small),('m_inverse',smallinv)]:
 for j,w in enumerate(retbasis,3):
  physical=[(1 if a>0 else -1)*fmap[abs(a)] for a in sub(w,am)]
  assert scan(physical)==actions[name][j]
q=[2,1];kappa=[-1,2];qp=[1,2]
assert sub(q,small)==q
assert mul(sub(kappa,small),kappa)==mul(inv(q),qp)
assert sub(sub([1],small),small)==mul(inv(q),[1],q)
assert sub(sub([2],small),small)==mul(inv(q),[2],q)
print('Retained f/g/x formulas and kappa2=q^-1 qprime identities PASS.')
out={'status':'PASS_EXACT_INDEX_TWO_FREE_SEVEN_AND_SOURCE_WORD',
 'input':str(p.relative_to(ROOT)),'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'target_basis':['B','bar_d','f^2','g f^-1','f g','x','f x f^-1'],
 'basis_F11':basis,'all21_RS_basis_F11':all_rs,'signed_actions':actions,
 'D0_basis_new_to_old':new_to_old,'D0_basis_old_to_new':old_to_new,
 'adapted_signed_actions':adapted,'source_D_old_basis':source_D,'source_D_adapted':[-1,2,1],
 'small_retained_actions':{'m':small,'m_inverse':smallinv},
 'scope':'All-orbit relation killing is the independently proved odd chi_sum argument. Exact21-generator quotient diagrams are checked. The whole integer orbit/free-subgroup consequence is proved in the companion note, not inferred from finite samples.'}
(ROOT/'work_CE/next_symmetric_nodes/even_sum_m_quotient26.json').write_text(json.dumps(out,indent=2)+'\n')
