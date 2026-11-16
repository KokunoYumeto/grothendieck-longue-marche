"""Linear translation constraints, with actual frames still to be supplied.

Rebuilds the independent characteristic-two certificate, then computes
only the homogeneous ambiguity after all E[3] translations.  It never
sets their inhomogeneous path classes to zero.
"""
import contextlib
import io
import runpy
import numpy as np
from collections import Counter

with contextlib.redirect_stdout(io.StringIO()):
    c=runpy.run_path('deliverable/code/b_char2_symmetry.py')
M=c['MOD'];U=c['U'];coords=c['expected'];D=c['D'];Pi=c['Pi']
lie3=c['lie3'];pivcols=c['pivcols'];inverse=c['inverse_unit'];smith=c['smith_transport']
index={x:i for i,x in enumerate(coords)}
Ts=[];LTs=[]
for shift in [(1,0),(0,1)]:
    P=np.zeros((8,8),dtype=np.int64)
    for j,(a,b) in enumerate(coords):
        target=((a+shift[0])%3,(b+shift[1])%3)
        if target==(0,0):P[:,j]=-1
        else:P[index[target],j]=1
    raw=U-P@U
    assert not np.any(raw%3)
    T=np.zeros((10,10),dtype=np.int64)
    T[:2,:2]=np.eye(2,dtype=np.int64);T[2:,2:]=P;T[2:,:2]=raw//3
    T%=M
    assert np.array_equal(T@T%M@T%M,np.eye(10,dtype=np.int64))
    L=lie3(T)
    assert not np.any((L@D-D@L)%M)
    Ts.append(T);LTs.append(L)
assert not np.any((Ts[0]@Ts[1]-Ts[1]@Ts[0])%M)
print('Both actual translation matrices reconstructed; order3, commutation and Frobenius compatibility: PASS')

# Coinvariants of the dual under Q8 equal its invariant direct summand.
Pid=Pi.T
cols=pivcols(Pid);assert len(cols)==41
Ed=Pid[:,cols]
rows=pivcols(Ed.T);assert len(rows)==41
inv=inverse(Ed[rows,:])
Dd=inv@(D.T@Ed%M)[rows,:]%M
assert not np.any((Ed@Dd-D.T@Ed)%M)
relations=[Dd]
for g in [c['LR'],c['R2']]+LTs:
    rel=(Pid@(g.T-np.eye(330,dtype=np.int64)))%M
    relations.append(inv@rel[rows,:]%M)
vals,Q=smith(np.hstack(relations))
hist=dict(sorted(Counter(vals).items()))
print('Full translation+Aut(E,O)+Frob2 homogeneous ambiguity Smith valuations:',hist)
print('Order exponent:',sum(vals),'largest elementary-divisor exponent:',max(vals))
print('The actual translation path terms remain inhomogeneous data; this output does not assert an eta value.')
np.savez_compressed('deliverable/code/b_char2_translation_linear_matrices.npz',modulus=np.array([M]),translations=np.stack(Ts),Lie_translations=np.stack(LTs),dual_invariant_basis=Ed,dual_invariant_rows=np.array(rows),dual_D=Dd,relations=np.hstack(relations),Smith_rows=Q)
