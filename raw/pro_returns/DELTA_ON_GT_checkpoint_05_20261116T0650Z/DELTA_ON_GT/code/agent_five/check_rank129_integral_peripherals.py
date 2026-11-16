"""Integral quasi-unipotence of all rank129 affine pentagon peripherals.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
Translation coordinates are scaled by256, a unit at every odd prime.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
D=np.load(ROOT/'ferrari_rank129_integral.npz');n=130;I=np.eye(n,dtype=np.int64)
def augment(M,v):
    A=I.copy();A[:129,:129]=M;A[:129,129]=v;return A
abc=[augment(D[k],D['translation_numerators'][i])for i,k in enumerate(('A','B','C'))]
def power(A,k):
    R=I
    while k:
        if k&1:R=R@A
        A=A@A;k//=2
    return R
A,B,C=abc
X=[A@A,B@B,C@C,power(A@B@A,2),power(C@B@C,2)]
records=[];inverses=[]
for i,M in enumerate(X):
    e=2 if i<3 else 4;N=power(M,e)-I
    assert not np.any(N@N)
    Mi=power(M,e-1)@(I-N)
    assert np.array_equal(M@Mi,I)and np.array_equal(Mi@M,I)
    inverses.append(Mi)
    records.append({'Xi':i+1,'two_power':e,'square_zero_unipotent_difference':True,
                    'max_absolute_difference_entry':int(np.max(np.abs(N)))})
pairs=[]
for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    z=inverses[j]@inverses[i]
    found=None
    for e in (1,2,4,8):
        N=power(z,e)-I
        if not np.any(N@N):found=e;break
    assert found
    pairs.append({'pair':[i+1,j+1],'third_peripheral_two_power':found,
                  'third_peripheral_square_zero_difference':True,
                  'max_absolute_difference_entry':int(np.max(np.abs(N)))})
np.savez_compressed(ROOT/'ferrari_rank129_integral_augmented.npz',A=A,B=B,C=C,X=np.stack(X),Xi_inverses=np.stack(inverses))
print(json.dumps({'coordinate_change':'multiply affine translation coordinates by256',
 'Xi_integral_quasi_unipotence':records,'pair_third_peripheral_checks':pairs,
 'exact_e3_formula':'If(g^m−I)^2=0 withm a powerof2, then g^e3=I+(g^m−I)/m overZ3.',
 'scope':'Exact integral polynomial identities, not extrapolation from a finite coefficient sample.'},indent=2))
