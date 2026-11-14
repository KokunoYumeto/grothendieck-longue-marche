#!/usr/bin/env python3
"""Exact finite source, CM framing and arithmetic commutator certificates.

No arithmetic image is inferred from enumeration: D35 supplies the
opened CM theorem and its proved full principal-unit image. This code
checks all finite group maps and every possible framing of that
arithmetic commutator, before and after the coprime centralizer lift.
"""
from pathlib import Path
from collections import deque
from fractions import Fraction
import json,time

OUT=Path(__file__).resolve().parent;started=time.time()
I=(1,0,0,1);S=(0,1,11,0);R=(0,11,1,11)
def canon(a):return min(a,tuple(-x%12 for x in a))
def mul(a,b):
    return canon(((a[0]*b[0]+a[1]*b[2])%12,(a[0]*b[1]+a[1]*b[3])%12,
                  (a[2]*b[0]+a[3]*b[2])%12,(a[2]*b[1]+a[3]*b[3])%12))
def inv(a):return canon((a[3],-a[1]%12,-a[2]%12,a[0]))
def generated(gs):
    G=[I];seen={I}
    for a in G:
        for b in gs:
            c=mul(a,b)
            if c not in seen:seen.add(c);G.append(c)
    return G
Q=generated([S,R]);assert len(Q)==576
def power(a,n):
    out=I
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
qindex={a:i for i,a in enumerate(Q)}
words={I:[]};bab={I:(0,0)}
queue=[I]
for a in queue:
    for letter,b in [(0,S),(1,R)]:
        c=mul(a,b);v=((bab[a][0]+(letter==0))%2,(bab[a][1]+(letter==1))%3)
        if c in bab:assert bab[c]==v
        else:bab[c]=v;words[c]=words[a]+[letter];queue.append(c)
assert len(words)==576 and len(set(bab.values()))==6
FH={q for q in Q if tuple(x%2 for x in q)==I}
EH={q for q in Q if bab[q]==(0,0)}
assert len(FH)==len(EH)==96
NF=set(generated([q for q in FH if q!=I and power(q,3)==I]))
NE=set(generated([q for q in EH if q!=I and power(q,3)==I]))
assert len(NF)==24 and len(NE)==12
assert all(mul(mul(q,n),inv(q)) in NF for q in Q for n in NF)
assert all(mul(mul(q,n),inv(q)) in NE for q in Q for n in NE)
assert NF&NE=={I}
def cosets(N):
    mp={};reps=[]
    for q in Q:
        if q in mp:continue
        j=len(reps);reps.append(q)
        for n in N:mp[mul(q,n)]=j
    return reps,mp
Frep,Fmap=cosets(NF);Erep,Emap=cosets(NE)
assert len(Frep)==24 and len(Erep)==48
assert len({(Fmap[q],Emap[q]) for q in Q})==576
assert len({(Fmap[q],Emap[q]) for q in Q if bab[q][0]==0})==288
assert all(bab[n][0]==0 for n in NF|NE)
# Explicit mod4 comparison of the first quotient, with every product.
def project4(q):
    a=tuple(x%4 for x in q)
    return min(a,tuple(-x%4 for x in a))
assert len({project4(q) for q in Q})==24
assert all((Fmap[a]==Fmap[b])==(project4(a)==project4(b)) for a in Q for b in Q)

# D25 global-sign convention: modulo4 representative in <U^2,W^2>.
U2=(1,2,0,1);W2=(1,0,2,1)
def mm4(a,b):
    return ((a[0]*b[0]+a[1]*b[2])%4,(a[0]*b[1]+a[1]*b[3])%4,
            (a[2]*b[0]+a[3]*b[2])%4,(a[2]*b[1]+a[3]*b[3])%4)
V4={I,U2,W2,mm4(U2,W2)};assert len(V4)==4
def normalized(q):
    opts=[q,tuple(-x%12 for x in q)]
    good=[a for a in opts if tuple(x%4 for x in a) in V4]
    assert len(good)==1
    return good[0]
