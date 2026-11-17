"""Actual common-base Burau(-1) matrices modulo3, projectively.

Exploratory finite quotient stage; no claim about lifting its common
image into the full profinite centralizer is made.
"""
from pathlib import Path
import json,itertools
import numpy as np
import sympy as s
HERE=Path(__file__).resolve().parent
data=json.loads((HERE.parent/'next_B59_image/common_base_braid_words.json').read_text())
n=11;p=3;eye=np.eye(10,dtype=np.int64)
gens={}
J=np.array([[0 if i==j else ((-1)**(j-i+1) if i<j else -(-1)**(i-j+1)) for j in range(10)] for i in range(10)],dtype=np.int64)
assert s.Matrix(J).det()==1
for j in range(1,n):
    B=np.eye(n,dtype=np.int64);B[j-1:j+1,j-1:j+1]=[[2,-1],[1,0]]
    integral=B[:10,:10]-B[10,:10]
    assert np.array_equal(integral.T@J@integral,J)
    M=integral%p
    assert np.array_equal(M@M@M%p,eye)
    gens[j]=M;gens[-j]=M@M%p
for i in range(1,10):
    assert np.array_equal(gens[i]@gens[i+1]@gens[i]%p,gens[i+1]@gens[i]@gens[i+1]%p)
for i in range(1,11):
    for j in range(i+2,11):assert np.array_equal(gens[i]@gens[j]%p,gens[j]@gens[i]%p)
def evaluate(w):
    M=eye.copy()
    for j in w:M=M@gens[j]%p
    return M
full_twist=evaluate(list(range(1,11))*11)
assert np.array_equal(full_twist,2*eye)
def projective(M):
    first=next(int(x) for x in M.flat if x)
    return M*first%p
def inv(M):return np.array(__import__('sympy').Matrix(M).inv_mod(p)).astype(np.int64)
def comm(A,B):return A@B@inv(A)@inv(B)%p
families={k:{int(i):evaluate(w) for i,w in data[k].items()} for k in ('T','C5')}
T,F=families['T'],families['C5']
h=T[6]@T[11]@inv(T[6])@inv(T[5])%p
b0=eye.copy()
for i,j,c in [(0,1,-2),(0,2,-1),(0,3,-1),(0,4,-1),(0,5,-1),(1,2,1),(1,5,1)]:
    Z=comm(F[i],F[j])
    if c<0:Z=inv(Z);c=-c
    for _ in range(c):b0=b0@Z%p
record={'prime':p,'dimension':10,'base_order':data['initial_order_labels'],
        'integral_symplectic_form':J.tolist(),'symplectic_form_determinant':1,'full_twist_matrix':full_twist.tolist(),
        'families':{k:{str(i):M.tolist() for i,M in v.items()} for k,v in families.items()},
        'h_matrix':h.tolist(),'b0_matrix':b0.tolist(),
        'scope':'Actual finite projective homology representation; no full intersection lift.'}
(HERE/'matrices.json').write_text(json.dumps(record,indent=2)+'\n')
with (HERE/'matrices.txt').open('w') as out:
    for k in ('T','C5'):
        out.write(str(len(families[k]))+'\n')
        for i,M in sorted(families[k].items()):out.write(' '.join(str(int(x)) for x in M.flat)+'\n')
    for M in (h,b0):out.write(' '.join(str(int(x)) for x in M.flat)+'\n')
print('PASS exact Burau braid/inverse relations; actual13+6 common-base words evaluated modulo3')
print('PASS integral unimodular alternating form; full twist maps to-I and is killed projectively')
print('h and b0 projective matrices equal:',np.array_equal(projective(h),projective(b0)))
print('Matrices saved; finite subgroup computation follows separately.')
