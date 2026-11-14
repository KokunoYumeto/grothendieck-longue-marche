#!/usr/bin/env python3
"""Exact transvection identities and literal symplectic elimination words.

The four word letters are the original column transvections.  The saved
right-permutation models are compared through their exact transposes.
Only this program's new output file is written.
"""
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import gcd, factorial
from pathlib import Path
import json
import random
import time
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
STEM = 'bc_symplectic_integral_targets'
I = np.eye(4,dtype=np.int64)
J0 = np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]],dtype=np.int64)
a,b,c,d = [I[:,i] for i in range(4)]
vectors = (a,b,c-a,d)
nilpotents = tuple(np.outer(v,v@J0) for v in vectors)


def inverse_word(word):
    return tuple((i,-t) for i,t in reversed(word))


@lru_cache(None)
def word_matrix(word,m):
    ans = I.copy()
    for i,t in word:
        ans = ans @ (I+(t%m)*nilpotents[i-1]) % m
    return ans


def ta(t): return ((1,int(t)),)
def tb(t): return ((2,int(t)),)
def td(t): return ((4,int(t)),)


def wab(u,m):
    return ta(u)+tb(pow(int(u)%m,-1,m))+ta(u)


@lru_cache(None)
def tc(t,m):
    half = int(t)*pow(2,-1,m)%m
    h = wab(1,m)*2
    return h+((3,half),)+inverse_word(h)+((3,half),)+ta(-t)


def wcd(u,m):
    return tc(int(u)%m,m)+td(pow(int(u)%m,-1,m))+tc(int(u)%m,m)


def diag_ab(u,m): return wab(u,m)+wab(-1,m)
def diag_cd(u,m): return wcd(u,m)+wcd(-1,m)


@lru_cache(None)
def ua(t,m):
    h = wab(1,m)*2
    return h+((3,int(t)),)+inverse_word(h)+ta(-t)+tc(-int(t)%m,m)


@lru_cache(None)
def ub(t,m):
    w = wab(1,m)
    return w+ua(-int(t)%m,m)+inverse_word(w)


@lru_cache(None)
def nword(x,y,z,m):
    return ua(x,m)+ub(y,m)+tc((int(z)-int(x)*int(y))%m,m)


def nmatrix(x,y,z,m):
    w = int(x)*a+int(y)*b
    return (I+np.outer(w,c@J0)+np.outer(c,w@J0)+int(z)*np.outer(c,c@J0))%m


def eliminate_vector(v,m):
    """Return a literal word taking a primitive vector to c, over a local ring."""
    v = np.array(v,dtype=np.int64)%m
    original = v.copy()
    word = ()
    def apply(op):
        nonlocal v,word
        v = word_matrix(op,m)@v%m
        word = op+word
    if gcd(int(v[2]),m)!=1 and gcd(int(v[3]),m)!=1:
        if gcd(int(v[1]),m)==1:
            apply(nword(1,0,0,m))
        else:
            assert gcd(int(v[0]),m)==1
            apply(nword(0,1,0,m))
        assert gcd(int(v[2]),m)==1
    if gcd(int(v[3]),m)!=1:
        apply(wcd(1,m))
    t = int(v[3]); ti = pow(t,-1,m)
    apply(nword(-int(v[0])*ti%m,-int(v[1])*ti%m,0,m))
    assert int(v[0])==int(v[1])==0
    apply(tc(-int(v[2])*ti%m,m))
    apply(diag_cd(t,m))
    apply(wcd(1,m))
    assert np.array_equal(v,c%m)
    assert np.array_equal(word_matrix(word,m)@original%m,c%m)
    return word


def sl2_word(A,m):
    A = np.array(A,dtype=np.int64)%m
    aa,bb,cc,dd = map(int,A.ravel())
    assert (aa*dd-bb*cc)%m==1
    if gcd(aa,m)!=1:
        assert gcd(cc,m)==1
        w = wab(1,m)
        turned = word_matrix(w,m)[:2,:2]@A%m
        return inverse_word(w)+sl2_word(turned,m)
    ai = pow(aa,-1,m)
    word = tb(-cc*ai%m)+diag_ab(aa,m)+ta(bb*ai%m)
    assert np.array_equal(word_matrix(word,m)[:2,:2],A)
    return word


