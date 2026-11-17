#!/usr/bin/env python3
"""Compare independent replay outputs with all original canonical certificates."""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
ORIGINAL=HERE.parent/'centralizer_code'
checks=[]
for name in [
    'check_modular_binary_central_obstruction',
    'check_common_mod6_liftable_automorphism',
    'check_common_mod6_canonical_correction',
]:
    a=np.load(HERE/('review_'+name+'.npz'))
    b=np.load(ORIGINAL/(name+'.npz'))
    assert set(a.files)==set(b.files)
    for key in a.files:
        assert np.array_equal(a[key],b[key]),(name,key)
    checks.append({'program':name,'arrays':len(a.files),
                   'exact_array_equality':True})
out={'independent_replays_passed':True,'checks':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
