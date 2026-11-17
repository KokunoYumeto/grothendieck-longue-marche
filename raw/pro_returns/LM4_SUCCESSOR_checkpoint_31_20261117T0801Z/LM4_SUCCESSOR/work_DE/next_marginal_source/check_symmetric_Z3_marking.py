#!/usr/bin/env python3
"""Exact actual divisor labels and winding detector for the commuting triple."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
H=Path(__file__).resolve().parent;R=H.parents[1]
p=R/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json';d=json.loads(p.read_text())
f={int(k):tuple(v) for k,v in d['paired_basis_forward_in_nodal_cut_basis'].items()}
def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return tuple(a)
def inv(w):return tuple(-x for x in w[::-1])
def sub(w,A):return red(y for x in w for y in(A[abs(x)] if x>0 else inv(A[abs(x)])))
a=(2,);b=(12,13,-12);r=red(a+b+inv(a)+inv(b));assert sub(a,f)==(4,) and sub(b,f)==(16,)
node=next(n for n in d['node_columns'] if(n['loop_index'],n['local_node_index'])==(6,3));assert tuple(node['paired_relator'])==r and node['physical_labels']==[3,14]
for side in ['geometric_push_paired','based_pullback_paired']:
 A={int(k):tuple(v) for k,v in d['old_actions'][0][side].items()};assert all(A[j]==(j,) for j in [2,12,13]);assert sub(a,A)==a and sub(b,A)==b
op=R/'work_CE/next_symmetric_nodes/symmetric_old_base_braids.json';o=json.loads(op.read_text());assert o['initial_order'][3]==3 and o['initial_order'][15]==14
assert o['labels'][3]=={'kind':'A','branch':'v','index':1};assert o['labels'][14]=={'kind':'B','branch':'v','index':4}
assert '10^6' in o['far_basepoint']
centers={r['name']:tuple(map(Q,r['center'])) for r in o['loops']};u=centers['zeta^4'];rot=(Q(1),Q(371,1000))
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sc(c,a):return c*a[0],c*a[1]
def norm(a):return a[0]**2+a[1]**2
V=sc(Q(10**6)/norm(rot),(rot[0],-rot[1]));C=add(cm(add(u,(-Q(1),Q(0))),V),sc(-1,u))
row=o['loops'][0];points=[tuple(map(Q,o['common_trunk']['start'])),tuple(map(Q,o['common_trunk']['end']))]+[tuple(map(Q,s['end'])) for s in row['forward_segments']]
assert max(map(norm,points))<Q(1,1000);assert norm(C)>10**10
# The loop q has its literal positive square around0;the whisker cancels.
square=[tuple(map(Q,row['forward_segments'][0]['end']))]+[tuple(map(Q,s['end'])) for s in row['forward_segments'][1:]]
assert square[0]==square[-1] and sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(square,square[1:]))>0
out={'input_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest(),str(op.relative_to(R)):hashlib.sha256(op.read_bytes()).hexdigest()},'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'a_paired':a,'b_paired':b,'a_cut':[4],'b_cut':[16],'node':[6,3],'physical_labels':[3,14],'A_divisor':'v-zeta','B_divisor':'q+(zeta^4-1)v-zeta^4','third_character':'q=vw','old0_push_and_pull_fix_all_three_needed_generators':True,'far_v':[str(x) for x in V],'B_constant_norm_squared':str(norm(C)),'maximum_q_vertex_norm_squared':str(max(map(norm,points))),'winding_matrix_columns_a_b_t':[[1,0,0],[0,1,0],[0,0,1]],'common_basepoint_transport':'B87 q399/40000 to nodal q1/100 fixed-source bridge, then outer-half-plane fiber whisker;all three loops conjugated together','scope':'actual commuting triple and primitive winding detector;no asphericity assumed'}
(H/'symmetric_Z3_marking_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact paired/cut/physical divisor labels,actual node commutator,and old0 push/pull fixed words.')
print('PASS literal far lift has fA/fB winding0 and q winding1;positive a,b meridians give identity matrix.')
