#!/usr/bin/env python3
"""Independent low-degree enumeration audit of binary group collection."""
from pathlib import Path
import json,time
from de_ferrari_two_model import FerrariTwo,exact_orders
from de_ferrari_two_generation import Collector,kernel_generators

start=time.time();rows=[]
for degree in (2,3,4):
    H=FerrariTwo(degree);unit_order,automorphism_order=exact_orders(H)
    C=Collector(H).close(kernel_generators(H));C.verify()
    assert 6*2**len(C.basis)==unit_order*automorphism_order
    row={'degree':degree,'complete_enumerated_free_kernel_order':unit_order,
        'complete_enumerated_automorphism_order':automorphism_order,
        'polycyclic_normal_kernel_length':len(C.basis),
        'same_actual_four_strand_order':unit_order*automorphism_order}
    rows.append(row);print(json.dumps(row),flush=True)
out={'records':rows,'all_full_enumerations_agree_with_exact_collection':True,
    'elapsed_seconds':round(time.time()-start,3)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
