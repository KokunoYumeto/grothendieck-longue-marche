#!/usr/bin/env python3
"""Exact marked PGL2(F7) kernel test after all perfect and symmetric quotients."""
from pathlib import Path
from collections import deque
from itertools import product
import hashlib,json,time

OUT=Path(__file__).resolve().parent
started=time.time()
p=7
I=(1,0,0,1)
def mm(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%p
                 for i in range(2) for j in range(2))
def canon(a):
    c=pow(next(x for x in a if x),-1,p)
    return tuple(c*x%p for x in a)
def mul(a,b):
    return canon(mm(a,b))
def inv(a):
    d=pow((a[0]*a[3]-a[1]*a[2])%p,-1,p)
    return canon(tuple(d*x%p for x in (a[3],-a[1],-a[2],a[0])))
def det(a):
    return (a[0]*a[3]-a[1]*a[2])%p
def pw(a,n):
    z=I
    for _ in range(n):z=mul(z,a)
    return z
def generated(gens):
    seen={I};todo=[I]
    for a in todo:
        for b in gens:
            c=mul(a,b)
            if c not in seen:seen.add(c);todo.append(c)
    return todo
def order(a):
    z=I
    for k in range(1,337):
        z=mul(z,a)
        if z==I:return k
    raise AssertionError
def action(a):
    out=[]
    for z in range(8):
        numerator,denominator=(a[0],a[2]) if z==7 else (
            (a[0]*z+a[1])%p,(a[2]*z+a[3])%p)
        out.append(7 if denominator==0 else numerator*pow(denominator,-1,p)%p)
    return out

s=(1,0,0,6)
r=(1,6,1,0)
assert pw(s,2)==pw(r,3)==I
G=generated([s,r])
assert len(G)==336
squares={a*a%p for a in range(1,p)}
L=[a for a in G if det(a) in squares]
assert len(L)==168 and det(s) not in squares and det(r) in squares
assert len({tuple(action(a)) for a in G})==336

# The restriction of sigma to B_even=<r,srs> is onto PSL2(F7).
rsr=mul(mul(s,r),s)
even=generated([r,rsr])
assert set(even)==set(L)
centralizer=[a for a in G if all(mul(a,b)==mul(b,a) for b in (r,rsr))]
assert centralizer==[I]

# Exhaust all conjugacy classes of L and the normal closure of each
# nonidentity representative.  This is a complete simplicity certificate.
remaining=set(L);classes=[]
while remaining:
    a=min(remaining)
    conjugates={mul(mul(g,a),inv(g)) for g in L}
    assert conjugates<=remaining
    remaining-=conjugates
    normal=generated(sorted(conjugates))
    if a!=I:assert len(normal)==168
    else:assert len(normal)==1
    classes.append({'representative':list(a),'class_size':len(conjugates),
                    'normal_closure_order':len(normal)})
assert sum(c['class_size'] for c in classes)==168

# Exact comparison with the existing marked good-prime congruence map.
S=canon((0,1,6,0))
R=canon((0,6,1,6))
assert pw(S,2)==pw(R,3)==I
canonical=generated([S,R])
assert set(canonical)==set(L)
SRs=mul(mul(S,R),S)
assert set(generated([R,SRs]))==set(L)

def pair_group(gens):
    identity=(I,I);seen={identity};todo=[identity]
    for a in todo:
        for b in gens:
            c=(mul(a[0],b[0]),mul(a[1],b[1]))
            if c not in seen:seen.add(c);todo.append(c)
    return todo
whole_pair=pair_group([(S,s),(R,r)])
even_pair=pair_group([(R,r),(SRs,rsr)])
assert len(whole_pair)==168*336
assert len(even_pair)==168**2
assert {b for a,b in whole_pair if a==I}==set(G)
assert {b for a,b in even_pair if a==I}==set(L)

t=mul(s,r);x=inv(mul(t,t))
assert order(t)==8 and order(x)==4
permutation_s=action(s);permutation_r=action(r)
def parity(a):
    return sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2
for a in G:
    assert parity(action(a))==int(det(a) not in squares)

summary={
 'PGL2F7_generators':{'s':list(s),'r':list(r)},
 'PGL2F7_order':len(G),'PSL2F7_order':len(L),
 'source_s_order':order(s),'source_r_order':order(r),
 'source_t_order':order(t),'source_x_order':order(x),
 'P1_action_s':permutation_s,'P1_action_r':permutation_r,
 'faithful_degree8_action_checked':True,
 'permutation_sign_equals_determinant_square_class_checked':True,
 'even_source_restriction_generates_PSL2F7':True,
 'centralizer_in_PGL2F7_of_PSL2F7_order':len(centralizer),
 'PSL2F7_conjugacy_and_normal_closure_certificate':classes,
 'actual_full_symmetric_quotient_of_degree8':False,
 'canonical_congruence_pair_order':len(whole_pair),
 'even_source_pair_order':len(even_pair),
 'canonical_congruence_kernel_surjects_PGL2F7':True,
 'even_canonical_congruence_kernel_surjects_PSL2F7':True,
 'remaining_kernel_after_all_perfect_and_symmetric_coordinates_image':'PSL2(F7)',
 'scope':'The exact finite marked maps and simplicity claims are checked here. The full simultaneous source image and its remaining-kernel map are proved in D41; full profinite realization remains unresolved.',
 'elapsed_seconds':round(time.time()-started,3),
}
certificate={'summary':summary,'PGL2F7_elements':[list(a) for a in G],
 'canonical_PSL2F7_s':list(S),'canonical_PSL2F7_r':list(R),
 'PSL2F7_elements':[list(a) for a in L],
 'whole_pair_sha256':hashlib.sha256(bytes(v for a,b in whole_pair for c in (a,b) for v in c)).hexdigest(),
 'even_pair_sha256':hashlib.sha256(bytes(v for a,b in even_pair for c in (a,b) for v in c)).hexdigest()}
(OUT/'d_cm_symmetric_completion.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
