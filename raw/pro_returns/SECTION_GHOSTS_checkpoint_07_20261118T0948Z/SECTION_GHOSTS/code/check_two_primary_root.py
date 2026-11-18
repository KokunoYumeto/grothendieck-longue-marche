"""Exact finite checks of the marked cyclic-root gluing in E.170."""
import json
from pathlib import Path

records=[]
total=0
for H in range(3,10):
    n=2**H
    translations=set(range(0,n,2))
    expected=set(range(0,n,8))
    tested=0
    for chi in range(5,n,8):
        image={(1-chi)*a%n for a in translations}
        assert image==expected
        # The affine map v |-> chi*v+b has a fixed conjugate root
        # through an allowed even translation exactly when b is 0 mod8.
        for b in range(0,n,2):
            solved=next((a for a in translations if (b+(1-chi)*a)%n==0),None)
            assert (solved is not None)==(b%8==0)
            if solved is not None:
                assert (b+(1-chi)*solved)%8==0
            tested+=1
        # A fourth-root mark sees b=4 as trivial, but it is not repairable.
        assert 4%4==0 and 4 not in image
    total+=tested
    records.append({'H':H,'modulus':n,'scalars':n//8,
                    'affine_parameters':tested,
                    'conjugation_image':'multiples of 8',
                    'fourth_root_counterexample_translation':4})
out={'result':'PASS','total_affine_parameters':total,'records':records,
     'scope':'Finite cyclic-root conjugation certificate; arithmetic field statements are proved in E.170.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
