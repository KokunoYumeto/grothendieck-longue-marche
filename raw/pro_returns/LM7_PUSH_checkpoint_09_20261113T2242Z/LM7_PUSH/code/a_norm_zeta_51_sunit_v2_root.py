#!/usr/bin/env python3
"""Larger exact cyclic-basis search following the retained bounded failure.

Searches coefficient boxes2 and3 for a basis yielding a norm-zeta
element integral away from3. Only an exact witness is positive evidence.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
from math import lcm
import io,json,runpy,time

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    d=runpy.run_path(str(here/'a_norm_zeta_51_dual_root.py'))
K,T,emul,zeta,zero,one=(d[k] for k in ('K','T','emul','zeta','zero','one'))
def det(cols):
    a,b,c=cols
    return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])

attempts=0;witnesses=[];summaries=[];start=time.time()
for bound in (2,3):
    vals=list(range(-bound,bound+1))
    for raw in product(vals,repeat=6):
        if max(map(abs,raw))!=bound:continue
        # Multiplication by a scalar sign gives the same delta.
        if next(x for x in raw if x)<0:continue
        attempts+=1
        v0=[K(raw[2*i],raw[2*i+1]) for i in range(3)]
        cols=[v0,T(v0),T(T(v0))]
        determinant=det(cols);assert determinant
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
        witnesses.append(row);print(json.dumps(row),flush=True);break
    summaries.append({'bound':bound,'cumulative_attempts':attempts,
                      'seconds':round(time.time()-start,3),'found':bool(witnesses)})
    print(json.dumps(summaries[-1]),flush=True)
    if witnesses:break
out={'attempted_basis_vectors':attempts,'box_summaries':summaries,'witnesses':witnesses,
     'status':'PASS_EXACT_SUNIT_NORM_ZETA' if witnesses else 'NO_WITNESS_IN_BOUNDED_BASIS_SEARCH'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],flush=True)
