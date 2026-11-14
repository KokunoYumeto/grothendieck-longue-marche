#!/usr/bin/env python3
"""E.84: exact ordinary capitulation from actual normalizer actions.

--gp rebuilds the certified base field and E.81 ideal/genus data, then the
actual automorphisms, prime permutations, and six literal class images.
It constructs a degree54 maximal order, never an upper BNF.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import product
import json
from math import gcd,lcm,prod
from pathlib import Path
import shutil
import subprocess
import tempfile

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
DEP76=[('e_basechange_field','cyclotomic_base1'),
       ('e_basechange_local_norms','cyclotomic_base1_local_norms'),
       ('e_basechange_genus','cyclotomic_base1_genus')]
DEP81=['e_prime73_field','e_prime73_relations','e_prime73_artin',
       'e_prime73_candidates','e_prime73_export']
OWN=['e_ramified_class_action','e_ramified_capitulation_export']

def locate(name,project):
    for p in [HERE/(name+'.gp'),HERE.parent.parent/project/'code'/(name+'.gp')]:
        if p.exists():return p
    raise FileNotFoundError(name)

def rebuild(gp):
    gp=str(Path(gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e84_exact_') as td:
        root=Path(td)
        d76=root/'research_norm_index/code';d81=root/'research_e81/code';own=root/'research_e84/code'
        for d in [d76,d81,own]:d.mkdir(parents=True)
        stages=[(locate(a,'research_e76'),d76/(b+'.gp'),
                 'e_ramified_dependency_'+a) for a,b in DEP76]
        stages +=[(locate(a,'research_e81'),d81/(a+'.gp'),
                   'e_ramified_dependency_'+a) for a in DEP81]
        stages +=[(HERE/(a+'.gp'),own/(a+'.gp'),a) for a in OWN]
        for source,target,name in stages:
            shutil.copyfile(source,target)
            r=subprocess.run([gp,'-q',str(target)],cwd=root,stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,text=True)
            (HERE/(name+'.out')).write_text(r.stdout)
            assert r.returncode==0,(name,r.returncode)
            assert '***   at top-level' not in r.stdout,r.stdout
            assert '***   user error' not in r.stdout,r.stdout
            assert 'DONE' in r.stdout or '"status":"PASS"' in r.stdout,name
        for p in own.glob('*.bin'):shutil.copyfile(p,HERE/p.name)

def records(path):
    raw=path.read_text()
    assert '***   at top-level' not in raw
    return [json.loads(s) for s in raw.splitlines() if s.startswith('{')]

def integral(M):return all(x.q==1 for x in M)
def ratmat(rows):return sp.Matrix([[sp.Rational(*x) for x in row] for row in rows])
def residue(v,ds):return tuple(int(a)%d for a,d in zip(v,ds))

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--gp');args=ap.parse_args()
    if args.gp:rebuild(args.gp)
    paths=[HERE/'e_ramified_dependency_e_prime73_export.out',
           HERE/'e_prime73_export.out',
           HERE.parent.parent/'research_e81/code/e_prime73_export.out']
    old=records(next(p for p in paths if p.exists()))
    base=next(r for r in old if r['type']=='base_field')
    art=next(r for r in old if r['type']=='artin')
    rr=records(HERE/'e_ramified_capitulation_export.out')
    assert len(rr)==14 and rr[-1]['status']=='PASS'
    rec={r['type']:r for r in rr if r['type'] not in ['literal_class_image','genus_action']}
    ac=rec['automorphisms']
    assert ac['h_class']==[[1,2],[0,1]] and ac['g_class']==[[1,1],[0,1]]
    assert ac['h_prime73_class']==[1,1] and ac['g_prime73_class']==[0,1]
    assert ac['h_prime_permutation']==[2,3,1,5,6,4]
    assert ac['g_prime_permutation']==[3,1,2,4,5,6]

    # Literal arithmetic in the certified base integral basis.
    x=sp.symbols('x')
    P=sp.Poly(sum(int(c)*x**i for i,c in enumerate(base['polynomial'])),x,domain=sp.QQ)
    def poly(v):
        return sp.Poly(sum(sp.Rational(*q)*x**i for i,q in enumerate(v)),x,domain=sp.QQ)
    basis=[poly(v) for v in base['basis']]
    Z=sp.Matrix(18,18,lambda i,j:basis[j].nth(i));Zi=Z.inv()
    def mul(a,b):return (a*b).rem(P)
    def pw(a,n):
        z=sp.Poly(1,x,domain=sp.QQ)
        while n:
            if n&1:z=mul(z,a)
            a=mul(a,a);n//=2
        return z
    def ev(p,a):
        z=sp.Poly(0,x,domain=sp.QQ)
        for c in p.all_coeffs():z=mul(z,a)+sp.Poly(c,x,domain=sp.QQ)
        return z
    def principal_matrix(v):
        f=poly(v);cols=[]
        for z in basis:
            r=mul(f,z);cols.append(Zi*sp.Matrix([r.nth(i) for i in range(18)]))
        return sp.Matrix.hstack(*cols)
    xi=poly(ac['xi']);beta=poly(ac['beta1']);zeta=pw(xi,3);a=mul(beta,pw(xi,8))
    one=sp.Poly(1,x,domain=sp.QQ);zero=sp.Poly(0,x,domain=sp.QQ)
    assert pw(xi,9)==one and pw(beta,3)==17*zeta and a-xi==sp.Poly(x,x,domain=sp.QQ)
    hf=poly(ac['h_base']);gf=poly(ac['g_base'])
    assert hf==mul(pw(zeta,2),a)-mul(zeta,xi)
    assert gf==mul(zeta,a)-xi
    field_checks=0
    for aut in [hf,gf]:
        assert ev(P,aut)==zero
        assert ev(ev(aut,aut),aut)==sp.Poly(x,x,domain=sp.QQ)
        field_checks+=2
    assert ev(xi,hf)==mul(zeta,xi) and ev(beta,hf)==beta
    assert ev(xi,gf)==xi and ev(beta,gf)==mul(zeta,beta)
    field_checks+=4
    literal=0
    for r in rr:
        if r['type']!='literal_class_image':continue
        I=ratmat(r['image_ideal']);R=ratmat(r['reference_ideal'])
        A=principal_matrix(r['principal_generator'])
        T=I.inv()*A*R
        assert integral(T) and abs(T.det())==1
        J=sp.Matrix(base['prime73'] if r['input']==3 else ac['class_generator_ideals'][r['input']-1])
        image_cols=[]
        for j in range(18):
            v=J[:,j];p=sum((v[i]*basis[i] for i in range(18)),zero)
            q=ev(p,hf if r['automorphism']=='h' else gf)
            image_cols.append(Zi*sp.Matrix([q.nth(i) for i in range(18)]))
        C=sp.Matrix.hstack(*image_cols);S=I.inv()*C
        assert integral(S) and abs(S.det())==1
        literal+=1
    assert literal==6

    # The two actual ray automorphisms preserve the precise genus kernel.
    C=sp.Matrix(art['s_map']);ds=art['cyclic'];D=sp.diag(*ds)
    ramified_orders=[lcm(*(d//gcd(d,int(a)) for d,a in zip(ds,C[:,j]))) for j in range(6)]
    assert ramified_orders==[3,3,3,3,3,3]
    genus_checks=0
    for r in rr:
        if r['type']!='genus_action':continue
        A,H,R,U,Ui,G=[sp.Matrix(r[k]) for k in
                     ['ray_action','relation_lattice','relation_action',
                      'smith_left','smith_left_inverse','genus_action']]
        assert A*H==H*R and integral(R)
        assert U*Ui==Ui*U==sp.eye(16) and U*A*Ui==G
        assert integral(D.inv()*(G**3-sp.eye(16)))
        perm=ac[r['automorphism']+'_prime_permutation']
        for j in range(6):
            assert residue(G*C[:,j]-C[:,perm[j]-1],ds)==(0,)*16
            genus_checks+=1
    # The only 3-power-order automorphism of a group of order three is 1.
    assert [u for u in [1,2] if pow(u,9,3)==1]==[1]
    assert [u for u in [1,2] if pow(u,3,3)==1]==[1]
    g=sp.Matrix(ac['g_class']);p=sp.Matrix([2,1])
    assert residue((g-sp.eye(2))*p,[3,3])==(1,0)
    assert residue(sp.Matrix(art['target'])+C[:,4]-C[:,3],ds)==(0,)*16

    r=rec['new_s_relations'];M=sp.Matrix(r['generators'])
    sm=rec['smith'];H,L,R,Li,Ri=[sp.Matrix(sm[k]) for k in
          ['hnf','left','right','left_inverse','right_inverse']]
    dd=sm['diagonal'];delta=sp.Matrix(r['delta'])
    assert H==hermite_normal_form(M) and H.det()==81
    assert L*H*R==sp.diag(*dd)
    assert L*Li==Li*L==R*Ri==Ri*R==sp.eye(6)
    assert dd==[3,3,3,3,1,1]
    assert integral(D.inv()*C*M)
    image=hermite_normal_form(D.row_join(C))
    assert D.det()/image.det()==27
    assert not integral(H.inv()*delta) and integral(H.inv()*(3*delta))
    assert residue(C*delta,ds)==(0,)*16
    kernel_checks=0;formal_classes=set();formal_kernel=set()
    for v in product(range(3),repeat=6):
        vv=sp.Matrix(v);q=residue(L*vv,dd);formal_classes.add(q)
        if residue(C*vv,ds)==(0,)*16:
            formal_kernel.add(q)
            assert any(integral(H.inv()*(vv-t*delta)) for t in range(3))
        kernel_checks+=1
    assert len(formal_classes)==81 and len(formal_kernel)==3
    counts=Counter()
    origin=sp.Matrix([0,0,0,-1,1,0]);qsum=sp.Matrix([1,1,1,0,0,0])
    e1=sp.eye(6)[:,0];e2=sp.eye(6)[:,1]
    for aa,b,c in product([-1,0,1],repeat=3):
        tt=(b+2*c)%3
        if tt==2:tt=-1
        m=(b+2*c-tt)//3
        v=sp.Matrix([3*aa+2*b+2*c,b,c,-1,1,0])
        assert v-origin-tt*delta==c*qsum+3*(aa+b+c-m)*e1+3*(m-c)*e2
        assert integral(H.inv()*(v-origin-tt*delta))
        counts[tt]+=1
    assert dict(counts)=={-1:9,0:9,1:9}
    principal_counts=set()
    for w,d in product(range(3),repeat=2):
        principal_counts.add(sum(9 for t in range(3) if (w+t*d)%3==0))
    assert principal_counts=={0,9,27}

    fixed=rec['fixed_field'];norm=rec['norm_target']
    assert fixed['discriminant']==-3**45*17**16
    assert fixed['upper_discriminant']==fixed['discriminant']**3
    assert fixed['relative_discriminant_norm']==1
    assert norm=={'type':'norm_target','c1_valuations':[1,1,1,0,0,0],
        'absolute_norm':27,'c1_cubic_residue_equals_zeta':[1,1,1],
        'corrected_cubic_residue_equals_one':[1,1,1]}
    summary={'statement':'E.84','status':'PASS','structured_records':len(rr),
      'literal_base_class_images':literal,'exact_base_field_substitution_checks':field_checks,
      'actual_upper_prime_permutations':2,'genus_artin_equivariance_checks':genus_checks,
      'full_smith_inverse_certificates':1,'formal_s_divisor_checks':kernel_checks,
      'formal_s_divisor_quotient':[3,3,3,3],'formal_genus_kernel_order':3,
      'ordinary_capitulation_kernel_generator':[1,0],'ordinary_capitulation_kernel_order':3,
      'ordinary_transfer_image_generator':'extended prime73','ordinary_transfer_image_order':3,
      'ramified_prime_class_orders':ramified_orders,
      'q1_q2_q3_principal':True,'q3_original_level2_order':3,
      'q3_original_level2_capitulates_in_B2':True,
      'candidate_comparison_identities':27,'reduced_candidate_multiplicities':dict(sorted(counts.items())),
      'remaining_candidate_values':'w+t*delta, t=-1,0,1',
      'possible_principal_counts':[0,9,27],
      's_capitulation':'three explicit remaining ideal classes; not evaluated',
      'corrected_xi_c1_s_unit_norm':'ordinary-unit norm coset remains unevaluated',
      'universal_h':'unevaluated'}
    (HERE/'e_ramified_capitulation.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
