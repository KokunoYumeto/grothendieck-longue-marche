#!/usr/bin/env python3
"""Choose a cyclic basis giving an S-unit norm-zeta witness at51.

The first dual-algebra basis gave a denominator2 and therefore is not
asserted to define an extension unramified away from3 and17. Search
actual basis vectors, checking that the resulting beta coefficients
have only powers of3 in their denominators. Each output norm is exact.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
from math import lcm
import io,json,runpy

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    d=runpy.run_path(str(here/'a_norm_zeta_51_dual_root.py'))
K,T,emul,zeta,zero,one=(d[k] for k in ('K','T','emul','zeta','zero','one'))

def det(cols):
    a,b,c=cols
    return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])

choices=[K(a,b) for a,b in product(range(-1,2),repeat=2)]
witnesses=[]
attempts=0
for v0 in product(choices,repeat=3):
    if not any(v0):continue
    attempts+=1
    cols=[list(v0),T(v0),T(T(v0))]
    determinant=det(cols)
    assert determinant
    rhs=emul([zero,one,zero],v0)
    delta=[]
    for i in range(3):
        cc=cols.copy();cc[i]=rhs
        delta.append(det(cc)/determinant)
    den=lcm(*(q.denominator for x in delta for q in (x.a,x.b)))
    remaining=den
    while remaining%3==0:remaining//=3
    if remaining!=1:continue
    a,b,c=delta
    assert a**3+51*b**3+51**2*c**3-153*a*b*c==zeta
    assert [sum((cols[j][i]*delta[j] for j in range(3)),zero) for i in range(3)]==rhs
    row={'cyclic_basis_vector':[x.encode() for x in v0],
         'basis_determinant':determinant.encode(),
         'delta_in_K_beta_beta3_equals51':[x.encode() for x in delta],
         'common_denominator':den,'norm_delta':zeta.encode(),
         'integral_away_from_three':True}
    witnesses.append(row)
    print(json.dumps(row),flush=True)
    break
out={'attempted_nonzero_basis_vectors':attempts,'witnesses':witnesses,
     'status':'PASS_EXACT_SUNIT_NORM_ZETA' if witnesses else 'NO_WITNESS_IN_BOUNDED_BASIS_SEARCH'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}),flush=True)
