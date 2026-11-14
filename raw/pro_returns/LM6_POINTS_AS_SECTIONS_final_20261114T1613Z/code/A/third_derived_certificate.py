"""Exact F_211 certificate for A:third-derived-obstruction.

No floating point arithmetic and no external packages are used. The proof
identifies the covers and Frobenius classes; this program certifies the
finite arithmetic, all cubic-root choices, and finite coset counts.
"""
from pathlib import Path
import json

q = 211
assert all(q % n for n in range(2, 15))
zeta, mu = 14, 55
assert zeta != 1 and pow(zeta, 3, q) == 1
assert mu != 1 and pow(mu, 5, q) == 1


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u and (y + v) % q == 0:
        return None
    slope = ((v-y) * pow(u-x, -1, q) if x != u
             else 3*x*x * pow(2*y, -1, q)) % q
    a = (slope*slope-x-u) % q
    return a, (slope*(x-a)-y) % q


def mul(n, P):
    out = None
    while n:
        if n & 1:
            out = add(out, P)
        P = add(P, P)
        n >>= 1
    return out


def cm(P):
    return None if P is None else (zeta*P[0] % q, P[1])


def fermat_cm(v):
    a, b = v
    return (b-a) % 5, -a % 5


def scalar(a, v):
    return tuple(a*x % 5 for x in v)


points = [None] + [(x, y) for x in range(q) for y in range(q)
                   if (y*y-x*x*x-16) % q == 0]
assert len(points) == 225
assert all(mul(15, P) is None for P in points)
E5 = [P for P in points if mul(5, P) is None]
assert len(E5) == 25
assert all(cm(P) in E5 for P in E5)
assert all(cm(P) != P for P in E5 if P is not None)
# pi=a+b*zeta has trace 2a-b=-13 and norm a^2-ab+b^2=211.
pi_options = [(a, b) for a in range(-30, 31) for b in range(-30, 31)
              if 2*a-b == -13 and a*a-a*b+b*b == q]
assert pi_options == [(-14, -15), (1, 15)]
P0, v0 = (2, 92), (3, 1)
assert P0 in E5 and P0 is not None
u0 = mul(2, P0)
J = {(mul(a, u0), scalar(a, v0)) for a in range(5)}
Jminus = {(mul(a, mul(4, u0)), scalar(a, v0)) for a in range(5)}
assert len(J) == len(Jminus) == 5
assert J.intersection(Jminus) == {(None, (0, 0))}


def fixed_cosets(delta, subgroup):
    # Nine complement coordinates each have 125 cosets in G/J.
    # Translation by delta fixes this entire group of cosets exactly
    # when the corresponding conjugate of delta belongs to J.
    P, v = delta
    total = 0
    for i in range(3):
        w = v
        for j in range(3):
            if (P, w) in subgroup:
                total += 125
            w = fermat_cm(w)
        P = cm(P)
    return total


for subgroup in (J, Jminus):
    conjugates = []
    for i in range(3):
        for j in range(3):
            transformed = set()
            for P, v in subgroup:
                for _ in range(i):
                    P = cm(P)
                for _ in range(j):
                    v = fermat_cm(v)
                transformed.add((P, v))
            conjugates.append(transformed)
    assert all(len(c) == 5 for c in conjugates)
    assert all(conjugates[i].intersection(conjugates[j]) == {(None, (0, 0))}
               for i in range(9) for j in range(i))
    assert len(set.union(*conjugates)) == 37

cubes = {}
for w in range(q):
    cubes.setdefault(pow(w, 3, q), []).append(w)
logs = {pow(mu, a, q): a for a in range(5)}
rows = []
no_cubic_lift = []
for t in range(2, q):
    c1, c2 = t*(t-1) % q, t*pow(t-1, -1, q) % q
    if c1 not in cubes or c2 not in cubes:
        no_cubic_lift.append(t)
        continue
    assert len(cubes[c1]) == len(cubes[c2]) == 3
    options = []
    for w1 in cubes[c1]:
        Q = (4*w1 % q, (8*t-4) % q)
        assert Q in points
        P = mul(9, Q)
        assert P in E5
        # pi-1=15*zeta^i; delta(Q)=3*zeta^i Q, conjugate to 2P.
        assert mul(3, Q) == mul(2, P)
        for w2 in cubes[c2]:
            r = (w2*zeta*zeta-zeta)*pow(w2-1, -1, q) % q
            assert r not in (0, q-1)
            assert (r-zeta)*pow(r-zeta*zeta, -1, q) % q == w2
            v = (logs[pow(r, 42, q)], logs[pow((-1-r) % q, 42, q)])
            delta = (mul(2, P), v)
            a, b = fixed_cosets(delta, J), fixed_cosets(delta, Jminus)
            options.append((a, b))
            assert (fixed_cosets((cm(delta[0]), v), J),
                    fixed_cosets((cm(delta[0]), v), Jminus)) == (a, b)
            assert delta != (None, (0, 0))
    assert len(set(options)) == 1
    w1, w2 = min(cubes[c1]), min(cubes[c2])
    Q = (4*w1 % q, (8*t-4) % q)
    P = mul(9, Q)
    r = (w2*zeta*zeta-zeta)*pow(w2-1, -1, q) % q
    v = (logs[pow(r, 42, q)], logs[pow((-1-r) % q, 42, q)])
    rows.append(dict(t=t, w1=w1, w2=w2, P=P, r=r, v=v,
                     fixed_J=options[0][0], fixed_Jminus=options[0][1]))

assert len(no_cubic_lift) == 185
assert len(rows) == 24
assert [r['t'] for r in rows if r['fixed_J']] == [12, 200]
assert all(r['fixed_J'] == 125 for r in rows if r['fixed_J'])
assert all(r['fixed_Jminus'] == 0 for r in rows)
counts = [sum(r[k] for r in rows) for k in ('fixed_J', 'fixed_Jminus')]
assert counts == [250, 0]
result = dict(status='all exact checks passed', q=q, zeta3=zeta, zeta5=mu,
              E_order=len(points), E5_order=len(E5), E_exponent=15,
              frobenius_pi_options=pi_options,
              P0=P0, u0=u0, fermat_generator=v0,
              group_order=5625, subgroup_order=5, cover_degree=1125,
              base_point_count=209, no_cubic_lift_count=len(no_cubic_lift),
              all_root_choices_checked=24*9, point_counts=counts, rows=rows)
Path(__file__).with_name('third_derived_certificate_output.json').write_text(
    json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'rows'}, indent=2))
