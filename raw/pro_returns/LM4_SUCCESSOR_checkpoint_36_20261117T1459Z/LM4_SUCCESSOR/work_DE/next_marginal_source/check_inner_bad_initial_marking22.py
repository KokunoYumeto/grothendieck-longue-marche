#!/usr/bin/env python3
"""Exact initial projection and lift margins for the inner regional comb."""
from pathlib import Path
import hashlib
import json
import sympy as S
from quadratic_pencil_braid import u, ROT, Q, I

q = Q(4, 5) + I/2
hs = [S.cancel((v*v+(1-2*v)*q)/(q+v*v-2*v)) for v in u[1:]]
ys = [S.Integer(0), q] + [S.cancel(h*h) for h in hs]
xs = [S.re(S.expand(ROT*y)) for y in ys]
order = sorted(range(6), key=lambda j: xs[j])
gaps = [S.cancel(xs[b]-xs[a]) for a,b in zip(order,order[1:])]
assert order == [2,0,5,3,4,1]
assert all(g > Q(1,100) for g in gaps)
assert all(S.re(h)>Q(1,4) and S.im(h)>Q(1,4) for h in hs)
assert all(S.im(S.expand(ROT*ys[j]))>Q(1,4) for j in (1,2,3,4,5))
out = {'status':'PASS', 'initial_physical_order':order,
       'all_adjacent_projection_gaps_greater_than':'1/100',
       'exact_adjacent_projection_gaps':[str(g) for g in gaps],
       'all_four_h_coordinates_greater_than':'1/4',
       'all_five_ordinary_projected_heights_greater_than':'1/4',
       'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Initial actual comb order and common square-root sheet; the uniform 10^-26 deformation bound is supplied by the full deformation audit.'}
Path(__file__).with_name('inner_bad_initial_marking22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact order [h1^2,cone0,h4^2,h2^2,h3^2,q]; all five gaps >1/100.')
print('PASS all h_i are first quadrant with both coordinates >1/4; all ordinary rotated heights >1/4.')
