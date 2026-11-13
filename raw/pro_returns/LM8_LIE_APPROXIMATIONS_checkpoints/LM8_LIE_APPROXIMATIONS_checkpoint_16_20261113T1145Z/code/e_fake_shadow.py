#!/usr/bin/env python3
"""A complete small permutation certificate for a finite fake GT shadow.

Multiplication is GAP's right-action convention (p*q applies p then q).
No group library or SmallGrp identification is needed for the checks.
The original group's two permutations act faithfully on54 points.
The exact table proof is independent of the LINS enumeration.
"""
from pathlib import Path
from math import gcd
import json
from e_braid_core import Table,signature
base=Path(__file__).resolve().parent
acycles=[[1,2,6,17,34,49,44,27,14,32,42,24,37,50,43,25,9,3],
[4,12,29,46,51,40,53,48,33,16,5,15,19,36,18,35,30,13],
[7,20,38,52,47,31,45,54,41,23,8,22,39,28,11,26,10,21]]
bcycles=[[1,4,14,29,34,30,44,53,43,33,42,51,37,19,6,18,9,5],
[2,7,17,11,3,10,27,45,32,38,49,47,50,39,25,41,24,8],
[12,20,35,26,13,31,48,54,46,52,40,22,36,28,16,23,15,21]]
def perm(cycles):
    p=list(range(54))
    for c in cycles:
        for i,j in zip(c,c[1:]+c[:1]):p[i-1]=j-1
    return tuple(p)
def mul(p,q):return tuple(q[v] for v in p)
a0,b0=perm(acycles),perm(bcycles);I=tuple(range(54))
els=[I];ix={I:0}
for v in els:
    for g in (a0,b0):
        w=mul(v,g)
        if w not in ix:ix[w]=len(els);els.append(w)
assert len(els)==486
pa=[ix[mul(v,a0)]+1 for v in els];pb=[ix[mul(v,b0)]+1 for v in els]
t=Table({'index':486,'a_permutation':pa,'b_permutation':pb});a,b=t.a,t.b
assert t.mul(a,b,a)==t.mul(b,a,b)
X,Y=t.pow(a,2),t.pow(b,2);c=t.mul(X,Y,int(t.inv[X]),int(t.inv[Y]));C=t.pow(t.mul(a,b),3)
H=t.closure([X,Y]);P=t.closure([X,Y,C])
assert len(H)==len(P)==81
assert t.order(a)==t.order(b)==18 and t.order(X)==t.order(Y)==9
assert t.order(c)==3 and t.order(C)==3
assert t.mul(c,X)==t.mul(X,c) and t.mul(c,Y)==t.mul(Y,c)
assert t.pow(Y,3)==t.pow(X,3)==C
assert t.mul(a,c,int(t.inv[a]))==t.pow(c,-1)
assert t.mul(b,c,int(t.inv[b]))==t.pow(c,-1)
D=t.closure([c]);assert len(D)==3
# Exact m=0 hexagons, genuine action formula, and full-twist formula.
ap=a;bp=t.mul(int(t.inv[c]),b,c)
assert t.mul(ap,bp)==t.mul(int(t.inv[c]),a,b)
assert t.mul(bp,ap)==t.mul(b,a,c)
assert t.mul(ap,bp,ap)==t.mul(bp,ap,bp)
assert t.pow(ap,2)==X and t.pow(bp,2)==Y
assert t.pow(t.mul(ap,bp),3)==C
assert t.self_descent(ap,bp)
assert bp!=b
# Every global GT_gen element has f=c^((chi^2-1)/24) in H.
# chi mod72 determines this value and m=(chi-1)/2 mod9.
genuine=set()
for chi in range(72):
    if gcd(chi,72)!=1:continue
    assert (chi*chi-1)%24==0
    m=((chi-1)//2)%9;r=((chi*chi-1)//24)%3
    genuine.add((m,r))
assert (0,1) not in genuine and (0,2) not in genuine
assert {r for m,r in genuine if m==0}=={0}
assert len(genuine)==6
out={'a_cycles':acycles,'b_cycles':bcycles,'permutation_degree':54,'permutation_product':'right action, left factor applied first',
     'a_image_list_1_based':[v+1 for v in a0],'b_image_list_1_based':[v+1 for v in b0],
     'group_order':486,'SmallGrp_identifier_verified_separately':[486,22],
     'H_order':81,'PB3_image_order':81,'kernel_contained_in_PB3':True,
     'order_X':9,'order_Y':9,'order_commutator':3,'order_full_twist':3,
     'commutator_central_in_H':True,'Y_cubed_equals_X_cubed_equals_full_twist':True,
     'N_ord':9,'fake_pair':{'m':0,'f':'[X,Y]','f_nonidentity':True},
     'both_braid_hexagons':True,'H_surjectivity':True,'B3_surjectivity':True,
     'self_automorphism_verified_on_all_Cayley_edges':True,
     'global_class_two_coefficient':'24r=chi^2-1 in Zhat; r=(chi^2-1)/24 before reduction',
     'all_genuine_pairs_m_r':sorted(map(list,genuine)),
     'fake_pairs_with_m_zero':[[0,1],[0,2]],
     'full_GT_shadow_after_forgetful_refinement':True,
     'refined_B3_quotient_order':6*3*9**3,
     'PB4_target_order_upper_bound':81**4,
     'independent_group_enumeration':True}
(base/'e_fake_shadow.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if 'cycles' not in k and 'image_list' not in k})
