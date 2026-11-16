#!/usr/bin/env python3
"""Actual group-word certificate for D37's two degree-five quotient classes."""
from pathlib import Path
import json
import de_tame_hall as m

c=m.comm(m.x,m.y)
words=[m.comm(c,m.comm(m.x,c)),m.comm(c,m.comm(m.y,c))]
columns=[]
for w in words:
    assert all(not a for v,a in w.items() if 0<len(v)<5)
    col,rest=m.top_coordinates(w,5)
    assert not rest
    columns.append([int(z) for z in col])
assert columns==[[0,0,-1,0,0,0],[0,0,0,0,-1,0]]
# These two rows form a unit determinant minor over Z, hence also mod5.
minor=[[columns[j][i] for j in range(2)] for i in (2,4)]
assert minor==[[-1,0],[0,-1]]
out={'status':'actual group words checked exactly',
     'words':['[[x,y],[x,[x,y]]]','[[x,y],[y,[x,y]]]'],
     'Lyndon_degree5_columns':columns,
     'unit_minor':minor,'minor_determinant':1,
     'all_lower_terms_zero':True,
     'uniform_K_r_double_derived_bound_mod5':
         'K_r subset1+augmentation^2 implies K_rprime subset1+augmentation^4 and K_rdoubleprime subset1+augmentation^8 for everyr>=1'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
