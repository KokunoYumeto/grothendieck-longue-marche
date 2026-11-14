#!/usr/bin/env python3
"""Explicit original-generator gate for the complete lifted presentations."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np
from de_a6_schreier_certificate import read_certificate

HERE=Path(__file__).resolve().parent
records=[]
for name in ('de_a6_a5_common_source.bin','de_a6_gl_lower_chain.bin'):
    raw=(HERE/name).read_bytes();d=read_certificate(HERE/name)
    assert not d['derived'] and len(d['original'])==2
    found=[]
    for j in range(2):
        assert tuple(d['nodes'][j+1])==(1,j,0)
        where=np.flatnonzero(d['words']==j+1)
        assert len(where)==1
        assert np.array_equal(d['strong'][where[0]],d['original'][j])
        found.append(int(where[0]))
    records.append({'certificate':name,'sha256':sha256(raw).hexdigest(),
                    'original_word_nodes':[1,2],
                    'literal_original_strong_generator_indices':found,
                    'both_original_generators_retained':True})
out={'status':'PASS_EXACT_PRESENTATION_GATE','records':records,
     'consequence':'The actual strong lifts generate exactly the original source image; complete stabilizer relations therefore bound its quotient by the exact base order.'}
(HERE/'de_a6_gl_presentation_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
