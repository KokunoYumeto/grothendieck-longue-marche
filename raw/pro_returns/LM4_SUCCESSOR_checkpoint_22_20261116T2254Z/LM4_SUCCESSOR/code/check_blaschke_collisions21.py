#!/usr/bin/env python3
"""Exact norm identity and complete physical mixed-collision set in Q(zeta5)."""
from pathlib import Path
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
q,p,u,r,x=S.symbols('q p u r x')
alpha=u*(2-u)
abar=(1/u)*(2-1/u)
d=u*u+(1-2*u)*q
dbar=u**-2+(1-2/u)*p
identity=S.factor((q-alpha)*(p-abar)-d*dbar-(alpha*abar-1)*(1-q*p))
assert identity==0
tu=(q+u*u-2*u)/d
tr=tu.subs(u,r)
mixed=S.factor(S.together(tu+tr)*d*d.subs(u,r)
               +2*(q+u*r-r-u)*(q*(r+u-1)-u*r))
assert mixed==0

phi=S.Poly(x**4+x**3+x**2+x+1,x,domain=S.QQ)
def red(expr):
    numer,denom=S.fraction(S.cancel(expr))
    n=S.Poly(numer,x,domain=S.QQ).rem(phi)
    de=S.Poly(denom,x,domain=S.QQ).rem(phi)
    assert not de.is_zero
    return (n*S.invert(de,phi)).rem(phi).as_expr()
def conj(expr): return red(expr.subs(x,x**4))
def real_sqrt5(expr):
    coeffs=[S.Poly(red(expr),x,domain=S.QQ).nth(k) for k in range(4)]
    assert coeffs[1]==0 and coeffs[2]==coeffs[3],coeffs
    return S.simplify(coeffs[0]-coeffs[2]*(1+S.sqrt(5))/2)

nodes={}
pairs=[]
for i in range(1,5):
    for j in range(i,5):
        ui,rj=red(x**i),red(x**j)
        al=red(ui+rj-ui*rj)
        be=red(ui*rj/(ui+rj-1))
        assert red(be*conj(al)-1)==0
        anorm=real_sqrt5(red(al*conj(al)))
        assert (anorm-1).is_positive or (anorm-1).is_negative
        row={'i':i,'j':j,'alpha':str(al),'beta':str(be),
             'alpha_absolute_square':str(anorm),
             'alpha_region':'outer' if (anorm-1).is_positive else 'inner'}
        pairs.append(row)
        for kind,value in [('alpha',al),('beta',be)]:
            assert value!=0
            norm=real_sqrt5(red(value*conj(value)))
            region='outer' if (norm-1).is_positive else 'inner'
            assert (norm-1).is_positive or (norm-1).is_negative
            key=str(value)
            entry=nodes.setdefault(key,{'q':key,'region':region,'pairs':[],
                                        'quotient_node_count':0})
            assert entry['region']==region
            entry['pairs'].append({'i':i,'j':j,'kind':kind})
            entry['quotient_node_count']+=1 if i==j else 2

assert len(nodes)==18
regions={side:{'critical_base_values':sum(a['region']==side for a in nodes.values()),
               'quotient_physical_nodes':sum(a['quotient_node_count'] for a in nodes.values() if a['region']==side)}
         for side in ['inner','outer']}
assert regions=={'inner':{'critical_base_values':9,'quotient_physical_nodes':16},
                 'outer':{'critical_base_values':9,'quotient_physical_nodes':16}}
assert sum(a['quotient_node_count'] for a in nodes.values())==32
out={'status':'PASS','norm_identity':str(identity),'mixed_factor_identity':str(mixed),
     'field':'Q[x]/(x^4+x^3+x^2+x+1), x=exp(2*pi*i/5)',
     'pairs':pairs,'critical_values':list(nodes.values()),'regions':regions,
     'scope':'Complete physical graph collisions of actual free-swap quotient; no global fixed-lifting claim.'}
(ROOT/'records/blaschke_collisions21.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
