#!/usr/bin/env python3
"""Actual class-two exponent-three quotient of the signed five-point kernel.

The source is the literal six-relator free-by-free presentation of Gamma_0,5.
All 1152 Reidemeister--Schreier relators are evaluated in class-two BCH
coordinates over F3.  This computes a finite group quotient and its maps;
it makes no assertion about lifting a finite associator record.
"""
from pathlib import Path
import hashlib, json, sys, time
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'ghost_code'))
import fivepoint_signed_level_data as C

start_time=time.time()
old=np.load(ROOT/'ghost_code/check_fivepoint_signed_module.npz')
P=old['target_h1_projection'].astype(np.int16)%3
R=C.matrix.astype(np.int16)%3
assert P.shape==(769,102) and not np.any(R@P%3)
ii,jj=np.triu_indices(102,1)
nc=len(ii)
assert nc==5151

def inverse(w):return tuple(-z for z in reversed(w))
def subst(w,images):
    return tuple(j for z in w for j in
                 (images[z-1] if z>0 else inverse(images[-z-1])))

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
assert len(relwords)==1152

def log0(w):
    v=np.zeros(102,dtype=np.int16);z=np.zeros(nc,dtype=np.int16)
    for a in w:
        u=P[abs(a)-1]*(1 if a>0 else -1)
        z=(z+2*(v[ii]*u[jj]-v[jj]*u[ii]))%3
        v=(v+u)%3
    return v,z

B=np.empty((1152,nc),dtype=np.int16)
for k,w in enumerate(relwords):
    v,B[k]=log0(w)
    assert not np.any(v)
print('PASS all1152 lifted relators have zero projected linear part;',
      'central width',nc,flush=True)

# Simultaneously eliminate the linear relations and their central values.
# Every operation is an exact F3 row operation.  The first rows prescribe
# the central corrections for pivot generators; the remaining rows are
# exactly the central relators after the free generators are chosen.
A=R.copy();Z=B.copy();piv=[];r=0
for c in range(769):
    nz=np.flatnonzero(A[r:,c])
    if not len(nz):continue
    k=r+int(nz[0]);A[[r,k]]=A[[k,r]];Z[[r,k]]=Z[[k,r]]
    u=int(A[r,c]);A[r]=A[r]*u%3;Z[r]=Z[r]*u%3
    nz=np.flatnonzero(A[:,c]);nz=nz[nz!=r]
    coeff=A[nz,c].copy()
    A[nz]=(A[nz]-coeff[:,None]*A[r])%3
    Z[nz]=(Z[nz]-coeff[:,None]*Z[r])%3
    piv.append(c);r+=1
    if r%100==0:print('linear elimination',r,'elapsed',round(time.time()-start_time,1),flush=True)
assert r==667 and not np.any(A[r:])
free=[j for j in range(769) if j not in set(piv)]
assert np.array_equal(P[free],np.eye(102,dtype=np.int16))
assert np.array_equal(P[piv],-A[:r,free]%3)
central_rel=Z[r:].copy()

def rref(a):
    a=(a%3).astype(np.int16).copy();r=0;pv=[]
    for c in range(a.shape[1]):
        if r==len(a):break
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        k=r+int(nz[0]);a[[r,k]]=a[[k,r]]
        a[r]=a[r]*int(a[r,c])%3
        nz=np.flatnonzero(a[:,c]);nz=nz[nz!=r]
        a[nz]=(a[nz]-a[nz,c,None]*a[r])%3
        pv.append(c);r+=1
    return a[:r],pv

CR,cpiv=rref(central_rel)
cfree=[j for j in range(nc) if j not in set(cpiv)]
def reduce_z(z):
    z=np.asarray(z,dtype=np.int64)%3
    return (z[...,cfree]-z[...,cpiv]@CR[:,cfree].astype(np.int64))%3

# The images of the actual 769 cover generators in the presented quotient.
GC=np.zeros((769,nc),dtype=np.int16)
GC[piv]=-Z[:r]%3
G=reduce_z(GC).astype(np.int16)
RB=reduce_z(B).astype(np.int16)
assert not np.any((R.astype(np.int64)@G+RB)%3)
assert not np.any(reduce_z(central_rel))
print('PASS all literal relators in resulting class-two group;',
      'linear dimension102, central relation rank',len(cpiv),
      'central quotient dimension',len(cfree),flush=True)

# Verify the BCH multiplication, generator inverse and commutator convention
# on a deterministic collection of actual source generators.
def wedge(v,w):return v[ii]*w[jj]-v[jj]*w[ii]
def mul(x,y):
    return ((x[0]+y[0])%3,
            (x[1]+y[1]+2*reduce_z(wedge(x[0],y[0])))%3)
def inv(x):return (-x[0]%3,-x[1]%3)
def same(x,y):return np.array_equal(x[0],y[0]) and np.array_equal(x[1],y[1])
zero=(np.zeros(102,dtype=np.int16),np.zeros(len(cfree),dtype=np.int16))
for a,b,c in [(0,1,2),(100,300,500),(768,767,766)]:
    x,y,z=[(P[i],G[i]) for i in (a,b,c)]
    assert same(mul(mul(x,y),z),mul(x,mul(y,z)))
    assert same(mul(x,inv(x)),zero)
    assert same(mul(mul(x,x),x),zero)
    comm=mul(mul(mul(x,y),inv(x)),inv(y))
    assert not np.any(comm[0])
    assert np.array_equal(comm[1],reduce_z(wedge(x[0],y[0])))

out={
 'scope':'Actual N/(gamma3(N) N^3), N=ker(Gamma_0,5 -> signed Q192); no genuine associator-image claim',
 'base_order':192,'cover_generators':769,'cover_relators':1152,
 'linear_relation_rank':r,'linear_dimension':102,
 'central_free_dimension':nc,'central_relation_rank':len(cpiv),
 'central_dimension':len(cfree),'kernel_order_power_of_3':102+len(cfree),
 'full_quotient_order':'192 * 3^'+str(102+len(cfree)),
 'bch_half_mod3':2,'all_assertions_passed':True,
 'input_sha256':{str(Path(C.__file__).relative_to(ROOT)):hashlib.sha256(Path(C.__file__).read_bytes()).hexdigest(),
                 'ghost_code/check_fivepoint_signed_module.npz':hashlib.sha256((ROOT/'ghost_code/check_fivepoint_signed_module.npz').read_bytes()).hexdigest()},
 'runtime_seconds':round(time.time()-start_time,3)}
HERE.joinpath('build_signed_class2.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(HERE/'build_signed_class2.npz',
 relation_matrix=R,linear_projection=P,
 linear_pivots=np.array(piv),linear_free=np.array(free),
 relator_raw_central=B,relator_reduced_central=RB,
 central_relation_matrix=central_rel,central_relation_rref=CR,
 central_pivots=np.array(cpiv),central_free=np.array(cfree),
 generator_central=G,wedge_i=ii,wedge_j=jj)
print(json.dumps(out,indent=2),flush=True)
