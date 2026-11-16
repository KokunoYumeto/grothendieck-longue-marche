#!/usr/bin/env python3
"""Exact framed Picard group of the punctured cubic over F4.

We evaluate regularized Miller functions and compare the resulting
generalized-Jacobian points with the integral Tate coinvariant module.
No geometric translation path is set equal to zero.
"""
from itertools import product
import json
import numpy as np

def mul(a,b):
    c=0
    for i in range(2):
        if (b>>i)&1:c ^= a<<i
    if c&4:c ^=7
    return c
def power(a,n):
    r=1
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
def div(a,b):
    assert b
    return mul(a,power(b,2))
def logz(a):
    assert a
    return {1:0,2:1,3:2}[a]
def neg(P):return None if P is None else (P[0],P[1]^1)
def plus(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u:
        if y!=v:return None
        slope=mul(x,x)
    else:slope=div(y^v,x^u)
    w=mul(slope,slope)^x^u
    return w,mul(slope,x^w)^y^1
def times(a,P):
    R=None
    for _ in range(a):R=plus(R,P)
    return R

zeta=2
cusps=[(1,2),(3,2),(2,2),(1,3),(3,3),(2,3),(0,0),(0,1)]
points=[None]+cusps
P1,P2=cusps[0],cusps[2]
coords={plus(times(a,P1),times(b,P2)):(a,b) for a,b in product(range(3),repeat=2)}
assert len(coords)==9
ks={None:1}
for i,P in enumerate(cusps):
    ks[P]=P[0] if i<6 else div(1,P[1]^zeta)
assert all(ks.values())

def addvec(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def scalevec(n,a):return tuple(n*x%3 for x in a)
zero=(0,)*8
def tor_at(P,e):
    if P is None:return (-e%3,)*8
    r=[0]*8;r[cusps.index(P)]=e%3
    return tuple(r)

def lead_line(P,Q,R):
    """Order and leading coefficient in delta=x-x_R for nonvertical line."""
    xp,yp=P;xq,yq=Q;xr,yr=R
    slope=mul(xp,xp) if P==Q else div(yp^yq,xp^xq)
    constant=yr^yp^mul(slope,xr^xp)
    if constant:return 0,constant
    first=mul(xr,xr)^slope
    if first:return 1,first
    return 3,1
def lead_vertical(x0,R):
    if R[0]!=x0:return 0,R[0]^x0
    return 1,1

def miller_torus(P,Q):
    """z_P+z_Q-z_{P+Q}, with prescribed cusp parameters."""
    if P is None or Q is None:return zero
    R=plus(P,Q)
    out=[]
    for T in cusps:
        if R is None:
            order,lead=lead_vertical(P[0],T)
        else:
            ol,ll=lead_line(P,Q,T)
            ov,lv=lead_vertical(R[0],T)
            order,lead=ol-ov,div(ll,lv)
        # s_T = k_T delta + higher terms.
        lead=mul(lead,power(ks[T],(-order)%3))
        # The leading coefficient at O in q=Z/X is one.
        out.append(logz(lead))
    return tuple(out)

cocycle={(P,Q):miller_torus(P,Q) for P in points for Q in points}
for P,Q,R in product(points,repeat=3):
    assert addvec(cocycle[P,Q],cocycle[plus(P,Q),R])==addvec(cocycle[Q,R],cocycle[P,plus(Q,R)])
for P,Q in product(points,repeat=2):assert cocycle[P,Q]==cocycle[Q,P]

def gadd(A,B):
    P,a=A;Q,b=B
    return plus(P,Q),addvec(addvec(a,b),cocycle[P,Q])
def gneg(A):
    P,a=A;Q=neg(P)
    return Q,scalevec(-1,addvec(a,cocycle[P,Q]))
def gtimes(n,A):
    R=(None,zero)
    for _ in range(n):R=gadd(R,A)
    return R
def z(P):return P,zero

U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
for P in points:
    triple=gtimes(3,z(P))
    assert triple[0] is None
    expected=tuple(int(x)%3 for x in 2*U@np.array(coords[P],dtype=np.int64))
    assert triple[1]==expected,(P,triple[1],expected)

def Hnorm(a,b):
    a=np.array(a,dtype=np.int64);b=np.array(b,dtype=np.int64)
    carry=a//3
    return tuple(int(x) for x in a%3),tuple(int(x) for x in (b-2*U@carry)%3)
def Hadd(A,B):return Hnorm(np.array(A[0])+B[0],np.array(A[1])+B[1])
def Hneg(A):return Hnorm(-np.array(A[0]),-np.array(A[1]))
def Hmatrix(A,X):
    vec=A@np.array(X[0]+X[1],dtype=np.int64)
    return Hnorm(vec[:2],vec[2:])

# Express each z_P in generators z_P1,z_P2 and eight torus generators.
zrelations={}
for P,(a,b) in coords.items():
    G= gadd(gtimes(a,z(P1)),gtimes(b,z(P2)))
    assert G[0]==P
    zrelations[P]=G[1]

def image(G,unknown=None):
    P,tor=G;a,b=coords[P]
    bottom=np.array(tor,dtype=np.int64)-np.array(zrelations[P],dtype=np.int64)
    if unknown is not None:bottom+=a*unknown[:8]+b*unknown[8:]
    return Hnorm([-a,-b],bottom)

def Wmatrix(pointmap):
    P=np.zeros((8,8),dtype=np.int64)
    for j,R in enumerate(cusps):
        image=pointmap(R)
        if image is None:P[:,j]=-1
        else:P[cusps.index(image),j]=1
    return P
def geometric_action(G,pointmap,differential):
    P,tor=G;gp=pointmap(P);go=pointmap(None)
    answer=gadd(z(gp),gneg(z(go)))
    a=div(mul(differential,ks[gp]),ks[P])
    b=div(1,mul(differential,ks[go]))
    correction=addvec(tor_at(gp,logz(a)),tor_at(go,logz(b)))
    moved=tuple(int(x)%3 for x in Wmatrix(pointmap)@np.array(tor,dtype=np.int64))
    return answer[0],addvec(answer[1],addvec(correction,moved))

MODPLUS=27
sqrtm2=next(s for s in range(MODPLUS) if s%3==1 and (s*s+2)%MODPLUS==0)
I=np.eye(2,dtype=np.int64)
QI=np.array([[sqrtm2,-1],[-1,-sqrtm2]],dtype=np.int64)%MODPLUS
QJ=np.array([[1,sqrtm2],[sqrtm2,-1]],dtype=np.int64)%MODPLUS
QK=QI@QJ%MODPLUS
compact=[I,(-I)%MODPLUS,QI,(-QI)%MODPLUS,QJ,(-QJ)%MODPLUS,QK,(-QK)%MODPLUS]
q8=[]
for r,b in product(range(4),repeat=2):
    if mul(b,b)^b!=power(r,3):continue
    def fn(P,r=r,b=b):
        return None if P is None else (P[0]^r,P[1]^mul(mul(r,r),P[0])^b)
    Mres=np.array([coords[fn(P1)],coords[fn(P2)]],dtype=np.int64).T
    matches=[M for M in compact if np.array_equal(M%3,Mres%3)]
    assert len(matches)==1
    q8.append((f'q8_{r}_{b}',fn,1,matches[0]))
R3=np.array([[0,-1],[1,-1]],dtype=np.int64)
candidates=[]
for signs in product((-1,1),repeat=3):
    S=(-I+signs[0]*QI+signs[1]*QJ+signs[2]*QK)*pow(2,-1,MODPLUS)%MODPLUS
    if np.array_equal(S%3,R3%3):candidates.append(S)
assert len(candidates)==1
S=candidates[0]
assert np.array_equal(S@S%MODPLUS@S%MODPLUS,I)
def sigma(P):return None if P is None else (mul(zeta,P[0]),P[1])
autos=q8+[('sigma',sigma,zeta,S)]
for d in (P1,P2):
    autos.append((f'translation_{coords[d]}',lambda P,d=d:plus(P,d),1,I))

equations=[];targets=[];automorphism_data=[]
for name,fn,diff,M in autos:
    W=Wmatrix(fn)
    C=U@M-W@U
    assert not np.any(C%3)
    A=np.zeros((10,10),dtype=np.int64)
    A[:2,:2]=M;A[2:,:2]=C//3;A[2:,2:]=W
    for P,Q in product(points,repeat=2):
        assert geometric_action(gadd(z(P),z(Q)),fn,diff)==gadd(geometric_action(z(P),fn,diff),geometric_action(z(Q),fn,diff)),name
    for P in (P1,P2):
        acted=geometric_action(z(P),fn,diff)
        difference=Hadd(image(acted),Hneg(Hmatrix(A,image(z(P)))))
        assert difference[0]==(0,0)
        aa=coords[acted[0]];bb=coords[P]
        linear=np.hstack((aa[0]*np.eye(8,dtype=np.int64)-bb[0]*W,
                          aa[1]*np.eye(8,dtype=np.int64)-bb[1]*W))%3
        equations.extend(linear.tolist());targets.extend((-np.array(difference[1]))%3)
    automorphism_data.append((name,A))

# Actual arithmetic Frob2 is (x^2,y^2+1); parameters are from the F2 model.
def frob2(P):return None if P is None else (power(P[0],2),power(P[1],2)^1)
M2=(QJ-QK)%MODPLUS
W2=2*Wmatrix(frob2)
C2=U@M2-W2@U
assert not np.any(C2%3)
A2=np.zeros((10,10),dtype=np.int64)
A2[:2,:2]=M2;A2[2:,:2]=C2//3;A2[2:,2:]=W2
for P,Q in product(points,repeat=2):
    lhs=gtimes(1,(frob2(plus(P,Q)),tuple(int(x)%3 for x in W2@np.array(cocycle[P,Q]))))
    rhs=gadd(z(frob2(P)),z(frob2(Q)))
    assert lhs==rhs,('Frob2',P,Q,lhs,rhs)
for P in (P1,P2):
    acted=z(frob2(P))
    difference=Hadd(image(acted),Hneg(Hmatrix(A2,image(z(P)))))
    assert difference[0]==(0,0)
    aa=coords[acted[0]];bb=coords[P]
    linear=np.hstack((aa[0]*np.eye(8,dtype=np.int64)-bb[0]*W2,
                      aa[1]*np.eye(8,dtype=np.int64)-bb[1]*W2))%3
    equations.extend(linear.tolist());targets.extend((-np.array(difference[1]))%3)

Aug=np.column_stack((np.array(equations,dtype=np.int64),np.array(targets,dtype=np.int64)))%3
rank=0;pivots=[]
for col in range(16):
    choices=np.nonzero(Aug[rank:,col])[0]
    if not len(choices):continue
    pivot=rank+int(choices[0]);Aug[[rank,pivot],:]=Aug[[pivot,rank],:]
    Aug[rank,:]=Aug[rank,:]*int(Aug[rank,col])%3
    for r in range(len(Aug)):
        if r!=rank:Aug[r,:]=(Aug[r,:]-Aug[r,col]*Aug[rank,:])%3
    pivots.append(col);rank+=1
consistent=not np.any(Aug[rank:,-1])
assert consistent,'Equivariant Kummer matching inconsistent'
particular=np.zeros(16,dtype=np.int64)
for r,col in enumerate(pivots):particular[col]=Aug[r,-1]
free=[j for j in range(16) if j not in pivots]
kernel=[]
for j in free:
    v=np.zeros(16,dtype=np.int64);v[j]=1
    for r,col in enumerate(pivots):v[col]=-Aug[r,j]%3
    kernel.append(v)

path_data=[]
for d in cusps:
    # Tangent translated from O has derivative k_d in the prescribed s_d.
    alpha=(d,tor_at(d,logz(ks[d])))
    im=image(alpha,particular)
    path_data.append({'cusp':cusps.index(d),'point':d,'E3_coordinates':coords[d],
                      'parameter_derivative':ks[d],
                      'framed_group_torus':alpha[1],
                      'one_equivariant_coinvariant_image':im})

result={
    'status':'exact framed group and equivariant matching verified',
    'field':'F4=F2[zeta]/(zeta^2+zeta+1)',
    'group_order':3**10,
    'Miller_cocycle_associativity_checks':9**3,
    'geometric_generator_group_law_checks':len(autos)*81,
    'Frobenius2_group_law_checks':81,
    'unknown_Kummer_shear_coordinates':16,
    'equivariant_constraint_rank':rank,
    'remaining_affine_dimension':len(free),
    'particular_shear':[int(x) for x in particular],
    'kernel_shears':[[int(x) for x in v] for v in kernel],
    'translation_paths':path_data,
    'scope':'Actual framed group computed. If residual affine dimension is nonzero, no single Kummer matching is asserted to be canonical.'
}
print(json.dumps(result,indent=2))
with open('deliverable/code/c_char2_translation_paths.json','w') as f:
    json.dump(result,f,indent=2);f.write('\n')
np.savez_compressed('deliverable/code/c_char2_translation_paths_matrices.npz',
                    particular=particular,kernel=np.array(kernel),
                    constraint_matrix=np.array(equations,dtype=np.int64)%3,
                    constraint_target=np.array(targets,dtype=np.int64)%3,
                    automorphism_matrices=np.stack([A for name,A in automorphism_data]),
                    Frobenius2=A2,compact_sigma=S,
                    translation_compact_point_basis=np.array([coords[P] for P in cusps]),
                    U=U)
