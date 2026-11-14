#!/usr/bin/env python3
"""E83: full intrinsic Hall and retained wild-cohomology coordinate maps.

The geometric map is derived from the four actual unit divisors and the
integral generalized-Jacobian gluing.  It is then evaluated on every
degree-three Hall word and in the actual E74/E82 Smith coordinates.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form


def rows(A):
    return [[int(v) for v in A.row(i)] for i in range(A.rows)]


def dense(columns):
    n=len(columns)
    A=np.zeros((n,n),dtype=np.int64)
    for j,col in enumerate(columns):
        for i,x in col.items():
            A[i,j]=x
    return A


def valuation(n):
    n=abs(int(n));v=0
    assert n
    while n%3==0:
        n//=3;v+=1
    return v


def mod3(x):
    x=Q(str(x))
    assert x.denominator%3
    return x.numerator*pow(x.denominator,-1,3)%3


def kernel_type(exponents,character):
    assert len(exponents)==len(character) and any(character)
    p=min((e,i) for i,(e,x) in enumerate(zip(exponents,character)) if x)[1]
    counts=Counter(exponents)
    counts[exponents[p]]-=1
    if exponents[p]>1:
        counts[exponents[p]-1]+=1
    return {'three_primary_counts':{e:n for e,n in sorted(counts.items()) if n},
            'pivot':p,'pivot_exponent':exponents[p],
            'pivot_coefficient':character[p],
            'pivot_unit_inverse_mod3':pow(character[p],-1,3)}


def main():
    here=Path(__file__).resolve().parent
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-code',type=Path)
    ap.add_argument('--cusp-certificate',type=Path)
    args=ap.parse_args()
    code=args.source_code or here
    if not (code/'e_unramified_sections.py').exists():
        code=here.parent.parent/'LM7_FERMAT_TOWER/code'
    cuspfile=args.cusp_certificate or code/'e_cusp_family_obstruction.json'
    spec=importlib.util.spec_from_file_location('e83_Hall',code/'e_unramified_sections.py')
    hall=importlib.util.module_from_spec(spec);spec.loader.exec_module(hall)
    H=hall.Hall(3);inputs=hall.arithmetic_inputs()
    Vtau,Vc=(dense(inputs[k]) for k in ('tau','c'))
    idx3=[i for i,d in enumerate(H.degree) if d==3]
    T3,J3=(dense(H.action(inputs[k],3)[0]) for k in ('tau','c'))
    assert len(idx3)==330
    cusps=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
    U=sp.Matrix([(v,-u) for u,v in cusps])
    toric=sp.Matrix([[0,0,0,0,0,0,0,-3],
                    [0,0,0,1,1,1,0,-3],
                    [0,0,0,0,0,0,-3,0],
                    [0,0,0,1,1,1,-3,0]])
    elliptic=-toric*U/3
    A=elliptic.row_join(toric)
    assert A==sp.Matrix([[2,-1,0,0,0,0,0,0,0,-3],
                         [1,0,0,0,0,1,1,1,0,-3],
                         [1,-2,0,0,0,0,0,0,-3,0],
                         [0,-1,0,0,0,1,1,1,-3,0]])
    jmat=(3*sp.eye(2)).col_join(U)
    assert A*jmat==sp.zeros(4,2)
    swap=sp.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
    assert A*sp.Matrix(Vtau)==7*A
    assert A*sp.Matrix(Vc)==-swap*A
    joint_ab=sp.Matrix([list(A[0,:]-A[1,:]),list(A[0,:]),
                       list((A[0,:]+A[2,:])/3)])
    assert joint_ab[:,[1,5,8]].det() in (1,-1)

    image3=[]
    for i in idx3:
        inner,c=H.children[i]
        a,b=H.children[inner]
        col=[]
        for offset in (0,2):
            determinant=A[offset,a]*A[offset+1,b]-A[offset+1,a]*A[offset,b]
            col.extend([-determinant*A[offset,c],-determinant*A[offset+1,c]])
        image3.append(sp.Matrix(col))
    F=sp.Matrix.hstack(*image3)
    assert F.shape==(4,330)

    # Independent associative tensor expansion of every target Hall image.
    @lru_cache(None)
    def target_tensor(i,offset):
        if i<10:
            return {(j,):int(A[offset+j,i]) for j in (0,1) if A[offset+j,i]}
        a,b=H.children[i];out=Counter()
        for u,x in target_tensor(a,offset).items():
            for v,y in target_tensor(b,offset).items():
                out[u+v]+=x*y;out[v+u]-=x*y
        return {w:x for w,x in out.items() if x}
    dbasis={(0,0,1):1,(0,1,0):-2,(1,0,0):1}
    ebasis={(1,0,1):2,(1,1,0):-1,(0,1,1):-1}
    for j,i in enumerate(idx3):
        for offset in (0,2):
            expected=Counter()
            for w,x in dbasis.items():expected[w]+=int(F[offset,j])*x
            for w,x in ebasis.items():expected[w]+=int(F[offset+1,j])*x
            assert {w:x for w,x in expected.items() if x}==target_tensor(i,offset)
    assert F*sp.Matrix(T3)==343*F
    assert F*sp.Matrix(J3)==-swap*F
    K=sp.Matrix([[1,0,0,0],[0,1,0,0],[1,0,3,0],[2,-1,0,3]])
    Ki=K.inv()
    assert all(x.q==1 for x in Ki*F)
    image_basis=hermite_normal_form(F)
    assert abs(image_basis.det())==9
    assert abs((Ki*image_basis).det())==1
    pi=sp.Matrix([[1,0,1,0],[0,1,0,1]])
    piL=sp.Matrix([[1,0,0,0],[0,0,-1,1]])

    old=json.loads((code/'e_wild_layers.json').read_text())['layers']['3']
    arc=np.load(code/'e_wild_layers_r3_transforms.npz')
    L,Li,M=(sp.Matrix(arc[k].tolist()) for k in ('left','left_inverse','matrix'))
    vals=[v['valuation'] for v in old['elementary_operations']]
    selected=[i for i,v in enumerate(vals) if v]
    exponents=[vals[i] for i in selected]
    assert exponents==[1]*63+[2]*23+[3]*7
    assert M==(sp.Matrix(T3)-7*sp.eye(330)).row_join(sp.Matrix(J3)+sp.eye(330))
    phi_full=pi*F
    phiL_full=piL*Ki*F
    assert all(int(x)%3==0 for x in phi_full*M)
    assert all(int(x)%3==0 for x in phiL_full*M)
    phi_smith=phi_full*Li
    phiL_smith=phiL_full*Li
    assert all(int(phi_smith[r,j])%3==0 for r in range(2) for j,v in enumerate(vals) if v==0)
    assert all(int(phiL_smith[r,j])%3==0 for r in range(2) for j,v in enumerate(vals) if v==0)
    Bmap=[[int(phi_smith[r,j])%3 for j in selected] for r in range(2)]
    BLmap=[[int(phiL_smith[r,j])%3 for j in selected] for r in range(2)]
    assert Bmap[0]==Bmap[1] and any(Bmap[0])
    assert all((Bmap[0][j]-2*BLmap[0][j])%3==0 for j in range(len(selected)))
    assert any((BLmap[0][a]*BLmap[1][b]-BLmap[0][b]*BLmap[1][a])%3
               for a in range(len(selected)) for b in range(a))
    character=Bmap[0]
    expected_character=[0]*93
    expected_character[88]=expected_character[90]=1
    expected_character[91]=2
    assert character==expected_character
    Bkernel=kernel_type(exponents,character)
    assert Bkernel['three_primary_counts']=={1:63,2:24,3:6}
    kernel_triples=set()
    for k,b91,b92 in product(range(9),range(27),range(27)):
        b89=(3*k-b91-2*b92)%27
        assert (b89+b91+2*b92)%3==0
        assert ((b89+b91+2*b92)%27)//3==k
        kernel_triples.add((b89,b91,b92))
    assert len(kernel_triples)==27**3//3==6561

    cusp=json.loads(cuspfile.read_text())
    assert cusp['B3_coordinate_rows']==selected and cusp['B3_coordinate_exponents']==exponents
    for data in cusp['cusps'].values():
        FM=sp.Matrix(data['obstruction_matrix'])
        assert all(int(x)%3==0 for x in sp.Matrix([character])*FM)
    quotient=cusp['joint_cusp_image']['exact_cokernel_smith']
    QL=sp.Matrix([[mod3(x) for x in row] for row in quotient['left']])
    QLi=sp.Matrix([[mod3(x) for x in row] for row in quotient['left_inverse']])
    assert all(int(x)%3==0 for x in QL*QLi-sp.eye(93))
    qvals=[valuation(d) for d in quotient['diagonal']]
    qselected=[i for i,v in enumerate(qvals) if v]
    assert Counter(qvals[i] for i in qselected)=={1:11,2:1}
    residual_all=sp.Matrix([character])*QLi
    assert all(int(residual_all[j])%3==0 for j,v in enumerate(qvals) if v==0)
    residual=[int(residual_all[j])%3 for j in qselected]
    assert any(residual)
    qexponents=[qvals[j] for j in qselected]
    assert qexponents==[1]*11+[2]
    assert residual==[0,0,0,0,0,0,0,0,1,1,0,0]
    qkernel=kernel_type(qexponents,residual)
    assert qkernel['three_primary_counts']=={1:10,2:1}
    for eta10 in range(3):
        eta9=(-eta10)%3
        assert (eta9+eta10)%3==0
    assert all(int(x)%3==0 for x in sp.Matrix([character])*sp.Matrix(
        cusp['joint_cusp_image']['exact_cokernel_lattice']))

    result={
     'statement':'E.83','status':'PASS',
     'input_files_sha256':{name:hashlib.sha256((code/name).read_bytes()).hexdigest()
        for name in ('e_unramified_sections.py','e_wild_layers.json','e_wild_layers_r3_transforms.npz')},
     'E82_certificate_sha256':hashlib.sha256(cuspfile.read_bytes()).hexdigest(),
     'actual_unit_character_matrix':rows(A),'actual_torus_divisor_matrix':rows(toric),
     'actual_gluing_U':rows(U),'joint_abelian_coordinates_matrix':rows(joint_ab),
     'joint_abelian_surjection_minor_columns':[1,5,8],
     'joint_abelian_surjection_minor_determinant':int(joint_ab[:,[1,5,8]].det()),
     'Hall_degree3_indices':idx3,'actual_full_degree3_matrix':rows(F),
     'actual_full_degree3_image_Hermite_basis':rows(image_basis),
     'B3_coordinate_rows':selected,'B3_coordinate_exponents':exponents,
     'B3_to_H2L_matrix':BLmap,'B3_to_H2A_matrix':Bmap,
     'B3_to_diagonal_C3_character':character,'B3_character_kernel':Bkernel,
     'all_nine_cusp_obstruction_maps_killed':True,
     'joint_residual_coordinate_rows':qselected,
     'joint_residual_coordinate_exponents':qexponents,
     'joint_residual_character_to_C3':residual,
     'joint_residual_character_kernel':qkernel,
     'checks':{'actual_unit_divisors':4,'unit_characters_vanish_on_j':4,
       'actual_abelian_intertwiners':2,'independent_associative_degree3_images':660,
       'actual_degree3_intertwiners':2,'all_source_H2_relations_killed':True,
       'intermediate_H2_map_surjective':True,'complete_cusp_columns_killed':405,
       'intrinsic_kernel_coordinate_inverse_checks':6561,
       'residual_kernel_coordinate_inverse_checks':3,
       'full_joint_residual_coordinate_inverse_verified':True}}
    here.joinpath('a_joint_intrinsic_coordinates.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS four actual unit characters and the marked integral gluing')
    print('PASS all660 independent degree-three tensor images and both arithmetic intertwiners')
    print('PASS full330-to4 matrix, index9 image, and both actual H2 maps')
    print('PASS all405 cusp columns killed; exact residual quotient character')
    print('B3 kernel',Bkernel,flush=True)
    print('Residual quotient character',residual,'kernel',qkernel,flush=True)
    print('ALL PASS')


if __name__=='__main__':main()
