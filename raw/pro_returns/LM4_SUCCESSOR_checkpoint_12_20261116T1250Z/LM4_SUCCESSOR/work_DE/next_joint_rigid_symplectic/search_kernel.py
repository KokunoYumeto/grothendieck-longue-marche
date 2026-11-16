"""Exploratory exact braid-kernel search, using finite matrices only to filter.

Any reported identity is independently checked by the faithful Artin
action. A failed finite filter is only a nonidentity test.
"""
from pathlib import Path
import json,itertools,sys,time
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import reduce_word,inverse,multiply,substitute,artin
j=json.loads((HERE/'rigid_restrictions.json').read_text())
words={k:{int(i)+1:tuple(r['braid']) for i,r in f.items()} for k,f in j['families'].items()}
p=101;n=6;eye=np.eye(n,dtype=np.int64);gens={}
for i in range(1,n):
 M=eye.copy();M[i-1:i+1,i-1:i+1]=[[-1,2],[1,0]];gens[i]=M%p
 N=eye.copy();N[i-1:i+1,i-1:i+1]=[[0,1],[51,51]];gens[-i]=N%p
 assert np.array_equal(gens[i]@gens[-i]%p,eye)
def ev(w):
 M=eye.copy()
 for a in w:M=M@gens[a]%p
 return M
mats={k:{i:ev(w) for i,w in ws.items()} for k,ws in words.items()}
def sev(w,name):
 M=eye.copy()
 for a in w:M=M@mats[name][a]%p
 return M
def test(a,b,names):
 for name in names:
  A=sev(a,name);B=sev(b,name)
  if not np.array_equal(A@B%p,B@A%p):return False
 w=multiply(a,b,inverse(a),inverse(b))
 if not w:return False
 out={}
 for name in names:
  ims=words[name]
  v=substitute(w,ims);A=artin(v)
  out[name]={'braid_length':len(v),'Artin_lengths':[len(x) for x in A],'identity':A==tuple((i,) for i in range(1,7))}
  print('Artin candidate',a,b,name,out[name],flush=True)
 if all(x['identity'] for x in out.values()):
  record={'source_word':w,'a':a,'b':b,'Artin':out}
  (HERE/('cyclic_rigid_kernel_witness_'+'_'.join(names)+'.json')).write_text(json.dumps(record,indent=2)+'\n')
  print('FOUND EXACT KERNEL',names,record,flush=True);return True
 return False

# Source indices here are original f0,...,f5 shifted to1,...,6.
for names in [('plus',),('minus',),('plus','minus')]:
 for perm in itertools.permutations(range(1,7)):
  if test((1,),perm,names):break
 else:print(names,'no commutator of f0 with a positive six-meridian permutation lies in these kernels',flush=True)
 for perm in itertools.permutations((1,3,6)):
  if test((2,),perm,names):break
 else:print(names,'no [f1, positive permutation of f0 f2 f5] lies in these kernels',flush=True)
