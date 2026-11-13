#!/usr/bin/env python3
"""Exact degree-six truncation and class-two-kernel comparison controls."""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_degree6_kernel import CombinedSix
from de_ferrari_degree5_kernel import CombinedFive
from de_ferrari_mod9_lift import Span

here=Path(__file__).resolve().parent
start=time.time();H=CombinedSix();old=CombinedFive()
rng=np.random.default_rng(226039)
generators=[H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c)]
oldgenerators=[old.a,old.b,old.c,old.inv(old.a),old.inv(old.b),old.inv(old.c)]
current=H.one;oldcurrent=old.one
for _ in range(400):
    k=int(rng.integers(6));current=H.mul(current,generators[k]);oldcurrent=old.mul(oldcurrent,oldgenerators[k])
    assert np.array_equal(H.to_old(current,old),oldcurrent)
    assert np.array_equal(H.to_old(H.inv(current),old),old.inv(oldcurrent))
    assert np.array_equal(H.mul(current,H.inv(current)),H.one)
xi1=H.mul(H.c,H.inv(H.a))
xi2=H.mul(H.mul(H.mul(H.mul(H.mul(H.a,H.b),H.a),H.inv(H.c)),H.inv(H.b)),H.inv(H.a))
c=H.comm(xi1,xi2)
kernels=[H.power(xi1,3),H.power(xi2,3),H.comm(xi1,c),H.comm(xi2,c),
    H.power(H.a,3),H.power(H.b,3),H.power(H.mul(H.a,H.b),6)]
for k in list(kernels):
    for g in (H.a,H.b,xi1,xi2):kernels.append(H.conj(g,k))
S=Span(367)
for a in kernels:
    assert np.array_equal(H.power(a,3),H.one)
    assert np.array_equal(H.exp_kernel(H.log_kernel(a)),a)
    S.add(H.log_kernel(a),[])
    for b in kernels:
        loga,logb=H.log_kernel(a),H.log_kernel(b)
        bracket=H.log_kernel(H.comm(a,b))
        assert np.array_equal(H.log_kernel(H.mul(a,b)),(loga+logb+2*bracket)%3)
derived=Span(367)
for a in kernels:
    for b in kernels:derived.add(H.log_kernel(H.comm(a,b)),[])
for c in derived.basis:
    for a in kernels:assert np.array_equal(H.comm(H.exp_kernel(c),a),H.one)
out={'exact_word_truncation_and_inverse_comparisons':400,
    'class_two_BCH_pair_checks':len(kernels)**2,'tested_actual_kernel_span_dimension':len(S.basis),
    'tested_derived_dimension':len(derived.basis),'third_commutators_zero':True,
    'all_actual_generator_cubes_zero':True,'elapsed_seconds':round(time.time()-start,3)}
here.joinpath('de_ferrari_degree6_model_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
