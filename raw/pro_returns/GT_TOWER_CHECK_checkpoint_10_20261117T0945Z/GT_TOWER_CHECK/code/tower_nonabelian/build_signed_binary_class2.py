#!/usr/bin/env python3
"""Exact collected exponent-four class-two quotient over signed Q192.

No division by two is used.  The universal group on 102 generators has
power coordinates modulo four and commutators modulo two.  Its last two
squares are retained as central coordinates while imposing the actual
C4^100 x C2^2 abelianization.  All 1152 cover relators are collected.
"""
from pathlib import Path
import hashlib,json,sys,time
import numpy as np

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'ghost_code'))
import fivepoint_signed_level_data as C
start_time=time.time()
INPUT=ROOT/'ghost_mod4/check_fivepoint_quartic_mixed_module.npz'
old=np.load(INPUT)
P4=old['target_h1_projection'].astype(np.int16)%4
Rint=C.matrix.astype(np.int16)
R=(Rint%2).astype(np.uint8)
assert P4.shape==(769,102)
assert not np.any(Rint@P4[:,:100]%4)
assert not np.any(Rint@P4[:,100:]%2)
ii,jj=np.triu_indices(102,1);nw=len(ii);nc=nw+2
assert (nw,nc)==(5151,5153)

def schreier(w,start=0):
    q=start;out=[]
    for z in w:
        if z>0:
            edge=(q,z-1);q=int(C.table[q,C.ig[z-1]]);sgn=1
        else:
            q=int(C.table[q,C.inverses[C.ig[-z-1]]]);edge=(q,-z-1);sgn=-1
        if edge in C.chordidx:out.append(sgn*(C.chordidx[edge]+1))
    assert q==start
    return tuple(out)

relwords=[schreier(w,s) for s in range(192) for w in C.relations]

def cross(v,w):
    # Normal form x1^a1 ... x102^a102 [xi,xj]^zij, i<j.
    # Moving the right xi through the left xj gives this sign, which
    # coincides with its negative modulo two.
    return (v[jj]*w[ii])%2

def collect_raw(w):
    v=np.zeros(102,dtype=np.int16);z=np.zeros(nw,dtype=np.uint8)
    for a in w:
        g=P4[abs(a)-1]
        u=g if a>0 else -g%4
        c=np.zeros(nw,dtype=np.uint8) if a>0 else cross(g,g).astype(np.uint8)
        z^=c;z^=cross(v,u).astype(np.uint8)
        v=(v+u)%4
    return v,z

B=np.empty((1152,nc),dtype=np.uint8)
for k,w in enumerate(relwords):
    v,z=collect_raw(w)
    assert not np.any(v[:100]) and not np.any(v[100:]%2)
    B[k,:2]=v[100:]//2;B[k,2:]=z
print('PASS all1152 collected relators are central after the exact',
      'C4^100 x C2^2 projection; retained squares2, commutators5151',flush=True)

A=R.copy();Z=B.copy();piv=[];r=0
for c in range(769):
    nz=np.flatnonzero(A[r:,c])
    if not len(nz):continue
    k=r+int(nz[0]);A[[r,k]]=A[[k,r]];Z[[r,k]]=Z[[k,r]]
    nz=np.flatnonzero(A[:,c]);nz=nz[nz!=r]
    A[nz]^=A[r];Z[nz]^=Z[r]
    piv.append(c);r+=1
assert r==667 and not np.any(A[r:])
free=[j for j in range(769) if j not in set(piv)]
assert len(free)==102

def rref2(a):
    a=np.array(a,dtype=np.uint8)%2;r=0;pv=[]
    for c in range(a.shape[1]):
        if r==len(a):break
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        k=r+int(nz[0]);a[[r,k]]=a[[k,r]]
        nz=np.flatnonzero(a[:,c]);nz=nz[nz!=r]
        a[nz]^=a[r];pv.append(c);r+=1
    return a[:r],pv

CR,cpiv=rref2(Z[r:]);cfree=[j for j in range(nc) if j not in set(cpiv)]
def reduce_z(z):
    z=np.asarray(z,dtype=np.int64)%2
    return (z[...,cfree]+z[...,cpiv]@CR[:,cfree].astype(np.int64))%2

