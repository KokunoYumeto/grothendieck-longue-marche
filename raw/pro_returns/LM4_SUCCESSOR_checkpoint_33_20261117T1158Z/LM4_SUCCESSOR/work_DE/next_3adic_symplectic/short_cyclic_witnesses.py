"""Short actual cyclic commutator witnesses for the mod9 common module."""
from pathlib import Path
import json,itertools
import numpy as np
import first_lift as f
HERE=Path(__file__).resolve().parent
C=json.loads((HERE/'C5_lift.json').read_text())
gg=[np.array(a,dtype=np.int64) for a in C['generator_mod9_matrices']]
ii=[f.inv(a) for a in gg];eye=f.eye
def red(w):
    out=[]
    for j in w:
        if out and out[-1]==-j:out.pop()
        else:out.append(j)
    return out
def wi(w):return[-j for j in w[::-1]]
def comm(a,b):return red(a+b+wi(a)+wi(b))
def evalw(w):
    out=eye.copy()
    for j in w:out=out@(gg[j-1] if j>0 else ii[-j-1])%9
    return f.norm(out)
def order3(a):
    b=eye.copy()
    for d in range(1,145):
        b=f.norm(b@a)
        if np.array_equal(b%3,eye):return d
    raise AssertionError
orders=[order3(a) for a in gg]
print('C5 source generator mod3 projective orders:',orders,flush=True)
pool={}
def add(w,desc):
    w=red(w)
    if not w:return
    a=evalw(w)
    assert np.array_equal(a%3,eye)
    v=np.zeros(6,dtype=np.int64)
    for j in w:v[abs(j)-1]+=1 if j>0 else -1
    assert not np.any(v)
    X=(((a-eye)%9)//3).reshape(-1)
    if not np.any(X):return
    pool[tuple(w)]=(X,desc)
for i,j in itertools.permutations(range(6),2):
    add(comm([i+1],[j+1]*orders[j]),['commutator',i,1,j,orders[j]])
for i,j in itertools.combinations(range(6),2):
    for a in range(1,4):
        for b in range(1,4):
            w=comm([i+1]*a,[j+1]*b);d=order3(evalw(w))
            add(w*d,['commutator_power',i,a,j,b,d])
items=sorted(pool.items(),key=lambda item:(len(item[0]),item[0]))
basis=[];chosen=[]
for w,(X,desc) in items:
    old=len(basis)
    if f.span(np.array(basis+[X]).T)[0].shape[1]>old:
        basis.append(X);chosen.append((list(w),desc))
    if len(basis)==9:break
assert len(basis)==9
V=np.array(basis,dtype=np.int64).T
assert f.span(np.hstack([V,np.array(C['full_basis'])]))[0].shape[1]==9
print('PASS nine short commutator words span the entire cyclic congruence image')
for i,(w,desc) in enumerate(chosen):print(i,'length',len(w),'description',desc)
R=json.loads((HERE/'rigid_lift_certificate.json').read_text())
N=np.array(R['normal_h_basis'],dtype=np.int64)
X,coordinates=f.intersection(N,V)
assert X.shape[1]==3
nw=R['normal_h_basis_actual_source_words']
Tgens=[np.array(a,dtype=np.int64) for a in json.loads((HERE/'T_lift.json').read_text())['generator_mod9_matrices']]
Ti=[f.inv(a) for a in Tgens]
def evalt(w):
    a=eye.copy()
    for j in w:a=a@(Tgens[j-1] if j>0 else Ti[-j-1])%9
    return f.norm(a)
matches=[]
for j in range(3):
    a=[];b=[]
    for i,w in enumerate(nw):a=red(a+w*int(coordinates[i,j]))
    for i,(w,_) in enumerate(chosen):b=red(b+w*int(coordinates[len(nw)+i,j]))
    assert np.array_equal(evalt(a),evalw(b))
    assert np.array_equal(evalt(a),(eye+3*X[:,j].reshape(10,10))%9)
    matches.append({'T_word':a,'C5_word':b})
    print('new matched source lengths',len(a),len(b))
_,piv=f.rref(X.T);minor=X[piv,:]
mi=np.array(__import__('sympy').Matrix(minor).inv_mod(3),dtype=np.int64)
brackets={}
for i,j in itertools.combinations(range(3),2):
    a=X[:,i].reshape(10,10);b=X[:,j].reshape(10,10)
    z=(a@b-b@a).reshape(-1)%3;v=mi@z[piv]%3
    assert np.array_equal(X@v%3,z)
    brackets[f'{i},{j}']=v.tolist()
print('new Lie brackets',brackets)
out={'cyclic_basis_words':[w for w,_ in chosen],'cyclic_basis_descriptions':[d for _,d in chosen],
     'cyclic_basis':V.tolist(),'common_basis':X.tolist(),'common_coordinates':coordinates.tolist(),
     'common_actual_words':matches,'common_coordinate_entries':piv,
     'common_coordinate_minor':minor.tolist(),'Lie_brackets':brackets}
(HERE/'short_word_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS short actual first-lift witnesses')
