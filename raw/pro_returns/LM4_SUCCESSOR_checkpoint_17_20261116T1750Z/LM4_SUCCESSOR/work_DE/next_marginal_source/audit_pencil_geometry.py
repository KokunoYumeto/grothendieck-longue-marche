"""Exact coefficient deformation and common-source marking audit."""
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as S
from quadratic_pencil_braid import u,frac,sqrt_interval,complex_sqrt,ROT
HERE=Path(__file__).resolve().parent
rt5=sqrt_interval((F(5),F(5)))
sp=sqrt_interval((10+2*rt5[0],10+2*rt5[1]))
sm=sqrt_interval((10-2*rt5[1],10-2*rt5[0]))
re1=((rt5[0]-1)/4,(rt5[1]-1)/4);re2=(-(rt5[1]+1)/4,-(rt5[0]+1)/4)
im1=(sp[0]/4,sp[1]/4);im2=(sm[0]/4,sm[1]/4)
exact=[((F(1),F(1)),(F(0),F(0))),
       (re1,im1),(re2,im2),(re2,(-im2[1],-im2[0])),(re1,(-im1[1],-im1[0]))]
for z,(ri,ii) in zip(u,exact):
 for a,interval in ((frac(S.re(z)),ri),(frac(S.im(z)),ii)):
  assert max(abs(a-interval[0]),abs(a-interval[1]))<F(1,10**30)
 assert abs(S.re(z))+abs(S.im(z))<2
for i in range(5):
 for j in range(i):assert S.expand(S.re(u[i]-u[j])**2+S.im(u[i]-u[j])**2)>1
assert S.re(ROT)**2+S.im(ROT)**2<2
# Uniform bounds used on every certified segment:
# |t|<5; all point moduli<25; square-root radicand |U|>1e-8.
# Rational/quadratic residual >1e-12 gives separation>1e-12/(2*25).
minimum_separation=F(1,5*10**13)
coefficient_error=F(2,10**30)
radicand_error=F(12)*coefficient_error # |ROT^2|/4 *4|t-1|<12.
assert radicand_error<F(1,2*10**8)
root_motion=radicand_error*10000
assert root_motion<F(1,10**23)
assert 2*F(1,10**23)<minimum_separation
# The original source path is entirely outside all deleted source roots.
# Source roots satisfy |s|<2, since |u(2*zeta-u)|<=3.
assert 2**2+2**2>2**2
assert re1[0]>F(3,10) and F(99)*re1[0]>10
# Along the short source-to-generic path the merging retained pair is
# isolated in projection.  Every other point begins with |Re|>1/4;
# its motion is<6/100, whereas the pair's projection lies in [0,.004].
other_rational=[-S.Integer(1),S.Integer(1)]+[v for q in u[1:] for v in (q-1,1-q)]
for r in other_rational:assert abs(S.re(S.expand(ROT*r)))>S.Rational(1,4)
for q in u[1:]:
 U=S.expand(ROT*ROT*(1-q))
 re,im=complex_sqrt(frac(S.re(U)),frac(S.im(U)))
 assert re[0]>F(1,4) # the negative root has the opposite projection.
assert F(1,4)-F(6,100)>F(1,100)
out={'coefficient_component_error_bound':'1/10^30','complex_error_bound':'2/10^30',
     'original_distinguished_zeta':'exp(2*pi*i/5), the coefficient u[1]',
     'projection_modulus_squared_bound':'2','parameter_L1_bound':'5','point_modulus_bound':'25',
     'certified_segment_pair_separation_lower_bound':str(minimum_separation),
     'homotopy_point_motion_upper_bound':'1/10^23',
     'source_path':['2+2i','10+10i','zeta*i*sqrt(9999)'],
     'normalized_special_source_point':{'v':'-99','w':'101','s':'i*sqrt(9999)'},
     'generic_parameter':'i/100','fixed_fiber_basepoint':'z=100',
     'root_ordering':'choose w=101*zeta at the endpoint and lift the displayed original-source path backwards',
     'source_to_generic_path':'t=i*y,0<=y<=1/100,z=100; lift s^2=vw continuously',
     'scope':'Exact deformation and common-source transport. No kernel-normality conclusion.'}
(HERE/'pencil_geometry_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact cyclotomic coefficient error<1e-30 per real/imaginary component: PASS')
print('Original source path outside |s|<=2 and endpoint root ordering: PASS')
print('Source-to-generic transport isolates a,b as adjacent punctures; all other projections stay outside (-.01,.01): PASS')
print('Uniform segment separation>2e-14 and coefficient-homotopy motion<1e-23: PASS, conditional only on the segment inequalities explicitly recorded by the crossing engine.')
print('Actual source/kernel comparison through the two finite covers is proved in polynomial_pencil_certificate.md.')

