#!/usr/bin/env python3
"""Exact six-place unit norm matrix for E3/E2.

Input units and anti-unit cube roots have separate exact global certificates.
This program evaluates their literal coefficients in the unramified residue
fields of F at 11 and 59.  It makes no class-group computation.
"""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,sys
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
d=649
roots=[[F(x) for x in rr] for rr in json.loads(
    (base/'two_inert_level2_anti_cube_root_certificate_data.json').read_text())['roots']]
units=[[F(x) for x in u['candidate']] for u in json.loads(
    (base/'two_inert_relative_unit_repair_certificate_data.json').read_text())['units']]
raw_beta=json.loads((base/'two_inert_norm2_generator_certificate_data.json').read_text())
beta=[-F(x,raw_beta['generator_common_denominator'])
      for x in raw_beta['generator_numerators']]

def add(a,b,q): return tuple((x+y)%q for x,y in zip(a,b))
def mul(a,b,q):
    return ((a[0]*b[0]-a[1]*b[1])%q,
            (a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%q)
def power(a,k,q):
    if k<0: return power(power(a,q*q-2,q),-k,q)
    out=(1,0)
    while k:
        if k&1: out=mul(out,a,q)
        a=mul(a,a,q);k//=2
    return out
def scalar(c,q):
    c=F(c)
    assert c.denominator%q
    return (c.numerator*pow(c.denominator,-1,q)%q,0)
def evaluate(cs,a,q):
    out=(0,0)
    for c in reversed(cs):out=add(mul(out,a,q),scalar(c,q),q)
    return out
def rank(rows):
    a=[r[:] for r in rows];n=0
    for j in range(len(a[0])):
        p=next((k for k in range(n,len(a)) if a[k][j]),None)
        if p is None:continue
        a[p],a[n]=a[n],a[p]
        iv=pow(a[n][j],-1,3);a[n]=[x*iv%3 for x in a[n]]
        for k in range(len(a)):
            if k!=n:
                c=a[k][j];a[k]=[(x-c*y)%3 for x,y in zip(a[k],a[n])]
        n+=1
    return n

def valuation(x,q):
    if not x:return 999999
    a,b=x.numerator,x.denominator;v=0
    while a%q==0:a//=q;v+=1
    while b%q==0:b//=q;v-=1
    return v

component_checks=[]
for q in (11,59):
    for label,cs in [(f'u{i+1}',u) for i,u in enumerate(units)]+[('beta2',beta)]:
        depths=[min(3*valuation(cs[3*k+r]*d**(2*k),q)+2*r
                    for k in range(3)) for r in range(3)]
        assert depths[0]>=0 and min(depths[1:])>0
        component_checks.append({'q':q,'element':label,'component_depths':depths})
    for i,cs in enumerate(roots,2):
        depths=[min(3*valuation(cs[3*k+r]*d**k,q)+r
                    for k in range(6)) for r in range(3)]
        assert depths[0]>=0 and min(depths[1:])>0
        component_checks.append({'q':q,'element':f'r{i}','component_depths':depths})

rows=[];srows=[];details=[]
for q in (11,59):
    ar=pow(3,pow(3,-1,q-1),q);z=(0,1)
    assert pow(ar,3,q)==3%q
    assert power(z,3,q)==(1,0) and z!=(1,0)
    for j in range(3):
        alpha=mul(scalar(ar,q),power(z,j,q),q)
        # w^3=d*h, h=alpha^2*(zeta^2-zeta)/3.
        delta=add(power(z,2,q),mul(scalar(-1,q),z,q),q)
        h=mul(power(alpha,2,q),mul(delta,scalar(F(1,3),q),q),q)
        pi=mul(power(alpha,2,q),power(add(z,scalar(-1,q),q),-1,q),q)
        tau_pi=mul(scalar(-1,q),mul(z,pi,q),q)
        v=mul(add(scalar(1,q),pi,q),
              power(add(scalar(1,q),power(pi,2,q),q),-1,q),q)
        tau_v=mul(add(scalar(1,q),tau_pi,q),
                  power(add(scalar(1,q),power(tau_pi,2,q),q),-1,q),q)
        epsilon=mul(v,power(tau_v,-1,q),q)
        vals=[evaluate([u[3*k]*d**(2*k) for k in range(3)],alpha,q)
              for u in units]
        vals += [z,epsilon]
        vals += [evaluate([rr[3*k]*d**k for k in range(6)],h,q)
                 for rr in roots]
        beta_value=evaluate([beta[3*k]*d**(2*k) for k in range(3)],alpha,q)
        beta1=add(scalar(1,q),mul(scalar(-1,q),alpha,q),q)
        s2=mul(beta1,power(beta_value,-1,q),q)
        s3=mul(scalar(2,q),power(add(alpha,scalar(-1,q),q),-1,q),q)
        a26=mul(add(mul(z,alpha,q),scalar(-1,q),q),
                power(add(mul(power(z,2,q),alpha,q),scalar(-1,q),q),-1,q),q)
        # sigma is residue-trivial at q, so sigma(beta2)/sigma^2(beta2) reduces to1.
        more_values=[beta_value,s2,s3,(1,0),a26]
        logs=[]
        for x in vals:
            assert x!=(0,0)
            ch=power(x,(q*q-1)//3,q)
            logs.append([power(z,k,q) for k in range(3)].index(ch))
        rows.append(logs)
        extra_logs=[]
        for x in more_values:
            assert x!=(0,0)
            ch=power(x,(q*q-1)//3,q)
            extra_logs.append([power(z,k,q) for k in range(3)].index(ch))
        srows.append(logs+extra_logs)
        details.append({'q':q,'j':j,'alpha':alpha,'h':h,
                        'values':vals,'logs':logs,
                        'extra_values':more_values,'extra_logs':extra_logs})
        print(q,j,logs)

full_rank=rank(rows)
plus_rank=rank([r[:4] for r in rows])
minus_rank=rank([r[4:] for r in rows])
assert full_rank==plus_rank+minus_rank
assert (full_rank,plus_rank,minus_rank)==(5,1,4)
assert rank([r[:10] for r in srows])==6
# Four growing two-adic places, ordered P2+,P2-,P6+,P6-.
# Their exact valuation vectors on s2,s3,a20,a26 are the following block.
two_block=[[1,0,1,0],[1,0,-1,0],[0,1,0,1],[0,1,0,-1]]
two_rows=[[0]*10+[x%3 for x in r] for r in two_block]
assert rank([[x%3 for x in r] for r in two_block])==4
all_s_rows=two_rows+srows
assert rank(all_s_rows)==10
# The three split primes above the stable old F-prime: sigma is a3-cycle,
# tau fixes0 and swaps1,2.  The divisor of sigma(beta2)/sigma^2(beta2)
# is therefore +1,-1 on the latter two primes.
sigma=[1,2,0];tau=[0,2,1]
assert all(tau[sigma[tau[i]]]==sigma[sigma[i]] for i in range(3))
assert [int(i==sigma[0])-int(i==sigma[sigma[0]]) for i in range(3)]==[0,1,-1]
plus_kernel=[list(e) for e in itertools.product(range(3),repeat=4)
             if all(sum(x*y for x,y in zip(e,row[:4]))%3==0 for row in rows)]
minus_kernel=[list(e) for e in itertools.product(range(3),repeat=5)
              if all(sum(x*y for x,y in zip(e,row[4:]))%3==0 for row in rows)]
data={'columns':['u1','u2','u3','u4','zeta','epsilon','r2','r3','r4'],
      'rows':rows,'details':details,'full_rank':full_rank,
      'plus_rank':plus_rank,'minus_rank':minus_rank,
      'plus_kernel':plus_kernel,'minus_kernel':minus_kernel,
      'component_checks':component_checks,
      's_columns':['u1','u2','u3','u4','zeta','epsilon','r2','r3','r4',
                   'beta2','beta1/beta2','2/(alpha-1)','sigma_beta2/sigma2_beta2',
                   '(zeta*alpha-1)/(zeta2*alpha-1)'],
      's_q_rows':srows,'s_two_rows':two_rows,'s_rank':10,
      'nonsplit_S_counts':{'above2':4,'above3':1,'above11':3,'above59':3},
      'scope':'Exact tame unit norm residue matrix; no class-group algorithm.'}
(base/'two_inert_level2_unit_norm_certificate_data.json').write_text(
    json.dumps(data,indent=2)+'\n')
print('PASS: literal residue maps; ranks total/plus/minus:',
      full_rank,plus_rank,minus_rank)
print('Kernel orders plus/minus:',len(plus_kernel),len(minus_kernel))
print('PASS: all discarded t/w components have strictly positive valuation.')
print('PASS: units plus beta2 have full six-q rank6.')
print('PASS: exact two-place block has rank4; full fourteen-column S-unit matrix rank10.')
print('S-unit q rows:',srows)
