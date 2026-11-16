"""Verify exact images of the control kernel under both resolvents."""
import runpy
from pathlib import Path
from sympy.combinatorics import Permutation,PermutationGroup
D=runpy.run_path(str(Path(__file__).with_name('check_resolvent_colors.py')))
G=D['G'];minus=D['minus'];mul=D['mul'];inv=D['inv'];base=D['base'];s=D['s'];r=D['rp'];by=D['by'];words=D['words']
# Schreier generators for the stabilizer of the point4 in the five blocks.
trans={i:next(g for g in G if base(g,4)==i) for i in range(5)}
sg=[]
for i in range(5):
 for a in [s,r]:
  j=base(a,i)
  v=mul(mul(inv(trans[j]),a),trans[i]);assert base(v,4)==4
  if v!=tuple(range(30)):sg.append(Permutation(list(v)))
J=PermutationGroup(sg);assert J.order()==5832
print('Q_J order',J.order(),'Schreier generators',len(sg))
for which,letter in [('plus',3),('minus',1)]:
 g=trans[letter];a=mul(mul(inv(g),r),g)
 H=J.normal_closure(PermutationGroup(Permutation(list(a))))
 n=int(H.order());print(which,'killed fixed letter',letter,'normal closure order',n,'quotient order',int(J.order())//n)
 assert n==972
print('PASS: both filled images rho_+(U) and rho_-(U) equal the full level-two subgroup F.')
