#!/usr/bin/env python3
"""Exact four-strand generation in the joint higher Ferrari quotient.

Schreier generators of the kernel over the order648 E18 quotient
give its complete elementary-abelian image.  The same exact check
is performed on each of the 24 corrected braid triples.
"""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_degree4_lift import Combined,Span
import de_ferrari_class2_model as old

here=Path(__file__).resolve().parent

def image_order(H,generators):
    low=[tuple(int(x) for x in H.project(g)) for g in generators]
    representatives={old.one:0};queue=[old.one];lifts=[H.one];inverses=[H.one]
    span=Span(79)
    for i,q in enumerate(queue):
        for g,h in zip(generators,low):
            qn=old.mul(q,h);image=H.mul(lifts[i],g)
            k=representatives.get(qn)
            if k is None:
                representatives[qn]=len(queue);queue.append(qn);lifts.append(image);inverses.append(H.inv(image))
            else:
                residual=H.mul(image,inverses[k]);span.add(H.kernel_vector(residual),[])
    assert len(queue)==648
    return len(queue)*3**len(span.basis),span.matrix()

def main():
    start=time.time();H=Combined()
    target_order,target_kernel=image_order(H,(H.a,H.b,H.c))
    assert all(np.array_equal(H.power(g,9),H.one) for g in (H.a,H.b,H.c))
    print('Joint four-strand target order',target_order,'kernel dimension',target_kernel.shape[1],flush=True)
    records=json.loads(here.joinpath('de_ferrari_degree4_lift.json').read_text())['records'];rows=[]
    original_center3=H.power(H.mul(H.a,H.b),3)
    original_center4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    for rec in records:
        assert rec['simultaneous_lift_exists']
        values=H.word(rec['actual_F_commutator_word'])
        assert np.array_equal(H.pentagon(values),H.one)
        images=H.braid_images(values);H.check_braids(images)
        order,kernel=image_order(H,images)
        assert order==target_order
        span=Span(79)
        for v in kernel.T:span.add(v,[])
        for v in target_kernel.T:span.coordinates(v)
        aa,bb,cc=images
        assert np.array_equal(H.power(H.mul(aa,bb),3),original_center3)
        assert np.array_equal(H.power(H.mul(H.mul(aa,bb),cc),4),original_center4)
        row={'certificate_index':rec['certificate_index'],'missing_coset':rec['missing_coset'],
             'four_strand_image_order':order,'kernel_image_dimension':kernel.shape[1],
             'image_equals_actual_joint_target':True,
             'three_and_four_strand_full_twists_preserved':True}
        rows.append(row);print(json.dumps(row),flush=True)
    output={'joint_target_order':target_order,'kernel_over_E18_dimension':target_kernel.shape[1],
            'pure_normal_four_strand_quotient_order':24*target_order,
            'all_braid_generators_have_order_dividing9':True,
            'records':rows,'elapsed_seconds':round(time.time()-start,3),
            'pure_quotient_comparison':'The B4 image has cyclic odd abelianization, whereas every nontrivial quotient of S4 has a C2 abelian quotient. Goursat gives the direct joint product with S4.'}
    here.joinpath('de_ferrari_degree4_generation.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_degree4_generation_certificate.npz',target_kernel_basis=target_kernel)
    print(json.dumps({k:v for k,v in output.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
