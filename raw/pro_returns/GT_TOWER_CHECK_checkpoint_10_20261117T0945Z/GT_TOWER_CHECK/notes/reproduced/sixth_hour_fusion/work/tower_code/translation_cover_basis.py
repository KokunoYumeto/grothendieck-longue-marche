#!/usr/bin/env python3
"""The literal nine-point translation cover F10 < F2 and a surface basis."""
from pathlib import Path
import json,numpy as np

def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(int(x))
 return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,images):
 out=()
 for x in w:out=red(out+(images[x-1] if x>0 else inv(images[-x-1])))
 return out
def compose(a,b):return tuple(sub(w,a) for w in b)
def comm(a,b):return a+b+inv(a)+inv(b)
Q=[(i,j) for j in range(3) for i in range(3)];qi={q:k for k,q in enumerate(Q)}
def step(q,k,sg=1):
 v=list(q);v[k]=(v[k]+sg)%3;return tuple(v)
def section(q):return (2,)*q[1]+(1,)*q[0]
tree={(qi[(i,j)],0) for j in range(3) for i in range(2)}|{(qi[(0,j)],1) for j in range(2)}
chords=[(q,k) for q in range(9) for k in range(2) if (q,k) not in tree]
ci={e:i+1 for i,e in enumerate(chords)}
def rewrite(w):
 q=(0,0);out=[]
 for x in w:
  k=abs(x)-1
  if x>0:
   e=(qi[q],k);q=step(q,k)
   if e in ci:out.append(ci[e])
  else:
   q=step(q,k,-1);e=(qi[q],k)
   if e in ci:out.append(-ci[e])
 return q,red(out)
old_E=[]
for q,k in chords:
 w=section(Q[q])+(k+1,)+inv(section(step(Q[q],k)))
 end,v=rewrite(w);assert end==(0,0) and v==(len(old_E)+1,);old_E.append(w)
aold=rewrite((1,1,1))[1];bold=rewrite((2,2,2))[1]
assert len(aold)==len(bold)==1 and aold[0]>0 and bold[0]>0
faces=[]
for q in Q:
 end,w=rewrite(section(q)+(1,2,-1,-2)+inv(section(q)))
 assert end==(0,0);faces.append(w)
known={aold[0]:(1,),bold[0]:(2,)};face_variables={};remaining=list(range(9))
while len(known)<10:
 success=False
 for f in remaining:
  unknown=[(j,x) for j,x in enumerate(faces[f]) if abs(x) not in known]
  if len(unknown)!=1:continue
  j,x=unknown[0];var=3+len(face_variables)
  images=tuple(known.get(k,(k,)) for k in range(1,11))
  left=sub(faces[f][:j],images);right=sub(faces[f][j+1:],images)
  expression=red(inv(left)+(var,)+inv(right))
  known[abs(x)]=expression if x>0 else inv(expression)
  face_variables[f]=var;remaining.remove(f);success=True;break
 assert success,('no free basis elimination',known,remaining)
assert len(remaining)==1 and len(face_variables)==8
last=remaining[0];temp_old_images=tuple(known[k] for k in range(1,11))
W=inv(sub(faces[last],temp_old_images));H=red(x for x in W if abs(x)<=2)
# Retain the exact orientation/basis change, rather than calling it canonical.
chosen=None
for swap in (False,True):
 for sa in (1,-1):
  for sb in (1,-1):
   images=((sa*(2 if swap else 1),),(sb*(1 if swap else 2),))+tuple((k,) for k in range(3,11))
   if sub(H,images)==(1,2,-1,-2):chosen=images;break
  if chosen:break
 if chosen:break
assert chosen is not None
old_to_temp=tuple(sub(w,chosen) for w in temp_old_images);W=sub(W,chosen)
handle_old=[None,None]
for oldhandle,image in enumerate(chosen[:2]):
 x=image[0];source=aold if oldhandle==0 else bold
 handle_old[abs(x)-1]=source if x>0 else inv(source)
