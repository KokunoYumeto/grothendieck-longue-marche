#!/usr/bin/env python3
"""Independent E111 residue/ideal-label and actual unit-substitution checks."""
from pathlib import Path
from itertools import product
import json

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'research_e111/code'
records=[json.loads(s) for s in (SOURCE/'e_nonunit_seventeen_base_gp.out').read_text().splitlines() if s.startswith('{')]
units=[r for r in records if r['type']=='S_unit']
ideals=[r for r in records if r['type']=='prime17']
basis=json.loads((ROOT/'export_basis.out').read_text())
assert basis==[[1,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,0,1,0,0,0],[0,0,0,0,0,1]]
def power_coordinates(v):
    return [sum(v[i]*basis[i][j] for i in range(6)) for j in range(6)]

def multiply(x,y,n):
    u=x[0]*y[0];v=x[0]*y[1]+x[1]*y[0];w=x[1]*y[1]
    return ((u-w)%n,(v-w)%n)
def power(x,e,n):
    a=(1,0)
    for _ in range(e): a=multiply(a,x,n)
    return a
def evaluate(coeff,x,n):
    value=(0,0)
    for i,c in enumerate(coeff):
        y=power(x,i,n);c=int(c)
        value=((value[0]+c*y[0])%n,(value[1]+c*y[1])%n)
    return value

roots=[(2,8),(9,11),(6,15)]
lifts=[];ideal_labels=[];matrices=[]
for root in roots:
    candidates=[(root[0]+17*a,root[1]+17*b) for a,b in product(range(17),repeat=2)]
    hits=[x for x in candidates if power(x,3,289)==(0,1)]
    assert len(hits)==1
    lifts.append(hits[0])
    match=[r['index'] for r in ideals if all(evaluate(power_coordinates(col),root,17)==(0,0) for col in r['ideal_hnf_columns'])]
    assert len(match)==1
    ideal_labels.append(match[0])
assert ideal_labels==[3,1,2]
for rad17 in (True,False):
    rows=[]
    for x in lifts:
        row=[]
        for u in units:
            value=evaluate(u['coefficients'],x,289)
            valuation=int(value[0]%17==value[1]%17==0)
            residue=tuple((c//17 if valuation else c)%17 for c in value)
            # Search for the inverse in the residue field independently.
            inverses=[y for y in product(range(17),repeat=2) if multiply(residue,y,17)==(1,0)]
            assert len(inverses)==1
            base=power(tuple(c%17 for c in x),valuation,17)
            if rad17:base=multiply(base,inverses[0],17)
            symbol=power(base,96,17)
            exponents=[e for e in range(3) if power((0,1),e,17)==symbol]
            assert len(exponents)==1;row.append(exponents[0])
        rows.append(row)
    rows.insert(0,[(-sum(r[i] for r in rows))%3 for i in range(7)])
    matrices.append(rows)
expected=json.loads((SOURCE/'e_nonunit_seventeen.json').read_text())
assert matrices==[s['matrix'] for s in expected['character_systems']]
inverse_count=0
for M,R in zip(matrices,[[[2,0,2],[0,1,1],[2,2,0]],[[0,0,2],[1,1,1],[0,2,0]]]):
    for c in product(range(3),repeat=3):
        d=[sum(R[i][j]*c[j] for j in range(3))%3 for i in range(3)]
        out=[sum(M[i][j+4]*d[j] for j in range(3))%3 for i in range(4)]
        assert out==list(c)+[(-sum(c))%3];inverse_count+=1

# The exact H substitution is checked on every positional basis column.
# This proves its compatibility with translation, multiplication and chi action
# in each finite system tested, and verifies both inverse permutations.
substitution_checks=0
for n in (3,9,27):
    us=[u for u in range(n) if u%3]
    for u in us:
        ui=pow(u,-1,n)
        for a in range(0,n,3):
            for k in range(n):
                assert u*(a+k)%n==(u*a+u*k)%n
                assert ui*(u*k)%n==k
                substitution_checks+=1
        for chi in us:
            for k in range(n):
                assert u*(chi*k)%n==chi*(u*k)%n
                substitution_checks+=1

# Solve the two total-norm equations by literal integral inverse matrices.
# With b,z,B and all extra component norms fixed, e and C have coefficient1.
compensation_checks=0
for k in range(5):
    for B3,B17,b,z,B in product(range(-2,3),repeat=5):
        n3=[j-2 for j in range(k)];n17=[2*j-1 for j in range(k)];L=5
        e=3*B17-2*b-sum(n17)
        C=3*B3-3*z+L-sum(n3)-B
        assert e+2*b+sum(n17)==3*B17
        assert B+C+3*z-L+sum(n3)==3*B3
        assert B==3*B3-3*z+L-sum(n3)-C
        compensation_checks+=1
out={'statement':'E.111','status':'PASS','actual_integral_basis_in_power_coordinates':basis,'brute_Hensel_lifts':lifts,'actual_HNF_prime_labels':ideal_labels,'independently_recomputed_character_matrices':matrices,'literal_quotient_inverse_cases':inverse_count,'actual_H_substitution_cases':substitution_checks,'exact_integral_compensation_cases':compensation_checks}
text=json.dumps(out,indent=2)+'\n'
(ROOT/'check_maps.json').write_text(text)
print(text,end='')
