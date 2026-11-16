"""Audit cusp-conjugator freedom omitted by normalized peripheral tests.

Independently computes the full centralizer of the cusp tau in F/D9(F)
and its next-layer defects.  This distinguishes tau -> tau^lambda from
tau -> v tau^lambda v^-1 with v centralizing tau only in the lower base.
"""
from functools import lru_cache
from itertools import product
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
B = json.loads((ROOT / "work/c_obstruction_replay/d_cm_solvable_even_boundary.json").read_text())
old = json.loads((OUT / "c_replay_d_cm_rank2_degree9.json").read_text())["certificates"][0]
sc = json.loads((OUT / "c_replay_d_cm_rank2_centralizers.json").read_text())["certificates"][0]
DEG = 9
ONE = (1,) + (0,) * DEG


def tensor(a, b, d):
    answer = 0
    while b:
        bit = b & -b
        b ^= bit
        answer ^= a << ((bit.bit_length() - 1) << d)
    return answer


def mul(a, b):
    result = [a[0] & b[0]] + [(b[d] if a[0] else 0) ^ (a[d] if b[0] else 0)
                              for d in range(1, DEG + 1)]
    for d in range(2, DEG + 1):
        for k in range(1, d):
            result[d] ^= tensor(a[k], b[d-k], k)
    return tuple(result)


def inverse(a):
    result = [1] + [0] * DEG
    for d in range(1, DEG + 1):
        result[d] = a[d]
        for k in range(1, d):
            result[d] ^= tensor(a[k], result[d-k], k)
    return tuple(result)


def free_reduce(word):
    answer = []
    for a in word:
        if answer and answer[-1] == -a:
            answer.pop()
        else:
            answer.append(a)
    return tuple(answer)


def free_inverse(word):
    return tuple(-a for a in reversed(word))


def free_commutator(a, b):
    return free_reduce(a + b + free_inverse(a) + free_inverse(b))


def evaluate(word):
    value = [1] + [0] * DEG
    for letter in word:
        i = abs(letter) - 1
        for d in (range(DEG, 0, -1) if letter > 0 else range(1, DEG + 1)):
            value[d] ^= value[d-1] << (i * (1 << (d-1)))
    return tuple(value)


def lyndon(word):
    return all(word < word[k:] + word[:k] for k in range(1, len(word)))


@lru_cache(None)
def bracket_word(word):
    if len(word) == 1:
        return (word[0] + 1,)
    k = next(k for k in range(1, len(word)) if lyndon(word[k:]))
    return free_commutator(bracket_word(word[:k]), bracket_word(word[k:]))


