#!/usr/bin/env python3
"""Entire degree-six joint target and actual four-strand generation."""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_degree6_kernel import CombinedSix
from de_ferrari_mod9_lift import Span
import de_ferrari_class2_model as old

here=Path(__file__).resolve().parent

def schreier_image(H,generators):
    low=[tuple(int(t) for t in H.project(g)) for g in generators]
    seen={old.one:0};queue=[old.one];lifts=[H.one];inverses=[H.one];S=Span(367)
    for i,q in enumerate(queue):
        for g,h in zip(generators,low):
            qn=old.mul(q,h);image=H.mul(lifts[i],g);j=seen.get(qn)
            if j is None:
                seen[qn]=len(queue);queue.append(qn);lifts.append(image);inverses.append(H.inv(image))
            else:S.add(H.log_kernel(H.mul(image,inverses[j])),[])
    assert len(queue)==648
    before=len(S.basis);at=0
    while at<len(S.basis):
        a=H.exp_kernel(S.basis[at])
        for v in list(S.basis):S.add(H.log_kernel(H.comm(a,H.exp_kernel(v))),[])
        at+=1
    return 648*3**len(S.basis),S,before

def main():
    start=time.time();H=CombinedSix();order,target,initial=schreier_image(H,(H.a,H.b,H.c))
    derived=Span(367)
    for a in target.basis:
        ea=H.exp_kernel(a);assert np.array_equal(H.power(ea,3),H.one)
        for b in target.basis:derived.add(H.log_kernel(H.comm(ea,H.exp_kernel(b))),[])
    for c in derived.basis:
        for a in target.basis:assert np.array_equal(H.comm(H.exp_kernel(c),H.exp_kernel(a)),H.one)
    rng=np.random.default_rng(226031);M=target.matrix()
    for _ in range(100):
        a=M@rng.integers(0,3,size=len(target.basis))%3;b=M@rng.integers(0,3,size=len(target.basis))%3
        ea,eb=H.exp_kernel(a),H.exp_kernel(b);bracket=H.log_kernel(H.comm(ea,eb))
        assert np.array_equal(H.log_kernel(H.mul(ea,eb)),(a+b+2*bracket)%3)
    assert all(np.array_equal(H.power(a,9),H.one) for a in (H.a,H.b,H.c))
    print(json.dumps({'joint_target_order':order,'kernel_Lie_dimension':len(target.basis),
        'kernel_commutator_dimension':len(derived.basis),'initial_Schreier_log_span_dimension':initial}),flush=True)
    data=json.loads(here.joinpath('de_ferrari_degree6_lift.json').read_text())['records']
    center3=H.power(H.mul(H.a,H.b),3);center4=H.power(H.mul(H.mul(H.a,H.b),H.c),4);rows=[]
    for rec in data:
        witness=rec['chosen_witness']
        if witness is None:continue
        images=[H.decode(x) for x in witness['actual_braid_images']];H.check_braids(images)
        neworder,image,_=schreier_image(H,images);assert neworder==order
        for v in target.basis:image.coordinates(v)
        a,b,c=images
        assert np.array_equal(H.power(H.mul(a,b),3),center3)
        assert np.array_equal(H.power(H.mul(H.mul(a,b),c),4),center4)
        row={'certificate_index':rec['certificate_index'],'missing_coset':rec['missing_coset'],
            'four_strand_image_order':neworder,'source_kernel_generation_rank':witness['source_kernel_generation_rank'],
            'actual_full_target_generated':True,'both_full_twists_preserved':True}
        rows.append(row);print(json.dumps(row),flush=True)
    output={'joint_target_order':order,'kernel_over_E18_Lie_dimension':len(target.basis),
        'kernel_over_E18_commutator_dimension':len(derived.basis),
        'pure_normal_four_strand_quotient_order':24*order,'surviving_records':rows,
        'elapsed_seconds':round(time.time()-start,3),
        'scope':'Complete Schreier image over E18 and exact class-two exponent3 kernel through degree6; actual source maps and full twists retained.'}
    here.joinpath('de_ferrari_degree6_generation.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_degree6_generation_certificate.npz',
        target_kernel_Lie_basis=target.matrix(),target_kernel_commutator_basis=derived.matrix())
    print(json.dumps({k:v for k,v in output.items() if k!='surviving_records'},indent=2),flush=True)

if __name__=='__main__':main()
