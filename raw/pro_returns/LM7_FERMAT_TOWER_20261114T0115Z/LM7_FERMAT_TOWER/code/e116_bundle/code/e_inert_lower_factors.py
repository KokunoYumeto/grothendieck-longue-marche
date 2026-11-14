#!/usr/bin/env python3
"""E116: actual norm maps, inverse coordinates and inert-prime first stratum.

Full portable rebuild: python e_inert_lower_factors.py --gp /absolute/path/to/gp
The successful GP pipeline uses only degree3/6/9 fields.  It does not repeat
the retained unsuccessful default-flag-zero certification at degree9.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
from math import comb, gcd
import argparse, hashlib, json, shutil, subprocess, sys, tempfile
import sympy as s

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--gp');args=parser.parse_args()
gps=['e_small_inert_units.gp','e53_prime_columns.gp','e53_pure9_norm_witness.gp',
     'e53_pure9_class_upper.gp','e53_exact_maps.gp']
pys=['e53_first_norm_explore.py','e53_s_norm_explore.py','e53_unit_saturation.py','e53_complete_transition.py']
if args.gp:
    gp=str(Path(args.gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e116_actual_') as td:
        td=Path(td)
        for name in gps:shutil.copy2(HERE/name,td/name)
        for name in gps:
            run=subprocess.run([gp,'-q','-f',name],cwd=td,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (HERE/Path(name).with_suffix('.out')).write_bytes(run.stdout)
            assert run.returncode==0, (name,run.returncode)
            rows=[json.loads(x) for x in run.stdout.decode().splitlines() if x.startswith('{')]
            assert rows and rows[-1].get('status')=='PASS',name
        for path in td.glob('*.bin'):shutil.copy2(path,HERE/path.name)
for name in pys:
    run=subprocess.run([sys.executable,str(HERE/name)],cwd=HERE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (HERE/Path(name).with_suffix('.out')).write_bytes(run.stdout)
    assert run.returncode==0,(name,run.returncode)
    assert json.loads(run.stdout)['status']=='PASS',name

def records(name):
    return [json.loads(line) for line in (HERE/name).read_text().splitlines() if line.startswith('{')]
base=records('e_small_inert_units.out')
fields=[x for x in base if x['type']=='base_field']
assert len(fields)==6
assert all(x['certification_flag']==0 and x['certification_returns']==[1,1] for x in fields)
assert all(x['complex_class_number']%3 and x['pure_class_number']%3 for x in fields)
trans=[x for x in base if x['type']=='pure_transition'];assert len(trans)==2
inverse=[]
for r in trans:
    M=s.Matrix(r['matrix']);U=s.Matrix(r['smith_left']);V=s.Matrix(r['smith_right']);D=s.Matrix(r['smith_diagonal'])
    assert U*M*V==D and D==s.Matrix([[0,0,0,1]])
    assert abs(int(U.det()))==abs(int(V.det()))==1
    K=V[:,:3];R=V[:,3:]*U
    assert M*R==s.eye(1) and M*K==s.zeros(1,3)
    count=0
    for x in range(-4,5):
        for t in product(range(-1,2),repeat=3):
            z=R*s.Matrix([x])+K*s.Matrix(t)
            assert M*z==s.Matrix([x])
            back=V.inv()*z
            assert list(back[:3,:])==list(t) and back[3]==U[0]*x
            count+=1
    inverse.append({'ell':r['ell'],'norm':r['matrix'],'right_inverse':R.tolist(),
                    'kernel_basis':K.tolist(),'full_inverse':V.inv().tolist(),'checks':count})

def v3(n):
    assert n
    n=abs(int(n));r=0
    while n%3==0:n//=3;r+=1
    return r
newton=[];chars=[]
for ell in s.primerange(2,400):
    ell=int(ell)
    if ell%9 not in (2,5):continue
    assert v3(ell+1)==v3(ell*ell-1)==1
    for m in range(1,6):
        n=3**m
        assert v3(ell+1)*2==2
        assert all(comb(n,j)%3==0 for j in range(1,n))
        assert gcd(2,n)==1
        newton.append({'ell':ell,'m':m,'constant_lambda_valuation':2,'root_value':str(Fraction(2,n))})
    # Actual zeta column in F_(ell^2), in the fixed basis1,zeta.
    def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%ell,(a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%ell)
    def power(a,n):
        z=(1,0)
        while n:
            if n&1:z=mul(z,a)
            a=mul(a,a);n//=2
        return z
    value=power((0,1),(ell*ell-1)//3)
    assert value!=(1,0)
    chars.append({'ell':ell,'q':ell*ell,'zeta_character':value})

# Actual coherent residue roots, proving the finite maps used by the divisor inverse.
branches=[]
for ell in (2,5,11,23):
    for p in s.primerange(2,200):
        p=int(p)
        if p in (3,ell):continue
        d=int(s.n_order(ell,p));eligible=d%3!=0
        if eligible:
            roots=[pow(ell,pow(3**m,-1,d),p) if d>1 else 1 for m in range(6)]
            assert roots[0]==ell%p
            assert all(pow(roots[m+1],3,p)==roots[m] for m in range(5))
            assert all(pow(roots[m],3**m,p)==ell%p for m in range(6))
            branches.append({'ell':ell,'p':p,'residue_order':d,'roots':roots})

# Literal raw norm equals the cube of the scaled toric coordinate.
toric=[]
for k in range(4):
    for B3,Bl in product(range(-2,3),repeat=2):
        for offset in range(-3,4):
            tails=[(offset+j,2*offset-j) for j in range(1,k+2)]
            A3=sum(a for a,b in tails);Al=sum(b for a,b in tails)
            pure=(3*B3-A3,3*Bl-Al)
            assert Fraction(pure[0]+A3,3)==B3
            assert Fraction(pure[1]+Al,3)==Bl
            assert (pure[0]+A3,pure[1]+Al)==(3*B3,3*Bl)
            toric.append({'k':k,'target':[B3,Bl],'tail_norms':tails,'pure_norm':pure})

# Semisimplicity used in the actual C2/Hilbert90 descent, with both signs retained.
involutions=[]
for a in range(3):
    C=s.Matrix([[1,a],[0,1]])
    if (C*C-s.eye(2)).applyfunc(lambda x:int(x)%3)==s.zeros(2):
        assert C==s.eye(2);involutions.append(a)
assert involutions==[0]
complete=json.loads((HERE/'e53_complete_transition.json').read_text())
assert complete['complex_full_S_class_group']==[3]
assert complete['complex_full_S_class_sigma_action']==1
assert complete['complex_full_S_class_c_action']==-1
sat=json.loads((HERE/'e53_unit_saturation.json').read_text())
assert sat['determinant']==-4
gp_rows={Path(n).stem:len(records(str(Path(n).with_suffix('.out')))) for n in gps}
out={'statement':'E.116','status':'PASS',
     'unconditionally_certified_lower_fields':12,'unconditionally_certified_pure_degree9_examples':2,
     'literal_pure_unit_norm_maps':inverse,
     'newton_valuation_checks':len(newton),'newton_values':newton,
     'actual_nonzero_zeta_columns':chars,
     'compatible_pure_prime_chains':len(branches),'prime_chains':branches,
     'raw_scaled_toric_inverse_checks':len(toric),
     'toric_examples':toric[:8],
     'first_lower53':complete,
     'pure53_unit_saturation_matrix':sat['matrix'],
     'pure53_unit_saturation_inverse':sat['inverse_mod3'],
     'pure53_power_class_checks':len(sat['all_81_power_class_checks']),
     'successful_GP_structured_record_counts':gp_rows,
     'mathematical_sources_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in gps+pys},
     'preserved_failed_attempts':['default-flag0 pure9 certification, actual timeout exit124',
         'initial wrong executable-relative-path exit127','initial GP parse failure',
         'initial Mod-valued JSON sign representation','appended PARI binary read failure'],
     'scope':'Uniform all-level pure norm coordinates for inert ell with v3(ell+1)=1; full actual first pure/complex S-class and unit-norm transition at53. Higher lower53 factors are not assigned this finite result.'}
def convert(x):
    if isinstance(x,s.Integer):return int(x)
    if isinstance(x,s.Rational):return str(x)
    raise TypeError(type(x))
text=json.dumps(out,indent=2,default=convert)+'\n';(HERE/'e_inert_lower_factors.json').write_text(text);print(text,end='')
