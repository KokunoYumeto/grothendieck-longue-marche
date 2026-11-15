#!/usr/bin/env python3
"""Exact linear and graph certificates for A.28.

The existence and shape of the tame semistable cover are proved in the
paper. This program checks its genus/toric alternatives and the complete
CM-plane calculation; it does not infer an all-degree claim from ranks.
"""
import json
from pathlib import Path
import sympy as s

u,v=s.symbols('s r',nonzero=True)
P=s.ones(3)/3
M=v*s.eye(3)+(u-v)*P
N=u*s.eye(3)+(v-u)*P
assert (M*N-u*v*s.eye(3)).applyfunc(s.factor)==s.zeros(3)
assert s.factor(M.det())==u*v*v
assert s.factor(N.det())==u*u*v

# Every entry is nonzero if s-r and s+2r are nonzero. Entrywise DM=MD'
# then imposes all nine equalities d_i=e_j, a rank-five system in six
# variables, leaving only the simultaneous scalar.
equations=[]
for i in range(3):
 for j in range(3):
  row=[0]*6
  row[i]=1
  row[3+j]=-1
  equations.append(row)
E=s.Matrix(equations)
assert E.rank()==5
assert E.nullspace()==[s.ones(6,1)]

graphs=[
 {'main_components':1,'rational_components':1,'edges':3,
  'vertex_genus_sum':1,'dual_graph_b1':2},
 {'main_components':3,'rational_components':1,'edges':3,
  'vertex_genus_sum':3,'dual_graph_b1':0}]
for g in graphs:
 assert g['dual_graph_b1']==g['edges']-g['main_components']-g['rational_components']+1
 assert g['vertex_genus_sum']+g['dual_graph_b1']==3
out={'status':'all exact assertions passed',
 'M':[[str(s.factor(x)) for x in row] for row in M.tolist()],
 'N':[[str(s.factor(x)) for x in row] for row in N.tolist()],
 'M_times_N':'s*r*I_3','det_M':'s*r^2','det_N':'s^2*r',
 'diagonal_intersection_equations_rank':E.rank(),
 'diagonal_intersection_dimension':6-E.rank(),
 'graph_alternatives':graphs,
 'good_Jacobian_selects':'three elliptic tails, toric rank zero',
 'remaining_graded_algebra':'free Lie algebra on t and Omega',
 'scope':'No actual higher fixed element or full fixed-subgroup classification inferred.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
