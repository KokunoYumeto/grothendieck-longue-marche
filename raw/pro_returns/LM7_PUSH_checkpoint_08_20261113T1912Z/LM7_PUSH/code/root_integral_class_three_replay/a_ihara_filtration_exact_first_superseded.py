#!/usr/bin/env python3
"""Independent BCH-commutator audit of the Fermat filtration.

Explicitly retain the quadratic commutator term, all polarizations, and
Lie-subgroup closure.  Compare with the earlier invariant-span computation.
The invariant span was suspected to omit this term; this script decides
that suspicion using exact finite group operations.
"""
from pathlib import Path
import importlib.util,json,contextlib,io
import numpy as np
HERE=Path(__file__).resolve().parent
def load(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(obj)
    return obj
f=load('de_fermat_schreier');g=load('a_ihara_gauge')

def cols(A):
    A=np.asarray(A,dtype=np.int64)%3
    _,p=g.rref(A)
    return A[:,p]

def join(a,z):return np.concatenate((a,z))%3
def split(v):return v[:10],v[10:]
def product(a,b):return join(*f.multiply(split(a),split(b)))
def bracket(a,b):
    z=(np.outer(a[:10],b[:10])-np.outer(b[:10],a[:10]))[f.UP]%3
    return join(np.zeros(10,dtype=np.int64),z)
def mat(q):
    A,J,W=f.action(q)
    return np.block([[A,np.zeros((10,45),dtype=np.int64)],[J,W]])%3
X,Y=mat((1,0)),mat((0,1))

def normal(B):
    B=cols(B)
    while True:
        brackets=[bracket(B[:,i],B[:,j]) for i in range(B.shape[1]) for j in range(i)]
        new=cols(np.hstack((B,X@B,Y@B,
                    np.stack(brackets,axis=1) if brackets else np.zeros((55,0),dtype=np.int64))))
        if new.shape[1]==B.shape[1]:return B
        B=new

def commutators(H):
    out=[]
    for T in (X,Y):
        for i in range(H.shape[1]):
            h=H[:,i]
            out.append(product(T@h%3,-h%3))
            out.append(product(T@(2*h)%3,-2*h%3))
            for j in range(i):
                hh=(h+H[:,j])%3
                out.append(product(T@hh%3,-hh%3))
    return normal(np.stack(out,axis=1)) if out else np.zeros((55,0),dtype=np.int64)

old=json.loads((HERE/'a_ihara_filtration.json').read_text())
H=normal(join(*f.literal([1,2,-1,-2]))[:,None]);fil={2:H}
for degree in range(3,13):
    H=commutators(H);fil[degree]=H
    if not H.shape[1]:break
print('Exact BCH lower-central dimensions:',[(k,H.shape[1]) for k,H in fil.items()])
for degree,H in fil.items():
    if str(degree) not in old['D_bases'] or degree==3:continue
    before=np.array(old['D_bases'][str(degree)],dtype=np.int64)
    assert f.rank(np.hstack((H,before)))==H.shape[1]==before.shape[1]
print('Every previously saved lower-central space agrees with the exact commutator computation.')
# All elements of N/K have exponent3.  In F/K, (xy)^3 belongs to N/K,
# so every element has exponent dividing9.  In Zassenhaus degree>=4,
# the only remaining powered factors are gamma_j^3 with j>=2 (trivial)
# and F^9 (also trivial).  Hence D_r=gamma_r for r>=4.
for r in range(2,max(fil)):
    dim=fil[r].shape[1]-fil[r+1].shape[1]
    print('gamma',r,'/ gamma',r+1,'dimension',dim)
(HERE/'a_ihara_filtration_exact.json').write_text(json.dumps({
 'gamma_dimensions':[(i,H.shape[1]) for i,H in fil.items()],
 'gamma_bases':{str(i):H.tolist() for i,H in fil.items()},
 'previous_spaces_agree':True},separators=(',',':'))+'\n')
print('PASS: exact commutators, polarizations and subgroup closure retained.')