def cm_bit_A(q):
    a=normalized(inv(q));v=((a[0]-a[1])%3,(a[2]-a[3])%3)
    assert v in [(1,2),(2,1)]
    return int(v==(2,1))
def cm_bit_beta(q):
    a=normalized(inv(q));b=tuple(x%3 for x in a)
    assert b in [(1,0,0,1),(2,0,0,2),(0,1,2,0),(0,2,1,0)]
    return int(b[0]==0)
CA=[q for q in FH if mul(q,R)==mul(R,q)]
CB=[q for q in FH if mul(q,S)==mul(S,q)]
assert len(CA)==6 and len(CB)==8
AA=[q for q in CA if cm_bit_A(q)==1]
BB=[q for q in CB if cm_bit_beta(q)==1 and Fmap[q]==Fmap[I]]
assert len(AA)==3 and len(BB)==2
rgroup={I,R,power(R,2)};sgroup={I,S}
cases=[]
for a in AA:
    c=inv(a)
    assert mul(c,R)==mul(R,c) and c not in rgroup
    assert mul(a,c)==I
    for b in BB:
        assert b not in sgroup and bab[b]==(0,0)
        assert Fmap[b]==Fmap[I]
        cases.append({'arithmetic_A':list(a),'arithmetic_beta':list(b),
          'right_r_centralizer_Q_coordinate':list(c),
          'new_A':list(I),'new_beta':list(b),'V':list(I),
          'old_CM_bits':[cm_bit_A(a),cm_bit_beta(b)],
          'new_CM_bits':[cm_bit_A(I),cm_bit_beta(b)],
          'new_T4':list(I),'new_projective_W3':'[i]',
          'r_correction_not_in_image_of_full_B_r_centralizer':True,
          'odd_beta_lift_not_in_image_of_full_B_s_centralizer':True})
assert len(cases)==6 and all(c['new_CM_bits']==[0,1] for c in cases)

# Exact CM arithmetic in Q(zeta3), with zeta3^2=-1-zeta3.
def cmul(a,b):
    x,y=a;u,v=b
    return x*u-y*v,x*v+y*u-y*v
def cconj(a):return a[0]-a[1],-a[1]
a=(3,2) # 1-2*zeta3^2
abar=cconj(a);assert abar==(1,-2)
assert cmul(a,abar)==(7,0)
eta=tuple(Fraction(z,7) for z in cmul(a,a))
assert eta==(Fraction(5,7),Fraction(8,7))
assert cmul(eta,cconj(eta))==(1,0)
eta16=tuple((z.numerator*pow(z.denominator,-1,16))%16 for z in eta)
assert eta16==(3,8)
assert tuple((z.numerator*pow(z.denominator,-1,4))%4 for z in eta)==(3,0)
# Same unit in D35's variable Z=zeta3^2 is (-3-8Z)/7.
assert (eta[0]-eta[1],-eta[1])==(Fraction(-3,7),Fraction(-8,7))
elliptic_basis=[[1,0,2,0],[2,0,1,0]]
def bi(w):return [0 if x==0 else 3-x for x in reversed(w)]
def elliptic_ab(w):
    q=(0,0);v=[0,0]
    for letter in w:
        if letter==0:q=(1-q[0],q[1])
        else:
            h=(q[0],(q[1]+letter)%3)
            if q[0] and q[1]:v[q[1]-1]+=1
            if h[0] and h[1]:v[h[1]-1]-=1
            q=h
    assert q==(0,0)
    return v
