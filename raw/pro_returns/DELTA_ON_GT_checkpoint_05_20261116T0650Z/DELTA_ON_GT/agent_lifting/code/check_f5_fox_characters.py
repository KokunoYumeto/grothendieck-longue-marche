"""Independent orientation check for all 1024 fourth-root Fox blocks.

F9 is encoded a+3b for a+b*i, i^2=-1.  Checks all six boundary
identities and both inverse block identities at every character.
"""
from pathlib import Path
from itertools import product
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'records'/'f5_nielsen_fox.json').read_text())
add=np.array([[(a%3+b%3)%3+3*((a//3+b//3)%3)for b in range(9)]for a in range(9)],dtype=np.int64)
mul=np.array([[((a%3)*(b%3)-(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)for b in range(9)]for a in range(9)],dtype=np.int64)
neg=np.array([(-a%3)%3+3*(-(a//3)%3)for a in range(9)],dtype=np.int64)
ipow=(1,3,2,6)
I=np.eye(5,dtype=np.int64)
def mm(A,B):
    C=np.zeros((A.shape[0],B.shape[1]),dtype=np.int64)
    for k in range(A.shape[1]):C=add[C,mul[A[:,k,None],B[k,None,:]]]
    return C
def evaluate(name,chi):
    J=np.zeros((5,5),dtype=np.int64)
    for i,row in enumerate(D['fox_abelianized'][name]):
        for j,terms in enumerate(row):
            value=0
            for t in terms:
                exponent=sum(a*b for a,b in zip(chi,t['monomial']))%4
                value=int(add[value,mul[t['coefficient']%3,ipow[exponent]]])
            J[i,j]=value
    return J
def drow(chi):return np.array([[add[ipow[c],2]for c in chi]],dtype=np.int64)
characters=list(product(range(4),repeat=5))
for chi in characters:
    row=np.array(chi,dtype=np.int64)
    for name in('a','b','c','a_inv','b_inv','c_inv'):
        invname=name[:-4]if name.endswith('_inv')else name+'_inv'
        Tinv=np.array(D['abelianization_matrices'][invname],dtype=np.int64)
        eta=tuple(map(int,row@Tinv%4))
        J=evaluate(name,eta)
        assert np.array_equal(mm(drow(eta),J),drow(chi))
        Jinv=evaluate(invname,chi)
        assert np.array_equal(mm(Jinv,J),I)
        assert np.array_equal(mm(J,Jinv),I)
out={'field':'F9=F3[i], i^2=-1; encoding a+3b',
     'character_count':1024,'full_chain_block_dimension':5,
     'all_6144_Fox_boundary_identities_checked':True,
     'all_12288_inverse_block_products_checked':True,
     'source_to_target':'eta=chi*T_inverse mod4',
     'block_evaluation':'J_alpha(eta), with rows derivative variables and columns generator images',
     'scope':'Exact orientation/invertibility audit of the full chain representation, not a pentagon implication.'}
(ROOT/'records'/'f5_fox_characters.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
