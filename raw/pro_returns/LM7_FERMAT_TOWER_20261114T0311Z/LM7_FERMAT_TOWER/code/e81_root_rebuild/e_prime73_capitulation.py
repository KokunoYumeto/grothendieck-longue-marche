#!/usr/bin/env python3
"""E.81: exact ordinary noncapitulation and 27 S-correction ideals.

With --gp, rebuild the certified B_1 field, exact local/ray quotient, the
degree54 maximal order (no upper BNF), and every displayed ideal identity.
All successful stage outputs and binary data are retained. The separately
retained bounded searches are attempts, not principality certificates.
"""
from __future__ import annotations
import argparse
from itertools import product, combinations
import json
from math import gcd,lcm,prod
from pathlib import Path
import shutil
import subprocess
import tempfile

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
DEPENDENCIES=[('e_basechange_field','cyclotomic_base1'),
              ('e_basechange_local_norms','cyclotomic_base1_local_norms'),
              ('e_basechange_genus','cyclotomic_base1_genus')]
OWNED=['e_prime73_field','e_prime73_relations','e_prime73_artin',
       'e_prime73_candidates','e_prime73_export']

def dependency(name):
    for p in [HERE/(name+'.gp'),HERE.parent.parent/'research_e76/code'/(name+'.gp')]:
        if p.exists():return p
    raise FileNotFoundError(name)

