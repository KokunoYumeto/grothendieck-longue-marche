#!/usr/bin/env python3
"""Generate a local PARI candidate extraction; all roots need exact rechecking."""
from pathlib import Path
from fractions import Fraction
import json,sys
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
data=json.loads((base/"two_inert_relative_unit_repair_certificate_data.json").read_text())
def expr(cs):
    return "+".join("("+str(Fraction(c))+")*T^"+str(i) for i,c in enumerate(cs))
lines=[
 r"\\ Candidate extraction only: no BNF, class or regulator completeness.",
 "default(parisizemax,1500000000);",
 "default(parisize,256000000);",
 "default(realprecision,100);setrand(170);",
 "x='x;y='y;d=649;P=y^18+3*d^6;",
 'print("START EXACT FIELD");',
 "E=nfinit([P,[2,3,11,59]]);",
 'print("NF READY ",nfcertify(E));',
 "W=Mod(y,P);Z=(W^9/d^3-1)/2;T=-Z*W^2;",
 "if(Z^2+Z+1 || T^9-3*d^6,error(\"field map\"));",
]
for i,row in enumerate(data["units"][1:],2):
    lines += [
        "C="+expr(row["candidate"])+";",
        "C1=subst(lift(C),y,Z*W);",
    ]
    # sigma fixes alpha and sends T to zeta*T; on W it sends W to zeta^2*W.
    lines[-1]="C1=subst(lift(C),y,Z^2*W);"
    lines += [
        "C1=Mod(C1,P);C2=Mod(subst(lift(C),y,Z*W),P);V=C1/C2;",
        'print("START ROOT ",'+str(i)+');',
        "R=nfroots(E,x^3-V);",
        'print("ROOT COUNT ",'+str(i)+', " ",#R);',
        "for(j=1,#R,if(R[j]^3!=V,error(\"returned root\")));",
        'if(#R,print("ROOT COEFFICIENTS ",'+str(i)+', " ",Vecrev(lift(R[1]))));',
    ]
lines+=["quit;"]
out=base/"two_inert_level2_anti_cube_roots_pari.gp"
out.write_text("\n".join(lines)+"\n")
print(out)
