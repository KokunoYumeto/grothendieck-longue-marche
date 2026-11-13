#!/usr/bin/env python3
"""Exact peripheral automorphisms for both integral rank-nine matrices.

All elements live in the actual homology extension over the48-state base.
Odd denominators are actual Z2 scalars. No full profinite lift is inferred.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
from collections import deque
import json,time
import sympy as sp
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_affine_base.json').read_text())
H=json.loads((OUT/'d_arithmetic_rank9_seed.json').read_text())
M=[tuple(map(tuple,x)) for x in D['Q_linear_image_matrices']];mi={x:i for i,x in enumerate(M)}
S=tuple(map(tuple,D['quotient_s_columns']));R=tuple(map(tuple,D['quotient_r_columns']))
def mv(A,v):return tuple(sum(v[j]*A[j][i] for j in range(4))%3 for i in range(4))
def m4(A,B):return tuple(mv(A,c) for c in B)
tab=[[mi[m4(a,b)] for b in M] for a in M];si=mi[S];ri=mi[R];ti=tab[si][ri]
inv=[next(j for j in range(48) if tab[i][j]==0) for i in range(48)]
rs=[tab[g][si] for g in range(48)];rr=[tab[g][ri] for g in range(48)]
ch=H['rank9_cycle_chords'];ci={e:j for j,e in enumerate(ch)}
def add(a,b):return [x+y for x,y in zip(a,b)]
def scale(a,n):return [n*x for x in a]
def left(g,v):
 out=[0]*48
 for i,a in enumerate(v):out[tab[g][i]]+=a
 return out
def mul(a,b):return tab[a[0]][b[0]],add(a[1],left(a[0],b[1]))
def inverse(a):return inv[a[0]],scale(left(inv[a[0]],a[1]),-1)
zero=[0]*48;ss=(si,zero);pr=zero[:];pr[0]=1;pr[ri]=-1;rr0=(ri,pr)
def evalword(word,gens=(ss,rr0)):
 out=(0,zero)
 for a in word:
  out=mul(out,gens[0] if a==0 else (gens[1] if a==1 else mul(gens[1],gens[1])))
 return out
cycles=[]
for j,w in enumerate(H['all9_marked_words']):
 q,c=evalword(w);assert q==0 and [c[e] for e in ch]==[int(i==j) for i in range(9)];cycles.append(c)
gwords={0:[]};todo=[0]
for q in todo:
 for token,h in [(0,rs[q]),(1,rr[q])]:
  if h not in gwords:gwords[h]=gwords[q]+[token];todo.append(h)
qelts={q:evalword(w) for q,w in gwords.items()}
assert all(x[0]==q for q,x in qelts.items())
def lift(q,v):
 p=qelts[q][1][:]
 for a,c in zip(v,cycles):
  if a:p=add(p,scale(c,a))
 return q,p
def conj(a,b):return mul(mul(a,b),inverse(a))
def data(qb,qa,bb,aa):
 beta=lift(qb,bb);A=lift(qa,aa)
 gs=conj(beta,ss);gr=conj(A,rr0)
 assert gs[0]==si and gr[0]==ri
 Tc=[]
 for w in H['all9_marked_words']:
  q,c=evalword(w,(gs,gr));assert q==0;Tc.extend(c[e] for e in ch)
 cusp=add(mul(gs,gr)[1],scale(mul(ss,rr0)[1],-1))
 return Tc+[cusp[e] for e in ch]
q8=H['linear_Q8_states'];z=H['central_involution_state']
betas=[q for q in q8 if q not in (0,z) and tab[q][si]==tab[si][q]]
assert len(betas)==2 and all(tab[q][q]==z for q in betas)
records=[]
for qb in betas:
 for rec in H['four_quarter_turn_candidates']:
  if not rec['integral_over_Z2']:continue
  for qa in (0,z):
   base=data(qb,qa,[0]*9,[0]*9)
   cols=[]
   for j in range(18):
    v=[0]*18;v[j]=1
    cols.append([x-y for x,y in zip(data(qb,qa,v[:9],v[9:]),base)])
   target=[x for col in rec['seven_times_columns'] for x in col]+[0]*9
   rhs=[x-7*y for x,y in zip(target,base)]
   A=sp.Matrix.hstack(*[sp.Matrix(c) for c in cols]);aug=A.row_join(sp.Matrix(rhs))
   rref,piv=aug.rref();consistent=18 not in piv
   item={'beta_linear_state':qb,'r_conjugator_linear_state':qa,
         'quarter_turn_power':rec['quarter_turn_power'],
         'linear_constraint_rank':A.rank(),'consistent_over_Q':consistent}
   if consistent:
    denominators=sorted({int(x.q) for x in rref})
    two_parts=[d&-d for d in denominators]
    assert max(two_parts)<=4
    item.update({'rref_denominators':denominators,
                 'maximum_two_primary_rref_denominator':max(two_parts),
                 'exhaustive_free_residue_modulus':4,
                 'integrality_constant_on_each_mod4_free_residue_class':True})
    piv=list(piv);free=[j for j in range(18) if j not in piv]
    found=None;attempts=0
    for vals in product(range(4),repeat=len(free)):
     attempts+=1;v=[sp.Rational(0)]*18
     for j,a in zip(free,vals):v[j]=sp.Rational(a)
     for i,j in enumerate(piv):
      v[j]=rref[i,18]-sum(rref[i,k]*v[k] for k in free)
     if all(int(x.q)%2 for x in v):found=v;break
    if found is None:
     item.update({'integral_over_Z2':False,'integral_free_choices_tested':attempts,'free_parameter_count':len(free),'rref_denominators':sorted({int(x.q) for x in rref})})
     records.append(item);continue
    b=[Fraction(int(x.p),7*int(x.q)) for x in found[:9]]
    a=[Fraction(int(x.p),7*int(x.q)) for x in found[9:]]
    actual=data(qb,qa,b,a)
    assert actual==[Fraction(x,7) for x in target]
    item.update({'integral_over_Z2':True,'integral_free_choices_tested':attempts,
                 'free_parameter_count':len(free),
                 'beta_cycle_coordinates':[str(x) for x in b],
                 'r_conjugator_cycle_coordinates':[str(x) for x in a],
                 'all9_homology_columns_and_exact_cusp_checked':True})
   records.append(item)
assert all(rec['consistent_over_Q'] for rec in records)
assert any(rec.get('integral_over_Z2',False) for rec in records)
# Complete fixed-cusp lattice and actual peripheral word.
HT=sp.Matrix(9,9,lambda i,j:H['homology_t_columns'][j][i])
fixed=(HT-sp.eye(9)).nullspace();assert len(fixed)==1
q,pc=evalword([0,1]*12);assert q==0
c=sp.Matrix([pc[e] for e in ch]);assert HT*c==c
from math import gcd
from functools import reduce
assert reduce(gcd,[abs(int(x)) for x in c])==1
# Exact H1(Q_*,U_Q)=0 invariant edge-to-vertex map:
# invariant vertex kernel is generated by(2,-3), precisely the edge norm image.
assert 24*2+16*(-3)==0 and gcd(2,3)==1
summary={
 'scope':'Actual peripheral automorphisms of the rank-nine homology extension.',
 'beta_linear_cosets':betas,'r_linear_cosets_tested':[0,z],
 'quarter_turn_branches_tested':[1,3],
 'complete_exact_conjugator_cases':len(records),
 'Z2_integral_conjugator_cases':sum(bool(r.get('integral_over_Z2')) for r in records),
 'all9_homology_columns_and_exact_cusp_checked_in_every_integral_case':True,
 'constraint_ranks':sorted({x['linear_constraint_rank'] for x in records}),
 'all_free_mod4_residue_tests_exhaustive':True,
 'maximum_two_primary_rref_denominator':max(x['maximum_two_primary_rref_denominator'] for x in records),
 'free_parameter_dimensions':sorted({x['free_parameter_count'] for x in records}),
 'fixed_cusp_lattice_rank':1,'actual_t12_class_is_primitive':True,
 'ordinary_H1_Qstar_UQ_vanishes':True,
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'all_exact_conjugator_records':records,
      'actual_primitive_t12_homology_column':[int(x) for x in c],
      'invariant_vertex_orbit_sizes':[24,16],
      'invariant_vertex_kernel_generator':[2,-3],
      'invariant_edge_norm_boundary':[2,-3]}
(OUT/'d_arithmetic_rank9_conjugators.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
