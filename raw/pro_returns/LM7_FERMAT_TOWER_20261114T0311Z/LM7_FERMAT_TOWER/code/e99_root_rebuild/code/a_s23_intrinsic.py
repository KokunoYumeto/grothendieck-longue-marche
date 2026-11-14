#!/usr/bin/env python3
"""Exact intrinsic class-two sections unramified outside {2,3}.

All rational matrices are over Z_(3).  The actual cusp-action constants
are read from the frozen E95 certificate.  No handle-action constant is
assigned: the proof retains the genuine order-two Lie projector there.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import importlib.util
import itertools
import json
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mat(v):
    return s.Matrix([[s.Rational(a) for a in row] for row in v])


def enc(v):
    return [[str(a) for a in v.row(i)] for i in range(v.rows)]


def integral(v):
    return all(s.Rational(a).q % 3 for a in v)


def mod(a,n):
    a=s.Rational(a)
    return int(a.p)*pow(int(a.q),-1,n) % n


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-code',type=Path,
                    default=Path(__file__).resolve().parents[2]/'LM7_FERMAT_TOWER/code')
    args=ap.parse_args()
    base=args.source_code.resolve()
    here=Path(__file__).resolve().parent
    names=['e_unramified_sections.py','e_cusp_local_smith.py',
           'a_horizontal_full.py','e_wild_layers.json','a_cusp_kummer.json']
    frozen={name:sha(base/name) for name in names}
    hall=load('e99_hall',base/names[0]).Hall(2)
    smith=load('e99_smith',base/names[1])
    kernels=load('e99_kernels',base/names[2])
    wild=json.loads((base/names[3]).read_text())['layers']
    paths=json.loads((base/names[4]).read_text())
    J=mat(wild['1']['input_c'])
    I=s.eye(10)
    glue=s.Matrix([[0,-1],[2,-2],[1,0],[0,-2],
                   [1,-1],[2,0],[1,-2],[2,-1]])
    F=(-2*s.eye(2)).row_join(s.zeros(2,8)).col_join(
        (-2*glue).row_join(4*s.eye(8)))
    assert F*J==J*F
    Vp=s.Matrix.hstack((I+J)*I[:,0]/2,I[:,3]-I[:,4],
                       I[:,6]-I[:,7],I[:,8]-I[:,9])
    Wm=s.Matrix.hstack(I[:,2],I[:,5],I[:,3]+I[:,4],
                       I[:,6]+I[:,7],I[:,8]+I[:,9])
    Vm=((I-J)*I[:,1]/2).row_join(Wm)
    SV=Vp.row_join(Vm)
    SVi=SV.inv()
    assert integral(SVi) and J*Vp==Vp and J*Vm==-Vm
    G=s.eye(4)-(SVi*F*Vp)[:4,:]
    gs=smith.local_smith(G.tolist())
    GL,GR,GD=(mat(gs[k]) for k in ['left','right','diagonal_matrix'])
    assert gs['valuations']==[0,1,1,2]
    Grep=mat(gs['left_inverse'])
    expected_Grep=s.Matrix([[3,3,-3,-1],[1,0,0,0],
                           [-1,-1,0,0],[-1,-1,1,0]])
    assert Grep==expected_Grep
    print('PASS exact V eigenspaces and Frobenius gauge Smith 1,3,3,9',flush=True)

    ii=[k for k,d in enumerate(hall.degree) if d==2]
    ri={k:i for i,k in enumerate(ii)}
    def bracket(a,b):
        out=s.zeros(45,1)
        for i in range(10):
            for j in range(10):
                if a[i] and b[j]:
                    for k,n in hall.bracket(i,j).items():
                        out[ri[k]]+=a[i]*b[j]*n
        return out
    def wedge(A):
        return s.Matrix.hstack(*[
            bracket(A[:,hall.children[k][0]],A[:,hall.children[k][1]])
            for k in ii])
    pp=[(i,j) for i in range(10) for j in range(i) if (i<4)==(j<4)]
    mm=[(i,j) for i in range(10) for j in range(i) if (i<4)!=(j<4)]
    SM=s.Matrix.hstack(*[bracket(SV[:,i],SV[:,j]) for i,j in pp+mm])
    SMi=SM.inv()
    assert integral(SMi)
    Mp,Mm=SM[:,:21],SM[:,21:]
    Minv=SMi[21:,:]
    F2,J2=wedge(F),wedge(J)
    assert J2==mat(wild['2']['input_c'])
    assert J2*Mp==Mp and J2*Mm==-Mm
    D=Minv*(F2-4*s.eye(45))*Mm
    ds=smith.local_smith(D.tolist())
    DL,DR,DD=(mat(ds[k]) for k in ['left','right','diagonal_matrix'])
    assert ds['valuations']==[0]*8+[1]*9+[2]*6 and ds['free_rank']==1
    Di=s.diag(*[s.Rational(1,3**v) for v in ds['valuations']])
    Q=-Mm*DR[:,:23]*Di*DL[:23,:]*Minv
    w=bracket(3*I[:,0]+I[:,2:]*glue[:,0],
              3*I[:,1]+I[:,2:]*glue[:,1])
    assert F2*w==4*w and J2*w==-w
    assert w==-Mm*DR[:,23]/4
    print('PASS tame Smith 1^8,3^9,9^6,0 and primitive compact kernel',flush=True)

    labels=['A0','A1','A2','B0','B1','B2','C1','C2']
    K=[]
    for label in labels:
        c=paths['global_cusp_coefficients'][label]
        b=s.Matrix([s.Rational(x) for x in c['rational_coboundary']])
        z=s.Matrix([s.Rational(x) for x in c['Kummer_zeta']])
        K.append((F-I)*b+z)
    Kmat=s.Matrix.hstack(*K)
    assert integral(Kmat)
    def omega(U):
        return s.Matrix.hstack(*[
            4*sum((Wm[d+2,j]*bracket(U-K[d],I[:,d+2]) for d in range(8)),
                  s.zeros(45,1)) for j in range(5)])
    def etaF(v):
        assert v[:2,:]==s.zeros(2,1)
        return -4*sum((v[d+2]*bracket(K[d],I[:,d+2]) for d in range(8)),
                      s.zeros(45,1))
    def mul(a,b):
        x,m=a;y,n=b
        return x+y,m+n+bracket(x,y)/2
    def inverse(a):return -a[0],-a[1]
    def F_on_inertia(a):return F*a[0],F2*a[1]+etaF(a[0])
    def tame_word(U,v,m,z=None):
        if z is None:z=s.zeros(45,1)
        u=(U,z);n=(v,m)
        out=mul(mul(mul(u,F_on_inertia(n)),inverse(u)),(-4*v,-4*m))
        return out
    for i in range(5):
        v=Wm[:,i]
        for j in range(4):
            h=Vp[:,j]
            assert 4*bracket((I-F)*h,v)==-(F2-4*s.eye(45))*bracket(h,v)
    print('PASS actual Frob4 cusp constants and 20 gauge identities',flush=True)

    select=[i for i,v in enumerate(ds['valuations']) if v]
    mods=[3**ds['valuations'][i] for i in select]
    residues_all=np.asarray(list(itertools.product(range(9),repeat=5)),dtype=np.int64)
    records=[]
    special={(0,0,0):(1,1,1,1,1),(2,2,7):(1,0,0,0,0),
             (2,0,2):(0,1,0,0,0)}
    rays=[s.Matrix([1,1,1,1,1]),s.Matrix([1,0,0,0,0]),s.Matrix([0,1,0,0,0])]
    relation_checks=0
    for a,b,c in itertools.product(range(3),range(3),range(9)):
        digits=s.Matrix([0,a,b,c])
        Uc=Grep*digits
        U=Vp*Uc
        om=omega(U)
        assert J2*om==-om
        raw=DL*Minv*om
        assert raw[23:,:]==s.zeros(1,5)
        assert (F2-4*s.eye(45))*Q*om==-om
        X=s.eye(5)
        for row,n in zip(select,mods):
            r=s.Matrix([[mod(x,n) for x in raw.row(row)]])
            X=hermite_normal_form(X*kernels.row_kernel(r*X,n))
        Xi=X.inv()
        assert integral(9*Xi) and integral(Q*om*X)
        sx=smith.local_smith(X.tolist())
        is_special=(a,b,c) in special
        order=9 if is_special else 3
        ray=rays[c%3]
        generator=ray if is_special else 3*ray
        assert sx['valuations']==([0,2,2,2,2] if is_special else [1,2,2,2,2])
        assert X==hermite_normal_form((9*s.eye(5)).row_join(generator))
        want={tuple(int(x*k)%9 for x in generator) for k in range(order)}
        X9=np.asarray([[mod(x,9) for x in(9*Xi).row(i)] for i in range(5)],dtype=np.int64)
        got={tuple(int(x) for x in row) for row in
             residues_all[np.all((residues_all@X9.T)%9==0,axis=1)]}
        assert got==want
        for j in range(5):
            v=Wm*X[:,j];m=Q*om*X[:,j]
            z=Mp[:,(a+b+c+j)%21]
            assert tame_word(U,v,m,z)==(s.zeros(10,1),s.zeros(45,1))
            assert Xi*(X[:,j])==s.eye(5)[:,j]
            relation_checks+=1
        records.append({'Frobenius_digits':[a,b,c],'Frobenius_value':enc(U),
            'obstruction_matrix':enc(raw),'inertia_HNF':enc(X),'inertia_inverse':enc(Xi),
            'inertia_Smith':sx['valuations'],'residue_order':order,
            'residue_generator':enc(generator),'particular_columns':enc(Q*om*X)})
    assert sum(r['residue_order'] for r in records)==261
    # Actual rational cusp Frobenius values give precisely the three exceptional classes.
    cusp_classes={}
    for label,k in [('O',s.zeros(10,1)),('A0',K[0]),('B0',K[3])]:
        assert J*k==k
        dd=GL*(SVi*k)[:4,:]
        qdigits=[mod(dd[i],3**gs['valuations'][i]) for i in range(4)]
        cusp_classes[label]=qdigits[1:]
    assert cusp_classes=={'O':[0,0,0],'A0':[2,2,7],'B0':[2,0,2]}
    print('PASS all81 exact inertia lattices, 4782969 residues and405 actual tame words',flush=True)

    # Use rho=(gamma c gamma^-1 c), with kappa_3(rho)=2.
    Z=s.Matrix([[0,-1],[1,-1]])
    Pi=s.eye(2)+3*Z;Pibar=s.eye(2)+3*Z**2
    E=Pi*Pibar.inv()
    A=E.row_join(s.zeros(2,8)).col_join(((glue*E-glue)/3).row_join(s.eye(8)))
    L=A*J
    assert L*L==I and integral(A)
    Lp=s.Matrix.hstack((I+L)*I[:,0]/2,I[:,3]-I[:,4],I[:,6]-I[:,7],I[:,8]-I[:,9])
    Lm=((I-L)*I[:,1]/2).row_join(Wm)
    SL=Lp.row_join(Lm);SLi=SL.inv()
    assert integral(SLi) and L*Lp==Lp and L*Lm==-Lm
    B1=G.col_join(SLi[4:,:]*(I-A)*Vp)
    b1s=smith.local_smith(B1.tolist())
    assert b1s['valuations']==[0,1,1,1] and b1s['free_rank']==6
    A2=wedge(A);L2=A2*J2
    SML=s.Matrix.hstack(*[bracket(SL[:,i],SL[:,j]) for i,j in pp+mm])
    SMLi=SML.inv()
    MLp,MLm=SML[:,:21],SML[:,21:]
    assert integral(SMLi) and L2*MLp==MLp and L2*MLm==-MLm
    Htop=SMi[:21,:]*(s.eye(45)-F2)*Mp
    Hbottom=SMLi[21:,:]*(s.eye(45)-A2)*Mp
    H=Htop.col_join(Hbottom)
    hs=smith.local_smith(H.tolist())
    assert hs['valuations']==[0]*7+[1]*9+[2]*5 and hs['free_rank']==24
    HL,HR,HD=(mat(hs[k]) for k in ['left','right','diagonal_matrix'])
    HLi=mat(hs['left_inverse'])
    round_trips=0
    for n in range(40):
        coordinates=s.Matrix([0 if i<7 else
            ((n*(i+3)+i*i)%(3**hs['valuations'][i]) if i<21 else n-i)
            for i in range(45)])
        h=s.Matrix([s.Rational(n+2*i-9,2**(i%3)) for i in range(21)])
        raw=HLi*coordinates+H*h
        transformed=HL*raw
        got=s.Matrix([0 if i<7 else
            (mod(transformed[i],3**hs['valuations'][i]) if i<21 else transformed[i])
            for i in range(45)])
        assert got==coordinates
        correction=HR*s.Matrix([(got[i]-transformed[i])/HD[i,i] for i in range(21)])
        assert integral(correction) and raw+H*correction==HLi*got
        round_trips+=1
    print('PASS rational rho action and central Smith 1^7,3^9,9^5, free24;40 inverse round trips',flush=True)
    print('PASS full abelian gauge Smith 1,3,3,3 and exact HNF ray formulas',flush=True)

    v=9*(I[:,2]+I[:,5]);U0=s.zeros(10,1)
    omega0=4*sum((v[d+2]*bracket(U0-K[d],I[:,d+2]) for d in range(8)),s.zeros(45,1))
    m=Q*omega0
    assert integral(m) and tame_word(U0,v,m)==(s.zeros(10,1),s.zeros(45,1))
    assert J*v==-v and J2*m==-m
    assert v not in [s.zeros(10,1)]
    # Its abelian inertia is outside every actual cusp line, including the omitted O cusp.
    all_cusps=[I[:,d+2] for d in range(8)]+[-sum((I[:,d+2] for d in range(8)),s.zeros(10,1))]
    assert all(s.Matrix.hstack(v,d).rank()==2 for d in all_cusps)
    assert frozen=={name:sha(base/name) for name in names}
    print('PASS actual global non-metabelian-lift witness and all frozen dependency hashes',flush=True)
    out={'status':'PASS','input_sha256':frozen,
        'basis_order':['f1','f2']+labels,'Hall_degree2_pairs':[list(hall.children[k]) for k in ii],
        'J':enc(J),'Frobenius4':enc(F),'Vplus':enc(Vp),'Vminus':enc(Vm),
        'Wminus':enc(Wm),'Vsplit_inverse':enc(SVi),'Frobenius_gauge':enc(G),
        'Frobenius_gauge_Smith':smith.encode(gs),'Frobenius_representative':enc(Grep),
        'Mplus':enc(Mp),'Mminus':enc(Mm),'Msplit_inverse':enc(SMi),
        'Frobenius_wedge':enc(F2),'tame_matrix':enc(D),'tame_Smith':smith.encode(ds),
        'particular_inverse':enc(Q),'actual_cusp_Frobenius4':enc(Kmat),
        'compact_w':enc(w),'compact_kernel_inverse_factor':-4,
        'finite_moduli':[3]*9+[9]*6,'all81_strata':records,
        'exceptional_cusp_classes':cusp_classes,'accepted_residue_pairs':261,
        'all_residue_pairs_checked':81*9**5,'actual_tame_words_checked':relation_checks,
        'rho_Kummer3':2,'rho_proper_scalar':enc(E),'rho_matrix':enc(A),'rho_J':enc(L),
        'rho_J_Vplus':enc(Lp),'rho_J_Vminus':enc(Lm),'rho_J_Vsplit_inverse':enc(SLi),
        'full_abelian_gauge':enc(B1),'full_abelian_gauge_Smith':smith.encode(b1s),
        'rho_wedge':enc(A2),'rho_J_Mplus':enc(MLp),'rho_J_Mminus':enc(MLm),
        'rho_J_Msplit_inverse':enc(SMLi),'central_gauge':enc(H),
        'central_gauge_Smith':smith.encode(hs),'central_round_trips':round_trips,
        'nonlifting_witness':{'Frobenius':enc(U0),'inertia':enc(v),'central_inertia':enc(m)},
        'kernel_types':{'central_free':25,'central_C3':9,'central_C9':5,
                        'each_complete_cell_free':36,'complete_cells':81}}
    here.joinpath('a_s23_intrinsic.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':
    main()
