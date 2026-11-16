#!/usr/bin/env python3
"""Primitive mod-five conductor-four Soulé class: exact residue certificate."""
from pathlib import Path
import json

q=101
primitive=2
i=pow(primitive,25,q)
zeta=pow(primitive,20,q)
assert i==10 and pow(i,2,q)==100
assert zeta==95 and pow(zeta,5,q)==1 and zeta!=1
assert pow(zeta,20,q)==1
factors=[]
unit=1
for a in range(1,5):
    factor=(1-i*pow(zeta,4*a,q))%q
    assert factor
    value=pow(factor,a**3,q)
    unit=unit*value%q
    factors.append({"a":a,"factor":factor,"exponent":a**3,"value":value})
assert unit==97 and pow(unit,20,q)==36 and pow(unit,20,q)!=1
out={
    "q":q,"primitive_root":primitive,"i":i,"zeta5":zeta,
    "exact_source_element":"product_{a=1}^4 (1-i*zeta5^(4a))^(a^3)",
    "factors":factors,
    "unit_mod_q":unit,"fifth_power_test":pow(unit,20,q),
    "zeta5_fifth_power_test":pow(zeta,20,q),
    "conclusion":"The source Kummer class is outside the cyclotomic line in Q(i,zeta5)^*/Q(i,zeta5)^*5; hence its character on Q(i,mu5^infty) is primitive.",
    "source":"Ishii-Goto, arXiv:2412.18846v2 Definition2.14 and Remark2.15(2); exact normalization checked by fgh_geometry."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
