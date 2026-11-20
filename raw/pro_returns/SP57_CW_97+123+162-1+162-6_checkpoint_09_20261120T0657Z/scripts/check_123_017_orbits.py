"""Exact small-rank checks of the source's orbit/affine-space assertions; no image processing."""
from pathlib import Path
import json
import sympy as S
O=Path(__file__).resolve().parents[1]
a,b,c=S.symbols('a b c')
e=S.Matrix([[0,1],[0,0]]);h=S.diag(1,-1);f=S.Matrix([[0,0],[1,0]]);z=S.zeros(2)
br=lambda x,y:x*y-y*x
assert br(e,h)==-2*e
# Product example: a=(h,0), v=(0,h). v centralizes e=(e,0), but a+v
# cannot equal [e,w] for any w because the second component is always zero.
assert br(z,h)==z
A=S.diag(2,0,-2); E=S.Matrix([[0,1,0],[0,0,1],[0,0,0]])
U=S.Matrix([[1,a,b],[0,1,c],[0,0,1]])
AU=S.simplify(U*A*U.inv());EU=S.simplify(U*E*U.inv())
assert AU==S.Matrix([[2,-2*a,2*a*c-4*b],[0,0,-2*c],[0,0,-2]])
assert EU==S.Matrix([[0,1,a-c],[0,0,1],[0,0,0]])
w12,w23,w13,t=S.symbols('w12 w23 w13 t')
inv={a:-w12/2,c:-w23/2,b:w12*w23/8-w13/4}
assert S.simplify(AU.subs(inv)-A)==S.Matrix([[0,w12,w13],[0,0,w23],[0,0,0]])
assert EU.subs({a:t,c:0,b:0})==E+S.Matrix([[0,0,t],[0,0,0],[0,0,0]])
result={
 'product_counterexample':{'G':'SL2 x SL2','e':'(E12,0)','a':'(diag(1,-1),0)','v':'(0,diag(1,-1))','centralizes_e':True,'a_plus_v_in_a_plus_full_g_centralizer':True,'a_plus_v_in_image_ad_e':False,'reason':'Every bracket with (E12,0) has second component zero. Thus a+v fails condition c) of scan16 although v is in g^e.','positive_weight_centralizer':'span((E12,0))'},
 'SL3_example':{'x':str(A),'e':str(E),'U':str(U),'Ad_U_x':str(AU),'Ad_U_e':str(EU),'inverse_for_Ad_U_x_minus_x':{str(k):str(v) for k,v in inv.items()},'surjectivity_onto_e_plus_Fil3':'a=t,c=0,b=0 gives e+t E13'},
 'status':'all exact symbolic assertions passed','scope':'Concrete examples/counterexample; general parabolic and integration theorems are not proved by this certificate.'}
p=O/'math_checks/123_017_orbits_certificate.json';p.write_text(json.dumps(result,indent=2));print(p)
