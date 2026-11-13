#!/usr/bin/env python3
"""E.91: ordinary class actions and the exact next genus/transvection maps.

--gp PATH rebuilds the certified B1 arithmetic and every ninth-genus input
in an empty temporary directory. It never starts a BNF in B2 or L2.
"""
from __future__ import annotations
import argparse
from itertools import product
import json
from math import gcd, lcm, prod
from pathlib import Path
import shutil
import subprocess
import tempfile
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
STAGES=[('e_basechange_field','cyclotomic_base1'),
        ('e_basechange_local_norms','cyclotomic_base1_local_norms'),
        ('e_basechange_unit_symbols','cyclotomic_base1_unit_symbols'),
        ('e_basechange_genus','cyclotomic_base1_genus'),
        ('e_basechange_ninth_norms','cyclotomic_base1_ninth_norms'),
        ('e_basechange_ninth_genus','cyclotomic_base1_ninth_genus'),
        ('e_basechange_ninth_transfer','cyclotomic_base1_ninth_transfer'),
        ('e_basechange_export','cyclotomic_base1_export')]

def locate(name):
    for p in (HERE/(name+'.gp'), HERE.parent.parent/'research_e76/code'/(name+'.gp')):
        if p.exists(): return p
    raise FileNotFoundError(name)

