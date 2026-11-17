#!/usr/bin/env python3
"""Exact auxiliary checks for OP notes; never edits or reads manuscript images.

The mathematical scope is stated in operations_proofs.md.  Finite tests of the
orange formula accompany a general symbolic proof; they are not an induction.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

z,c,t,a=s.symbols("z c t a")
mob=z/(c*z+1-c)
mob2=s.factor(mob.subs(z,mob))
assert s.cancel(mob2-z+c*z*(c-2)*(z-1)/(c**2*z-c**2-2*c*z+2*c-1))==0
assert s.cancel(mob.subs(c,0)-z)==0
assert s.cancel(mob.subs(c,2).subs(z,mob.subs(c,2))-z)==0
fold=(2*z-1)**2
assert s.cancel(fold-1-4*z*(z-1))==0
assert s.cancel(s.diff(fold,z)-4*(2*z-1))==0
noncartographic=(2*z**3-1)**2
assert s.cancel(noncartographic-1-4*z**3*(z**3-1))==0
orange_checks=[]
for n in range(1,9):
    f=4*z**n/(1+z**n)**2
    assert s.cancel(f-1+(z**n-1)**2/(1+z**n)**2)==0
    assert s.cancel(s.diff(f,z)-4*n*z**(n-1)*(1-z**n)/(1+z**n)**3)==0
    assert s.cancel(f.subs(z,1/z)-f)==0
    orange_checks.append({"n":n,"degree":2*n,"passport":[[n,n],[2]*n,[2]*n]})
bouquet=z**4/(4*(z**2-1))
assert s.cancel(bouquet-1-(z**2-2)**2/(4*(z**2-1)))==0
assert s.cancel(s.diff(bouquet,z)-z**3*(z**2-2)/(2*(z-1)**2*(z+1)**2))==0
u,v=s.symbols("u v")
assert s.cancel(4*u*(1-u)-4*v*(1-v)+4*(u-v)*(u+v-1))==0
out={
 "checked_utc":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
 "scope":"Exact symbolic identities only; topology and categorical scope are in operations_proofs.md",
 "mobius_square":str(mob2),
 "mobius_square_minus_identity":str(s.factor(mob2-z)),
 "mobius_nonconstant_condition":"c != 1",
 "mobius_involution_parameters":[0,2],
 "fold_minus_one":str(s.factor(fold-1)),
 "fold_z_cubed_minus_one":str(s.factor(noncartographic-1)),
 "orange_checks":orange_checks,
 "bouquet_map":str(bouquet),
 "bouquet_minus_one":str(s.factor(bouquet-1)),
 "bouquet_derivative":str(s.factor(s.diff(bouquet,z))),
 "bouquet_passport":[[4],[2,2],[2,1,1]],
 "cleaning_identity":str(s.factor(4*u*(1-u)-4*v*(1-v))),
 "all_assertions_passed":True,
}
dest=Path(__file__).with_suffix(".json")
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"output":str(dest),"all_assertions_passed":True}))
