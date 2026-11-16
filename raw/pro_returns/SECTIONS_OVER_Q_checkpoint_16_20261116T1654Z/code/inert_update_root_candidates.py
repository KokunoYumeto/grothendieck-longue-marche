#!/usr/bin/env python3
"""Exact finite-field tests for inert auxiliary primes5 and11."""
from pathlib import Path
import json
w=Path(__file__).resolve().parents[1]
results=[]
for q,ga,gb in [(5,2,-1),(11,2,1)]:
    roots=[r for r in range(q) if pow(r,3,q)==3%q]
    assert len(roots)==1
    r=roots[0]
    assert ga**3+3*gb**3==q
    assert (ga+gb*r)%q==0
    def mul(x,y):
        b=x[0]*y[1]+x[1]*y[0]
        c=x[1]*y[1]
        return ((x[0]*y[0]-r*r*c)%q,(b-r*c)%q)
    def pw(x,n):
        o=(1,0)
        while n:
            if n&1:o=mul(o,x)
            x=mul(x,x);n//=2
        return o
    alpha=(0,1)
    assert pw(alpha,3)==(3%q,0)
    zet=pw(alpha,(q*q-1)//3)
    assert zet!=(1,0) and pw(zet,3)==(1,0)
    def char(x):
        z=pw(x,(q*q-1)//3)
        return next(j for j in range(3) if pw(zet,j)==z)
    one_minus=(1,q-1)
    a2=mul(alpha,alpha)
    unit=((a2[0]-2)%q,a2[1])
    row={'q':q,'gamma_coefficients':[ga,gb,0],'linear_root':r,
         'quadratic_polynomial':[1,r,r*r%q],'alpha_character':char(alpha),
         'one_minus_alpha_character':char(one_minus),'U_character':char(unit),
         'old_cover_24th_roots_minus_two':[x for x in range(1,q) if pow(x,24,q)==(-2)%q],
         'successful_choices':[]}
    for t in range(3):
        b0=mul(one_minus,pw(unit,t))
        for e in (8,16):
            symbol=(e*char(b0)-char(alpha))%3
            if symbol==0:row['successful_choices'].append({'U_exponent':t,'q_exponent_in_z':e})
    results.append(row)
(w/'code/inert_update_root_candidates_data.json').write_text(json.dumps(results,indent=2)+'\n')
out=json.dumps(results,indent=2)+'\nAll finite-field identities checked. This program does not construct a compatible global norm family.\n'
(w/'code/inert_update_root_candidates_output.txt').write_text(out)
print(out,end='')
