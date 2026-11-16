#!/usr/bin/env python3
"""Search exact locally soluble harmonic quartic twists and one joint character.

Each reported local witness is a rational T for which all three radicands are
actual fourth powers in Q_p, certified by the valuation/unit criterion.  A
missing witness in this search is not a proof of local insolubility.  A proposed
all-place example is tested at every prime <=4500 and every bad prime; the
remaining good primes have an affine point by genus33 and64 boundary points.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
from math import ceil
import json
import sys
from sympy import primerange, factorint
from harmonic_tripod_obstruction_search import hilbert,vu,is_square

BOUNDARIES=(F(0),F(1),F(1,2))
COUNTS={'covers':0,'dyadic_pass':0,'initial_local_pass':0,'nonzero_finite_sum':0,'allplace_witnesses':0}
OUT=[]

def dyadic_key(q):
    z=vu(q,2,16)
    return None if z is None else (z[0]%4,z[1])

def make_dyadic_witnesses():
    table={}
    for b,h,u in product(BOUNDARIES,range(-6,10),range(1,32,2)):
        T=b+F(2)**h*u
        if T in BOUNDARIES:continue
        key=tuple(dyadic_key(T-bb) for bb in BOUNDARIES)
        table.setdefault(key,T)
    return table

DYADIC_WITNESSES=make_dyadic_witnesses()

@lru_cache(maxsize=None)
def pset(x):
    x=F(x)
    return frozenset(int(p) for m in (abs(x.numerator),x.denominator) for p in factorint(m))

def fourth(a,p):
    if not a:return False
    v,u=vu(a,p,16 if p==2 else p)
    return v%4==0 and (u==1 if p==2 else pow(u,(p-1)//__import__('math').gcd(4,p-1),p)==1)

def actual(T,a,p,c):
    return T!=c and all(T!=b and fourth((T-b)/aa,p) for b,aa in zip(BOUNDARIES,a))

def local(a,p,c):
    if p==2:
        key=tuple(dyadic_key(aa) for aa in a)
        T=DYADIC_WITNESSES.get(key)
        if T is None:return None
        if T==c:
            M=max(vu(T-b,2)[0] for b in BOUNDARIES)+8
            T+=F(2)**M
        assert actual(T,a,p,c)
        return T
    # Boundary and infinity discs, using literal representatives.
    for i,b in enumerate(BOUNDARIES):
        if all(i==j or fourth((b-bb)/aa,p) for j,(bb,aa) in enumerate(zip(BOUNDARIES,a))):
            va=vu(a[i],p)[0]
            htarget=6 if p==2 else 2
            e=ceil((htarget-va)/4)
            for step in (e,e+1):
                T=b+a[i]*F(p)**(4*step)
                if actual(T,a,p,c):return T
    if all(fourth(a[0]/aa,p) for aa in a):
        va=vu(a[0],p)[0]
        e=(-8-va)//4
        for step in (e,e-1):
            T=a[0]*F(p)**(4*step)
            if actual(T,a,p,c):return T
    if p==2:
        # Integral discs and all shallow negative-valuation discs. Deep discs
        # have been tested above. These are actual points, not rounded roots.
        for h in range(-4,2):
            for u in range(1,128,2):
                T=F(u)*F(2)**h
                if actual(T,a,p,c):return T
        for T in map(F,range(-64,193)):
            if actual(T,a,p,c):return T
        return None
    for T in map(F,range(p)):
        if actual(T,a,p,c):return T
    return None

def stringify(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):stringify(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [stringify(v) for v in x]
    return x

def main():
    broad='--broad' in sys.argv
    cs=sorted({F(j,k) for k in range(3,9) for j in range(1,k)}-{F(1,2)})
    vals=[1,2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,29,30,31]
    scalars=[1]
    if broad:
        cs=sorted(set(cs)|{F(-2),F(-1),F(-1,2),F(3,2),F(2),F(3)})
        vals=[-z for z in vals]+vals
        scalars=[1,2,3,5,7]
    data_path=Path(__file__).with_name('arbitrary_harmonic_twist_'+('broad_' if broad else '')+'search_data.json')
    small=list(primerange(3,102))
    allgood=list(primerange(3,4501))
    for c,d,e,z in product(cs,vals,vals,scalars):
        # Literal product -r^2 and the character sqrt(2r).
        D=(F(d),F(e),F(-d*e*z*z))
        r=F(abs(d*e*z))
        a=tuple((c-b)/dd for b,dd in zip(BOUNDARIES,D))
        COUNTS['covers']+=1
        if COUNTS['covers']%1000==0:print('progress',COUNTS,flush=True)
        if not any(all((T-b)/aa>0 for b,aa in zip(BOUNDARIES,a)) for T in map(F,[-1,F(1,4),F(3,4),2])):continue
        T2=local(a,2,c)
        if T2 is None:continue
        COUNTS['dyadic_pass']+=1
        witness={2:T2}
        for p in small:
            T=local(a,p,c)
            if T is None:break
            witness[p]=T
        else:
            COUNTS['initial_local_pass']+=1
            S={2}
            for z in (*a,*(c-b for b in BOUNDARIES),2*r):S.update(pset(z))
            for p in sorted(S-set(witness)):
                T=local(a,p,c)
                if T is None:break
                witness[p]=T
            else:
                inv={p:hilbert(witness[p]-c,2*r,p) for p in sorted(S)}
                if sum(inv.values())%2:
                    COUNTS['nonzero_finite_sum']+=1
                    print('NONZERO FINITE SUM',stringify({'c':c,'D':D,'a':a,'r':r,'invariants':inv}),flush=True)
                    for p in allgood:
                        if p in witness:continue
                        T=local(a,p,c)
                        if T is None:
                            print('No searched local witness at',p,flush=True)
                            break
                        witness[p]=T
                    else:
                        assert any(all((T-b)/aa>0 for b,aa in zip(BOUNDARIES,a)) for T in map(F,[-1,F(1,4),F(3,4),2]))
                        COUNTS['allplace_witnesses']+=1
                        boundary_no_i=[]
                        for i,b in enumerate(BOUNDARIES):
                            z=[(b-bb)/aa for j,(bb,aa) in enumerate(zip(BOUNDARIES,a)) if i!=j]
                            boundary_no_i.append(not any(is_square(-q) for q in (z[0],z[1],z[0]*z[1])))
                        item=stringify({'c':c,'D':D,'a':a,'r':r,'invariants':inv,'boundary_no_i':boundary_no_i,'local_T':witness})
                        OUT.append(item)
                        print('ALL-PLACE CANDIDATE',stringify({k:v for k,v in item.items() if k!='local_T'}),flush=True)
                        data_path.write_text(json.dumps({'counts':COUNTS,'candidates':OUT},indent=2)+'\n')
                        if all(boundary_no_i):
                            print('COMPLETE TARGET WITNESS',COUNTS,flush=True)
                            return
        if COUNTS['covers']%1000==0:print('progress',COUNTS,flush=True)
    print('FINITE SEARCH COMPLETE',COUNTS,flush=True)
    data_path.write_text(json.dumps({'counts':COUNTS,'candidates':OUT},indent=2)+'\n')

if __name__=='__main__':main()
