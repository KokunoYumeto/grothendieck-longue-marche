#!/usr/bin/env python3
"""Exact tame norm and ambiguous-class pairings for the degree-eighteen field."""
from pathlib import Path
import json

w = Path(__file__).resolve().parents[1]

def add(x,y,q): return ((x[0]+y[0])%q,(x[1]+y[1])%q)
def neg(x,q): return ((-x[0])%q,(-x[1])%q)
def sub(x,y,q): return add(x,neg(y,q),q)
def mul(x,y,q):
    a,b=x; c,d=y
    return ((a*c-b*d)%q,(a*d+b*c-b*d)%q)
def power(x,n,q):
    if n < 0: return power(power(x,q*q-2,q),-n,q)
    out=(1,0)
    while n:
        if n&1: out=mul(out,x,q)
        x=mul(x,x,q); n//=2
    return out
def div(x,y,q):
    assert y!=(0,0)
    return mul(x,power(y,-1,q),q)
def scalar(a,q): return (a%q,0)
def cubic_log(x,q):
    assert x!=(0,0)
    y=power(x,(q*q-1)//3,q)
    return [power((0,1),k,q) for k in range(3)].index(y)
def rank_mod3(rows):
    a=[[x%3 for x in row] for row in rows]; rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        k=pow(a[rank][j],-1,3)
        a[rank]=[(k*x)%3 for x in a[rank]]
        for i in range(len(a)):
            if i!=rank:
                k=a[i][j]
                a[i]=[(x-k*y)%3 for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank

rows=[]; pairings={}; residue_details=[]
for q in [11,59]:
    z=(0,1); one=(1,0)
    root=pow(3,pow(3,-1,q-1),q)
    assert pow(root,3,q)==3%q
    qrows=[]; z1_logs=[]; z2_logs=[]
    for j in range(3):
        alpha=mul(scalar(root,q),power(z,j,q),q)
        U=sub(power(alpha,2,q),scalar(2,q),q)
        pi=div(power(alpha,2,q),sub(z,one,q),q)
        tau_pi=neg(mul(z,pi,q),q)
        v=div(add(one,pi,q),add(one,power(pi,2,q),q),q)
        tau_v=div(add(one,tau_pi,q),add(one,power(tau_pi,2,q),q),q)
        epsilon=div(v,tau_v,q)
        assert mul(v,tau_v,q)==U
        logs=[cubic_log(U,q),cubic_log(epsilon,q),cubic_log(z,q)]
        rows.append(logs); qrows.append(logs)
        if j:
            h=add(one,mul(scalar(6,q),alpha,q),q)
            assert h==sub(one,power(z,j,q),q)
            # z2=d: divide by (t^2/q)^3, leaving (q/d)^3 alpha^-2.
            z2_unit=power(alpha,-2,q)
            # z1=11*h: valuation1 at q11, valuation0 at q59 on these branches.
            z1_unit=mul(h,power(alpha,-2,q),q) if q==11 else h
            z1_logs.append(cubic_log(z1_unit,q))
            z2_logs.append(cubic_log(z2_unit,q))
    pairings[str(q)]={'z1':(z1_logs[0]-z1_logs[1])%3,'z2':(z2_logs[0]-z2_logs[1])%3}
    residue_details.append({'q':q,'rational_root':root,'unit_rows_U_epsilon_zeta':qrows,'z1_plus_minus':z1_logs,'z2_plus_minus':z2_logs})

rank=rank_mod3(rows)
assert rank==3, (rank,rows)
matrix=[[pairings[str(q)][name] for q in [11,59]] for name in ['z1','z2']]
assert matrix==[[0,2],[2,1]],matrix
assert rank_mod3(matrix)==2

# K1 has v(alpha)=1 and v(3)=3.  The exact difference
# (2+alpha)^3 - 11*(1+6*alpha) = 6*alpha^2 - 54*alpha
# has distinct term valuations5 and10, and a unit denominator.
def vp(n,p):
    n=abs(n); k=0
    assert n
    while n%p==0: n//=p; k+=1
    return k
residual_terms=[3*vp(6,3)+2,3*vp(54,3)+1]
assert residual_terms==[5,10]
# With delta of depth5, c=delta/3 has depth2, first residual depth6;
# one further Newton correction has depth3 and residual at least9>6.
assert min(3+2*2,3*2)==6
assert min(3+2*3,3*3)==9 and 9>2*3
assert vp(649-1,3)==4

data={'field':'E2=Q(t,zeta), t^9=3*649^6; alpha=t^3/649^2',
      'radicals':{'z1':'11*(1+6*alpha)','z2':'649'},
      'residue_details':residue_details,'unit_norm_character_rank':rank,
      'anti_ambiguous_pairing_matrix':matrix,
      'local_cubic_check':{'K1_residual_depths':residual_terms,'second_Newton_residual_lower_bound':9,'derivative_depth':3,'v3_648':4},
      'scope':'Finite exact arithmetic supporting the separately proved class-group comparison; the program does not compute a class group.'}
target=Path(__file__).with_name('two_inert_level2_genus_pairing_certificate_data.json')
target.write_text(json.dumps(data,indent=2)+'\n')
print('PASS: six exact cubic-residue maps on U, epsilon, zeta have rank3')
print('Rows:',rows)
print('PASS: anti-ambiguous Frobenius pairing matrix',matrix,'has rank2')
print('PASS: exact depth5 local cube comparison, second Newton residual>=9>6, and d=649 rational cube criterion')
print('Data:',target)
