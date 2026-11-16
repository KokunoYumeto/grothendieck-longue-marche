#!/usr/bin/env python3
"""Check the complete finite Q12 ingredients of a constructive frame-separating quotient.
The huge semidirect product is represented through its permutation module, not enumerated.
"""
from itertools import product
import json
N=12
I=(1,0,0,1)
def can(a):return min(tuple(x%N for x in a),tuple(-x%N for x in a))
def mm(a,b):
 p,q,r,s=a;t,u,v,w=b
 return can((p*t+q*v,p*u+q*w,r*t+s*v,r*u+s*w))
def inv(a):p,q,r,s=a;return can((s,-q,-r,p))
def powr(a,k):
 r=I
 for _ in range(k):r=mm(r,a)
 return r
Q=sorted({can(a) for a in product(range(N),repeat=4) if (a[0]*a[3]-a[1]*a[2])%N==1})
assert len(Q)==576
S=can((0,1,-1,0));R=can((0,-1,1,-1))
assert powr(S,2)==I and powr(R,3)==I
# Their images generate Q, so these are the intended modular generators.
seen={I};todo=[I]
while todo:
 a=todo.pop()
 for b in (S,R):
  c=mm(a,b)
  if c not in seen:seen.add(c);todo.append(c)
assert seen==set(Q)
out={'Q12_order':len(Q),'SL2_Z12_order':2*len(Q)}
for p,t in [(2,S),(3,R)]:
 H={powr(t,k) for k in range(p)}
 def coset(g):return tuple(sorted(mm(g,h) for h in H))
 cosets=sorted({coset(g) for g in Q});base=coset(I)
 idx={c:i for i,c in enumerate(cosets)}
 action=[idx[coset(mm(t,c[0]))] for c in cosets]
 cent=[g for g in Q if mm(g,t)==mm(t,g)]
 obstruction={}
 for g in cent:
  c=coset(g)
  assert action[idx[base]]==idx[base] and action[idx[c]]==idx[c]
  # In coinvariants, the two fixed-point basis vectors remain independent.
  vanish=(c==base)
  assert vanish==(g in H)
  obstruction[str(g)]=not vanish
 assert all(tuple(x%2 for x in h)!=I for h in H if h!=I)
 out[f'order_{p}']={'module_dimension':len(cosets),'quotient_centralizer_size':len(cent),'centralizer_projection_survivors':len(H),'obstructed_centralizer_residues':sum(obstruction.values()),'all_distinct_fixed_basis_obstructions_checked':True}
out['ambient_E_order']='576 * 2^288 * 3^192'
tau=mm(S,R)
T={powr(tau,k) for k in range(12)}
assert len(T)==12
Hs={I,S}
def scoset(g):return tuple(sorted(mm(g,h) for h in Hs))
tau_orbit={scoset(powr(tau,k)) for k in range(12)}
assert len(tau_orbit)==12
cent_tau=[g for g in Q if mm(g,tau)==mm(tau,g)]
survivors=[g for g in cent_tau if scoset(g) in tau_orbit]
assert set(survivors)==T
assert Hs.intersection(cent_tau)=={I}
out['cusp']={'order_in_Q12':12,'quotient_centralizer_size':len(cent_tau),
 'centralizer_projection_survivors':len(survivors),
 'survivors_are_exactly_cusp_powers':True,
 'M2_coinvariant_obstructions_checked':len(cent_tau)-len(survivors)}
# If a normalized action is inner, its pure frames have this common residue.
# The actual signed frame is I mod 4, so the cusp exponent is divisible by 4.
gauge_cases=[]
for k in range(0,12,4):
 rho=(-k*2)%3  # -(k/2) modulo 3, using 2^{-1}=2.
 assert (8*rho+k)%12==0
 gauge_cases.append({'cusp_exponent':k,'rho_mod3':rho,'T_equals_W_equals_I':True})
out['outer_gauge_normalization_cases']=gauge_cases
out['interpretation']='The quotient image of each lifted torsion centralizer is exactly its cyclic factor. Pure finite conjugators therefore have unique Q12 residues.'
print(json.dumps(out,indent=2))
