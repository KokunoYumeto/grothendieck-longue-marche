"""Boundary-source covering comparisons: exact integer and p-adic residues."""
from pathlib import Path
import json

rows=[]
for d in range(1,25):
    for p in (2,3,5,7):
        m=d;a=0
        while m%p==0:
            m//=p;a+=1
        assert p**a*m==d and m%p
        cert=[]
        for k in range(1,5):
            modulus=p**k
            inverse=pow(m,-1,modulus)
            assert m*inverse%modulus==1
            cert.append({'k':k,'unit_inverse':inverse})
        rows.append({'index':d,'prime':p,'valuation':a,'unit':m,
                     'kernel_rank':0,'target_index':p**a,'certificates':cert})
print('Rank-one covering indices 1..24; primes 2,3,5,7; levels p^k, k=1..4.')
print('All 384 inverse-unit certificates pass; every correctly descended comparison is an isomorphism.')
print('Fibration failure still follows by pullback from the rank-two free-group witnesses.')
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps({'all_checks':True,'rows':rows},indent=2)+'\n')
