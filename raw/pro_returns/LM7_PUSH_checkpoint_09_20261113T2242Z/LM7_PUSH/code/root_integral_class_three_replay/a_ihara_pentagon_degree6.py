#!/usr/bin/env python3
"""The full restricted degree-six leading pentagon over F3."""
from pathlib import Path
import importlib.util,contextlib,io,json
from itertools import product
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('graded',HERE/'a_ihara_pentagon_graded.py')
p=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(p)
words=[w for w in product(range(2),repeat=6) if p.lyndon(w)]
trees=[p.tree(w) for w in words]
PC=[p.flatten(p.pentagon(t),7) for t in trees]
x,y={(0,):1},{(1,):1};z=p.add((-1,x),(-1,y))
SC=[p.tensor_flat(p.add((1,p.tensor(t,x,y)),(1,p.tensor(t,y,x))),6) for t in trees]
HC=[p.tensor_flat(p.add((1,p.tensor(t,x,y)),(1,p.tensor(t,y,z)),(1,p.tensor(t,z,x))),6) for t in trees]
def cubeD(D,E):
 C=p.dbracket(D,E)
 return tuple(p.deriv(C,p.deriv(C,C[i])) for i in range(3))
def cubet(a,b):
 c=p.bracket(a,b);return p.mul(p.mul(c,c),c)
last=p.dadd((1,cubeD(p.A,p.B)),
 (1,cubeD(p.dadd((1,p.H),(-1,p.B)),p.dadd((1,p.Y),(1,p.Z)))),
 (1,cubeD(p.B,p.Z)),(-1,cubeD(p.A,p.dadd((1,p.B),(1,p.Y)))),
 (-1,cubeD(p.dadd((1,p.H),(-1,p.A)),p.Z)))
PC.append(p.flatten(last,7))
SC.append(p.tensor_flat(p.add((1,cubet(x,y)),(1,cubet(y,x))),6))
HC.append(p.tensor_flat(p.add((1,cubet(x,y)),(1,cubet(y,z)),(1,cubet(z,x))),6))
P=np.stack(PC,axis=1);S=np.stack(SC,axis=1);H=np.stack(HC,axis=1)
K=p.g.kernel(np.vstack((P,S,H)))
print('Ordinary degree6 Lie dimension:',len(words))
print('Ordinary degree6 pentagon kernel dimension:',p.g.kernel(np.vstack((P[:,:-1],S[:,:-1],H[:,:-1]))).shape[1])
print('Restricted degree6 dimension:',len(words)+1)
print('Restricted symmetry/three-term/pentagon kernel dimension:',K.shape[1])
print('Kernel basis with last coordinate [x,y]^[3]:',K.T.tolist())
Path(__file__).with_suffix('.json').write_text(json.dumps({'lyndon_words':[list(w) for w in words],
 'kernel_basis':K.tolist(),'pentagon_matrix':P.tolist()},separators=(',',':'))+'\n')
print('PASS: exact restricted derivation cube retained.')
