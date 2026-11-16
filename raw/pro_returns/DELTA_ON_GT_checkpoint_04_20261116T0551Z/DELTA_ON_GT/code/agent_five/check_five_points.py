#!/usr/bin/env python3
"""Exact finite checks for the five-point audit. No GT shadow assertion is made."""
from itertools import permutations
from fractions import Fraction as F
import json
from pathlib import Path

def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))
def inv(p): return tuple(p.index(i) for i in range(len(p)))
def power(p,k):
 if k<0: return power(inv(p),-k)
 ans=tuple(range(len(p)))
 for _ in range(k): ans=compose(ans,p)
 return ans
def cyc(n,k): return tuple((i+1)%k if i<k else i for i in range(n))
def canonical(t):
 t=tuple(t); n=len(t)
 return min([t[i:]+t[:i] for i in range(n)]+[t[::-1][i:]+t[::-1][:i] for i in range(n)])
polygons=sorted(set(map(canonical, permutations(range(5)))))
assert len(polygons)==12
stabilizers=[]
for poly in polygons:
 stab=[p for p in permutations(range(5)) if canonical(tuple(p[i] for i in poly))==poly]
 assert len(stab)==10
 stabilizers.append(stab)
subgroups=set()
for poly in polygons:
 p=list(range(5))
 for i in range(5): p[poly[i]]=poly[(i+1)%5]
 p=tuple(p)
 subgroups.add(tuple(sorted(power(p,k) for k in range(5))))
assert len(subgroups)==6
def cycle_lengths(p):
 seen=set();lengths=[]
 for i in range(len(p)):
  if i in seen:continue
  j=i;n=0
  while j not in seen:seen.add(j);n+=1;j=p[j]
  lengths.append(n)
 return sorted(lengths)
power_operation={}
label_action={}
for a in (1,2,3,4):
 ip=pow(a,-1,5)
 act=[polygons.index(canonical(tuple(poly[(ip*j)%5] for j in range(5)))) for poly in polygons]
 assert sorted(act)==list(range(12))
 power_operation[a]={"permutation":act,"fixed_count":sum(i==j for i,j in enumerate(act)),"cycle_lengths":cycle_lengths(act)}
 assert power_operation[a]['fixed_count']==(12 if a in (1,4) else 0)
 arithmetic=[polygons.index(canonical(tuple((a*i)%5 for i in poly))) for poly in polygons]
 label_action[a]={"permutation":arithmetic,"fixed_count":sum(i==j for i,j in enumerate(arithmetic)),"cycle_lengths":cycle_lengths(arithmetic)}
 assert label_action[a]['cycle_lengths']==({1:[1]*12,2:[2,2,4,4],3:[2,2,4,4],4:[1,1,1,1,2,2,2,2]}[a])

# Fractional linear transformations, including infinity represented by None.
def mob(m,x):
 a,b,c,d=m
 if x is None: return None if c==0 else F(a,c)
 den=c*x+d
 return None if den==0 else F(a*x+b,den)
def mm(m,n):
 a,b,c,d=m; e,f,g,h=n
 return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def scalar(m): return m[1]==m[2]==0 and m[0]==m[3] and m[0]!=0
C=[F(0),F(1),F(9),None]
W={2:(1,-9,1,-1),3:(0,9,1,0),6:(9,-9,1,-9)}
wp={}
for n,m in W.items():
 assert scalar(mm(m,m))
 values=[mob(m,x) for x in C]
 assert set(values)==set(C)
 wp[n]=[C.index(x) for x in values]
 assert all(wp[n][i]!=i for i in range(4))
for x in C:
 assert mob(W[2],mob(W[3],x))==mob(W[6],x)
 assert mob(W[3],mob(W[2],x))==mob(W[6],x)

# The relation for an orbifold covering is target_order=e*source_order.
branch_data=[('0','0',1,3,3),('1','0',1,3,3),('1/2','1',2,1,2),('infinity','infinity',2,2,4)]
assert all(e*src==tar for _,_,e,src,tar in branch_data)
chi_source=F(1,3)+F(1,3)+F(1,2)-1
chi_target=F(1,3)+F(1,2)+F(1,4)-1
assert chi_source==2*chi_target

out={
 'pure_conjugator_permutation_counterexample':[{"order":k,"permutation":cyc(5,k),"inverse":inv(cyc(5,k)),"equal":cyc(5,k)==inv(cyc(5,k))} for k in (3,4,5)],
 'pentagonal_structures':len(polygons), 'stabilizer_order':10,'cyclic_C5_subgroups':len(subgroups),
 'polygons':polygons,'generator_power_operation':power_operation,
 'arithmetic_label_action_on_mu5':label_action,
 'Atkin_Lehner_cusp_order':['0','1','9','infinity'],'Atkin_Lehner_permutations':wp,
 'harmonic_orbifold_branch_data':branch_data,'orbifold_euler_characteristics':[str(chi_source),str(chi_target)],
 'principal_levels_not_nested':{'T3_in_Gamma3':True,'T3_in_Gamma4':3%4==0,'T4_in_Gamma4':True,'T4_in_Gamma3':4%3==0},
 'diagram_counts':{'vertices':12+20+30+60+60+120+60+120+60,'oriented_edges_assuming_independent_generators':1620,'graph_rank_if_connected':1620-542+1}
}
assert not any(r['equal'] for r in out['pure_conjugator_permutation_counterexample'])
print(json.dumps(out,indent=2))
