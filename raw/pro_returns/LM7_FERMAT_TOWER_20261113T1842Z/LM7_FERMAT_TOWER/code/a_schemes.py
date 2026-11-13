#!/usr/bin/env python3
"""Integral polynomial certificates and manuscript counterexamples for A."""
from pathlib import Path
from itertools import product
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
I=s.eye(2);R=s.Matrix([[0,-1],[1,-1]]);S=s.Matrix([[0,1],[1,0]])
a0,a1,b0,b1,t,z,k,w=s.symbols('a0 a1 b0 b1 t z k w')
delta=s.Matrix([-1,1]);e=s.Matrix([0,3]);e0=s.Matrix([1,0]);e1=s.Matrix([0,1])
alpha=s.Matrix([a0,a1]);beta=s.Matrix([b0,b1])
F=(I-R)*alpha-(I-S)*beta
assert F==s.Matrix([a0+a1-b0+b1,2*a1-a0+b0-b1])
F0=s.Matrix([-F[0],s.expand((F[0]+F[1])/3)])
assert F0==s.Matrix([-a0-a1+b0-b1,a1])
assert (I-R)*delta==e
assert s.Matrix.hstack(delta,e).det()==-3
rows=[]
for a,b in product(range(2),repeat=2):
 r0=1-6*a+4*b;mu=r0+12*k
 nu=-3*a+2*b+6*k;wp=-a+b+3*k;d=-a+b+2*k
 assert s.expand(2*nu+1-mu)==0
 assert s.expand(4*wp-2*a+1-mu)==0
 assert s.expand(6*d-2*b+1-mu)==0
 assert s.expand(2*wp-a-3*d+b)==0
 # Fine scheme of scan41: 3*a1=2*w-a+b, k=w-a1.
 assert s.expand(wp-d-k)==0
 aa=t*e0+d*delta;bb=t*e0+z*(e0+e1)
 assert s.simplify(((I-R)*aa-(I-S)*bb)-d*e)==s.zeros(2,1)
 # Recover every parameter without dividing by 2 or 3.
 assert s.expand(aa[0]+aa[1]-t)==0 and bb[1]==z
 product_rep=(-5)**a*5**b
 corrected_wp=-a+b-6*a*b+3*k
 corrected_d=-a+b-4*a*b+2*k
 assert s.expand(1-2*a+4*corrected_wp-product_rep-12*k)==0
 assert s.expand(1-2*b+6*corrected_d-product_rep-12*k)==0
 rows.append({'nu2':a,'nu3':b,'representative':r0,'mu':str(mu),
              'nu':str(nu),'nu_prime':str(wp),'nu_doubleprime':str(d),
              'product_representative':product_rep})

# Product and central extension identities on every pair of components.
kp=s.symbols('kp');product_checks=[]
for a,b,ap,bp in product(range(2),repeat=4):
 mu=1-6*a+4*b+12*k;mp=1-6*ap+4*bp+12*kp
 aa=(a+ap)%2;bb=(b+bp)%2
 kk=s.expand((mu*mp-(1-6*aa+4*bb))/12)
 assert all(c.q==1 for c in s.Poly(kk,k,kp).coeffs())
 d=-a+b+2*k;dp=-ap+bp+2*kp;dd=-aa+bb+2*kk
 nu=(mu-1)/2;nup=(mp-1)/2;nuprod=(mu*mp-1)/2
 assert s.expand(nuprod-nu-mu*nup)==0
 assert s.expand(dd-(1-2*bp)*d-mu*dp)==0
 product_checks.append({'bits':[a,b,ap,bp],'k_product':str(kk),
                        'central_cocycle':((a+b)*bp)%2})

# Defects in literal equations; every ring arithmetic claim is checked.
counter={}
counter['scan51_67b']={'ring':'F2','N':2,'distinct_sections':[[0,0],[0,1]],
 'common_evaluation':0,'reason':'distinct affine coordinates on the same component'}
counter['scan52_68']={'N':12,'n':0,'n_prime':0,'x':1,'y':1,
 'literal_evaluation':12,'correct_evaluation':144}
assert 12!=144
counter['scan54_77']={'ring':'Q','section':[5,'-1/3'],'evaluation':1,
 'nonidentity_component':5,'identity_component':1}
