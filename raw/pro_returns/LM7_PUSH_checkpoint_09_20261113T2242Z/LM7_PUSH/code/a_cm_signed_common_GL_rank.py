#!/usr/bin/env python3
"""Reproducible rank audit of all six retained signed-source characters."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np

HERE=Path(__file__).resolve().parent
p=HERE/'a_cm_signed_common_GL.json'
j=json.loads(p.read_text())
a=np.asarray(j['old44_to_six_actual_signs'],dtype=np.uint8)
assert a.shape==(6,44)
b=a.copy();pivots=[];r=0
for c in range(44):
    k=next((i for i in range(r,6) if b[i,c]),None)
    if k is None:continue
    b[[r,k]]=b[[k,r]]
    for i in range(6):
        if i!=r and b[i,c]:b[i]^=b[r]
    pivots.append(c);r+=1
assert r==5
out={'status':'PASS_SIX_INDUCED_SIGN_MAP_RANK','input_sha256':sha256(p.read_bytes()).hexdigest(),
     'shape':[6,44],'rank':r,'pivot_columns':pivots,'reduced_rows':b.tolist(),
     'all_six_sign_coordinates_retained':True}
(HERE/'a_cm_signed_common_GL_rank.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
