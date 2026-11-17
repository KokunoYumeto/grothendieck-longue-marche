#!/usr/bin/env python3
"""Exact universal word identities for the actual ordinary star/cross rewrite."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
names = {1:"a",2:"A1",3:"k",4:"K1",5:"j0",6:"j1",7:"h"}
involutions = {5,6}

def red(word):
    out=[]
    for letter in word:
        letter=abs(letter) if abs(letter) in involutions else letter
        if out and (out[-1]==-letter or (abs(letter) in involutions and out[-1]==letter)):
            out.pop()
        else:
            out.append(letter)
    return out

def mul(*words):
    return red([x for w in words for x in w])

def inv(word):
    return red([-x for x in reversed(word)])

def conj(word, by):
    return mul(by,word,inv(by))

def comm(a,b):
    return mul(a,b,inv(a),inv(b))

def sub(word, values):
    return mul(*[values[x] if x>0 else inv(values[-x]) for x in word])

a,A,k,K,j,J,h=([i] for i in range(1,8))
t0=mul(j,a,inv(A),J)
j0p=conj(j,inv(a))
j1p=conj(J,inv(A))
g=mul(j0p,j1p)
bar={1:A,2:a,3:K,4:k,5:J,6:j,7:h}
r0=mul(t0,K,inv(t0),inv(k))
rstar=mul(g,K,inv(g),inv(k))
alpha=comm(inv(A),K)
beta=comm(inv(a),inv(k))
difference=mul(r0,inv(conj(rstar,a)))
factorization=mul(conj(alpha,mul(a,g)),conj(beta,mul(a,g,K,inv(g))))
with_h={i:[i] for i in names}
with_h[4]=conj(k,h)
checks={
    'selected_cone_square': mul(t0,sub(t0,bar))==[],
    'exact_adjusted_conjugator': t0==mul(a,g,inv(A)),
    'other_cross_sheet': sub(r0,bar)==conj(inv(r0),inv(t0)),
    'commuting_relator_factorization': difference==factorization,
    'regional_h_substitution': sub(rstar,with_h)==comm(mul(g,h),k),
}
assert all(checks.values()), checks
output={'scope':'Universal exact free-product checks; no final quotient normal-form assertion.',
        'basis':names,'involutions':sorted(involutions),
        't0':t0,'j0_prime':j0p,'j1_prime':j1p,'g':g,
        'r0':r0,'rstar':rstar,'alpha':alpha,'beta':beta,
        'difference':difference,'factorization':factorization,
        'checks':checks}
(ROOT/'work_A/ordinary_star_cross25.json').write_text(json.dumps(output,indent=2)+'\n')
for key,value in checks.items():
    print('PASS',key)
print('Scope: all actual regional/neck relations remain; final centralizer unresolved.')
