#!/usr/bin/env python3
"""Exact class-two maps for the degree-two and degree-three flex pencils.

This work calculation constructs the geometric quadratic comparison
from the elliptic-parent Schreier words.  It does not yet identify the
global arithmetic reference origin used by the B43 radical fibres.
"""
from pathlib import Path
from itertools import product
import ast,json
import numpy as np
import sympy as sp

source=ast.parse(Path('deliverable/code/b_elliptic_schreier.py').read_text())
names={'transversal','inv','reduce','step','rewrite','abelian','wedge','class_two','substitute'}
exec(compile(ast.Module(body=[x for x in source.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),'Schreier_functions','exec'))
cosets=list(product(range(3),repeat=2));edges={};words=[]
for c in cosets:
    for x in [1,2]:
        w=reduce(transversal(c)+[x]+inv(transversal(step(c,x))))
        if w:edges[(c,x)]=len(words)+1;words.append(w)
        else:edges[(c,x)]=0
pairs=[(i,j) for i in range(10) for j in range(i)]
sch=np.load('deliverable/code/b_elliptic_schreier_matrices.npz')
P=sp.Matrix(sch['original_basis_in_Schreier']);Pinv=P.inv()
def wedge_matrix(M):
    return sp.Matrix([[M[a,i]*M[b,j]-M[a,j]*M[b,i] for i,j in pairs] for a,b in pairs])
WPinv=wedge_matrix(Pinv)
def actual_action(parent_images):
    image=[rewrite(substitute(w,parent_images)) for w in words]
    C=Pinv*sp.Matrix(np.column_stack([abelian(w) for w in image]))*P
    # The exact chronological/fibre reversal from B40 negates degree2.
    B=-WPinv*sp.Matrix(np.column_stack([class_two(w)[1] for w in image]))*P/2
    return C,B
delta=[1,2,-1,-2]
sigma={1:[1,2,-1],2:[-2,-1]}
iota={1:[1,2,-1,-2,-1],2:[1,-2,-1]}
t=[1,1]
hinv={x:reduce(t+iota[x]+inv(t)) for x in [1,2]}
kh=reduce(t+substitute(t,iota)+delta)
for x in [1,2]:
    assert substitute(substitute([x],hinv),hinv)==reduce(kh+[x]+inv(kh))
assert substitute(kh,hinv)==kh
Ch,Bh=actual_action(hinv)
kv=Pinv*sp.Matrix(abelian(rewrite(kh)))
inner=sp.Matrix.hstack(*[sp.Matrix([kv[i]*Ch[j,k]-kv[j]*Ch[i,k] for i,j in pairs]) for k in range(10)])
# Actual h^2=Int(M_k^-1).  Multiplying h by Int(M_k^1/2) makes it order2.
Bh0=Bh+inner/2
assert Ch*Ch==sp.eye(10)
assert Bh0*Ch+wedge_matrix(Ch)*Bh0==sp.zeros(45,10)
Cs,Bs=actual_action(sigma)
assert Cs**3==sp.eye(10)

coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2),(0,0)]
peripheral=[]
for c in coords:
    w=rewrite(transversal(c)+delta+inv(transversal(c)))
    v,z2=class_two(w)
    peripheral.append((Pinv*sp.Matrix(v),-WPinv*sp.Matrix(z2)/2))

data=json.loads(Path('deliverable/code/b_dilog_origin_projections.json').read_text())
results=[]
for idx,(C,B,kill,normal) in enumerate([(Ch,Bh0,[3,5],[1,4]),(Cs,Bs,[8,7],[0,3])]):
    p=sp.Matrix(data[idx]['V_map'])
    assert p*C==p
    wp=sp.Matrix([[p[1,i]*p[0,j]-p[0,i]*p[1,j] for i,j in pairs]])
    coeff=(C-sp.eye(10)).T
    rhs=(-wp*B).T
    for target in kill+normal:
        v,z=peripheral[target]
        coeff=coeff.col_join(v.T)
        rhs=rhs.col_join(-wp*z)
    q,params=coeff.gauss_jordan_solve(rhs)
    assert params.rows==0
    q=q.T
    assert q*C+wp*B==q
    for target in kill+normal:
        v,z=peripheral[target]
        assert q*v+wp*z==sp.zeros(1,1)
    assert all(sp.denom(x)%3 for x in q)
    image_peripheral=[]
    for v,z in peripheral:
        image_peripheral.append([*(str(x) for x in p*v),str((q*v+wp*z)[0])])
    rec={'pencil':idx+1,'linear_map':p.tolist(),
         'quadratic_map':[str(x) for x in q],
         'coefficient_rank':int(coeff.rank()),
         'peripheral_images_log':image_peripheral,
         'killed':kill,'normalized':normal}
    results.append(rec)
    print(json.dumps(rec,default=str),flush=True)
Path('work/b_quadratic_pencil_maps.json').write_text(json.dumps({'status':'exact integral class-two comparison solved','results':results},indent=2,default=str)+'\n')
np.savez_compressed('work/b_quadratic_pencil_maps_matrices.npz',
    involution_linear=np.array(Ch,dtype=np.int64),
    involution_quadratic_twice=np.array(2*Bh0,dtype=np.int64),
    sigma_linear=np.array(Cs,dtype=np.int64),sigma_quadratic_twice=np.array(2*Bs,dtype=np.int64))
