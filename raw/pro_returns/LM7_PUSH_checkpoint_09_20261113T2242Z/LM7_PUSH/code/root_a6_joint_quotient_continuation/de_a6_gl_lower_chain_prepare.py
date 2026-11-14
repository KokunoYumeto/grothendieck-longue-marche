#!/usr/bin/env python3
"""Prepare the exact lower joint source for a complete C++ order replay."""
from pathlib import Path
import json,struct
import numpy as np
from de_ferrari_a6_kernel_source import compress

HERE=Path(__file__).resolve().parent
A=np.load(HERE/'de_ferrari_a6_perm_source_compressed.npz')
B=np.load(HERE/'de_ferrari_a5_source_compressed.npz')
na=len(A['s'])
ps,metadata=compress(np.r_[A['s'],na+B['s']],np.r_[A['r'],na+B['r']])
sizes=metadata['retained_orbit_sizes'];starts=np.r_[0,np.cumsum(sizes)]
order=sorted(range(len(sizes)),key=lambda i:sizes[i],reverse=True)
points=np.concatenate([np.arange(starts[i],starts[i+1]) for i in order])
inverse=np.argsort(points);ps=inverse[ps[:,points]]
np.savez_compressed(HERE/'de_a6_gl_lower_chain.npz',s=ps[0],r=ps[1],point_order=points,point_order_inverse=inverse)
with (HERE/'de_a6_gl_lower_chain.input').open('w') as f:
    f.write(f'{len(points)} 2\n')
    for p in ps:f.write(' '.join(map(str,p))+'\n')
raw=(HERE/'de_a6_gl_model.bin').read_bytes();tail=8+2*11010*2
assert struct.unpack_from('<II',raw,len(raw)-tail)==(11010,2)
(HERE/'de_a6_gl_lower_chain_model.bin').write_bytes(raw[:-tail]+struct.pack('<II',len(points),2)+ps.astype('<u2').tobytes())
metadata['status']='PASS_EXACT_PREPARATION'
(HERE/'de_a6_gl_lower_chain_prepare.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps({'status':metadata['status'],'degree':len(points)}))
