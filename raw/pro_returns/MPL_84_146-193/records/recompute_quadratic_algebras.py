#!/usr/bin/env python3
"""Exact, post-freeze checks of the local algebra on cote 84 scans 172–192.

Run: python records/recompute_quadratic_algebras.py
Requires SymPy. Writes recompute_quadratic_algebras_results.json beside this file.
This script does not read images or change transcription files. The mathematical
model is an editorial interpretation, explicitly separated from doubtful ink:
Ai=R[ui]/(ui**2+bi*ui+ci), A=R[t]/(t**2+b1*b2*t+c).
All universal assertions are polynomial or matrix identities over Z[parameters].
The finite examples illustrate them; no finite search is used to prove a general
classification or any categorical coherence claim.
"""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
from itertools import product
import json
from pathlib import Path
import sympy as s

x,y,t,b1,b2,c1,c2=s.symbols('x y t b1 b2 c1 c2')
b=b1*b2
c=b1**2*c2+b2**2*c1-4*c1*c2
u=2*x*y+b2*x+b1*y

def red(z):
    return s.expand(s.rem(s.rem(s.expand(z),x*x+b1*x+c1,x),y*y+b2*y+c2,y))
def vec(z):
    p=s.Poly(red(z),x,y)
    return s.Matrix([p.coeff_monomial(m) for m in [1,x,y,x*y]])
def serial_mat(m):
    return [[str(s.factor(v)) for v in row] for row in m.tolist()]

identities={
 'quadratic_relation':red(u*u+b*u+c),
 'discriminant_product':s.expand(b*b-4*c-(b1*b1-4*c1)*(b2*b2-4*c2)),
 'total_conjugation_fixes_u':s.expand(u.subs({x:-b1-x,y:-b2-y},simultaneous=True)-u),
 'single_conjugation_on_u':s.expand(u.subs(x,-b1-x)+b+u),
 'star_tensor_shift':s.expand(x*y+(-b1-x)*(-b2-y)-u-b),
}
S=s.Matrix.hstack(*[vec(z.subs({x:-b1-x,y:-b2-y},simultaneous=True)) for z in [s.Integer(1),x,y,x*y]])
T=s.eye(4)+S
I=s.Matrix.hstack(vec(s.Integer(1)),vec(u))
Q=s.Matrix([[2,-b1,-b2,b],[0,0,0,1]])
for name,m in [('conjugation_involution',S*S-s.eye(4)),('symmetrizer_factorization',I*Q-T),('reverse_composite',Q*I-2*s.eye(2)),('symmetrizer_square',T*T-2*T),('dual_factorization',Q.T*I.T-T.T),('restricted_dual_pairing',I.T*Q.T-2*s.eye(2))]:
    assert all(s.expand(v)==0 for v in m),name
assert all(s.expand(v)==0 for v in identities.values())

# Associativity of the displayed coefficient law, not a proof of categorical coherence.
b3,c3=s.symbols('b3 c3')
def law(B,C,D,E):
    return B*D,s.expand(B*B*E+D*D*C-4*C*E)
b12,c12=law(b1,c1,b2,c2)
bL,cL=law(b12,c12,b3,c3)
b23,c23=law(b2,c2,b3,c3)
bR,cR=law(b1,c1,b23,c23)
assert s.expand(bL-bR)==s.expand(cL-cR)==0
b21,c21=law(b2,c2,b1,c1)
assert s.expand(b12-b21)==s.expand(c12-c21)==0
assert law(b1,c1,s.Integer(1),s.Integer(0))==(b1,c1)

# Generator changes ui'=ai*ui+ri, ai units; identities themselves hold polynomially.
a1,a2,r1,r2=s.symbols('a1 a2 r1 r2')
xp=a1*x+r1;yp=a2*y+r2
bp1=a1*b1-2*r1;bp2=a2*b2-2*r2
cp1=r1*r1-a1*b1*r1+a1*a1*c1
cp2=r2*r2-a2*b2*r2+a2*a2*c2
scale=a1*a2
shift=a1*b1*r2+a2*b2*r1-2*r1*r2
up=2*xp*yp+bp2*xp+bp1*yp
bp=bp1*bp2
cp=bp1*bp1*cp2+bp2*bp2*cp1-4*cp1*cp2
assert s.expand(up-scale*u-shift)==0
assert s.expand(bp-(scale*b-2*shift))==0
assert s.expand(cp-(shift*shift-scale*b*shift+scale*scale*c))==0

# Trace and norm in A, using t²+b t+c=0.
lam,mu=s.symbols('lambda mu')
mult_t=s.Matrix([[0,-c],[1,-b]])
mult_lam_t_mu=lam*mult_t+mu*s.eye(2)
assert s.expand(s.trace(mult_lam_t_mu)-(-lam*b+2*mu))==0
assert s.expand(mult_lam_t_mu.det()-(lam*lam*c+mu*mu-lam*mu*b))==0