layers = {}
for n in range(1, 10):
    layer = []
    power = 1
    while n % power == 0:
        for word in product(range(2), repeat=n // power):
            if lyndon(word):
                w = free_reduce(bracket_word(word) * power)
                p = evaluate(w)
                assert not any(p[1:n]) and p[n]
                layer.append((p, w))
        power *= 2
    layers[n] = layer


def echelon(columns, descending=False):
    pivots = {}
    null = []
    order = range(len(columns)-1, -1, -1) if descending else range(len(columns))
    for j in order:
        value, mask = columns[j], 1 << j
        while value:
            p = value.bit_length() - 1
            if p not in pivots:
                pivots[p] = (value, mask)
                break
            v, m = pivots[p]
            value ^= v
            mask ^= m
        if not value:
            null.append(mask)
    if descending:
        null.reverse()

    def reduce(value):
        mask = 0
        for p, (v, m) in sorted(pivots.items(), reverse=True):
            if value >> p & 1:
                value ^= v
                mask ^= m
        return value, mask
    return pivots, reduce, null


def selected(mask, generators):
    value, word = ONE, ()
    while mask:
        bit = mask & -mask
        mask ^= bit
        p, w = generators[bit.bit_length() - 1]
        value, word = mul(value, p), free_reduce(word + w)
    return value, word


G = [tuple(q) for q in B["sphere_quotient_states"]]
index = {q: j for j, q in enumerate(G)}
chords = {j: i for i, j in enumerate(B["sphere_cycle_chords"])}
basis_words = B["sphere_F_basis_B_words"]
perm_mul = lambda a, b: tuple(a[b[i]] for i in range(3))
identity, s, r = (0, 1, 2), (1, 0, 2), (1, 2, 0)
r2 = perm_mul(r, r)


def collapse(word):
    q, answer = identity, []
    for a in word:
        if a == 0:
            q = perm_mul(q, s)
        else:
            nxt = perm_mul(q, r if a == 1 else r2)
            if index[q] in chords:
                answer.append(chords[index[q]] + 1)
            if index[nxt] in chords:
                answer.append(-chords[index[nxt]] - 1)
            q = nxt
    assert q == identity
    return free_reduce(answer)


tau_images = [collapse([0, 1] + w + [2, 0]) for w in basis_words]
X = [tuple([0] + list(evaluate(w)[1:])) for w in tau_images]
monomials = {(): ONE}
for n in range(1, 10):
    for word in product(range(2), repeat=n):
        monomials[word] = mul(monomials[word[:-1]], X[word[-1]])
encoded = {n: [monomials[tuple((j >> k) & 1 for k in range(n))]
               for j in range(1 << n)] for n in range(1, 10)}


def action(p):
    result = [p[0]] + [0] * DEG
    for n in range(1, 10):
        value = p[n]
        while value:
            bit = value & -value
            value ^= bit
            monomial = encoded[n][bit.bit_length() - 1]
            for d in range(n, 10):
                result[d] ^= monomial[d]
    return tuple(result)


def leading_independence(generators, degree):
    by_degree = {}
    for p, word in generators:
        assert evaluate(word) == p
        d = next(d for d in range(1, degree+1) if p[d])
        by_degree.setdefault(d, []).append(p[d])
    for d, values in by_degree.items():
        assert len(echelon(values)[0]) == len(values)
    return {d: len(values) for d, values in by_degree.items()}


centralizer = []
history = []
for n in range(1, 9):
    layer = layers[n]
    columns = [p[n] ^ action(p)[n] for p, word in layer]
    central_pivots, reduce_central, fixed = echelon(columns)
    obstruction = []
    for p, word in centralizer:
        defect = mul(action(p), inverse(p))
        assert not any(defect[1:n])
        obstruction.append(reduce_central(defect[n])[0])
    connecting, reduce_connecting, kernel = echelon(obstruction, descending=True)
    lifted = []
    for mask in kernel:
        p, word = selected(mask, centralizer)
        defect = mul(action(p), inverse(p))
        remainder, correction = reduce_central(defect[n])
        assert remainder == 0
        z, w = selected(correction, layer)
        value, v = mul(z, p), free_reduce(w + word)
        assert not any(mul(action(value), inverse(value))[1:n+1])
        lifted.append((value, v))
    lifted += [selected(mask, layer) for mask in fixed]
    assert len(lifted) == len(centralizer) - len(connecting) + len(fixed)
    independence = leading_independence(lifted, n)
    centralizer = lifted
    history.append({"base": "F/D" + str(n+1),
                    "log2_centralizer_order": len(centralizer),
                    "connecting_rank": len(connecting),
                    "leading_dimensions": independence})

defects = []
for p, word in centralizer:
    defect = mul(action(p), inverse(p))
    assert not any(defect[1:9])
    defects.append(defect[9])
functional = int(sc["annihilating_functional"], 16)
values = [(functional & v).bit_count() % 2 for v in defects]
columns = [int(v, 16) for v in old["correction_columns"]]
columns += [int(v, 16) for v in sc["centralizer_degree9_defects"]]
before = len(echelon(columns)[0])
all_pivots, all_reduce, _ = echelon(columns + defects)
remainder, solution = all_reduce(int(old["target"], 16))
summary = {"centralizer_history": history,
           "complete_cusp_centralizer_log2_order": len(centralizer),
           "Lambda_values_on_cusp_defects": values,
           "normalized_correction_rank": before,
           "rank_with_all_lower_cusp_centralizer_defects": len(all_pivots),
           "same_lower_action_has_conjugate_cusp_lift": remainder == 0,
           "scope": "All s-frame, r-frame (coprime), and cusp-frame changes in the sphere B/D9F -> B/D10F test; multiplier changes preserving the base are invisible here."}

# Produce an actual finite automorphism witness, not just a rank equality.
assert remainder == 0
block = (1 << 56) - 1
beta_mask = solution & block
A_mask = (solution >> 56) & block
s_mask = (solution >> 112) & ((1 << 38) - 1)
tau_mask = solution >> (112 + 38)
beta_central, beta_central_word = selected(beta_mask, layers[9])
A_central, A_central_word = selected(A_mask, layers[9])
s_generators = [(tuple(int(v, 16) for v in p), tuple(w))
                for p, w in zip(sc["centralizer_polynomials"], sc["centralizer_free_words"])]
s_right, s_right_word = selected(s_mask, s_generators)
V, V_word = selected(tau_mask, centralizer)


def substitution_from_words(words):
    XX = [tuple([0] + list(evaluate(w)[1:])) for w in words]
    mons = {(): ONE}
    for n in range(1, 10):
        for word in product(range(2), repeat=n):
            mons[word] = mul(mons[word[:-1]], XX[word[-1]])
    code = {n: [mons[tuple((j >> k) & 1 for k in range(n))]
                for j in range(1 << n)] for n in range(1, 10)}

    def apply(p):
        result = [p[0]] + [0] * DEG
        for n in range(1, 10):
            value = p[n]
            while value:
                bit = value & -value
                value ^= bit
                for d in range(n, 10):
                    result[d] ^= code[n][bit.bit_length() - 1][d]
        return tuple(result)
    return apply


s_images = [collapse([0] + w + [0]) for w in basis_words]
r_images = [collapse([1] + w + [2]) for w in basis_words]
act_s, act_r = substitution_from_words(s_images), substitution_from_words(r_images)
boundary = read_boundary = json.loads((OUT / "c_replay_d_cm_rank2_boundary_test.json").read_text())["graphs"][0]
AA = tuple(int(v, 16) for v in boundary["A_polynomials"][index[identity]])
BB = tuple(int(v, 16) for v in boundary["beta_polynomials"][index[identity]])
new_A = mul(A_central, AA)
new_beta = mul(mul(beta_central, BB), s_right)
# Phi(s) Phi(r) tau^-1 = beta s(beta^-1 A) sr(A^-1).
actual_cusp_error = mul(mul(new_beta, act_s(mul(inverse(new_beta), new_A))),
                        action(inverse(new_A)))
conjugate_cusp_error = mul(V, action(inverse(V)))
assert actual_cusp_error == conjugate_cusp_error
assert actual_cusp_error[:9] == ONE[:9]
assert not any(mul(s_right, inverse(act_s(s_right)))[1:9])
assert evaluate(beta_central_word) == beta_central
assert evaluate(A_central_word) == A_central
assert evaluate(s_right_word) == s_right
assert evaluate(V_word) == V
summary["literal_corrected_conjugator_polynomials_verified"] = True
summary["witness_word_lengths"] = {"beta_left_central": len(beta_central_word),
                                   "A_left_central": len(A_central_word),
                                   "beta_right_lower_centralizer": len(s_right_word),
                                   "cusp_frame": len(V_word)}
summary["same_lower_action_retained"] = True
summary["automorphism_by_identity_Frattini_action"] = True

# Stronger check: solve the complete affine inner-conjugator problem, including
# every lower centralizer of both s and r at each intermediate stage.
targets = (mul(BB, act_s(inverse(BB))), mul(AA, act_r(inverse(AA))))
inner, inner_word = ONE, ()
inner_history = []
joint_centralizer = []
for n in range(1, 9):
    layer = layers[n]
    old_s = mul(inner, act_s(inverse(inner)))
    old_r = mul(inner, act_r(inverse(inner)))
    residual_s = mul(targets[0], inverse(old_s))
    residual_r = mul(targets[1], inverse(old_r))
    assert not any(residual_s[1:n]) and not any(residual_r[1:n])
    layer_columns = [(p[n] ^ act_s(p)[n]) | ((p[n] ^ act_r(p)[n]) << (1 << n))
                     for p, w in layer]
    central_pivots, central_reduce, fixed = echelon(layer_columns)
    previous_defects = []
    for p, word in joint_centralizer:
        ds = mul(p, act_s(inverse(p)))
        dr = mul(p, act_r(inverse(p)))
        assert not any(ds[1:n]) and not any(dr[1:n])
        previous_defects.append(ds[n] | (dr[n] << (1 << n)))
    all_columns = layer_columns + previous_defects
    pivots, reduce, null = echelon(all_columns)
    residual = residual_s[n] | (residual_r[n] << (1 << n))
    rem, correction = reduce(residual)
    inner_history.append({"degree": n, "joint_layer_rank": len(central_pivots),
                          "all_conjugator_change_rank": len(pivots),
                          "previous_joint_centralizer_order_log2": len(joint_centralizer),
                          "some_inner_conjugator_extends": rem == 0})
    if rem:
        break
    z, w = selected(correction & ((1 << len(layer))-1), layer)
    c, cw = selected(correction >> len(layer), joint_centralizer)
    inner, inner_word = mul(mul(z, inner), c), free_reduce(w + inner_word + cw)
    assert not any(mul(targets[0], inverse(mul(inner, act_s(inverse(inner)))))[1:n+1])
    assert not any(mul(targets[1], inverse(mul(inner, act_r(inverse(inner)))))[1:n+1])
    # Recompute the complete homogeneous stabilizer of this affine torsor.
    reduced = [central_reduce(v)[0] for v in previous_defects]
    connecting, _, kernel = echelon(reduced, descending=True)
    lifted = []
    for mask in kernel:
        p, word = selected(mask, joint_centralizer)
        ds, dr = mul(p, act_s(inverse(p))), mul(p, act_r(inverse(p)))
        zero, c_mask = central_reduce(ds[n] | (dr[n] << (1 << n)))
        assert zero == 0
        z, w = selected(c_mask, layer)
        value, v = mul(z, p), free_reduce(w + word)
        assert not any(mul(value, act_s(inverse(value)))[1:n+1])
        assert not any(mul(value, act_r(inverse(value)))[1:n+1])
        lifted.append((value, v))
    lifted += [selected(mask, layer) for mask in fixed]
    assert len(lifted) == len(joint_centralizer) - len(connecting) + len(fixed)
    leading_independence(lifted, n)
    joint_centralizer = lifted
summary["complete_inner_action_test"] = inner_history
summary["recorded_lower_action_is_inner"] = not bool(rem)

certificate = {"summary": summary, "cusp_conjugation_free_generator_images": tau_images,
               "centralizer_free_words": [list(w) for p, w in centralizer],
               "degree9_defects": [hex(v) for v in defects],
               "remaining_target": hex(remainder), "solution_mask": hex(solution),
               "actual_witness_corrections": {
                   "beta_left_central_word": list(beta_central_word),
                   "A_left_central_word": list(A_central_word),
                   "beta_right_lower_s_centralizer_word": list(s_right_word),
                   "cusp_frame_word": list(V_word),
                   "corrected_cusp_error_polynomial": [hex(v) for v in actual_cusp_error],
                   "cusp_frame_conjugation_error_polynomial": [hex(v) for v in conjugate_cusp_error],
                   "inner_word_if_successful": list(inner_word) if not rem else None,
               }}
(OUT / "c_cusp_centralizer_scope.json").write_text(json.dumps(certificate, indent=2) + "\n")
print(json.dumps(summary, indent=2))
