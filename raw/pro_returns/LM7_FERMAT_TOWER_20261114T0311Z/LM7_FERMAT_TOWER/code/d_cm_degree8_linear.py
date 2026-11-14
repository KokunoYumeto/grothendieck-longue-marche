#!/usr/bin/env python3
"""All central degree-eight corrections of the exact D31 lower action.

The correction group is D8(K)/D9(K), the full restricted Lie degree eight.
The actual cusp error is read from the direct-word certificate. A multiplier
change by144 preserves the old finite shadow multiplier and contributes the
nonzero t48 column at this degree. Lower-conjugator changes are not tested.
"""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import product
import io,runpy,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))

# Verify that the entire degree-eight kernel fixes retained G2 homology.
Q,qm,one=R['Q'],R['qm'],R['one'];CN=R['CN'];chN=R['chN'];ix=R['ixQ']
chordN={j:i for i,j in enumerate(chN)}
def hom(word):
    q=one;v=0
    for a in word:
        if a==0:q=qm(q,R['qs'])
        else:
            qq=qm(q,R['qr'] if a==1 else R['qr2'])
            for j in (ix[q],ix[qq]):
                if j in chordN:v^=1<<chordN[j]
            q=qq
    return q,v
def mat(q):
    a=np.zeros_like(CN);a[[ix[qm(q,x)] for x in Q]]=CN
    b=a[chN]%2
    return [sum(int(x)<<i for i,x in enumerate(b[:,j])) for j in range(97)]
def apply(v,M):
    z=0
    while v:
        bit=v&-v;z^=M[bit.bit_length()-1];v^=bit
    return z
MK=[]
for w in R['Kwords']:
    q,v=hom(w);MK.append(mat(q))
g3=[]
for i,j,k in product(range(4),repeat=3):
    w=R['comm'](R['Kwords'][i],R['comm'](R['Kwords'][j],R['Kwords'][k]))
    q,v=hom(w);assert q==one;g3.append(v)
bas=R['echelon'](g3)
while True:
    new=R['echelon']([v[0] for v in bas.values()]+[apply(v[0],M) for v in bas.values() for M in MK])
    if len(new)==len(bas):break
    bas=new
ranks={3:len(bas)}
for k in range(4,10):
    bas=R['echelon']([v[0]^apply(v[0],M) for v in bas.values() for M in MK]);ranks[k]=len(bas)
print('Ordinary lower-central homology ranks:',ranks,flush=True)
assert ranks[8]==0
# The other restricted terms in degree8 are fourth powers of degree2,
# squares of degree4, and eighth powers of degree1. They vanish because
# their half-powers already belong to the exponent-two kernel N/Phi(N).
for w in R['Kwords']:
    q,v=hom(w*4);assert q==one
for i in range(4):
    for j in range(i):
        q,v=hom(R['comm'](R['Kwords'][i],R['Kwords'][j])*2);assert q==one

L8=[w for w in product(range(4),repeat=8) if R['lyndon'](w)]
L4=[w for w in product(range(4),repeat=4) if R['lyndon'](w)]
L2=[w for w in product(range(4),repeat=2) if R['lyndon'](w)]
Z=[R['lie'](w) for w in L8];labels=[(w,1) for w in L8]
for words,power in [(L4,2),(L2,4),([(i,) for i in range(4)],8)]:
    for w in words:
        p=R['lie'](w);n=len(w);j=1
        while j<power:p=R['mulpoly'](p,p,n);n*=2;j*=2
        Z.append(p);labels.append((w,power))
assert len(Z)==8230

def action(v,M):
    a=R['arraypoly'](v,8).reshape((4,)*8)
    for axis in range(8):
        x=np.moveaxis(a,axis,0);y=np.zeros_like(x)
        for i in range(4):
            for j in np.flatnonzero(M[i]):y[i]^=x[j]
        a=np.moveaxis(y,0,axis)
    return R['bitpoly'](np.ascontiguousarray(a).reshape(-1))

bas={};source_columns=0
def add(v,cert):
    while v:
        k=v.bit_length()-1
        if k not in bas:bas[k]=(v,cert);return
        v^=bas[k][0];cert^=bas[k][1]

for j,z in enumerate(Z):
    s=action(z,R['MS']);sr=action(z,R['MSR'])
    add(z^s,1<<j);add(s^sr,1<<(len(Z)+j))
    if j and j%1000==0:print('Central basis',j,'of8230; rank',len(bas),flush=True)
rank_without=len(bas)
data=json.loads((OUT/'d_cm_degree8_seed.json').read_text())
target=int(data['degree8_target'],16);mult=int(data['t48_degree8_column'],16)
good0,sol0,rem0=R['solve'](target,bas)
add(mult,1<<(2*len(Z)))
good,sol,rem=R['solve'](target,bas)
summary={'restricted_degree8_dimension':len(Z),
 'ordinary_K_lower_central_image_in_Nab2_ranks':ranks,
 'all_central_degree8_corrections_fix_G2_homology':True,
 'fixed_conjugator_correction_rank':rank_without,'fixed_conjugator_lift':good0,
 'rank_with_multiplier144':len(bas),'lift_with_multiplier144':good,
 'multiplier144_is_t48_in_this_layer':True,
 'scope':'Only central corrections to the exact recorded lower conjugators; arbitrary lower centralizer freedom and C1 replacement are not exhausted.',
 'elapsed_seconds':round(time.time()-started,3)}
payload={'summary':summary,'without_multiplier_remainder':hex(rem0),
 'with_multiplier_remainder':hex(rem),'solution':hex(sol) if good else None,
 'basis_labels':[[list(w),power] for w,power in labels]}
(OUT/'d_cm_degree8_linear.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