# Full finite coefficient grids: p^4 choices, retaining inseparable/nonreduced cases.
finite=[]
for p in (2,3,5):
    ranks=Counter(); root_counts=Counter(); etale_inputs=0
    for B1,B2,C1,C2 in product(range(p),repeat=4):
        B=(B1*B2)%p; C=(B1*B1*C2+B2*B2*C1-4*C1*C2)%p
        rank=1 if all(v%p==0 for v in (2,B1,B2)) else 2
        ranks[rank]+=1
        root_counts[sum((v*v+B*v+C)%p==0 for v in range(p))]+=1
        etale_inputs+=int((B1*B1-4*C1)%p!=0 and (B2*B2-4*C2)%p!=0)
        # Relation, evaluated in the free tensor basis, for all finite choices.
        val=red(u*u+b*u+c).subs({b1:B1,b2:B2,c1:C1,c2:C2})
        assert val==0
    assert sum(ranks.values())==p**4
    finite.append({'p':p,'parameter_order':['b1','b2','c1','c2'],'parameter_values':list(range(p)),
                   'total':p**4,'embedding_matrix_ranks':dict(sorted(ranks.items())),
                   'product_polynomial_root_counts':dict(sorted(root_counts.items())),
                   'both_inputs_etale':etale_inputs})

artin_schreier=[]
for C1,C2 in product(range(2),repeat=2):
    C=(C1+C2)%2
    artin_schreier.append({'b1':1,'b2':1,'c1':C1,'c2':C2,'product_b':1,'product_c':C,
                          'roots_in_F2':[v for v in range(2) if (v*v+v+C)%2==0]})

# Direct finite-ring kernel computation, testing the general annihilator criterion.
ring_cases=[]
for modulus,B1,B2 in [(4,0,0),(4,2,0),(4,1,0),(6,0,0),(6,3,0)]:
    kernel=[(A,D) for A,D in product(range(modulus),repeat=2)
            if all(v%modulus==0 for v in (A,D*B2,D*B1,2*D))]
    ann=[D for D in range(modulus) if all(D*v%modulus==0 for v in (2,B1,B2))]
    assert kernel==[(0,D) for D in ann]
    ring_cases.append({'ring':f'Z/{modulus}Z','b1':B1,'b2':B2,'c1':0,'c2':0,
                       'kernel_as_constant_t_coefficient_pairs':kernel,
                       'annihilator_of_2_b1_b2':ann,'injective':len(kernel)==1})

# Special b1=b2=0 table of scan 186, with order made explicit.
special_table=[str(v) for v in T.subs({b1:0,b2:0})*s.Matrix([1,0,0,0])]
special_images={str(z):str(s.expand(z+z.subs({x:-x,y:-y},simultaneous=True))) for z in [s.Integer(1),x,y,x*y]}

report={
 'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'scope':'Post-freeze interpretation and exact checks; does not resolve doubtful ink or prove full category coherence.',
 'sympy_version':s.__version__,
 'source_scans':[172,174,176,178,180,182,184,186,188,190,192],
 'basis_B':['1','u1','u2','u1*u2'],'basis_A':['1','t'],
 'quadratic_product':{'b':str(b),'c':str(c),'image_of_t':str(u)},
 'universal_polynomial_remainders':{k:str(v) for k,v in identities.items()},
 'matrices':{'sigma1_tensor_sigma2':serial_mat(S),'T_id_plus_sigma':serial_mat(T),'i_A_to_B':serial_mat(I),'q_B_to_A':serial_mat(Q)},
 'verified_matrix_identities':['S^2=I4','i*q=T','q*i=2I2','T^2=2T','q^T*i^T=T^T','i^T*q^T=2I2'],
 'general_kernel':'ker(i) = {d*t : d in Ann_R(2,b1,b2)}',
 'general_cokernel_q':'coker(q) = R/(2,b1,b2)',
 'general_injectivity':'i is injective iff Ann_R(2,b1,b2)=0; it is a split injection iff (2,b1,b2)=R',
 'coefficient_law':{'associative':True,'commutative':True,'unit_pair':[1,0],'triple_c':str(cL),'categorical_coherence_proved':False},
 'generator_change':{'new_ui':'ai*ui+ri','new_bi':'ai*bi-2*ri','new_ci':'ri^2-ai*bi*ri+ai^2*ci','new_t':'a1*a2*t+a1*b1*r2+a2*b2*r1-2*r1*r2','verified':True},
 'trace_norm':{'element':'lambda*t+mu','trace':str(-lam*b+2*mu),'norm':str(lam*lam*c+mu*mu-lam*mu*b),'verified':True},
 'finite_fields':finite,
 'characteristic_two_etale_examples':artin_schreier,
 'finite_ring_kernel_examples':ring_cases,
 'scan186_specialized_table':special_images,
 'interpretation_limits':['R is commutative, all displayed local quadratic presentations are monic and free rank two.','The input coefficients b1,b2,c1,c2 are freely varying scalar coordinates, not global untwisted sections by default.','Perfect abstract A-E duality is distinct from the trace pairing and from restriction of tensor pairings.','A universal polynomial identity plus finite checks does not settle the full Hua symmetric-monoidal or invertibility assertions.']
}
path=Path(__file__).with_name('recompute_quadratic_algebras_results.json')
path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'output':str(path),'universal_identities_passed':len(identities),'matrix_identities_passed':6,'finite_parameter_cases':sum(z['total'] for z in finite),'finite_ring_cases':len(ring_cases)},indent=2))
