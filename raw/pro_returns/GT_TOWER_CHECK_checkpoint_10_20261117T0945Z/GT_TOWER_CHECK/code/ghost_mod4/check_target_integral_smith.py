#!/usr/bin/env python3
"""Exact integral Smith invariants of the actual five-point cover relation map."""
from pathlib import Path
import json
import numpy as np
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent
z=np.load(HERE/'check_fivepoint_quartic_mixed_module.npz')
R=z['target_relation_matrix'].astype(np.int64)
assert R.shape==(1152,769)
print('Starting exact integral Smith reduction of the actual1152x769 relation matrix.',flush=True)
S=fmpz_mat(R.tolist()).snf()
diagonal=[int(S[i,i]) for i in range(769)]
nonzero=[abs(a) for a in diagonal if a]
assert all(nonzero[i+1]%nonzero[i]==0 for i in range(len(nonzero)-1))
out={'relation_shape':list(R.shape),'rank':len(nonzero),
     'free_rank':769-len(nonzero),'nontrivial_torsion':[a for a in nonzero if a!=1],
     'unit_invariants':nonzero.count(1),'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),relation_matrix=R,
                    smith_diagonal=np.array(diagonal,dtype=np.int64))
print(json.dumps(out,indent=2),flush=True)
