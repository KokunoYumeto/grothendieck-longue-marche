#!/usr/bin/env python3
"""Complete central-sign comparison of Q20 with the Ferrari SL2 source.

Q20=SL2(Z/20)/{+/-I} is retained as actual modular matrices.  Above
the already verified Ferrari A5 source, its only possible extra
coordinate is the scalar 9I.  All Schreier relators and their normal
closure are replayed jointly with the full 2052-dimensional ambient
Ferrari double-cover kernel.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json,time
import numpy as np
from sympy.combinatorics import Permutation
from de_ferrari_a6_source_data import load_data
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_sl2_5_source import Source
from de_ferrari_degree4_lift import InducedCombined
from de_lifted_schreier_kernel import lifted_kernel
from de_ferrari_two_core import Span2

HERE=Path(__file__).resolve().parent
ONE=(1,0,0,1)
CENTRAL=(9,0,0,9)
def canonical(a):return min(tuple(int(x)%20 for x in a),tuple(-int(x)%20 for x in a))
def matmul(a,b):
    A,B,C,D=a;e,f,g,h=b
    return canonical((A*e+B*g,A*f+B*h,C*e+D*g,C*f+D*h))
def matinv(a):
    A,B,C,D=a
    return canonical((D,-B,-C,A))
def value(w):
    s=(0,1,19,0);r=(0,19,1,19);r2=matmul(r,r)
    a=ONE
    for t in w:a=matmul(a,s if t==0 else r if t==1 else r2)
    return a

class Joint:
    def __init__(self,W):self.W=W;self.one=(W.one,ONE)
    def mul(self,a,b):return self.W.mul(a[0],b[0]),matmul(a[1],b[1])
    def inv(self,a):return self.W.inv(a[0]),matinv(a[1])
    def conj(self,a,b):return self.mul(self.mul(a,b),self.inv(a))

def main():
    started=time.time()
    names=['de_ferrari_sl2_5_source.json','de_ferrari_sl2_5_source.npz',
           'de_ferrari_a5_source_compressed.json','de_ferrari_a5_source_compressed.npz',
           'bc_symplectic_five_p5_residual.json','bc_symplectic_five_p5_modular.json',
           'de_ferrari_a6_source_data.py','de_lifted_schreier_kernel.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    # Reconstruct Source without the legacy runpy initializer.  In
    # particular this script never rewrites de_distribution_test outputs.
    model=object.__new__(Source);model.d=load_data();model.H=FerrariSL2Five()
    model.W=InducedCombined(model.H,model.d)
    compression=json.loads((HERE/'de_ferrari_a5_source_compressed.json').read_text())
    model.keep=np.array([x for orbit in compression['retained_original_canonical_orders'] for x in orbit],dtype=np.int64)
    model.renumber=np.full(6840,-1,dtype=np.int64);model.renumber[model.keep]=np.arange(len(model.keep))
    model.points=[(0,0),(1,0),(0,1),(1,1)]
    W,d=model.W,model.d
    qgens=[value([0]),value([1])]
    vals=[ONE];indices={ONE:0};parents=[-1];last=[-1]
    for at,a in enumerate(vals):
        for j,b in enumerate(qgens):
            c=matmul(a,b)
            if c not in indices:indices[c]=len(vals);vals.append(c);parents.append(at);last.append(j)
    assert len(vals)==2880
    fx,fy=value(d['xword']),value(d['yword'])
    fvals=[ONE];fset={ONE}
    for a in fvals:
        for b in (fx,fy):
            c=matmul(a,b)
            if c not in fset:fset.add(c);fvals.append(c)
    assert len(fvals)==480
    # The ordinary exponent sums mod2 and the signed mod5 matrix
    # reconstruct each F value.  The sign is fixed by its mod4 diagonal.
    def signed_F(a):
        A=np.array(a,dtype=np.int64).reshape(2,2)
        if int(A[0,0])%4==3:A=-A%20
        assert int(A[0,0])%4==int(A[1,1])%4==1
        assert int(A[0,1])%2==int(A[1,0])%2==0
        return tuple((A%5).ravel()),(int(A[0,1])//2%2,-int(A[1,0])//2%2)
    images={signed_F(a) for a in fvals};assert len(images)==120*4
    assert signed_F(fx)==((1,2,0,1),(1,0))
    assert signed_F(fy)==((1,0,3,1),(0,1))
    assert all(sum(1 if t==j else -1 if t==-j else 0 for t in d['fword'](w))%2==0
               for w in d['Nwords'] for j in (1,2))
    nvalues=[value(w) for w in d['Nwords']]
    nseen={ONE};nall=[ONE]
    for a in nall:
        for b in nvalues:
            c=matmul(a,b)
            if c not in nseen:nseen.add(c);nall.append(c)
    assert len(nall)==120
    old=json.loads((HERE/'de_ferrari_sl2_5_source.json').read_text())
    saved=np.load(HERE/'de_ferrari_sl2_5_source.npz')
    ps=[model.permutation(W.letters[t]) for t in (0,1)]
    assert np.array_equal(ps[0].array_form,saved['s'])
    assert np.array_equal(ps[1].array_form,saved['r'])
    joint=Joint(W);gs=[(W.letters[t],qgens[i]) for i,t in enumerate((0,1))]
    def vector(a):
        assert a[1] in (ONE,CENTRAL),('unexpected central value',a[1])
        return np.r_[model.vector(a[0]),int(a[1]==CENTRAL)]
    def element(v):return model.element(v[:-1]),CENTRAL if v[-1]%2 else ONE
    G,S,info=lifted_kernel(joint,gs,ps,vector,element,2053,known_order=int(old['base_order']))
    expected=saved['full_kernel_basis'];P=Span2(2052)
    for j,v in enumerate(expected.T):P.add(v,j)
    assert len(P.basis)==44
    for v in S.basis:P.coordinates(v[:-1])
    projected=Span2(2052)
    for j,v in enumerate(S.basis):projected.add(v[:-1],j)
    assert len(projected.basis)==44
    for v in expected.T:projected.coordinates(v)
    assert len(S.basis) in (44,45)
    factors=len(S.basis)==44
    signs=None
    if factors:
        # A square 44-column coordinate system in the actual old kernel.
        C=Span2(2052)
        for j,v in enumerate(S.basis):C.add(v[:-1],j)
        assert len(C.basis)==44
        raw=np.column_stack(S.basis)
        # Span2.add retains the supplied column, so its coordinate map
        # applies directly to raw, including the final central row.
        assert np.array_equal(C.matrix(),raw[:-1])
        signs=np.array([int(raw[-1]@C.coordinates(v)%2) for v in expected.T])
        assert len(signs)==44
    out={**info,'status':'PASS_COMPLETE_P5_SIGNED_COMPARISON',
         'Q20_order':2880,'Q20_F_image_order':480,'Q20_N_image_order':120,
         'Q20_F_image':'SL2(F5) x C2^2 with the printed signed coordinate map',
         'Q20_central_scalar_over_Q4_and_Q5':list(CENTRAL),
         'Q20_kernel_in_prime5_source_order':3125,
         'Q20_kernel_in_prime5_source':'O5(N)=(C5)^5',
         'old_kernel_dimension':44,'joint_kernel_dimension':len(S.basis),
         'Q20_factors_through_G_L':factors,
         'central_sign_on_old44_kernel_columns':None if signs is None else signs.tolist(),
         'input_sha256':hashes,'total_seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p5_signed'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    arrays={'joint_kernel_basis':S.matrix(),'Q20_elements':np.array(vals),
            'Q20_parents':np.array(parents),'Q20_last':np.array(last),
            'Q20_F_elements':np.array(fvals),'Q20_N_elements':np.array(nall)}
    if signs is not None:arrays['old44_signs']=signs
    np.savez_compressed(target.with_suffix('.npz'),**arrays)
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in
        ('input_sha256','literal_word_DAG','kernel_basis_word_nodes')},indent=2),flush=True)

if __name__=='__main__':main()
