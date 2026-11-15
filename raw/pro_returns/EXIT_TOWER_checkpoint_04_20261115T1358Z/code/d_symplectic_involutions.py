"""Exact certificate against Boggi2014, Lemma 5.12 (retrieved v5, p.26)."""
import json
from pathlib import Path

def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a): return list(map(list,zip(*a)))
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def mod(a,m): return [[x%m for x in r] for r in a]
def det(a):
    if len(a)==1: return a[0][0]
    return sum((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)))
I=[[int(i==j) for j in range(4)] for i in range(4)]
Omega=[[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]]
A=[[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]]
B=[[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]
Q=[[1,0,1,0],[0,2,0,2],[1,0,-1,0],[0,2,0,-2]]
QB=[[1,0,1,0],[0,1,0,1],[1,0,-1,0],[0,1,0,-1]]
assert mul(A,A)==I and mul(B,B)==I
assert mul(mul(tr(A),Omega),A)==Omega
assert mul(mul(tr(B),Omega),B)==Omega
assert mul(B,Q)==mul(Q,A)
assert mod(mul(mul(tr(Q),Omega),Q),3)==mod(Omega,3)
assert det(Q)%3!=0
assert mul(B,QB)==mul(QB,A)
assert abs(det(QB))==4
out={"symplectic_form":Omega,"A":A,"B":B,"modulus":3,"Q":Q,
     "A_squared":mul(A,A),"B_squared":mul(B,B),"Q_det":det(Q),
     "Q_transpose_Omega_Q":mul(mul(tr(Q),Omega),Q),
     "BQ_minus_QA":sub(mul(B,Q),mul(Q,A)),
     "A_eigenlattice_sum_basis":I,"A_eigenlattice_sum_index":1,
     "B_eigenlattice_sum_basis":QB,"B_eigenlattice_sum_index":abs(det(QB)),
     "checks":"Both order-two matrices are integral symplectic; Q is symplectic modulo 3 and intertwines A and B; eigenlattice-sum indices 1 and 4 obstruct integral conjugacy."}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print('A^2=B^2=I; A and B preserve Omega over Z: verified')
print('B Q=Q A over Z: verified')
print('det(Q) =',det(Q))
print('Q^t Omega Q =',out['Q_transpose_Omega_Q'])
print('Q is symplectic and invertible modulo 3: verified')
print('Integral eigenlattice-sum indices: A = 1, B = 4')
print('Therefore the order-two cyclic subgroups are not conjugate over Z, but are conjugate modulo 3.')
