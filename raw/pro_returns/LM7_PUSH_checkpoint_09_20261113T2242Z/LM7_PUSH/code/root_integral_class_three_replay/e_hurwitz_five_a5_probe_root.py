#!/usr/bin/env python3
"""Save the completed tuple action before the slow exact group-order step.

The order calculation in the original attempt remains running.  This
read-only diagnostic stops at that boundary and retains its input arrays.
No group order is asserted by this file.
"""
from pathlib import Path
import json,hashlib,time
import numpy as np
from sympy.combinatorics import PermutationGroup
import e_hurwitz_five_a5_root as original

class Captured(Exception):pass

def capture(self):
    h=Path(__file__).resolve().parent
    arrays=np.array([p.array_form for p in self.generators])
    np.savez_compressed(h/'e_hurwitz_five_a5_probe_root.npz',sigma=arrays)
    out={'degree':self.degree,'generators':len(self.generators),
         'generator_orders':[int(p.order()) for p in self.generators],
         'generator_cycle_types':[dict(p.cycle_structure) for p in self.generators],
         'orbits':[sorted(o) for o in self.orbits()],
         'order_not_computed':True,
         'source_sha256':hashlib.sha256(Path(original.__file__).read_bytes()).hexdigest()}
    (h/'e_hurwitz_five_a5_probe_root.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='orbits'},indent=2),flush=True)
    print('Orbit sizes',list(map(len,out['orbits'])),flush=True)
    raise Captured

PermutationGroup.order=capture
at=time.time()
try:original.build()
except Captured:print('PASS: complete tuple-action input captured in',round(time.time()-at,3),'seconds',flush=True)
