#!/usr/bin/env python3
"""Universal free-word identities for the actual nonlinear comb section.

Formal U,A belong to the first free factor; V,B,X to the second.
No mixed commutation is imposed. Retained actions enter by substituting
tau_t(A),tau_beta(t)(B),tau_beta(t)(X), so these are uniform identities.
"""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2]
def r(w):
    z=[]
    for x in w:
        if z and z[-1]==-x:z.pop()
        else:z.append(x)
    return tuple(z)
def iv(w):return tuple(-x for x in reversed(w))
def m(*w):return r(x for v in w for x in v)
def comm(a,b):return m(a,b,iv(a),iv(b))
def conj(a,b):return m(a,b,iv(a))
U,A,V,B,X=(1,),(2,),(3,),(4,),(5,)
def c(a,b,x):return conj(b,comm(a,x))
records=[]
def check(name,left,right):
    assert r(left)==r(right),name
    records.append({'name':name,'left_word':left,'right_word':right,'reduced_word':r(left)})
started=time.monotonic()
check('positive_B_prefix',m(B,A,X),m(c(A,B,X),B,X,A))
check('negative_B_prefix',m(B,A,iv(X)),m(iv(c(A,m(B,iv(X)),X)),B,iv(X),A))
omega=conj(V,comm(U,B))
check('section_product_cocycle',m(V,U,B,A),m(omega,V,B,U,A))
check('uniform_nonlinear_coefficient_transport',conj(m(V,U),c(A,B,X)),
      conj(omega,m(c(m(U,A),m(V,B),X),iv(c(U,m(V,B),X)))))
# Here U plays b_A, A plays x_A, and B plays the entire a_B path.
check('involution_comb_transport',conj(U,comm(B,A)),
      m(comm(U,B),iv(comm(m(U,A),B))))
# Choose four symbols u_A,v_B,u_B,v_A, with F swapping1<->3,2<->4.
uA,vB,uB,vA=(1,),(2,),(3,),(4,)
eta=comm(vA,uB)
check('involution_section_defect',m(vA,uB),m(eta,uB,vA))
check('involution_defect_squared',m(comm(vB,uA),comm(uA,vB)),())
out={'scope':__doc__,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'records':records,'passed':len(records),
 'interpretation':'All equalities are literal in the free group. The same identities hold for arbitrary substituted factor words. Nonlinear coefficient lifts form a crossed action with omega, not a split G action.',
 'claims_excluded':['simultaneous free basis of the full node family','normal-closure decision or fixed lift'],
 'elapsed_seconds':time.monotonic()-started}
(ROOT/'work_CE/next_symmetric_nodes/nonlinear_comb_transport_identities.json').write_text(json.dumps(out,indent=2)+'\n')
for x in records:print('PASS',x['name'])
print('DONE seven universal nonlinear identities')
