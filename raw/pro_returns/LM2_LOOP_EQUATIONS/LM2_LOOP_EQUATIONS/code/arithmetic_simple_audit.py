#!/usr/bin/env python3
"""Exhaustively verify the automorphism and power-class inputs for simple shadows."""
from pathlib import Path
from math import gcd
import json
from finite_groups import permutation_group,matrix_group,matmul

out=[]
for G in [permutation_group(5,even=True),matrix_group(7,projective=True)]:
 pairs=G.generating_pairs();x,y=pairs[0]
 autos=[]
 for a,b in pairs:
  h=G.map_from_generators(x,y,a,b)
  if h is not None:
   assert len(set(h))==G.n
   autos.append(h)
 assert len(autos)==2*G.n
 assert len(set(G.classes[a] for a,b in pairs))==len(set(G.classes))-1
 units=[k for k in range(G.exponent) if gcd(k,G.exponent)==1]
 kernel=[k for k in units if all(G.classes[G.power(a,k)]==G.classes[a] for a in range(G.n))]
 if G.name=='A5':
  p=(1,0,2,3,4)
  outer=tuple(G.index[tuple(p[a[p[i]]] for i in range(5))] for a in G.elements)
 else:
  d=(3,0,0,1);di=(5,0,0,1)
  canon=lambda a:min(a,tuple(-z%7 for z in a))
  outer=tuple(G.index[canon(matmul(matmul(d,a,7),di,7))] for a in G.elements)
 assert outer in autos and outer not in [tuple(c) for c in G.conj]
 assert all(outer[outer[a]]==a for a in range(G.n)) if G.name=='A5' else True
 out.append({'group':G.name,'group_order':G.n,'generating_pairs':len(pairs),
             'automorphism_group_order':len(autos),'outer_automorphism_group_order':len(autos)//G.n,
             'specified_outer_automorphism_verified':True,'all_nontrivial_classes_generate_with_a_mate':True,
             'exponent':G.exponent,'power_class_kernel':kernel,'power_class_index':len(units)//len(kernel)})
path=Path(__file__).resolve().parent
(path/'arithmetic_simple_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
