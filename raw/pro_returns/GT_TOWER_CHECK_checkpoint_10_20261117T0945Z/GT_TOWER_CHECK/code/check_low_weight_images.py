#!/usr/bin/env python3
"""Exact source and pentagon spaces in weights 2 through 9 at prime 11.

All equations are expanded in free associative algebras. Rational nullspaces
are verified against every integer equation, and their reductions span the
entire mod-11 nullspace. These data accompany, but do not replace, the
separate proof constructing actual full gentle and arithmetic lifts.
"""
from pathlib import Path
import json, importlib.util, itertools, math
import sympy as sp
base=Path(__file__).parent
spec=importlib.util.spec_from_file_location('witness',base/'check_weight9_witness.py')
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
# Reuse only the explicitly defined pure-braid semidirect-product arithmetic.
# The stopped file prefix contains no census or assertions about GT images.
pent={"__file__":str(base/"check_weight9_pentagon.py")}
exec((base/'check_weight9_pentagon.py').read_text().split('pentagon_columns=[]')[0],pent)
p=11

def rref(A,n):
 A=[r[:] for r in A];positions=list(range(len(A)));piv=[];selected=[];rank=0
 for col in range(n):
  k=next((k for k in range(rank,len(A)) if A[k][col]%p),None)
  if k is None:continue
  selected.append(positions[k])
  A[rank],A[k]=A[k],A[rank];positions[rank],positions[k]=positions[k],positions[rank]
  inv=pow(A[rank][col],-1,p);A[rank]=[c*inv%p for c in A[rank]]
  for k in range(len(A)):
   if k!=rank and A[k][col]:
    c=A[k][col];A[k]=[(a-c*b)%p for a,b in zip(A[k],A[rank])]
  piv.append(col);rank+=1
 free=[i for i in range(n) if i not in piv];ker=[]
 for i in free:
  v=[0]*n;v[i]=1
  for k,j in enumerate(piv):v[j]=-A[k][i]%p
  ker.append(v)
 return rank,ker,selected

records=[]
for degree in range(2,10):
 lyndon=[''.join(t) for t in itertools.product('xy',repeat=degree) if w.is_lyndon(''.join(t))]
 rows={}
 for j,s in enumerate(lyndon):
  H=w.lyndon_word(s);K=w.scale(w.substitute(H,w.Z,w.X),-1)
  polynomials=[w.add(H,w.substitute(H,w.Y,w.X)),
   w.add(w.bracket(w.X,H),w.scale(w.bracket(w.add(w.X,w.Y),w.substitute(H,w.Z,w.Y)),-1)),
   w.add(w.bracket(H,w.Y),w.scale(w.bracket(K,w.add(w.X,w.Y)),-1)),
   w.add(H,w.substitute(H,w.Y,w.Z),w.substitute(H,w.Z,w.X))]
  for k,P in enumerate(polynomials):
   for mon,c in P.items():rows.setdefault((k,mon),[0]*len(lyndon))[j]=c
 integer_matrix=[r for _,r in sorted(rows.items()) if any(r)]
 matrix=[[c%p for c in r] for r in integer_matrix]
 rank,basis,selected=rref(matrix,len(lyndon))
 # An invertible mod-11 minor supplies rank>=rank over Q. Every exact
 # nullspace vector below is checked on ALL rows, proving equality.
 A=sp.Matrix([integer_matrix[i] for i in selected])
 null=A.nullspace();integral=[]
 for v in null:
  den=math.lcm(*(int(c.q) for c in v));assert den%11
  iv=[int(c*den) for c in v]
  assert all(sum(a*b for a,b in zip(row,iv))==0 for row in integer_matrix)
  integral.append(iv)
 assert len(integral)==len(basis)
 if integral:assert rref([[v[j]%p for v in integral] for j in range(len(lyndon))],len(integral))[0]==len(basis)
 ev=pent['ev'];add=pent['add'];scale=pent['scale']
 columns=[add(ev[0](s),ev[1](s),scale(ev[2](s),-1),scale(ev[3](s),-1)) for s in lyndon]
 outputs=[add(*(scale(P,c) for P,c in zip(columns,v) if c)) for v in basis]
 keys=sorted(set().union(*(P.keys() for P in outputs))) if outputs else []
 pm=[[P.get(k,0) for P in outputs] for k in keys]
 prank,pbasis,_=rref(pm,len(basis))
 actual_basis=[]
 for v in pbasis:actual_basis.append([sum(a*b[j] for a,b in zip(v,basis))%p for j in range(len(lyndon))])
 rec={'degree':degree,'free_lie_dimension':len(lyndon),'constraint_rank':rank,
      'gentle_dimension':len(basis),'pentagon_rank':prank,'pentagon_kernel_dimension':len(pbasis),
      'lyndon_words':lyndon,'source_basis':basis,'integer_source_basis':integral,
      'pentagon_kernel_in_source_basis':pbasis,'pentagon_kernel_lyndon_basis':actual_basis}
 records.append(rec)
 print('degree',degree,'free',len(lyndon),'gentle',len(basis),'pentagon kernel',len(pbasis),'integral lifting PASS',flush=True)
