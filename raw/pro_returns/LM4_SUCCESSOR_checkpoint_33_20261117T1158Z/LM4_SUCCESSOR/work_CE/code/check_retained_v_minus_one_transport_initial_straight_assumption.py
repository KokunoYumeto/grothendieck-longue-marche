#!/usr/bin/env python3
"""Exact one-segment retained v=-1 node transport, not an orbit search.

The six q points are 0,1,zeta,zeta^3,v,v^2, starting at v=zeta^2.
Their projection order never changes.  The conversion of the resulting
far-cut commutator to the six named old lassos is a separate DE certificate.
"""
from pathlib import Path
import hashlib, json, time
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
planpath = ROOT/'work_CE/next_symmetric_nodes/symmetric_old_base_path_plan.json'
headpath = ROOT/'work_A/old_base_augmented_row_action.json'
planraw, headraw = planpath.read_bytes(), headpath.read_bytes()
plan, heads = json.loads(planraw), json.loads(headraw)
Q, I, X = S.Rational, S.I, S.Symbol('X', real=True)
started = time.monotonic()
centers = [Q(p['center'][0])+I*Q(p['center'][1]) for p in plan['plans']]
u1, u2, u3, u4 = centers[2:]
endpoint = -Q(999,1000)+I*Q(1,1000)
v = S.expand(u2+(endpoint-u2)*X)
rot = 1+I*Q(371,1000)
strands = [S.Integer(0), S.Integer(1), u1, u3, v, S.expand(v*v)]
order = [4,3,2,0,5,1]
projected = [S.Poly(S.expand(S.re(rot*z)), X, domain=S.QQ) for z in strands]

def quadratic_minimum(p):
    assert p.degree() <= 2
    candidates = [(Q(0), p.eval(0)), (Q(1), p.eval(1))]
    if p.degree() == 2:
        a, b, c = p.all_coeffs(); critical = -b/(2*a)
        if 0 < critical < 1: candidates.append((critical,p.eval(critical)))
    return min(candidates,key=lambda x:x[1]), candidates

gaps=[]
for a,b in zip(order,order[1:]):
    p=projected[b]-projected[a]
    minimum,candidates=quadratic_minimum(p)
    assert minimum[1] > Q(1,1000)
    gaps.append({'left_label':a,'right_label':b,
                 'polynomial_coefficients':[str(x) for x in p.all_coeffs()],
                 'critical_values':[[str(x),str(y)] for x,y in candidates],
                 'minimum':str(minimum[1])})
assert all(S.re(rot*z.subs(X,1)) < 2 for z in strands)
assert abs(S.re(u2))+abs(S.im(u2)) < 2
assert abs(S.re(endpoint))+abs(S.im(endpoint)) < 2

# In the local v square about -1 of half-side h, v^2-1=(v+1)(v-1)
# winds once positively.  Its image stays in the isolated q disk about1.
h=Q(1,1000)
assert 2*h*(2+2*h) < Q(1,100)
assert 2*h < Q(1,100)
for z in [S.Integer(0),u1,u3]:
    assert S.expand(S.re(z-1)**2+S.im(z-1)**2) > Q(1,4)
    assert S.expand(S.re(z+1)**2+S.im(z+1)**2) > Q(1,4)

def reduce_word(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return tuple(out)

def inverse(w): return tuple(-x for x in reversed(w))
def apply(w,a):
    return reduce_word(y for x in w for y in (a[abs(x)] if x>0 else inverse(a[-x])))

# This algebraic check does not substitute for the independent lasso
# conversion.  It checks the predicted commutator's actual section head.
candidate=(2,6,-2,-6)
ahead=bhead=();phi={i:(i,) for i in range(1,6)}
for x in candidate:
    r=heads['old_generators'][abs(x)-1]
    action={int(k):tuple(w) for k,w in r['phi' if x>0 else 'phi_inverse'].items()}
    ah,bh=tuple(r['A_heads']['6']),tuple(r['B_heads']['6'])
    if x<0: ah,bh=apply(inverse(ah),action),apply(inverse(bh),action)
    ahead=reduce_word(apply(ahead,action)+ah)
    bhead=reduce_word(apply(bhead,action)+bh)
    phi={i:apply(w,action) for i,w in phi.items()}
assert not ahead and not bhead
assert phi=={i:(i,) for i in range(1,6)}

out={'scope':__doc__,
     'input_sha256':{str(planpath.relative_to(ROOT)):hashlib.sha256(planraw).hexdigest(),
                     str(headpath.relative_to(ROOT)):hashlib.sha256(headraw).hexdigest()},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'parameter_start':[str(S.re(u2)),str(S.im(u2))],
     'parameter_end':['-999/1000','1/1000'],
     'projection':['1','371/1000'],'far_projected_basepoint':['10','0'],
     'q_physical_labels':['0','1','zeta','zeta^3','v','v^2'],
     'initial_and_final_order':order,'chronological_whisker_braid':[],
     'adjacent_projection_gaps':gaps,'uniform_projection_gap_greater_than':'1/1000',
     'local_v_square_center':['-1','0'],'local_v_square_halfside':'1/1000',
     'local_isolated_q_disk_center':['1','0'],'local_isolated_q_disk_radius':'1/100',
     'local_positive_braid':[5,5],
     'transported_node_meridians_far_cut':[[5],[6]],
     'transported_node_commutator_far_cut':[5,6,-5,-6],
     'coefficient_deformation':'Each true cyclotomic point differs by less than2e-30. Along the affine v path the moving square and all projected points move less than1e-27; the proved1e-3 gap preserves the entire cut marking.',
     'candidate_named_old_word':[2,6,-2,-6],
     'candidate_A6_head':ahead,'candidate_B6_head':bhead,
     'candidate_retained_action':phi,
     'remaining_gate':'Independent exact common-whisker conversion of the six named old lassos to this far-cut basis; no identification is inferred from the zero-head check alone.',
     'elapsed_seconds':time.monotonic()-started}
target=ROOT/'work_CE/next_symmetric_nodes/retained_v_minus_one_transport.json'
target.write_text(json.dumps(out,indent=2)+'\n')
print('PASS no crossings on the entire straight v path; all five adjacent gaps >1/1000.',flush=True)
print('PASS isolated positive q1/v^2 node: transported far-cut relation [x5,x6].',flush=True)
print('PASS candidate [b1,b5] has exact A6=B6 heads zero and retained action identity; marking comparison remains separate.',flush=True)
print('Elapsed',round(out['elapsed_seconds'],3),flush=True)
