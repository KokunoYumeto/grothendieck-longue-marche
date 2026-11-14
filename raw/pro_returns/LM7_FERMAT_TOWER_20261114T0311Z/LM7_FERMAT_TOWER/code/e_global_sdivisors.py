#!/usr/bin/env python3
"""E.88: all-level S-principal divisors from one certified degree-six field."""
from __future__ import annotations
import argparse
from itertools import product
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent

def read(path):
    raw=path.read_text()
    assert '***   at top-level' not in raw
    assert 'syntax error' not in raw
    return [json.loads(s) for s in raw.splitlines() if s.startswith('{')]

def integral(M):return all(x.q==1 for x in M)
def ratmat(rows):return sp.Matrix([[sp.Rational(*q) for q in row] for row in rows])
def red(v,m):return tuple(int(x)%m for x in v)

def rebuild(gp):
    gp=str(Path(gp).resolve())
    lower=next(p for p in [
        HERE/'e_stable_lower_genus.gp',
        HERE.parent.parent/'research_e86/code/e_stable_lower_genus.gp'] if p.exists())
    with tempfile.TemporaryDirectory(prefix='e88_exact_') as td:
        root=Path(td);d86=root/'research_e86/code';d88=root/'research_e88/code'
        d86.mkdir(parents=True);d88.mkdir(parents=True)
        for src,dst,out in [
            (lower,d86/'e_stable_lower_genus.gp','e_global_sdivisors_lower.out'),
            (HERE/'e_global_sdivisors.gp',d88/'e_global_sdivisors.gp',
             'e_global_sdivisors_gp.out')]:
            shutil.copyfile(src,dst)
            p=subprocess.run([gp,'-q',str(dst)],cwd=root,
                stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            (HERE/out).write_text(p.stdout)
            assert p.returncode==0 and '***   at top-level' not in p.stdout
            assert 'syntax error' not in p.stdout
            assert 'DONE' in p.stdout or '"status":"PASS"' in p.stdout
            print(dst.name,'PASS',flush=True)
        shutil.copyfile(d88/'e_global_sdivisors.bin',HERE/'e_global_sdivisors.bin')

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--gp')
    args=ap.parse_args()
    if args.gp:rebuild(args.gp)
    rr=read(HERE/'e_global_sdivisors_gp.out')
    assert rr[-1]['status']=='PASS'
    pp={r['p']:r for r in rr if r['type']=='eligible_prime'}
    expected=[int(p) for p in sp.primerange(2,2001) if p not in [3,17]
              and sp.multiplicity(3,sp.n_order(17,p))==1]
    assert sorted(pp)==expected and len(pp)==79
    chain_checks=0
    S=sp.Matrix([[2,2],[0,1]])
    for p,r in pp.items():
        zz=r['zeta'];order=sp.n_order(17,p)
        assert (zz*zz+zz+1)%p==0 and zz!=1
        a=17*zz%p
        assert sp.n_order(a,p)%3
        m=(p-1)//3**int(sp.multiplicity(3,p-1))
        for d in range(1,11):
            root=pow(a,pow(3**d,-1,m),p)
            assert pow(root,3**d,p)==a and sp.n_order(root,p)%3
            if d==1:assert root==r['beta1']
            if d==2:assert root==r['beta2']
            nextroot=pow(a,pow(3**(d+1),-1,m),p)
            assert pow(nextroot,3,p)==root
            chain_checks+=1
        assert red(S*sp.Matrix(r['L1_class']),3)==tuple(r['S_class'])
        assert tuple(x%3 for x in r['L2_class'])==tuple(r['S_class'])
    assert pp[7]['S_class']==[2,1] and pp[73]['S_class']==[0,1]
    assert pp[7]['beta1']==pp[7]['beta2']==6
    assert pp[73]['beta1']==22 and pp[73]['beta2']==63
    z=next(r for r in rr if r['type']=='pivot_system')
    primes=z['prime_order'];N=len(primes)
    C,Q,Qi,H,L,R,Li,Ri=[ratmat(z[k]) if k=='basis_inverse' else sp.Matrix(z[k])
                        for k in ['class_map','basis','basis_inverse','hnf',
                                  'left','right','left_inverse','right_inverse']]
    assert primes[:2]==[7,73] and sorted(primes)==expected
    assert Q*Qi==Qi*Q==sp.eye(N) and abs(Q.det())==9
    assert H==hermite_normal_form(Q)
    assert L*H*R==sp.diag(*z['diagonal'])
    assert L*Li==Li*L==R*Ri==Ri*R==sp.eye(N)
    assert z['diagonal']==[3,3]+[1]*(N-2)
    assert integral(Qi*H) and integral(H.inv()*Q)
    assert red(C*Q,3)==(0,)*(2*N)
    for j,p in enumerate(primes):
        assert list(C[:,j])==pp[p]['S_class']
        if j>=2:
            v=sp.zeros(N,1);v[j]=1
            v[0]=pp[p]['S_class'][0]
            v[1]=-sum(pp[p]['S_class'])
            assert Q[:,j]==v
    ell=sp.Matrix([z['L2_first_coordinates']])
    phase=-ell*Q/3
    assert integral(phase) and red(phase,3)==tuple(z['phase_on_basis_mod3'])
    kernel_cases=0
    for v in product(range(3),repeat=6):
        w=sp.Matrix(list(v)+[0]*(N-6))
        assert integral(Qi*w)==(red(C*w,3)==(0,0))
        kernel_cases+=1
    inverse_cases=0
    for k in range(120):
        a=sp.Matrix([((k+3)*(j+5)**2+7*k*j)%81-40 for j in range(N)])
        t=Q*a
        assert Qi*t==a
        assert (t[0]-sum(C[0,j]*t[j] for j in range(2,N)))/3==a[0]
        assert (t[1]+sum((C[0,j]+C[1,j])*t[j] for j in range(2,N)))/3==a[1]
        inverse_cases+=1

    # Every ordinary class equation behind the phase and both directions
    # of the norm-cube condition in a complete finite power quotient.
    small=[0,1,2,3]
    cube_cases=0;accepted=0
    for v in product(range(9),repeat=4):
        cl=[sum(int(C[i,j])*v[j] for j in small)%3 for i in range(2)]
        if cl!=[0,0]:continue
        num=sum(int(ell[j])*v[j] for j in small)
        assert num%3==0
        theta=(-num//3)%3
        for b in range(3):
            actual=(b==0 and all(a%3==0 for a in v) and theta==0)
            formula=(b==0 and all(a%3==0 for a in v)
                     and sum(int(C[0,j])*(v[j]//3) for j in small)%3==0)
            assert actual==formula
            cube_cases+=1;accepted+=actual
    assert cube_cases==2187 and accepted==27

    # The one-condition locus has an exact index-three coordinate map.
    Rone=sp.eye(N);Rone[0,0]=3
    for j in range(1,N):Rone[0,j]=-(2*int(C[0,j])%3)
    assert abs(Rone.det())==3 and red(C[0,:]*Rone,3)==(0,)*N

    # Literal norm-coherent families, including signs and phase.
    Y,B,Z=sp.symbols('Y B Z')
    assert sp.resultant(Y**3-B,Y+1,Y)==B+1
    assert sp.resultant(Y**3-B,Y-1,Y)==B-1
    assert sp.resultant(Z**2+Z+1,17*Z+1,Z)==273
    assert sp.resultant(Z**2+Z+1,17*Z-1,Z)==307
    assert sp.factorint(273)=={3:1,7:1,13:1} and sp.isprime(307)
    plus=sp.zeros(N,1);plus[primes.index(7)]=plus[primes.index(13)]=1
    minus=sp.zeros(N,1);minus[primes.index(307)]=1
    assert integral(Qi*plus) and integral(Qi*minus)
    assert red(-ell*plus/3,3)==(1,) and red(-ell*minus/3,3)==(0,)
    for p in [7,13]:assert pp[p]['beta1']==pp[p]['beta2']==p-1
    assert pp[307]['beta1']==pp[307]['beta2']==1

    # Explicit finite tails illustrating the topology used in the proof:
    # bounded pivot coefficients preserve uniform 3-adic tail convergence.
    tail_checks=0
    for cutoff in range(1,10):
        tail=sp.Matrix([0,0]+[3**(j//4) for j in range(2,N)])
        kept=sp.Matrix([int(v) if int(v)%3**cutoff else 0 for v in tail])
        delta=Q*(tail-kept)
        assert red(delta,3**cutoff)==(0,)*N
        tail_checks+=1
    result={
        'statement':'E.88','status':'PASS','eligible_primes_bound':2000,
        'eligible_prime_count':len(pp),'coherent_root_chain_checks':chain_checks,
        'complete_pivot_matrix_dimension':N,'pivot_index':9,
        'full_smith_inverse_systems':1,'finite_kernel_cases':kernel_cases,
        'forward_inverse_tests':inverse_cases,
        'complete_mod9_cube_cases':cube_cases,'accepted_cube_cases':accepted,
        'one_condition_index':3,'uniform_tail_checks':tail_checks,
        'explicit_norm_families':[
            {'family':'beta_d+1','rational_norm':273,'outside_S':[7,13],'three_valuation':1},
            {'family':'beta_d-1','rational_norm':307,'outside_S':[307],'three_valuation':0}],
        'first_prime_table':[pp[p] for p in sorted(pp)[:15]],
        'remaining_arithmetic':'The eventual h and the canonical phase modulo3^h beyond its proved modulo3 evaluation remain actual finite arithmetic data. The entire outside-S coherent-lift criterion is the two displayed L1 class congruences.',
    }
    (HERE/'e_global_sdivisors.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
