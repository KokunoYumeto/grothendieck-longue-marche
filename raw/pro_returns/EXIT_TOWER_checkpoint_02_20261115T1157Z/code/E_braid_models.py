"""Exact word and finite-matrix checks for the Part E braid constructions.

No packages outside the Python standard library are required.
"""
from math import gcd
import json
from pathlib import Path


def reduce_word(word):
    ans = []
    for x in word:
        if ans and ans[-1] == -x:
            ans.pop()
        else:
            ans.append(x)
    return tuple(ans)


def inverse(word):
    return tuple(-x for x in reversed(word))


def subst(images, word):
    return reduce_word(x for s in word for x in
                       (images[s-1] if s > 0 else inverse(images[-s-1])))


def compose(left, right):
    return tuple(subst(left, w) for w in right)


def power(aut, n):
    ans = tuple((i,) for i in range(1, len(aut)+1))
    for _ in range(n):
        ans = compose(ans, aut)
    return ans


report = {"artin_full_twists": [], "hyperelliptic_abelianizations": [],
          "inner_extension_counterexample_mod_3": {},
          "elliptic_boundary_relations": {}}
for r in (3, 4):
    identity = tuple((i,) for i in range(1, r+1))
    ts = []
    for i in range(1, r):
        images = list(identity)
        images[i-1] = (i, i+1, -i)
        images[i] = (i,)
        ts.append(tuple(images))
    beta = identity
    for t in ts:
        beta = compose(beta, t)
    omega = power(beta, r)
    c = tuple(range(1, r+1))
    expected = tuple(reduce_word(c+(i,)+inverse(c)) for i in range(1, r+1))
    assert omega == expected
    assert all(subst(t, c) == c for t in ts)
    for i in range(r-2):
        assert compose(compose(ts[i],ts[i+1]),ts[i]) == \
               compose(compose(ts[i+1],ts[i]),ts[i+1])
    report["artin_full_twists"].append({"r":r,"images":omega,
                                       "equals_conjugation_by_product":True})

    if r == 4:
        a,b,d=ts
        v=compose(compose(b,power(a,2)),b)
        assert compose(a,v)==compose(v,a)
        assert compose(a,d)==compose(d,a)
        assert power(compose(v,d),2)==power(compose(d,v),2)
        assert omega==compose(power(a,2),power(compose(v,d),2))
        report["elliptic_boundary_relations"].update({
            "a_commutes_with_v_and_d":True,
            "v_d_v_d_equals_d_v_d_v":True,
            "omega_4_equals_a_squared_times_vd_squared":True})

def matrix_multiply(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))

aa=(1,1,0,1)
bb=(1,0,-1,1)
vv=matrix_multiply(matrix_multiply(bb,matrix_multiply(aa,aa)),bb)
assert vv==(-1,2,0,-1)
v_permutation=list(range(4))
for strand in (2,1,1,2):
    v_permutation[strand-1],v_permutation[strand]=v_permutation[strand],v_permutation[strand-1]
assert v_permutation==list(range(4))
report["elliptic_boundary_relations"].update({
    "q_v_matrix":vv,"equals_minus_a_to_minus_two":True,
    "v_permutation":v_permutation,"v_pure_braid":True,
    "v_reverses_oriented_nonseparating_curve":True,
    "v_on_a_homology_mod_3":(vv[0]%3,vv[2]%3)})
assert (vv[0]%3,vv[2]%3)==(2,0)

for g in range(2, 7):
    m = 2*g+2
    actual = (m-1)*gcd(4,m)
    wrong = 2*(2*g+1)*(2*g)
    assert actual != wrong
    report["hyperelliptic_abelianizations"].append(
        {"g":g,"full_hyperelliptic_abelianization_order":actual,
         "B_2g_plus_1_mod_z_squared_abelianization_order":wrong})


def multiply(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % 3
                 for i in range(2) for j in range(2))


ta=(1,1,0,1)
tb=(1,0,2,1)
ta_inv=(1,2,0,1)
conjugate=multiply(multiply(ta,tb),ta_inv)
assert conjugate != tb
report["inner_extension_counterexample_mod_3"]={
    "tau_gamma":ta,"tau_beta":tb,
    "tau_gamma_tau_beta_tau_gamma_inverse":conjugate,
    "distinct":True}

out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
