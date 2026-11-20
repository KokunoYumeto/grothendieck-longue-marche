"""Exact countermodel for the relations labelled (1),(2),rho^3=1.

The affine transformations x -> a*x+b are represented by integer pairs.
Composition is from right to left, matching the author's function convention.
This checks only that the displayed proposed relators do not imply the
separately displayed cyclic conjugation relations; it does not import a
presentation of a geometric group from outside these pages.
"""
from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
def mul(f,g):
    a,b=f;c,d=g
    return (a*c,a*d+b)
def inv(f):
    a,b=f
    assert a in (1,-1)
    return (a,-a*b)
I=(1,0)
s0=(-1,0);s1=(-1,2);si=s0;rho=I
l0=mul(s0,s1);l1=mul(s1,si);li=mul(si,s0)
checks={
 'sigma0_squared':mul(s0,s0)==I,
 'sigma1_squared':mul(s1,s1)==I,
 'sigmainfinity_squared':mul(si,si)==I,
 'sigma0_sigma1_equals_rho_l0':mul(s0,s1)==mul(rho,l0),
 'sigma1_sigmainfinity_equals_rho_l1':mul(s1,si)==mul(rho,l1),
 'sigmainfinity_sigma0_equals_rho_linfinity':mul(si,s0)==mul(rho,li),
 'linfinity_l1_l0_equals_one':mul(mul(li,l1),l0)==I,
 'rho_cubed_equals_one':mul(mul(rho,rho),rho)==I,
}
assert all(checks.values())
conjugate=mul(mul(rho,s0),inv(rho))
assert conjugate!=s1
out={
 'model':'Affine transformations x -> a*x+b on the real line; tuple (a,b)',
 'assignments':dict(sigma0=s0,sigma1=s1,sigmainfinity=si,rho=rho,l0=l0,l1=l1,linfinity=li),
 'relators':checks,
 'failed_consequence':{'rho_sigma0_rho_inverse':conjugate,'sigma1':s1,'unequal':True},
 'infinite_image_certificate':'l0(x)=x-2, so l0^n(x)=x-2n and the image is infinite.',
 'scope':'The labelled proposed relations admit a model violating the cyclic conjugation identity shown separately on the page. No external group presentation is assumed.'
}
(E/'reader_reports/145_scan018_presentation_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
