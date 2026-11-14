#!/usr/bin/env python3
"""E114 universal group-ring inverse and literal inert-prime comparisons.

The GP stage only reads the retained, certified E111 degree-six object.
It starts no BNF calculation. Optional full replay uses --gp /path/to/gp.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import argparse,hashlib,json,random,shutil,subprocess,tempfile,warnings
import sympy as s
from sympy.utilities.exceptions import SymPyDeprecationWarning

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
parser=argparse.ArgumentParser();parser.add_argument('--gp');args=parser.parse_args()
if args.gp:
    gp=str(Path(args.gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e114_orbit_') as td:
        td=Path(td);(td/'code').mkdir();(td/'inputs').mkdir()
        shutil.copy2(HERE/'e_inert_tail_orbit.gp',td/'code/orbit.gp')
        shutil.copy2(ROOT/'inputs/e114_cyclo9_base.bin',td/'inputs/e114_cyclo9_base.bin')
        run=subprocess.run([gp,'-q','-f','orbit.gp'],cwd=td/'code',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (HERE/'e_inert_tail_orbit.out').write_bytes(run.stdout)
        if run.returncode:raise RuntimeError('actual GP exit '+str(run.returncode))
        assert b'"status":"PASS"' in run.stdout
        shutil.copy2(td/'code/e_inert_tail_orbit.bin',HERE/'e_inert_tail_orbit.bin')
gp_records=[json.loads(line) for line in (HERE/'e_inert_tail_orbit.out').read_text().splitlines() if line.startswith('{')]
assert gp_records[-1]=={'type':'completion','status':'PASS'}
orbits=[r for r in gp_records if r['type']=='orbit']
assert len(orbits)==3
coordinates=next(r['rows'] for r in gp_records if r['type']=='matrix')
assert coordinates==[[0,6,0],[0,0,0],[0,0,0],[0,0,0],[1,0,0],[0,0,1],[0,1,0]]
X=s.symbols('X');phi=X**6+X**3+1
pi=2+X+X**2+X**3+2*X**4
U=[X,1+X,1+X**2,1-X,pi,2+X+X**3-X**4+X**5,-1+X+X**2+X**3-X**4]
for rec in orbits:
    g=rec['g'];actual=s.rem(pi.subs(X,X**(4**g)),phi,X)
    frozen=sum(s.Rational(a)*X**i for i,a in enumerate(rec['polynomial_coefficients']))
    assert actual==frozen
    expr=s.Poly(rec['sign'],X)
    for u,e in zip(U,rec['S_unit_coordinates']):
        assert e>=0
        expr=s.rem(expr*s.Poly(u,X)**e,s.Poly(phi,X))
    assert s.rem(expr.as_expr()-actual,phi,X)==0

def cyclic_mul(a,b):
    t=len(a);out=[0]*t
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[(i+j)%t]=(out[(i+j)%t]+x*y)%3
    return out
def cyclic_inverse(a,c):
    t=len(a);one=[1]+[0]*(t-1);q=[-pow(c,-1,3)*x%3 for x in a]
    term=one[:];ans=[0]*t
    for _ in range(t):
        ans=[(x+pow(c,-1,3)*y)%3 for x,y in zip(ans,term)]
        term=cyclic_mul(term,q)
    assert term==[0]*t
    f=a[:];f[0]=(f[0]+c)%3
    assert cyclic_mul(f,ans)==one
    assert cyclic_mul(ans,f)==one
    return ans

ring_digest=hashlib.sha256();ring_counts={};large_cases=[]
for t in (1,3,9):
    count=0
    for aa in product(range(3),repeat=t-1):
        a=list(aa)+[-sum(aa)%3]
        for c in (1,2):
            inv=cyclic_inverse(a,c)
            ring_digest.update(json.dumps([t,c,a,inv],separators=(',',':')).encode()+b'\n')
            count+=1
    ring_counts[str(t)]=count
rng=random.Random(176114)
for t,count in ((27,50),(81,20)):
    for _ in range(count):
        a=[rng.randrange(3) for _ in range(t-1)];a.append(-sum(a)%3)
        for c in (1,2):
            inv=cyclic_inverse(a,c)
            large_cases.append({'t':t,'c':c,'augmentation_zero_a':a,'inverse':inv})

# Literal F_289 and its cubic unramified extension, retaining the chosen roots.
def badd(a,b):return ((a[0]+b[0])%17,(a[1]+b[1])%17)
def bmul(a,b):return ((a[0]*b[0]-a[1]*b[1])%17,(a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%17)
def bpow(x,n):
    a=(1,0)
    while n:
        if n&1:a=bmul(a,x)
        x=bmul(x,x);n//=2
    return a
def ring17mul(a,b,M):return ((a[0]*b[0]-a[1]*b[1])%M,(a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%M)
def ring17pow(x,n,M):
    a=(1,0)
    while n:
        if n&1:a=ring17mul(a,x,M)
        x=ring17mul(x,x,M);n//=2
    return a
def evaluate(coeff,xi,M):
    z=(0,0)
    for a in reversed(coeff):
        a=Fraction(a);z=ring17mul(z,xi,M)
        z=((z[0]+a.numerator*pow(a.denominator,-1,M))%M,z[1])
    return z

zeta=(0,1)
roots_mod289=[(94,113),(19,195),(176,270)] # actual orbit prime order T1,T3,T2
assert all(ring17pow(x,3,289)==zeta for x in roots_mod289)
local=[]
for xi in roots_mod289:
    row=[]
    for rec in orbits:
        v=evaluate(rec['polynomial_coefficients'],xi,289)
        val=int(v[0]%17==v[1]%17==0)
        residue=tuple((a//17 if val else a)%17 for a in v)
        assert residue!=(0,0)
        row.append({'valuation':val,'unit_residue':residue})
    local.append(row)
assert [[d['valuation'] for d in row] for row in local]==[[1,0,0],[0,1,0],[0,0,1]]

def base_char(radell,radxi,r):
    out=[];mod=3**r
    for xi,row in zip(roots_mod289,local):
        xi=tuple(a%17 for a in xi);root=bpow(xi,3**(2-r));line=[]
        for u in row:
            a=bmul(bpow(xi,radxi*u['valuation']),bpow(bpow(u['unit_residue'],287),radell))
            val=bpow(a,288//mod)
            ex=[e for e in range(mod) if bpow(root,e)==val]
            assert len(ex)==1;line.append(ex[0])
        out.append(line)
    return out

def extension_ops(xi):
    zero=((0,0),(0,0),(0,0));one=((1,0),(0,0),(0,0))
    def mul(a,b):
        out=[(0,0)]*5
        for i in range(3):
            for j in range(3):out[i+j]=badd(out[i+j],bmul(a[i],b[j]))
        for i in (4,3):out[i-3]=badd(out[i-3],bmul(out[i],xi))
        return tuple(out[:3])
    def power(a,n):
        out=one
        while n:
            if n&1:out=mul(out,a)
            a=mul(a,a);n//=2
        return out
    return one,mul,power

def next_char(r):
    mod=3**r;out=[]
    for xi,row in zip(roots_mod289,local):
        xi=tuple(c%17 for c in xi);one,mul,power=extension_ops(xi)
        w=((0,0),(1,0),(0,0));q=17**6
        assert power(w,3)==(xi,(0,0),(0,0))
        assert power(w,27)==one and power(w,9)!=one
        assert power(w,(q-1)//288)==(xi,(0,0),(0,0))
        root=power(w,3**(3-r));line=[]
        for u in row:
            val=mul(power(w,u['valuation']),(bpow(u['unit_residue'],287),(0,0),(0,0)))
            val=power(val,(q-1)//mod)
            ex=[e for e in range(mod) if power(root,e)==val]
            assert len(ex)==1;line.append(ex[0])
        out.append(line)
    return out

chars=[];character_inverse_count=0
for j in (2,3):
    for r in range(1,j+1):
        mod=3**r;C=s.Matrix(base_char(1,1,r) if j==2 else next_char(r))
        inv=(pow(int(C.det()),-1,mod)*C.adjugate()).applyfunc(lambda x:int(x)%mod)
        assert (C*inv).applyfunc(lambda x:int(x)%mod)==s.eye(3)
        assert (inv*C).applyfunc(lambda x:int(x)%mod)==s.eye(3)
        if j==3 and r<=2:
            expected=3*s.Matrix(base_char(1,0,r))+s.Matrix(base_char(0,1,r))
            assert (C-expected).applyfunc(lambda x:int(x)%mod)==s.zeros(3)
        if r==1:
            expected=s.Matrix([[1,2,2],[2,1,2],[2,2,1]]) if j==2 else 2*s.eye(3)
            assert C==expected
        Cm=[[int(x) for x in row] for row in C.tolist()]
        Im=[[int(x) for x in row] for row in inv.tolist()]
        for h in product(range(mod),repeat=3):
            coeff=[sum(Im[i][a]*h[a] for a in range(3))%mod for i in range(3)]
            back=[sum(Cm[i][a]*coeff[a] for a in range(3))%mod for i in range(3)]
            assert back==list(h)
            assert (-sum(back)+sum(h))%mod==0
            character_inverse_count+=1
        chars.append({'j':j,'r':r,'modulus':mod,'tame_character_matrix':Cm,
                      'inverse':Im,'determinant':int(C.det()),
                      'norm_quotient_order':mod**3})

prime_examples=[]
def cheb(n,t,p):
    a,b=2,t%p
    if n==0:return a
    for _ in range(1,n):a,b=b,(t*b-a)%p
    return b
for ell in (2,5,17,71,53,107,647):
    assert s.isprime(ell) and ell%3==2
    ss=0;q=ell+1
    while q%3==0:ss+=1;q//=3
    t=3**(ss-1);F=s.Poly(s.cyclotomic_poly(3**ss,X),X,modulus=ell)
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore',message='(?s).*Ordered comparisons with modular integers.*',category=SymPyDeprecationWarning)
        coeff,factors=s.factor_list(F)
    assert int(coeff)%ell==1 and len(factors)==t
    ff=[];traces=[]
    for f,e in factors:
        assert e==1 and f.degree()==2
        cc=[int(a)%ell for a in f.all_coeffs()]
        assert cc[0]==cc[2]==1
        ff.append(cc);traces.append(-cc[1]%ell)
    inv4=pow(4,-1,3**ss)
    orbit=[min(traces)]
    for _ in range(t-1):orbit.append(cheb(inv4,orbit[-1],ell))
    assert len(set(orbit))==t and set(orbit)==set(traces)
    assert cheb(inv4,orbit[-1],ell)==orbit[0]
    c=((ell*ell-1)//(3**ss))%3;assert c in (1,2)
    prime_examples.append({'ell':ell,'s':ss,'t':t,'primitive_diagonal_character':c,
                           'actual_quadratic_factors':ff,'actual_sigma_prime_trace_orbit':orbit})

local_counts=0;cube_checks=0;ramification=[]
for ell in s.primerange(2,3000):
    ell=int(ell)
    if ell%3!=2:continue
    ss=0;a=ell+1
    while a%3==0:ss+=1;a//=3
    t=3**(ss-1);c=((ell*ell-1)//3**ss)%3
    for j in range(ss,ss+4):
        f=2*3**(j-ss)
        residue=(pow(ell,f,3**(j+1))-1)%(3**(j+1))
        assert residue//(3**j)%3==c
        assert (2*3**(j-1))//f==t
        assert int(s.n_order(ell,3**j))==f
        ramification.append({'ell':ell,'s':ss,'j':j,'number_ell_primes':t,
                              'ell_residue_degree':f,'four_or_more_place_Herbrand_exponent':t})
        local_counts+=1
    if ss>=2:
        root=-1+3*(((ell+1)//9)%3)
        assert (root**3-ell)%27==0
        for n in range(3,9):
            step=((ell-root**3)//(3**n)*pow(root*root,-1,3))%3
            root+=step*3**(n-1)
            assert (root**3-ell)%(3**(n+1))==0
            cube_checks+=1

# Actual rational prime chains in the Chebotarev strata used in the proof.
surviving_prime_chains=[];prime_chain_steps=0
for rec in prime_examples:
    ell,ss=rec['ell'],rec['s']
    for j in range(ss,ss+3):
        found=0
        for a in range(4,6000,6):
            p=a*3**j+1
            if p==ell or not s.isprime(p):continue
            if pow(ell,(p-1)//3,p)==1:continue
            assert a%3==1 and p%(3**(j+1))==1+3**j
            part=pow(ell,a*pow(a,-1,3**j),p)
            xi=pow(part,-1,p)
            assert pow(xi,3**j,p)==1 and pow(xi,3**(j-1),p)!=1
            beta0=ell*xi%p
            assert pow(beta0,a,p)==1
            roots=[pow(beta0,pow(3**m,-1,a),p) for m in range(5)]
            assert roots[0]==beta0
            for m in range(1,5):
                assert pow(roots[m],3,p)==roots[m-1]
                assert pow(roots[m],3**m,p)==ell*xi%p
                prime_chain_steps+=1
            surviving_prime_chains.append({'ell':ell,'j':j,'p':int(p),'xi_j_residue':xi,
                'literal_beta_0_through_4_residues':roots,'prime_to_three_order_bound':a})
            found+=1
            if found==3:break
        assert found==3

out={'statement':'E.114','status':'PASS','actual_orbit_GP_records':gp_records,
 'literal_Galois_orbit_comparison':coordinates,'prime_ideal_order':['T1','T3','T2'],
 'all_small_augmentation_ideal_cases':ring_counts,
 'all_small_inverse_data_SHA256':ring_digest.hexdigest(),
 'larger_exact_inverse_cases':large_cases,'actual_local_unit_residues':local,
 'actual_cubic_and_higher_character_matrices':chars,
 'all_actual_character_inverse_checks':character_inverse_count,
 'actual_cyclotomic_prime_factorizations':prime_examples,
 'actual_cyclotomic_ramification_tests':local_counts,
 'literal_Q3_cube_Hensel_checks':cube_checks,
 'actual_surviving_prime_chains':surviving_prime_chains,
 'actual_surviving_prime_transition_checks':prime_chain_steps,
 'ramification_table':ramification,
 'scope':'The universal S-class and norm result is proved with exact class/unit maps. This certificate verifies the universal ring inverse, actual ell17 character and norm comparisons, and actual finite cyclotomic prime data; it starts no upper BNF and does not infer the untreated lower factors.',
 'inputs':{'e114_cyclo9_base.bin':hashlib.sha256((ROOT/'inputs/e114_cyclo9_base.bin').read_bytes()).hexdigest()}}
text=json.dumps(out,indent=2)+'\n'
(HERE/'e_inert_tail.json').write_text(text)
print(text,end='')
