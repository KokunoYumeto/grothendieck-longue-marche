#!/usr/bin/env python3
"""Actual finite-prime cubic characters of the 45 literal upper S-units.

A residue rank is a lower bound on the image modulo global cubes.
A null vector is only a candidate for a subsequent exact root test.
"""
from pathlib import Path
from fractions import Fraction
import argparse,hashlib,json
from sympy import primerange,primitive_root

R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--prime-bound',type=int,default=10000)
args=ap.parse_args()
def rec(path,tag):
    return next(x for x in (json.loads(l) for l in path.read_text().splitlines() if l.startswith('{')) if x['type']==tag)
lowerpath=R/'inputs/e119_six_character_witness.out'
upperpath=R/'code/e53_upper_unit_candidates.out'
L=rec(lowerpath,'six_characters')['unit_columns']
U=rec(upperpath,'verified_candidate_S_units')['elements']
L=[[Fraction(t) for t in f] for f in L]
U=[[Fraction(t) for t in f] for f in U]
assert len(L)==15 and len(U)==10
def modcoeff(f,p):
    assert all(t.denominator%p for t in f)
    return [t.numerator*pow(t.denominator,-1,p)%p for t in f]
def ev(f,x,p):
    a=0
    for c in reversed(f):a=(a*x+c)%p
    return a
def insert(row,echelon):
    v=list(row)
    for j,w in sorted(echelon.items()):
        a=v[j]
        if a:v=[(x-a*y)%3 for x,y in zip(v,w)]
    at=next((j for j,x in enumerate(v) if x),None)
    if at is None:return False
    v=[pow(v[at],-1,3)*x%3 for x in v]
    for j,w in list(echelon.items()):
        a=w[at]
        if a:echelon[j]=[(x-a*y)%3 for x,y in zip(w,v)]
    echelon[at]=v
    return True

rows=[];basis=[];echelon={};primes_tested=[];split_primes=[];denominator_primes=[]
for p in primerange(5,args.prime_bound+1):
    if p==53 or p%9!=1:continue
    if any(t.denominator%p==0 for f in L+U for t in f):
        denominator_primes.append(int(p));continue
    primes_tested.append(int(p))
    g=int(primitive_root(p));xi0=pow(g,(p-1)//9,p)
    xis=[pow(xi0,k,p) for k in [1,2,4,5,7,8]]
    coeffL=[modcoeff(f,p) for f in L];coeffU=[modcoeff(f,p) for f in U]
    inv53=pow(53,-1,p);n0=len(rows)
    for b in range(1,p):
        z=pow(b,9,p)*inv53%p
        if (z*z+z+1)%p:continue
        for xi in xis:
            if pow(xi,3,p)!=z:continue
            a=pow(b,3,p)*pow(xi,-1,p)%p
            assert pow(a,3,p)==53%p
            x=(xi-a)%p
            values=[ev(f,x,p) for f in coeffL]
            values += [ev(f,b*pow(xi,j,p)%p,p) for f in coeffU for j in range(3)]
            assert len(values)==45 and all(values),(p,b,xi)
            phases={1:0,z:1,z*z%p:2}
            row=[phases[pow(v,(p-1)//3,p)] for v in values]
            witness={'p':int(p),'beta2':b,'xi':xi,'zeta':z,'character':row}
            rows.append(witness)
            if insert(row,echelon):basis.append(witness)
    if len(rows)>n0:split_primes.append(int(p))
    if len(echelon)==33:break
assert len(echelon)<=33
free=[j for j in range(45) if j not in echelon]
null=[]
for j in free:
    v=[0]*45;v[j]=1
    for k,w in echelon.items():v[k]=-w[j]%3
    assert all(sum(a*b for a,b in zip(v,r['character']))%3==0 for r in rows)
    null.append(v)
d={'status':'PASS','prime_bound':args.prime_bound,'primes_tested':primes_tested,
   'primes_skipped_for_power_basis_denominators':denominator_primes,
   'split_primes':split_primes,'actual_embedding_count':len(rows),
   'rank_mod_three':len(echelon),'ambient_S_unit_dimension_mod_cubes':33,
   'independent_witnesses':basis,'all_witnesses':rows,
   'rref_pivots':sorted(echelon),'rref_rows':[echelon[k] for k in sorted(echelon)],
   'residue_nullspace_candidates':null,
   'column_order':'15 literal lower columns, then each of ten smaller-field columns at beta2,xi*beta2,xi^2*beta2',
   'scope':'Exact finite-prime residue maps; rank is a proved lower bound. Null vectors are only candidates, not assertions of global cubeness or unit-basis completeness.',
   'input_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [lowerpath,upperpath]}}
out=json.dumps(d,indent=2)+'\n'
(R/'code/e53_upper_residue_search.json').write_text(out)
print(out,end='')
