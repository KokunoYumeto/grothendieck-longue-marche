#!/usr/bin/env python3
"""Exact fixed-row unit-lattice certificate for A194; no bounded-search premise."""
from pathlib import Path
from fractions import Fraction as F
import json,sys,itertools
import sympy as S
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parent;d=649
base=json.loads((B/'two_inert_zeta9_base_units_certificate_data.json').read_text())
nat=base['natural_unit_numerators']
us=[[F(x)for x in u['candidate']]for u in json.loads(
    (B/'two_inert_relative_unit_repair_certificate_data.json').read_text())['units']]
rs=[[F(x)for x in r]for r in json.loads(
    (B/'two_inert_level2_anti_cube_root_certificate_data.json').read_text())['roots']]
labels=[f'e{i+1}'for i in range(9)]+[
    f'g{j}({u})'for j in range(3)
    for u in ['u1','u2','u3','u4','epsilon','r2','r3','r4']]
W=[(307,78,287),(307,78,93),(307,78,53),(307,78,168),
   (307,78,274),(307,78,46),(307,98,287),(307,98,93),
   (307,143,287),(307,143,93),(307,189,287),(523,20,468),
   (523,20,410),(523,20,217),(523,154,468),(523,154,410),
   (523,156,468),(523,156,410),(523,311,468),(523,311,410),
   (613,47,467)]
C=[1,2,3,4,5,6,7,8,9,11,12,15,16,17,19,20,23,24,25,31,32]
def residue(cs,p):return [c.numerator*pow(c.denominator,-1,p)%p for c in cs]
def ev(cs,x,p):
    a=0
    for c in reversed(cs):a=(a*x+c)%p
    return a
rows=[];values=[]
for p,t,z in W:
    assert S.isprime(p) and p%9==1
    assert pow(t,9,p)==3*d**6%p and pow(z,9,p)==1 and pow(z,3,p)!=1
    assert all(c.denominator%p for cs in us+rs for c in cs)
    um=[residue(cs,p)for cs in us];rm=[residue(cs,p)for cs in rs]
    om=pow(z,3,p);alpha=pow(t,3,p)*pow(d*d,-1,p)%p
    mon=[pow(alpha,i,p)*pow(z,j,p)%p for i in range(3)for j in range(6)]
    vals=[sum(c*m for c,m in zip(row,mon))*pow(3,-1,p)%p for row in nat]
    for j in range(3):
        tj=t*pow(z,j,p)%p;aj=pow(tj,3,p)*pow(d*d,-1,p)%p
        w=pow(tj,5,p)*pow(d**3*(om-1),-1,p)%p
        assert pow(w,18,p)==-3*d**6%p
        assert (pow(w,9,p)*pow(d**3,-1,p)-1)*pow(2,-1,p)%p==om
        assert -om*w*w%p==tj
        pi=aj*aj*pow(om-1,-1,p)%p;tp=-om*pi%p
        v=(1+pi)*pow(1+pi*pi,-1,p)%p
        tv=(1+tp)*pow(1+tp*tp,-1,p)%p
        eps=v*pow(tv,-1,p)%p
        vals += [ev(cs,tj,p)for cs in um]+[eps]+[ev(cs,w,p)for cs in rm]
    assert len(vals)==33 and all(vals)
    powers=[1,om,om*om%p]
    rows.append([powers.index(pow(v,(p-1)//3,p))for v in vals])
    values.append(vals)
minor=S.Matrix([[row[c-1]for c in C]for row in rows])
det=int(minor.det());assert det==13000436 and det%3==2
print('PASS: all693 literal finite-field unit values and cube characters.')
print('PASS: exact21x21 minor determinant13000436, nonzero modulo3.')
G=list(itertools.product(range(3),repeat=2))
Hs=[]
for u in G:
    if u==(0,0):continue
    H=frozenset((k*u[0]%3,k*u[1]%3)for k in range(3))
    if H not in Hs:Hs.append(H)
assert len(Hs)==4
for a in G:assert sum(a in H for H in Hs)==1+3*(a==(0,0))
for j in range(3):
    assert frozenset(((3-j)*k%3,k)for k in range(3)) in Hs
assert 54//2-1+1==27 and 27-21==6
print('PASS: exact integral norm-sum identity on C3xC3 and four stabilizers.')
out={'labels':labels,'residue_maps':W,'values':values,'matrix':rows,
     'minor_columns_one_based':C,'minor_determinant':det,
     'norm_subgroups':[[list(x)for x in sorted(H)]for H in Hs],
     'quotient_exponent':3,'quotient_dimension_upper_bound':6,
     'scope':'Exact elementary quotient bound, without asserting equality of its order.'}
(B/'two_inert_ninth_root_subfield_unit_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