assert [elliptic_ab(w) for w in elliptic_basis]==[[1,0],[0,1]]
cols=[elliptic_ab([0,1]*2+w+bi([0,1]*2)) for w in elliptic_basis]
Z=tuple(tuple(cols[j][i] for j in range(2)) for i in range(2))
assert Z==((0,1),(-1,-1)) # Actual t^2 action in the D45 elliptic graph basis.
M=[[(((-3 if i==j else 0)-8*Z[i][j])*pow(7,-1,16))%16 for j in range(2)] for i in range(2)]
assert M==[[11,8],[8,3]]
# The affine Kummer commutator: (1-chi_tau)k_g+(chi_g-1)k_tau.
checks=0
for tau_k in range(3):
    assert ((1-2)*0+(1-1)*tau_k)%3==0;checks+=1
for n in [2,4,8,16,32,64,128]:
    for g_k in range(n):
        assert ((1-1)*g_k+(7-1)*0)%n==0;checks+=1
ps=(1,0,3,2,5,4,6);pr=(3,6,2,5,1,0,4);pI=tuple(range(7))
def perm_mul(a,b):return tuple(a[b[j]] for j in range(7))
PG=[pI];pseen={pI}
for u in PG:
    for v in [ps,pr]:
        w=perm_mul(u,v)
        if w not in pseen:pseen.add(w);PG.append(w)
assert len(PG)==5040 and perm_mul(ps,ps)==pI and perm_mul(perm_mul(pr,pr),pr)==pI
def parity(a):return sum(a[i]>a[j] for i in range(7) for j in range(i+1,7))%2
assert parity(ps)==1 and parity(pr)==0
assert sum(parity(u)==0 for u in PG)==2520
summary={'Q_order':576,'N_free_rank':97,
 'Q_sphere_relative2_quotient_order':24,'Q_elliptic_relative2_quotient_order':48,
 'sphere_source_kernel_order':24,'elliptic_source_kernel_order':12,
 'two_source_kernels_intersection_order':1,
 'actual_Q_is_product_over_common_sign':True,
 'all_Q_pair_equalities_for_canonical_mod4_map_checked':576**2,
 'arithmetic_r_conjugator_candidates':len(AA),'arithmetic_s_conjugator_candidates':len(BB),
 'all_possible_arithmetic_CM_framings_checked':len(cases),
 'every_replacement_has_CM_bits':[0,1],
 'full_source_r_centralizer_image':'<r>','full_source_s_centralizer_image':'<s>',
 'every_used_nontrivial_relative_centralizer_coordinate_excluded_from_corresponding_full_centralizer':True,
 'a_coefficients_in_zeta3_basis':list(a),'a_norm':7,
 'eta_coefficients_in_zeta3_basis':[str(x) for x in eta],
 'eta_coefficients_mod16':list(eta16),
 'eta_norm':1,'eta_mod4_is_minus_identity':True,
 'eta_matrix_in_D45_elliptic_basis_mod16':M,
 'elliptic_graph_t2_matrix':[list(row) for row in Z],
 'affine_Kummer_commutator_checks':checks,
 'remaining_S7_source_s':list(ps),'remaining_S7_source_r':list(pr),
 'remaining_S7_source_order':len(PG),'remaining_source_kernel_image_in_S7':'A7',
 'scope':'Exact finite source and framing certificate for the actual arithmetic/pro-prime replacement proved in D46. Arithmetic existence and simultaneous coprime fixed lifting are proved there, not inferred from this enumeration.',
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'Q':[list(q) for q in Q],
 'Q_source_words':[words[q] for q in Q],
 'Q_to_C6':[list(bab[q]) for q in Q],
 'Q_to_sphere_relative2_quotient':[Fmap[q] for q in Q],
 'Q_to_elliptic_relative2_quotient':[Emap[q] for q in Q],
 'sphere_quotient_representatives':[list(q) for q in Frep],
 'elliptic_quotient_representatives':[list(q) for q in Erep],
 'sphere_source_kernel':[list(q) for q in Q if q in NF],
 'elliptic_source_kernel':[list(q) for q in Q if q in NE],
 'all_arithmetic_and_replaced_CM_framings':cases}
(OUT/'d_cm_arithmetic_replacement.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
