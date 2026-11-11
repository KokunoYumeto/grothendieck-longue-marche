#!/usr/bin/env python3
"""Exact finite checks for the arithmetic contribution. Python 3 + sympy."""
from itertools import product
from math import gcd
from pathlib import Path
import json
import sympy as sp

def mul(a,b,n):
    A,B,C,D=a; e,f,g,h=b
    return ((A*e+B*g)%n,(A*f+B*h)%n,(C*e+D*g)%n,(C*f+D*h)%n)
def inv(a,n):
    A,B,C,D=a
    return (D%n,(-B)%n,(-C)%n,A%n)
def scale(a,c,n): return tuple(c*v%n for v in a)
def det(a,n): return (a[0]*a[3]-a[1]*a[2])%n
def parity(a):
    vs=[(1,0),(0,1),(1,1)]
    p=[vs.index(((a[0]*x+a[1]*y)%2,(a[2]*x+a[3]*y)%2)) for x,y in vs]
    return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

def twist(a,n): return scale(a,-1 if parity(a) else 1,n)

out={}
# Unit norm residues prove the signs, independently of class field theory.
out['unit_norm_residues']={
    't^2+u^2 mod4':sorted({(t*t+u*u)%4 for t,u in product(range(4),repeat=2) if gcd(t*t+u*u,4)==1}),
    'c^2+cd+d^2 mod3':sorted({(c*c+c*d+d*d)%3 for c,d in product(range(3),repeat=2) if gcd(c*c+c*d+d*d,3)==1})}
out['characters_mod12']=[{'mu':a,'epsilon2':1 if a%4==1 else -1,'epsilon3':1 if a%3==1 else -1} for a in (1,5,7,11)]
out['two_adic_square_counterexample']={'mu_mod8':5,'epsilon2':1,'odd_squares_mod8':sorted({a*a%8 for a in (1,3,5,7)})}
# Symbolic matrix proof of epsilon' = epsilon2 and norm determinant.
t,u,mu,e=sp.symbols('t u mu e'); S=sp.Matrix([[0,1],[-1,0]])
U=sp.Matrix([[u,e*t],[-t,e*u]])
out['matrix_US_minus_eSU_mod_e2minus1']=[str(sp.rem(x,e**2-1,e)) for x in U*S-e*S*U]
out['matrix_determinant']=str(sp.factor(U.det()))
x,L=sp.symbols('x L'); out['legendre_discriminant']=str(sp.factor(16*sp.discriminant(x*(x-1)*(x-L),x)))
# Check all six candidate r for Pop's rigidity reduction.
v=sp.symbols('v'); rr=[x,1-x,1/x,1/(1-x),x/(x-1),(x-1)/x]
out['pop_rigidity']=[{'r':str(r),'difference':str(sp.factor(r.subs(x,v)-r.subs(x,u)-r.subs(x,v-u))),'satisfies':sp.simplify(r.subs(x,v)-r.subs(x,u)-r.subs(x,v-u))==0} for r in rr]
# The central transvection is tested on all elements and generators.
rows=[]
for n in (2,4,6,8,12,24):
    G=[a for a in product(range(n),repeat=4) if det(a,n)==1]
    S=(0,1%n,(-1)%n,0); T=(1,1,0,1)
    assert all(twist(twist(g,n),n)==g for g in G)
    assert all(twist(mul(g,a,n),n)==mul(twist(g,n),twist(a,n),n) for g in G for a in (S,T))
    candidates=[g for g in G if all(mul(mul(g,a,n),inv(g,n),n)==twist(a,n) for a in (S,T))]
    rows.append({'n':n,'SL2_order':len(G),'twist_is_automorphism':True,'twist_inner':bool(candidates),'inner_conjugator_count':len(candidates),'twisted_S':twist(S,n),'twisted_T':twist(T,n)})
out['central_transvection']=rows
# Fixed modular inclusion lifts: signs chosen independently for generators.
out['geometric_lift_signs']=[{'a':a,'b':b,'twist':f'lambda^{a}*(lambda-1)^{b}'} for a,b in product((0,1),repeat=2)]
# Four complements in the level-four image of Gamma(2).
n=4; ident=(1,0,0,1); AA=(1,2,0,1); BB=(1,0,2,1)
comps=[]
for ee,ff in product((0,1),repeat=2):
    cc=set()
    for aa,bb in product((0,1),repeat=2):
        g=mul(AA if aa else ident,BB if bb else ident,n)
        cc.add(scale(g,(-1)**(ee*aa+ff*bb),n))
    assert len(cc)==4
    comps.append(cc)
out['four_complements_mod4']={'sizes':[len(c) for c in comps],'intersection':sorted(set.intersection(*comps)),'Gamma2_image_size':8,'index_intersection_in_Gamma2':8}
out['central_lift_abelianization']=[{'mu_mod12':m,'S_exponent_mod4':m%4,'R_exponent_mod6':m%6,'T_image_mod12':(3*(m%4)-2*(m%6))%12,'other_lift_T_image_mod12':(3*(m%4)-2*(m%6)+6)%12} for m in (1,5,7,11)]
path=Path(__file__).with_suffix('.json'); path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
