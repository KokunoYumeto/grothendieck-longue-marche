#!/usr/bin/env python3
"""Literal actual source filling and both selected-cone coarse actions."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
path=P/'annular_ordinary13_24.json';J=json.loads(path.read_text())
def red(w):
 s=[]
 for x in w:
  if s and s[-1]==-x:s.pop()
  else:s.append(x)
 return tuple(s)
def inv(w):return tuple(-x for x in reversed(w))
def cat(*ws):return red(x for w in ws for x in w)
def sub(w,A):return red(x for j in w for x in(A[abs(j)]if j>0 else inv(A[-j])))
def table(A):return {int(j):tuple(w)for j,w in A.items()}
fill=table(J['actual_family_filling'])
am,ap=[table(J['coarse_positive_actions'][s])for s in('kminus','kplus')]
ami,api=[table(J['coarse_negative_actions'][s])for s in('kminus','kplus')]
actions={4:am,-4:ami,5:ap,-5:api}
def acted(w,head):
 for j in reversed(head):w=sub(w,actions[j])
 return w
def normal(w):
 v=();head=()
 for j in w:
  if abs(j)<=3:v=cat(v,acted((j,),head))
  else:head=cat(head,(j,))
 return v,head
sources=[sub(row['ordinary13'],fill)for row in J['actual_six_source_words']]
assert sources==[(),(),(),(),(-1,5),(4,)]
D13=table(J['selected_plus_cone_action'])
old={1:5,2:10,3:13,4:11,5:12}
D={i:sub(D13[j],fill)for i,j in old.items()}
assert D=={1:(3,2,-3),2:(3,1,-3),3:(-3,),4:(4,),5:(3,5,-3)}
for j in range(1,6):assert sub(D[j],D)==(j,)
for row in J['all_eight_nonempty_coarse_relators']:
 assert normal(sub(row['word'],D))==((),())
for s in sources:assert normal(cat(sub(s,D),inv(s)))==((),())
# Replace the free base p by its actual source lift v=f^-1 p.
# Its fiber action is Inn(f^-1) alpha_p, not alpha_p itself.
av={j:cat((-1,),ap[j],(1,))for j in range(1,4)}
avi={j:sub(cat((1,j,-1)),api)for j in range(1,4)}
Dfiber={j:D[j]for j in range(1,4)}
for A,Ai in ((am,ami),(av,avi)):
 for j in range(1,4):
  assert sub(A[j],Ai)==sub(Ai[j],A)==(j,)
  assert sub(A[j],Dfiber)==sub(Dfiber[j],A)
# The three independent equations for each old base imply the action.
# Their fixed free-basis products are checked literally.
assert sub((3,1),am)==(3,1) and sub((2,-3),am)==(2,-3)
assert sub((1,3),ap)==(1,3) and sub((2,-3),ap)==(2,-3)
out={'status':'PASS_LITERAL_SOURCE_FILLING_AND_COARSE_FIXED_SPLITTING',
 'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'actual_six_source_images':sources,'selected_plus_cone_action':D,
 'actual_source_lifts':{'m':(4,),'v':(-1,5)},
 'source_fiber_actions':{'m':am,'v':av},'source_fiber_inverse_actions':{'m':ami,'v':avi},
 'all_fiber_action_cone_commutations':6,
 'scope':'The actual eight-family-filled quotient only. Fixed subgroup proof uses the full free-product fiber cone centralizer; no unfilled kernel fixed-lifting inference.'}
(P/'annular_coarse_source24.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual six source images are exactly1,1,1,1,f^-1 p,m')
print('PASS actual selected-plus cone action on all5 coarse generators, its square and all8 relators')
print('PASS both source lifts fixed in the complete coarse semidirect product')
print('PASS all6 exact fiber action/cone commutations and both source action inverses')
print('SCOPE exact coarse source/F2 comparison only; the unfilled fixed kernel remains open')
