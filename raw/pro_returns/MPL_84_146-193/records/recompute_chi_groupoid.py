#!/usr/bin/env python3
"""Post-freeze local rank-one model for chi-trivialised extensions.

Not a transcription: this script verifies a proposed interpretation against
explicit identities. Requires SymPy; writes chi_groupoid_results.json here.
Objects are scalars t. An arrow a has source t and target t+chi*a.
Tensor product on arrows is (t,a)*(s,b) = (t*s,a*s+t*b+chi*a*b).
This establishes this local groupoid's laws, not descent or identification of
the two global manuscript products. No images or transcription files are read.
"""
from datetime import datetime, timezone
from itertools import product
from math import gcd
from pathlib import Path
import json
import sympy as s

chi,t,u,v,a,b,c,d,e=s.symbols('chi t u v a b c d e')
def h(t,a,u,b):
    return a*u+t*b+chi*a*b
identities={
 'target':(t+chi*a)*(u+chi*b)-(t*u+chi*h(t,a,u,b)),
 'identity_arrows':h(t,0,u,0),
 'composition':h(t,a,u,b)+h(t+chi*a,c,u+chi*b,d)-h(t,a+c,u,b+d),
 'associativity':h(t*u,h(t,a,u,b),v,c)-h(t,a,u*v,h(u,b,v,c)),
 'symmetry':h(t,a,u,b)-h(u,b,t,a),
 'left_unit':h(1,0,t,a)-a,
 'right_unit':h(t,a,1,0)-a,
}
for name,value in identities.items():
    assert s.expand(value)==0,name

# Matrix convention: new splitting vector is x'=x+a*ell.
P=s.Matrix([[chi,t],[0,0]])
V=s.Matrix([[0,-t],[0,chi]])
G=s.Matrix([[1,a],[0,1]])
assert P+V==chi*s.eye(2)
assert P*V==V*P==s.zeros(2)
assert G.inv()*P*G==P.subs(t,t+chi*a)
assert G.inv()*V*G==V.subs(t,t+chi*a)

finite=[]
for n in (2,3,4,6,8):
    for X in range(n):
        units=[]; automorphisms=[]
        for T in range(n):
            witnesses=[(U,A) for U,A in product(range(n),repeat=2) if (T*U+X*A-1)%n==0]
            invertible=bool(witnesses)
            assert invertible==(gcd(gcd(T,X),n)==1)
            if invertible:units.append(T)
            automorphisms.append(sum((X*A)%n==0 for A in range(n)))
        finite.append({'ring':f'Z/{n}Z','chi':X,'objects':n,'invertible_object_representatives':units,
                       'invertible_object_count':len(units),'automorphisms_per_object':automorphisms[0]})

report={
 'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'source_scans':[146,164,168,170],
 'status':'Our verified local model; not a proof of the full manuscript/Hua global categorical claim',
 'object':'t in R; pi=(chi,t), varpi=(-t,chi)^T',
 'arrows':'a:t -> t+chi*a; composition by addition',
 'object_product':'t*u',
 'arrow_product':'a*u+t*b+chi*a*b',
 'unit_object':1,
 'universal_identities':{k:str(s.expand(v)) for k,v in identities.items()},
 'matrix_identities_verified':['P+V=chi*I','P*V=V*P=0','P transforms by t->t+chi*a','V transforms by t->t+chi*a'],
 'invertibility_criterion':'t represents an invertible object iff t*u+chi*a=1 for some u,a, equivalently (t,chi)=R',
 'automorphism_group':'Ann_R(chi) under addition',
 'finite_examples':finite,
 'scope_limits':['Rank-one endpoints are locally trivialized and fixed; splittings exist in this local model.',
                  'The full scheme version requires descent and line-bundle bookkeeping.',
                  'The endpoint-preserving comparison with the pullback construction is a separate problem.',
                  'No novelty or historical priority claim.']
}
out=Path(__file__).with_name('chi_groupoid_results.json')
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'output':str(out),'symbolic_laws':len(identities),'finite_ring_chi_cases':len(finite),
                  'finite_object_cases':sum(r['objects'] for r in finite)}))
