#!/usr/bin/env python3
"""Compare every independent quaternary replay array with the retained originals."""
from pathlib import Path
import json
import numpy as np
HERE=Path(__file__).resolve().parent
OTHER=HERE.parent/'centralizer_mod4'
names=('lift_mask31_mod4','check_modular_quaternary_central_model',
       'check_mod4_canonical_lift','check_selected_mod4_automorphism')
counts={}
for name in names:
    a=np.load(HERE/(name+'.npz'));b=np.load(OTHER/(name+'.npz'))
    assert set(a.files)==set(b.files),(name,set(a.files)^set(b.files))
    for k in a.files:assert np.array_equal(a[k],b[k]),(name,k)
    counts[name]=len(a.files)
    print('PASS exact independent array replay',name,len(a.files),flush=True)
out={'scope':'All independent modulus-four canonical and automorphism replay arrays.',
     'array_counts':counts,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
