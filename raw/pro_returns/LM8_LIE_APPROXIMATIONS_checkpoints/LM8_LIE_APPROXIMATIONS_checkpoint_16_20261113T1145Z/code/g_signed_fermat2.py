"""Exact integral q_2 cocycle model and the characteristic-two lift obstruction.

Only standard-library arithmetic is used.  Integer matrices certify every word
identification; Schreier rewriting computes the integral rank-five lattice.
No rational completion is base-changed to characteristic two.
"""
from collections import deque
from fractions import Fraction
from functools import reduce
from itertools import product
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent


def mm(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return tuple(tuple(sum(a[i][q]*b[q][j] for q in range(k))
                       for j in range(m)) for i in range(n))


def mv(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def va(*vs):
    return tuple(map(sum, zip(*vs)))


def neg(v):
    return tuple(-x for x in v)


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def transpose(a):
    return tuple(map(tuple, zip(*a)))


def mat2(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def inverse2(a):
    assert a[0]*a[3]-a[1]*a[2] == 1
    return (a[3], -a[1], -a[2], a[0])


def reduce_word(w):
    ans = []
    for a in w:
        if ans and ans[-1] == -a:
            ans.pop()
        else:
            ans.append(a)
    return tuple(ans)


def wi(w):
    return tuple(-a for a in reversed(w))


I2 = (1, 0, 0, 1)
rho = (0, 1, -1, 1)
sigma = (0, -1, 1, 0)
CG = {1: rho, -1: inverse2(rho), 2: sigma, -2: inverse2(sigma)}


def cmatrix(w):
    a = I2
    for g in w:
        a = mat2(a, CG[g])
    return a


# omega=rho^3, x=omega(sigma rho)^2, y=omega(rho sigma)^2.
x_c = (1, 1, 1, 2, 1, 2, 1)
y_c = (1, 1, 1, 1, 2, 1, 2)
xmat, ymat = cmatrix(x_c), cmatrix(y_c)
FG = {1: xmat, -1: inverse2(xmat), 2: ymat, -2: inverse2(ymat)}


def fmatrix(w):
    a = I2
    for g in w:
        a = mat2(a, FG[g])
    return a


def mod4(a):
    return tuple(v % 4 for v in a)


def m4(a, b):
    return mod4(mat2(a, b))


V4 = {I2}
queue = [I2]
for a in queue:
    for g in (mod4(xmat), mod4(ymat)):
        b = m4(a, g)
        if b not in V4:
            V4.add(b)
            queue.append(b)
assert len(V4) == 4


def h12(a):
    return min(m4(v, mod4(a)) for v in V4)


# Deterministic actual group representatives in both finite quotients.
def representatives(key):
    ans = {key(I2): ()}
    todo = list(ans)
    for a in todo:
        for g in (1, 2):
            w = ans[a] + (g,)
            b = key(cmatrix(w))
            if b not in ans:
                ans[b] = w
                todo.append(b)
    return ans


reps12 = representatives(h12)
reps48 = representatives(mod4)
assert len(reps12) == 12 and len(reps48) == 48
keys12, keys48 = list(reps12), list(reps48)
idx12 = {h: i for i, h in enumerate(keys12)}
idx48 = {h: i for i, h in enumerate(keys48)}

# Express the finitely many Schreier edges for Pi_0 in the free basis x,y.
needed = {}
for h, t in reps12.items():
    for g in (1, -1, 2, -2):
        nxt = h12(cmatrix(t+(g,)))
        w = t+(g,)+wi(reps12[nxt])
        needed[cmatrix(w)] = None
found = {I2: ()}
front = deque([(I2, ())])
while any(needed[a] is None for a in needed):
    a, w = front.popleft()
    if a in needed:
        needed[a] = w
    assert len(w) <= 10, "Unexpectedly long finite Schreier certificate"
    for g in (1, -1, 2, -2):
        if w and w[-1] == -g:
            continue
        b = mat2(a, FG[g])
        if b not in found:
            found[b] = w+(g,)
            front.append((b, w+(g,)))
edge12 = {}
for h, t in reps12.items():
    for g in (1, -1, 2, -2):
        nxt = h12(cmatrix(t+(g,)))
        mat = cmatrix(t+(g,)+wi(reps12[nxt]))
        edge12[h, g] = (nxt, needed[mat])
        assert fmatrix(needed[mat]) == mat


def c_to_f(w):
    h, out = h12(I2), ()
    for g in w:
        h, piece = edge12[h, g]
        out = reduce_word(out+piece)
    assert h == h12(I2), "Word is not in Pi_0"
    assert fmatrix(out) == cmatrix(w)
    return out


H4 = [(0, 0), (1, 0), (0, 1), (1, 1)]
trans4 = {(0, 0): (), (1, 0): (1,), (0, 1): (2,), (1, 1): (1, 2)}


def h4_step(h, g):
    z = list(h)
    z[abs(g)-1] ^= 1
    return tuple(z)


kbasis, kedge = [], {}
for h in H4:
    for g in (1, 2):
        k = h4_step(h, g)
        w = reduce_word(trans4[h]+(g,)+wi(trans4[k]))
        if w:
            kedge[h, g] = len(kbasis)
            kbasis.append(w)
assert len(kbasis) == 5


def schreier(w):
    h, v = (0, 0), [0]*5
    for g in w:
        k = h4_step(h, g)
        e, sign = ((h, g), 1) if g > 0 else ((k, -g), -1)
        if e in kedge:
            v[kedge[e]] += sign
        h = k
    assert h == (0, 0), "Word is not in K"
    return tuple(v)


def substitute(w, images):
    return reduce_word(sum((images[g] if g > 0 else wi(images[-g])
                            for g in w), ()))


Rfree, Sfree = {1: (2,), 2: (-1, -2)}, {1: (2,), 2: (1,)}
TauFree = {1: (-1,), 2: (-2,)}
AR = transpose(tuple(schreier(substitute(w, Rfree)) for w in kbasis))
AS = transpose(tuple(schreier(substitute(w, Sfree)) for w in kbasis))
AT = transpose(tuple(schreier(substitute(w, TauFree)) for w in kbasis))
I5 = eye(5)
assert mm(mm(AR, AR), AR) == I5 and mm(AS, AS) == I5
assert mm(AT, AT) == I5
assert mm(mm(AT, AR), AT) == mm(mm(AS, mm(AR, AR)), AS)
assert mm(mm(AT, AS), AT) == AS


def action48(w):
    a = I5
    for g in w:
        a = mm(a, AR if g == 1 else AS)
    return a


actions48 = [action48(reps48[h]) for h in keys48]
R = ((0, -1), (1, -1))
S = ((0, 1), (1, 0))


def action12(w):
    a = eye(2)
    for g in w:
        a = mm(a, R if g == 1 else S)
    return a


actions12 = [action12(reps12[h]) for h in keys12]


def abelian(w):
    return (sum((1 if g > 0 else -1) for g in w if abs(g) == 1),
            sum((1 if g > 0 else -1) for g in w if abs(g) == 2))


J = transpose(tuple(abelian(w) for w in kbasis))
assert all(x % 2 == 0 for row in J for x in row)
assert (2, 0) in transpose(J) and (0, 2) in transpose(J)
assert mm(J, AR) == mm(R, J) and mm(J, AS) == mm(S, J)


def extension_data(keys, reps, idx, key, coords):
    mult, coc = [], []
    for h in keys:
        row, crow = [], []
        for k in keys:
            hk = key(mat2(cmatrix(reps[h]), cmatrix(reps[k])))
            row.append(idx[hk])
            w = reps[h]+reps[k]+wi(reps[hk])
            crow.append(coords(c_to_f(w)))
        mult.append(row)
        coc.append(crow)
    return mult, coc


mul48, coc48 = extension_data(keys48, reps48, idx48, mod4, schreier)
mul12, coc12 = extension_data(keys12, reps12, idx12, h12, abelian)
projection = []
for h in keys48:
    q = h12(cmatrix(reps48[h]))
    shift = abelian(c_to_f(reps48[h]+wi(reps12[q])))
    projection.append((idx12[q], shift))

for h, k in product(range(48), repeat=2):
    hk = mul48[h][k]
    assert mm(actions48[h], actions48[k]) == actions48[hk]
    ph, mh = projection[h]
    pk, mk = projection[k]
    phk, mhk = projection[hk]
    assert phk == mul12[ph][pk]
    assert va(mv(J, coc48[h][k]), mhk) == va(mh, mv(actions12[ph], mk), coc12[ph][pk])
for h, k, l in product(range(48), repeat=3):
    assert va(coc48[h][k], coc48[mul48[h][k]][l]) == va(
        mv(actions48[h], coc48[k][l]), coc48[h][mul48[k][l]])

image2 = {(q, tuple(a % 2 for a in shift)) for q, shift in projection}
assert len(image2) == 48
assert image2 == {(q, (a, b)) for q in range(12) for a, b in product(range(2), repeat=2)}

# Six labelled cusp directions of the q_2 covering.
z = (-2, -1)
peripheral_words = [(1, 1), (2, 1, 1, -2), (2, 2), (1, 2, 2, -1),
                    z+z, (1,)+z+z+(-1,)]
peripheral = [schreier(w) for w in peripheral_words]
assert va(*peripheral) == (0,)*5


def determinant(a):
    a = [[Fraction(x) for x in row] for row in a]
    result = Fraction(1)
    for i in range(len(a)):
        k = next(k for k in range(i, len(a)) if a[k][i])
        if k != i:
            a[k], a[i] = a[i], a[k]
            result = -result
        pivot = a[i][i]
        result *= pivot
        for k in range(i+1, len(a)):
            scale = a[k][i]/pivot
            a[k] = [x-scale*y for x, y in zip(a[k], a[i])]
    return int(result)


peripheral_minors = [determinant(transpose(peripheral[:i]+peripheral[i+1:])) for i in range(6)]
assert all(abs(d) == 1 for d in peripheral_minors)
permutations = []
for a in actions48:
    permutations.append([peripheral.index(mv(a, v)) for v in peripheral])
assert {g[0] for g in permutations} == set(range(6))


def rank2(rows):
    pivots = {}
    for row in rows:
        v = sum((x & 1) << i for i, x in enumerate(row))
        while v:
            p = v.bit_length()-1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)


def rref2(rows):
    a = [[x & 1 for x in row] for row in rows]
    i = 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(i, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        for k in range(len(a)):
            if k != i and a[k][j]:
                a[k] = [x ^ y for x, y in zip(a[k], a[i])]
        i += 1
    return a[:i]


def sum_matrix(a, b):
    return tuple(va(x, y) for x, y in zip(a, b))


zeroJ = tuple((0,)*10 for _ in range(5))
gr = tuple(tuple(int(j == i) for j in range(10)) for i in range(5))
gs = tuple(tuple(int(j == i+5) for j in range(10)) for i in range(5))
Jcoc = []
for h in keys48:
    a, d = I5, zeroJ
    for g in reps48[h]:
        d = sum_matrix(d, mm(a, gr if g == 1 else gs))
        a = mm(a, AR if g == 1 else AS)
    Jcoc.append(d)
ri, si = idx48[mod4(rho)], idx48[mod4(sigma)]
cocycle_rows = []
for h in range(48):
    for gi, dg in ((ri, gr), (si, gs)):
        lhs = sum_matrix(Jcoc[h], mm(actions48[h], dg))
        rhs = Jcoc[mul48[h][gi]]
        cocycle_rows.extend(tuple(x-y for x, y in zip(a, b)) for a, b in zip(lhs, rhs))
z1_dim = 10-rank2(cocycle_rows)
cocycle_rref = rref2(cocycle_rows)
assert len(cocycle_rref) == 4
invariant_rows = [tuple(a-b for a, b in zip(r, e))
                  for a in (AR, AS) for r, e in zip(a, I5)]
invariant_dim = 5-rank2(invariant_rows)

# A norm-annihilating functional witnesses that scalar lambda must equal 1.
AX = transpose(tuple(schreier((1,)+w+(-1,)) for w in kbasis))
kx = schreier((1, 1))
norm = sum_matrix(I5, AX)
functional = next(l for l in product(range(2), repeat=5)
                  if all(sum(l[i]*norm[i][j] for i in range(5)) % 2 == 0 for j in range(5))
                  and sum(x*y for x, y in zip(l, kx)) % 2 == 1)
xi48 = idx48[mod4(xmat)]
assert sum(x*y for x, y in zip(functional, coc48[xi48][xi48])) % 2 == 1

# Exact commutant and the line-preserving subspace (linear equations over F_2).
commutant_rows = []
for a in (AR, AS):
    for i, j in product(range(5), repeat=2):
        row = [0]*25
        for k in range(5):
            row[5*i+k] += a[k][j]
            row[5*k+j] -= a[i][k]
        commutant_rows.append(row)
commutant_dim = 25-rank2(commutant_rows)
line_rows = []
for p in peripheral:
    for i in range(5):
        for j in range(i+1, 5):
            row = [0]*25
            for k in range(5):
                row[5*i+k] += p[j]*p[k]
                row[5*j+k] -= p[i]*p[k]
            line_rows.append(row)
line_dim = 25-rank2(line_rows)
assert line_dim == 1

# Dual numbers use bit 0 for the scalar and bit 1 for epsilon.
def da(x, y):
    return x ^ y


def dm(x, y):
    return ((x & 1)*(y & 1)) ^ ((((x & 1)*((y >> 1) & 1)) ^
                               (((x >> 1) & 1)*(y & 1))) << 1)


def dmv(a, v):
    return tuple(reduce(da, (dm(z % 2, w) for z, w in zip(row, v)), 0)
                 for row in a)


counts = {"fine_parameter_points": 0, "liftable_parameter_points": 0}
image_counts, lift_image = {}, set()
for nu2, nu3, a, b, k in product(range(2), range(2), range(4), range(4), range(4)):
    # E.24's integral coordinates specialize: a1=nu2+nu3, beta0=a+a1+b.
    a1 = nu2 ^ nu3
    alpha = (a, a1)
    beta = (a ^ a1 ^ b, b)
    ar = dmv(((1, 1), (-1, 2)), alpha)
    bs = dmv(((1, -1), (-1, 1)), beta)
    xi = (ar[0], ar[1] ^ nu3)
    assert xi == (bs[0], bs[1] ^ nu2)
    t = bs[0]
    key = (t, nu2)
    image_counts[key] = image_counts.get(key, 0)+1
    counts["fine_parameter_points"] += 1
    if dm(t, t) == t:
        counts["liftable_parameter_points"] += 1
        lift_image.add(key)
assert counts == {"fine_parameter_points": 256, "liftable_parameter_points": 128}
assert len(image_counts) == 8 and set(image_counts.values()) == {32} and len(lift_image) == 4
assert dm(2, 2) == 0 and da(dm(2, 2), 2) == 2

# Polynomial, not just A-point, checks for the invisible Frobenius direction.
# Monomials have exponents (epsilon,x,y); epsilon^2=0.
def pa(*ps):
    ans = set()
    for p in ps:
        ans.symmetric_difference_update(p)
    return ans


def pm(p, q):
    ans = set()
    for a in p:
        for b in q:
            c = tuple(x+y for x, y in zip(a, b))
            if c[0] < 2:
                ans.symmetric_difference_update({c})
    return ans


pe, px, py, po = {(1, 0, 0)}, {(0, 1, 0)}, {(0, 0, 1)}, {(0, 0, 0)}


def frob_aut(p):
    return pa(p, pm(pe, pa(pm(p, p), p)))


assert frob_aut(pa(px, py)) == pa(frob_aut(px), frob_aut(py))
assert frob_aut(frob_aut(px)) == px
assert frob_aut(po) == po and frob_aut(set()) == set()
assert (1, 2, 0) in frob_aut(px)

result = {
    "status": "Proved",
    "input": "C=SL2(Z); Pi0=<x,y> index12; K=ker(Pi0->(C2)^2)=Gamma(4)",
    "quotient_orders": {"C/Pi0": 12, "C/K": 48, "Pi0/K": 4},
    "schreier_basis_words": kbasis,
    "projection_matrix_Kab_to_Pi0ab": J,
    "projection_smith_nonzero_entries": [2, 2],
    "projection_mod2_rank": 0,
    "actions_Kab": {"rho": AR, "sigma": AS, "tau": AT, "x": AX},
    "peripheral_words": peripheral_words,
    "peripheral_vectors": peripheral,
    "peripheral_five_by_five_minors": peripheral_minors,
    "integral_cocycle_associativity_checks": 48**3,
    "integral_projection_checks": 48**2,
    "characteristic2_image_order": len(image2),
    "characteristic2_image_equations_on_each_component": ["X^2-X", "Y^2-Y"],
    "dual_number_counterexample": {
        "ring": "F2[epsilon]/epsilon^2", "alpha": ["epsilon", "0"],
        "beta": ["epsilon", "0"], "nu": 0, "nu_prime": 0,
        "nu2": 0, "nu3": 0, "mu": 1,
        "rho_translation": ["epsilon", "epsilon"],
        "violated_image_equation_value": "epsilon != 0"
    },
    "fine_parameter_counts": counts,
    "minimal_automorphism_image_size": len(image_counts),
    "fine_parameter_fiber_cardinality": 32,
    "liftable_minimal_automorphisms": sorted(lift_image),
    "mod2_module_computations": {
        "centralizer_End_H_Kab_dimension": commutant_dim,
        "all_six_lines_preserving_End_dimension": line_dim,
        "invariants_dimension": invariant_dim,
        "Z1_H_Kab_dimension": z1_dim,
        "Z1_constraints_rref_on_d_rho_d_sigma": cocycle_rref,
        "H1_H_Kab_dimension": z1_dim-(5-invariant_dim),
        "norm_annihilator": functional,
        "norm_annihilator_on_x_squared": 1,
        "degree2_invisible_peripheral_tangent_dimension": 1,
        "degree2_full_peripheral_lift_kernel_tangent_dimension": z1_dim+1
    },
    "frobenius_counterexample": "Phi(v,h)=(v+epsilon*(v^[2]-v),h)",
    "frobenius_polynomial_checks": ["additivity", "inverse", "fixes 0 and 1", "nonzero epsilon*x^2 coefficient"],
    "kernel_formula": "T(v)=f(v) coordinatewise, f additive polynomial automorphism, f(1)=1; b in Z1(H48,Kab tensor R)",
    "scope": "Integral finite stage and labelled boundary vector subgroups; no assertion that the entire Section49 profinite signed functor equals the minimal Section51 functor"
}
(OUT/'g_signed_fermat2.json').write_text(json.dumps(result, indent=2)+'\n')
model = {"rank": 5, "basis_words": kbasis, "representatives": [reps48[h] for h in keys48],
         "quotient_matrices_mod4": keys48, "multiplication": mul48, "actions": actions48,
         "cocycle": coc48, "projection": projection, "projection_linear": J,
         "minimal_representatives": [reps12[h] for h in keys12],
         "minimal_actions": actions12, "minimal_multiplication": mul12,
         "minimal_cocycle": coc12, "peripheral_vectors": peripheral,
         "peripheral_permutations": permutations, "cocycle_linear_constraints_mod2": cocycle_rows}
(OUT/'g_signed_fermat2_model.json').write_text(json.dumps(model, separators=(',', ':'))+'\n')
print(json.dumps(result, indent=2))