# Explicit independent Kummer detections, no class-group hypothesis.
kummer=[]
for weight in [3,5,7,9]:
 for q in sp.primerange(23,5000):
  if (q-1)%11:continue
  gen=int(sp.primitive_root(q));zeta=pow(gen,(q-1)//11,q)
  unit=1
  exponents=[pow(a,weight-1,11) for a in range(1,11)]
  for a,e in zip(range(1,11),exponents):unit=unit*pow((1-pow(zeta,a,q))%q,e,q)%q
  residue=pow(unit,(q-1)//11,q)
  if residue!=1:
   rec={'weight':weight,'prime':int(q),'primitive_generator':gen,'zeta':zeta,'exponents':exponents,'unit':unit,'power_residue':residue}
   kummer.append(rec);print('Kummer',rec,flush=True);break
 else:raise AssertionError('No Kummer detector found')
# Check the actual commutator direction required in weight eight.
def from_coeff(rec,v):
 return w.add(*(w.scale(w.lyndon_word(t),c) for t,c in zip(rec['lyndon_words'],v) if c))
def delta(H,K):
 out={}
 for mon,c in K.items():
  for i,ch in enumerate(mon):
   if ch=='y':
    for term,a in w.bracket(w.Y,H).items():out[mon[:i]+term+mon[i+1:]]=out.get(mon[:i]+term+mon[i+1:],0)+c*a
 return w.clean(out)
r3=next(r for r in records if r['degree']==3);r5=next(r for r in records if r['degree']==5);r8=next(r for r in records if r['degree']==8)
h3=from_coeff(r3,r3['pentagon_kernel_lyndon_basis'][0]);h5=from_coeff(r5,r5['pentagon_kernel_lyndon_basis'][0])
ihara=w.add(w.bracket(h3,h5),delta(h3,h5),w.scale(delta(h5,h3),-1))
ihara={k:v%11 for k,v in ihara.items() if v%11}
h8={k:v%11 for k,v in from_coeff(r8,r8['pentagon_kernel_lyndon_basis'][0]).items() if v%11}
key=next(iter(h8));factor=ihara.get(key,0)*pow(h8[key],-1,11)%11
assert factor and ihara=={k:v*factor%11 for k,v in h8.items()}
print('Ihara bracket of weight3 and weight5: nonzero; factor',factor,'times weight8 basis',flush=True)
# An explicit smaller integral separating polynomial, still requiring the
# full lifting proof in the manuscript.
r7=next(r for r in records if r['degree']==7)
separators=[]
for coeff in r7['integer_source_basis']:
 H=from_coeff(r7,coeff)
 P=w.add(w.evaluate(H,w.tij(1,2),w.add(w.tij(2,3),w.tij(2,4))),
  w.evaluate(H,w.add(w.tij(1,3),w.tij(2,3)),w.tij(3,4)),
  w.scale(w.evaluate(H,w.tij(2,3),w.tij(3,4)),-1),
  w.scale(w.evaluate(H,w.add(w.tij(1,2),w.tij(1,3)),w.add(w.tij(2,4),w.tij(3,4))),-1),
  w.scale(w.evaluate(H,w.tij(1,2),w.tij(2,3)),-1))
 if P:
  rec={'lyndon_coefficients':{a:c for a,c in zip(r7['lyndon_words'],coeff) if c},'s4_pentagon':[[list(k),v] for k,v in sorted(P.items())]}
  separators.append(rec);print('Integral weight7 S4 separator:',rec,flush=True)
orders=[]
for c in range(3,11):
 dg=sum(r['gentle_dimension'] for r in records if r['degree']<c)
 dt=sum(r['pentagon_kernel_dimension'] for r in records if r['degree']<c)
 orders.append({'nilpotency_class':c,'gentle_unipotent_order':11**dg,'gt_unipotent_order':11**dt,'gentle_full_order':10*11**dg,'gt_full_order':10*11**dt})
print('Candidate finite image orders (the exact lift proof is in the paper):',orders,flush=True)
output={'prime':11,'weights':records,'kummer_detectors':kummer,'ihara_3_5_factor':factor,'weight7_separators':separators,'image_orders':orders}
(base/'check_low_weight_images.json').write_text(json.dumps(output,indent=2)+'\n')
print('Exact integer source lattices and mod-11 pentagons checked in every weight 2--9.')
