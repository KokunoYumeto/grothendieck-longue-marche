#!/usr/bin/env python3
"""Exact all-Fermat base lattice and normalized closed-source comparisons."""
from pathlib import Path
from math import gcd
import argparse,json,time

ap=argparse.ArgumentParser()
ap.add_argument('--source-code',type=Path,default=Path(__file__).resolve().parents[2]/'LM7_FERMAT_TOWER'/'code')
args=ap.parse_args();OUT=Path(__file__).resolve().parent;started=time.time()
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
def power(a,n):
    if n<0:a=inv(a);n=-n
    out=I
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
Q=generated([S,R]);assert len(Q)==576
T=mul(S,R);X=inv(mul(T,T));Y=mul(mul(S,X),S)
H=generated([X,Y]);assert len(H)==96
comm=mul(mul(mul(X,Y),inv(X)),inv(Y))
Hp=set(generated([mul(mul(q,comm),inv(q)) for q in H]))
assert len(Hp)==8
assert all(mul(mul(a,b),mul(inv(a),inv(b))) in Hp for a in H for b in H)
assert all(mul(mul(q,h),inv(q)) in Hp for q in Q for h in Hp)
q8_r_fixed=[h for h in Hp if mul(h,R)==mul(R,h)]
assert set(q8_r_fixed)=={I,(5,0,0,5)}
assert all(power(h,4)==I for h in Hp)
assert sum(power(h,2)==I for h in Hp)==2
# The full source H image has abelianization C2 x C6.
relations=[]
for a in range(12):
    for b in range(12):
        value=mul(power(X,a),power(Y,b))
        expected=(a%2==0 and b%2==0 and (a+b)%3==0)
        assert (value in Hp)==expected
        if expected:relations.append([a,b])
assert len(relations)==12
Lambda=[[2,0],[-2,6]] # columns (2,-2),(0,6), determinant12
table=[]
for m in range(1,61):
    seen={(0,0)};queue=[(0,0)]
    for a,b in queue:
        for u,v in [(2,-2),(0,6)]:
            c=((a+u)%m,(b+v)%m)
            if c not in seen:seen.add(c);queue.append(c)
    common=gcd(2,m)**2*gcd(3,m)
    assert len(seen)==m*m//common
    order=576*len(seen);rank=1+order//6
    table.append({'m':m,'common_F_abelian_quotient_order':common,
                  'N_over_Lm_order':len(seen),'H_m_order':order,'L_m_free_rank':rank})
assert table[3]['H_m_order']==2304 and table[3]['L_m_free_rank']==385
assert table[11]['H_m_order']==6912 and table[11]['L_m_free_rank']==1153

# Actual r action in the original sphere graph; f1=x and f2=y^-1.
B=json.loads((args.source_code/'d_cm_solvable_even_boundary.json').read_text())
G=[tuple(q) for q in B['sphere_quotient_states']];ix={q:i for i,q in enumerate(G)}
pi=(0,1,2);ps=(1,0,2);pr=(1,2,0)
pm=lambda a,b:tuple(a[b[i]] for i in range(3))
pr2=pm(pr,pr);ch={j:i for i,j in enumerate(B['sphere_cycle_chords'])}
def ab(w):
    q=pi;v=[0,0]
    for a in w:
        if a==0:q=pm(q,ps)
        else:
            h=pm(q,pr if a==1 else pr2)
            if ix[q] in ch:v[ch[ix[q]]]+=1
            if ix[h] in ch:v[ch[ix[h]]]-=1
            q=h
    assert q==pi
    return v
fb=B['sphere_F_basis_B_words']
assert [ab(w) for w in fb]==[[1,0],[0,1]]
cols=[ab([1]+w+[2]) for w in fb]
MR=[[cols[j][i] for j in range(2)] for i in range(2)]
one_minus=[[int(i==j)-MR[i][j] for j in range(2)] for i in range(2)]
det=one_minus[0][0]*one_minus[1][1]-one_minus[0][1]*one_minus[1][0]
assert det==3
summary={'Q_order':576,'qF_order':96,'qF_prime_order':8,
 'qF_prime_is_Q8':True,'Q_over_qF_prime_order':72,
 'qF_abelianization_order':12,'qF_abelianization_type':['C2','C6'],
 'full_N_abelian_image_lattice_columns':Lambda,'lattice_index_in_Zhat_squared':12,
 'lattice_congruences':['a=0 mod2','b=0 mod2','a+b=0 mod3'],
 'all144_mod12_relation_classes_checked':True,
 'all_Fermat_base_indices_checked_through':60,
 'H12_order':6912,'L12_free_rank':1153,
 'r_matrix_on_sphere_graph_homology':MR,
 'determinant_one_minus_r':det,
 'centralizer_of_r_in_qF_prime':[list(q) for q in q8_r_fixed],
 'actual_arithmetic_A_H_infinity_coordinate':[5,0,0,5],
 'scope':'Exact finite/lattice certificate for the closed-source inverse systems and coherent arithmetic/identity-prime action proved in D47. The inverse-limit and centralizer existence proofs are given there; they are not inferred from finite indices.',
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'Q':[list(q) for q in Q],'qF':[list(q) for q in H],
 'qF_prime':[list(q) for q in sorted(Hp)],'mod12_abelian_relation_classes':relations,
 'finite_Fermat_base_table':table}
(OUT/'d_cm_fermat_relative_tower.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
