#!/usr/bin/env python3
"""Complete G_L factorization test for the literal signed common candidate.

All six induced central signs are retained above the actual 2124-point
base. This file never runs a legacy initializer and never infers a map
from a group order alone.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_sl2_5_source import Source
from de_ferrari_degree4_lift import InducedCombined
from de_lifted_schreier_kernel import lifted_kernel
from de_ferrari_two_core import Span2

HERE=Path(__file__).resolve().parent


class Joint:
    def __init__(self,W,H,letters):
        self.W,self.H=W,H
        self.id=np.arange(6,dtype=np.int64)
        self.one=(W.one,(self.id,np.full(6,H.sid,dtype=np.int64)))
        self.letters=letters
    def mul(self,a,b):
        p,v=a[1];q,w=b[1]
        return self.W.mul(a[0],b[0]),(q[p],self.H.sm[v,w[p]])
    def inv(self,a):
        p,v=a[1];q=np.argsort(p)
        return self.W.inv(a[0]),(q,self.H.si[v[q]])
    def conj(self,a,b):return self.mul(self.mul(a,b),self.inv(a))


def main():
    start=time.monotonic()
    names=['a_cm_signed_common_candidate.json','a_cm_signed_common_candidate.npz',
           'de_ferrari_sl2_5_source.json','de_ferrari_sl2_5_source.npz',
           'de_ferrari_a5_source_compressed.json','de_ferrari_a5_source_compressed.npz',
           'de_a6_gl_A5_factors.json','de_lifted_schreier_kernel.py',
           'de_ferrari_a6_source_data.py','de_ferrari_sl2_5_model.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    # Same read-only reconstruction already used in the independent P5
    # signed-source certificate; no runpy initializer is invoked.
    model=object.__new__(Source);model.d=load_data();model.H=FerrariSL2Five()
    model.W=InducedCombined(model.H,model.d)
    compression=json.loads((HERE/'de_ferrari_a5_source_compressed.json').read_text())
    model.keep=np.array([x for orbit in compression['retained_original_canonical_orders'] for x in orbit],dtype=np.int64)
    model.renumber=np.full(6840,-1,dtype=np.int64);model.renumber[model.keep]=np.arange(len(model.keep))
    model.points=[(0,0),(1,0),(0,1),(1,1)]
    W,H=model.W,model.H
    candidate=json.loads((HERE/'a_cm_signed_common_candidate.json').read_text())
    cp=np.load(HERE/'a_cm_signed_common_candidate.npz')
    factors=json.loads((HERE/'de_a6_gl_A5_factors.json').read_text())
    assert set(candidate['six_induced_A5_epikernel_indices']) <= set(factors['factoring_epikernel_indices'])
    signed=[]
    for j,label in enumerate(('s','r')):
        p=cp[label][:720]
        perm=np.array([int(p[120*k])//120 for k in range(6)],dtype=np.int64)
        vals=np.array([r['SL2_value'] for r in candidate['actual_B_transition_words_and_SL_values'][j]],dtype=np.int64)
        assert np.array_equal(p,np.concatenate([120*perm[k]+H.sm[:,vals[k]] for k in range(6)]))
        signed.append((perm,vals))
    J=Joint(W,H,signed)
    gs=[(W.letters[a],signed[j]) for j,a in enumerate((0,1))]
    old=json.loads((HERE/'de_ferrari_sl2_5_source.json').read_text())
    saved=np.load(HERE/'de_ferrari_sl2_5_source.npz')
    perms=[model.permutation(W.letters[a]) for a in (0,1)]
    assert all(np.array_equal(p.array_form,saved[k]) for p,k in zip(perms,('s','r')))
    def vector(a):
        p,v=a[1];assert np.array_equal(p,J.id)
        assert np.all((v==H.sid)|(v==H.z))
        return np.r_[model.vector(a[0]),v==H.z].astype(np.int64)
    def element(v):
        return model.element(v[:2052]),(J.id,np.where(v[2052:],H.z,H.sid))
    G,S,info=lifted_kernel(J,gs,perms,vector,element,2058,known_order=int(old['base_order']))
    expected=saved['full_kernel_basis'];P=Span2(2052)
    for j,v in enumerate(expected.T):P.add(v,j)
    assert len(P.basis)==44
    projected=Span2(2052)
    for j,v in enumerate(S.basis):P.coordinates(v[:2052]);projected.add(v[:2052],j)
    assert len(projected.basis)==44
    for v in expected.T:projected.coordinates(v)
    factors=len(S.basis)==44
    signmap=None
    if factors:
        C=Span2(2052)
        for j,v in enumerate(S.basis):C.add(v[:2052],j)
        raw=np.column_stack(S.basis)
        assert np.array_equal(C.matrix(),raw[:2052])
        signmap=np.column_stack([raw[2052:]@C.coordinates(v)%2 for v in expected.T])
        assert signmap.shape==(6,44)
    out={**info,'status':'PASS_COMPLETE_SIGNED_COMMON_GL_COMPARISON',
         'all_six_induced_central_signs_retained':True,
         'old_kernel_dimension':44,'joint_kernel_dimension':len(S.basis),
         'signed_induced_candidate_factors_through_G_L':factors,
         'old44_to_six_actual_signs':None if signmap is None else signmap.tolist(),
         'ordinary_Fab_mod30_comparison':'Already retained by the literal G_L abelianization and the existing Q30 map; the new computation tests every induced SL2 sign.',
         'factorization_through_X2_asserted':False,
         'input_sha256':hashes,'total_seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_signed_common_GL.npz',joint_kernel_basis=S.matrix(),
                        **({} if signmap is None else {'old44_to_six_signs':signmap}))
    (HERE/'a_cm_signed_common_GL.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in {'literal_word_DAG','kernel_basis_word_nodes','old44_to_six_actual_signs'}},indent=2),flush=True)


if __name__=='__main__':main()
