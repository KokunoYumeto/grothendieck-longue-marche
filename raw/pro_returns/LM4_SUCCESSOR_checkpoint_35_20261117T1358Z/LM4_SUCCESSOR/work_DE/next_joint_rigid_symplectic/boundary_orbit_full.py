"""Exact boundary-normal-closure action for the actual full theta5 map.

Exploration after B68: this records the affine vertex action on the free
normal-closure basis modulo its commutator group.  It does not infer
injectivity or an induced profinite topology from that module.
"""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import reduce_word as red,inverse as inv,multiply as mul,substitute as sub,artin
j=json.loads((HERE/'cyclic_rigid_braid_words.json').read_text())
tau=(3,4,5)
braids={r['index']+1:mul(inv(tau),r['braid'],tau) for r in j['basis']}
B=(1,2,3,4,5);q=(3,5)
def extract(A):
    v=list(A[-1]);a=[]
    while len(v)>1:
        assert v[0]==-v[-1]
        a.append(v.pop(0));v.pop()
    assert v==[6]
    return red(x for x in a if abs(x)!=6)
quot={i:(i,) for i in range(1,5)};quot[5]=(-4,-3,-2,-1)
records={}
for i,b in braids.items():
    A=artin(b,6);Q=extract(A)
    D={k:red(x for x in A[k-1] if abs(x)!=6) for k in range(1,6)}
    alpha={k:mul(inv(Q),D[k],Q) for k in range(1,6)}
    assert sub(B,alpha)==mul(inv(Q),B,Q)
    # Conjugate the fiber identification by q^-1, so f1 maps exactly to B.
    alpha0={k:mul(inv(q),sub(mul(q,(k,),inv(q)),alpha),q) for k in range(1,6)}
    R=mul(inv(q),sub(q,alpha),inv(Q))
    assert sub(B,alpha0)==mul(R,B,inv(R))
    beta={k:sub(alpha0[k],quot) for k in range(1,5)}
    rho=sub(R,quot)
    if i==2:
        assert Q==mul(q,inv(B),inv(q))
        assert all(alpha0[k]==mul(B,(k,),inv(B)) for k in range(1,6))
        assert not rho and beta=={k:(k,) for k in range(1,5)}
    records[i]={'source_index':i,'braid':b,'fiber_conjugator':Q,'normalized_action':alpha0,
                'boundary_conjugator':R,'quotient_action':beta,'affine_vertex':rho}
    print('source f'+str(i-1),'affine vertex',rho,'; action lengths',[len(beta[k]) for k in range(1,5)],flush=True)
print('f1 becomes the literal peripheral basis element B; its quotient action and vertex are trivial: PASS')
print('Every normalized action sends B to R B R^-1; all quotient actions/vertices saved exactly: PASS')
(HERE/'full_boundary_orbit_action.json').write_text(json.dumps({
    'fiber_basis':list(range(1,6)),'boundary':B,'normalizing_conjugator':q,'quotient':quot,
    'records':records,'affine_action_convention':'v -> beta_g(v) rho_g; rho_gh=beta_g(rho_h)rho_g',
    'scope':'Action on the normal-closure abelianization only; no source injection or profinite comparison asserted'
},indent=2)+'\n')
