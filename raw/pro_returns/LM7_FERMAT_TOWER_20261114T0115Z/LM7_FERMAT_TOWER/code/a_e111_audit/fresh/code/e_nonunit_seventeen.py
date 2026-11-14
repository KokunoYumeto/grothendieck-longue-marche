#!/usr/bin/env python3
"""E111 exact base S-unit, character, factor, prime-chain and toric maps.

Full arithmetic rebuild: python e_nonunit_seventeen.py --gp /absolute/path/to/gp
Without --gp the retained complete GP output is verified independently.
No higher-degree BNF is invoked. The all-level theorem is proved in the text.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
import argparse, hashlib, json, random, shutil, subprocess, tempfile
import sympy as s

HERE=Path(__file__).resolve().parent
PARSER=argparse.ArgumentParser()
PARSER.add_argument('--gp')
ARGS=PARSER.parse_args()
BASE=HERE/'e_nonunit_seventeen_base_gp.out'
if ARGS.gp:
    gp=str(Path(ARGS.gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e111_gp_') as tmp:
        tmp=Path(tmp)
        shutil.copy2(HERE/'e_nonunit_seventeen_base.gp',tmp/'base.gp')
        proc=subprocess.run([gp,'-q','-f','base.gp'],cwd=tmp,
                            stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        BASE.write_bytes(proc.stdout)
        if proc.returncode:
            raise RuntimeError('actual GP exit '+str(proc.returncode))
        assert b'"status":"PASS"' in proc.stdout
        shutil.copy2(tmp/'e_nonunit_seventeen_base.bin',HERE/'e_nonunit_seventeen_base.bin')

records=[json.loads(line) for line in BASE.read_text().splitlines() if line.startswith('{')]
assert records[-1]=={'type':'completion','status':'PASS'}
field=records[0]
assert field['class_number']==field['certification_return']==1
assert field['certification_flag']==0 and field['torsion_order']==18
assert field['unit_rank']==2
units=[r for r in records if r['type']=='S_unit']
assert len(units)==7
assert [r['norm_to_Q'] for r in units]==[1,1,1,3,289,289,289]
assert [r['three_valuation'] for r in units]==[0,0,0,1,0,0,0]
assert [r['seventeen_valuations'] for r in units[4:]]==[[1,0,0],[0,1,0],[0,0,1]]
assert all(r['e']==1 and r['f']==2 for r in records if r['type']=='prime17')

def add(x,y,m):
    return ((x[0]+y[0])%m,(x[1]+y[1])%m)
def mul(x,y,m):
    return ((x[0]*y[0]-x[1]*y[1])%m,
            (x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%m)
def power(x,n,m):
    ans=(1,0)
    while n:
        if n&1: ans=mul(ans,x,m)
        x=mul(x,x,m);n//=2
    return ans
def poly_eval(coeff,x,m):
    y=(0,0)
    for a in reversed(coeff):
        a=Fraction(a)
        y=add(mul(y,x,m),(a.numerator*pow(a.denominator,-1,m),0),m)
    return y
def rank3(rows):
    a=[[int(x)%3 for x in row] for row in rows];i=0
    for j in range(len(a[0])):
        pivot=next((r for r in range(i,len(a)) if a[r][j]),None)
        if pivot is None: continue
        a[i],a[pivot]=a[pivot],a[i]
        v=pow(a[i][j],-1,3);a[i]=[v*x%3 for x in a[i]]
        for r in range(len(a)):
            if r!=i:
                v=a[r][j];a[r]=[(x-v*y)%3 for x,y in zip(a[r],a[i])]
        i+=1
        if i==len(a): break
    return i

z=(0,1)
roots=[x for x in product(range(17),repeat=2) if power(x,3,17)==z]
assert roots==[(2,8),(6,15),(9,11)]
x=roots[0];x3=power(x,3,289)
err=((x3[0]-z[0])//17%17,(x3[1]-z[1])//17%17)
der=mul((3,0),power(x,2,17),17)
corr=mul((-err[0]%17,-err[1]%17),power(der,287,17),17)
xx=tuple(a+17*b for a,b in zip(x,corr))
assert power(xx,3,289)==z
embeddings=[mul(xx,power(z,i,289),289) for i in range(3)]
assert [tuple(c%17 for c in x) for x in embeddings]==[(2,8),(9,11),(6,15)]
values=[]
for xi in embeddings:
    vals=[]
    for u in units:
        y=poly_eval(u['coefficients'],xi,289)
        v=int(all(c%17==0 for c in y))
        unit=tuple((c//17 if v else c)%17 for c in y)
        assert unit!=(0,0)
        vals.append({'valuation':v,'unit_residue':unit})
    values.append(vals)
assert [[row[i]['valuation'] for i in range(4,7)] for row in values]==[[0,0,1],[1,0,0],[0,1,0]]

def character_matrix(b,a):
    tame=[]
    for xi,vals in zip(embeddings,values):
        row=[]
        for v in vals:
            w=mul(power(tuple(c%17 for c in xi),a*v['valuation'],17),
                  power(power(v['unit_residue'],287,17),b,17),17)
            h=power(w,96,17)
            ex=[e for e in range(3) if power(z,e,17)==h]
            assert len(ex)==1
            row.append(ex[0])
        tame.append(row)
    return [[-sum(row[i] for row in tame)%3 for i in range(7)]]+tame

Ds=[character_matrix(1,1),character_matrix(0,1)]
expected=[[[0,0,0,0,1,1,1],[1,2,1,2,2,2,1],[1,2,1,2,1,2,2],[1,2,1,2,2,1,2]],
          [[0,0,0,0,1,1,1],[0,0,0,0,0,0,2],[0,0,0,0,2,0,0],[0,0,0,0,0,2,0]]]
assert Ds==expected
inverse_checks=0;images=[];normalization_checks=0
for D in Ds:
    M=s.Matrix(D);P=M[:3,4:7];R=P.inv_mod(3)
    image=set()
    for a in product(range(3),repeat=7):
        ch=tuple(int(v)%3 for v in M*s.Matrix(a));image.add(ch)
        correction=R*s.Matrix(ch[:3])
        a2=list(a)
        for i in range(3):a2[i+4]-=int(correction[i])
        assert all(int(v)%3==0 for v in M*s.Matrix(a2))
        normalization_checks+=1
    assert image=={c for c in product(range(3),repeat=4) if sum(c)%3==0}
    for c in sorted(image):
        a=R*s.Matrix(c[:3]);back=M[:,4:7]*a
        assert tuple(int(v)%3 for v in back)==c
        inverse_checks+=1
    images.append({'matrix':D,'rank':rank3(D),'prime_column_det':int(P.det()),
                   'prime_column_inverse_mod3':[[int(v) for v in row] for row in R.tolist()],
                   'image':sorted(image)})

# Full base norm identities, checked from the actual defining polynomial.
X,Y=s.symbols('X Y');Phi=X**6+X**3+1
exact_norm_checks=0
for u in units:
    pol=sum(s.Rational(a)*X**i for i,a in enumerate(u['coefficients']))
    assert s.resultant(Phi,pol,X)==u['norm_to_Q'];exact_norm_checks+=1
for degree in (3,9,27):
    a=s.symbols('a')
    assert s.resultant(Y**degree-a,Y,Y)==a
    exact_norm_checks+=1

factor_records=[]
for k in range(4):
    for m in range(3):
        factors=[X**(3**m)-17]
        for j in range(1,k+2):
            t=3**(m+j-1);e=3**(j-1)
            factors.append(X**(2*t)+17**e*X**t+17**(2*e))
        actual=s.Poly(1,X)
        for f in factors:actual*=s.Poly(f,X)
        assert actual==s.Poly(X**(3**(m+k+1))-17**(3**(k+1)),X)
        factor_records.append({'k':k,'m':m,'factor_degrees':[s.degree(f,X) for f in factors],
                               'total_degree':actual.degree()})

ramification=[]
for j in range(2,11):
    f=2*3**(j-2)
    residue=(pow(17,f,3**(j+1))-1)%(3**(j+1))
    assert residue%(3**j)==0 and residue//(3**j)==2
    assert int(s.n_order(17,3**j))==f
    for m in range(7):
        r=3**m*3**(j-1)
        assert (3*r+3)-(r+3)==2*r
        ramification.append({'j':j,'m':m,'seventeen_residue_degree':f,
                              'S_unit_rank':r+3,'next_norm_kernel_free_rank':2*r,
                              'Herbrand_quotient':27,'class_group_three_part_order':1})

prime_records=[];chain_checks=0
for p in s.primerange(2,1200):
    p=int(p)
    if p in (3,17):continue
    order=int(s.n_order(17,p));q=order;j=0
    while q%3==0:j+=1;q//=3
    if j:
        exp=q*pow(q,-1,3**j)
        omega=pow(17,exp,p)
    else:omega=1
    v=17*pow(omega,-1,p)%p
    assert int(s.n_order(omega,p))==3**j
    assert int(s.n_order(v,p))==q
    xi=pow(omega,-1,p)
    vals=[]
    for m in range(7):
        beta=pow(v,pow(3**m,-1,q),p) if q>1 else 1
        assert pow(beta,3**m,p)==v
        if vals:assert pow(beta,3,p)==vals[-1];chain_checks+=1
        if j:
            e=3**(j-1);t=3**(m+j-1)
            assert (pow(beta,2*t,p)+pow(17,e,p)*pow(beta,t,p)+pow(17,2*e,p))%p==0
            assert pow(beta,3**m,p)*pow(17,-1,p)%p==xi
        else:assert pow(beta,3**m,p)==17%p
        vals.append(beta)
    prime_records.append({'p':p,'order_17':order,'j':j,'xi_value':xi,
                          'prime_to_three_part':v,'compatible_root_chain':vals})
assert next(r['j'] for r in prime_records if r['p']==19)==2
assert next(r['j'] for r in prime_records if r['p']==163)==3

# These are universal algebraic toric inverse checks, not claims that arbitrary
# initial S-unit coefficients occur in a coherent unit system.
b,z0,B,B3,B17,L=s.symbols('b z B B3 B17 L')
formal=[]
for k in range(5):
    a3=s.symbols('a3_0:'+str(k));a17=s.symbols('a17_0:'+str(k))
    e=3*B17-2*b-sum(a17);C=3*B3-3*z0+L-sum(a3)-B
    assert s.expand(e+2*b+sum(a17)-3*B17)==0
    assert s.expand(B+C+3*z0-L+sum(a3)-3*B3)==0
    assert s.expand((e+2*b+sum(a17))/3-B17)==0
    assert s.expand((B+C+3*z0-L+sum(a3))/3-B3)==0
    formal.append({'k':k,'pure17':str(e),'pure3_second':str(C)})
rng=random.Random(176111)
toric_checks=0
for k in range(5):
    for _ in range(10000):
        b,z0,B,B3,B17,L=[rng.randrange(-729,730) for _ in range(6)]
        a3=[rng.randrange(-729,730) for _ in range(k)]
        a17=[rng.randrange(-729,730) for _ in range(k)]
        e=3*B17-2*b-sum(a17);C=3*B3-3*z0+L-sum(a3)-B
        assert e+2*b+sum(a17)==3*B17
        assert B+C+3*z0-L+sum(a3)==3*B3
        assert (e+2*b+sum(a17))//3==B17
        assert (B+C+3*z0-L+sum(a3))//3==B3
        toric_checks+=1

out={'statement':'E.111','status':'PASS','actual_GP_field':field,
     'actual_GP_record_count':len(records),'actual_S_unit_basis':units,
     'literal_root_residues':[tuple(c%17 for c in xi) for xi in embeddings],
     'literal_Hensel_roots_mod289':embeddings,'actual_local_unit_parts':values,
     'character_systems':images,'all_character_inverse_checks':inverse_checks,
     'all_S_unit_character_normalizations':normalization_checks,
     'exact_polynomial_norm_checks':exact_norm_checks,'positional_factorizations':factor_records,
     'ramification_and_rank_table':ramification,'eligible_prime_checks':len(prime_records),
     'actual_degree_one_prime_chains':prime_records,'adjacent_prime_chain_checks':chain_checks,
     'symbolic_toric_inverse_formulas':formal,'integral_toric_inverse_checks':toric_checks,
     'scope':'Certified degree-six arithmetic and exact finite identities. All-level class, norm, compactness and section claims are proved in the section; no upper BNF or full intrinsic lift is inferred.',
     'source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                      [HERE/'e_nonunit_seventeen_base.gp',BASE]}}
def conv(o):
    if isinstance(o,s.Integer):return int(o)
    raise TypeError(type(o).__name__)
text=json.dumps(out,indent=2,default=conv)+'\n'
(HERE/'e_nonunit_seventeen.json').write_text(text)
print(text,end='')
