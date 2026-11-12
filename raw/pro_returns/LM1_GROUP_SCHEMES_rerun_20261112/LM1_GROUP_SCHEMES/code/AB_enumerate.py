"""Independent exact finite-ring counts, modular triples, and missed points."""
import json
from pathlib import Path
from itertools import product
from collections import Counter
from math import gcd
from AB_core import *

root=Path(__file__).resolve().parent
rows=[]; misses={}; triples=[]
for n in [2,3,4,5,7,8,9,11,13]:
    units=[x for x in range(n) if gcd(x,n)==1]
    signs=[x for x in units if x*x%n==1]
    matrices=gl(n); special=[x for x in matrices if det(x,n)==1]
    determinant_counts=Counter(det(x,n) for x in matrices)
    r=(0,1,n-1,1); j=(0,1,n-1,0)
    Tr=[x for x in matrices if mul(x,r,n)==mul(r,x,n)]
    Ns=[(x,e) for x in matrices for e in signs if mul(x,j,n)==scale(e,mul(j,x,n),n)]
    count_direct=sum(determinant_counts[det(b,n)] for a in Tr for b,e in Ns
                     if (det(b,n)*pow(det(a,n),-1,n))**2%n==1)
    N3=Counter((c*c+c*d+d*d)%n for c,d in product(range(n),repeat=2))
    N2=Counter((t*t+u*u)%n for t,u in product(range(n),repeat=2))
    x_count=sum(N2[q]*N3[(e*f*q)%n] for e in signs for f in signs for q in units)
    count_formula=x_count*len(special)
    assert count_direct==count_formula
    h0=sum(N2[q]*N3[q] for q in units)
    hdet1=sum(N2[e]*N3[f] for e in signs for f in signs)
    row={'n':n,'SL2':len(special),'T_rho':len(Tr),'N_sigma':len(Ns),
         'mu2':len(signs),'X':x_count,'M':count_direct,
         'M_unsigned':len(special)*h0,'M_det1':len(special)*hdet1,
         'SL_loop_unsigned':n*h0,'SGstar':n*x_count}
    rows.append(row)
    print('COUNT',json.dumps(row,sort_keys=True))
    if n in [2,3,4,8,9]:
        for key,z in [('rho',r),('sigma',j)]:
            target={a for a in special if tr(mul(a,z,n),n)==tr(z,n)}
            regular_target={a for a in target if regular(mul(a,z,n),n)}
            gi={comm(a,z,n) for a in matrices}
            si={comm(a,z,n) for a in special}
            assert gi==regular_target
            v={'target':len(target),'regular_target':len(regular_target),'GL_image':len(gi),'SL_image':len(si),
               'GL_missed':[list(x) for x in sorted(target-gi)],'SL_missed':[list(x) for x in sorted(target-si)]}
            misses[f'{key}_Zmod{n}']=v
            print('COMMUTATOR',key,n,'target',len(target),'GLimage',len(gi),'SLimage',len(si))
            if n in [2,3,4]:print('MISSED',key,n,json.dumps(v,sort_keys=True))
    if n in [2,3,4,5,7,8,9]:
        rhos=[x for x in special if tr(x,n)==1%n]
        sigmas=[x for x in special if tr(x,n)==0]
        actual={(rho,sigma) for rho in rhos for sigma in sigmas
                if tr(mul(rho,sigma,n),n)==2%n and transverse_unipotent(mul(rho,sigma,n),sigma,n)}
        canonical_s=scale(-1,j,n)
        gl_orbit={(conj(g,r,n),conj(g,canonical_s,n)) for g in matrices}
        assert actual==gl_orbit
        remaining=set(actual); reps=[]; sizes=[]
        while remaining:
            a,b=min(remaining)
            orb={(conj(g,a,n),conj(g,b,n)) for g in special}
            assert orb<=remaining
            reps.append([list(a),list(b)]);sizes.append(len(orb));remaining-=orb
        squareclasses=len(units)//len({u*u%n for u in units})
        assert len(reps)==squareclasses
        v={'n':n,'valid_pairs':len(actual),'GL_orbits':1,'SL_orbits':len(reps),'SL_orbit_sizes':sizes,'representatives':reps}
        proj=lambda a:min(scale(z,a,n) for z in units)
        pp={(proj(a),proj(b)) for a,b in actual}
        prem=set(pp); preps=[]
        while prem:
            a,b=min(prem)
            orb={(proj(conj(g,a,n)),proj(conj(g,b,n))) for g in special}
            assert orb<=prem
            preps.append([list(a),list(b)]);prem-=orb
        v.update(projective_pairs=len(pp),projective_SL_orbits=len(preps),projective_SL_representatives=preps)
        triples.append(v)
        print('MODULAR_TRIPLES',json.dumps(v,sort_keys=True))
    if n in [2,3,4]:
        # Direct target enumeration for X (scan370) and explicit inverse.
        actual=set()
        for eta in special:
            if tr(mul(eta,j,n),n):continue
            for mu in range(n):
                zeta=mul(eta,(1,0,(mu-1)%n,1),n)
                if tr(mul(zeta,r,n),n)==1%n:actual.add((zeta,eta,mu))
        param=set()
        for mu in units:
            for lam in range(n):
                b0=(mu,lam,0,1)
                param.add((comm(b0,r,n),comm(b0,j,n),mu))
        assert actual==param and len(actual)==n*len(units)
        print('X PARAMETRIZATION',n,'target',len(actual),'image',len(param),'missed []')

data={'counts':rows,'commutators':misses,'modular_triples':triples}
(root/'AB_enumeration.json').write_text(json.dumps(data,indent=2))
print('ALL ASSERTIONS PASSED')