def rebuild(gp):
    gp=str(Path(gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e91_exact_') as td:
        root=Path(td); dep=root/'research_norm_index/code'; own=root/'research_e91/code'
        dep.mkdir(parents=True); own.mkdir(parents=True)
        tasks=[(locate(a),dep/(b+'.gp'),'e_ordinary_dependency_'+a) for a,b in STAGES]
        tasks.append((HERE/'e_ordinary_refinement.gp',own/'e_ordinary_refinement.gp','e_ordinary_refinement_gp'))
        for source,dest,label in tasks:
            shutil.copyfile(source,dest)
            p=subprocess.run([gp,'-q',str(dest)],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            (HERE/(label+'.out')).write_text(p.stdout)
            assert p.returncode==0,(label,p.returncode)
            assert '***   at top-level' not in p.stdout,p.stdout
            assert '***   user error' not in p.stdout,p.stdout
            assert 'DONE' in p.stdout or '"status":"PASS"' in p.stdout or 'CLASS_GENERATORS' in p.stdout,label
            print(label,'PASS',flush=True)
        shutil.copyfile(own/'e_ordinary_refinement.bin',HERE/'e_ordinary_refinement.bin')

def modmat(A,ds): return s.Matrix(A.rows,A.cols,lambda i,j:int(A[i,j])%ds[i])
def vecmod(v,ds): return tuple(int(x)%d for x,d in zip(v,ds))
def integral(A): return all(x.q==1 for x in A)
def rankmod(A,p):
    R=[[int(x)%p for x in row] for row in A.tolist()]; r=0
    for j in range(A.cols):
        pivot=next((i for i in range(r,len(R)) if R[i][j]),None)
        if pivot is None: continue
        R[r],R[pivot]=R[pivot],R[r]
        inv=pow(R[r][j],-1,p);R[r]=[(x*inv)%p for x in R[r]]
        for i in range(len(R)):
            if i!=r:
                a=R[i][j];R[i]=[(x-a*y)%p for x,y in zip(R[i],R[r])]
        r+=1
        if r==len(R): break
    return r

def partitions(n,maxpart=None):
    if n==0:
        yield ();return
    if maxpart is None: maxpart=n
    for x in range(min(n,maxpart),0,-1):
        for tail in partitions(n-x,x): yield (x,)+tail

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--gp');arg=ap.parse_args()
    if arg.gp: rebuild(arg.gp)
    text=(HERE/'e_ordinary_refinement_gp.out').read_text()
    assert '***   at top-level' not in text
    rr=[json.loads(x) for x in text.splitlines() if x.startswith('{')]
    G,L,end=rr; assert end['status']=='PASS'
    ds=G['orders']; D=s.diag(*ds); K=s.Matrix(G['kernel_basis']);P=s.Matrix(G['presentation'])
    U=s.Matrix(G['smith_left']);V=s.Matrix(G['smith_right']);ad=G['smith_diagonal']
    assert K*P==D and abs(K.det())==9 and U*P*V==s.diag(*ad)
    assert U*s.Matrix(G['smith_left_inverse'])==s.eye(4)
    assert V*s.Matrix(G['smith_right_inverse'])==s.eye(4)
    assert integral(U.inv()) and integral(V.inv())
    assert ad==[9,9,3,1]
    chi=s.Matrix([G['kummer_character']]); assert vecmod(chi*K,[9]*4)==(0,0,0,0)
    J=s.Matrix([[-2,2,3],[1,0,0],[0,1,0],[0,0,1]])
    proj=s.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    orders=(9,9,3); A=s.diag(*orders)
    assert proj*J==s.eye(3) and modmat(chi*J,[9])==s.zeros(1,3)
    H0=s.Matrix(G['h_genus']);H=modmat(proj*H0*J,orders)
    assert H==s.Matrix([[4,3,0],[8,7,6],[1,0,1]])
    assert modmat(H0*J-J*H,ds)==s.zeros(4,3)
    assert modmat(H**3-s.eye(3),orders)==s.zeros(3)
    C=s.Matrix(G['ramified_columns']);C0=proj*C;pv=proj*s.Matrix(G['prime73'])
    expected=s.Matrix([[6,6,6,6,3,0],[0,6,3,5,8,5],[2,2,2,1,1,1]])
    assert modmat(C0,orders)==expected
    for j in range(6):
        nxt=(j//3)*3+(j+1)%3
        assert vecmod(H*C0[:,j]-C0[:,nxt],orders)==(0,0,0)
    assert vecmod(pv,orders)==(1,8,2)
    ram=hermite_normal_form(s.Matrix.hstack(A,C0))
    assert ram==s.diag(3,1,1)
    assert abs(A.det()/ram.det())==81
    assert hermite_normal_form(s.Matrix.hstack(ram,pv))==s.eye(3)
    R=s.Matrix(G['ramified_hnf'])
    assert hermite_normal_form(s.Matrix.hstack(D,C))==R
    RU=s.Matrix(G['ramified_smith_left']);RV=s.Matrix(G['ramified_smith_right'])
    assert RU*R*RV==s.diag(*G['ramified_smith_diagonal'])
    HC=s.Matrix(G['h_coinvariant_hnf']);HU=s.Matrix(G['h_coinvariant_left']);HV=s.Matrix(G['h_coinvariant_right'])
    assert HU*HC*HV==s.diag(*G['h_coinvariant_diagonal'])
    assert G['h_coinvariant_diagonal']==[3,3,1,1]
    hco=hermite_normal_form(s.Matrix.hstack(A,H-s.eye(3)))
    assert abs(hco.det())==9
    roundtrips=0
    for y,z,t in product(range(9),range(9),range(3)):
        a=s.Matrix([y,z,t]);x=modmat(J*a,ds)
        assert vecmod(proj*x,orders)==(y,z,t)
        b=modmat(U*K.inv()*x,ad);back=modmat(K*U.inv()*b,ds)
        assert back==x
        assert int((chi*x)[0])%9==0
        roundtrips+=1
    q=s.Matrix([6,0,2]);tt=s.Matrix([6,5,1]);NH=s.eye(3)+H+H**2
    cube_rel=A.inv()*(H**3-s.eye(3));qnorm=A.inv()*NH*q;tnorm=A.inv()*NH*tt
    assert integral(cube_rel) and integral(qnorm) and integral(tnorm)
    assert [int(x) for x in qnorm]==[34,80,14]
    assert [int(x) for x in tnorm]==[52,119,18]
    extchecks=0;liftchecks=0;allowed=[]
    for a,b,c in product(range(3),repeat=3):
        rel=s.Matrix([[a,b,c]])
        preserve=b==0
        cube=vecmod(rel*cube_rel,[3]*3)
        good=preserve and cube==(0,0,0)
        assert good==(a==b==0)
        extchecks+=1
        if good:
            allowed.append([a,b,c])
            for e,f,k in product(range(3),repeat=3):
                corr=s.Matrix([[e,f,k]])
                assert vecmod(corr*NH,[3]*3)==(0,0,0)
                nq=int((rel*qnorm+corr*(2*s.eye(3)+H)*q)[0])%3
                n3q=int((rel*A.inv()*(3*q))[0])%3
                assert nq==n3q==2*c%3
                nt=int((rel*tnorm+corr*(2*s.eye(3)+H)*tt)[0])%3
                assert nt==0
                liftchecks+=1
    vals=s.Matrix(L['valuation_matrix']);symbols=s.Matrix(L['symbol_matrix']);classes=s.Matrix(L['upper_S_class_matrix']);Z=s.Matrix(L['principal_kernel'])
    assert modmat(classes*vals*Z,[3]*3)==s.zeros(3,Z.cols)
    assert rankmod(Z,3)==Z.cols==13
    assert rankmod(classes*vals,3)==2
    assert modmat(symbols*Z,[3]*6)==s.Matrix(L['lifted_symbols'])
    assert rankmod(symbols*Z,3)==L['rank']==3
    assert rankmod(symbols[:,:9],3)==L['base_unit_rank']==3
    checked=0;valid=0;type_counts={}
    for aa in range(1,5):
        accepted=set()
        for pp in partitions(aa+2):
            od=tuple(3**v for v in pp)
            triples=[tuple((3 if j==i else 0)%od[j] for j in range(len(od))) for i in range(len(od))]
            for v in product(*(range(d) for d in od)):
                checked+=1
                if lcm(*(d//gcd(d,x) for d,x in zip(od,v)))!=3**aa: continue
                cyclic={tuple(k*x%d for d,x in zip(od,v)) for k in range(3**aa)}
                if not all(x in cyclic for x in triples): continue
                accepted.add(pp);valid+=1
                in3=all(x%3==0 for x in v)
                assert in3==(pp==(aa+1,1))
        assert accepted=={(aa+1,1),(aa,1,1)}
        type_counts[str(aa)]=[list(x) for x in sorted(accepted,reverse=True)]
    ans=dict(status='PASS',statement='E.91',genus_orders=ds,
             actual_kummer_character=G['kummer_character'],relative_genus_orders=list(orders),
             simple_inclusion=J.tolist(),simple_projection=proj.tolist(),
             h_relative=H.tolist(),ramified_relative=expected.tolist(),prime73_relative=[1,8,2],
             ramified_relative_image_order=81,genus_roundtrips=roundtrips,
             exact_smith_systems=3,extension_presentations_checked=extchecks,
             allowed_extension_parameters=allowed,h_lifts_checked=liftchecks,
             q_norm_relation_coefficients=[int(x) for x in qnorm],
             t_norm_relation_coefficients=[int(x) for x in tnorm],
             exact_B3_exponent=9,B3_possible_orders=[243,729],
             B3_possible_cyclic_factors=[[9,9,3],[9,9,9],[9,9,3,3]],
             lower_group_cases_checked=checked,valid_original_prime_cases=valid,
             lower_group_alternatives=type_counts,unit_lifting_rank=3,
             unit_lifting_kernel_dimension=13,
             remaining='The actual transvection and the Q-prime triple in its order-at-most-three kernel remain unevaluated; no value of h is inferred.')
    def integer(x):
        if isinstance(x,s.Integer):return int(x)
        raise TypeError(type(x).__name__)
    out=json.dumps(ans,indent=2,default=integer)
    (HERE/'e_ordinary_refinement.json').write_text(out+'\n')
    print(out)

if __name__=='__main__':main()
