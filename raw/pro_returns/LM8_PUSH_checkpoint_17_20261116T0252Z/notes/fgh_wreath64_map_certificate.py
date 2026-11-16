from pathlib import Path
import sympy as s,json
x=s.symbols('x');F=x**3-6*x**2+x
u=(x-1)**2/(4*x);v2=F*(1-x*x)**2/(64*x**4)
assert s.factor(v2-(u**3-u))==0
# Exact doubling at R=(1,2i) on y^2=x^3+a*x^2+b*x.
a=-6;b=1;xR=s.Integer(1);yR=2*s.I
slope=(3*xR*xR+2*a*xR+b)/(2*yR)
x2=s.simplify(slope*slope-a-2*xR);y2=s.simplify(-yR+slope*(xR-x2))
assert x2==0 and y2==0
assert s.simplify(u.subs(x,1))==0
out={'status':'PASS','curve':'y^2=x^3-6x^2+x','isogeny_u':str(u),'isogeny_v_over_y':'(1-x^2)/(8*x^2)','target_equation_residual':'0','R':['1','2i'],'twice_R':['0','0'],'R_image':['0','0'],'scope':'Exact proper isogeny/doubling identities; no marked-reduction or fixed-subgroup inference.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