GC=np.zeros((769,nc),dtype=np.uint8);GC[piv]=Z[:r]
Graw=np.zeros((769,nc),dtype=np.uint8);Graw[:,:2]=P4[:,100:]//2
G=reduce_z(GC+Graw).astype(np.uint8)
assert not np.any((R.astype(np.int64)@reduce_z(GC)+reduce_z(B))%2)
Bnormalized=B^(R.astype(np.int64)@Graw%2).astype(np.uint8)
assert not np.any((R.astype(np.int64)@G+reduce_z(Bnormalized))%2)
assert not np.any(reduce_z(Z[r:]))
assert len(rref2(CR[:,:2])[1])==2
assert len(rref2(P4[free]%2)[1])==102

P=P4.copy();P[:,100:]%=2
sq=np.zeros((2,nc),dtype=np.uint8);sq[0,0]=sq[1,1]=1
square_images=reduce_z(sq).astype(np.uint8)
def mul(x,y):
    v=x[0]+y[0]
    carry=(v[100:]//2).astype(np.int64)
    v[:100]%=4;v[100:]%=2
    raw=np.zeros(nc,dtype=np.uint8);raw[2:]=cross(x[0],y[0])
    c=(x[1]+y[1]+reduce_z(raw)+carry@square_images)%2
    return v,c
def inv(x):
    v=-x[0];v[:100]%=4;v[100:]%=2
    raw=np.zeros(nc,dtype=np.uint8);raw[2:]=cross(x[0],v)
    c=(x[1]+reduce_z(raw)+x[0][100:]@square_images)%2
    return v,c
def same(x,y):return np.array_equal(x[0],y[0]) and np.array_equal(x[1],y[1])
zero=(np.zeros(102,dtype=np.int16),np.zeros(len(cfree),dtype=np.int64))
for a,b,c in [(0,1,2),(100,300,500),(768,767,766)]:
    x,y,z=[(P[i],G[i].astype(np.int64)) for i in (a,b,c)]
    assert same(mul(mul(x,y),z),mul(x,mul(y,z)))
    assert same(mul(x,inv(x)),zero)
    xx=mul(x,x);assert same(mul(xx,xx),zero)
    cm=mul(mul(mul(x,y),inv(x)),inv(y))
    assert not np.any(cm[0]) and same(mul(cm,cm),zero)

out={
 'scope':'Actual N/(gamma3(N) N^4), N=ker(Gamma_0,5 -> signed Q192); no genuine associator-image claim',
 'base_order':192,'cover_generators':769,'cover_relators':1152,
 'abelian_group':'C4^100 x C2^2','abelian_order_power_of_2':202,
 'linear_mod2_relation_rank':r,'retained_torsion_squares':2,
 'universal_commutator_dimension':nw,'central_relation_rank':len(cpiv),
 'central_dimension':len(cfree),'commutator_dimension':len(cfree),
 'kernel_order_power_of_2':202+len(cfree),
 'full_quotient_order':'192 * 2^'+str(202+len(cfree)),
 'division_by_two_used':False,'all_assertions_passed':True,
 'input_sha256':{'ghost_code/fivepoint_signed_level_data.py':hashlib.sha256(Path(C.__file__).read_bytes()).hexdigest(),
                  str(INPUT.relative_to(ROOT)):hashlib.sha256(INPUT.read_bytes()).hexdigest()},
 'runtime_seconds':round(time.time()-start_time,3)}
HERE.joinpath('build_signed_binary_class2.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(HERE/'build_signed_binary_class2.npz',
 relation_matrix=Rint,linear_projection=P,raw_linear_projection=P4,
 linear_pivots=np.array(piv),linear_free=np.array(free),
 relator_raw_central=B,relator_normalized_central=Bnormalized,
 central_relation_matrix=Z[r:],central_relation_rref=CR,
 central_pivots=np.array(cpiv),central_free=np.array(cfree),
 generator_central=G,generator_central_correction=GC,
 square_images=square_images,wedge_i=ii,wedge_j=jj)
print(json.dumps(out,indent=2),flush=True)
