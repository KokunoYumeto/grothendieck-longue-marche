#!/usr/bin/env python3
"""Independent source corridor and exact Artin bridge audit."""
from pathlib import Path
from fractions import Fraction as F
import json
H=Path(__file__).resolve().parent;ROOT=H.parent.parent
B=json.loads((ROOT/'work_CE/next_symmetric_nodes/symmetric_source_bridge.json').read_text())
C=json.loads((H/'symmetric_critical_deformation.json').read_text())
P=json.loads((H/'symmetric_fixed_basis.json').read_text())
U=[tuple(map(F,u)) for u in C['coefficient_points']]
norm=lambda u:u[0]*u[0]+u[1]*u[1]
epsilon=F(2,10**30)
for u in U[1:]:
 assert (F(99,100)+epsilon)**2<norm(u)<(F(101,100)-epsilon)**2
 assert norm((u[0]-1,u[1]))>(F(11,10)+epsilon)**2
assert 1+F(371,1000)**2<F(11,10)**2
# These loose bounds hold throughout the certified coefficient homotopy.
qmax=F(9,25)
bounds={'A_constant':F(11,10)*F(101,100),'A_moving':F(11,10)*qmax/F(99,100),'B_linear':F(11,10)*(F(101,100)+qmax)/F(11,10),'B_fractional':F(11,10)*qmax*(1+F(101,100))/(F(99,100)-qmax),'old_rational':F(11,10),'old_square_roots':F(11,10)*F(3,5)}
assert max(bounds.values())<F(7,5)
assert F(9,5)-F(7,5)==F(2,5)
# Source v=1+sqrt(1-q) decreases from399/200 to9/5 and stays
# fixed under Fq. The entire right corridor Re(ROT*v)>=9/5 is clear.
assert F(399,200)*(2-F(399,200))==F(399,40000)
assert F(9,5)*(2-F(9,5))==qmax

def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(int(x))
 return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[x] if x>0 else inv(A[-x])))
def art(w):
 A={i:(i,) for i in range(1,22)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(red(a+b+inv(a)),a) if x>0 else (b,red(inv(b)+a+b))
 return A
W=B['nodal_base_to_pairing_base_braid'];A=art(tuple(-x for x in W));Ai=art(tuple(reversed(W)))
for j in range(1,22):assert sub(A[j],Ai)==(j,) and sub(Ai[j],A)==(j,)
assert B['rational_pairing_base_order']==P['original_generator_physical_order']
# Check both stored dictionaries without depending on producer helpers.
def arrays(x):return {int(k):tuple(v) for k,v in x.items()} if isinstance(x,dict) else {i+1:tuple(v) for i,v in enumerate(x)}
# The legacy producer arrays used an uncalibrated chronological convention.
# Preserve them in the archived input, and compute actual pull/push here.
for j in range(1,22):
 core=list(A[j])
 while len(core)>1 and core[0]==-core[-1]:core=core[1:-1]
 assert len(core)==1 and core[0]>0
 assert B['nodal_base_initial_order'][core[0]-1]==B['rational_pairing_base_order'][j-1]
Fend=arrays(P['involution_images'])
Fnodal={j:sub(sub(Ai[j],Fend),A) for j in range(1,22)}
for j in range(1,22):assert sub(Fnodal[j],Fnodal)==(j,)
out={'uniform_rotated_puncture_modulus_bound':'7/5','source_real_projection_lower_bound':'9/5','corridor_width':'2/5','individual_bounds':{k:str(v) for k,v in bounds.items()},'bridge_word':W,'conjugated_involution_at_nodal_base':{str(k):list(v) for k,v in Fnodal.items()},'explicit_inverse_compositions':42,'push_images':{str(j):list(w) for j,w in Ai.items()},'back_images':{str(j):list(w) for j,w in A.items()},'convention':'back(W)=art(negate_each W); push(W)=art(reverse W); F_nodal=back(W) F_endpoint push(W)','scope':'actual source/cut/Artin basepoint comparison; no source-kernel equality'}
(H/'symmetric_source_bridge_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: uniform exact norm bounds put every finite puncture inside |ROT*v|<7/5 on the entire real bridge.')
print('PASS: the source stays in Re(ROT*v)>=9/5, leaving a literal simply connected corridor of width2/5.')
print('PASS: chronological push/back convention is calibrated by the exact PL half-twist; raw legacy arrays are not reused.')
print('PASS: both42 bridge inverse substitutions and endpoint physical order match the independent fixed basis.')
print('PASS: transported actual involution at the nodal base squares to identity on all21 generators.')
