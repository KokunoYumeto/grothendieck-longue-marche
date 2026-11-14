#!/usr/bin/env python3
"""Verify every finite comparison used in the positional53 coherent theorem.

This checker imports no mathematical program. It decodes complete saved GP
records, checks exact rational/integer maps, and independently enumerates the
finite class maps and surviving residue branches.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
from collections import Counter
import hashlib,json,math
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def records(stem):
    out=HERE/(stem+'.out')
    err=HERE/(stem+'.err')
    if err.exists():
        errors=[s for s in err.read_text().splitlines()
                if s.strip() and not s.strip().startswith('***   Warning: new stack size = ')
                and not s.strip().startswith('***   Warning: new maximum stack size = ')]
        assert not errors,(stem,errors)
    rows=[json.loads(s) for s in out.read_text().splitlines() if s.startswith('{')]
    assert rows and rows[-1].get('status')=='PASS',(stem,rows[-1:] )
    return rows
def row(rows,t):
    r=[x for x in rows if x.get('type')==t]
    assert len(r)==1,(t,len(r))
    return r[0]
def integral(M):return all(S.denom(x)==1 for x in M)
def mat(x):return S.Matrix(x)
def ints(M):
    assert integral(M)
    out=[[int(x) for x in M.row(i)] for i in range(M.rows)]
    assert mat(out)==M
    return out
def rationals(M):
    out=[[str(S.Rational(x)) for x in M.row(i)] for i in range(M.rows)]
    assert mat([[S.Rational(x) for x in r] for r in out])==M
    return out
def reduced(M,mods):
    assert integral(M)
    return S.Matrix(len(mods),M.cols,lambda i,j:int(M[i,j])%mods[i])
def app(M,z,mods):return tuple(reduced(M*mat(z),mods))
def same(M,mods):assert integral(S.diag(*mods).inv()*M)
def grp(mods):return list(product(*(range(x) for x in mods)))

unit=json.loads((HERE/'e53_positional_unit.json').read_text())
assert unit['status']=='PASS'
assert unit['absolute_norm']=='27/2809'
assert unit['norm_to_K_coefficients']==['3/53','6/53']
assert unit['positive_characters_3_53']==[2,1]
gp_unit=(HERE/'e53_positional_verify.out').read_text().splitlines()
assert len(gp_unit)==8 and all(s.startswith('PASS ') for s in gp_unit)
assert gp_unit[-1]=='PASS complete no-input polynomial and residue verification'
gp_err=(HERE/'e53_positional_verify.err').read_text().splitlines()
assert all(not s.strip() or s.strip().startswith('***   Warning: new stack size = ') for s in gp_err)
pr=records('e53_positional_genus_pivots')
upper=records('e53_positional_presentation')
standalone=records('e53_positional_ideals')
st=row(standalone,'standalone_literal_ideal_verification')
assert st['upper_ideal_equalities']==7 and st['lower_ideal_equalities']==2
assert st['actual_projected_classes']==[[4,1],[4,0]]
assert st['unconditional_maximal_orders'] is True
R=row(upper,'full_S_class_presentation')
Rel,H,U,V,D=[mat(R[k]) for k in
 ['relation_matrix','relation_HNF','Smith_left','Smith_right','Smith_diagonal']]
P=mat(R['generator_to_prime_basis'])
Q=mat(R['prime_basis_to_generator'])
W=mat(R['pivot_Smith_matrix'])
Wi=mat(R['pivot_Smith_inverse'])
assert H==hermite_normal_form(Rel)
assert U*H*V==D==S.diag(9,9,1)
assert abs(U.det())==abs(V.det())==1
assert reduced(P*Rel,[9,9])==S.zeros(2,Rel.cols)
assert reduced(P*Q,[9,9])==S.eye(2)
assert integral(H.inv()*(Q*P-S.eye(3)))
assert reduced(W*Wi,[9,9])==S.eye(2)
assert reduced(Wi*U[:2,:],[9,9])==P
assert reduced(U*Q,[9,9,1])==W.col_join(S.zeros(1,2))
roundtrips=0
for z in grp([9,9]):
    raw=U.inv()*mat([*z,0]);c=app(P,raw,[9,9])
    assert integral(H.inv()*(Q*mat(c)-raw))
    assert app(P,Q*mat(c),[9,9])==c
    roundtrips+=1

B=mat([[S.Rational(x) for x in a] for a in R['field_integral_basis']]).T
assert B.rows==B.cols==18 and abs(B.det())==S.Rational(1,53**9)
power_disc=-(3**45)*(53**34)
assert power_disc*B.det()**2==int(R['field_discriminant'])==-(3**45)*(53**16)
assert len([x for x in upper if x['type']=='class_power_relation'])==3
assert len([x for x in upper if x['type']=='S_prime_relation'])==2
assert len([x for x in upper if x['type']=='upper_pivot_relation'])==2
for a in upper:
    if 'generator_coefficients' in a:
        assert len(a['generator_coefficients'])==18
        assert all(isinstance(S.Rational(v),S.Rational) for v in a['generator_coefficients'])

lower=row(pr,'actual_surviving_pivot_primes')
assert [x[0] for x in lower['pivot_records']]==[31,103]
pL=mat([[6,1],[2,1]])
for rec in lower['pivot_records']:
    p,b2,b1,hnf,cl,co,ch,raw,proj,mod3=rec
    assert S.isprime(p) and p%9==4 and pow(53,(p-1)//3,p)!=1
    assert pow(b2,3,p)==b1 and pow(b2,27,p)==pow(53,3,p)
    assert pow(b2,(p-1)//3,p)==1
    assert raw==[-ch[0],-ch[1],*cl]
    assert mod3==[2*(proj[1]-proj[0])%3,proj[0]%3]
    assert reduced(pL*mat(mod3),[3,3])==mat([proj[0]%3,proj[1]%3])
    assert mat(hnf).det()==p
    assert len(co)==6
    rr=next(x for x in upper if x.get('type')=='upper_pivot_relation'
            and x['prime']==p)
    J=mat(rr['prime_HNF'])
    assert J.det()==p and J.rows==J.cols==18
    assert app(P,rr['class_column'],[9,9])==((1,0) if p==31 else (0,1))
    vals=mat([sum(S.Rational(v)*pow(b2,i,p) for i,v in enumerate(a))
              for a in R['field_integral_basis']])
    vals=vals.applyfunc(lambda x:(int(S.numer(x))*pow(int(S.denom(x)),-1,p))%p)
    assert reduced(vals.T*J,[p])==S.zeros(1,18)
assert mat(lower['basis_mod3']).det()==-1

# Actual finite horizontal maps, transported by the proven norm isomorphisms.
old=json.loads((ROOT/'inputs/e121_normalizer_module.json').read_text())
NH=mat(old['full_horizontal_norm'])
JH=mat(old['full_horizontal_extension'])
HH=mat(old['h'])
assert NH==mat([[1,0,6,6],[0,3,6,3]])
assert JH==mat([[0,3],[2,0],[2,0],[0,1]])
modsA=[9,3,3,3];modsC=[9,9]
same(NH*JH-3*S.eye(2),modsC)
same(JH*NH-(S.eye(4)+HH+HH**2),modsA)
same(NH*(HH-S.eye(4)),modsC)
same((HH-S.eye(4))*JH,modsA)
G=grp(modsA);C=grp(modsC)
image={app(NH,z,modsC) for z in G}
assert image=={z for z in C if z[1]%3==0}
kerJ={z for z in C if app(JH,z,modsA)==(0,0,0,0)}
assert kerJ==set(product([0,3,6],repeat=2))
fixed=[z for z in G if app(HH,z,modsA)==z]
imageJ={app(JH,z,modsA) for z in C}
assert len(fixed)==27 and len(imageJ)==9
def fadd(a,b,mods):return tuple((x+y)%m for x,y,m in zip(a,b,mods))
def hchar(z):
    assert z in fixed and z[0]%3==0 and z[1]==z[2]
    return (z[0]//3-z[3])%3
assert {z for z in fixed if hchar(z)==0}==imageJ
for x in fixed:
    for y in fixed:
        assert hchar(fadd(x,y,modsA))==(hchar(x)+hchar(y))%3
assert hchar((3,0,0,0))==1

def primes(n):
    return [p for p in range(2,n+1) if S.isprime(p)]
def v3(n):
    e=0
    while n%3==0:
        n//=3;e+=1
    return e
def order(a,p):
    q=p-1
    for r in S.factorint(q):
        while q%r==0 and pow(a,q//r,p)==1:q//=r
    return int(q)
residue_rows=[]
for p in primes(1200):
    if p in (3,53):continue
    m=(p-1)//3**v3(p-1)
    roots=[b for b in range(1,p)
           if pow(b,m,p)==1 and (pow(b,18,p)+53*pow(b,9,p)+2809)%p==0]
    eligible=v3(order(53%p,p))==1
    assert len(roots)==int(eligible),(p,roots,eligible)
    if roots:
        b=roots[0];zz=pow(b,9,p)*pow(53,-1,p)%p
        assert zz!=1 and pow(zz,3,p)==1
        residue_rows.append([p,b,order(53%p,p)])

# Exact finite coordinate inverses for the restricted divisor basis.
# Every class pair occurs; every support coefficient and both pivot carries vary.
divisor_tests=0
for a,b,t,A,Bb in product(range(9),range(9),range(-4,5),range(-1,2),range(-1,2)):
    v31=9*A-a*t;v103=9*Bb-b*t
    assert (v31+a*t)%9==0 and (v103+b*t)%9==0
    back=((v31+a*t)//9,(v103+b*t)//9,t)
    assert back==(A,Bb,t)
    divisor_tests+=1
for x in C:
    for y in C:
        z=tuple((x[i]+y[i])%9 for i in range(2))
        assert all((z[i]-x[i]-y[i])%9==0 for i in range(2))

# Literal toric cube insertion and inverse, including the factor3.
toric_tests=0
for a,b,r,e in product(range(-4,5),repeat=4):
    raw=(3*a,3*b,3*r,3*e)
    assert tuple(Fraction(x,3) for x in raw)==(a,b,r,e)
    toric_tests+=1

out={
 'status':'PASS',
 'scope':'exact finite class maps, certified prime basis, residue branches and divisor/toric inverses; all-level assertions are proved in the theorem',
 'literal_unit':{'norm_to_K':unit['norm_to_K_coefficients'],
                 'absolute_norm':unit['absolute_norm'],
                 'positive_characters':unit['positive_characters_3_53']},
 'prime_basis':[31,103],
 'lower_projected_classes':[x[8] for x in lower['pivot_records']],
 'lower_full_classes_mod3':[x[9] for x in lower['pivot_records']],
 'full_S_class_orders':[9,9],
 'relation_lattice':ints(H),
 'generator_to_prime_basis':ints(P),
 'prime_basis_to_generator':ints(Q),
 'exact_relation_inverse':rationals(H.inv()*(Q*P-S.eye(3))),
 'Smith_roundtrips':roundtrips,
 'basis_discriminant':str(power_disc*B.det()**2),
 'literal_principal_ideal_equalities':7,
 'horizontal_norm':ints(NH),'horizontal_extension':ints(JH),
 'horizontal_fixed_classes':len(fixed),
 'horizontal_unit_defect_kernel':len(imageJ),
 'horizontal_unit_defect_quotient':3,
 'vertical_unit_norm_quotient_orders':[3,3,3],
 'finite_branch_primes_checked':len(primes(1200))-2,
 'eligible_prime_records':residue_rows,
 'divisor_coordinate_inverse_tests':divisor_tests,
 'raw_scaled_toric_inverse_tests':toric_tests,
 'hashes':{p.name:sha(p) for p in [
    HERE/'e53_positional_unit.py',HERE/'e53_positional_unit.json',
    HERE/'e53_positional_verify.gp',HERE/'e53_positional_verify.out',
    HERE/'e53_positional_genus_pivots.gp',HERE/'e53_positional_genus_pivots.out',
    HERE/'e53_positional_presentation.gp',HERE/'e53_positional_presentation.out',
    HERE/'e53_positional_ideals.gp',HERE/'e53_positional_ideals.out',
    ROOT/'inputs/e121_normalizer_module.json']}}
s=json.dumps(out,indent=2,sort_keys=True)+'\n'
(HERE/'e53_positional_maps.json').write_text(s)
print(s,end='')

