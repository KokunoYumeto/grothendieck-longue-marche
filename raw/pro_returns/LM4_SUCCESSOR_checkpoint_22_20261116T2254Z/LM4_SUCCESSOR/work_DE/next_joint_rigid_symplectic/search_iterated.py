"""Search actual full rigid kernels from exact two-moving-point relations."""
from pathlib import Path
import json,itertools,sys
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import reduce_word as red,inverse as inv,multiply as mul,substitute,artin
j=json.loads((HERE/'rigid_restrictions.json').read_text())
words={k:{int(i)+1:tuple(r['braid']) for i,r in f.items()} for k,f in j['families'].items()}
p=101;n=6;eye=np.eye(n,dtype=np.int64);gens={}
for i in range(1,n):
 M=eye.copy();M[i-1:i+1,i-1:i+1]=[[-1,2],[1,0]];gens[i]=M%p
 N=eye.copy();N[i-1:i+1,i-1:i+1]=[[0,1],[51,51]];gens[-i]=N%p
def ev(w):
 M=eye.copy()
 for a in w:M=M@gens[a]%p
 return M
def comm(a,b):return mul(a,b,inv(a),inv(b))
results=[]
for i,j0 in itertools.combinations(range(1,7),2):
 h=comm((i,),(j0,))
 for k in range(1,7):
  w=comm(h,(k,))
  for name in words:
   v=substitute(w,words[name])
   if not np.array_equal(ev(v),eye):continue
   A=artin(v)
   if A==tuple((i,) for i in range(1,7)):
    rec={'name':name,'source_word':w,'braid_length':len(v),'Artin_lengths':[len(x) for x in A]};results.append(rec)
    print('EXACT FULL RIGID KERNEL',rec,flush=True)
(HERE/'iterated_kernel_search.json').write_text(json.dumps(results,indent=2)+'\n')
print('Total exact successes',len(results),flush=True)
