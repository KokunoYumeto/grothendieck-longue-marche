#!/usr/bin/env python3
"""Exact remaining PGL2(F11) source map after the relative PGL2(F7) lift.

This independently enumerates the displayed 2,3-generators, their even
restriction, every even conjugacy class and every corresponding normal
closure.  The exclusion of this quotient from the previous completion
and the exact remaining-kernel image are proved in D.42.
"""
from pathlib import Path
from collections import Counter
import json,time

OUT=Path(__file__).resolve().parent;started=time.time();p=11
I=(1,0,0,1)
def canon(a):
    z=pow(next(x for x in a if x),-1,p)
    return tuple(z*x%p for x in a)
def mul(a,b):
    return canon(((a[0]*b[0]+a[1]*b[2])%p,
                  (a[0]*b[1]+a[1]*b[3])%p,
                  (a[2]*b[0]+a[3]*b[2])%p,
                  (a[2]*b[1]+a[3]*b[3])%p))
def inv(a):return canon((a[3],-a[1]%p,-a[2]%p,a[0]))
def det(a):return (a[0]*a[3]-a[1]*a[2])%p
def generated(gens):
    seen={I};todo=[I]
    for a in todo:
        for g in gens:
            b=mul(a,g)
            if b not in seen:seen.add(b);todo.append(b)
    return todo
def order(a):
    b=a;n=1
    while b!=I:n+=1;b=mul(b,a)
    return n
def action(a):
    out=[]
    for z in range(12):
        num,den=(a[0],a[2]) if z==11 else ((a[0]*z+a[1])%p,(a[2]*z+a[3])%p)
        out.append(11 if den==0 else num*pow(den,-1,p)%p)
    return tuple(out)
def parity(perm):return sum(perm[i]>perm[j] for i in range(12) for j in range(i+1,12))%2
s=(1,0,0,10);r=(1,10,1,0)
assert order(s)==2 and order(r)==3
G=generated([s,r]);assert len(G)==1320
squares={a*a%p for a in range(1,p)}
L=[a for a in G if det(a) in squares];assert len(L)==660
srs=mul(mul(s,r),s)
assert set(generated([r,srs]))==set(L)
assert len({action(a) for a in G})==1320
assert all(parity(action(a))==int(det(a) not in squares) for a in G)
centralizer=[a for a in G if all(mul(a,b)==mul(b,a) for b in [r,srs])]
assert centralizer==[I]
remaining=set(L);classes=[]
while remaining:
    a=min(remaining)
    cc={mul(mul(g,a),inv(g)) for g in L}
    assert cc<=remaining;remaining-=cc
    normal=generated(sorted(cc))
    assert len(normal)==(1 if a==I else 660)
    classes.append({'representative':list(a),'class_size':len(cc),'normal_closure_order':len(normal)})
assert sum(c['class_size'] for c in classes)==660
t=mul(s,r);x=inv(mul(t,t))
assert order(t)==10 and order(x)==5
summary={
    'PGL2F11_generators':{'s':list(s),'r':list(r)},
    'PGL2F11_order':len(G),'PSL2F11_order':len(L),
    'source_s_order':order(s),'source_r_order':order(r),
    'source_t_order':order(t),'source_x_order':order(x),
    'even_source_restriction_generates_PSL2F11':True,
    'centralizer_in_PGL2F11_of_PSL2F11_order':len(centralizer),
    'faithful_degree12_action_checked':True,
    'permutation_sign_equals_determinant_square_class_checked':True,
    'PSL2F11_conjugacy_and_normal_closure_certificate':classes,
    'PGL2F11_has_no_PGL2F7_quotient_by_order':1320%336!=0,
    'remaining_source_kernel_image':'PSL2(F11)',
    'scope':'Actual marked finite map and all finite simplicity claims. The exact residual image is proved in D42; it is not a nonlifting assertion for the retained CM pair.',
    'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_relative_kernel.json').write_text(json.dumps({'summary':summary,'PGL2F11_elements':G},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
