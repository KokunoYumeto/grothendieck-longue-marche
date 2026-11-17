#!/usr/bin/env python3
"""Exact five-point retraction and its signed/projective kernel marking.

No finite-shadow lift is inferred.  This certifies the literal maps that
retain the rank-97 ternary modular homology detector in the fifth insertion.
"""
from pathlib import Path
import json

def inverse(w):
    return tuple(-j for j in reversed(w))

def reduce(w):
    out=[]
    for j in w:
        if out and out[-1]==-j:
            out.pop()
        else:
            out.append(j)
    return tuple(out)

def subst(w,images):
    return reduce(j for z in w for j in
                  (images[z-1] if z>0 else inverse(images[-z-1])))

def comm(i,j):
    return (-j,-i,j,i)

relations=[]
for left,right in [
    ((1,3,-1),(-5,3,5)),
    ((1,4,-1),comm(3,5)+(4,)+inverse(comm(3,5))),
    ((1,5,-1),comm(3,5)+(5,)),
    ((2,3,-2),(3,)),
    ((2,4,-2),(-5,4,5)),
    ((2,5,-2),comm(4,5)+(5,))]:
    relations.append(left+inverse(right))

pi=((-1,-2),(2,),(2,),(-2,-1),(1,))
rel_images=[subst(w,pi) for w in relations]
assert rel_images==[()]*6
x12=(-5,-4,-3,-2,-1)
assert subst(x12,pi)==(1,)
assert subst((2,),pi)==(2,)
print('PASS all six five-point defining relators vanish under the literal free retraction')
print('PASS fifth insertion (A12,A23) retracts exactly to (x,y)')

I=(1,0,0,1)
def mul(a,b,m=12):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m
                 for i in range(2) for j in range(2))
def inv(a,m=12):
    return (a[3]%m,-a[1]%m,-a[2]%m,a[0]%m)
def word(w,images,m=12):
    ans=I
    for j in w:
        ans=mul(ans,images[j-1] if j>0 else inv(images[-j-1],m),m)
    return ans
def closure(images,m=12):
    ans=[I]; seen={I:0}
    for a in ans:
        for b in images:
            c=mul(a,b,m)
            if c not in seen:
                seen[c]=len(ans);ans.append(c)
    return ans
U=(1,1,0,1); L=(1,0,11,1)
def band(i,j):
    front=tuple(range(j-1,i,-1))
    return front+(i,i)+inverse(front)
target=[word(band(i,j),(U,L,U)) for i,j in
        ((1,3),(2,3),(1,4),(2,4),(3,4))]
theta=(mul(U,U),mul(L,L))
epsilon=(1,0,0,1,0)
minusI=(11,0,0,11)
comparisons=[]
for i,g in enumerate(target):
    right=word(pi[i],theta)
    if epsilon[i]:right=mul(minusI,right)
    assert g==right
    comparisons.append({'generator':i+1,'q192':g,'signed_retraction':right,
                        'epsilon':epsilon[i]})
assert word(x12,target)==theta[0]
assert target[1]==theta[1]
theta_image=closure(theta)
target_image=closure(target)
theta_mod4=sorted({tuple(z%4 for z in g) for g in theta_image})
assert len(theta_image)==96
assert len(target_image)==192
assert len(theta_mod4)==4
assert (3,0,0,3) not in theta_mod4
assert minusI not in theta_image
assert {mul(minusI,g) for g in theta_image}.isdisjoint(theta_image)
assert set(target_image)==set(theta_image)|{mul(minusI,g) for g in theta_image}
assert all(word(rel,target)==I for rel in relations)
print('PASS q192(g)=(-I)^epsilon(g) theta12(pi(g)) on all five marked generators')
print('PASS signed free image order96; modulo-four image V4 excludes -I')
print('PASS target image is the exact disjoint union theta(F) and -theta(F), order192')

# B=C2*C3 projective marking: x=(sr)^-2, y=sxs.
S=(0,1,11,0);R=(0,11,1,11)
bx=(-2,1,-2,1);by=(1,)+bx+(1,)
def projective(g):return min(g,tuple(-z%12 for z in g))
assert projective(word(bx,(S,R)))==projective(theta[0])
assert projective(word(by,(S,R)))==projective(theta[1])
assert projective(mul(S,S))==projective(I)
assert projective(mul(mul(R,R),R))==projective(I)
B_image=closure((S,R))
assert len({projective(g) for g in B_image})==576
assert len({projective(g) for g in theta_image})==96
print('PASS exact B projective marking; kernel index576 in B, index96 in F, free rank97')

out={
 'scope':'Exact retraction and homology quotient maps; no claim excluding every parity-one GT record',
 'free_retraction':pi,'fivepoint_relators':relations,'relator_images':rel_images,
 'fifth_insertion':[x12,(2,)],'theta_generators':theta,
 'generator_matrix_comparisons':comparisons,
 'signed_free_image_order':96,'target_image_order':192,
 'theta_mod4':theta_mod4,'minus_identity_absent':True,
 'B_projective_order':576,'kernel_free_rank':97,
 'kernel_map':'pi(N) subset K, iota5(K) subset N, pi*iota5=id_K',
 'quotient_map':'Gamma05/(Nprime*N^3) -> F/(Kprime*K^3)',
 'section':'F/(Kprime*K^3) -> Gamma05/(Nprime*N^3)',
 'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual quotient retraction retains the entire rank-97 ternary modular source')
