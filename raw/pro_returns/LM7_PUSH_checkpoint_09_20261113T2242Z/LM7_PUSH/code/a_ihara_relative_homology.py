#!/usr/bin/env python3
"""Exact relative Fermat homology comparison with the actual Kummer row.

The real edge beta runs from (0,1) to (1,0) in u^3+v^3=1.
x around0 contributes no edge after filling the six finite cusps;
y at sheet(a,b) contributes beta_(a,b)-beta_(a,b+1).
The arithmetic B matrix is Davis--Pries--Stojanoska--Wickelgren,
Theorem1.1 and Lemma5.5, with (c0,c1)=(kappa(zeta),kappa(1-zeta^-1)).
The Ihara convention g(y)=f^-1*y^chi*f gives f=beta*(g beta)^-1,
hence its relative chain is 1-B. Both signs are printed for audit.
"""
from pathlib import Path
import importlib.util,json
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)

def chain(word):
    a=b=0;out=np.zeros((3,3),dtype=np.int64)
    for l in word:
        step=1 if l>0 else -1
        if abs(l)==1:a=(a+step)%3
        else:
            out[a,b]+=1;b=(b+step)%3;out[a,b]-=1
    assert (a,b)==(0,0)
    return out.reshape(-1)%3

R=np.stack([chain(w) for w in f.NWORDS],axis=1)
assert f.rank(R)==4
# Frob7 at zeta=2: kappa(zeta)=2, kappa(1-zeta)=0,
# 1-zeta^-1=-zeta^2*(1-zeta), so the second row is1.
c0,c1=2,1
B=np.zeros((3,3),dtype=np.int64)
B[0,0]=(1+c0-c0*c0)%3
B[0,1]=B[1,0]=(c1-c0*c0)%3
B[1,1]=(-c1-c0*c0)%3
B[0,2]=B[2,0]=(1-B[0,0]-B[0,1])%3
B[1,2]=B[2,1]=(-B[1,0]-B[1,1])%3
B[2,2]=(-B[2,0]-B[2,1])%3
unit=np.zeros(9,dtype=np.int64);unit[0]=1
target=(unit-B.reshape(-1))%3
raw=json.loads((HERE/'a_ihara_pentagon_compare.json').read_text())
print('Theorem1.1 B_Frob7=',B.tolist())
print('Actual f relative chain 1-B=',target.reshape(3,3).tolist())
selected=[]
for row in raw['branches']:
    fa=np.array(row['fa'],dtype=np.int64);got=R@fa%3
    yes=np.array_equal(got,target)
    minus=np.array_equal(got,-target%3)
    print('Branch',row['branch'],'relative chain',got.reshape(3,3).tolist(),
          'matches actual convention',yes,'matches opposite sign',minus)
    if yes:selected.append(row['branch'])
print('Selected branches:',selected)
out={'relative_chain_map':R.tolist(),'B_Frob7':B.tolist(),'target_1_minus_B':target.tolist(),
     'selected_branches':selected,'Kummer_row':[c0,c1]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact chain calculation; the stated based Ihara convention is retained.')
