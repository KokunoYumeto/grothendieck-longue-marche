"""Independent fixed-coset certificate for the third-derived obstruction.

This uses the actual elliptic Kummer value 3Q, up to the common C3
rotation of Frobenius, rather than the first probe's normalized 9Q.
It counts membership of conjugates in J directly, without orbit keys.
The arithmetic and fundamental-group comparison is a separate proof.
"""
from pathlib import Path
import json

q = 211
zeta = 14
zeta5 = 55
assert pow(zeta, 3, q) == 1 and zeta != 1
assert pow(zeta5, 5, q) == 1 and zeta5 != 1

def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x, y = P
    u, v = Q
    if x == u and (y+v) % q == 0: return None
    slope = ((v-y)*pow(u-x, -1, q) if x != u
             else 3*x*x*pow(2*y, -1, q)) % q
    a = (slope*slope-x-u) % q
    return a, (slope*(x-a)-y) % q

def mul(n, P):
    R = None
    for _ in range(n): R = add(R, P)
    return R

def rotate(P):
    return None if P is None else (zeta*P[0] % q, P[1])

def turn(v):
    return ((v[1]-v[0]) % 5, -v[0] % 5)

def scale(a, v):
    return tuple(a*x % 5 for x in v)

points = [None] + [(x,y) for x in range(q) for y in range(q)
                  if (y*y-x*x*x-16) % q == 0]
E5 = [P for P in points if mul(5,P) is None]
assert len(points) == 225 and len(E5) == 25
assert all(mul(15,P) is None for P in points)
assert all(mul(3,P) == mul(2,mul(9,P)) for P in points)
P0 = (2,92)
assert P0 in E5
gen = (mul(2,P0), (3,1))
gen_minus = (mul(4,gen[0]), gen[1])

def subgroup(g):
    return {(mul(a,g[0]), scale(a,g[1])) for a in range(5)}

J = subgroup(gen)
Jminus = subgroup(gen_minus)
assert len(J) == len(Jminus) == 5 and J != Jminus

def fixed_cosets(g, H):
    # Translation coordinates of a conjugator have 25^2 choices.
    # Divide by |H|=5 to count right cosets, not conjugators.
    P, v = g
    matches = 0
    for _ in range(3):
        w = v
        for _ in range(3):
            matches += (P,w) in H
            w = turn(w)
        P = rotate(P)
    return 125*matches

fifth_logs = {pow(zeta5,a,q): a for a in range(5)}
cubes = {}
for x in range(q): cubes.setdefault(pow(x,3,q),x)
rows = []
for t in range(2,q):
    a = t*(t-1) % q
    b = t*pow(t-1,-1,q) % q
    if a not in cubes or b not in cubes:
        rows.append({'t':t,'cubic_quotient_nontrivial':True,
                     'J_fixed':0,'Jminus_fixed':0})
        continue
    w1,w2 = cubes[a],cubes[b]
    Q = (4*w1 % q,(8*t-4) % q)
    assert Q in points
    # Fr-1 = 15*zeta^i; delta_5(Q)=3*zeta^i Q.
    # The common zeta^i is among the conjugations counted below.
    delta = mul(3,Q)
    assert delta in E5
    r = (w2*zeta*zeta-zeta)*pow(w2-1,-1,q) % q
    v = (fifth_logs[pow(r,42,q)],
         fifth_logs[pow((-1-r) % q,42,q)])
    rows.append({'t':t,'elliptic_Kummer':delta,'Fermat_Kummer':v,
                 'J_fixed':fixed_cosets((delta,v),J),
                 'Jminus_fixed':fixed_cosets((delta,v),Jminus)})

counts = [sum(r[key] for r in rows) for key in ('J_fixed','Jminus_fixed')]
assert counts == [250,0]
assert [r['t'] for r in rows if r['J_fixed']] == [12,200]

out = {'field_order':q,'zeta3':zeta,'zeta5':zeta5,
       'elliptic_point_count':len(points),'rational_E5_size':len(E5),
       'elliptic_exponent_divides':15,
       'Frobenius_trace':q+1-len(points),
       'Frobenius_candidates':[[1,15],[-14,-15]],
       'Frobenius_basis':'a+b*zeta3',
       'deck_group_order':75*75,'J_order':len(J),
       'cover_degree':75*75//len(J),
       'J_generator':gen,'Jminus_generator':gen_minus,
       'affine_point_counts':counts,
       'nonzero_fibres':[r for r in rows if r['J_fixed'] or r['Jminus_fixed']],
       'all_fibre_counts':rows,
       'scope':'Exact finite-field and fixed-coset calculation. The arithmetic extension and third-derived comparisons require the accompanying proof.'}
Path(__file__).with_name('A_m3_independent_output.json').write_text(
    json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_fibre_counts'},indent=2))
