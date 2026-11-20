"""Exact n=1 matrix certificate for the claims discussed in note 16/015."""
def unit(i,j):
    return tuple(tuple(int(r==i and c==j) for c in range(4)) for r in range(4))
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)) for i in range(4))
def add(a,b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(4)) for i in range(4))
zero=tuple((0,0,0,0) for _ in range(4))
P0,P2,L,C=unit(0,0),unit(3,3),unit(3,0),unit(0,3)
P1=add(unit(1,1),unit(2,2))
phi={(0,0,0):P0,(0,1,0):L,(0,0,1):C,(0,1,1):P2,(1,0,0):P1}
for (ip,bp,ap),a in phi.items():
    for (i,b,al),d in phi.items():
        expected=phi[(i,bp,al)] if ip==i and ap==b else zero
        assert mul(a,d)==expected
assert mul(mul(L,L),P0)==zero
# Five independent coordinates, one for each listed matrix.
assert [m[i][j] for m,(i,j) in zip(phi.values(),[(0,0),(3,0),(0,3),(3,3),(1,1)])]==[1]*5
print('Verified 25 products for the five n=1 basis matrices.')
print('Written extra element phi_0^(2,0)=L^2 P0 is the zero matrix.')
print('Mat_2(Z) plus Z maps to the 1,v block and the common e,f scalar block.')
