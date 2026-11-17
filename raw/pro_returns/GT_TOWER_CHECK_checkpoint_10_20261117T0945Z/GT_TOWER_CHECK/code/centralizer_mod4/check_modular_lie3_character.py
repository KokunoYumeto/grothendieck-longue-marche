#!/usr/bin/env python3
"""Exact rational degree-three character of the actual modular relation module.
This is a rational representation calculation, not a canonical obstruction computation.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
import numpy as np
HERE=Path(__file__).resolve().parent
src=HERE.parent/'ghost_mod4_review/check_modular_wedge_character.npz'
p=np.load(src);t=p['group_table'];c=p['relation_module_character'].astype(object)
g=np.arange(576);g3=t[t[g,g],g]
a=c**3-c[g3]
assert all(int(v)%3==0 for v in a)
chi=a//3
assert int(sum(chi))%576==0
rank=int(sum(chi))//576
assert rank==512 and int(chi[0])==304192
out={'scope':'Rational coinvariants of the actual rank97 free Lie degree3 module; no finite obstruction or lifting conclusion.',
 'group_order':576,'ambient_dimension':304192,'rational_coinvariant_dimension':rank,
 'character_distribution':dict(Counter(map(int,chi))),
 'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'all_assertions_passed':True}
np.savez_compressed(Path(__file__).with_suffix('.npz'),group_cubes=g3,character=np.array(chi,dtype=np.int64))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