def parabolic_word(g,m):
    assert np.array_equal(g@c%m,c%m)
    A = g[:2,:2]%m
    aa,bb,cc,dd = map(int,A.ravel())
    linv = I.copy();linv[:2,:2]=np.array([[dd,-bb],[-cc,aa]])%m
    nn = linv@g%m
    x,y,z = map(int,nn[:3,3])
    assert np.array_equal(nn,nmatrix(x,y,z,m))
    word = sl2_word(A,m)+nword(x,y,z,m)
    assert np.array_equal(word_matrix(word,m),g%m)
    return word


def local_factor(g,m):
    h = eliminate_vector(g[:,2],m)
    k = word_matrix(h,m)@g%m
    word = inverse_word(h)+parabolic_word(k,m)
    assert np.array_equal(word_matrix(word,m),g%m)
    return word


def full_factor(g,m):
    powers = [int(p)**int(n) for p,n in sp.factorint(m).items()]
    word = ()
    for q in powers:
        local = local_factor(g%q,q)
        e = (m//q)*pow(m//q,-1,q)%m
        word += tuple((i,t*e%m) for i,t in local)
    assert np.array_equal(word_matrix(word,m),g%m)
    return word


def random_symplectic(m,rng):
    def vec(): return np.array([rng.randrange(m) for _ in range(4)],dtype=np.int64)
    def pair(u,v): return int(u@J0@v)%m
    while True:
        v,w = vec(),vec();q=pair(v,w)
        if gcd(q,m)==1: break
    w=w*pow(q,-1,m)%m
    while True:
        z,t=vec(),vec()
        z=(z-pair(v,z)*w+pair(w,z)*v)%m
        t=(t-pair(v,t)*w+pair(w,t)*v)%m
        q=pair(z,t)
        if gcd(q,m)==1: break
    t=t*pow(q,-1,m)%m
    g=np.column_stack((v,w,z,t))%m
    assert np.array_equal(g.T@J0@g%m,J0%m)
    return g


def main():
    start=time.time()
    dependencies=['e_symplectic_five_p5_model_root.npz','bc_symplectic_five_p7_model.npz',
                  'bc_symplectic_five_p5_target.json','bc_symplectic_five_p7_target.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in dependencies}
    js=sp.Matrix(J0);ii=sp.eye(4)
    aa,bb,cc,dd=[ii[:,i] for i in range(4)]
    T=lambda v,t:ii+t*v*v.T*js
    h=(T(aa,1)*T(bb,1)*T(aa,1))**2
    t=sp.Symbol('t')
    assert h*(cc-aa)==cc+aa
    assert T(cc+aa,t)*T(cc-aa,t)==T(cc,2*t)*T(aa,2*t)
    assert T(cc+aa,t)*T(aa,-t)*T(cc,-t)==ii+t*(aa*cc.T*js+cc*aa.T*js)
    x,y,z,xp,yp,zp=sp.symbols('x y z xp yp zp')
    N=lambda x,y,z:ii+(x*aa+y*bb)*cc.T*js+cc*(x*aa+y*bb).T*js+z*cc*cc.T*js
    assert sp.simplify(N(x,y,z)*N(xp,yp,zp)-N(x+xp,y+yp,z+zp+x*yp-y*xp))==sp.zeros(4)
    assert sp.simplify(N(x,y,z).T*js*N(x,y,z)-js)==sp.zeros(4)
    assert sp.simplify(N(x,0,0)*N(0,y,0)*N(-x,0,0)*N(0,-y,0)-N(0,0,2*x*y))==sp.zeros(4)
    J=sp.zeros(4)
    for i in range(3):J[i,i+1]=1;J[i+1,i]=-1
    es=[ii[:,i] for i in range(4)]
    C=sp.Matrix.hstack(es[0],es[1],es[0]+es[2],es[3])
    assert C.det()==1 and C.T*J*C==js
    original_T=[ii+v*v.T*J for v in es]
    right=[v.T for v in original_T]
    original_c=es[0]+es[2]
    for i in range(4):
        assert J.inv()*right[i]*J==original_T[i].inv()
        assert right[i].T*J.inv()*right[i]==J.inv()
        assert C.inv()*original_T[i]*C==T((aa,bb,cc-aa,dd)[i],1)
        if i<3:
            assert original_T[i]*original_c==original_c
            assert original_c.T*right[i]==original_c.T
    assert J*original_c==-es[3]
    for i in range(4):
        for j in range(i+1,4):
            if j==i+1:
                assert original_T[i]*original_T[j]*original_T[i]==original_T[j]*original_T[i]*original_T[j]
            else:
                assert original_T[i]*original_T[j]==original_T[j]*original_T[i]
    saved=[]
    for p,name in ((5,dependencies[0]),(7,dependencies[1])):
        frozen=np.load(HERE/name)
        assert np.array_equal(frozen['J'],np.array(J,dtype=np.int64))
        points=frozen['points'];idx={tuple(map(int,v)):j for j,v in enumerate(points)}
        for i in range(4):
            Ti=np.array(original_T[i],dtype=np.int64)%p
            assert np.array_equal(frozen['matrices'][i]%p,Ti)
            values=points@Ti.T%p
            sigma=np.array([idx[tuple(map(int,v))] for v in values])
            assert np.array_equal(sigma,frozen['sigma'][i])
        target=json.loads((HERE/f'bc_symplectic_five_p{p}_target.json').read_text())
        assert target['actual_common_quotient_order']==1
        order=p**3*(p*(p*p-1))
        assert target['new_four_strand_image_order']==order
        saved.append({'prime':p,'literal_permutation_entries':int(4*len(points)),
                      'four_strand_order':order,'saved_TL_joint_order':target['exact_joint_target_order']})
    vector_counts={}
    witnesses=[]
    for p in (5,7):
        count=0
        for v in product(range(p),repeat=4):
            if not any(v):continue
            word=eliminate_vector(v,p);count+=1
        assert count==p**4-1
        vector_counts[str(p)]=count
    rng=random.Random(560052)
    full_counts={}
    for m in (5,7,25,49,35,175,245):
        count=0
        for j in range(16):
            g=random_symplectic(m,rng)
            word=full_factor(g,m);count+=1
            if j==0:
                witnesses.append({'modulus':m,'matrix':g.tolist(),
                                  'literal_four_transvection_word':list(map(list,word)),
                                  'word_length':len(word)})
        full_counts[str(m)]=count
    assert factorial(96)>96**10
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==v for n,v in hashes.items())
    result={'status':'PASS_INTEGRAL_TRANVECTION_AND_EXACT_ELIMINATION_CERTIFICATE',
            'scope':'Polynomial identities, exact saved target maps, complete field-vector elimination, and literal local/CRT matrix factorizations. The uniform theorem is proved in E56.',
            'input_sha256':hashes,'all_original_artifacts_unchanged':True,
            'symplectic_basis':np.array(C,dtype=np.int64).tolist(),
            'column_fixed_vector':np.array(original_c,dtype=np.int64).ravel().tolist(),
            'right_column_fixed_vector':np.array(J*original_c,dtype=np.int64).ravel().tolist(),
            'half_turn_and_central_transvection_identities_exact':True,
            'Heisenberg_multiplication_and_symplecticity_exact':True,
            'literal_saved_target_comparisons':saved,
            'all_primitive_field_vectors_eliminated':vector_counts,
            'independently_constructed_symplectic_basis_factorizations':full_counts,
            'literal_word_witnesses':witnesses,
            'alternating_order_bound_verified':True,
            'seconds':round(time.time()-start,3)}
    (HERE/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='literal_word_witnesses'},indent=2),flush=True)


if __name__=='__main__':main()