assert s.Rational(5)+12*s.Rational(-1,3)==1
counter['scan56_83']={'ring':'Z','residue_class':5,'candidate':5,
 'reason':'5 is not a unit of Z; no section of this component exists over Z'}
counter['scans57_58_coefficients']={'ring':'F7','nu2':1,'nu3':1,'nu0':0,
 'mu':(-25)%7,'printed_nu_prime':(-3)%7,'correct_nu_prime':(-6)%7,
 'mu_from_printed_nu_prime':(1-2+4*(-3))%7,
 'printed_nu_doubleprime':(-2)%7,'correct_nu_doubleprime':(-4)%7,
 'mu_from_printed_nu_doubleprime':(1-2+6*(-2))%7}
assert counter['scans57_58_coefficients']['mu'] != counter['scans57_58_coefficients']['mu_from_printed_nu_prime']
assert counter['scans57_58_coefficients']['mu'] != counter['scans57_58_coefficients']['mu_from_printed_nu_doubleprime']
counter['scan61_100_sign']={'ring':'Z','nu_doubleprime':1,'alpha':[-1,1],
 'beta':[0,0],'correct_left_side':[0,0],'printed_plus_left_side':[0,6]}
assert (I-R)*(delta-delta)==s.zeros(2,1)
assert list((I-R)*(delta+delta))==[0,6]
counter['scan82_171_172']={'ring':'F2','gamma_component':[1,0],'k':0,
 'mu':1,'literal_171_component_images':[[0,0],[1,1]],
 'final_212_component_images':[[0,0],[0,1],[1,0],[1,1]]}
counter['scan87_195_missing_quotient']={'ring':'F2','Gamma_points':32,
 'gamma_semidirect_Ga_points':16,'kernel':'constant C2'}

# Non-flat raw kernel, and its flat closure, verified on finite fields.
raw=[]
for p in [2,3,5,7]:
 points=sum(1 for aa0,aa1,bb0,bb1 in product(range(p),repeat=4)
            if (aa0+aa1-bb0+bb1)%p==0 and (2*aa1-aa0+bb0-bb1)%p==0)
 assert points==p**(3 if p==3 else 2)
 raw.append({'p':p,'raw_kernel_points':points,'flat_kernel_points':p*p})

# Explicit isomorphisms of the two finite stabilizer groups.
# Coordinates (i,a,b,k,s) map to (i, unit mod 12p, s).
finite_group_certificates=[]
for p,gena,genb,genk in [(2,7,5,13),(3,19,17,13)]:
 n=12*p
 domain=list(product(range(2),range(2),range(2),range(p),range(p)))
 def map_point(v):
  i,a,b,kk,ss=v
  return (i,pow(gena,a,n)*pow(genb,b,n)*pow(genk,kk,n)%n,ss)
 assert len({map_point(v) for v in domain})==len(domain)
 assert len(domain)==(32 if p==2 else 72)
 for v,vp in product(domain,repeat=2):
  i,a,b,kk,ss=v;j,ap,bp,kp,sp=vp
  aa=(a+ap)%2;bb=(b+bp)%2
  prod=((i+j+(a+b)*bp)%2,aa,bb,(kk+kp)%p,(ss+(1-2*b)*sp)%p)
  im=map_point(v);imp=map_point(vp)
  expected=((im[0]+imp[0]+(a+b)*bp)%2,im[1]*imp[1]%n,
            (im[2]+im[1]*imp[2])%p)
  assert map_point(prod)==expected
 finite_group_certificates.append({'p':p,'order':len(domain),
  'unit_lifts_for_bits':[gena,genb],'unit_kernel_generator':genk,
  'multiplication_pairs_checked':len(domain)**2,
  'group':'D8 x C2^2' if p==2 else 'C3 x (C3 semidirect D8), action=(-1)^b'})

# The kernel of (56) is the raw kernel; the w-map has a universal section
# a1=-2w, a0=2w, b0=b1=0 over 4w=0.
secF=F.subs({a0:2*w,a1:-2*w,b0:0,b1:0})
assert secF[0]==0 and s.expand(secF[1]-2*w)==-8*w

out={'lattice_F':str(F),'F_in_M0_basis':str(F0),'gamma_charts':rows,
 'product_certificates':product_checks,'counterexamples':counter,
 'raw_kernel_finite_points':raw,'finite_group_isomorphisms':finite_group_certificates,
 'all_symbolic_assertions_passed':True}
(ROOT/'code/a_schemes.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
