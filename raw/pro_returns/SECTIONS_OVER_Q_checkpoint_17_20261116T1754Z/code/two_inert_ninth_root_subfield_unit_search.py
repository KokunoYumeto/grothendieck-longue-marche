#!/usr/bin/env python3
"""Bounded literal residue search on the four cubic subfields of M/F.

All columns are certified units from A175/A191 and their actual conjugates.
The output rank is a finite residue-image rank unless it reaches 27.
No class-group or unit-group completeness is inferred from a smaller rank.
"""
from pathlib import Path
from fractions import Fraction as F
import json,sys
import sympy as S
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parent;d=649
base=json.loads((B/'two_inert_zeta9_base_units_certificate_data.json').read_text())
nat=base['natural_unit_numerators']
us=[[F(x)for x in u['candidate']]for u in json.loads(
    (B/'two_inert_relative_unit_repair_certificate_data.json').read_text())['units']]
rs=[[F(x)for x in r]for r in json.loads(
    (B/'two_inert_level2_anti_cube_root_certificate_data.json').read_text())['roots']]
cols=[f'Fprime_e{i+1}'for i in range(9)]+[
    f'E2_conjugate{j}_{u}'for j in range(3)
    for u in ['u1','u2','u3','u4','epsilon','r2','r3','r4']]
assert len(cols)==33
def residue(cs,p):return [c.numerator*pow(c.denominator,-1,p)%p for c in cs]
def ev(cs,x,p):
    a=0
    for c in reversed(cs):a=(a*x+c)%p
    return a
echelon={};rows=[];witnesses=[];count=0;primes=0
for pp in S.primerange(19,20000):
    p=int(pp)
    if p%9!=1 or d%p==0 or any(c.denominator%p==0 for cs in us+rs for c in cs):continue
    ts=S.nthroot_mod(3*d**6%p,9,p,all_roots=True)
    if not ts:continue
    primes+=1
    g=int(S.primitive_root(p));z0=pow(g,(p-1)//9,p)
    assert pow(z0,9,p)==1 and pow(z0,3,p)!=1
    um=[residue(cs,p)for cs in us];rm=[residue(cs,p)for cs in rs]
    for t in map(int,ts):
      for z in [pow(z0,k,p)for k in (1,2,4,5,7,8)]:
        om=pow(z,3,p);alpha=pow(t,3,p)*pow(d*d,-1,p)%p
        mon=[pow(alpha,i,p)*pow(z,j,p)%p for i in range(3)for j in range(6)]
        vals=[sum(c*m for c,m in zip(row,mon))*pow(3,-1,p)%p for row in nat]
        for j in range(3):
            tj=t*pow(z,j,p)%p;aj=pow(tj,3,p)*pow(d*d,-1,p)%p
            w=pow(tj,5,p)*pow(d**3*(om-1),-1,p)%p
            assert pow(w,18,p)==-3*d**6%p
            pi=aj*aj*pow(om-1,-1,p)%p;tp=-om*pi%p
            v=(1+pi)*pow(1+pi*pi,-1,p)%p
            tv=(1+tp)*pow(1+tp*tp,-1,p)%p
            eps=v*pow(tv,-1,p)%p
            vals += [ev(cs,tj,p)for cs in um]+[eps]+[ev(cs,w,p)for cs in rm]
        assert len(vals)==33 and all(vals)
        powers=[1,om,om*om%p]
        row=[powers.index(pow(v,(p-1)//3,p))for v in vals]
        count+=1;r=row[:]
        for k,b in sorted(echelon.items()):
            c=r[k]
            if c:r=[(x-c*y)%3 for x,y in zip(r,b)]
        k=next((i for i,x in enumerate(r)if x),None)
        if k is not None:
            iv=pow(r[k],-1,3);echelon[k]=[x*iv%3 for x in r]
            rows.append(row);witnesses.append({'p':p,'t':t,'zeta9':z,'row':row})
            print('INDEPENDENT',len(rows),'prime',p,'t',t,'zeta9',z,flush=True)
        if len(rows)==27:break
      if len(rows)==27:break
    if len(rows)==27:break
out={'columns':cols,'rank':len(rows),'matrix':rows,'witnesses':witnesses,
     'maps_checked':count,'physical_primes':primes,'prime_bound':20000,
     'scope':'Exact finite residue-image rank on explicit subfield units; smaller rank gives no completeness.'}
(B/'two_inert_ninth_root_subfield_unit_search_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('RESULT: residue rank',len(rows),'on',count,'maps at',primes,'primes',flush=True)