def rebuild(gp):
    gp=str(Path(gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e81_exact_') as folder:
        root=Path(folder);dep=root/'research_norm_index/code';own=root/'research_e81/code'
        dep.mkdir(parents=True);own.mkdir(parents=True)
        stages=[(dependency(n),dep/(i+'.gp'),'e_prime73_dependency_'+n.removeprefix('e_basechange_')) for n,i in DEPENDENCIES]
        stages += [(HERE/(n+'.gp'),own/(n+'.gp'),n) for n in OWNED]
        for source,target,name in stages:
            shutil.copyfile(source,target)
            r=subprocess.run([gp,'-q',str(target)],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            (HERE/(name+'.out')).write_text(r.stdout)
            assert r.returncode==0,(name,r.returncode)
            assert '***   at top-level' not in r.stdout,r.stdout
            assert '***   user error' not in r.stdout,r.stdout
            assert 'DONE' in r.stdout or '"status":"PASS"' in r.stdout,name
        for p in own.glob('*.bin'):shutil.copyfile(p,HERE/p.name)

def integral(M):return all(x.q==1 for x in M)
def ratmat(rows):return sp.Matrix([[sp.Rational(*x) for x in row] for row in rows])
def reduced(v,ds):return tuple(int(a)%d for a,d in zip(v,ds))

def check_smith(r):
    H,L,R=[sp.Matrix(r[k]) for k in ['hnf','left','right']]
    Li,Ri=[sp.Matrix(r[k]) for k in ['left_inverse','right_inverse']]
    ds=r['diagonal'];eye=sp.eye(H.rows)
    assert L*H*R==sp.diag(*ds)
    assert L*Li==Li*L==R*Ri==Ri*R==eye
    assert integral(Li) and integral(Ri)
    assert abs(L.det())==abs(R.det())==1 and abs(H.det())==prod(ds)
    return H,L,R,ds

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--gp');args=p.parse_args()
    if args.gp:rebuild(args.gp)
    raw=(HERE/'e_prime73_export.out').read_text();assert '***   at top-level' not in raw
    recs=[json.loads(s) for s in raw.splitlines() if s.startswith('{')]
    assert recs[-1]['status']=='PASS'
    rec={r['type']:r for r in recs if r['type'] not in ['candidate','smith']}
    smith={r['name']:check_smith(r) for r in recs if r['type']=='smith'}
    assert len(smith)==4
    base,ext,rel,ar=[rec[k] for k in ['base_field','extension','relations','artin']]
    assert base['class_group']==[3,3] and base['prime_class']==[2,1]
    assert abs(sp.Matrix(base['prime73']).det())==73
    assert ext['degree']==54 and ext['discriminant']==-3**135*17**48
    assert ext['relative_index']==1 and ext['extended_prime_norm']==73**3 and ext['cube_verified']
    assert ext['upper_prime_data']==[[3,18,1]]*3+[[17,9,2]]*3
    V=sp.Matrix(rel['base_valuation']);M=sp.Matrix(rel['matrix'])
    assert M==(3*V).row_join(sp.Matrix([0,0,0,1,1,1]))
    H=smith['s_relations'][0]
    assert H==hermite_normal_form(M) and H.det()==729
    assert H==M[:,[0,1,2,3,4,6]]
    assert [d for d in smith['s_relations'][3] if d>1]==[9,3,3,3,3]
    C=sp.Matrix(ar['s_map']);target=sp.Matrix(ar['target']);origin=sp.Matrix(ar['origin'])
    ds=ar['cyclic'];D=sp.diag(*ds);K=sp.Matrix(ar['kernel']);Ki=ratmat(ar['kernel_inverse'])
    assert K*Ki==Ki*K==sp.eye(6) and K.det()==27
    assert K*sp.Matrix(ar['quotient_matrix'])==H
    assert smith['correction_quotient'][3]==[3,3,3,1,1,1]
    assert reduced(target,ds)==(6,0,0,0)+tuple(0 for _ in ds[4:])
    assert lcm(*(d//gcd(d,int(a)) for d,a in zip(ds,target)))==3
    active=sp.Matrix([[3,3,3,0,3,6],[1,1,1,2,2,2],[0,0,0,2,2,2],[1,1,1,0,0,0]])
    assert sp.Matrix(4,6,lambda i,j:int(C[i,j])%ds[i])==active
    assert reduced(target+C*origin,ds)==(0,)*len(ds)
    assert all(int(z)%ds[i]==0 for i in range(len(ds)) for z in (C*K)[i,:])
    image=smith['s_artin_image'][0]
    assert image==hermite_normal_form(D.row_join(C))
    assert abs(D.det()/image.det())==27

    # Exhaust the complete genus congruence quotient, not an ideal search.
    congruences=0
    for v in product(range(3),repeat=6):
        vv=sp.Matrix(v);value=reduced(target+C*vv,ds)==(0,)*len(ds)
        expected=(sum(v[:3])%3==0 and (v[3]-v[5]+1)%3==0 and (v[4]-v[5]-1)%3==0)
        assert value==expected
        assert integral(Ki*(vv-origin))==value
        congruences+=1

    # Verify every literal base ideal generator in the actual integral basis.
    x=sp.symbols('x');P=sp.Poly(sum(int(c)*x**i for i,c in enumerate(base['polynomial'])),x,domain=sp.QQ)
    assert P.degree()==18
    def poly(v):return sp.Poly(sum(sp.Rational(*q)*x**i for i,q in enumerate(v)),x,domain=sp.QQ)
    basis=[poly(v) for v in base['basis']]
    Z=sp.Matrix(18,18,lambda i,j:basis[j].nth(i));Zi=Z.inv()
    def principal_matrix(v):
        f=poly(v);columns=[]
        for z in basis:
            p=(f*z).rem(P);columns.append(Zi*sp.Matrix([p.nth(i) for i in range(18)]))
        return sp.Matrix.hstack(*columns)
    fm=principal_matrix(base['cube_generator'])
    assert abs(fm.det())==73**3
    candidates=[r for r in recs if r['type']=='candidate'];assert len(candidates)==27
    literal=0
    for r in candidates:
        a,b,c=r['parameters'];v=sp.Matrix(r['exponents'])
        assert v==sp.Matrix([3*a+2*b+2*c,b,c,-1,1,0])
        assert r['cube_verified'] and reduced(target+C*v,ds)==(0,)*len(ds)
        N=ratmat(r['base_norm_ideal']);A=principal_matrix(r['base_cube_generator'])
        T=N.inv()*A
        assert integral(T) and abs(T.det())==1
        assert abs(N.det())==sp.Integer(73)**3*sp.Integer(3)**(3*(a+b+c))
        literal+=1
    distinct=0;Hi=H.inv()
    for r,s in combinations(candidates,2):
        assert not integral(Hi*(sp.Matrix(r['exponents'])-sp.Matrix(s['exponents'])))
        distinct+=1

    # Every possible affine class map F3^3 -> a group of order <=3 has
    # 0,9 or27 zeros; this is the exact remaining principality count bound.
    count_values=set();affine_cases=0
    for coeff in product(range(3),repeat=4):
        zeros=sum((coeff[0]+sum(a*b for a,b in zip(coeff[1:],v)))%3==0 for v in product(range(3),repeat=3))
        count_values.add(zeros);affine_cases+=1
    assert count_values=={0,9,27}
    summary={'statement':'E.81','status':'PASS','full_integer_smith_inverse_certificates':4,
      'literal_principal_s_relations':7,'genus_congruence_checks':congruences,
      'literal_candidate_cube_generators':literal,'distinct_candidate_pairs':distinct,
      'affine_principality_count_maps':affine_cases,'ordinary_extended_prime_class_order':3,
      'ordinary_extended_prime_artin':[6,0,0,0],'ramified_artin_image_order':27,
      'ambiguous_group_order':81,'ambiguous_genus_kernel_order_divides':3,
      'proved_s_relation_quotient':[9,3,3,3,3],'correction_quotient':[3,3,3],
      'possible_principal_candidate_counts':[0,9,27],
      's_capitulation':'unevaluated; a bounded reduction search is not used as a nonprincipality proof',
      'h':'unevaluated'}
    (HERE/'e_prime73_capitulation.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
