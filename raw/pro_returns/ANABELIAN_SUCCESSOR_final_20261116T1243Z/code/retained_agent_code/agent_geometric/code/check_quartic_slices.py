"""Exact symbolic verification of all normalization identities in AG.25."""
import sympy as s
import json
x,y,z,A,B,C,D,E=s.symbols('x y z A B C D E')
a,b,c,d,e,f,g,u,v,w,r,t=s.symbols('a b c d e f g u v w r t')
F=y*z**3+(a*x*x+b*x*y+c*y*y)*z*z+(d*x**3+e*x*x*y+f*x*y*y+g*y**3)*z+u*x**4+v*x**3*y+w*x*x*y*y+r*x*y**3+t*y**4
G=s.Poly(s.expand(F.subs({x:A*x+B*y,y:C*y,z:z+D*x+E*y},simultaneous=True)/C),x,y,z)
expressions={
 'a':(G.coeff_monomial(x*x*z*z),a*A*A/C),
 'b':(G.coeff_monomial(x*y*z*z),3*D+2*a*A*B/C+b*A),
 'c':(G.coeff_monomial(y*y*z*z),3*E+a*B*B/C+b*B+c*C),
 'd':(G.coeff_monomial(x**3*z),2*a*A*A*D/C+d*A**3/C),
 'flex_e':(G.coeff_monomial(x*x*y*z).subs(a,0).subs(C,d*A**3),
           3*D*D+2*b*A*D+3*B/A+e*A*A),
 'hyperflex_v':(G.coeff_monomial(x**3*y).subs({a:0,d:0}).subs(C,u*A**4),
                D**3+b*A*D*D+e*A*A*D+4*B/A+v*A**3),
}
for name,(actual,expected) in expressions.items():
    assert s.cancel(actual-expected)==0,name
normalizations=[]
Cn=a*A*A;Dn=-d*A/(2*a);Bn=-A*(3*Dn+b*A)/2
En=-(a*Bn*Bn/Cn+b*Bn+c*Cn)/3
normalizations.append(('nonflex',{C:Cn,D:Dn,B:Bn,E:En},{x*x*z*z:1,x*y*z*z:0,y*y*z*z:0,x**3*z:0}))
Cn=d*A**3;Dn=-b*A/3;Bn=-A*(3*Dn*Dn+2*b*A*Dn+e*A*A)/3;En=-(b*Bn+c*Cn)/3
normalizations.append(('flex',{a:0,C:Cn,D:Dn,B:Bn,E:En},{x*x*z*z:0,x*y*z*z:0,y*y*z*z:0,x**3*z:1,x*x*y*z:0}))
Cn=u*A**4;Dn=-b*A/3;Bn=-A*(Dn**3+b*A*Dn*Dn+e*A*A*Dn+v*A**3)/4;En=-(b*Bn+c*Cn)/3
normalizations.append(('hyperflex',{a:0,d:0,C:Cn,D:Dn,B:Bn,E:En},{x*x*z*z:0,x*y*z*z:0,y*y*z*z:0,x**3*z:0,x**4:1,x**3*y:0}))
for name,sub,targets in normalizations:
    for mon,value in targets.items():
        assert s.cancel(G.coeff_monomial(mon).subs(sub,simultaneous=True)-value)==0,(name,mon)
print(json.dumps({'symbolic_coefficient_identities':list(expressions),
                  'normalizations':[n for n,_,_ in normalizations],
                  'all_rational_function_identities':True,
                  'denominators_require':'characteristic different from2 and3; A and the indicated a,d,u nonzero',
                  'F5_slice_forms':5**8+5**7+5**6,
                  'F5_full_stabilizer_order':(5-1)**2*5**3,
                  'F5_residual_group_order':4,
                  'assertions':'all passed'},indent=2))
