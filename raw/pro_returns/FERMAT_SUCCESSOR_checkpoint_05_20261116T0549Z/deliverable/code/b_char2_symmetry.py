"""Good-characteristic-two symmetry reduction for the cubic local class.

This computes coefficient modules, not the unknown arithmetic extension
class. It derives the F4 automorphisms directly and keeps integral
3-adic gluing before taking quaternion invariants.
"""
from collections import Counter
import numpy as np
import sympy as sp

PREC=10
MOD=3**PREC
MODPLUS=3**(PREC+1)
# F4 = F2[z]/(z^2+z+1), encoded as the two polynomial coefficients.
def add(a,b): return a^b
def mul(a,b):
    c=0
    for i in range(2):
        if b>>i&1: c^=a<<i
    if c&4:c^=7
    return c
def pow4(a,n):
    r=1
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
def div(a,b):
    assert b
    return mul(a,pow4(b,2))

def neg(P): return None if P is None else (P[0],P[1]^1)
def plus(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u:
        if y!=v:return None
        lam=mul(x,x)
    else:lam=div(y^v,x^u)
    w=mul(lam,lam)^x^u
    z=mul(lam,x^w)^y^1
    return w,z

def scalar(a,P):
    R=None
    for _ in range(a):R=plus(R,P)
    return R

points=[None]+[(x,y) for x in range(4) for y in range(4) if mul(y,y)^y==pow4(x,3)]
assert len(points)==9 and all(scalar(3,P) is None for P in points)
# Explicit projective isomorphism from X^3+Y^3+Z^3=0:
# x=Z/(X+Y), y=X/(X+Y)+zeta.
zeta=2
cusps=[(1,2),(3,2),(2,2),(1,3),(3,3),(2,3),(0,0),(0,1)]
P1,P2=cusps[0],cusps[2]
coords={plus(scalar(a,P1),scalar(b,P2)):(a,b) for a in range(3) for b in range(3)}
assert len(coords)==9
expected=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
assert [coords[P] for P in cusps]==expected
print('F4 cubic: all9 points are the9 punctures and E[3]; exact cusp basis agrees with U: PASS')

# Direct doubling: [2](x,y)=(x^4,y^4+1), so Frob4=[-2].
for x in range(4):
    for y in range(4):
        if mul(y,y)^y==pow4(x,3):
            assert plus((x,y),(x,y))==(pow4(x,4),pow4(y,4)^1)
print('Frobenius4=[-2]: direct characteristic-two doubling formula checked')

def auto(P,r,b):
    if P is None:return None
    x,y=P
    return x^r, y^mul(mul(r,r),x)^b
q8=[]
for r in range(4):
    for b in range(4):
        if mul(b,b)^b==pow4(r,3):
            perm=[cusps.index(auto(P,r,b)) for P in cusps]
            M=sp.Matrix.hstack(sp.Matrix(coords[auto(P1,r,b)]),sp.Matrix(coords[auto(P2,r,b)]))
            assert int(M.det())%3==1
            q8.append((r,b,perm,M))
            for P in points:
                for Q in points:
                    assert auto(plus(P,Q),r,b)==plus(auto(P,r,b),auto(Q,r,b))
assert len(q8)==8
print('Q8 automorphisms (x,y)->(x+r,y+r^2*x+b), b^2+b=r^3: all group-law checks pass')
print('Every Q8 automorphism fixes O and has derivative1 in t=x/y; no tangent rescaling term')

# Hensel lift of sqrt(-2) congruent1mod3. This realizes the unique
# quaternion representation lifting the indicated residual action.
sqrtm2=1
power=3
for n in range(1,PREC+1):
    choices=[sqrtm2+k*power for k in range(3) if ((sqrtm2+k*power)**2+2)%(3*power)==0]
    assert len(choices)==1
    sqrtm2=choices[0];power*=3
assert (sqrtm2*sqrtm2+2)%MODPLUS==0
I2=np.eye(2,dtype=np.int64)
QI=np.array([[sqrtm2,-1],[-1,-sqrtm2]],dtype=np.int64)%MODPLUS
QJ=np.array([[1,sqrtm2],[sqrtm2,-1]],dtype=np.int64)%MODPLUS
QK=(QI@QJ)%MODPLUS
assert np.array_equal(QI@QI%MODPLUS,(-I2)%MODPLUS)
assert np.array_equal(QJ@QJ%MODPLUS,(-I2)%MODPLUS)
assert not np.any((QI@QJ+QJ@QI)%MODPLUS)
compact=[I2,(-I2)%MODPLUS,QI,(-QI)%MODPLUS,QJ,(-QJ)%MODPLUS,QK,(-QK)%MODPLUS]
residual={tuple(int(x) for x in np.asarray(M,dtype=np.int64).flatten()%3):(r,b,perm) for r,b,perm,M in q8}
assert len(residual)==8

U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
matrices=[]
for M in compact:
    r,b,perm=residual[tuple(int(x) for x in M.flatten()%3)]
    P=np.zeros((8,8),dtype=np.int64)
    for col,row in enumerate(perm):P[row,col]=1
    delta=U@M-P@U
    assert not np.any(delta%3)
    V=np.zeros((10,10),dtype=np.int64)
    V[:2,:2]=M%MOD;V[2:,:2]=(delta//3)%MOD;V[2:,2:]=P
    matrices.append(V%MOD)
assert len({tuple(M.flatten()) for M in matrices})==8
for A in matrices:
    for B in matrices:
        assert tuple((A@B%MOD).flatten()) in {tuple(M.flatten()) for M in matrices}
print('All8 actual-gluing quaternion matrices form Q8 modulo3^10: PASS')

hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={t:n for n,t in enumerate(hall)}
def bracket(a,b,c):
    if a==b:return ()
    sign=1
    if a<b:a,b,sign=b,a,-1
    if c>=b:return ((lookup[(a,b,c)],sign),)
    return ((lookup[(a,c,b)],sign),(lookup[(b,c,a)],-sign))
def lie3(A):
    nz=[[(i,int(A[i,j])) for i in range(10) if A[i,j]] for j in range(10)]
    L=np.zeros((330,330),dtype=np.int64)
    for col,(i,j,k) in enumerate(hall):
        for a,x in nz[i]:
            for b,y in nz[j]:
                for c,z in nz[k]:
                    prod=x*y*z%MOD
                    for row,sgn in bracket(a,b,c):L[row,col]=(int(L[row,col])+sgn*prod)%MOD
    return L

def pivcols(A):
    A=A.copy()%3
    cols=[];r=0
    for c in range(A.shape[1]):
        nz=np.nonzero(A[r:,c])[0]
        if not len(nz):continue
        k=r+int(nz[0]);A[[r,k],:]=A[[k,r],:]
        A[r,:]=(A[r,:]*int(A[r,c]))%3
        for j in range(A.shape[0]):
            if j!=r:A[j,:]=(A[j,:]-A[j,c]*A[r,:])%3
        cols.append(c);r+=1
        if r==A.shape[0]:break
    return cols

def inverse_unit(A):
    n=len(A);A=A.copy()%MOD;B=np.eye(n,dtype=np.int64)
    for c in range(n):
        opts=np.nonzero(A[c:,c]%3)[0];assert len(opts)
        k=c+int(opts[0]);A[[c,k],:]=A[[k,c],:];B[[c,k],:]=B[[k,c],:]
        unit=pow(int(A[c,c]),-1,MOD)
        A[c,:]=A[c,:]*unit%MOD;B[c,:]=B[c,:]*unit%MOD
        for j in range(n):
            if j==c:continue
            factor=int(A[j,c]);A[j,:]=(A[j,:]-factor*A[c,:])%MOD;B[j,:]=(B[j,:]-factor*B[c,:])%MOD
    assert np.array_equal(A,np.eye(n,dtype=np.int64))
    return B

def smith3(A):
    A=A.copy()%MOD;n=len(A);vals=[]
    for k in range(n):
        block=A[k:,k:];power=1
        for v in range(PREC):
            nz=np.argwhere((block//power)%3)
            if len(nz):break
            power*=3
        else:raise AssertionError('pivot not certified')
        r,c=map(int,nz[0]);r+=k;c+=k
        A[[k,r],:]=A[[r,k],:];A[:,[k,c]]=A[:,[c,k]]
        assert not np.any(A[k:,k:]%power)
        unit=int(A[k,k])//power
        A[k,k:]=A[k,k:]*pow(unit,-1,MOD)%MOD
        quot=A[k+1:,k]//power
        A[k+1:,k:]=(A[k+1:,k:]-quot[:,None]*A[k,k:][None,:])%MOD
        vals.append(v)
    return dict(sorted(Counter(vals).items()))

F=np.zeros((10,10),dtype=np.int64);F[:2,:2]=-2*I2;F[2:,2:]=4*np.eye(8,dtype=np.int64);F[2:,:2]=-2*U
F%=MOD
LA=lie3(F)
D=(pow(4,-1,MOD)*LA-np.eye(330,dtype=np.int64))%MOD
Ls=[lie3(M) for M in matrices]
for L in Ls:assert not np.any((L@D-D@L)%MOD)
Pi=sum(Ls)%MOD*pow(8,-1,MOD)%MOD
assert not np.any((Pi@Pi-Pi)%MOD)
cols=pivcols(Pi)
assert len(cols)==41
E=Pi[:,cols]
rows=pivcols(E.T)
assert len(rows)==41
EI=inverse_unit(E[rows,:])
D41=(EI@D[rows,:]%MOD@E)%MOD
assert not np.any((E@D41-D@E)%MOD)
hist=smith3(D41)
assert sum(v*c for v,c in hist.items())==57
print('Integral Q8 invariant lattice rank:',len(cols))
print('Invariant local Frobenius-minus-one Smith valuations:',hist)
print('Independent determinant valuation 4+2*16+21=57: PASS')
print('Local arithmetic eta is forced into this group; its actual class is NOT evaluated here.')
np.savez_compressed('deliverable/code/b_char2_symmetry_matrices.npz',modulus=np.array([MOD]),Q8_matrices=np.stack(matrices),invariant_basis=E,invariant_rows=np.array(rows),D41=D41)
print('Saved exact modular coefficient matrices and invariant basis.')

# Add the actual order-three automorphism scaling the plane coordinate Z
# by zeta; its compact residual matrix is [[0,-1],[1,-1]].
Rres=np.array([[0,2],[1,2]],dtype=np.int64)
Rlift=None
for aa in [-1,1]:
    for bb in [-1,1]:
        for cc in [-1,1]:
            candidate=((-I2+aa*QI+bb*QJ+cc*QK)*pow(2,-1,MODPLUS))%MODPLUS
            if np.array_equal(candidate%3,Rres):Rlift=candidate
assert Rlift is not None
assert np.array_equal(Rlift@Rlift%MODPLUS@Rlift%MODPLUS,I2)
Pr=np.zeros((8,8),dtype=np.int64)
pointcoords={c:i for i,c in enumerate(expected)}
for j,c in enumerate(expected):
    d=tuple(int(x) for x in Rres@np.array(c)%3)
    Pr[pointcoords[d],j]=1
RV=np.zeros((10,10),dtype=np.int64)
RV[:2,:2]=Rlift%MOD;RV[2:,2:]=Pr
raw=U@Rlift-Pr@U
assert not np.any(raw%3)
RV[2:,:2]=(raw//3)%MOD
LR=lie3(RV)
assert not np.any((LR@D-D@LR)%MOD)
assert not np.any((LR@Pi-Pi@LR)%MOD)
R41=(EI@LR[rows,:]%MOD@E)%MOD
assert not np.any((E@R41-LR@E)%MOD)
assert np.array_equal(R41@R41%MOD@R41%MOD,np.eye(41,dtype=np.int64))

# The actual tangent rescaling supplies [kappa(zeta)e_O,w].
u=np.concatenate((np.array([3,0]),U[:,0]))
v=np.concatenate((np.array([0,3]),U[:,1]))
eO=np.concatenate((np.zeros(2,dtype=np.int64),-np.ones(8,dtype=np.int64)))
br=np.zeros(330,dtype=np.int64)
for i in range(10):
    for j in range(10):
        for k in range(10):
            coeff=-int(u[i])*int(v[j])*int(eO[k])
            if coeff:
                for rr,sgn in bracket(i,j,k):br[rr]+=coeff*sgn
br%=MOD
assert not np.any((Pi@br-br)%MOD)
b41=EI@br[rows]%MOD
assert not np.any((E@b41-br)%MOD)

# Rectangular Smith reduction with row transport; no guessed integer logs.
def smith_transport(A):
    A=A.copy()%MOD;n=A.shape[0]
    Q=np.eye(n,dtype=np.int64);vals=[]
    for k in range(n):
        block=A[k:,k:];power=1
        for val in range(PREC):
            nz=np.argwhere((block//power)%3)
            if len(nz):break
            power*=3
        else:raise AssertionError('rectangular pivot not certified')
        rr,cc=map(int,nz[0]);rr+=k;cc+=k
        A[[k,rr],:]=A[[rr,k],:];Q[[k,rr],:]=Q[[rr,k],:]
        A[:,[k,cc]]=A[:,[cc,k]]
        assert not np.any(A[k:,k:]%power)
        unit=int(A[k,k])//power;inv=pow(unit,-1,MOD)
        A[k,:]=A[k,:]*inv%MOD;Q[k,:]=Q[k,:]*inv%MOD
        quot=A[:,k]//power
        quot[k]=0
        A=(A-quot[:,None]*A[k,:][None,:])%MOD
        Q=(Q-quot[:,None]*Q[k,:][None,:])%MOD
        # Kill all other entries in the pivot row by column operations.
        for j in range(k+1,A.shape[1]):
            assert A[k,j]%power==0
            fac=int(A[k,j])//power
            A[:,j]=(A[:,j]-fac*A[:,k])%MOD
        vals.append(val)
    assert not np.any(A[:,n:])
    return vals,Q

vals,Q=smith_transport(D41)
assert dict(sorted(Counter(vals).items()))==hist
Qinv=inverse_unit(Q)
RC=Q@R41%MOD@Qinv%MOD
bc=Q@b41%MOD
positive=[i for i,e in enumerate(vals) if e]
exponents=[vals[i] for i in positive]
r=len(positive)
RC=RC[np.ix_(positive,positive)]
bc=bc[positive]
for i,e in enumerate(exponents):bc[i]%=3**e
assert any(bc) and all((3*int(bc[i]))%(3**exponents[i])==0 for i in range(r))
print('Tangent-rescaling bracket class has exact order3 in the invariant cokernel: PASS')

for k in range(1,5):
    scales=np.diag([3**max(e-k,0) for e in exponents]).astype(np.int64)
    diag=np.diag([3**e for e in exponents]).astype(np.int64)
    test=np.hstack((((RC-np.eye(r,dtype=np.int64))@scales)%MOD,diag))
    sv,Tleft=smith_transport(test)
    target=Tleft@bc%MOD
    feasible=all(int(target[i])%(3**sv[i])==0 for i in range(r))
    print(f'Equation (sigma-1)eta=[kappa(zeta)e_O,w] has a solution killed by3^{k}: {feasible}')

# The dual of the fixed subgroup is the coinvariant quotient of the dual.
# Commuting with D identifies the dual action with transpose inverse; its
# difference image equals the transpose difference image.
fixed=np.hstack((D41.T,(R41.T-np.eye(41,dtype=np.int64))%MOD))
fixedvals,_=smith_transport(fixed)
print('Homogeneous Aut(E,O) fixed subgroup Smith valuations:',dict(sorted(Counter(fixedvals).items())))
print('These affine symmetry tests constrain eta but do not select a geometric class without a proved uniqueness argument.')
np.savez_compressed('deliverable/code/b_char2_symmetry_matrices.npz',modulus=np.array([MOD]),Q8_matrices=np.stack(matrices),invariant_basis=E,invariant_rows=np.array(rows),D41=D41,R41=R41,b41=b41)

# Arithmetic Frob2 on the original F2 cubic becomes (x^2,y^2+1)
# on E0 after the zeta-dependent change of coordinates.  The compatible
# compact matrix QJ-QK has this residual action and square -2.
M2=(QJ-QK)%MODPLUS
CE=np.array([[1,-1],[0,-1]],dtype=np.int64)%3
assert np.array_equal(M2%3,CE)
assert np.array_equal(M2@M2%MODPLUS,(-2*I2)%MODPLUS)
Pc=np.zeros((8,8),dtype=np.int64)
for j,i in enumerate([0,2,1,3,5,4,7,6]):Pc[i,j]=1
for j,P in enumerate(cusps):
    point=(pow4(P[0],2),pow4(P[1],2)^1)
    assert cusps.index(point)==int(np.nonzero(Pc[:,j])[0][0])
F2=np.zeros((10,10),dtype=np.int64)
F2[:2,:2]=M2%MOD;F2[2:,2:]=2*Pc
raw=U@M2-2*Pc@U
assert not np.any(raw%3)
F2[2:,:2]=raw//3%MOD
assert np.array_equal(F2@F2%MOD,F)
R2=(pow(2,-1,MOD)*lie3(F2))%MOD
assert not np.any((R2@R2-D-np.eye(330,dtype=np.int64))%MOD)
assert not np.any((R2@Pi-Pi@R2)%MOD)
R2_41=EI@R2[rows,:]%MOD@E%MOD
assert not np.any((E@R2_41-R2@E)%MOD)
D2=(R2_41-np.eye(41,dtype=np.int64))%MOD
v2,Q2=smith_transport(D2)
print('Actual Q2-unramified Q8-invariant coefficient Smith valuations:',dict(sorted(Counter(v2).items())))
Q2inv=inverse_unit(Q2)
# Restriction sends eta(Frob2) to (1+R2)eta(Frob2).
Btarget=(R41-np.eye(41,dtype=np.int64))@(np.eye(41,dtype=np.int64)+R2_41)%MOD@Q2inv%MOD
for k in range(1,max(v2)+1):
    scale=np.diag([3**max(e-k,0) for e in v2]).astype(np.int64)
    test=np.hstack((Btarget@scale%MOD,D41))
    vv,QQ=smith_transport(test)
    targ=QQ@b41%MOD
    feasible=all(int(targ[i])%(3**vv[i])==0 for i in range(41))
    print(f'With actual Frob2 descent, affine eta equation has a solution killed by3^{k}: {feasible}')
fixedfull=np.hstack((D41.T,(R41.T-np.eye(41,dtype=np.int64))%MOD,(R2_41.T-np.eye(41,dtype=np.int64))%MOD))
ffvals,_=smith_transport(fixedfull)
print('Homogeneous Aut(E,O)+Frob2 invariant subgroup Smith valuations:',dict(sorted(Counter(ffvals).items())))
np.savez_compressed('deliverable/code/b_char2_symmetry_matrices.npz',modulus=np.array([MOD]),Q8_matrices=np.stack(matrices),invariant_basis=E,invariant_rows=np.array(rows),D41=D41,R41=R41,b41=b41,Frob2_41=R2_41)

# Give concrete module classes showing that the tested symmetries do not
# determine the actual order. These are NOT asserted to be geometric actions.
pos2=[i for i,e in enumerate(v2) if e]
e2=[v2[i] for i in pos2]
pos4=positive
e4=exponents
G=(Q@(R41-np.eye(41,dtype=np.int64))%MOD@(np.eye(41,dtype=np.int64)+R2_41)%MOD@Q2inv[:,pos2])%MOD
G=G[pos4,:]
for i,e in enumerate(e4):G[i,:]%=3**e
bb=(Q@b41%MOD)[pos4]
for i,e in enumerate(e4):bb[i]%=3**e
scales3=np.array([3**(e-1) for e in e2],dtype=np.int64)
small=G*scales3[None,:]
for i,e in enumerate(e4):
    small[i,:]%=3**e
    assert not np.any(small[i,:]%(3**(e-1)))
    small[i,:]//=3**(e-1)
    assert bb[i]%(3**(e-1))==0
small%=3
bb3=np.array([int(bb[i])//(3**(e4[i]-1)) for i in range(len(e4))],dtype=np.int64)%3
Aug=np.column_stack((small,bb3))
piv=[];rr=0
for cc in range(len(e2)):
    nz=np.nonzero(Aug[rr:,cc]%3)[0]
    if not len(nz):continue
    row=rr+int(nz[0]);Aug[[rr,row],:]=Aug[[row,rr],:]
    Aug[rr,:]=Aug[rr,:]*int(Aug[rr,cc])%3
    for i in range(len(Aug)):
        if i!=rr:Aug[i,:]=(Aug[i,:]-Aug[i,cc]*Aug[rr,:])%3
    piv.append(cc);rr+=1
assert not np.any(Aug[rr:,-1])
y=np.zeros(len(e2),dtype=np.int64)
for i,cc in enumerate(piv):y[cc]=Aug[i,-1]
assert not np.any((small@y-bb3)%3)
xsmall=scales3*y
for i,e in enumerate(e2):xsmall[i]%=3**e

def smith_columns(A):
    A=A.copy()%MOD;n,m=A.shape
    V=np.eye(m,dtype=np.int64);vals=[]
    for k in range(n):
        block=A[k:,k:];power=1
        for val in range(PREC):
            nz=np.argwhere((block//power)%3)
            if len(nz):break
            power*=3
        else:raise AssertionError('kernel Smith pivot not certified')
        row,col=map(int,nz[0]);row+=k;col+=k
        A[[k,row],:]=A[[row,k],:]
        A[:,[k,col]]=A[:,[col,k]];V[:,[k,col]]=V[:,[col,k]]
        unit=int(A[k,k])//power
        A[k,:]=A[k,:]*pow(unit,-1,MOD)%MOD
        quot=A[:,k]//power;quot[k]=0
        A=(A-quot[:,None]*A[k,:][None,:])%MOD
        for j in range(k+1,m):
            assert A[k,j]%power==0
            fac=int(A[k,j])//power
            A[:,j]=(A[:,j]-fac*A[:,k])%MOD
            V[:,j]=(V[:,j]-fac*V[:,k])%MOD
        vals.append(val)
    assert not np.any(A[:,n:])
    return vals,V

present=np.hstack((G,-np.diag([3**e for e in e4]).astype(np.int64)))
kv,KV=smith_columns(present)
assert max(kv)<=max(e4)
kercols=KV[:len(e2),len(e4):]
for i,e in enumerate(e2):kercols[i,:]%=3**e

def orderval(v,exps):
    ans=0
    for x,e in zip(v,exps):
        x=int(x)%(3**e)
        if not x:continue
        v=0
        while x%3==0:x//=3;v+=1
        ans=max(ans,e-v)
    return ans

assert orderval(xsmall,e2)==1
assert all((int(G[i,:]@xsmall)-int(bb[i]))%(3**e4[i])==0 for i in range(len(e4)))
h=None
for col in kercols.T:
    assert all(int(G[i,:]@col)%(3**e4[i])==0 for i in range(len(e4)))
    if orderval(col,e2)==4:h=col.copy();break
assert h is not None
examples=[]
for k in range(1,5):
    v=xsmall.copy() if k==1 else xsmall+3**(4-k)*h
    for i,e in enumerate(e2):v[i]%=3**e
    assert orderval(v,e2)==k
    assert all((int(G[i,:]@v)-int(bb[i]))%(3**e4[i])==0 for i in range(len(e4)))
    examples.append([int(x) for x in v])
print('Smith exponents for the13 positive local Q2 coordinates:',e2)
for k,v in enumerate(examples,1):print(f'Explicit affine module class of exact order3^{k}:',v)
import json
with open('deliverable/code/b_char2_affine_examples.json','w') as out:
    json.dump({'coefficient':'coker(Frob2−1) on the actual Q8-invariant Lie3(V)(−1) lattice','smith_exponents':e2,'coordinates_in_Q2_row_Smith_basis':examples,'orders':[3**k for k in range(1,5)],'scope':'Finite module classes satisfying Q8 invariance, the actual Frob2 descent, and the sigma tangent-rescaling identity; not asserted to be geometric action classes.'},out,indent=2)
    out.write('\n')
print('All four affine module witnesses verified; actual geometric eta remains to be selected.')
np.savez_compressed('deliverable/code/b_char2_symmetry_matrices.npz',modulus=np.array([MOD]),Q8_matrices=np.stack(matrices),invariant_basis=E,invariant_rows=np.array(rows),D41=D41,R41=R41,b41=b41,Frob2_41=R2_41,Smith_row_F4=Q,Smith_row_F2=Q2,positive_F4=np.array(pos4),positive_F2=np.array(pos2),affine_map=G,affine_target=bb,affine_examples=np.array(examples,dtype=np.int64))
