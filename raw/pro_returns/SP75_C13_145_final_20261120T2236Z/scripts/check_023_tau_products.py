"""Exact checks of the three products in scan023, using the local loop orientation."""
from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
def apply(f,w):return red(y for x in w for y in (f[x] if x>0 else inv(f[-x])))
def comp(f,g):return {i:apply(f,g[i]) for i in (1,2)}
def inner(w):return {i:mul(w,(i,),inv(w)) for i in (1,2)}
a=(1,);b=(2,);c=(-1,-2)
s0={1:mul(inv(c),inv(b)),2:c}
s1={1:c,2:mul(inv(a),inv(c))}
si={1:b,2:a}
t0={1:inv(a),2:inv(c)}
t1={1:inv(c),2:inv(b)}
ti={1:inv(b),2:inv(a)}
tau0=comp(s0,t0);tau1=comp(s1,t1);taui=comp(si,ti)
checks=[]
for name,left,right in [('tau-infinity tau1 = inner(l0)',comp(taui,tau1),inner(a)),('tau0 tau-infinity = inner(l1)',comp(tau0,taui),inner(b)),('tau1 tau0 = inner(l-infinity)',comp(tau1,tau0),inner(c))]:
    checks.append({'claim':name,'left':left,'right':right,'equal':left==right})
    assert left==right
def involution_reduce(w):
    out=[]
    for x in w:
        if out and out[-1]==x:out.pop()
        else:out.append(x)
    return tuple(out)
loops={'l0':(2,1),'l1':(0,2),'linfinity':(1,0)}
product=involution_reduce(loops['linfinity']+loops['l1']+loops['l0'])
assert product==()
even_pairs={(0,0):(),(1,1):(),(2,2):(),(2,1):('l0',),(1,2):('l0^-1',),(0,2):('l1',),(2,0):('l1^-1',),(1,0):('linfinity',),(0,1):('linfinity^-1',)}
out={'encoding':'Automorphisms act on F(l0,l1), l-infinity=l0^-1 l1^-1; right map acts first. In involution words, 0,1,2 denote tau0,tau1,tau-infinity.',
     'scope':'Checks the written product identities in the displayed automorphism model and the elementary parity-kernel generation argument. Does not independently prove the full extension presentation.',
     'automorphism_checks':checks,'fundamental_product_reduces_to_empty':product==(),
     'even_pair_expressions':[{'pair':k,'loop_expression':v} for k,v in even_pairs.items()]}
(E/'reader_reports/145_scan023_tau_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'automorphism_checks':len(checks),'all_equal':all(c['equal'] for c in checks),'fundamental_product_empty':product==()}))
