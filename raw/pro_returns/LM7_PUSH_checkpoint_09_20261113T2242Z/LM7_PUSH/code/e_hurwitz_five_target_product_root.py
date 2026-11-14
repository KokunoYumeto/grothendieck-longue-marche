#!/usr/bin/env python3
"""Literal right-action normal-closure word used in E46.27."""
from pathlib import Path
import json
from sympy.combinatorics import Permutation

c=Permutation(*range(1,12),size=96)
h=Permutation(1,12,13,size=96)
k=c*h*~c*~h
assert c.order()==11 and c.signature()==1 and h.signature()==1
assert k==Permutation(1,13,11,size=96)
target_order=2**117*3**36*5**31*7**2
assert target_order%11!=0
out={'right_action_commutator_cycle':k.cyclic_form,
     'c_order':int(c.order()),'all_permutations_even':True,
     'SL2_F5_Ferrari_target_order_has_no_factor11':True,
     'status':'PASS_EXACT_NORMAL_CLOSURE_WORD'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