ci_positions=[(i,x) for i,x in enumerate(W) if abs(x)>=3]
assert len(ci_positions)==8 and all(x>0 for _,x in ci_positions)
assert len({x for _,x in ci_positions})==8
var_to_face={v:f for f,v in face_variables.items()}
temp_to_std=[(1,),(2,)]+[None]*8
std_old=list(handle_old);std_labels=[]
for n,(pos,var) in enumerate(ci_positions,3):
 suffix=red(x for x in W[pos+1:] if abs(x)<=2)
 temp_to_std[var-1]=red(suffix+(n,)+inv(suffix))
 suffix_old=sub(suffix,handle_old)
 std_old.append(red(inv(suffix_old)+faces[var_to_face[var]]+suffix_old))
 std_labels.append(Q[var_to_face[var]])
old_std=tuple(sub(w,temp_to_std) for w in old_to_temp);std_old=tuple(std_old)
for k in range(10):
 assert sub(old_std[k],std_old)==(k+1,)
 assert sub(std_old[k],old_std)==(k+1,)
assert sub(faces[last],old_std)==inv((1,2,-1,-2)+tuple(range(3,11)))
std_E=tuple(sub(w,old_E) for w in std_old)

def E_to_std(w):
 q,v=rewrite(w);assert q==(0,0);return sub(v,old_std)
def restricted(substitution):return tuple(E_to_std(sub(w,substitution)) for w in std_E)
deck=[]
for g in (1,2):deck.append(tuple(E_to_std((g,)+w+(-g,)) for w in std_E))
normalizer=[restricted(((1,),(2,1))),restricted(((1,-2),(2,)))]
# Deck cubes and their commutator have the literal inner corrections.
identity=tuple((i,) for i in range(1,11))
for j,g in enumerate(deck):
 cub=compose(g,compose(g,g));u=E_to_std((j+1,)*3)
 assert cub==tuple(red(u+(i,)+inv(u)) for i in range(1,11))
# Nine peripheral vectors, upstairs forgetting, and the separate covering map.
peripheral_words=[sub(w,old_std) for w in faces]
def exponent(w,n=10):return [sum(1 if x==j else -1 if x==-j else 0 for x in w) for j in range(1,n+1)]
periph=np.array([exponent(w) for w in peripheral_words],dtype=np.int16)
assert not np.any(periph[:,:2]) and not np.any(periph.sum(axis=0))
cover_periods=np.array([[sum(1 if x==j else -1 if x==-j else 0 for x in w) for j in (1,2)] for w in std_E],dtype=np.int16)
assert not np.any(cover_periods%3)
# Integral coordinates in the primitive UPSTAIRS lattice basis (3a,3b).
# This division occurs over Z and is never a division in F3.
forget=cover_periods//3
assert np.array_equal(forget[2:],np.zeros((8,2),dtype=np.int16))
assert abs(round(np.linalg.det(forget[:2])))==1
print('PASS literal F10 < F2 cover, nine labels, inverse free-basis substitutions',flush=True)
print('Surface basis peripheral labels:',std_labels,'last',Q[last],flush=True)
print('Upstairs forgetting in primitive lattice basis (3a,3b):',forget[:2].tolist(),flush=True)
print('Composite covering periods in downstairs basis (a,b):',cover_periods[:2].tolist(),flush=True)
print('Deck generator lengths:',[[len(w) for w in d] for d in deck],flush=True)
print('Normalizer generator lengths:',[[len(w) for w in d] for d in normalizer],flush=True)
out={'H_labels':[list(q) for q in Q],'chords':chords,'old_basis_E':old_E,
 'standard_basis_E':std_E,'standard_basis_old':std_old,'old_basis_standard':old_std,
 'peripheral_words':peripheral_words,'standard_peripheral_labels':std_labels,'last_peripheral_label':Q[last],
 'deck_automorphisms':deck,'normalizer_automorphisms':normalizer,
 'upstairs_period_lattice_basis':['3a','3b'],
 'ordinary_forgetting_homology':forget.tolist(),
 'covering_lattice_inclusion':[[3,0],[0,3]],
 'composite_covering_periods_downstairs':cover_periods.tolist()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
